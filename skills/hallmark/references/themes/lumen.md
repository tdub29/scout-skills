# Theme â€” Lumen

Premium AI-tool register, built around a **hand-engineered apparatus** rather than a glowing orb. One precision SVG/CSS object per page, with leader-line callouts in mono micro-type, set against dead space alongside a **lowercase classical-serif headline** and a technical mono eyebrow. Three font families. Two palette drops (Night Foundry / Day Foundry) with different physics â€” Night emits, Day refracts â€” and entirely different visual languages, not the same shape in two colours.

Lumen runs a strict **two-register typography system**: all prose is **lowercase** (hero titles, section titles, lede, body, buttons, nav, brand, footer copy â€” even acronyms when they appear in body text); all mono labels are **UPPERCASE** (eyebrows, callouts, meter labels, stat labels). The contrast between quiet lowercase prose and loud UPPERCASE machine-readout is the typographic signature.

Loaded eagerly by SKILL.md Step 3 whenever the catalog pick is `lumen`. Palettes + font stack live in [`site/css/tokens.css`](../../../../site/css/tokens.css) under `[data-theme="lumen"]` (Night, default) and `[data-theme="lumen"][data-drop="day"]` (Day). This file carries the drops + apparatus family + signature moves + motion + anti-patterns.

## Axes (diversification)

- **Paper band** â€” Night: dark cool-violet (`L 13%, H 265`). Day: light cool bone with violet pull (`L 97%, H 265`). The 265Â° hue is deliberate â€” sits 25Â° from Midnight's 250 and 65Â° from Aurora's 200, so a Lumen page is not confusable with either neighbour at a glance.
- **Display style** â€” **classical-serif-lowercase** (Instrument Serif 400, upright, **all-lowercase**, with verb landmark via accent colour + draw-in underline). No italic anywhere. Distinct from italic-serif (Specimen/Studio/Atelier ship italic as default) and from roman-serif (Newsprint uses sentence case). Lumen is the catalog's only lowercase-headline theme.
- **Accent hue** â€” Night: **molten brass** (`H 50`, not amber). Day: **deep indigo with violet tilt** (`H 268`). Coral chord (`H 18`) sits behind both as the secondary chromatic.

## Reference register

Modal Â· Anthropic (Claude product surfaces) Â· Together AI Â· ElevenLabs Â· Cluely Â· Adept Â· Granola Â· Cohere Â· Inflection Â· Linear (premium pricing pages) Â· Vercel (design guidelines, frontier-AI sections) Â· Cursor (high-fidelity product mockup heroes).

The aesthetic to match: a single hand-engineered artefact in dead space; a lowercase classical-serif headline with one accent-coloured verb; mono UPPERCASE technical labels that read as if pulled from an internal docs site; tabular numerals everywhere a number appears. The combination is what AI-tool defaults do not ship â€” and exactly the combination that breaks every default the model was trained on.

**Patron-saint reference (internal):** *Modal homepage rate sheet* (the receipt is the artwork) + *Together AI hero diagram* (annotated apparatus + leader lines + labelled callouts) + *Anthropic Claude landing typography* (transitional serif + humanist sans). When in doubt about restraint, ask "would Modal ship this much chrome?" If yes, you've gone too far.

## Palette drops

A Lumen drop is a named palette + apparatus-physics pair. The structural signature (italic-pivot headline + mono eyebrow + apparatus + leader callouts + meter strip + blueprint grid + hairline cards + three-stat row) is constant; the drop rotates the canvas, the accent, and what the apparatus *does*.

### Drop 01 Â· Night Foundry *(default Â· canonical)*

Cool-violet near-black canvas. Molten-brass accent that *emits*. The apparatus is an instrument â€” a filament-in-chamber, a circuit topology, a precision indicator â€” and it generates the light. Halos and inner-emit washes use `--color-glow` at 42% opacity.

- `--color-paper: oklch(13% 0.014 265)` â€” late-night studio, violet tilt
- `--color-ink: oklch(96% 0.006 262)` â€” near-white headlines
- `--color-accent: oklch(76% 0.17 50)` â€” molten brass
- `--color-accent-2: oklch(68% 0.16 18)` â€” coral chord
- `--color-glow: oklch(80% 0.16 50 / 0.42)` â€” dense halo
- `--color-paper-emit: oklch(76% 0.17 50 / 0.04)` â€” inner-emit canvas wash
- `--rule-blueprint: oklch(96% 0.006 262 / 0.04)` â€” grid hairline

