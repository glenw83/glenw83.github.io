"""Directed-rounding Poincare--Miranda certificate for the shrinker.

This program validates signs on the six faces of the affine shooting box

    4.65 <= R <= 4.90,
    M = 1.09154305 + 0.03910820 (R-4.65) + d,  |d| <= 0.0003,
    L = 1.28426000 + 0.74769648 R + 266.65848 d + e,
                                                    |e| <= 0.03.

It uses a self-contained directed-rounding Decimal interval type and integrates
only the seven polynomial state variables

    (r, 1/r, z, cos(alpha), sin(alpha), H, p)

on the normalised time interval [0,1].  Each face is covered by a finite grid
of closed rectangles.  On every rectangle a Picard tube and interval Taylor
remainder enclose all shots in that rectangle.  Thus the output is a direct
finite certificate of the Poincare--Miranda face signs; there is no root
search, sensitivity equation, numerical Jacobian, or Krawczyk operator.

No third-party Python package is required.
"""

from argparse import ArgumentParser
from decimal import (
    Decimal as D, Context, localcontext, ROUND_FLOOR, ROUND_CEILING,
    getcontext,
)
from multiprocessing import Pool
from os import cpu_count
from time import monotonic

getcontext().prec = 80
CTX_LO = Context(prec=80, rounding=ROUND_FLOOR)
CTX_HI = Context(prec=80, rounding=ROUND_CEILING)


def dd(x):
    return x if isinstance(x, D) else D(str(x))


class I:
    """Closed Decimal interval with directed rounding after every operation."""

    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi=None):
        self.lo = dd(lo)
        self.hi = self.lo if hi is None else dd(hi)
        if self.lo > self.hi:
            raise ValueError((self.lo, self.hi))

    @staticmethod
    def hull(a, b):
        a, b = as_i(a), as_i(b)
        return I(min(a.lo, b.lo), max(a.hi, b.hi))

    def __repr__(self):
        return f"[{self.lo},{self.hi}]"

    def mid(self):
        with localcontext() as context:
            context.prec = 80
            return (self.lo+self.hi)/D(2)

    def contains_zero(self):
        return self.lo <= 0 <= self.hi

    def subset_interior(self, other):
        other = as_i(other)
        return other.lo < self.lo and self.hi < other.hi

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __add__(self, other):
        other = as_i(other)
        with localcontext(CTX_LO):
            lo = self.lo+other.lo
        with localcontext(CTX_HI):
            hi = self.hi+other.hi
        return I(lo, hi)

    __radd__ = __add__

    def __sub__(self, other):
        return self+(-as_i(other))

    def __rsub__(self, other):
        return as_i(other)-self

    def __mul__(self, other):
        other = as_i(other)
        with localcontext(CTX_LO):
            products = (self.lo*other.lo, self.lo*other.hi,
                        self.hi*other.lo, self.hi*other.hi)
            lo = min(products)
        with localcontext(CTX_HI):
            products = (self.lo*other.lo, self.lo*other.hi,
                        self.hi*other.lo, self.hi*other.hi)
            hi = max(products)
        return I(lo, hi)

    __rmul__ = __mul__

    def reciprocal(self):
        if self.contains_zero():
            raise ZeroDivisionError(self)
        with localcontext(CTX_LO):
            lo = D(1)/self.hi
        with localcontext(CTX_HI):
            hi = D(1)/self.lo
        return I(lo, hi)

    def __truediv__(self, other):
        return self*as_i(other).reciprocal()

    def __rtruediv__(self, other):
        return as_i(other)/self


def as_i(x):
    return x if isinstance(x, I) else I(x)


ZERO = I(0)
ONE = I(1)
QUARTER = I(D(1)/D(4))


def conv2(a, b, k):
    value = ZERO
    for j in range(k+1):
        value = value+a[j]*b[k-j]
    return value


def conv3(a, b, c, k):
    value = ZERO
    for i in range(k+1):
        for j in range(k-i+1):
            value = value+a[i]*b[j]*c[k-i-j]
    return value


R_LO = D("4.65")
R_HI = D("4.90")
D_LO = D("-0.0003")
D_HI = D("0.0003")
E_LO = D("-0.03")
E_HI = D("0.03")
HALF_PI_LO = D("1.5707963267948966192313216916397514420985846996875529104874722961539082031431044")
HALF_PI_HI = D("1.5707963267948966192313216916397514420985846996875529104874722961539082031431045")


