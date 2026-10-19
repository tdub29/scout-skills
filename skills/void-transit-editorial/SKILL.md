---
name: void-transit-editorial
description: "Streetwear/editorial-tech aesthetic â€” warm-paper + near-black ink on a 1px hairline spec-sheet grid, tri-accent (signal red / electric blue / acid), Inter Tight tight-tracked display over DM Mono technical labels, giant outlined numerals as texture, a fixed left rail, and scroll-driven signature interactions (pinned smootherstep hero, horizontal scroll-jacked lookbook, pointer-parallax lerp follower, shared IntersectionObserver entrance engine). Use when the ask is a bold fashion/streetwear/product drop page, a lookbook, an editorial-tech landing page, a scroll-driven campaign site, or anything described as 'Void 03', 'transit shell', 'techwear', 'award-level scroll animation', or 'spec-sheet / blueprint' styling. Ships a worked exemplar (references/void-reference.html) and a reusable AI-image method (references/image-prompts.md)."
---

# Void Transit Editorial

A single, committed aesthetic: streetwear drop page crossed with an engineering spec-sheet. Warm paper, near-black ink, hairline grid, three loud accents used sparingly, tight display type over mono labels, and heavy scroll-driven motion that still respects `prefers-reduced-motion`. The worked build is `references/void-reference.html` â€” read it when you need the exact resting values; this file teaches the reusable recipe.

## Use When
- A fashion / streetwear / techwear drop page, product launch, or lookbook.
- An editorial-tech landing page that must feel engineered, not lifestyle-soft.
- A scroll-driven campaign site ("award-level scroll animation", Awwwards energy).
- Anything the user calls "Void 03", "transit shell", "spec-sheet", or "blueprint" styling.

Not for: quiet corporate SaaS, dense dashboards, or anything needing calm restraint â€” this look is loud on purpose.

## 1. Color system

Five tokens plus one shared easing curve. Accents punctuate; they never fill.

```css
:root{
  --ink:#101010;    /* near-black â€” text, borders, ghost surfaces */
  --paper:#f3efe5;  /* warm paper â€” the default ground */
  --red:#f33a2f;    /* signal red â€” primary accent / CTAs / progress */
  --blue:#123fdd;   /* electric blue â€” secondary accent / hover flip */
  --acid:#d9ff00;   /* acid â€” rare highlight + ::selection */
  --muted:#d7d2c6;  /* warm neutral for quiet fields */
  --ease:cubic-bezier(.16,1,.3,1);  /* THE shared curve â€” every transition uses it */
  --rail:86px;      /* left side-rail width, everything offsets by it */
}
```

Rules:
- One easing curve everywhere (`var(--ease)`). Consistency of motion is the tell.
- `::selection{background:var(--acid);color:var(--ink)}` â€” the acid rarely appears elsewhere; that's what keeps it loud.
- Whole slides may flood a single accent (`.slide-two{background:var(--red)}`) but body copy stays ink-on-paper.
- Hover flips inkâ†”paper or redâ†’blue; don't introduce new hues.

## 2. Type system

Two families, opposite jobs.

- **Display â€” Inter Tight**, weights 700â€“900, tightly tracked and low line-height. Tracking runs `-.06em` to `-.15em`, `line-height` `.64`â€“`.86`. The tighter the value the more it visually crops glyphs, so pair every tight title with cap-height padding (see Â§7).
- **Technical labels â€” DM Mono**, `text-transform:uppercase`, letter-spacing `.06em`â€“`.18em`, small (8â€“11px). Everything utility â€” counters, specs, nav, footer â€” is mono.

```css
h1{font-family:'Inter Tight';font-weight:800;line-height:.72;letter-spacing:-.09em}
.eyebrow{font:500 10px/1.55 'DM Mono',monospace;text-transform:uppercase;letter-spacing:.08em}
```

**Giant outlined / transparent numerals as background texture.** Oversized drop/section numbers sit behind content as structure, drawn with `webkit-text-stroke`:

```css
.launch-visual:before{content:'03';font-size:40vw;font-weight:900;letter-spacing:-.13em;
  color:var(--paper);mix-blend-mode:screen}                 /* filled ghost numeral */
h1 span{color:transparent;-webkit-text-stroke:1.5px var(--ink)}  /* outlined word/number */
.front-type{color:transparent;-webkit-text-stroke:2px currentColor;mix-blend-mode:difference}
```

Use `clamp()` per breakpoint for these, never raw `vw` alone on semantic titles.

## 3. Layout chrome â€” the spec-sheet grid