**Apparatus physics â€” emission.** The focal element is a built object (filament, circuit, indicator dial, layered lens stack) that *contains* the light source. Subtle pulse animation (`--dur-pulse: 4s`) suggests the instrument is *running*. Card shadows are soft depth (`0 24px 60px -28px oklch(0% 0 0 / 0.55)`), not glows â€” the apparatus is the only thing that emits.

**When to pick:** inference platforms Â· serverless GPU Â· model APIs Â· AI coding agents Â· voice synthesis Â· agentic tools Â· developer infra Â· anything that wants to feel "after hours" and "instrument-grade." Default.

### Drop 02 Â· Day Foundry

Cool-bone canvas with a violet pull. Deep indigo accent that *refracts*. The apparatus is a transparent prism / lens stack / chromatic dispersion element â€” light passes through and is *separated*, not generated. Spectrum exit-fan + measurement annotations + scale bar give it the feel of a calibrated optical instrument, not a vibey gradient.

- `--color-paper: oklch(97% 0.008 265)` â€” cool bone, violet pull
- `--color-ink: oklch(18% 0.014 265)` â€” near-black, cool
- `--color-accent: oklch(46% 0.24 268)` â€” deep violet-indigo
- `--color-accent-2: oklch(68% 0.16 18)` â€” coral chord (red end of spectrum)
- `--color-glow: oklch(58% 0.22 268 / 0.28)` â€” indigo halo through prism
- `--color-paper-emit: oklch(46% 0.24 268 / 0.03)` â€” canvas wash, faint

**Apparatus physics â€” refraction.** The focal element is *static at rest* with a 320ms reveal on first paint (the prism appears, the spectrum fans, both settle). No perpetual motion. The light is captured, not generated. Annotations carry mono micro-labels: `Î» = 612 nm`, `Î¸_out = 38Â°`, etc. â€” the prism reads as a *measurement instrument*, not decoration.

**When to pick:** AI for science Â· climate / research labs Â· document AI Â· typography / design tools Â· daytime productivity Â· briefs that want "considered" and "clear" rather than "after-dark and intense."

### Drop rotation rule

The diversification log records `"theme": "lumen", "drop": "night"` (or `"day"`). Two consecutive Lumen builds must use different drops unless the brief contains a strong drop signal.

### Why two drops, not five

Lumen's identity is the apparatus, not the palette. Adding more drops would dilute what makes the theme legible. Two drops with *different physics* (emission vs refraction) carry more variety than five drops with the same artefact in different colours.

## The apparatus family

Lumen's central commitment: **never a generic glowing orb**. The orb is the most overworked AI-tool tell of 2024â€“2025; every inference platform ships one. Lumen builds a *specific* hand-engineered object per page, chosen to reflect what the product *does*.

The canonical family (pick one per build, in the order of preference for the brief):

### Apparatus type Â· Filament chamber *(Night Foundry, instrument-grade)*

A vertical glowing rod inside a rounded-rect cylindrical chamber, crossed by 3â€“4 horizontal hairline "electrodes." Subtle pulse on the filament (3% intensity oscillation, 4s period). References vacuum tubes, Tesla coils, fusion experiments, mass spectrometers. Reads as a *machine*.

**When to pick:** inference, runtime, model serving, anything that *produces* output. Brand verbs: think, run, generate, infer, render, execute.

**SVG/CSS skeleton:**

