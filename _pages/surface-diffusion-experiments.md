---
layout: page
title: surface diffusion in the lab
description: Historical observations of motion by surface diffusion.
permalink: /surface-diffusion-experiments/
nav: true
nav_order: 2.5
---

<link rel="stylesheet" href="{{ '/assets/css/surface-diffusion-gallery.css' | relative_url }}" />

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
          Each example below is built around a figure from the cited paper. Experimental and
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
    </div>

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
      identified by paper and figure number in its caption. No image is AI-generated. The conical
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
  </section>
</div>
