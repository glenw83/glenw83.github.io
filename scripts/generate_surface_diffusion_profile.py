"""Generate the pinchoff-profile SVG used on the experiments page.

The meridian is the independently regenerated numerical solution of the
certified centre system from *Pinchoff by surface diffusion*.  The final panel
is the rigorously identified singular-time cone, not a post-breakup guess.
"""

from __future__ import annotations

import math
from pathlib import Path

GAMMA = 0.63169185949612983
MU = 0.030292801498271463
ALPHA = 1.037079401503446
STEP = 0.0025

WIDTH = 1160
HEIGHT = 340
PANEL_WIDTH = 270
PANEL_GAP = 16
PANEL_LEFT = 18
MIDLINE_Y = 154.0
X_SCALE = 56.0
R_SCALE = 48.0
Z_MAX = 2.08


def flux_system(zeta: float, state: list[float]) -> tuple[float, float, float, float]:
    """The regular flux formulation for the rotational similarity profile."""

    u, q, curvature, flux = state
    metric = 1.0 + q * q
    return (
        q,
        metric / u - metric**1.5 * curvature,
        math.sqrt(metric) * flux / u,
        -2.0 * MU * u * (u - zeta * q),
    )


def rk4_step(zeta: float, state: list[float], step: float) -> list[float]:
    k1 = flux_system(zeta, state)
    k2_state = [value + step * slope / 2 for value, slope in zip(state, k1, strict=True)]
    k2 = flux_system(zeta + step / 2, k2_state)
    k3_state = [value + step * slope / 2 for value, slope in zip(state, k2, strict=True)]
    k3 = flux_system(zeta + step / 2, k3_state)
    k4_state = [value + step * slope for value, slope in zip(state, k3, strict=True)]
    k4 = flux_system(zeta + step, k4_state)
    return [
        value + step * (s1 + 2 * s2 + 2 * s3 + s4) / 6
        for value, s1, s2, s3, s4 in zip(state, k1, k2, k3, k4, strict=True)
    ]


sample_zeta = [0.0]
sample_u = [1.0]
state = [1.0, 0.0, 1.0 - GAMMA, 0.0]
for index in range(round(20.0 / STEP)):
    zeta = index * STEP
    state = rk4_step(zeta, state, STEP)
    sample_zeta.append((index + 1) * STEP)
    sample_u.append(state[0])


def profile(zeta_values: list[float]) -> list[float]:
    values = []
    for raw_zeta in zeta_values:
        zeta = abs(raw_zeta)
        if zeta > sample_zeta[-1]:
            raise ValueError(f"profile requested beyond certified centre interval: {zeta}")
        position = zeta / STEP
        lower = min(int(position), len(sample_u) - 2)
        fraction = position - lower
        values.append(sample_u[lower] * (1 - fraction) + sample_u[lower + 1] * fraction)
    return values


def points_for_scale(scale: float, panel_index: int, sign: float) -> str:
    z = [-Z_MAX + 2 * Z_MAX * index / 180 for index in range(181)]
    if scale == 0.0:
        radius = [ALPHA * abs(value) for value in z]
    else:
        radius = [scale * value for value in profile([value / scale for value in z])]

    centre_x = PANEL_LEFT + panel_index * (PANEL_WIDTH + PANEL_GAP) + PANEL_WIDTH / 2
    x = [centre_x + X_SCALE * value for value in z]
    y = [MIDLINE_Y - sign * R_SCALE * value for value in radius]
    return " ".join(f"{px:.2f},{py:.2f}" for px, py in zip(x, y, strict=True))


def closed_shape_for_scale(scale: float, panel_index: int) -> str:
    upper = points_for_scale(scale, panel_index, +1.0).split()
    lower = points_for_scale(scale, panel_index, -1.0).split()
    return " ".join(upper + list(reversed(lower)))


stages = [
    (0.54, "earlier", "A/A₀ = 1"),
    (0.28, "later", "A/A₀ = 0.52"),
    (0.11, "near T", "A/A₀ = 0.20"),
    (0.0, "singular time", "A = 0"),
]

parts = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="title desc">',
    "  <title id=\"title\">Numerical meridian profiles approaching conical pinchoff</title>",
    "  <desc id=\"desc\">Three scaled copies of the certified similarity profile narrow toward a final double cone at singular time.</desc>",
    "  <defs>",
    "    <linearGradient id=\"profile-fill\" x1=\"0\" x2=\"0\" y1=\"0\" y2=\"1\">",
    "      <stop offset=\"0\" stop-color=\"#f6d58c\"/>",
    "      <stop offset=\"0.52\" stop-color=\"#c47a33\"/>",
    "      <stop offset=\"1\" stop-color=\"#70431f\"/>",
    "    </linearGradient>",
    "    <marker id=\"arrow\" viewBox=\"0 0 10 10\" refX=\"9\" refY=\"5\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto\">",
    "      <path d=\"M0 0L10 5L0 10Z\" fill=\"#70d8e8\"/>",
    "    </marker>",
    "  </defs>",
    "  <rect width=\"1160\" height=\"340\" rx=\"12\" fill=\"#101e2b\"/>",
]

for index, (scale, label, scale_label) in enumerate(stages):
    left = PANEL_LEFT + index * (PANEL_WIDTH + PANEL_GAP)
    centre_x = left + PANEL_WIDTH / 2
    parts.append(
        f'  <line x1="{left + 15}" y1="{MIDLINE_Y}" x2="{left + PANEL_WIDTH - 15}" y2="{MIDLINE_Y}" '
        'stroke="#45606d" stroke-width="1" stroke-dasharray="4 6"/>'
    )
    parts.append(
        f'  <polygon points="{closed_shape_for_scale(scale, index)}" fill="url(#profile-fill)" '
        'stroke="#ffe4b2" stroke-width="2.2" stroke-linejoin="round"/>'
    )
    if scale == 0.0:
        parts.append(
            f'  <circle cx="{centre_x:.2f}" cy="{MIDLINE_Y}" r="4.5" fill="#70d8e8"/>'
        )
        parts.append(
            f'  <text x="{centre_x:.2f}" y="35" text-anchor="middle" fill="#70d8e8" '
            'font-size="15" font-family="system-ui, sans-serif">conical pinch</text>'
        )
    parts.append(
        f'  <text x="{centre_x:.2f}" y="294" text-anchor="middle" fill="#f3f6f7" '
        f'font-size="18" font-weight="650" font-family="system-ui, sans-serif">{label}</text>'
    )
    parts.append(
        f'  <text x="{centre_x:.2f}" y="318" text-anchor="middle" fill="#a9bbc3" '
        f'font-size="14" font-family="system-ui, sans-serif">{scale_label}</text>'
    )
    if index < len(stages) - 1:
        x1 = left + PANEL_WIDTH - 3
        x2 = left + PANEL_WIDTH + PANEL_GAP - 3
        parts.append(
            f'  <line x1="{x1}" y1="{MIDLINE_Y}" x2="{x2}" y2="{MIDLINE_Y}" '
            'stroke="#70d8e8" stroke-width="2.5" marker-end="url(#arrow)"/>'
        )

parts.extend(
    [
        "  <text x=\"22\" y=\"24\" fill=\"#a9bbc3\" font-size=\"13\" font-family=\"system-ui, sans-serif\">meridian; rotate around the dashed axis</text>",
        "</svg>",
    ]
)

output = Path(__file__).resolve().parents[1] / "assets" / "img" / "surface-diffusion" / "certified-pinchoff-profile.svg"
output.write_text("\n".join(parts) + "\n", encoding="utf-8")
print(output)