```html
<figure class="apparatus apparatus--filament" aria-hidden="true">
  <div class="chamber">
    <span class="chamber__wall"></span>
    <span class="chamber__electrode" style="--y: 22%"></span>
    <span class="chamber__electrode" style="--y: 42%"></span>
    <span class="chamber__electrode" style="--y: 62%"></span>
    <span class="chamber__electrode" style="--y: 82%"></span>
    <span class="chamber__filament"></span>
    <span class="chamber__glow"></span>
    <span class="chamber__stencil">RX-04</span>
  </div>
  <ul class="callouts">
    <li class="callout" style="--side: left; --y: 18%"><span>P50 Â· 28 ms</span></li>
    <li class="callout" style="--side: right; --y: 36%"><span>cold-start Â· 0.4 s</span></li>
    <li class="callout" style="--side: left; --y: 62%"><span>rps Â· 12 k</span></li>
    <li class="callout" style="--side: right; --y: 80%"><span>RX-04 Â· h100 80gb</span></li>
  </ul>
</figure>
```

```css
.chamber {
  position: relative; width: clamp(180px, 22vw, 280px); aspect-ratio: 0.55;
  border: 1px solid var(--color-rule-2);
  border-radius: 999px;
  background: oklch(17% 0.016 265 / 0.8);
  overflow: hidden;
}
.chamber__filament {
  position: absolute; top: 8%; bottom: 8%; left: 50%;
  width: 2px; margin-left: -1px;
  background: linear-gradient(to bottom,
    oklch(96% 0.05 50) 0%,
    oklch(80% 0.17 50) 50%,
    oklch(96% 0.05 50) 100%);
  box-shadow:
    0 0 16px 4px var(--color-glow),
    0 0 48px 12px oklch(80% 0.16 50 / 0.22);
  animation: filament-pulse var(--dur-pulse) ease-in-out infinite;
}
.chamber__electrode {
  position: absolute; left: 0; right: 0; top: var(--y);
  height: 1px; background: var(--color-rule-2);
}
.chamber__glow {
  position: absolute; inset: 0;
  background: radial-gradient(ellipse 60% 50% at 50% 50%, var(--color-glow-2) 0%, transparent 70%);
  pointer-events: none;
}
@keyframes filament-pulse {
  0%, 100% { opacity: 1; }
  50%      { opacity: 0.86; }
}
.callout {
  font-family: var(--font-mono);
  font-size: 10.5px;
  letter-spacing: var(--tracking-micro);
  text-transform: uppercase;
  color: var(--color-muted);
  position: absolute;
  /* leader-line drawn as ::before pseudo */
}
.callout::before {
  content: ""; position: absolute;
  top: 50%; height: 1px;
  background: var(--color-rule-2);
}
```

### Apparatus type Â· Codebase graph / topology *(Night Foundry)*

An annotated SVG graph: one central node + 5â€“7 satellite nodes connected by hairlines, each satellite labelled with a mono filename or symbol. Light "flows" along the connecting lines at a slow walk (subtle gradient dot moving along each path). References CAD schematics, dependency graphs, electrical circuits, knowledge graphs.

**When to pick:** AI coding agents, knowledge tools, anything that *traverses* a structured space. Brand verbs: read, trace, explore, connect.

### Apparatus type Â· Indicator dial / spectrum *(either drop)*

A circular dial (Night) or a horizontal spectrum bar with annotated wavelength labels (Day). Includes scale ticks at known increments, a moving needle or active band, and mono callouts at boundaries. References analogue gauges, oscilloscopes, audio meters.

**When to pick:** voice synthesis, audio AI, anything measuring a continuous quantity. Brand verbs: tune, measure, listen.

### Apparatus type Â· Prism + measurement *(Day Foundry canonical)*

A clip-path triangle (the prism) + an incoming beam from the left + a chromatic spectrum fan emerging from the right edge + leader-line annotations with wavelength labels and exit-angle measurements. References optical-bench experiments, atmospheric refraction diagrams, the cover of Pink Floyd's *Dark Side of the Moon* re-read as a calibrated instrument.

**When to pick:** Day Foundry default. AI for science, climate, research, document AI.

### Building rules across the family

