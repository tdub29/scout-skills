---
version: alpha
name: Biennale Yellow â€” Frame (video / frame layer)
description: >
  Video-first companion to Biennale Yellow's design.md. The unit is the frame (1920Ã—1080). Atoms
  are identical and sacred â€” warm parchment grounds, a single deep indigo ink, solar yellow deployed
  as bloom / panel / tile underprint, Instrument Serif display + Archivo sans + JetBrains Mono data,
  1px hairline rules as the only border, atmospheric depth (no shadows), and the bottom-right
  pagenum. Composition + frame scale rewritten. Restraint is the rule; motion out of scope.
unit: the frame â€” 1920Ã—1080 primary; 9:16 and 1:1 documented
principle: atoms are sacred Â· composition is free Â· numbers come from the script

colors:
  paper: "#E9E5DB"
  paper-deep: "#DCD6C4"
  sun: "#F1EE2E"
  sun-soft: "#F8F39B"
  haze: "#F0DA7C"
  ink: "#1B2566"
  ember: "#E26B4A"

typography:
  # â€” reading + data ramp â€”
  body:    { fontFamily: "Archivo", cqw: 0.85, weight: 400, lineHeight: 1.5, color: "ink" }
  body-lede:{ fontFamily: "Archivo", cqw: 0.95, weight: 400, lineHeight: 1.55 }
  micro-label:{ fontFamily: "Archivo", px: 13, weight: 600, tracking: "0.18em", upper: true }
  rail-label:{ fontFamily: "Archivo", px: 13, weight: 600, tracking: "0.32em", upper: true }
  mono-data:{ fontFamily: "JetBrains Mono", cqw: 0.73, weight: 400, tracking: "0.04em" }
  pagenum: { fontFamily: "JetBrains Mono", px: 13, weight: 400, tracking: "0.08em", opacity: 0.75 }
  # â€” display ramp (Instrument Serif 400, tight, negative tracking) â€”
  ledger-title:{ fontFamily: "Instrument Serif", cqw: 1.55, weight: 400, lineHeight: 1.15 }
  strand-title:{ fontFamily: "Instrument Serif", cqw: 1.7, weight: 400, lineHeight: 1.1 }
  headline-sm:{ fontFamily: "Instrument Serif", cqw: 2.9, weight: 400, lineHeight: 1.0 }
  headline:{ fontFamily: "Instrument Serif", cqw: 4.6, weight: 400, lineHeight: 1.06, tracking: "-0.005em" }
  date-rail:{ fontFamily: "Instrument Serif", cqw: 5.0, weight: 400, lineHeight: 0.96, tracking: "-0.005em" }
  display-it:{ fontFamily: "Instrument Serif", cqw: 7.0, weight: 400, italic: true, lineHeight: 1.04, tracking: "-0.005em" }
  numeral-md:{ fontFamily: "Instrument Serif", cqw: 7.5, weight: 400, lineHeight: 0.92, tracking: "-0.01em" }
  display:{ fontFamily: "Instrument Serif", cqw: 14.6, weight: 400, lineHeight: 0.86, tracking: "-0.018em" }
  numeral-jumbo:{ fontFamily: "Instrument Serif", cqw: 28.0, weight: 400, lineHeight: 0.84, tracking: "-0.04em" }

spacing:
  pad-edge: "4cqw"
  pad-region: "4.2cqw"
  gap-region: "2.5cqw"

components:
  sun-bloom:
    background: "radial gradient {colors.sun} core â†’ {colors.sun-soft} â†’ {colors.haze} â†’ transparent on {colors.paper}"
    size: "42â€“70% of the frame, off-center or behind the focal element"
    description: "The primary depth layer. One per frame; a flat parchment frame reads as broken."
  ember-bloom:
    background: "radial {colors.ember} at 15â€“22% opacity"
    placement: "corner opposite the sun-bloom"
    description: "Subordinate counter-temperature balance; never dominant."
  block-tile:
    backgroundColor: "{colors.sun} at 40â€“70% opacity"
    layout: "rectangles on an 8Ã—4 grid behind cover/colophon"
    description: "A layered poster underprint."
  yellow-panel:
    backgroundColor: "{colors.sun}"
    textColor: "{colors.ink}"
    rounded: "0"
    border: "none (meets paper directly)"
    description: "Full-bleed column/third â€” the strongest color statement, ink on top."
  hairline-rule:
    rule: "1px solid {colors.ink} (soft variant: {colors.ink} at 18â€“20%)"
    description: "The ONLY border â€” header underlines, footer tops, ledger separators. No thicker rule exists."
  strand-row:
    borderBottom: "1px {colors.ink} 18â€“20%"
    typography: "{typography.strand-title} + {typography.body}"
    description: "Serif numeral + serif title + sans body. Numbered editorial lists."
  ledger-row:
    borderBottom: "1px {colors.ink} 18â€“20%"
    typography: "{typography.mono-date} Â· {typography.ledger-title} Â· {typography.body} Â· {typography.mono-data}"
    description: "4-col tabular â€” mono date Â· serif title Â· sans venue Â· mono duration (right)."
  footer-band:
    borderTop: "1px solid {colors.ink} per cell"
    typography: "{typography.micro-label} + {typography.body-sm}"
    description: "4-column metadata strip at the foot of cover/colophon."
  vertical-rail:
    typography: "{typography.rail-label}"
    transform: "rotated up the left edge"
    description: "Section marker on chapter/divider frames."
  pagenum:
    typography: "{typography.pagenum}"
    color: "{colors.ink} at 75%"
    placement: "bottom-right"
    description: "The only persistent chrome."