def require(condition, message, exception=RuntimeError):
    """An optimisation-proof proof guard (unlike Python's ``assert``)."""
    if not condition:
        raise exception(message)


def affine_parameters(R, d, e):
    """Return interval (R,M,L) from intervals in the box coordinates."""
    R, d, e = as_i(R), as_i(d), as_i(e)
    M = I("1.09154305") + I("0.03910820")*(R-I("4.65")) + d
    L = I("1.28426000") + I("0.74769648")*R + I("266.65848")*d + e
    return R, M, L


def initial_state(R, d, e):
    R, M, L = affine_parameters(R, d, e)
    return [R, ONE/R, ZERO, ZERO, ONE, M, ZERO], L


class AA:
    """First-order affine form with a rigorous interval remainder.

    An instance represents ``c + sum(a[j]*xi[j]) + rem`` for independent
    ``xi[j]`` in [-1,1].  The three fixed noise symbols are the box coordinates
    R,d,e.  Retaining these symbols prevents the severe wrapping seen in plain
    interval propagation.  Every discarded quadratic term is put into ``rem``.
    """

    __slots__ = ("c", "a", "rem")
    nnoise = 3

    def __init__(self, c, a=None, rem=ZERO):
        self.c = as_i(c)
        self.a = tuple(as_i(v) for v in (a if a is not None else [ZERO]*self.nnoise))
        self.rem = as_i(rem)

    @staticmethod
    def from_interval(v):
        v = as_i(v)
        m = v.mid()
        return AA(I(m), rem=v-I(m))

    @staticmethod
    def input(v, index):
        v = as_i(v)
        m = v.mid()
        with localcontext(CTX_HI):
            rad = max(m-v.lo, v.hi-m)
        a = [ZERO]*AA.nnoise
        a[index] = I(rad)
        return AA(I(m), a)

    def interval(self):
        ans = self.c+self.rem
        unit = I(-1, 1)
        for coefficient in self.a:
            ans = ans+coefficient*unit
        return ans

    def is_constant(self):
        return (all(v.lo == 0 and v.hi == 0 for v in self.a)
                and self.rem.lo == 0 and self.rem.hi == 0)

    def __neg__(self):
        return AA(-self.c, [-v for v in self.a], -self.rem)

    def __add__(self, other):
        other = as_aa(other)
        return AA(self.c+other.c,
                  [self.a[j]+other.a[j] for j in range(self.nnoise)],
                  self.rem+other.rem)

    __radd__ = __add__

    def __sub__(self, other):
        return self+(-as_aa(other))

    def __rsub__(self, other):
        return as_aa(other)-self

    def __mul__(self, other):
        other = as_aa(other)
        if self.is_constant():
            return AA(self.c*other.c,
                      [self.c*v for v in other.a], self.c*other.rem)
        if other.is_constant():
            return AA(self.c*other.c,
                      [other.c*v for v in self.a], other.c*self.rem)

        centre = self.c*other.c
        linear = [self.c*other.a[j]+other.c*self.a[j]
                  for j in range(self.nnoise)]
        # Exact quadratic decomposition, with xi_i^2 in [0,1] and
        # xi_i xi_j in [-1,1] for i != j.
        nonlinear = ZERO
        for i in range(self.nnoise):
            nonlinear = nonlinear+self.a[i]*other.a[i]*I(0, 1)
            for j in range(i+1, self.nnoise):
                coefficient = self.a[i]*other.a[j]+self.a[j]*other.a[i]
                nonlinear = nonlinear+coefficient*I(-1, 1)

        lin_self = self.c
        lin_other = other.c
        for j in range(self.nnoise):
            lin_self = lin_self+self.a[j]*I(-1, 1)
            lin_other = lin_other+other.a[j]*I(-1, 1)
        remainder = (nonlinear + lin_self*other.rem
                     + lin_other*self.rem + self.rem*other.rem)
        return AA(centre, linear, remainder)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = as_aa(other)
        if not all(v.lo == 0 and v.hi == 0 for v in other.a):
            raise NotImplementedError("only division by a constant affine form")
        denominator = other.interval()
        return AA(self.c/denominator, [v/denominator for v in self.a],
                  self.rem/denominator)

    def __rtruediv__(self, other):
        raise NotImplementedError