- **Pure CSS + SVG.** Never `<img>`, never icon fonts, never SVG paths copied from Figma. The apparatus is *constructed*, not *placed*.
- **One per page.** Never two apparatus objects on a single Lumen build.
- **Leader-line callouts.** Every apparatus carries 3â€“5 mono micro-type annotations (`P50 Â· 28 ms`, `Î» = 612 nm`, `â†’ refunds.ts`) on horizontal leader lines. The callouts MUST contain real values from the brief â€” never `LOREM Â· 000`.
- **Size.** 240â€“480 px max dimension on desktop. Scales down to ~180 px on mobile but never disappears.
- **Pulse, not rotation.** Night apparatus *pulses* (3% intensity oscillation, 4s period). It does *not* rotate. Rotation was the orb's signature; the apparatus's signature is that it's clearly machined.
- **Day Foundry: no perpetual motion.** Day apparatus reveals once on first paint (320ms) and stays static. The light is captured.
- **`prefers-reduced-motion: reduce`:** all pulses freeze at maximum intensity, all reveals collapse to final state.

## The seven signature moves

A Lumen build must exhibit **all seven**. Skipping any single one is what makes the page slip back into generic-dark-AI territory.

### 1. Hand-built apparatus (no orb)

See Â§ The apparatus family above. The single most important move.

### 2. Lowercase headline with verb-landmark (no italics)

Classical Instrument Serif at `--text-display`, **all-lowercase, upright**, with **exactly one word** rendered in `--color-accent-2` (coral chord) â€” and that word is the verb. A 1px underline in the same accent draws in over 320ms on first paint and stays. **No `font-style: italic` is used anywhere** in Lumen â€” the verb landmark is built from colour + line, not from a glyph variation.

```html
<h1 class="hero__title">built to&nbsp;<em>think</em>&nbsp;in real time.</h1>
```

```css
.hero__title {
  text-transform: lowercase;  /* defensive â€” also applied at the prose level */
}
.hero__title em {
  font-style: normal;          /* explicit â€” em is repurposed as the verb landmark */
  color: var(--color-accent-2);
  position: relative;
  white-space: nowrap;
}
.hero__title em::after {
  content: ""; position: absolute;
  left: 0.05em; right: 0.05em; bottom: 0.04em;
  height: 1px;
  background: var(--color-accent-2);
  transform-origin: left;
  animation: pivot-underline 320ms var(--ease-soft) 900ms backwards;
}
@keyframes pivot-underline {
  from { transform: scaleX(0); }
  to   { transform: scaleX(1); }
}
@media (prefers-reduced-motion: reduce) {
  .hero__title em::after { animation: none; }
}
```

**Rules:** the coloured word is the verb, never a noun. One word per headline, never two. The underline is the persistent landmark â€” once drawn, never animates again. `<em>` is repurposed semantically (still emphasis), but renders without italic.

### 3. Mono eyebrow above every section

`01 Â· INFERENCE` style â€” JetBrains Mono, uppercase, 11px, tracking `0.10em`, half-opacity. Numbered roman ordinal (01, 02, 03), middle-dot separator, then the section role. Sits directly above the heading on its own line. Cap at 6 per page.

### 4. Blueprint grid background (4% opacity)

The hero `<section>` and the meter strip both carry a **ruled grid background** at 4% opacity â€” 32px or 48px square cells, single hairline in `--rule-blueprint`. This is the "engineered, not vibed" signal. Aurora has blooms; Lumen has the grid. The grid sits beneath `--color-paper-emit` so the canvas appears to emit *through* the grid lines.

```css
.hero {
  background:
    linear-gradient(var(--rule-blueprint) 1px, transparent 1px) 0 0 / 48px 48px,
    linear-gradient(90deg, var(--rule-blueprint) 1px, transparent 1px) 0 0 / 48px 48px,
    radial-gradient(60% 50% at 78% 30%, var(--color-paper-emit) 0%, transparent 65%),
    var(--color-paper);
}
```

### 5. Meter strip (below the hero)

A full-bleed 32â€“48px band beneath the hero showing 60â€“80 thin vertical ticks (1px wide, varying height/opacity). Mono labels at each end name the readout (`SIGNAL Â· 12.4 KHZ` left, `DRIFT Â· 0.04 Ïƒ` right). Reads as spectrum analyser / oscilloscope output. The values match the brief â€” never invented.

```html
<aside class="meter" aria-label="Signal readout">
  <p class="meter__label meter__label--left">SIGNAL Â· 12.4 KHZ</p>
  <div class="meter__bars">
    <!-- 64 spans, height + opacity per index -->
  </div>
  <p class="meter__label meter__label--right">DRIFT Â· 0.04 Ïƒ</p>
</aside>
```