---

# Biennale Yellow â€” Frame (video / frame layer)

## Overview

Biennale Yellow at frame scale is a **literary-editorial system** in the register of an art
biennale catalogue: warm parchment, a single deep indigo ink, and solar yellow as atmosphere. No
cards, no buttons, no shadows, no rounded corners â€” the structural vocabulary is just **paper, ink,
and yellow.** Depth is delivered by soft radial **sun blooms**, not elevation.

The voice is three faces in rigid roles: **Instrument Serif** (weight 400, tight line-height,
negative tracking) carries every display, numeral, and quote from 40px to 720px+; **Archivo** carries
body and the wide-tracked uppercase micro-label; **JetBrains Mono** carries every date, figure, and
the pagenum. Text is **always ink** â€” contrast comes from size and weight, never color. The mood
sits between a folded museum brochure and a slow-reading literary quarterly: confident, atmospheric,
deeply restrained.

**Key characteristics at frame scale:**

- **Warm parchment ground** on every frame; never white, never gray.
- **Single ink** (`{colors.ink}`) for all type and all rules; **solar yellow** as bloom / panel / tile.
- **Instrument Serif 400** display (tight, negative-tracked); **Archivo** body + micro-labels; **JetBrains Mono** data.
- **1px hairline rules** are the only border â€” no thicker weight exists; **no shadows, no rounded corners**.
- **Sun bloom** is the primary depth layer on every frame; an ember counter-bloom adds warm-cool tension.
- **Editorial-restrained** â€” sparse reads as elegant; crowding breaks the catalogue feel.

## The Frame

### Frame Craft Bar

Three eyeball tests gate every frame before any structural check:

- **Squint** â€” one Instrument Serif moment dominates at 3â€“6Ã— its neighbor; the sun bloom centers the eye.
- **Silence** â€” frames read **55â€“60% empty**; the **ledger is the one dense exception** (density via quiet hairline repetition, not richness).
- **Restraint** â€” **one ink color** for all type and rules; **one sun bloom** per frame (+ optional subordinate ember); never invert (no yellow text on ink).
- **Reference** â€” aim at an **art-biennale catalogue / slow exhibition poster / literary quarterly**; failure looks like a **flat CMS template** (no bloom) or a **bordered-card deck**.

- **Primary:** 1920Ã—1080 (16:9). Display authored in **`cqw`** (`px Ã· 1920 Ã— 100 = cqw`).
- **Vertical:** 1080Ã—1920 (9:16). **Square:** 1080Ã—1080 (1:1).
- **Safe area:** `pad-edge` 4cqw (40â€“76px equivalent) â€” the elegance depends on edge negative space; only blooms, tiles, and panels bleed.

**The container law (load-bearing).** Every frame ground sets `container-type: size`; ALL
frame-relative units are `cqw`/`cqh` against it â€” never `vw`. Hairlines stay 1px; bloom sizes scale
as `%` of the frame.

## Colors

Tokens identical to the source. `{colors.paper}` is the universal ground; `{colors.ink}` (deep
indigo navy) is **every line of type and every rule** â€” there is no secondary text color.
`{colors.sun}` deploys three ways: the **bloom** (radial atmosphere), the **yellow-panel**
(full-bleed poster fill, ink on top), and the **block-tile** underprint. `{colors.sun-soft}`/`haze`
are bloom mid/outer stops. `{colors.ember}` appears **only** as a 15â€“22% counter-bloom â€” never a
fill, never text. **The system never inverts** â€” ink on sun is correct; yellow text on ink does not exist.

## Typography

Two ramps. The **reading/data ramp** (Archivo body 0.85cqw ink, micro-labels in px, JetBrains Mono
data) carries copy + chrome; the **display ramp** (Instrument Serif `ledger-title` 1.55cqw â†’
`numeral-jumbo` 28cqw) carries every headline, numeral, and quote.

