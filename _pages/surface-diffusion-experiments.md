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
        differences in curvature. Small corrugations flatten. Grain boundaries carve grooves.
        A long, thin wire can amplify a neck until it separates.
      </p>
      <p>
        This is the laboratory story behind
        <a href="https://arxiv.org/abs/2608.21882"><em>Pinchoff by surface diffusion</em></a>:
        experiments had revealed the motion, its fourth-order clock, and many instances of
        breakup. The new theorem proves that the ideal geometric law itself can carry a smooth,
        closed surface all the way to a one-point pinching singularity.
      </p>
    </div>

    <figure class="sd-hero-figure">
      <svg viewBox="0 0 760 300" role="img" aria-labelledby="hero-svg-title hero-svg-desc">
        <title id="hero-svg-title">A solid neck evolving to pinchoff</title>
        <desc id="hero-svg-desc">Four stages show a cylindrical solid developing a narrower waist and finally separating.</desc>
        <defs>
          <linearGradient id="hero-metal" x1="0" x2="0" y1="0" y2="1">
            <stop offset="0" stop-color="#f5d7a1"/>
            <stop offset="0.48" stop-color="#c57a31"/>
            <stop offset="1" stop-color="#70411d"/>
          </linearGradient>
          <filter id="hero-glow" x="-50%" y="-50%" width="200%" height="200%">
            <feGaussianBlur stdDeviation="5"/>
          </filter>
          <marker id="hero-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
            <path d="M 0 0 L 10 5 L 0 10 z" fill="#71d8ee"/>
          </marker>
        </defs>

        <g opacity="0.28" stroke="#71d8ee" stroke-width="1">
          <path d="M20 42H740M20 96H740M20 150H740M20 204H740M20 258H740"/>
          <path d="M58 24V276M232 24V276M406 24V276M580 24V276M724 24V276"/>
        </g>

        <g transform="translate(44 0)">
          <path d="M0 110 C35 110 70 109 116 110 L116 190 C70 191 35 190 0 190 Z" fill="url(#hero-metal)"/>
          <path d="M0 110 C35 110 70 109 116 110" fill="none" stroke="#ffe4b7" stroke-width="3"/>
          <text x="58" y="226" text-anchor="middle">uniform</text>
        </g>

        <path d="M174 150H215" stroke="#71d8ee" stroke-width="3" marker-end="url(#hero-arrow)"/>

        <g transform="translate(236 0)">
          <path d="M0 103 C31 103 42 122 58 122 C74 122 87 103 116 103 L116 197 C87 197 74 178 58 178 C42 178 31 197 0 197 Z" fill="url(#hero-metal)"/>
          <path d="M0 103 C31 103 42 122 58 122 C74 122 87 103 116 103" fill="none" stroke="#ffe4b7" stroke-width="3"/>
          <text x="58" y="226" text-anchor="middle">necking</text>
        </g>

        <path d="M366 150H407" stroke="#71d8ee" stroke-width="3" marker-end="url(#hero-arrow)"/>

        <g transform="translate(428 0)">
          <path d="M0 91 C33 91 49 143 58 143 C67 143 83 91 116 91 L116 209 C83 209 67 157 58 157 C49 157 33 209 0 209 Z" fill="url(#hero-metal)"/>
          <ellipse cx="58" cy="150" rx="14" ry="32" fill="#ffca72" opacity="0.28" filter="url(#hero-glow)"/>
          <path d="M0 91 C33 91 49 143 58 143 C67 143 83 91 116 91" fill="none" stroke="#ffe4b7" stroke-width="3"/>
          <text x="58" y="226" text-anchor="middle">singular waist</text>
        </g>

        <path d="M558 150H599" stroke="#71d8ee" stroke-width="3" marker-end="url(#hero-arrow)"/>

        <g transform="translate(620 0)">
          <path d="M0 80 C30 80 43 128 51 140 L51 213 C35 210 20 218 0 218 Z" fill="url(#hero-metal)"/>
          <path d="M65 140 C73 128 86 80 116 80 L116 218 C96 218 81 210 65 213 Z" fill="url(#hero-metal)"/>
          <circle cx="58" cy="150" r="4" fill="#71d8ee"/>
          <text x="58" y="246" text-anchor="middle">pinchoff</text>
        </g>
      </svg>
      <figcaption>
        Original schematic. Surface diffusion moves material along the boundary; the body remains
        solid throughout.
      </figcaption>
    </figure>

  </section>

  <section class="sd-primer" aria-labelledby="sd-mullins-title">
    <div>
      <p class="sd-section-number">01</p>
      <h2 id="sd-mullins-title">The question, from Mullins&rsquo; point of view</h2>
    </div>
    <div class="sd-primer-copy">
      <p>
        Mullins&rsquo; theory begins with a practical materials question: how does a hot crystalline
        surface rearrange when atoms are mobile on the surface but the solid as a whole does not
        flow? The normal velocity is governed by the surface Laplacian of mean curvature. Area
        decreases, enclosed material is conserved, and the characteristic length scale changes like
        the fourth root of time.
      </p>
      <div class="sd-law" role="group" aria-label="Three experimental signatures of surface diffusion">
        <div><strong>Grooves</strong><span>width and depth &prop; t<sup>1/4</sup></span></div>
        <div><strong>Gratings</strong><span>decay rate &prop; &lambda;<sup>&minus;4</sup></span></div>
        <div><strong>Filaments</strong><span>lifetime &prop; d<sup>4</sup></span></div>
      </div>
      <p>
        The same law that erases a short-wavelength scratch destabilises a sufficiently long wave on
        a cylinder. In the isotropic linear theory the fastest mode has wavelength
        \(2\pi\sqrt{2}R\approx 4.44D\). The engineering endpoint is not merely smoothing: it is
        loss of a load-bearing path, an electrical connection, or an entire component through
        pinchoff.
      </p>
    </div>
  </section>

  <section class="sd-gallery-section" aria-labelledby="sd-gallery-title">
    <div class="sd-section-heading">
      <p class="sd-section-number">02</p>
      <div>
        <h2 id="sd-gallery-title">Eight experiments, one accumulating case</h2>
        <p>
          No single movie identifies the mechanism. Together, direct atom motion, conserved mass,
          fourth-order scaling, and repeatable neck formation make the case compelling.
        </p>
      </div>
    </div>

    <h3 class="sd-chapter"><span>Measure the law</span></h3>
    <div class="sd-card-grid">
      <article class="sd-card">
        <figure class="sd-card-visual sd-visual-copper">
          <svg viewBox="0 0 640 360" role="img" aria-labelledby="groove-title groove-desc">
            <title id="groove-title">Copper grain-boundary groove</title>
            <desc id="groove-desc">A sequence of surface profiles shows a groove deepening at a vertical grain boundary.</desc>
            <defs>
              <linearGradient id="cu-ground" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#d7934f"/><stop offset="1" stop-color="#71401d"/></linearGradient>
            </defs>
            <rect width="640" height="360" fill="#14232a"/>
            <path d="M0 116 H280 Q320 116 320 144 Q320 116 360 116 H640 V360 H0Z" fill="url(#cu-ground)" opacity="0.4"/>
            <path d="M0 116 H279 Q320 116 320 145 Q320 116 361 116 H640" fill="none" stroke="#f7d29b" stroke-width="5"/>
            <path d="M0 106 H272 Q320 106 320 176 Q320 106 368 106 H640" fill="none" stroke="#efa24f" stroke-width="7"/>
            <path d="M0 96 H262 Q320 96 320 222 Q320 96 378 96 H640" fill="none" stroke="#ff6e50" stroke-width="8"/>
            <path d="M320 48V330" stroke="#77d7e5" stroke-width="2" stroke-dasharray="7 8"/>
            <text x="30" y="52">same shape after rescaling</text>
            <text x="336" y="314" class="sd-svg-small">grain boundary</text>
            <text x="505" y="136" class="sd-svg-small">early</text>
            <text x="505" y="174" class="sd-svg-small">later</text>
            <text x="505" y="218" class="sd-svg-small">latest</text>
          </svg>
          <figcaption>Original schematic of the measured profile sequence.</figcaption>
        </figure>
        <div class="sd-card-body">
          <p class="sd-card-meta">Copper · 1959</p>
          <h3>Thermal grooves keep the predicted shape</h3>
          <p>
            Copper bicrystals were annealed in dry hydrogen at 930&nbsp;&deg;C and 1035&nbsp;&deg;C.
            The groove at a grain boundary retained a self-similar profile while both its width and
            depth grew as \(t^{1/4}\).
          </p>
          <p class="sd-pinchoff-lens"><strong>Pinchoff lens.</strong> This is the classic macroscopic
            measurement of the fourth-order clock that also governs a collapsing waist.</p>
        </div>
        <a class="sd-paper-link" href="https://doi.org/10.1016/0001-6160(59)90069-0">Mullins &amp; Shewmon, <em>Acta Metallurgica</em> <span aria-hidden="true">&nearr;</span></a>
      </article>

      <article class="sd-card">
        <figure class="sd-card-visual sd-visual-silicon">
          <svg viewBox="0 0 640 360" role="img" aria-labelledby="grating-title grating-desc">
            <title id="grating-title">Silicon grating flattening</title>
            <desc id="grating-desc">Three sinusoidal surface gratings with the same wavelength have successively smaller amplitude.</desc>
            <rect width="640" height="360" fill="#101f2e"/>
            <g fill="none" stroke-linecap="round">
              <path d="M40 78 C80 30 120 30 160 78 S240 126 280 78 S360 30 400 78 S480 126 520 78 S600 30 640 78" stroke="#ffcb68" stroke-width="8"/>
              <path d="M40 182 C80 150 120 150 160 182 S240 214 280 182 S360 150 400 182 S480 214 520 182 S600 150 640 182" stroke="#73d9e7" stroke-width="7"/>
              <path d="M40 284 C80 272 120 272 160 284 S240 296 280 284 S360 272 400 284 S480 296 520 284 S600 272 640 284" stroke="#c79cff" stroke-width="6"/>
            </g>
            <g class="sd-svg-small">
              <text x="42" y="38">t = 0</text><text x="42" y="148">later</text><text x="42" y="252">latest</text>
            </g>
            <path d="M485 133H605" stroke="#f7fafc" stroke-width="2"/>
            <path d="M485 124V142M605 124V142" stroke="#f7fafc" stroke-width="2"/>
            <text x="545" y="121" text-anchor="middle" class="sd-svg-small">wavelength &lambda;</text>
          </svg>
          <figcaption>Original schematic of periodic grating decay.</figcaption>
        </figure>
        <div class="sd-card-body">
          <p class="sd-card-meta">Silicon (001) · 1994</p>
          <h3>A fourth-power mechanism test</h3>
          <p>
            Etched silicon gratings were annealed between 800&nbsp;&deg;C and 1100&nbsp;&deg;C. Their
            amplitudes decayed exponentially and the decay rate scaled approximately as
            \(\lambda^{-4}\); scanning tunnelling microscopy also resolved the evolving atomic
            steps.
          </p>
          <p class="sd-pinchoff-lens"><strong>Pinchoff lens.</strong> Competing transport laws predict
            different powers. This experiment cleanly identifies surface diffusion, although the
            geometry stays graphical and never breaks.</p>
        </div>
        <a class="sd-paper-link" href="https://doi.org/10.1016/0022-3697(94)90116-3">Keeffe, Umbach &amp; Blakely, <em>JPCS</em> <span aria-hidden="true">&nearr;</span></a>
      </article>
    </div>

    <h3 class="sd-chapter"><span>Watch a neck fail</span></h3>
    <div class="sd-card-grid">
      <article class="sd-card">
        <figure class="sd-card-visual sd-visual-wire">
          <svg viewBox="0 0 640 360" role="img" aria-labelledby="cuwire-title cuwire-desc">
            <title id="cuwire-title">Copper nanowire breaking into spheres</title>
            <desc id="cuwire-desc">A uniform nanowire becomes periodically necked and then a row of spheres.</desc>
            <rect width="640" height="360" fill="#182229"/>
            <defs><linearGradient id="cu-wire" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#ffe0aa"/><stop offset="0.5" stop-color="#cb7d34"/><stop offset="1" stop-color="#6f3c1a"/></linearGradient></defs>
            <rect x="42" y="52" width="556" height="44" rx="22" fill="url(#cu-wire)"/>
            <path d="M42 164 C78 142 104 142 140 164 C176 186 202 186 238 164 C274 142 300 142 336 164 C372 186 398 186 434 164 C470 142 496 142 532 164 C560 181 580 182 598 174 L598 226 C562 246 536 246 500 224 C464 202 438 202 402 224 C366 246 340 246 304 224 C268 202 242 202 206 224 C170 246 144 246 108 224 C80 207 60 206 42 214Z" fill="url(#cu-wire)"/>
            <g fill="url(#cu-wire)">
              <circle cx="95" cy="305" r="35"/><circle cx="245" cy="305" r="35"/><circle cx="395" cy="305" r="35"/><circle cx="545" cy="305" r="35"/>
            </g>
            <g fill="#74d9e8"><path d="M318 111l-9 15h18z"/><path d="M318 246l-9-15h18z"/></g>
            <text x="336" y="139" class="sd-svg-small">mass leaves the neck</text>
          </svg>
          <figcaption>Original schematic of constriction and sphere-chain formation.</figcaption>
        </figure>
        <div class="sd-card-body">
          <p class="sd-card-meta">Copper nanowires · 2004</p>
          <h3>The geometric prediction lands on the numbers</h3>
          <p>
            Wires 30&ndash;50&nbsp;nm across were annealed at 400&ndash;600&nbsp;&deg;C and evolved from
            constrictions to shorter rods and then spheres. For a 38&nbsp;nm wire, the measured
            spacing was \(165\pm57\)&nbsp;nm and sphere diameter \(73\pm9\)&nbsp;nm; the
            surface-diffusion model predicted 169&nbsp;nm and 73&nbsp;nm.
          </p>
          <p class="sd-pinchoff-lens"><strong>Pinchoff lens.</strong> This is the cleanest classical
            match between a visible solid-state breakup and the wavelength and volume bookkeeping
            of the Mullins&ndash;Nichols instability.</p>
        </div>
        <a class="sd-paper-link" href="https://doi.org/10.1063/1.1826237">Toimil Molares et al., <em>Applied Physics Letters</em> <span aria-hidden="true">&nearr;</span></a>
      </article>

      <article class="sd-card">
        <figure class="sd-card-visual sd-visual-silver">
          <svg viewBox="0 0 640 360" role="img" aria-labelledby="agwire-title agwire-desc">
            <title id="agwire-title">Ultrathin silver nanowire observed by cryogenic microscopy</title>
            <desc id="agwire-desc">A nanoscale wire profile and thermometer show neck growth beginning near 260 kelvin.</desc>
            <rect width="640" height="360" fill="#17232f"/>
            <g stroke="#edf4f5" fill="none" stroke-linecap="round">
              <path d="M52 166 C108 128 142 203 202 164 C261 126 293 205 355 164 C415 124 447 205 508 163 C546 137 570 144 598 162" stroke-width="28" opacity="0.22"/>
              <path d="M52 166 C108 128 142 203 202 164 C261 126 293 205 355 164 C415 124 447 205 508 163 C546 137 570 144 598 162" stroke="#dce8ec" stroke-width="12"/>
            </g>
            <g transform="translate(72 245)">
              <rect x="0" y="0" width="450" height="18" rx="9" fill="#3b4d59"/>
              <rect x="0" y="0" width="292" height="18" rx="9" fill="#70d5e7"/>
              <path d="M292 -12V35" stroke="#ffcb67" stroke-width="4"/>
              <text x="292" y="58" text-anchor="middle">~260 K: breakup begins</text>
              <text x="0" y="58">77 K</text><text x="425" y="58">300 K</text>
            </g>
            <circle cx="391" cy="162" r="34" fill="none" stroke="#ffcb67" stroke-width="3" stroke-dasharray="6 7"/>
            <path d="M415 136L468 84" stroke="#ffcb67" stroke-width="3"/>
            <text x="476" y="80">predicted</text><text x="476" y="102">break point</text>
          </svg>
          <figcaption>Original schematic of the cryo-TEM experiment.</figcaption>
        </figure>
        <div class="sd-card-body">
          <p class="sd-card-meta">Pristine silver nanowires · 2015</p>
          <h3>A solid wire breaks below room temperature</h3>
          <p>
            Solvent- and template-free silver wires, about 5&nbsp;nm in diameter, were followed by
            cryogenic TEM. Smoothing and neck growth began near 260&nbsp;K. A Mullins calculation,
            initialised from the measured contour, reproduced where the real wire later broke.
          </p>
          <p class="sd-pinchoff-lens"><strong>Pinchoff lens.</strong> The experiment removes the idea
            that breakup requires melting. Substrate effects, anisotropy, and carbon deposited by
            repeated imaging still perturb the ideal equation.</p>
        </div>
        <a class="sd-paper-link" href="https://doi.org/10.1039/C5CP04696C">Volk et al., <em>Physical Chemistry Chemical Physics</em> <span aria-hidden="true">&nearr;</span></a>
      </article>

      <article class="sd-card">
        <figure class="sd-card-visual sd-visual-atomic">
          <img
            class="sd-open-figure"
            src="{{ '/assets/img/surface-diffusion/silver-step-migration-yin-2021.jpg' | relative_url }}"
            alt="Sequential transmission electron microscopy frames showing surface steps migrating along a silver nanowire, beside the measured stress-strain curve"
            loading="lazy"
          />
          <figcaption>
            Experimental TEM sequence. Yin et al. (2021),
            <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>; cropped to fit.
          </figcaption>
        </figure>
        <div class="sd-card-body">
          <p class="sd-card-meta">Silver nanowires · 2021</p>
          <h3>Surface steps walk across a crystalline solid</h3>
          <p>
            Sequential atomic-resolution TEM images track surface steps migrating along a silver
            nanowire while the interior remains crystalline. The motion supplies a direct microscopic
            view of the transport inferred from the larger-scale shape laws.
          </p>
          <p class="sd-pinchoff-lens"><strong>Pinchoff lens.</strong> This experiment makes the carrier
            of the geometric law visible. Tensile loading, dislocations, and the electron beam are
            also present, so it establishes atomic mobility rather than unforced pinchoff by itself.</p>
        </div>
        <a class="sd-paper-link" href="https://doi.org/10.1038/s41467-021-25542-2">Yin et al., <em>Nature Communications</em> <span aria-hidden="true">&nearr;</span></a>
      </article>
    </div>

    <h3 class="sd-chapter"><span>Use the motion — or design against it</span></h3>
    <div class="sd-card-grid">
      <article class="sd-card">
        <figure class="sd-card-visual sd-visual-void">
          <svg viewBox="0 0 640 360" role="img" aria-labelledby="void-title void-desc">
            <title id="void-title">Silicon holes reorganising into a buried cavity</title>
            <desc id="void-desc">Vertical holes close at the surface and coalesce below into a plate-shaped empty cavity.</desc>
            <rect width="640" height="360" fill="#11202b"/>
            <path d="M0 84H640V360H0Z" fill="#77858c"/>
            <path d="M0 84H640" stroke="#d8e1e4" stroke-width="7"/>
            <g fill="#11202b" stroke="#a9edf4" stroke-width="3">
              <path d="M100 84V218Q100 248 130 248Q160 248 160 218V84Z"/>
              <path d="M218 84V218Q218 248 248 248Q278 248 278 218V84Z"/>
              <path d="M336 84V218Q336 248 366 248Q396 248 396 218V84Z"/>
            </g>
            <path d="M485 228 C505 192 563 192 583 228 C563 264 505 264 485 228Z" fill="#11202b" stroke="#ffcd68" stroke-width="4"/>
            <path d="M414 228H465" stroke="#75dbe8" stroke-width="4" marker-end="url(#void-arrow)"/>
            <defs><marker id="void-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#75dbe8"/></marker></defs>
            <text x="188" y="45" text-anchor="middle">patterned holes</text>
            <text x="534" y="45" text-anchor="middle">buried empty space</text>
            <text x="534" y="300" text-anchor="middle" class="sd-svg-small">surface closes; volume remains</text>
          </svg>
          <figcaption>Original schematic of silicon-on-nothing fabrication.</figcaption>
        </figure>
        <div class="sd-card-body">
          <p class="sd-card-meta">Silicon-on-nothing · 2000</p>
          <h3>Topology change becomes a fabrication method</h3>
          <p>
            Patterned holes in silicon were annealed in hydrogen. Surface transport closed the
            openings, rounded the voids, and allowed nearby voids to coalesce into a buried,
            plate-shaped cavity&mdash;useful for suspended device layers and micromachining.
          </p>
          <p class="sd-pinchoff-lens"><strong>Pinchoff lens.</strong> Here a deliberately prepared
            surface is allowed to change connectivity. Crystallographic anisotropy and the hydrogen
            environment are essential parts of the real experiment.</p>
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
            Experimental retention and diameter scaling. Wang et al. (2019),
            <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>; cropped to fit.
          </figcaption>
        </figure>
        <div class="sd-card-body">
          <p class="sd-card-meta">Ag/Cu memory filaments · 2019</p>
          <h3>A pinching law predicts device retention</h3>
          <p>
            Conductive filaments in resistive-memory devices were measured over lifetimes from
            microseconds to years. Thin-filament lifetime followed \(\tau\sim d^4\), whereas bulk
            out-diffusion would give \(d^2\). Above roughly 10&ndash;14&nbsp;nm, filaments approached
            stable capillary bridges.
          </p>
          <p class="sd-pinchoff-lens"><strong>Pinchoff lens.</strong> The fourth-order clock becomes a
            reliability law: a modest change in diameter produces an enormous change in data
            retention.</p>
        </div>
        <a class="sd-paper-link" href="https://doi.org/10.1038/s41467-018-07979-0">Wang et al., <em>Nature Communications</em> <span aria-hidden="true">&nearr;</span></a>
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
            Silver-wire networks before and after annealing. Chung, Park &amp; Lee (2020),
            <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>; cropped to fit.
          </figcaption>
        </figure>
        <div class="sd-card-body">
          <p class="sd-card-meta">Transparent silver electrodes · 2020</p>
          <h3>A conducting network fails wire by wire</h3>
          <p>
            Annealed silver-nanowire electrodes reveal a stark diameter effect. Networks made from
            130, 160, 225, and 320&nbsp;nm wires spheroidised at progressively higher temperatures,
            turning continuous conducting paths into isolated rods and beads.
          </p>
          <p class="sd-pinchoff-lens"><strong>Pinchoff lens.</strong> A local topological event becomes
            a system-level failure when the last percolating path breaks. Junction sintering and the
            substrate make a network more complicated than an isolated free wire.</p>
        </div>
        <a class="sd-paper-link" href="https://doi.org/10.1016/j.dib.2020.105422">Chung, Park &amp; Lee, <em>Data in Brief</em> <span aria-hidden="true">&nearr;</span></a>
      </article>
    </div>

  </section>

  <section class="sd-evidence" aria-labelledby="sd-evidence-title">
    <div class="sd-section-heading">
      <p class="sd-section-number">03</p>
      <div>
        <h2 id="sd-evidence-title">What the experiments establish</h2>
        <p>Evidence strengthens as independent signatures agree.</p>
      </div>
    </div>
    <ol class="sd-evidence-chain">
      <li><span>1</span><div><strong>The carrier exists.</strong><p>Individual surface atoms and atomic steps move at temperatures where the body remains solid.</p></div></li>
      <li><span>2</span><div><strong>The clock is fourth order.</strong><p>Gratings, grooves, and filaments display \(\lambda^{-4}\), \(t^{1/4}\), and \(d^4\) scaling.</p></div></li>
      <li><span>3</span><div><strong>Curvature directs the mass.</strong><p>Material leaves some necks, builds others, and conserves volume to experimental accuracy.</p></div></li>
      <li><span>4</span><div><strong>Solid pinchoff occurs.</strong><p>Metal nanowires repeatedly narrow and fragment well below their melting temperatures.</p></div></li>
    </ol>
    <aside class="sd-caveat">
      <p class="sd-eyebrow">The honest boundary</p>
      <h3>Real materials are richer than the ideal equation</h3>
      <p>
        Substrates, oxide shells, crystal anisotropy, facets, impurities, grain boundaries, and TEM
        beams can all alter a measured rate or selected wavelength. Rayleigh-like breakup alone does
        not prove surface diffusion. The strongest identification combines a kinetic exponent,
        conserved material, Arrhenius mobility, profile evolution, and direct microscopy.
      </p>
    </aside>
  </section>

  <section class="sd-theorem" aria-labelledby="sd-theorem-title">
    <div class="sd-theorem-copy">
      <p class="sd-section-number">04</p>
      <h2 id="sd-theorem-title">What the new theorem adds</h2>
      <p>
        The experiments show that surface diffusion is real and that solids pinch. They do not, by
        themselves, prove that the clean geometric evolution equation develops a singularity on a
        smooth closed surface. The theorem closes precisely that gap.
      </p>
      <ul>
        <li>a smooth embedded torus remains embedded for every \(t&lt;T\);</li>
        <li>one waist reaches zero in finite time with \(A(t)\sim\{4\mu(T-t)\}^{1/4}\);</li>
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
      <small>and the magnified neck tends to a cone of opening angle approximately 46.04&deg;</small>
    </div>
  </section>

  <section class="sd-next" aria-labelledby="sd-next-title">
    <p class="sd-section-number">05</p>
    <div>
      <p class="sd-eyebrow">The next decisive experiment</p>
      <h2 id="sd-next-title">Test the whole pinchoff fingerprint at once</h2>
      <p>
        A minimally supported nanowire, or a fabricated toroidal neck, could be imaged through its
        final approach to rupture. Measure the waist \(A(t)\), the evolving profile, and the material
        budget simultaneously.
      </p>
      <div class="sd-next-grid">
        <div><strong>Linearise the clock</strong><span>Plot \(A(t)^4\) against time.</span></div>
        <div><strong>Collapse the profiles</strong><span>Plot \(r/A\) against \(z/A\).</span></div>
        <div><strong>Measure the cone</strong><span>Look for the 46.04&deg; limiting angle.</span></div>
        <div><strong>Close the ledger</strong><span>Verify conserved material and a smooth outer surface.</span></div>
      </div>
      <p class="sd-next-note">
        That would connect atom-scale transport, the engineering failure, and the rigorous singularity
        in one experiment.
      </p>
    </div>
  </section>

  <section class="sd-sources" aria-labelledby="sd-sources-title">
    <h2 id="sd-sources-title">Sources and image note</h2>
    <p>
      Historical and explanatory visuals are original schematics. Three experimental composites are
      reproduced from open-access papers under CC BY 4.0, with attribution in their captions. Follow
      each paper link for the uncropped figures and full methodology. Additional direct pinchoff
      imaging appears in <a href="https://doi.org/10.1007/s12274-017-1667-3">Xu, Li &amp; Lu (2018)</a>;
      comparative evidence is available in the multi-material nanowire study of
      <a href="https://doi.org/10.1039/C7CP00463J">Schnedlitz et al. (2017)</a> and the modern nickel
      grooving study of <a href="https://doi.org/10.1016/j.actamat.2022.118334">Haremski et al. (2022)</a>.
    </p>
  </section>
</div>
