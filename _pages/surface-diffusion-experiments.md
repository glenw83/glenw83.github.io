---
layout: page
title: experiments
description: What laboratory experiments tell us about pinchoff by surface diffusion.
permalink: /surface-diffusion-experiments/
nav: true
nav_order: 2.5
---

<div class="sd-gallery-page">
  <section class="sd-hero" aria-labelledby="sd-hero-title">
    <div class="sd-hero-copy">
      <p class="sd-eyebrow">Surface diffusion · real experiments</p>
      <h2 id="sd-hero-title">When a solid flows along its own surface</h2>
      <p class="sd-deck">
        A solid need not melt to change shape. Atoms can migrate along its surface, driven by
        differences in curvature. A groove can deepen, a wire can bead up, and a narrow neck can
        break.
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
        last panel is the singular-time double cone $$r=\alpha|z|$$. This is a calculation, not an
        experimental photograph.
      </figcaption>
    </figure>

  </section>

  <section class="sd-primer" aria-labelledby="sd-mullins-title">
    <div>
      <p class="sd-section-number">01</p>
      <h2 id="sd-mullins-title">The practical question, from Mullins&rsquo; point of view</h2>
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
          Left: the groove after 1, 16, and 81 hours at 930&nbsp;&deg;C. Right: its width follows
          $$w\propto t^{1/4}$$ at both 930&nbsp;&deg;C and 1035&nbsp;&deg;C. Mullins &amp; Shewmon
          (1959), Figs. 4 and 5.
        </figcaption>
      </figure>

      <p>
        The pictures make the point that matters for pinchoff. Surface diffusion is a smoothing law,
        but it is not simply a law that makes every shape rounder. The same fourth-order transport
        that broadens a groove can amplify a long-wave disturbance on a thin cylinder until the
        cylinder loses connectivity.
      </p>
      <a class="sd-paper-link sd-paper-link-inline" href="https://doi.org/10.1016/0001-6160(59)90069-0"
        >Mullins &amp; Shewmon, <em>Acta Metallurgica</em> <span aria-hidden="true">&nearr;</span></a
      >
    </div>

  </section>

  <section class="sd-gallery-section" aria-labelledby="sd-gallery-title">
    <div class="sd-section-heading">
      <p class="sd-section-number">02</p>
      <div>
        <h2 id="sd-gallery-title">Where the motion can be seen&mdash;and why it matters</h2>
        <p>
          Each example below is built around a figure from the cited paper. Experimental and
          simulated panels are identified in the caption.
        </p>
      </div>
    </div>

    <h3 class="sd-chapter"><span>See the atoms move</span></h3>
    <div class="sd-card-grid">
      <article class="sd-card sd-card-wide">
        <figure class="sd-card-visual sd-visual-atomic">
          <img
            class="sd-open-figure"
            src="{{ '/assets/img/surface-diffusion/wang-silver-step-migration-2021-fig2a-l.jpg' | relative_url }}"
            alt="Twelve sequential atomic-resolution TEM frames showing steps migrating along a silver nanowire"
            loading="lazy"
          />
          <figcaption>
            Experimental in-situ HRTEM sequence, cropped to panels a&ndash;l from Wang et al. (2021),
            Fig. 2; <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>.
          </figcaption>
        </figure>
        <div class="sd-card-body">
          <p class="sd-card-meta">Silver nanowire · room temperature · 2021</p>
          <h3>Surface steps walk across a crystalline solid</h3>
          <p>
            The atomic lattice remains visible while surface steps migrate along a 6.6&nbsp;nm silver
            wire under tension. When two steps overlap, a partial dislocation nucleates. The image
            makes the microscopic carrier of surface diffusion visible rather than merely inferred.
          </p>
          <p class="sd-pinchoff-lens">
            <strong>Why it matters.</strong> Surface motion can change the mechanical strength of a
            nanoscale component even when the component remains solid.
          </p>
        </div>
        <a class="sd-paper-link" href="https://doi.org/10.1038/s41467-021-25542-2"
          >Wang et al., <em>Nature Communications</em> <span aria-hidden="true">&nearr;</span></a
        >
      </article>
    </div>

    <h3 class="sd-chapter"><span>Watch a neck fail</span></h3>
    <div class="sd-card-grid">
      <article class="sd-card sd-card-wide">
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
        <div class="sd-card-body">
          <p class="sd-card-meta">Gold nanowire · 150 °C · 2017</p>
          <h3>A solid neck thins, separates, and rounds into particles</h3>
          <p>
            The lower row follows a gold wire in the TEM for nearly half an hour. The upper row is a
            three-dimensional atom-hopping calculation. Both show material leaving the constricted
            regions and accumulating in the thicker parts until the wire separates.
          </p>
          <p class="sd-pinchoff-lens">
            <strong>Why it matters.</strong> The experiment records the topology change, while the
            model tests whether thermally activated surface motion can reproduce its timing and
            location.
          </p>
        </div>
        <a class="sd-paper-link" href="https://doi.org/10.1039/C7CP00463J"
          >Schnedlitz et al., <em>Physical Chemistry Chemical Physics</em>
          <span aria-hidden="true">&nearr;</span></a
        >
      </article>
    </div>

    <h3 class="sd-chapter"><span>See the engineering consequence</span></h3>
    <div class="sd-card-grid">
      <article class="sd-card">
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
        <div class="sd-card-body">
          <p class="sd-card-meta">Ag/Cu memory filaments · 2019</p>
          <h3>A pinching law predicts how long a memory survives</h3>
          <p>
            Conductive filaments in resistive-memory devices were measured over lifetimes from
            microseconds to years. Thin-filament lifetime follows $$\tau\sim d^4$$, the diameter law
            expected when surface diffusion controls the break.
          </p>
          <p class="sd-pinchoff-lens">
            <strong>Why it matters.</strong> A small change in filament diameter can turn a fleeting
            electrical state into long-term data retention.
          </p>
        </div>
        <a class="sd-paper-link" href="https://doi.org/10.1038/s41467-018-07979-0"
          >Wang et al., <em>Nature Communications</em> <span aria-hidden="true">&nearr;</span></a
        >
      </article>

      <article class="sd-card">
        <figure class="sd-card-visual sd-visual-sinter">
          <img
            class="sd-open-figure"
            src="{{ '/assets/img/surface-diffusion/silver-wire-electrode-chung-2020.jpg' | relative_url }}"
            alt="Scanning electron micrographs of silver nanowire networks before and after annealing"
            loading="lazy"
          />
          <figcaption>
            Silver-wire networks before and after annealing, Chung, Park &amp; Lee (2020), Fig. 1;
            <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>. Cropped from the
            open figure.
          </figcaption>
        </figure>
        <div class="sd-card-body">
          <p class="sd-card-meta">Transparent silver electrodes · 2020</p>
          <h3>A conducting network fails wire by wire</h3>
          <p>
            After annealing, continuous silver wires become isolated rods and beads. Thicker wires
            survive to higher temperatures; thinner wires lose the connected paths that carry
            current.
          </p>
          <p class="sd-pinchoff-lens">
            <strong>Why it matters.</strong> A local pinchoff becomes device failure when it breaks
            the last conducting route across a transparent electrode.
          </p>
        </div>
        <a class="sd-paper-link" href="https://doi.org/10.1016/j.dib.2020.105422"
          >Chung, Park &amp; Lee, <em>Data in Brief</em> <span aria-hidden="true">&nearr;</span></a
        >
      </article>

      <article class="sd-card sd-card-wide">
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
        <div class="sd-card-body">
          <p class="sd-card-meta">Single-crystal silicon · 2019</p>
          <h3>Crystal structure can be used to prevent breakup</h3>
          <p>
            Templated dewetting turns patterned silicon films into connected, sub-millimetre-long
            crystalline wires. Facet-dependent surface energies steer the evolution away from the
            bead-forming instability of an isotropic cylinder.
          </p>
          <p class="sd-pinchoff-lens">
            <strong>Why it matters.</strong> Understanding pinchoff also suggests how to suppress it:
            use crystalline anisotropy to preserve a long conducting path.
          </p>
        </div>
        <a class="sd-paper-link" href="https://doi.org/10.1038/s41467-019-13371-3"
          >Bollani et al., <em>Nature Communications</em> <span aria-hidden="true">&nearr;</span></a
        >
      </article>
    </div>

  </section>

  <section class="sd-model" aria-labelledby="sd-model-title">
    <div class="sd-section-heading">
      <p class="sd-section-number">03</p>
      <div>
        <h2 id="sd-model-title">Which model does the cold silver wire follow?</h2>
        <p>The experimental photograph determines exactly what the calculation can claim.</p>
      </div>
    </div>

    <figure class="sd-source-figure sd-model-figure">
      <img
        src="{{ '/assets/img/surface-diffusion/volk-silver-wire-2015-fig1.png' | relative_url }}"
        alt="The same ultrathin silver nanowire photographed at 253, 268, 293, and 363 Kelvin"
        loading="lazy"
      />
      <figcaption>
        The same ultrathin Ag wire at 253, 268, 293, and 363&nbsp;K, Volk et al. (2015), Fig. 1;
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
          <strong>two-dimensional, constant-thickness contour</strong>. They set $$B=1$$, so the
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
          A round free cylinder is unstable when $$kR_0&lt;1$$. Its fastest wavelength is
          $$2\pi\sqrt2R_0=4.44D$$, and the fastest growth rate scales like $$R_0^{-4}$$. That
          fourth-power clock explains why a wire only a few nanometres across can change rapidly.
        </p>
      </div>
    </div>

    <div class="sd-model-reading">
      <h3>What the picture and model support</h3>
      <p>
        The wire is solid: it is unchanged at 253&nbsp;K, begins smoothing and necking at
        268&nbsp;K, and is segmented by 293&nbsp;K. The contour model reproduces several observed
        break locations, which is good evidence for curvature-driven surface flux.
      </p>
      <p>
        It is not yet the theorem&rsquo;s ideal three-dimensional experiment. TEM records a projection;
        the wire lies on a 3&nbsp;nm amorphous-carbon film; crystalline anisotropy is suppressed in
        the calculation; and the diameter is only about twelve lattice spacings. The change near
        260&nbsp;K is a diameter- and protocol-dependent kinetic onset, not a phase transition.
      </p>
      <a class="sd-paper-link sd-paper-link-inline" href="https://doi.org/10.1039/C5CP04696C"
        >Volk et al., <em>Physical Chemistry Chemical Physics</em>
        <span aria-hidden="true">&nearr;</span></a
      >
    </div>

  </section>

  <section class="sd-theorem" aria-labelledby="sd-theorem-title">
    <div class="sd-theorem-copy">
      <p class="sd-section-number">04</p>
      <h2 id="sd-theorem-title">What the new theorem adds</h2>
      <p>
        The experiments show that surface diffusion is real and that solid wires pinch. They do not
        prove that the clean geometric evolution equation develops a singularity on a smooth closed
        surface. The theorem closes that gap.
      </p>
      <ul>
        <li>a smooth embedded torus remains embedded for every $$t&lt;T$$;</li>
        <li>one waist reaches zero with $$A(t)\sim\{4\mu(T-t)\}^{1/4}$$;</li>
        <li>the magnified neck converges to the positive conical profile;</li>
        <li>the rest of the surface converges smoothly.</li>
      </ul>
      <a class="sd-primary-link" href="https://arxiv.org/abs/2608.21882"
        >Read <em>Pinchoff by surface diffusion</em> <span aria-hidden="true">&rarr;</span></a
      >
    </div>
    <figure class="sd-theorem-figure">
      <img
        src="{{ '/assets/img/surface-diffusion/certified-pinchoff-profile.svg' | relative_url }}"
        alt="Numerically regenerated pinchoff profile approaching its singular double-cone limit"
        loading="lazy"
      />
      <figcaption>
        Numerical profile from the certified equation: the waist follows the
        $$(T-t)^{1/4}$$ clock and the limiting cone has half-angle approximately 46.04&deg;.
      </figcaption>
    </figure>
  </section>

  <section class="sd-next" aria-labelledby="sd-next-title">
    <p class="sd-section-number">05</p>
    <div class="sd-next-content">
      <div>
        <p class="sd-eyebrow">An experiment worth trying</p>
        <h2 id="sd-next-title">One measurement could connect the whole story</h2>
        <p>
          Schnedlitz and co-workers already show what a useful time-resolved pinchoff sequence looks
          like. It would be really interesting to repeat that kind of experiment on a minimally
          supported nanowire, or a fabricated toroidal neck, while measuring the waist, the full
          profile, and the material budget throughout the final approach to rupture.
        </p>
        <p class="sd-next-note">
          A single dataset could test whether $$A(t)^4$$ is linear in time, whether rescaled profiles
          collapse, whether the terminal slope approaches 46.04&deg;, and whether material is conserved
          while the outer surface remains smooth.
        </p>
      </div>
      <figure class="sd-source-figure sd-next-figure">
        <img
          src="{{ '/assets/img/surface-diffusion/schnedlitz-gold-wire-2017-fig5.png' | relative_url }}"
          alt="Time-resolved experimental and simulated gold nanowire pinchoff sequence"
          loading="lazy"
        />
        <figcaption>
          The closest existing template: calculation above and time-resolved TEM below. Schnedlitz
          et al. (2017), Fig. 5; <a href="https://creativecommons.org/licenses/by/3.0/">CC BY 3.0</a>.
        </figcaption>
      </figure>
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
      (2019), and Chung, Park &amp; Lee (2020) are used under the Creative Commons licences linked
      in their captions. Volk et al. (2015) is used under CC BY-NC 3.0. Mullins &amp; Shewmon
      (1959), Figs. 4 and 5, are reproduced at reduced resolution for scholarly commentary; rights
      remain with the publisher.
    </p>
  </section>
</div>