def as_aa(x):
    if isinstance(x, AA):
        return x
    if isinstance(x, I):
        return AA.from_interval(x)
    return AA(I(x))


def reciprocal_input_positive(x):
    """Affine reciprocal of a positive, exactly affine input.

    Uses the exact identity
      1/(m+v) = 1/m - v/m^2 + v^2/(m^2(m+v)).
    The last term is bounded as an interval remainder.
    """
    require(isinstance(x, AA) and x.rem.lo == 0 and x.rem.hi == 0,
            "reciprocal input must be exactly affine", ValueError)
    require(x.c.lo == x.c.hi, "reciprocal centre must be a point", ValueError)
    m = x.c
    v = x-AA(m)
    vrange = v.interval()
    require((m+vrange).lo > 0, "reciprocal input is not positive", ValueError)
    mag = max(abs(vrange.lo), abs(vrange.hi))
    with localcontext(CTX_HI):
        mag_squared = mag*mag
    rem = I(0, mag_squared)/(m*m*(m+vrange))
    ans = AA(ONE/m)-v/(m*m)
    return AA(ans.c, ans.a, ans.rem+rem)


def affine_initial_state(R, d, e):
    Ra = AA.input(R, 0)
    da = AA.input(d, 1)
    ea = AA.input(e, 2)
    M = AA(I("1.09154305")) + AA(I("0.03910820"))*(Ra-AA(I("4.65"))) + da
    L = (AA(I("1.28426000")) + AA(I("0.74769648"))*Ra
         + AA(I("266.65848"))*da + ea)
    w = reciprocal_input_positive(Ra)
    return [Ra, w, AA(0), AA(0), AA(1), M, AA(0)], L


def rhs_state(x, ell):
    r, w, z, c, s, H, p = x
    a = 2*H-s*w
    return [
        ell*c,
        -ell*c*w*w,
        ell*s,
        -ell*s*a,
        ell*c*a,
        ell*p*w,
        -ell*QUARTER*(r*r*s-r*z*c),
    ]


def picard_tube(x0, ell, h, max_iter=30):
    """Validated tube for all initial points in interval vector ``x0``."""
    time = I(0, h)
    B = list(x0)
    factor = D("1.10")
    eps = D("1e-60")
    for _ in range(max_iter):
        C = [x0[i] + time*f for i, f in enumerate(rhs_state(B, ell))]
        if all(C[i].subset_interior(B[i]) for i in range(7)):
            return B
        newB = []
        for i in range(7):
            hull = I.hull(x0[i], C[i])
            with localcontext(CTX_HI):
                left = max(D(0), x0[i].lo-hull.lo)*factor+eps
                right = max(D(0), hull.hi-x0[i].hi)*factor+eps
            with localcontext(CTX_LO):
                lo = x0[i].lo-left
            with localcontext(CTX_HI):
                hi = x0[i].hi+right
            newB.append(I(lo, hi))
        B = newB
    raise RuntimeError("Picard tube failed")


def rhs_coeff_state(y, ell, k):
    """Coefficient k of the seven-dimensional polynomial vector field."""
    r, w, z, c, s, H, p = y
    sw = [conv2(s, w, m) for m in range(k+1)]
    a = [2*H[m]-sw[m] for m in range(k+1)]
    f = [
        c[k],
        -conv3(c, w, w, k),
        s[k],
        -conv2(s, a, k),
        conv2(c, a, k),
        conv2(p, w, k),
        -QUARTER*(conv3(r, r, s, k)-conv3(r, z, c, k)),
    ]
    return [ell*v for v in f]


def conv2_model(a, b, k):
    v = a[0]*b[k]
    for j in range(1, k+1):
        v = v+a[j]*b[k-j]
    return v


def conv3_model(a, b, c, k):
    v = None
    for i in range(k+1):
        for j in range(k-i+1):
            term = a[i]*b[j]*c[k-i-j]
            v = term if v is None else v+term
    return v


