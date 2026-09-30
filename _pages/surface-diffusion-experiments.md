---
layout: page
title: surface diffusion and related phenomena in the lab
description: Experimental observations of surface diffusion, bulk diffusion, and related capillarity-driven motion.
permalink: /surface-diffusion-experiments/
nav: true
nav_order: 2.5
---

<link rel="stylesheet" href="{{ '/assets/css/surface-diffusion-gallery.css' | relative_url }}" />
<link rel="stylesheet" href="{{ '/assets/css/voorhees-curvature.css' | relative_url }}" />
<script src="{{ '/assets/js/voorhees-curvature.js' | relative_url }}" defer></script>

<div class="sd-gallery-page">
  <section class="sd-hero" aria-labelledby="sd-hero-title">
    <div class="sd-hero-copy">
      <p class="sd-eyebrow">Surface diffusion in real life</p>
      <h2 id="sd-hero-title">A solid flowing along its own surface</h2>
      <p class="sd-deck">
        In many physical systems, an evolving solid may change shape without losing volume. Atoms can migrate along its surface, driven by
        differences in curvature. A groove can deepen, a wire can bead up, and a narrow neck can break.
      </p>
      <p>
        These experiments are the physical setting for
        <a href="https://arxiv.org/abs/2608.21882"><em>Pinchoff by surface diffusion</em></a>.
        They show the transport mechanism and its practical consequences. The theorem proves that
        the ideal geometric law itself can carry a smooth closed surface to a one-point conical
        singularity.
      </p>
    </div>

    <figure class="sd-hero-figure">
      <img
        src="{{ '/assets/img/surface-diffusion/certified-pinchoff-profile.svg' | relative_url }}"
        alt="Numerically regenerated meridian profiles narrowing toward a double cone at singular time"
      />
      <figcaption>
        Numerical rendering of meridians $$r=A\,U(z/A)$$ from the certified profile equation. The
        last panel is the singular-time double cone $$r=\alpha|z|$$.
      </figcaption>
    </figure>

  </section>

  <section class="sd-primer" aria-labelledby="sd-mullins-title">
    <div>
      <p class="sd-section-number">01</p>
      <h2 id="sd-mullins-title">The practical question, from Mullins' point of view</h2>
    </div>
    <div class="sd-primer-copy">
      <p>
        Mullins began with a materials problem: how does a hot crystalline surface rearrange when
        atoms are mobile on the surface but the solid as a whole does not flow? Curvature changes
        the surface chemical potential; atoms diffuse along the surface; conservation of mass turns
        that flux into motion of the surface itself.
      </p>

      <figure class="sd-source-figure sd-mullins-figure">
        <div class="sd-source-pair">
          <div>
            <img
              src="{{ '/assets/img/surface-diffusion/mullins-shewmon-copper-groove-1959-fig4.png' | relative_url }}"
              alt="Interference micrographs showing a copper grain-boundary groove after 1, 16, and 81 hours at 930 degrees Celsius"
              loading="lazy"
            />
            <span>Observed groove · Fig. 4</span>
          </div>
          <div>
            <img
              src="{{ '/assets/img/surface-diffusion/mullins-shewmon-fourth-root-1959-fig5.png' | relative_url }}"
              alt="Log-log graph of copper grain-boundary groove width against annealing time with lines of slope one quarter"
              loading="lazy"
            />
            <span>Measured clock · Fig. 5</span>
          </div>
        </div>
        <figcaption>
          Left: the groove after 1, 16, and 81 hours at 930 degrees Celsius. Right: its width follows
          $$w\propto t^{1/4}$$ at both 930 degrees and 1035 degrees. Mullins and Shewmon
          (1959), Figs. 4 and 5.
        </figcaption>
      </figure>

      <p>
        Surface diffusion is a smoothing law,
        but it is not simply a law that makes every shape rounder. The same fourth-order transport
        that broadens a groove can amplify a long-wave disturbance on a thin cylinder until the
        cylinder loses connectivity.
      </p>
      <a class="sd-paper-link sd-paper-link-inline" href="https://doi.org/10.1016/0001-6160(59)90069-0"
        >Mullins and Shewmon, <em>Acta Metallurgica</em> <span aria-hidden="true"> </span></a
      >
    </div>

  </section>

  <section class="sd-gallery-section" aria-labelledby="sd-gallery-title">
    <div class="sd-section-heading">
      <p class="sd-section-number">02</p>
      <div>
        <h2 id="sd-gallery-title">Examples</h2>
        <p>
          Each example below is built around a published figure or an image supplied by a researcher. Experimental and
          simulated panels are identified in the caption.
        </p>
      </div>
    </div>

    <h3 class="sd-chapter"><span>Atoms diffuse</span></h3>
    <div class="sd-card-grid">
      <article class="sd-card sd-card-wide">
        <div class="sd-card-body">
          <p class="sd-card-meta">Silver nanowire · room temperature · 2021</p>
          <h3>Surface steps walk across a crystalline solid</h3>
          <p>
            The atomic lattice remains visible while surface steps migrate along a 6.6 nm silver
            wire under tension. When two steps overlap, a partial dislocation nucleates. The image
            makes the microscopic carrier of surface diffusion visible rather than merely inferred.
          </p>
          <a class="sd-card-citation" href="https://doi.org/10.1038/s41467-021-25542-2"
            >Wang et al. (2021), <em>Nature Communications</em>
            <span aria-hidden="true"></span></a
          >
        </div>
        <figure class="sd-card-visual sd-visual-atomic">
          <img
            class="sd-open-figure"
            src="{{ '/assets/img/surface-diffusion/wang-silver-step-migration-2021-fig2a-l.jpg' | relative_url }}"
            alt="Twelve sequential atomic-resolution TEM frames showing steps migrating along a silver nanowire"
            loading="lazy"
          />
          <figcaption>
            Experimental in-situ HRTEM sequence, cropped to panels a to l from Wang et al. (2021),
            Fig. 2; <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>.
          </figcaption>
        </figure>
        <p class="sd-pinchoff-lens">
          <strong>Why is this important? </strong> Because surface motion can change the mechanical strength of a
          nanoscale component even when the component remains solid.
        </p>
      </article>
    </div>

    <h3 class="sd-chapter"><span>Phase interfaces coarsen</span></h3>
    <div class="sd-card-grid">
      <article class="sd-card sd-card-wide">
        <div class="sd-card-body">
          <p class="sd-card-meta">Ag&ndash;Cu binary alloy · 700 °C · 2008</p>
          <h3>A binary alloy separates isothermally and coarsens</h3>
          <p>
            At a fixed temperature, the fine silver-rich and copper-rich pattern reorganises. Thin
            regions disappear and the typical size of the remaining regions grows between 2 and 40
            hours.
          </p>
          <a class="sd-card-citation" href="https://doi.org/10.1016/j.commatsci.2007.07.034"
            >B&ouml;hme and M&uuml;ller (2008), <em>Computational Materials Science</em>
            <span aria-hidden="true"></span></a
          >
        </div>
        <figure class="sd-card-visual">
          <div class="sd-alloy-sequence">
            <div>
              <img
                src="{{ '/assets/img/surface-diffusion/boehme-muller-agcu-2h.jpg' | relative_url }}"
                alt="Microstructure of a silver-copper binary alloy after two hours at 700 degrees Celsius"
                loading="lazy"
              />
              <span>2 hours</span>
            </div>
            <div>
              <img
                src="{{ '/assets/img/surface-diffusion/boehme-muller-agcu-5h.jpg' | relative_url }}"
                alt="Microstructure of the same silver-copper binary alloy after five hours at 700 degrees Celsius"
                loading="lazy"
              />
              <span>5 hours</span>
            </div>
            <div>
              <img
                src="{{ '/assets/img/surface-diffusion/boehme-muller-agcu-40h.jpg' | relative_url }}"
                alt="Coarsened microstructure of the same silver-copper binary alloy after forty hours at 700 degrees Celsius"
                loading="lazy"
              />
              <span>40 hours</span>
            </div>
          </div>
          <figcaption>
            Experimental micrographs of Ag<sub>71</sub>Cu<sub>29</sub> held at 700&nbsp;&deg;C
            (approximately 970 K) for 2, 5 and 40 hours, B&ouml;hme and M&uuml;ller (2008), Fig. 5.
            Images courtesy of B&ouml;hme and M&uuml;ller.
          </figcaption>
        </figure>
        <p class="sd-pinchoff-lens">
          <strong>Why is this important? </strong> Because coarsening changes the strength and
          lifetime of solder joints. Here the measured $$t^{1/3}$$ growth points to
          bulk-diffusion-driven Ostwald ripening, not surface diffusion. With interface-localised
          mobility, however, the sharp-interface limit of the Cahn&ndash;Hilliard model is surface
          diffusion.
        </p>
      </article>
    </div>

    <h3 class="sd-chapter"><span>Watch a neck fail</span></h3>
    <div class="sd-card-grid">
      <article class="sd-card sd-card-wide">
        <div class="sd-card-body">
          <p class="sd-card-meta">Gold nanowire · 150 °C · 2017</p>
          <h3>A solid neck thins, separates, and rounds into particles</h3>
          <p>
            The lower row follows a gold wire in the TEM for nearly half an hour. The upper row is a
            three-dimensional atom-hopping calculation. Both show material leaving the constricted
            regions and accumulating in the thicker parts until the wire separates.
          </p>
          <a class="sd-card-citation" href="https://doi.org/10.1039/C7CP00463J"
            >Schnedlitz et al. (2017), <em>Physical Chemistry Chemical Physics</em>
            <span aria-hidden="true"></span></a
          >
        </div>
        <figure class="sd-card-visual sd-visual-gold">
          <img
            class="sd-open-figure"
            src="{{ '/assets/img/surface-diffusion/schnedlitz-gold-wire-2017-fig5.png' | relative_url }}"
            alt="Four stages of a gold nanowire pinching, shown in a cellular-automaton calculation and a TEM experiment"
            loading="lazy"
          />
          <figcaption>
            Cellular-automaton calculation (top) and TEM experiment at 150&nbsp;&deg;C (bottom),
            Schnedlitz et al. (2017), Fig. 5;
            <a href="https://creativecommons.org/licenses/by/3.0/">CC BY 3.0</a>.
          </figcaption>
        </figure>
        <p class="sd-pinchoff-lens">
          <strong>Why is this important? </strong> The experiment records the topology change, while the
          model tests whether thermally activated surface motion can reproduce its timing and
          location.
        </p>
      </article>

      <article class="sd-card sd-card-wide">
        <div class="sd-card-body">
          <p class="sd-card-meta">Al&ndash;Cu liquid rod · 565 °C · 2010</p>
          <h3>Bulk diffusion has its own universal pinchoff</h3>
          <p>
            Time-resolved synchrotron tomography follows a liquid rod through a 27.5-minute interval
            spanning separation. Copper is transported through the high-diffusivity liquid phase,
            rather than along the interface, yet the neck still approaches a conical pinch.
          </p>
          <a class="sd-card-citation" href="https://doi.org/10.1038/nphys1737"
            >Aagesen et al. (2010), <em>Nature Physics</em>
            <span aria-hidden="true"></span></a
          >
        </div>
        <figure class="sd-card-visual">
          <img
            class="sd-open-figure"
            src="{{ '/assets/img/surface-diffusion/aagesen-voorhees-bulk-diffusion-pinchoff-2010-fig1.png' | relative_url }}"
            alt="Four time-resolved tomographic reconstructions of a liquid aluminium-copper rod narrowing and separating under bulk diffusion"
            loading="lazy"
          />
          <figcaption>
            Liquid-rod pinchoff at 142.5, 155, 165 and 170 minutes, Aagesen et al. (2010),
            Fig. 1. Reproduced with the permission of Peter W. Voorhees; rights remain with
            Macmillan Publishers Limited.
          </figcaption>
        </figure>
        <p class="sd-pinchoff-lens">
          <strong>Why is this important? </strong> The same visible event can come from a different
          kinetic law. Here the similarity length scales as $$(T-t)^{1/3}$$, whereas for surface
          diffusion it scales as $$(T-t)^{1/4}$$. The shape alone does not identify the transport
          mechanism.
        </p>
      </article>
    </div>

    <article class="sd-card sd-curvature-card" aria-labelledby="sd-curvature-title">
      <div class="sd-card-body">
        <p class="sd-card-meta">Experimental liquid-interface measurements · supplied by Peter W. Voorhees</p>
        <h3 id="sd-curvature-title">See the curvature at the narrowing neck</h3>
        <p>
          Peter also supplied these five measured interface shapes, coloured by mean curvature.
          Follow the sequence from a connected neck to separation: the neck moves towards the
          blue, violet and black end of the supplied scale as its signed mean curvature becomes
          more negative. The colour reveals local geometry, which an outline alone cannot show.
        </p>
      </div>
      <figure class="sd-card-visual sd-curvature-viewer" data-curvature-viewer>
        <div class="sd-curvature-controls" role="group" aria-label="Choose an interface stage" hidden>
          <button type="button" aria-controls="sd-curvature-1" aria-pressed="true" data-stage="0">Stage 1</button>
          <button type="button" aria-controls="sd-curvature-2" aria-pressed="false" data-stage="1">Stage 2</button>
          <button type="button" aria-controls="sd-curvature-3" aria-pressed="false" data-stage="2">Stage 3</button>
          <button type="button" aria-controls="sd-curvature-4" aria-pressed="false" data-stage="3">Stage 4</button>
          <button type="button" aria-controls="sd-curvature-5" aria-pressed="false" data-stage="4">Stage 5</button>
        </div>
        <div class="sd-curvature-frame" id="sd-curvature-1">
          <a href="{{ '/assets/img/surface-diffusion/voorhees-mean-curvature-stage-1.png' | relative_url }}" aria-label="Open stage 1 at full size">
            <img src="{{ '/assets/img/surface-diffusion/voorhees-mean-curvature-stage-1.png' | relative_url }}" width="1120" height="784" loading="lazy" alt="Stage 1: a connected liquid-interface neck, coloured by signed mean curvature, with spatial axes in micrometres and the original colour bar" />
          </a>
        </div>
        <div class="sd-curvature-frame" id="sd-curvature-2">
          <a href="{{ '/assets/img/surface-diffusion/voorhees-mean-curvature-stage-2.png' | relative_url }}" aria-label="Open stage 2 at full size">
            <img src="{{ '/assets/img/surface-diffusion/voorhees-mean-curvature-stage-2.png' | relative_url }}" width="1120" height="784" loading="lazy" alt="Stage 2: a narrower connected neck with a blue region at the waist, retaining the original spatial axes and mean-curvature colour bar" />
          </a>
        </div>
        <div class="sd-curvature-frame" id="sd-curvature-3">
          <a href="{{ '/assets/img/surface-diffusion/voorhees-mean-curvature-stage-3.png' | relative_url }}" aria-label="Open stage 3 at full size">
            <img src="{{ '/assets/img/surface-diffusion/voorhees-mean-curvature-stage-3.png' | relative_url }}" width="1120" height="784" loading="lazy" alt="Stage 3: further neck thinning and more negative mean curvature near the waist, on the original colour scale" />
          </a>
        </div>
        <div class="sd-curvature-frame" id="sd-curvature-4">
          <a href="{{ '/assets/img/surface-diffusion/voorhees-mean-curvature-stage-4.png' | relative_url }}" aria-label="Open stage 4 at full size">
            <img src="{{ '/assets/img/surface-diffusion/voorhees-mean-curvature-stage-4.png' | relative_url }}" width="1120" height="784" loading="lazy" alt="Stage 4: a very thin connected neck with a violet and black waist on the supplied mean-curvature scale" />
          </a>
        </div>
        <div class="sd-curvature-frame" id="sd-curvature-5">
          <a href="{{ '/assets/img/surface-diffusion/voorhees-mean-curvature-stage-5.png' | relative_url }}" aria-label="Open stage 5 at full size">
            <img src="{{ '/assets/img/surface-diffusion/voorhees-mean-curvature-stage-5.png' | relative_url }}" width="1120" height="784" loading="lazy" alt="Stage 5: the liquid interface has separated into two pieces, retaining the original spatial axes and mean-curvature colour bar" />
          </a>
        </div>
        <p class="sd-curvature-status" aria-live="polite" aria-atomic="true" hidden>Stage 1 of 5 · Connected neck</p>
        <figcaption>
          Experimental interface shapes from Peter W. Voorhees&rsquo; supplied images, reproduced
          with permission. Stages follow the supplied order, with the original axes and colour
          bars intact; click an image to open it at full size. Spatial axes are in micrometres.
          Acquisition times and curvature units were not specified. These are additional images,
          distinct from the published Fig. 1 above.
        </figcaption>
      </figure>
      <p class="sd-pinchoff-lens">
        <strong>Why is this important? </strong> Curvature helps set the interfacial chemical potential
        that drives redistribution of material. Identifying the transport law still requires
        evidence of where material moves and how the neck changes with time; a curvature map alone
        does not distinguish bulk diffusion from surface diffusion.
      </p>
    </article>

    <h3 class="sd-chapter"><span>An engineering consequence</span></h3>
    <div class="sd-card-grid">
      <article class="sd-card">
        <div class="sd-card-body">
          <p class="sd-card-meta">Ag/Cu memory filaments · 2019</p>
          <h3>Memory survives until pinchoff, which needs precise prediction</h3>
          <p>
            Conductive filaments in resistive-memory devices were measured over lifetimes from
            microseconds to years. Thin-filament lifetime follows $$\tau\sim d^4,$$ the diameter law
            expected when surface diffusion controls the break.
          </p>
          <a class="sd-card-citation" href="https://doi.org/10.1038/s41467-018-07979-0"
            >Wang et al. (2019), <em>Nature Communications</em>
            <span aria-hidden="true"></span></a
          >
        </div>
        <figure class="sd-card-visual sd-visual-memory">
          <img
            class="sd-open-figure"
            src="{{ '/assets/img/surface-diffusion/rram-filament-lifetime-wang-2019.jpg' | relative_url }}"
            alt="Experimental switching data and a graph of silver and copper filament lifetime against initial diameter"
            loading="lazy"
          />
          <figcaption>
            Experimental retention data and diameter scaling, Wang et al. (2019), Fig. 5;
            <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>. Cropped from the
            open figure.
          </figcaption>
        </figure>
        <p class="sd-pinchoff-lens">
          <strong>Why is this important? </strong> A small change in filament diameter can turn a fleeting
          electrical state into long-term data retention.
        </p>
      </article>

      <article class="sd-card">
        <div class="sd-card-body">
          <p class="sd-card-meta">Transparent silver electrodes · 2020</p>
          <h3>A conducting network fails wire by wire</h3>
          <p>
            After annealing, continuous silver wires become isolated rods and beads. Thicker wires
            survive to higher temperatures; thinner wires lose the connected paths that carry
            current.
          </p>
          <a class="sd-card-citation" href="https://doi.org/10.1016/j.dib.2020.105422"
            >Chung, Park and Lee (2020), <em>Data in Brief</em>
            <span aria-hidden="true"></span></a
          >
        </div>
        <figure class="sd-card-visual sd-visual-sinter">
          <img
            class="sd-open-figure"
            src="{{ '/assets/img/surface-diffusion/silver-wire-electrode-chung-2020.jpg' | relative_url }}"
            alt="Scanning electron micrographs of silver nanowire networks before and after annealing"
            loading="lazy"
          />
          <figcaption>
            Silver-wire networks before and after annealing, Chung, Park and Lee (2020), Fig. 1;
            <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>. Cropped from the
            open figure.
          </figcaption>
        </figure>
        <p class="sd-pinchoff-lens">
          <strong>Why is this important? </strong> A local pinchoff becomes device failure when it breaks
          the last conducting route across a transparent electrode.
        </p>
      </article>

      <article class="sd-card sd-card-wide">
        <div class="sd-card-body">
          <p class="sd-card-meta">Single-crystal silicon · 2019</p>
          <h3>Crystal structure can be used to prevent breakup</h3>
          <p>
            Templated dewetting turns patterned silicon films into connected, sub-millimetre-long
            crystalline wires. Facet-dependent surface energies steer the evolution away from the
            bead-forming instability of an isotropic cylinder.
          </p>
          <a class="sd-card-citation" href="https://doi.org/10.1038/s41467-019-13371-3"
            >Bollani et al. (2019), <em>Nature Communications</em>
            <span aria-hidden="true"></span></a
          >
        </div>
        <figure class="sd-card-visual sd-visual-silicon-wire">
          <img
            class="sd-open-figure"
            src="{{ '/assets/img/surface-diffusion/bollani-silicon-wire-2019-fig1.jpg' | relative_url }}"
            alt="Fabrication diagram and electron micrographs of long single-crystal silicon nanowire arrays"
            loading="lazy"
          />
          <figcaption>
            Fabrication and SEM views of long silicon wires, Bollani et al. (2019), Fig. 1;
            <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>.
          </figcaption>
        </figure>
        <p class="sd-pinchoff-lens">
          <strong>Why is this important? </strong> Understanding pinchoff also suggests how to suppress it:
          use crystalline anisotropy to preserve a long conducting path.
        </p>
      </article>
    </div>

  </section>

  <section class="sd-model" aria-labelledby="sd-model-title">
    <div class="sd-section-heading">
      <p class="sd-section-number">03</p>
      <div>
        <h2 id="sd-model-title">Which model does the cold silver wire follow?</h2>
        <p>Experimental photographs</p>
      </div>
    </div>

    <figure class="sd-source-figure sd-model-figure">
      <img
        src="{{ '/assets/img/surface-diffusion/volk-silver-wire-2015-fig1.png' | relative_url }}"
        alt="The same ultrathin silver nanowire photographed at 253, 268, 293, and 363 Kelvin"
        loading="lazy"
      />
      <figcaption>
        The same ultrathin Ag wire at 253, 268, 293, and 363 K, Volk et al. (2015), Fig. 1;
        <a href="https://creativecommons.org/licenses/by-nc/3.0/">CC BY-NC 3.0</a>. The projected
        outline of the first frame was used as the input to the paper&rsquo;s contour calculation.
      </figcaption>
    </figure>

    <div class="sd-model-grid">
      <div class="sd-equation-card">
        <p class="sd-eyebrow">The model actually used</p>
        <div class="sd-equation">
          $$
          V_n=B\,\partial_s^2\kappa,
          \qquad
          B=\frac{D_s\gamma\Omega^{4/3}}{k_BT}.
          $$
        </div>
        <p>
          Volk and co-workers traced the TEM silhouette and evolved it as a
          <strong>two-dimensional, constant-thickness contour</strong>. They set $$B=1,$$ so the
          calculation predicts the order and location of breaks, not the physical breakup time.
        </p>
      </div>

      <div class="sd-equation-card">
        <p class="sd-eyebrow">The free three-dimensional surface</p>
        <div class="sd-equation">
          $$
          V_n=B_3\Delta_\Sigma H,
          \qquad
          \omega(k)=B_3k^2(R_0^{-2}-k^2).
          $$
        </div>
        <p>
          A round free cylinder is unstable when $$kR_0&lt;1.$$ Its fastest wavelength is
          $$2\pi\sqrt2R_0=4.44D,$$ and the fastest growth rate scales like $$R_0^{-4}.$$ That
          fourth-power clock explains why a wire only a few nanometres across can change rapidly.
        </p>
      </div>
    </div>

    <div class="sd-model-reading">
      <h3>What the picture and model support</h3>
      <p>
        The wire is solid: it is unchanged at 253 K, begins smoothing and necking at
        268 K, and is segmented by 293 K. The contour model reproduces several observed
        break locations, which is good evidence for curvature-driven surface flux.
      </p>
      <p>
        It is not yet the theorem&rsquo;s ideal three-dimensional experiment. TEM records a projection;
        the wire lies on a 3 nm amorphous-carbon film; crystalline anisotropy is suppressed in
        the calculation; and the diameter is only about twelve lattice spacings. The change near
        260 K is a diameter- and protocol-dependent kinetic onset, not a phase transition.
      </p>
      <a class="sd-paper-link sd-paper-link-inline" href="https://doi.org/10.1039/C5CP04696C"
        >Volk et al., <em>Physical Chemistry Chemical Physics</em>
        <span aria-hidden="true"></span></a
      >
    </div>

  </section>

  <section class="sd-next" aria-labelledby="sd-scope-title">
    <p class="sd-section-number">04</p>
    <div class="sd-next-content">
      <div>
        <h2 id="sd-scope-title">When is surface diffusion the right model?</h2>
        <p>
          Cahn and Taylor's 1994 overview gives a useful checklist: surface energy is the driving
          force; matter is transported along the interface rather than through the bulk or the
          surrounding medium; and the relevant mass is conserved.
        </p>
        <p>
          They distinguish three scenarios. If attachment and detachment are fast, transport along
          the surface is the bottleneck and Mullins' fourth-order law applies. If surface transport
          is fast, attachment kinetics controls a different volume-preserving curvature law. If the
          rates are comparable, their full intermediate law is needed. The material, temperature,
          crystal orientation and length scale determine which scenario is seen.
        </p>
        <a
          class="sd-paper-link sd-paper-link-inline"
          href="https://doi.org/10.1016/0956-7151(94)90123-6"
          >Cahn and Taylor, <em>Acta Metallurgica et Materialia</em>
          <span aria-hidden="true"> </span></a
        >
      </div>
      <figure class="sd-source-figure sd-next-figure">
        <img
          src="{{ '/assets/img/surface-diffusion/carter-roosen-cahn-taylor-1995-fig5.gif' | relative_url }}"
          alt="Numerical comparison in which a staircase-shaped particle splits under surface diffusion but not under surface-attachment-limited kinetics"
          loading="lazy"
        />
        <figcaption>
          The same initial staircase under two kinetic laws: light gray is surface diffusion and
          dark gray is surface-attachment-limited kinetics. The surface-diffusion shape splits; the
          other does not. Carter, Roosen, Cahn and Taylor (1995), Fig. 5; see
          <a href="https://doi.org/10.1016/0956-7151(95)00134-H">the article</a> and the
          <a href="https://www.ctcms.nist.gov/~roosen/SD_SALK/SD_SALK/section3_9.html"
            >authors' NIST page</a
          >.
        </figcaption>
      </figure>
    </div>
  </section>

  <section class="sd-next sd-next-text-only" aria-labelledby="sd-next-title">
    <p class="sd-section-number">05</p>
    <div class="sd-next-content">
      <div>
        <h2 id="sd-next-title">An experiment I'd love to see</h2>
        <p>
          Schnedlitz and co-workers already show what a useful time-resolved pinchoff sequence looks
          like. It would be really interesting to repeat that kind of experiment on a minimally
          supported nanowire, or a fabricated toroidal neck, while measuring the waist, the full
          profile, and the material budget throughout the final approach to rupture.
        </p>
        <p class="sd-next-note">
          A single dataset could test whether $$A(t)^4$$ is linear in time, whether rescaled profiles
          collapse, whether the terminal slope approaches 46.04 degrees, and whether material is conserved
          while the outer surface remains smooth.
        </p>
      </div>
    </div>
  </section>

  <section class="sd-sources" aria-labelledby="sd-sources-title">
    <h2 id="sd-sources-title">Sources and image credits</h2>
    <p>
      Every scientific image on this page is attached to the specific claim it supports and is
      identified by paper and figure number, or by its contributing researcher, in its caption. No image is AI-generated. The conical
      profile is regenerated numerically from the certified equation.
    </p>
    <p>
      Figures from Wang et al. (2021), Schnedlitz et al. (2017), Wang et al. (2019), Bollani et al.
      (2019), and Chung, Park and Lee (2020) are used under the Creative Commons licences linked
      in their captions. Volk et al. (2015) is used under CC BY-NC 3.0. Mullins and Shewmon
      (1959), Figs. 4 and 5, are reproduced at reduced resolution for scholarly commentary; rights
      remain with the publisher.
    </p>
    <p>
      The Ag&ndash;Cu micrographs from B&ouml;hme and M&uuml;ller (2008), Fig. 5, and the kinetic
      comparison from Carter, Roosen, Cahn and Taylor (1995), Fig. 5, are reproduced at reduced
      resolution for scholarly commentary; rights remain with the publishers.
    </p>
    <p>
      The liquid-rod time sequence from Aagesen et al. (2010), Fig. 1, is reproduced with the
      permission of Peter W. Voorhees; rights remain with Macmillan Publishers Limited. The five
      additional mean-curvature images were supplied by Peter W. Voorhees and are reproduced with
      permission, preserving their original axes and colour scales.
    </p>
  </section>
</div>