```css
.meter {
  display: grid;
  grid-template-columns: auto 1fr auto;
  gap: 1.5rem;
  align-items: center;
  padding: 0.75rem var(--page-gutter);
  border-block: 1px solid var(--color-rule);
  font-family: var(--font-mono);
}
.meter__bars { display: flex; gap: 2px; align-items: end; height: 28px; }
.meter__bars > span {
  flex: 1; min-width: 1px;
  background: var(--color-accent);
  border-radius: 0.5px;
}
```

The meter MUST be procedurally varied â€” never a flat row of equal ticks. Heights drawn from a clean envelope (sine, gaussian, log) so the strip reads as a *measurement*, not a decorative pattern.

### 6. Hairline cards with inner emission

Cards carry a 1px hairline border in `--color-rule` and an inner radial gradient at 4â€“6% accent opacity â€” they feel **lit from within**, not dropped. On hover, inner glow brightens to 10â€“12% and the card lifts 4px. Never drop-shadow cards (the shadow Lumen uses is for elevated chrome only).

### 7. Three-stat row with Instrument Serif numerals + tabular-nums

Stats display in Instrument Serif at large size (`clamp(2.5rem, 4vw + 1rem, 4.5rem)`), `font-variant-numeric: tabular-nums`, label in mono uppercase 11px. Hairline vertical dividers. **Always three cells** â€” never two (reads as comparison), never four (reads as bento). If the brief has fewer than three honest numbers, skip the row entirely.

## Motion direction

Lumen's motion stack is **lighter than Hum, heavier than Coral**.

| Element | Motion |
|---|---|
| Apparatus (Night) | Pulse: 3% intensity oscillation, 4s period. **Never rotates.** |
| Apparatus (Day) | 320ms reveal on first paint, static thereafter. |
| Verb landmark | Color set permanently to accent-2; 1px underline draws in 320ms `delay: 900ms`. No font-style change. |
| Cards | `translateY(-4px)` + inner-glow brighten on hover, 220ms `--ease-soft`. |
| Section heads | Opacity 0â†’1 + translateY 12pxâ†’0 on view enter, 600ms, 60ms stagger. |
| Meter strip | Static. No "live" animation â€” the strip is a printed readout, not a streaming feed. |
| Scroll | Lenis optional (`duration: 0.7, lerp: 0.08`). |

**No magnetic cursors. No bento tile flips. No flashy parallax. No particle systems. No rotating orbs.** If you reach for any of these, you've drifted out of Lumen.

`prefers-reduced-motion: reduce` collapses all animations to instant final state.