- **Fixed left side-rail, `--rail` = 86px:** brand mark (top), a rotated vertical label (`writing-mode:vertical-rl;transform:rotate(180deg)`), and a circular counter (bottom). `main{margin-left:var(--rail)}`; the top bar and all fixed overlays start at `left:var(--rail)`.
- **Fixed top bar,** 65px, `grid-template-columns:1fr auto 1fr`, `backdrop-filter:blur(14px)` over a translucent paper, mono uppercase links.
- **1px hairline borders throughout** (`border:1px solid var(--ink)` / `border-right` / `border-top`) turn every panel into a spec-sheet cell. Sections are separated by single ink rules, not shadows or gaps.
- `body{overflow-x:clip}` â€” **`clip`, never `hidden`**. Sticky pins break if an ancestor is `overflow:hidden`; `clip` still contains horizontal bleed.

## 4. Signature interactions

Four interactions run off one `requestAnimationFrame` loop gated by a `ticking` flag and a passive scroll listener, and all are disabled when `reduceMotion` is true: (4.1) pinned smootherstep hero, (4.2) horizontal scroll-jacked lookbook, (4.3) pointer-parallax lerp follower, (4.4) shared section-entrance engine. Full code and CSS: `references/interactions.md`.

## 5. Product-photography moves

Consistent subject via an invariants paragraph, ghost-mannequin product shots, exploded flat-lay, green-screen then cutout, and the hard-shadow sticker look. Details: `references/product-photography.md`.

## 6. Film grain + scanline overlays

A fixed fractal-noise grain and an animated scanline band over media stages. Code: `references/film-grain-overlays.md`.

## 7. prefers-reduced-motion â€” non-negotiable

Every motion path has a reduced-motion off-ramp. Detect in JS (`reduceMotion` gate above) AND in CSS:

```css
@media(prefers-reduced-motion:reduce){
  html{scroll-behavior:auto}
  *,*:before,*:after{animation-duration:.001ms!important;animation-iteration-count:1!important;
    transition-duration:.001ms!important}
  .conveyor{height:auto}                     /* collapse scroll-jack to normal flow */
  .conveyor-sticky{position:relative;height:auto}
  .track{position:relative;width:auto;display:block}
  .slide{width:auto;height:100vh}
  .enter{opacity:1!important;transform:none!important;clip-path:inset(0)!important;
    filter:none!important;transition:none!important}
}
```
Also: skip the pointer-parallax and the hero first-load entrance when `reduceMotion`, and never gate content visibility on an animation that reduced-motion disables.

## 8. Display-type overflow audit (do this once)

Tight tracking plus huge sizes clips glyph ink. Log `clientWidth`/`scrollWidth` and `clientHeight`/`scrollHeight` for every large title at rest, mid-animation, and max pointer offset, and fix until each reports zero. Method and fixes: `references/type-overflow-audit.md`.


## Section blueprint (order that carries the look)
1. Pinned smootherstep hero (Â§4.1) with a product-view switcher (preload next image, fade, keep alt text).
2. Horizontal scroll-jacked lookbook (Â§4.2).
3. Commerce split â€” product info left, ghost-form image right, `clamp()` headlines, stacks on mobile.
4. Full-width system laboratory â€” exploded top-down image edge-to-edge, dark overlay, modular cards with hover lift.
5. Drop index â€” typographic table (number / name / status), hover reveals a cursor-following image preview.
6. Campaign finale â€” full dark panel on macro-cloth image, oversized wordmark, one circular CTA, complete real footer (into normal flow on mobile).

## Responsive
Recompose, don't just stack: narrow the rail, drop the top-bar mid-nav, let hero copy overlay the visual on a soft gradient so the subject stays large, make the view switcher numeric, step the lab dock 5â†’2â†’1 columns, move the footer into flow, and disable hover-only transforms under `@media(hover:none)`.

## Avoid
- `overflow:hidden` on any ancestor of a sticky pin (use `clip`).
- Direct pointer-position assignment (always the lerp follower).
- One generic fade-up for every section (use the variant engine).
- Accents as fills for body/large areas â€” they punctuate.
- Raw `vw` on semantic display type (use `clamp()` + cap-height padding).
- Any motion with no `prefers-reduced-motion` off-ramp.

## References
- `references/interactions.md`: load when implementing the hero pin, lookbook conveyor, pointer follower, or entrance engine.
- `references/product-photography.md`: load when planning or styling product imagery and cutouts.
- `references/film-grain-overlays.md`: load when adding the grain and scanline overlays.
- `references/type-overflow-audit.md`: load when auditing large display titles for clipping.
- `references/image-prompts.md`: reusable AI-asset method: the invariants paragraph, the 8-part image-prompt template, and the green-screen to cutout to verify workflow. Cross-aesthetic, use standalone.
- `references/Void03-PROMPTS.md`: load for the full original prompt recipe (brief, iteration asks, 8 image prompts, build sequence, audits).
- `references/void-reference.html`: the complete 175-line single-file build and the source of every exact value here; read it for resting states and the full CSS/JS. Treat as a static exemplar, do not execute it.