def rhs_coeff_model(y, ell, k):
    """Coefficient recurrence over affine forms (or intervals)."""
    r, w, z, c, s, H, p = y
    sw = [conv2_model(s, w, m) for m in range(k+1)]
    a = [2*H[m]-sw[m] for m in range(k+1)]
    f = [
        c[k],
        -conv3_model(c, w, w, k),
        s[k],
        -conv2_model(s, a, k),
        conv2_model(c, a, k),
        conv2_model(p, w, k),
        -(conv3_model(r, r, s, k)-conv3_model(r, z, c, k))*QUARTER,
    ]
    return [ell*v for v in f]


def jets_model(x0, ell, order):
    z = x0[0]-x0[0]
    y = [[v]+[z]*order for v in x0]
    for k in range(order):
        fc = rhs_coeff_model(y, ell, k)
        for i in range(7):
            y[i][k+1] = fc[i]/I(k+1)
    return y


def jets_state(x0, ell, order):
    y = [[v]+[ZERO]*order for v in x0]
    for k in range(order):
        fc = rhs_coeff_state(y, ell, k)
        for i in range(7):
            y[i][k+1] = fc[i]/I(k+1)
    return y


def taylor_step(x0, ell, h, order, return_tube=False):
    B = picard_tube(x0, ell, h)
    cs = jets_state(x0, ell, order-1)
    rem = jets_state(B, ell, order)
    powers = [I(1)]
    for _ in range(order):
        powers.append(powers[-1]*I(h))
    out = []
    for i in range(7):
        v = ZERO
        for k in range(order):
            v = v+cs[i][k]*powers[k]
        out.append(v+rem[i][order]*powers[order])
    return (out, B) if return_tube else out


def exact_decimal_unit_step(steps):
    """Return 1/steps, requiring a terminating decimal expansion."""
    require(isinstance(steps, int) and steps > 0,
            "step count must be a positive integer", ValueError)
    reduced = steps
    for prime in (2, 5):
        while reduced % prime == 0:
            reduced //= prime
    require(reduced == 1, "step count may have no prime factors except 2 and 5",
            ValueError)
    h = D(1)/D(steps)
    require(D(steps)*h == D(1), "Decimal step does not sum exactly to one")
    return h


def integrate_box(R, d, e, steps=80, order=12, record_tubes=False):
    require(isinstance(order, int) and order >= 2,
            "Taylor order must be an integer at least two", ValueError)
    x, ell = initial_state(R, d, e)
    h = exact_decimal_unit_step(steps)
    rlo = x[0].lo
    slo = x[4].lo
    tubes = []
    for _ in range(steps):
        x, B = taylor_step(x, ell, h, order, return_tube=True)
        rlo = min(rlo, B[0].lo)
        slo = min(slo, B[4].lo)
        if record_tubes:
            tubes.append(B)
    return x, rlo, slo, tubes


def affine_taylor_step(x0, ell, h, order, return_tube=False):
    x0_box = [v.interval() for v in x0]
    ell_box = ell.interval()
    B = picard_tube(x0_box, ell_box, h)
    cs = jets_model(x0, ell, order-1)
    rem = jets_state(B, ell_box, order)
    powers = [I(1)]
    for _ in range(order):
        powers.append(powers[-1]*I(h))
    out = []
    for i in range(7):
        v = AA(0)
        for k in range(order):
            v = v+cs[i][k]*powers[k]
        v = v+rem[i][order]*powers[order]
        out.append(v)
    return (out, B) if return_tube else out


def integrate_box_affine(R, d, e, steps=80, order=12, record_tubes=False):
    require(isinstance(order, int) and order >= 2,
            "Taylor order must be an integer at least two", ValueError)
    x, ell = affine_initial_state(R, d, e)
    h = exact_decimal_unit_step(steps)
    rlo = x[0].interval().lo
    slo = x[4].interval().lo
    tubes = []
    for _ in range(steps):
        x, B = affine_taylor_step(x, ell, h, order, return_tube=True)
        rlo = min(rlo, B[0].lo)
        slo = min(slo, B[4].lo)
        if record_tubes:
            tubes.append(B)
    return [v.interval() for v in x], rlo, slo, tubes