## Required dependencies

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Geist:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />
```

Three families, three weights each at most. No fourth family.

## Macrostructure affinity

**Lumen loves these.**

- **Marquee Hero** â€” canonical: apparatus at hero-right, italic-pivot headline at hero-left, meter strip below
- **Workbench** â€” when the page has live product UI to show (used with annotated codebase graph)
- **Stat-Led** â€” numbers carry the story (latency, throughput)
- **Long Document** â€” technical narrative with the apparatus at hero (Day Foundry canonical)
- **Specimen** â€” only when typography is the subject

## Macrostructure rejection

**Lumen refuses these.**

- **Bento Grid** â€” too playful; Lumen is one apparatus, not a tile collage
- **Quote-Led** â€” too literary
- **Conversational FAQ** â€” too soft
- **Photographic** â€” Lumen is pure-code; no photographic anchor
- **Catalogue** â€” one apparatus, not a grid of products

## Voice fixtures

Lumen voice is **direct, technical, slightly aphoristic**. Verbs over nouns. Mono labels read as if from internal docs. No marketing-ese.

Headlines â€” **all lowercase**, with one verb in accent-2 colour (underlined):

- "built to **think** in real time."
- "inference, **rendered**."
- "a new way to **ship** models."
- "built for the people who **read** the docs."
- "models for a **moving** atmosphere."
- "code that **knows** the codebase."

Body patterns â€” also lowercase, including acronyms:

- "p50 latency at 28 ms. p99 at 84. the numbers hold under load."
- "one primitive. scales down to zero. scales up to a thousand replicas."
- "three engineers built this in fourteen weeks."

Mono eyebrows â€” UPPERCASE (these are tags, not language):

- `00 Â· INFERENCE`
- `01 Â· RUNTIME`
- `02 Â· PRICING`
- `03 Â· CHANGELOG`

Leader-line callouts (real values only) â€” UPPERCASE:

- `P50 Â· 28 MS`
- `Î› = 612 NM`
- `Î¸_OUT = 38Â°`
- `RX-04 Â· H100 80GB`
- `INDEXED Â· 412 FILES`

Brand wordmarks â€” lowercase: `cinder`, `wright`, `stratum`. Legal entity names and person names in fine print also lowercase (`cinder labs, inc.`, `maya okonkwo`). The lowercase commitment is total â€” only mono labels break it.

**Never any of:** experience, journey, elevate, curate, transform, holistic, mindful, ecosystem, platform, leverage, unlock, supercharge, revolutionize, ai-powered, intelligent.

## Anti-patterns (theme-specific)

- **NEVER a glowing CSS orb / sphere / ring.** The single most reliable AI-tool tell of 2024â€“2025. Lumen explicitly refuses it. Pick from the apparatus family or build a new precision object â€” never a generic ball of light.
- **NEVER `<img>` for the apparatus.** Pure CSS + SVG. Figma-exported SVG paths fail this â€” the apparatus is constructed in code.
- **NEVER sentence-case or title-case prose.** All headlines, lede, body, buttons, nav, captions, brand wordmarks, footer copy, person names, place names, and legal-entity names are lowercase. Mono labels are the ONLY uppercase surface (eyebrows, callouts, meter labels, stat labels). This two-register split is non-negotiable.
- **NEVER `font-style: italic` anywhere.** The previous italic-pivot signature is retired. The verb landmark is built from colour + a 1px underline, not from a glyph variation. Italic body emphasis, italic founder signatures, italic captions â€” all banned. `<em>` is repurposed as the verb landmark and renders upright.
- **Never colour-emphasise a noun.** The verb landmark is the verb. Always.
- **Never more than one accent-coloured word per headline.** Two is a marketing landing page; one is a design move.
- **Never invent stats.** If the brief has no real numbers, skip the three-stat row entirely.
- **Never re-draw browser chrome.** Real screenshots only (slop-test gate 47).
- **Never two apparatus objects on one page.** One per build.
- **Never a system font for the display.** Instrument Serif or the documented fallback chain (`"Tiempos Headline", ui-serif, Georgia, serif`).
- **Never rotate the apparatus.** Night apparatus pulses; Day apparatus is static.
- **Never accent on display text outside the verb landmark.** Headlines are ink colour with one accent-coloured verb.
- **Never emoji icons in eyebrows.** The mono ordinal + middle-dot + role label IS the eyebrow.
- **Never two-cell stat rows.** Three only.
- **Never atmospheric blooms larger than the apparatus.** The grid is the background discipline.
- **Never blank leader-callouts.** Every annotation carries a real value from the brief.

## Macrostructure pitfalls

1. **Apparatus + embedded chrome on the same side â†’ both fight for the focal point.** Pick one per side. Default: apparatus at hero-right, chrome (if any) in a later section.
2. **Italic-pivot word at a line break â†’ the verb hangs alone.** Force `&nbsp;` before and after so it stays mid-line.
3. **Stats with two cells â†’ reads as comparison.** Three only.
4. **Apparatus glow bleeds into next section â†’ page background looks washed.** Wrap in `overflow: clip` so the halo stays inside the hero.
5. **Meter strip with uniform ticks â†’ reads as decorative pattern.** Drive heights from a real envelope (sine, gaussian, log) so the strip looks measured.
6. **Card inner-radial > 8% accent opacity â†’ cards read as accent-tinted, not lit.** Cap at 6% rest / 12% hover.

## How Lumen differs from neighbouring themes

| vs | difference |
|---|---|
| **Midnight** (atmospheric, closest) | Midnight is geometric Geist on cool dark (`H 250`), no apparatus, no italic pivot, no grid. Lumen sits 25Â° hue away (`H 265`) with classical Instrument Serif, hand-built apparatus + leader callouts, blueprint grid, meter strip. The differentiation is large at every signature axis. |
| **Aurora** (atmospheric) | Aurora is cool cyan blooms on dark, Sentient serif body. Lumen is brass-on-violet apparatus + Instrument Serif headline. Different temperature, different focal-element philosophy (Aurora: ambient blooms; Lumen: built apparatus). |
| **Bloom** (atmospheric) | Bloom is warm cream paper, expressive content (Suno/Runway). Lumen is dark or cool-bone, technical content (Modal/Anthropic). Different register entirely. |
| **Atelier** (editorial) | Atelier is Playfair Display Didone on warm cream â€” luxury fashion. Lumen's Instrument Serif is a 1960s technical-journal serif. Atelier sells perfume; Lumen sells inference. |

## Test brief expectations

Lumen should be a candidate when the brief mentions:

- *inference Â· model Â· LLM Â· AI tool Â· agent Â· coding agent Â· voice Â· synthesis Â· API Â· platform Â· GPU Â· serverless Â· runtime Â· developer experience Â· DX Â· the docs Â· the console Â· pricing Â· research lab Â· atmospheric model Â· weather Â· climate*
- product categories: *AI infrastructure Â· ML platform Â· model API Â· AI dev tool Â· voice / audio AI Â· research AI Â· climate / science AI Â· agentic coding*
- emotional tone: *engineered Â· premium Â· technical Â· instrument Â· after-hours Â· considered Â· post-Modal*

Briefs that say *bakery / cafÃ© / atelier / fashion / podcast / record label / hot sauce / agency portfolio* never route to Lumen.

## Build hint

The first 22 lines of CSS should establish Lumen's anchor moves:

```css
body {
  background: var(--color-paper); color: var(--color-ink-2);
  font-family: var(--font-body);
  font-variant-numeric: tabular-nums;
  text-transform: lowercase;            /* prose default â€” the two-register foundation */
}

