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
      <p class="sd-eyebrow">Surface diffusion · an experimental gallery</p>
      <h2 id="sd-hero-title">When a solid flows along its own surface</h2>
      <p class="sd-deck">
        A solid need not melt to change shape. Atoms can migrate along its surface, driven by
        differences in curvature. Small corrugations flatten. Grain boundaries carve grooves. A
        long, thin wire can amplify a neck until it pinches.
      </p>
      <p>
        This is the laboratory story behind
        <a href="https://arxiv.org/abs/2608.21882"><em>Pinchoff by surface diffusion</em></a>.
        Experiments had revealed the motion, its fourth-order clock, and many instances of breakup.
        The new theorem proves that the ideal geometric law itself can carry a smooth, closed surface
        all the way to a one-point conical singularity.
      </p>
    </div>

    <figure class="sd-hero-figure">
      <img
        src="{{ '/assets/img/surface-diffusion/certified-pinchoff-profile.svg' | relative_url }}"
        alt="Numerically regenerated meridian profiles narrowing toward a double cone at singular time"
      />
      <figcaption>
        Mathematical rendering, not an experiment: meridians $$r=A\,U(z/A)$$ regenerated from the
        profile ODE at the certificate&rsquo;s central parameter values. The last panel is the
        singular-time double cone $$r=\alpha|z|$$, not a guessed post-breakup shape.
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
        atoms are mobile on the surface but the solid as a whole does not flow? Curvature changes the
        surface chemical potential, atoms diffuse down its gradient, and mass conservation turns that
        flux into normal motion. Area decreases while enclosed material is conserved.
      </p>
      <div class="sd-law" role="group" aria-label="Three experimental signatures of surface diffusion">
        <div><strong>Grooves</strong><span>width and depth &prop; t<sup>1/4</sup></span></div>
        <div><strong>Gratings</strong><span>decay rate &prop; &lambda;<sup>&minus;4</sup></span></div>
        <div><strong>Filaments</strong><span>lifetime &prop; d<sup>4</sup></span></div>
      </div>
      <p>
        The same law that erases a short-wavelength scratch destabilises a sufficiently long wave on
        a cylinder. In isotropic linear theory the fastest mode has wavelength
        $$2\pi\sqrt{2}R\approx4.44D$$. The practical endpoint is not merely smoothing: a neck can
        remove a load-bearing path, an electrical connection, or an entire component.
      </p>
    </div>
  </section>

  <section class="sd-gallery-section" aria-labelledby="sd-gallery-title">
    <div class="sd-section-heading">
      <p class="sd-section-number">02</p>
      <div>
        <h2 id="sd-gallery-title">Eleven experimental windows on the same motion</h2>
        <p>
          Every image below comes from an identified published paper, and each caption distinguishes
          experiment from simulation. Where a reusable figure was not available, the result is
          described in words and linked at source; no substitute image was invented.
        </p>
      </div>
    </div>

    <h3 class="sd-chapter"><span>Identify the transport law</span></h3>
    <div class="sd-card-grid">
      <article class="sd-card">
        <div class="sd-card-visual sd-text-visual" role="img" aria-label="The fourth-root time law measured in copper grooves">
          <span>Measured kinetic exponent</span>
          <strong>d, w &prop; t<sup>1/4</sup></strong>
          <small>Paper figure linked, not reproduced</small>
        </div>
        <div class="sd-card-body">
          <p class="sd-card-meta">Copper bicrystals · 1959</p>
          <h3>Thermal grooves keep the predicted clock</h3>
          <p>
            Copper bicrystals were annealed in dry hydrogen at 930&nbsp;&deg;C and 1035&nbsp;&deg;C.
            The groove where a grain boundary met the free surface retained a rescaled shape while
            both its depth and width grew with the fourth root of time.
          </p>
          <p class="sd-pinchoff-lens"><strong>Pinchoff lens.</strong> This is the classic macroscopic
            test of the clock that also governs a collapsing waist. It is an open groove, however,
            not a topology change.</p>
        </div>
        <a class="sd-paper-link" href="https://doi.org/10.1016/0001-6160(59)90069-0">Mullins &amp; Shewmon, <em>Acta Metallurgica</em> <span aria-hidden="true">&nearr;</span></a>
      </article>

      <article class="sd-card">
        <div class="sd-card-visual sd-text-visual" role="img" aria-label="The inverse fourth-power wavelength law measured in silicon gratings">
          <span>Measured spectral fingerprint</span>
          <strong>&Gamma;(q) &prop; q<sup>4</sup></strong>
          <small>Paper figure linked, not reproduced</small>
        </div>
        <div class="sd-card-body">
          <p class="sd-card-meta">Silicon (001) · 1994</p>
          <h3>Short ripples disappear first</h3>
          <p>
            Etched silicon gratings were annealed between 800&nbsp;&deg;C and 1100&nbsp;&deg;C. Their
            amplitudes decayed exponentially, with a rate scaling approximately as
            $$\lambda^{-4}$$; scanning tunnelling microscopy also resolved the evolving atomic steps.
          </p>
          <p class="sd-pinchoff-lens"><strong>Pinchoff lens.</strong> Competing transport mechanisms
            predict different powers, so this is a clean mechanism test. The geometry remains a
            small graph and never breaks.</p>
        </div>
        <a class="sd-paper-link" href="https://doi.org/10.1016/0022-3697(94)90116-3">Keeffe, Umbach &amp; Blakely, <em>J. Phys. Chem. Solids</em> <span aria-hidden="true">&nearr;</span></a>
      </article>

      <article class="sd-card">
        <figure class="sd-card-visual sd-visual-atomic">
          <img
            class="sd-open-figure"
            src="{{ '/assets/img/surface-diffusion/silver-step-migration-wang-2021.jpg' | relative_url }}"
            alt="Sequential transmission electron microscopy frames showing surface steps migrating along a silver nanowire"
            loading="lazy"
          />
          <figcaption>
            Experimental TEM sequence, Wang et al. (2021), Fig. 5;
            <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>. The displayed
            composite is cropped from the open figure.
          </figcaption>
        </figure>
        <div class="sd-card-body">
          <p class="sd-card-meta">Silver nanowires · 2021</p>
          <h3>Surface steps walk across a crystalline solid</h3>
          <p>
            Sequential atomic-resolution TEM frames track steps moving along a silver nanowire while
            its interior remains crystalline. The carrier behind the continuum law becomes visible.
          </p>
          <p class="sd-pinchoff-lens"><strong>Pinchoff lens.</strong> Tensile loading, dislocations,
            and the electron beam are also present, so this establishes atom-scale surface mobility,
            not unforced pinchoff by itself.</p>
        </div>
        <a class="sd-paper-link" href="https://doi.org/10.1038/s41467-021-25542-2">Wang et al., <em>Nature Communications</em> <span aria-hidden="true">&nearr;</span></a>
      </article>
    </div>

    <h3 class="sd-chapter"><span>Watch a neck fail</span></h3>
    <div class="sd-card-grid">
      <article class="sd-card">
        <div class="sd-card-visual sd-text-visual" role="img" aria-label="Measured wavelength and sphere diameter in annealed copper nanowires">
          <span>38 nm copper wire</span>
          <strong>165 &plusmn; 57 nm</strong>
          <small>measured bead spacing; theory: 169 nm</small>
        </div>
        <div class="sd-card-body">
          <p class="sd-card-meta">Copper nanowires · 2004</p>
          <h3>The cylinder calculation lands on the numbers</h3>
          <p>
            Wires 30&ndash;50&nbsp;nm across were annealed at 400&ndash;600&nbsp;&deg;C and evolved from
            constrictions to rods and then spheres. For a 38&nbsp;nm wire, the measured spacing was
            $$165\pm57$$&nbsp;nm and sphere diameter $$73\pm9$$&nbsp;nm; the isotropic model predicted
            169&nbsp;nm and 73&nbsp;nm.
          </p>
          <p class="sd-pinchoff-lens"><strong>Pinchoff lens.</strong> The selected wavelength and
            volume ledger agree strikingly, although static micrographs cannot resolve the final
            singular profile.</p>
        </div>
        <a class="sd-paper-link" href="https://doi.org/10.1063/1.1826237">Toimil Molares et al., <em>Applied Physics Letters</em> <span aria-hidden="true">&nearr;</span></a>
      </article>

      <article class="sd-card sd-card-wide">
        <figure class="sd-card-visual sd-visual-silver">
          <img
            class="sd-open-figure"
            src="{{ '/assets/img/surface-diffusion/volk-silver-wire-2015-fig1.png' | relative_url }}"
            alt="Four cryogenic TEM frames of ultrathin silver nanowires progressing from necked wires to separated fragments"
            loading="lazy"
          />
          <figcaption>
            The same ultrathin Ag wire at 253, 268, 293, and 363&nbsp;K, Volk et al. (2015), Fig. 1;
            <a href="https://creativecommons.org/licenses/by-nc/3.0/">CC BY-NC 3.0</a>.
          </figcaption>
        </figure>
        <div class="sd-card-body">
          <p class="sd-card-meta">Pristine silver nanowires · 2015</p>
          <h3>A solid wire breaks below room temperature</h3>
          <p>
            Solvent- and template-free wires, about 5&nbsp;nm across, were unchanged at 253&nbsp;K,
            visibly smoother and more necked at 268&nbsp;K, and segmented by 293&nbsp;K. A reference
            held at 77&nbsp;K for 48 hours did not change. A contour calculation anticipated the order
            and position of several breaks.
          </p>
          <p class="sd-pinchoff-lens"><strong>Pinchoff lens.</strong> This removes the idea that a
            liquid phase is required. The precise model used here&mdash;and what it leaves out&mdash;is
            unpacked in the next section.</p>
        </div>
        <a class="sd-paper-link" href="https://doi.org/10.1039/C5CP04696C">Volk et al., <em>Physical Chemistry Chemical Physics</em> <span aria-hidden="true">&nearr;</span></a>
      </article>

      <article class="sd-card sd-card-wide">
        <figure class="sd-card-visual sd-visual-gold">
          <img
            class="sd-open-figure"
            src="{{ '/assets/img/surface-diffusion/schnedlitz-gold-wire-2017-fig5.png' | relative_url }}"
            alt="A four-stage gold nanowire breakup experiment paired with a four-stage cellular-automaton calculation"
            loading="lazy"
          />
          <figcaption>
            Cellular-automaton calculation (top) and TEM experiment at 150&nbsp;&deg;C (bottom),
            Schnedlitz et al. (2017), Fig. 5;
            <a href="https://creativecommons.org/licenses/by/3.0/">CC BY 3.0</a>.
          </figcaption>
        </figure>
        <div class="sd-card-body">
          <p class="sd-card-meta">Au, Ag, Cu, and Ni nanowires · 2017</p>
          <h3>Four metals share an instability, but not a clock</h3>
          <p>
            Time-resolved gold breakup agrees closely with a three-dimensional atom-hopping model.
            Silver behaves similarly; copper and nickel are slowed by oxide shells. This comparison
            shows why surface mobility and chemistry matter as much as geometry.
          </p>
          <p class="sd-pinchoff-lens"><strong>Pinchoff lens.</strong> The real shape and a discrete
            surface-diffusion mechanism can be followed side by side, but a supported, faceted wire
            is not the isotropic closed surface of the theorem.</p>
        </div>
        <a class="sd-paper-link" href="https://doi.org/10.1039/C7CP00463J">Schnedlitz et al., <em>Physical Chemistry Chemical Physics</em> <span aria-hidden="true">&nearr;</span></a>
      </article>

      <article class="sd-card">
        <div class="sd-card-visual sd-text-visual" role="img" aria-label="Gold nanowire junctions break sooner than isolated wires">
          <span>Experiment + kinetic Monte Carlo</span>
          <strong>the crossing breaks first</strong>
          <small>Paper figure linked, not reproduced</small>
        </div>
        <div class="sd-card-body">
          <p class="sd-card-meta">Gold nanowire junctions · 2018</p>
          <h3>A crossing can be less stable than a wire</h3>
          <p>
            Annealed gold-wire junctions broke preferentially near their crossings. Kinetic Monte
            Carlo calculations supported a surface-atom-diffusion explanation and showed that
            network geometry changes where failure begins.
          </p>
          <p class="sd-pinchoff-lens"><strong>Pinchoff lens.</strong> Pinchoff is not only a property
            of an isolated cylinder; contacts can concentrate the mass flux and become the weak
            points of a device.</p>
        </div>
        <a class="sd-paper-link" href="https://doi.org/10.1088/1361-6528/aa9a1b">Vigonski et al., <em>Nanotechnology</em> <span aria-hidden="true">&nearr;</span></a>
      </article>
    </div>

    <h3 class="sd-chapter"><span>Use the motion — or design against it</span></h3>
    <div class="sd-card-grid">
      <article class="sd-card">
        <div class="sd-card-visual sd-text-visual" role="img" aria-label="Patterned silicon holes reorganise into a buried cavity during annealing">
          <span>Hydrogen anneal</span>
          <strong>holes &rarr; buried void</strong>
          <small>Paper figure linked, not reproduced</small>
        </div>
        <div class="sd-card-body">
          <p class="sd-card-meta">Silicon-on-nothing · 2000</p>
          <h3>Topology change becomes a fabrication method</h3>
          <p>
            Patterned holes in silicon were annealed in hydrogen. Surface transport closed the
            openings, rounded the voids, and allowed neighbouring voids to coalesce into a buried
            plate-shaped cavity for suspended device layers and micromachining.
          </p>
          <p class="sd-pinchoff-lens"><strong>Pinchoff lens.</strong> Connectivity change is useful
            here rather than destructive. Crystal anisotropy and the processing environment are
            essential parts of the experiment.</p>
        </div>
        <a class="sd-paper-link" href="https://doi.org/10.1063/1.1324987">Mizushima et al., <em>Applied Physics Letters</em> <span aria-hidden="true">&nearr;</span></a>
      </article>

      <article class="sd-card">
        <figure class="sd-card-visual sd-visual-memory">
          <img
            class="sd-open-figure"
            src="{{ '/assets/img/surface-diffusion/rram-filament-lifetime-wang-2019.jpg' | relative_url }}"
            alt="Experimental switching data and a log-scale graph of silver and copper filament lifetime against initial diameter"
            loading="lazy"
          />
          <figcaption>
            Experimental retention and diameter scaling, Wang et al. (2019), Fig. 5;
            <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>. The displayed
            composite is cropped from the open figure.
          </figcaption>
        </figure>
        <div class="sd-card-body">
          <p class="sd-card-meta">Ag/Cu memory filaments · 2019</p>
          <h3>A pinching law predicts device retention</h3>
          <p>
            Conductive filaments in resistive-memory devices were measured over lifetimes from
            microseconds to years. Thin-filament lifetime followed $$\tau\sim d^4$$, whereas bulk
            out-diffusion would give $$d^2$$. Above roughly 10&ndash;14&nbsp;nm, filaments approached
            stable capillary bridges.
          </p>
          <p class="sd-pinchoff-lens"><strong>Pinchoff lens.</strong> The fourth-order clock becomes a
            reliability law: a modest change in diameter produces an enormous change in data
            retention.</p>
        </div>
        <a class="sd-paper-link" href="https://doi.org/10.1038/s41467-018-07979-0">Wang et al., <em>Nature Communications</em> <span aria-hidden="true">&nearr;</span></a>
      </article>

      <article class="sd-card">
        <figure class="sd-card-visual sd-visual-silicon-wire">
          <img
            class="sd-open-figure"
            src="{{ '/assets/img/surface-diffusion/bollani-silicon-wire-2019-fig1.jpg' | relative_url }}"
            alt="Fabrication diagram and electron micrographs of long single-crystal silicon nanowire arrays formed by templated dewetting"
            loading="lazy"
          />
          <figcaption>
            Fabrication and SEM views of long silicon wires, Bollani et al. (2019), Fig. 1;
            <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>.
          </figcaption>
        </figure>
        <div class="sd-card-body">
          <p class="sd-card-meta">Single-crystal silicon · 2019</p>
          <h3>Anisotropy can be used to avoid breakup</h3>
          <p>
            Templated dewetting turned patterned silicon films into connected, sub-millimetre-long
            crystalline wires. Facet-dependent surface energies steer the flow away from the
            Rayleigh breakup expected in an isotropic calculation.
          </p>
          <p class="sd-pinchoff-lens"><strong>Pinchoff lens.</strong> This is the counter-design: use
            crystalline anisotropy to keep a long conducting path connected instead of allowing it
            to bead up.</p>
        </div>
        <a class="sd-paper-link" href="https://doi.org/10.1038/s41467-019-13371-3">Bollani et al., <em>Nature Communications</em> <span aria-hidden="true">&nearr;</span></a>
      </article>

      <article class="sd-card">
        <figure class="sd-card-visual sd-visual-sinter">
          <img
            class="sd-open-figure"
            src="{{ '/assets/img/surface-diffusion/silver-wire-electrode-chung-2020.jpg' | relative_url }}"
            alt="Scanning electron micrographs of silver nanowire networks with four wire diameters before and after thermal annealing"
            loading="lazy"
          />
          <figcaption>
            Silver-wire networks before and after annealing, Chung, Park &amp; Lee (2020), Fig. 1;
            <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>. The displayed
            composite is cropped from the open figure.
          </figcaption>
        </figure>
        <div class="sd-card-body">
          <p class="sd-card-meta">Transparent silver electrodes · 2020</p>
          <h3>A conducting network fails wire by wire</h3>
          <p>
            Networks made from 130, 160, 225, and 320&nbsp;nm silver wires spheroidised at
            progressively higher annealing temperatures, turning continuous conducting paths into
            isolated rods and beads.
          </p>
          <p class="sd-pinchoff-lens"><strong>Pinchoff lens.</strong> A local topology change becomes
            system-level failure when the last percolating path breaks. Junction sintering and the
            substrate make the network richer than a free cylinder.</p>
        </div>
        <a class="sd-paper-link" href="https://doi.org/10.1016/j.dib.2020.105422">Chung, Park &amp; Lee, <em>Data in Brief</em> <span aria-hidden="true">&nearr;</span></a>
      </article>
    </div>

  </section>

  <section class="sd-model" aria-labelledby="sd-model-title">
    <div class="sd-section-heading">
      <p class="sd-section-number">03</p>
      <div>
        <h2 id="sd-model-title">Which model does the cold silver wire follow?</h2>
        <p>The answer is more specific&mdash;and more limited&mdash;than &ldquo;the theorem&rsquo;s equation.&rdquo;</p>
      </div>
    </div>

    <div class="sd-model-grid">
      <div class="sd-equation-card">
        <p class="sd-eyebrow">Volk&rsquo;s planar contour model</p>
        <div class="sd-equation">
          $$
          V_n=B\,\partial_s^2\kappa,
          \qquad
          B=\frac{D_s\gamma\Omega^{4/3}}{k_BT}.
          $$
        </div>
        <p>
          Curvature sets the driving force, atoms diffuse along the outline, and mass conservation
          converts the flux divergence into normal motion. The calculation set $$B=1$$, so it tested
          break locations and order, not the physical breakup time.
        </p>
      </div>

      <div class="sd-equation-card">
        <p class="sd-eyebrow">The full free-cylinder model</p>
        <div class="sd-equation">
          $$
          V_n=B_3\Delta_\Sigma H,\qquad
          \omega(k)=B_3 k^2(R_0^{-2}-k^2).
          $$
        </div>
        <p>
          Modes with $$kR_0&lt;1$$ grow. The fastest has $$kR_0=1/\sqrt2$$, hence
          $$\lambda_{\max}=2\pi\sqrt2\,R_0=4.44D$$ and
          $$\omega_{\max}=B_3/(4R_0^4)$$. The $$R_0^{-4}$$ factor is why a wire only a few
          nanometres across can evolve rapidly. Temperature enters through the Arrhenius diffusivity
          $$D_s=D_0e^{-Q_s/(k_BT)}$$.
        </p>
      </div>
    </div>

    <div class="sd-model-reading">
      <h3>What the calculation captures&mdash;and what it cannot</h3>
      <p>
        Volk and co-workers traced the projected TEM silhouette and evolved that
        <strong>two-dimensional, constant-thickness contour</strong> from its measured irregular
        shape. Breakup was declared when opposite contour segments crossed, after which the pieces
        evolved separately. The numerical area drift stayed below 4%. Reproducing several break
        locations and their order is therefore strong evidence for curvature-driven surface flux.
      </p>
      <p>
        It is not a direct test of the new theorem&rsquo;s three-dimensional law. A TEM silhouette does
        not record height; the wire rests on a 3&nbsp;nm amorphous-carbon film; crystal anisotropy is
        suppressed; repeated imaging deposits carbon. For a genuine surface, the corresponding
        isotropic equation is $$V_n=B_3\Delta_\Sigma H$$, involving both principal curvatures and the
        Laplace&ndash;Beltrami operator. A faithful next model would add anisotropic surface energy and
        mobility, the substrate contact law, and an atomistic check at only about twelve lattice
        spacings across.
      </p>
      <p>
        The change seen near 260&nbsp;K is therefore a diameter- and protocol-dependent kinetic onset,
        not a phase-transition temperature.
      </p>
    </div>

  </section>

  <section class="sd-history" aria-labelledby="sd-history-title">
    <div class="sd-section-heading">
      <p class="sd-section-number">04</p>
      <div>
        <h2 id="sd-history-title">From numerical prediction to a proved cone</h2>
        <p>Experiments establish the mechanism; computations discovered the singular shape; analysis proves it can occur.</p>
      </div>
    </div>

    <ol class="sd-history-list">
      <li>
        <time>1957&ndash;65</time>
        <div><strong>Mullins, then Nichols &amp; Mullins</strong><p>The continuum law, thermal-groove scaling, cylinder instability, and early axisymmetric computations.</p></div>
        <a href="https://doi.org/10.1063/1.1714360">source</a>
      </li>
      <li>
        <time>1995&ndash;96</time>
        <div><strong>Coleman, Falk &amp; Moakher</strong><p>Stability analysis and finite-element computations follow cylinders toward bead formation and breakup.</p></div>
        <a href="https://doi.org/10.1137/S1064827594274589">source</a>
      </li>
      <li>
        <time>1998</time>
        <div><strong>Wong et al.; Bernoff, Bertozzi &amp; Witelski</strong><p>Self-similar pinchoff calculations identify the fourth-root clock and the fundamental cone with half-angle about 46.04&deg;.</p></div>
        <a href="https://doi.org/10.1023/B:JOSS.0000033251.81126.AF">source</a>
      </li>
      <li>
        <time>2001</time>
        <div><strong>Uwe Mayer</strong><p>Three-dimensional front-tracking calculations show a dumbbell pinching and a torus tightening its inner loop toward curvature blow-up; see especially Figs. 1 and 6.</p></div>
        <a href="https://www.math.utah.edu/~mayer/math/Mayer07.pdf">author PDF</a>
      </li>
      <li>
        <time>2026</time>
        <div><strong><em>Pinchoff by surface diffusion</em></strong><p>The numerical profile is certified as an exact positive solution and embedded into an exact finite-time flow of smooth closed tori.</p></div>
        <a href="https://arxiv.org/abs/2608.21882">arXiv</a>
      </li>
    </ol>

    <aside class="sd-provenance-note">
      <p class="sd-eyebrow">About the profile image</p>
      <p>
        The earlier gallery graphic labelled &ldquo;original schematic&rdquo; was drawn for this webpage;
        it was not taken from Mayer or from an experiment, and it has been removed. The new hero is
        independently regenerated from the certified profile ODE and ends at the actual conical
        singular-time limit. Mayer&rsquo;s historically important figures are linked rather than copied
        because no reuse licence was located.
      </p>
    </aside>

  </section>

  <section class="sd-evidence" aria-labelledby="sd-evidence-title">
    <div class="sd-section-heading">
      <p class="sd-section-number">05</p>
      <div>
        <h2 id="sd-evidence-title">What the experiments establish</h2>
        <p>Evidence strengthens as independent signatures agree.</p>
      </div>
    </div>
    <ol class="sd-evidence-chain">
      <li><span>1</span><div><strong>The carrier exists.</strong><p>Individual surface atoms and atomic steps move at temperatures where the body remains solid.</p></div></li>
      <li><span>2</span><div><strong>The clock is fourth order.</strong><p>Gratings, grooves, and filaments display $$\lambda^{-4}$$, $$t^{1/4}$$, and $$d^4$$ scaling.</p></div></li>
      <li><span>3</span><div><strong>Curvature directs the mass.</strong><p>Material leaves some necks, builds others, and remains on the evolving solid to experimental accuracy.</p></div></li>
      <li><span>4</span><div><strong>Solid pinchoff occurs.</strong><p>Metal nanowires repeatedly narrow and fragment far below their melting temperatures.</p></div></li>
    </ol>
    <aside class="sd-caveat">
      <p class="sd-eyebrow">The honest boundary</p>
      <h3>Real materials are richer than the ideal equation</h3>
      <p>
        Substrates, oxide shells, crystal anisotropy, facets, impurities, grain boundaries, and TEM
        beams can all alter a measured rate or wavelength. Rayleigh-like breakup alone does not
        identify surface diffusion. The strongest case combines a kinetic exponent, conserved
        material, Arrhenius mobility, profile evolution, and direct microscopy.
      </p>
    </aside>
  </section>

  <section class="sd-theorem" aria-labelledby="sd-theorem-title">
    <div class="sd-theorem-copy">
      <p class="sd-section-number">06</p>
      <h2 id="sd-theorem-title">What the new theorem adds</h2>
      <p>
        The experiments show that surface diffusion is real and that solids pinch. They do not, by
        themselves, prove that the clean geometric evolution equation develops a singularity on a
        smooth closed surface. The theorem closes precisely that gap.
      </p>
      <ul>
        <li>a smooth embedded torus remains embedded for every $$t&lt;T$$;</li>
        <li>one waist reaches zero in finite time with $$A(t)\sim\{4\mu(T-t)\}^{1/4}$$;</li>
        <li>after rescaling, the neck converges to the classical positive conical profile;</li>
        <li>away from the pinching point, the surface converges smoothly.</li>
      </ul>
      <a class="sd-primary-link" href="https://arxiv.org/abs/2608.21882">Read <em>Pinchoff by surface diffusion</em> <span aria-hidden="true">&rarr;</span></a>
    </div>
    <div class="sd-theorem-mark" role="group" aria-label="The proven pinchoff scaling law">
      <span>waist radius</span>
      <strong>A(t)</strong>
      <span>falls on the clock</span>
      <strong>(T &minus; t)<sup>1/4</sup></strong>
      <small>and the magnified neck tends to a cone of half-angle approximately 46.04&deg;</small>
    </div>
  </section>

  <section class="sd-next" aria-labelledby="sd-next-title">
    <p class="sd-section-number">07</p>
    <div>
      <p class="sd-eyebrow">An experiment worth trying</p>
      <h2 id="sd-next-title">One measurement could connect the whole story</h2>
      <p>
        It would be really interesting to image a minimally supported nanowire, or a fabricated
        toroidal neck, throughout its final approach to rupture while recording the waist $$A(t)$$,
        the evolving profile, and the material budget together.
      </p>
      <div class="sd-next-grid">
        <div><strong>The clock</strong><span>$$A(t)^4$$ should be nearly linear in time.</span></div>
        <div><strong>Profile collapse</strong><span>$$r/A$$ against $$z/A$$ tests self-similarity.</span></div>
        <div><strong>The cone angle</strong><span>The terminal slope can be compared with 46.04&deg;.</span></div>
        <div><strong>The material ledger</strong><span>Volume should remain fixed while the outer surface stays smooth.</span></div>
      </div>
      <p class="sd-next-note">
        Seeing all four in one dataset would connect atom-scale transport, engineering failure, and
        the rigorous singularity in a single experiment.
      </p>
    </div>
  </section>

  <section class="sd-sources" aria-labelledby="sd-sources-title">
    <h2 id="sd-sources-title">Further papers and image provenance</h2>
    <p>
      Every experimental image on this page comes from an identified open-access paper, with its
      figure number and licence in the caption. Historical figures without a clear reuse licence are
      linked rather than copied. The conical profile is a reproducible numerical rendering of the
      certified equations, not a journal figure or an AI-generated image.
    </p>
    <p>
      Further experimental evidence includes
      <a href="https://doi.org/10.1007/s12274-017-1667-3">Xu, Li &amp; Lu (2018)</a> on in-situ
      atomic-scale Rayleigh instability in ultrathin gold wires and
      <a href="https://doi.org/10.1016/j.actamat.2022.118334">Haremski et al. (2022)</a> on
      anisotropic surface-diffusion-controlled grooving in nickel bicrystals. For the analytical
      prehistory, see
      <a href="https://doi.org/10.1016/S1359-6462(98)00127-4">Wong et al. (1998)</a>,
      <a href="https://doi.org/10.1023/B:JOSS.0000033251.81126.AF">Bernoff, Bertozzi &amp; Witelski (1998)</a>,
      and <a href="https://doi.org/10.14943/83525">Giga &amp; Ito (1998)</a> on pinching for planar
      curves.
    </p>
  </section>
</div>