def split_interval(lo, hi, n):
    require(isinstance(n, int) and n > 0,
            "subdivision count must be a positive integer", ValueError)
    lo, hi = D(lo), D(hi)
    # The internal decimal breakpoints may round, but using the very same
    # breakpoint as the right and left endpoint of adjacent cells leaves no
    # gap.  The two outer endpoints are installed exactly.
    points = [lo]
    for j in range(1, n):
        points.append(lo+(hi-lo)*D(j)/D(n))
    points.append(hi)
    require(all(points[j] < points[j+1] for j in range(n)),
            "partition points are not strictly increasing")
    cells = [I(points[j], points[j+1]) for j in range(n)]
    require(cells[0].lo == lo and cells[-1].hi == hi,
            "partition does not contain both outer endpoints")
    require(all(cells[j].hi == cells[j+1].lo for j in range(n-1)),
            "partition has a gap")
    return cells


FACES = {
    "Rlo": ("R", I(R_LO), "z", 2, -1),
    "Rhi": ("R", I(R_HI), "z", 2, +1),
    "dlo": ("d", I(D_LO), "p", 6, -1),
    "dhi": ("d", I(D_HI), "p", 6, +1),
    # cos(pi/2+beta) has the opposite sign to beta while sin(alpha)>0.
    "elo": ("e", I(E_LO), "c", 3, -1),
    "ehi": ("e", I(E_HI), "c", 3, +1),
}


def face_cells(name, n1, n2):
    fixed, value, _, _, _ = FACES[name]
    ranges = {
        "R": split_interval(R_LO, R_HI, n1 if fixed != "R" else n2),
        "d": split_interval(D_LO, D_HI, n1 if fixed == "R" else n2),
        "e": split_interval(E_LO, E_HI, n2 if fixed != "e" else n1),
    }
    # Give each face an explicit, predictable ordering of its two free axes.
    if fixed == "R":
        axes = (ranges["d"], ranges["e"])
        return [(value, a, b) for a in axes[0] for b in axes[1]]
    if fixed == "d":
        axes = (ranges["R"], ranges["e"])
        return [(a, value, b) for a in axes[0] for b in axes[1]]
    axes = (ranges["R"], ranges["d"])
    return [(a, b, value) for a in axes[0] for b in axes[1]]


def hull_all(values):
    ans = values[0]
    for v in values[1:]:
        ans = I.hull(ans, v)
    return ans


def box_cells(nR, nd, ne):
    return [(R, d, e)
            for R in split_interval(R_LO, R_HI, nR)
            for d in split_interval(D_LO, D_HI, nd)
            for e in split_interval(E_LO, E_HI, ne)]


def _tube_hull(tubes, first, last, component):
    """Hull component on tubes first,...,last-1."""
    return hull_all([tubes[j][component] for j in range(first, last)])


def _geometry_worker(args):
    R, d, e, steps, order = args
    if steps % 100:
        raise ValueError("geometry steps must be divisible by 100")
    _, _, _, tubes = integrate_box_affine(
        R, d, e, steps=steps, order=order, record_tubes=True)
    unit = steps//100
    A = [2*B[5]-B[4]*B[1] for B in tubes]
    return {
        "r_all": _tube_hull(tubes, 0, steps, 0),
        # The end strips use c_t=-qA together with c(0)=c(1)=0;
        # keeping c itself away from the endpoints sharply improves enclosure.
        "q_early": _tube_hull(tubes, 0, 5*unit, 4),
        "A_early": hull_all(A[0:5*unit]),
        "c_middle": _tube_hull(tubes, 5*unit, 95*unit, 3),
        "z_positive": _tube_hull(tubes, 2*unit, 35*unit, 2),
        "q_cross": _tube_hull(tubes, 35*unit, 47*unit, 4),
        "z_negative": _tube_hull(tubes, 47*unit, 90*unit, 2),
        "q_late": _tube_hull(tubes, 90*unit, steps, 4),
        "A_late": hull_all(A[95*unit:steps]),
    }