- **Legibility floor:** any load-bearing line â‰¥ **1.4cqw**; mono/labels in px are chrome only.
- **Fit-to-measure:** size the headline to its length. Cap the block at **â‰¤ 78cqw**; â‰¤3 words â†’ `display`; 4â€“6 â†’ `headline`; 7+ â†’ `headline-sm`. The jumbo numeral is a divider's whole point â€” don't shrink it.
- **Instrument Serif is weight 400 only** (its contrast is the weight signal), tight line-height (0.84â€“1.06), negative tracking; **micro-labels uppercase Archivo 600, â‰¥0.16em**; **mono for all numerals/dates**. No bold serif, no second text color, no mono in body/display.

## Depth & Surface

Atmospheric, not structural. Depth from:

- **Sun bloom** â€” the primary layer: a layered radial (sun 70â€“95% core â†’ sun-soft â†’ haze 18â€“22% â†’ paper 0%), 42â€“70% of the frame. One per frame.
- **Ember bloom** â€” a 15â€“22% peach counter-bloom in the opposite corner; always subordinate.
- **Block-tile underprint** â€” translucent yellow rectangles on an 8Ã—4 grid (cover/colophon).
- **Yellow panel** â€” the one "hard" color statement: a flooded column/third, ink on top.
- **Hairline rules** â€” 1px ink for structural separation (soft 18â€“20% variant for dense rows).

**Ceiling:** zero box-shadow, zero text-shadow, zero rounded corner, no border thicker than 1px.

## Shapes

- **0 radius on everything** â€” strict rectangles. Blooms are edgeless (they fade into paper).

## Components

- **sun-bloom / ember-bloom / block-tile** â€” the atmospheric depth set. **yellow-panel** â€” the poster-fill statement.
- **hairline-rule** â€” the only border (1px ink; soft variant for dense rows).
- **strand-row / ledger-row / footer-band** â€” the editorial list, tabular calendar, and metadata strip.
- **vertical-rail** â€” rotated chapter marker. **pagenum** â€” the bottom-right mono chrome.

## Frame Treatments

> Recipe: ground Â· container Â· composes Â· focal Â· chrome Â· accent Â· silence Â· Fixed/Free Â· density.
> A sun bloom + bottom-right pagenum on every frame; sparse is the default.

### 1 Â· Cover (identity Â· move: display + sun bloom Â· left)

**Ground** paper + a large sun-bloom (left-of-center) + an ember counter-bloom (opposite corner).
**Composes** micro-label, display, date-rail, footer-band, pagenum. **Focal** a 2-line Instrument
Serif `display` (italic key word) in ink, left, under a micro-label. **Chrome** a serif date-rail
top-right; a 4-column footer-band at the foot. **Accent** the sun bloom + yellow. **Silence** the
bloom holds the open space. **Fixed** ink type, one bloom, 1px footer rules, no shadow. **Free**
title, date, footer cells. **Density** low.

### 2 Â· Chapter Divider (section Â· move: jumbo numeral Â· vertical rail)

**Ground** paper + a corner-anchored sun-bloom. **Composes** vertical-rail, numeral-jumbo,
headline-sm. **Focal** a single huge Instrument Serif `numeral-jumbo` (â‰ˆ28cqw) dominating, with a
serif title beneath. **Chrome** a rotated vertical-rail label up the left edge; pagenum. **Accent**
the bloom behind the numeral. **Silence** ~60%. **Fixed** serif 400, jumbo numeral, rail label.
**Free** the ordinal, title, rail text. **Density** low.

### 3 Â· Ledger (catalog Â· move: hairline tabular rows Â· the dense frame)

**Ground** paper (bloom optional, subtle). **Composes** headline-sm + micro-label topbar, ledger-rows.
**Focal** a 4-column tabular calendar â€” mono date Â· serif title Â· sans venue Â· mono duration â€”
separated by hairline-soft rules under a 1px ink header rule. **Chrome** pagenum. **Accent** none â€”
density through quiet repetition, not color. **Silence** tight â€” the density exception (achieved by
repetition, not richness). **Fixed** hairline rules, mono dates, serif titles. **Free** rows, venues.
**Density** dense-exception.

### 4 Â· Manifesto / Quote (quote Â· move: italic serif Â· centered bloom)

**Ground** paper + a centered sun-bloom. **Composes** numeral-lg quote mark, display-it, attribution.
**Focal** a 2-line Instrument Serif **italic** `display-it` quote in ink, centered, under an
oversized serif quote mark. **Chrome** a micro-label attribution. **Accent** the centered bloom.
**Silence** ~60% â€” deliberately open. **Fixed** italic serif, one bloom, ink. **Free** quote,
attribution. **Density** low.

### 5 Â· Poster Panel (statement Â· move: yellow panel Â· split)