.eyebrow, .callout, .meter__label, .stat__label, .card__eyebrow {
  font-family: var(--font-label); font-size: 11px; letter-spacing: 0.10em;
  text-transform: uppercase;            /* mono labels are the only uppercase surface */
  color: var(--color-ink); opacity: 0.55;
}

.hero__title {
  font-family: var(--font-display); font-weight: 400;
  font-size: var(--text-display); line-height: 1.02;
  letter-spacing: -0.032em; max-width: 16ch;
}
.hero__title em {
  font-style: normal;                   /* italic is RETIRED in Lumen */
  color: var(--color-accent-2);
  position: relative; white-space: nowrap;
}

.hero {
  background:
    linear-gradient(var(--rule-blueprint) 1px, transparent 1px) 0 0 / 48px 48px,
    linear-gradient(90deg, var(--rule-blueprint) 1px, transparent 1px) 0 0 / 48px 48px,
    radial-gradient(60% 50% at 78% 30%, var(--color-paper-emit) 0%, transparent 65%),
    var(--color-paper);
}
```

The `text-transform: lowercase` on `<body>` + selective `text-transform: uppercase` on label classes is the typographic foundation. Write your HTML in normal case for accessibility (screen readers); let CSS render the lowercase. Mono labels override back to UPPERCASE.

## What Lumen refuses (restated)

Disqualifiers â€” if any appears in a Lumen build, the build is not Lumen:

- No glowing orb / sphere / ring of any kind.
- No `font-style: italic` anywhere on the page.
- No sentence-case or title-case prose â€” headlines, lede, body, buttons, nav, brand are all lowercase.
- No lowercase mono labels â€” eyebrows, callouts, meter labels are all UPPERCASE.
- No bento grids.
- No glassmorphism / `backdrop-filter` blur.
- No "trusted by" logo cloud as a full-width band.
- No three-feature-card row with icon tops.
- No emoji icons in eyebrows.
- No invented metrics.
- No re-drawn browser chrome.
- No more than one apparatus per page.
- No more than one accent-coloured word per headline.
- No system-font fallback for the display.
- No rotating apparatus (pulse only on Night; static on Day).
- No accent-coloured display text outside the verb landmark.
- No two-cell stat rows.
- No atmospheric blooms larger than the apparatus.
- No blank leader-line callouts.