def certify_geometry(nR, nd, ne, steps, order, jobs=1):
    """Certify the one-crossing geometry conditionally on an endpoint zero."""
    cells = box_cells(nR, nd, ne)
    tasks = [(R, d, e, steps, order) for R, d, e in cells]
    start = monotonic()
    if jobs > 1:
        with Pool(jobs) as pool:
            outputs = pool.map(_geometry_worker, tasks)
    else:
        outputs = map(_geometry_worker, tasks)
    combined = None
    for j, result in enumerate(outputs):
        if combined is None:
            combined = result
        else:
            combined = {key: I.hull(combined[key], result[key]) for key in combined}
        checks = (
            result["r_all"].lo > 0,
            result["q_early"].lo > 0,
            result["A_early"].lo > 0,
            result["c_middle"].hi < 0,
            result["z_positive"].lo > 0,
            result["q_cross"].hi < 0,
            result["z_negative"].hi < 0,
            result["q_late"].lo > 0,
            result["A_late"].hi < 0,
        )
        if not all(checks):
            R, d, e = cells[j]
            failed = [key for key, ok in zip(result, checks) if not ok]
            raise AssertionError(
                f"geometry failed on cell {j}, R={R}, d={d}, e={e}; "
                f"failed={failed}; bounds={result}"
            )
    elapsed = monotonic()-start
    print({"geometry_cells": len(cells), "bounds": combined, "seconds": elapsed})
    print("whole-box conditional geometry checks passed")
    return combined


def _integrate_worker(args):
    R, d, e, steps, order = args
    x, rlo, _, _ = integrate_box_affine(R, d, e, steps=steps, order=order)
    return x, rlo


def certify_face(name, n1, n2, steps, order, progress=0, jobs=1):
    fixed, _, component, index, sign = FACES[name]
    cells = face_cells(name, n1, n2)
    endpoint = []
    r_lowers = []
    s_endpoints = []
    start = monotonic()
    tasks = [(R, d, e, steps, order) for R, d, e in cells]
    if jobs > 1:
        with Pool(jobs) as pool:
            outputs = pool.map(_integrate_worker, tasks)
    else:
        outputs = map(_integrate_worker, tasks)
    for j, ((R, d, e), (x, rlo)) in enumerate(zip(cells, outputs)):
        value = x[index]
        endpoint.append(value)
        r_lowers.append(rlo)
        s_endpoints.append(x[4])
        if sign*value.lo <= 0 if sign > 0 else sign*value.hi <= 0:
            raise AssertionError(
                f"{name} sign failed on cell {j}: R={R}, d={d}, e={e}, "
                f"{component}={value}"
            )
        if rlo <= 0:
            raise AssertionError(f"{name} radius failed on cell {j}: {rlo}")
        if x[4].lo <= 0:
            raise AssertionError(f"{name} endpoint sin(alpha) failed on cell {j}: {x[4]}")
        if progress and (j+1) % progress == 0:
            print(name, j+1, "/", len(cells), "elapsed", f"{monotonic()-start:.1f}s")
    return {
        "name": name,
        "fixed": fixed,
        "cells": len(cells),
        "component": component,
        "range": hull_all(endpoint),
        "radius_lower": min(r_lowers),
        "endpoint_sine": hull_all(s_endpoints),
        "seconds": monotonic()-start,
    }


def bisect_interval(value):
    value = as_i(value)
    if value.lo == value.hi:
        return [value]
    midpoint = value.mid()
    pieces = [I(value.lo, midpoint), I(midpoint, value.hi)]
    require(pieces[0].lo == value.lo and pieces[-1].hi == value.hi,
            "bisection lost an outer endpoint")
    require(pieces[0].hi == pieces[1].lo, "bisection has a gap")
    return pieces


def split_face_cell(name, cell):
    fixed = FACES[name][0]
    R, d, e = cell
    if fixed == "R":
        return [(R, dd, ee) for dd in bisect_interval(d) for ee in bisect_interval(e)]
    if fixed == "d":
        return [(RR, d, ee) for RR in bisect_interval(R) for ee in bisect_interval(e)]
    return [(RR, dd, e) for RR in bisect_interval(R) for dd in bisect_interval(d)]