**Ground** paper with a full-bleed `{colors.sun}` `yellow-panel` (column or third). **Composes**
yellow-panel, micro-label, headline. **Focal** an Instrument Serif `headline` in ink sitting **on
the sun panel** (ink-on-yellow â€” a signature). **Chrome** micro-label; pagenum. **Accent** the panel
itself. **Silence** the paper side stays open. **Fixed** ink-on-sun, panel meets paper directly (no
border), no shadow. **Free** headline, panel side/width. **Density** low.

### 6 Â· Strand List (programme Â· move: numbered editorial rows Â· left)

**Ground** paper + a subtle sun-bloom. **Composes** micro-label, headline-sm, strand-rows. **Focal**
a numbered list â€” serif numeral + serif title + sans body, hairline-soft separators. **Chrome**
micro-label; pagenum. **Accent** the bloom. **Silence** moderate; rows breathe. **Fixed** serif
numerals, hairline-soft rules. **Free** items, copy. **Density** standard.

## Composition Rules

### Do

- Start on **warm parchment**; add **one sun bloom** (optionally an ember counter-bloom) â€” atmosphere is the depth.
- Set every line in **ink**; use **Instrument Serif 400** (tight, negative-tracked) for display, **Archivo** body, **JetBrains Mono** for all numerals/dates.
- Make every separator a **1px ink hairline** (soft variant for dense rows); flood a **yellow panel** for poster moments (ink on top).
- Keep micro-labels **uppercase Archivo 600, 0.16â€“0.32em**; pin the **pagenum** bottom-right.
- Lean sparse; left/asymmetric on cover/chapter/list, centered on manifesto.

### Don't

- No drop shadows, no rounded corners, no bordered cards, no border thicker than 1px.
- No second text color; no bold Instrument Serif; no inverted ink grounds.
- No mono for body/display; no font substitutes.
- Don't crowd the canvas â€” sparse reads as elegant; don't omit the bloom (flat parchment reads as a CMS template).
- Don't blow a headline edge-to-edge â€” step the ramp down.

## Aspect-Ratio Behavior

| Treatment       | 16:9                                           | 9:16                       | 1:1                        |
| --------------- | ---------------------------------------------- | -------------------------- | -------------------------- |
| Cover           | display left, date-rail top-right, footer foot | display top, footer stacks | display upper, footer foot |
| Chapter Divider | jumbo numeral, rail left                       | numeral centered, rail top | numeral centered           |
| Ledger          | 4-col rows                                     | drop venue col â†’ 3-col     | 3-col                      |
| Manifesto       | centered italic                                | centered, taller           | centered                   |
| Poster Panel    | side panel + paper                             | top/bottom panel band      | panel third                |
| Strand List     | numbered rows                                  | rows (tighter)             | rows                       |

`pad-edge` holds on the short edge; display clamps use the shorter axis so portrait doesn't blow out
headlines. Keep load-bearing lines â‰¥ 1.4cqw. Ledger/strand fixed first columns may tighten on 9:16.

## Approved Entities

No real customers, logos, or vendors are defined in the source â€” render any such mark as a
placeholder. Programme titles, venues, and dates are content; the system supplies paper, ink, yellow.

## Numerals & Claims (hard rule)

Never invent figures, dates, durations, or counts at frame scale. Render slots as `â€” figure â€”`,
`{metric}`, `NN JUN`, `N m`. Ledger dates/durations and chart values especially carry placeholders
until the script supplies them. Chapter ordinals (01, 02â€¦) are decorative.

## Pre-Render Self-Audit

- **Squint** â€” one serif display moment dominates; the bloom centers the eye.
- **Silence** â€” sparse frames 55â€“60% open; only the ledger runs dense (via repetition, not richness).
- **One color** â€” ink for all text + rules; sun for bloom/panel/tile; ember counter-bloom only; no inversion.
- **Type** â€” Instrument Serif 400 tight negative-tracked, fit-to-measure; micro-labels uppercase 0.16em+; mono numerals; â‰¥1.4cqw floor.
- **Depth** â€” 0 shadow, 0 rounded corner, 1px hairlines only; one sun bloom present.
- **Anchor** â€” left on cover/chapter/list, centered on manifesto; pagenum bottom-right.
- **Fabrication** â€” every numeral/date traces to the script, else placeholder.

## Known Gaps

- **Motion intentionally out of scope.** frame.md specifies composition only; the source's 280ms crossfade is a deck mechanic.
- **Instrument Serif + Archivo + JetBrains Mono via Google Fonts.** CJK: Smiley Sans (display) / Noto Serif SC (body) / Noto Sans SC (labels); italic serif and mono tabular figures have no exact Hanzi equal â€” keep ledger dates Latin.
- **9:16 / 1:1 are guidance**; the `min(vw,vh)` clamp pattern keeps display from blowing out â€” verify per ratio.
- Sun/ember blooms, block tiles, yellow panels, and hairline rules are CSS-only; no external imagery is required.