def certify_face_adaptive(name, n1, n2, steps, order, max_depth=4, jobs=1):
    """Certify a face by a base grid followed by rigorous quadtree refinement."""
    require(isinstance(max_depth, int) and max_depth >= 0,
            "maximum refinement depth must be a nonnegative integer", ValueError)
    _, _, component, index, sign = FACES[name]
    pending = [(cell, 0) for cell in face_cells(name, n1, n2)]
    certified_values = []
    certified_r = []
    certified_s = []
    integrated_by_depth = [0]*(max_depth+1)
    leaves_by_depth = [0]*(max_depth+1)
    start = monotonic()
    while pending:
        tasks = [(R, d, e, steps, order) for (R, d, e), _ in pending]
        if jobs > 1:
            with Pool(jobs) as pool:
                outputs = pool.map(_integrate_worker, tasks)
        else:
            outputs = map(_integrate_worker, tasks)
        next_pending = []
        for (cell, depth), (x, rlo) in zip(pending, outputs):
            integrated_by_depth[depth] += 1
            value = x[index]
            sign_ok = value.lo > 0 if sign > 0 else value.hi < 0
            other_ok = rlo > 0 and x[4].lo > 0
            if sign_ok and other_ok:
                leaves_by_depth[depth] += 1
                certified_values.append(value)
                certified_r.append(rlo)
                certified_s.append(x[4])
            else:
                if depth == max_depth:
                    raise AssertionError(
                        f"{name} adaptive certificate exhausted at {cell}: "
                        f"{component}={value}, rlo={rlo}, sine={x[4]}"
                    )
                next_pending.extend((child, depth+1)
                                    for child in split_face_cell(name, cell))
        pending = next_pending
        if pending:
            print(name, "refining", len(pending), "cells to depth",
                  pending[0][1], "elapsed", f"{monotonic()-start:.1f}s")
    result = {
        "name": name,
        "base_grid": (n1, n2),
        "max_depth": max(i for i, n in enumerate(leaves_by_depth) if n),
        "integrated_by_depth": integrated_by_depth,
        "leaves_by_depth": leaves_by_depth,
        "certified_leaves": len(certified_values),
        "component": component,
        "range": hull_all(certified_values),
        "radius_lower": min(certified_r),
        "endpoint_sine": hull_all(certified_s),
        "seconds": monotonic()-start,
    }
    print(result)
    return result


def main():
    parser = ArgumentParser()
    parser.add_argument("--faces", nargs="+", choices=sorted(FACES), default=sorted(FACES))
    parser.add_argument("--n1", type=int, default=12)
    parser.add_argument("--n2", type=int, default=12)
    parser.add_argument("--face-steps", type=int, default=40)
    parser.add_argument("--face-order", type=int, default=8)
    parser.add_argument("--geometry-steps", type=int, default=100)
    parser.add_argument("--geometry-order", type=int, default=8)
    parser.add_argument("--progress", type=int, default=0)
    parser.add_argument("--jobs", type=int, default=min(8, cpu_count() or 1))
    parser.add_argument("--faces-only", action="store_true")
    parser.add_argument("--geometry-only", action="store_true")
    parser.add_argument("--nR", type=int, default=7)
    parser.add_argument("--nd", type=int, default=7)
    parser.add_argument("--ne", type=int, default=7)
    parser.add_argument("--uniform", action="store_true")
    parser.add_argument("--max-depth", type=int, default=3)
    args = parser.parse_args()
    require(not (args.faces_only and args.geometry_only),
            "--faces-only and --geometry-only are mutually exclusive", ValueError)
    require(args.jobs > 0, "--jobs must be positive", ValueError)
    require(args.max_depth >= 0, "--max-depth must be nonnegative", ValueError)
    require(args.face_order >= 2 and args.geometry_order >= 2,
            "Taylor orders must be at least two", ValueError)
    print("face grid", args.n1, "x", args.n2, "steps", args.face_steps,
          "order", args.face_order)
    if not args.geometry_only:
        results = []
        for name in args.faces:
            if not args.uniform:
                result = certify_face_adaptive(
                    name, args.n1, args.n2, args.face_steps, args.face_order,
                    args.max_depth, args.jobs)
            else:
                result = certify_face(name, args.n1, args.n2,
                                      args.face_steps, args.face_order,
                                      args.progress, args.jobs)
            results.append(result)
            print(result)
        require(len(results) == len(args.faces), "not every requested face was checked")
        print("all requested face checks passed")
    if not args.faces_only:
        print("geometry grid", args.nR, "x", args.nd, "x", args.ne,
              "steps", args.geometry_steps, "order", args.geometry_order)
        certify_geometry(args.nR, args.nd, args.ne,
                         args.geometry_steps, args.geometry_order, args.jobs)


if __name__ == "__main__":
    main()
