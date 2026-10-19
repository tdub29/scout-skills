---
version: alpha
name: Cobalt Grid â€” Frame (video / frame layer)
description: >
  Video-first companion to Cobalt Grid's design.md. The unit is the frame (1920Ã—1080). Atoms
  are identical and sacred â€” warm cream paper, electric cobalt ink (the only ink), the permanent
  graph-paper grid, Newsreader serif 400 + Hanken Grotesk + DM Mono, the top/bottom cobalt
  hairlines, and the pixel-glitch + QR-block signatures. Composition, frame scale, and
  aspect-ratio behavior are rewritten for the frame. Motion is out of scope.
unit: the frame â€” 1920Ã—1080 primary; 9:16 and 1:1 documented
principle: atoms are sacred Â· composition is free Â· numbers come from the script

colors:
  paper: "#F0EBDE"
  paper-2: "#E6E0CE"
  ink: "#1F2BE0"
  ink-soft: "#5560E5"
  grid: "rgba(31,43,224,0.10)"
  ink-faint: "rgba(31,43,224,0.18)"

typography:
  # â€” reading ramp â€”
  body:        { fontFamily: "Hanken Grotesk", cqw: 0.83, weight: 400, lineHeight: 1.5 }
  body-lede:   { fontFamily: "Hanken Grotesk", cqw: 0.95, weight: 400, lineHeight: 1.5 }
  micro:       { fontFamily: "Hanken Grotesk", px: 13, weight: 600, tracking: "0.16em", upper: true }
  micro-strong:{ fontFamily: "Hanken Grotesk", px: 16, weight: 600, tracking: "0.18em", upper: true }
  mono-tag:    { fontFamily: "DM Mono", cqw: 0.78, weight: 400, tracking: "0.05em" }
  mono-chrome: { fontFamily: "DM Mono", px: 13, weight: 400, tracking: "0.06em" }
  # â€” display / hero ramp (Newsreader 400, negative tracking) â€”
  table-name:  { fontFamily: "Newsreader", cqw: 1.5, weight: 400, lineHeight: 1.15 }
  row-headline:{ fontFamily: "Newsreader", cqw: 2.1, weight: 400, lineHeight: 1.05 }
  ed-callout:  { fontFamily: "Newsreader", cqw: 2.6, weight: 400, lineHeight: 1.1, italic: true }
  headline:    { fontFamily: "Newsreader", cqw: 4.6, weight: 400, lineHeight: 0.95 }
  headline-index:{ fontFamily: "Newsreader", cqw: 5.0, weight: 400, lineHeight: 0.95 }
  display-quote:{ fontFamily: "Newsreader", cqw: 5.7, weight: 400, lineHeight: 1.05, tracking: "-0.005em" }
  display-chapter:{ fontFamily: "Newsreader", cqw: 6.8, weight: 400, lineHeight: 1.0, tracking: "-0.005em" }
  display-closing:{ fontFamily: "Newsreader", cqw: 9.4, weight: 400, lineHeight: 0.96, tracking: "-0.005em" }
  display-hero:{ fontFamily: "Newsreader", cqw: 10.4, weight: 400, lineHeight: 0.9, tracking: "-0.008em" }
  vbig-numeral:{ fontFamily: "Newsreader", cqw: 12.5, weight: 400, lineHeight: 0.9, tracking: "-0.015em" }

spacing:
  edge: "4cqw"          # standard frame edge inset (~80px@1920)
  pad-top: "7cqw"
  pad-bottom: "6cqw"
  gap-md: "2cqw"

components:
  graph-grid:
    backgroundImage: "linear-gradient grid, ~2cqw cells, 10% {colors.ink} ({colors.grid})"
    placement: "behind EVERY frame on the ground"
    description: "Permanent graph-paper grid â€” never disabled; the canvas tone."
  hairlines:
    rule: "0.12cqw solid {colors.ink}"
    placement: "â‰ˆ3cqw from top + bottom, inset {spacing.edge}"
    description: "Two persistent cobalt rules framing every composition."
  page-chrome:
    typography: "{typography.pagenum}"
    color: "{colors.ink}"
    placement: "page number bottom-right, nav/meta hint bottom-left, above the bottom hairline"
    description: "The only persistent chrome."
  pixel-glitch:
    backgroundColor: "{colors.paper}"
    fill: "repeating-linear-gradient(90deg, {colors.ink} 0 2px, transparent 2px 8px)"
    size: "14â€“30cqw wide, full height, stair-stepped"
    placement: "right on cover/data, left on chapter/colophon; z above grid, below headline"
    description: "Stair-stepped scanline column. Decorative."
  qr-block:
    backgroundColor: "{colors.paper}"
    cells: "8Ã—8, {colors.ink} on / {colors.grid} off"
    size: "3â€“9cqw square"
    shadow: "0 0 0 0.12cqw {colors.paper} (anti-shadow for readability, not elevation)"
    description: "QR mosaic patch â€” corner punctuation."
  topbar-rule:
    typography: "{typography.headline-index} + {typography.mono-tag}"
    borderBottom: "0.12cqw solid {colors.ink}"
    description: "Section header on index/data/table frames."
  ledger-row:
    layout: "grid: mono num Â· Newsreader name Â· Hanken desc Â· mono delta"
    borderBottom: "0.06cqw solid {colors.ink-faint} (header 0.12cqw solid {colors.ink})"
    typography: "{typography.mono-tag} + {typography.table-name} + {typography.body}"
    description: "Dense matrix row with â†‘/â†“/â€” delta."
  pixel-stack-bar:
    cells: "column-reverse, {colors.grid} off / {colors.ink} on"
    baseline: "0.12cqw solid {colors.ink} + {typography.mono-tick} ticks"
    description: "Data as grid-unit cells; echoes the glitch."
  vstack-label:
    typography: "{typography.mono-tick}"
    transform: "writing-mode: vertical-rl"
    description: "Catalogue chrome along a frame edge."
---

# Cobalt Grid â€” Frame (video / frame layer)

## Overview

Cobalt Grid at frame scale is a **two-color risograph trend-report** â€” warm cream paper, electric
cobalt ink, and a **permanent graph-paper grid** behind every frame. Cobalt is the _only_ ink:
headlines, body, rules, the grid, the pixel-glitch decoration, the QR patches. There is no accent
color and no second surface.

The voice is a three-face conversation: **Newsreader** serif at weight 400 (size, not weight,
makes hierarchy) carries every display and headline; **Hanken Grotesk** carries body and
uppercase tracked labels; **DM Mono** carries all chrome â€” page numbers, tags, ticks, vertical
stacks. Every frame is framed by top + bottom cobalt hairlines; declarative frames carry the
**pixel-glitch column** and a **QR-block** patch.

**Key characteristics at frame scale:**

- **Strictly two-color** â€” cream paper + cobalt ink; no accent, no second surface.
- **Permanent ~2cqw graph-paper grid** (10% cobalt) behind every frame; cannot be disabled.
- **Top + bottom 1.5px cobalt hairlines** frame every composition, inset by `edge`.
- **Newsreader 400** for all display (negative tracking); **Hanken 600** uppercase 0.16em labels; **DM Mono** chrome.
- **Pixel-glitch column + QR-block** as the signature decorative patches on declarative frames.
- **Pixel-stack bars** render data as grid-unit cells (cobalt on / 10% off).

## The Frame

### Frame Craft Bar

Three eyeball tests gate every frame before any structural check:

- **Squint** â€” one Newsreader element dominates at **3â€“6Ã— its nearest neighbor** (`display-hero`/`vbig-numeral`); hierarchy is size, never weight.
- **Silence** â€” declarative frames (cover, chapter, quote, colophon) read **45â€“60% empty** with the grid showing; the **index ledger and data frame are the one dense exception** (density via quiet repetition, not richness).
- **Restraint** â€” **two-color only** (cream + cobalt, never a second hue); one pixel-glitch column and at most one QR-block per declarative frame.
- **Reference** â€” aim at a **WIRED Japan / Shift two-color risograph monograph**; failure looks like a **colorful dashboard with a second accent hue**.

- **Primary:** 1920Ã—1080 (16:9). Display authored in **`cqw`** (`px Ã· 1920 Ã— 100 = cqw`).
- **Vertical:** 1080Ã—1920 (9:16). **Square:** 1080Ã—1080 (1:1).
- **Safe area:** `edge` (4cqw) inset; hairlines + page chrome live on the safe line.

**The container law (load-bearing).** Every frame ground sets `container-type: size` AND carries
the graph-paper `background-image`; ALL frame-relative units are `cqw`/`cqh` against it â€” never
`vw`. The grid `background-size` is `~2cqw 2cqw` so cell density holds at any render size.

## Colors

Tokens identical to the source. `{colors.paper}` is the ground; `{colors.ink}` cobalt is the only
ink (type, rules, grid lines, glitch, QR). `{colors.ink-soft}` is a secondary cobalt for editorial
subtitles only; `{colors.grid}` (10%) is the permanent grid + chart "off" cells; `{colors.ink-faint}`
(18%) is faint row dividers. **Never a second hue** â€” emphasis comes from size, from switching
Hankenâ†’Newsreader, from a mono delta arrow, or from opacity, never from color.

## Typography

Two ramps. The **reading ramp** (Hanken body 0.83cqw, mono chrome in px) carries copy + labels;
the **display/hero ramp** (Newsreader `headline` 4.6cqw â†’ `vbig-numeral` 12.5cqw) carries every
statement and figure.

- **Legibility floor:** any load-bearing line â‰¥ **1.4cqw**; mono chrome (px) is colophon only.
- **Fit-to-measure:** size the headline to its line length. Cap the block at **â‰¤ 78cqw**; â‰¤3 words â†’ `display-hero`/`vbig-numeral`; 4â€“6 â†’ `display-chapter`; 7+ â†’ `headline`.
- **Newsreader at 400 only**, in cobalt, with negative tracking (hero âˆ’0.008em, numeral âˆ’0.015em). **Hanken labels uppercase, 0.16â€“0.18em.** **DM Mono 0.04â€“0.08em.** No bold serif.

## Depth & Surface

Flat. Depth is structural only:

- **1.5px cobalt rules** â€” slide hairlines, topbar rule, chart baseline.
- **1px ink-faint dividers** â€” dense list / ledger rows.
- **The graph-paper grid** â€” measured-plane tone behind everything.
- **Pixel-glitch + QR** â€” texture and graphic punctuation, no z-axis.

**Ceiling:** no drop shadow (the QR's 1.5px paper outset is an anti-shadow for readability, not elevation), no gradient, no rounded corner, no second color.

## Shapes

- **0 radius everywhere** â€” frames, ledger rows, QR cells, glitch blocks, charts. Zero circular elements; this squareness is part of the identity.

## Components

- **graph-grid / hairlines / page-chrome** â€” the permanent frame furniture, inherited by every composition.
- **pixel-glitch** (edge column) + **qr-block** (corner patch) â€” the signature decoration on declarative frames.
- **topbar-rule** â€” the index/data/table section header. **ledger-row** â€” dense matrix row with delta arrows.
- **pixel-stack-bar** â€” data as grid-unit cells. **vstack-label** â€” vertical mono catalogue chrome.

## Frame Treatments

> Recipe: ground Â· container Â· composes Â· focal Â· chrome Â· accent Â· silence Â· Fixed/Free Â· density.
> The grid + hairlines are present on every frame. Choose density by type: declarative = sparse, index/data = dense.

### 1 Â· Hero Cover (identity Â· move: serif + glitch Â· left)

**Ground** paper + grid, hairlines. **Composes** pixel-glitch (right, ~26cqw), qr-block (top-right), display-hero, ed-callout. **Focal** a 1â€“2 line `display-hero` Newsreader headline in cobalt, left-anchored, with an italic `ed-callout` subtitle in `{colors.ink-soft}`. **Chrome** Hanken kicker; mono meta top + page number. **Accent** none (cobalt is the only ink). **Silence** ~45% paper. **Fixed** Newsreader 400, glitch + QR present, grid + hairlines. **Free** title, glitch step pattern, QR placement. **Density** sparse.

### 2 Â· Index Ledger (catalog Â· move: dense matrix Â· left â€” the dense frame)

**Ground** paper + grid, hairlines, `pad-top`/`pad-bottom`. **Composes** topbar-rule, ledger-rows. **Focal** a topbar (`headline-index` + mono lab-tag, 1.5px rule) over 4â€“6 ledger rows (mono num Â· Newsreader name Â· Hanken desc), ink-faint dividers. **Chrome** page number. **Accent** mono delta arrows. **Silence** tight â€” the density exception (the grid wants filling). **Fixed** 1.5px topbar rule, 1px ink-faint dividers, Newsreader names. **Free** rows, lab-tag, deltas. **Density** dense-exception.

### 3 Â· Chapter Opener (section Â· move: scale Â· sparse Â· left)

**Ground** paper + grid, hairlines. **Composes** pixel-glitch (left, ~14cqw, low opacity), mono index, display-chapter, body-lede. **Focal** a `display-chapter` Newsreader title, with a small mono `CHAPTER NN` index above and an optional Hanken lede â‰¤42cqw. **Accent** none. **Silence** ~60% â€” let the grid breathe. **Fixed** Newsreader 400, glitch low-opacity, grid showing. **Free** title, lede, glitch side. **Density** sparse.

### 4 Â· Data Frame (chart Â· move: pixel-stack Â· left)

**Ground** paper + grid, hairlines, `pad-top`. **Composes** topbar-rule, pixel-stack-bar row. **Focal** a row of 6â€“8 pixel-stack bars (cobalt on / 10% off) over a 1.5px cobalt baseline with mono ticks. **Chrome** topbar headline + mono fig-tag; page number. **Accent** none â€” data is cobalt cells. **Silence** moderate. **Fixed** grid-unit cells, cobalt baseline, mono ticks. **Free** bar values (from script), tick labels. **Density** standard/dense.

### 5 Â· Manifesto / Quote (quote Â· move: centered statement Â· sparse)

**Ground** paper + grid, hairlines. **Composes** display-quote (or display-manifesto), attribution rule, optional compact glitch. **Focal** a 2â€“3 line Newsreader pull in cobalt, with a Hanken kicker above and a 1px cobalt attribution rule + mono byline beneath. **Accent** none. **Silence** ~55% â€” deliberately open. **Fixed** Newsreader 400, attribution rule, grid showing. **Free** quote, byline. **Density** sparse.

### 6 Â· Colophon (closer Â· move: right-aligned close Â· sparse)

**Ground** paper + grid, hairlines. **Composes** pixel-glitch (left edge, mirroring the cover), display-closing, mono credit columns. **Focal** a right-aligned `display-closing` Newsreader title with a Hanken kicker above. **Chrome** 3â€“4 column mono credit grid at the foot; page number. **Accent** none. **Silence** ~50%. **Fixed** glitch on left, Newsreader 400. **Free** closing line, credits. **Density** sparse.

## Composition Rules

### Do

- Keep the **graph-paper grid + top/bottom hairlines** on every frame â€” they are the system.
- Set **Newsreader at 400 in cobalt**; make hierarchy with size, not weight; negative-track display.
- Track **Hanken labels uppercase 0.16em**; **DM Mono chrome 0.04â€“0.08em**.
- Render data as **pixel-stack cells** (cobalt on / 10% off); echo the glitch language.
- Use the **pixel-glitch column + QR patch** on declarative frames (cover, chapter, quote, colophon).
- Lean: declarative frames sparse and breathing; index/data dense. Vary anchor (left for index/chapter, centered for quote/closer).

### Don't

- Don't introduce a second ink color â€” cream + cobalt only.
- Don't bold Newsreader, round any corner, or add a drop shadow (QR outset is an anti-shadow only).
- Don't disable the grid or suppress the hairlines.
- Don't crowd chapter / quote / colophon â€” those let the grid show.
- Don't blow a serif headline edge-to-edge â€” fit to measure.

## Aspect-Ratio Behavior

| Treatment         | 16:9                        | 9:16                                 | 1:1                          |
| ----------------- | --------------------------- | ------------------------------------ | ---------------------------- |
| Hero Cover        | headline left, glitch right | headline top, glitch full-width band | headline upper, glitch lower |
| Index Ledger      | topbar + rows               | topbar + fewer rows                  | 2-col compresses to 1        |
| Chapter Opener    | title left, glitch left     | title top, glitch side               | centered title               |
| Data Frame        | 6â€“8 bars                    | 4â€“5 bars taller                      | square chart                 |
| Manifesto / Quote | centered pull               | centered, taller                     | centered                     |
| Colophon          | right-aligned, glitch left  | stacked, glitch top                  | centered close               |

Grid + hairlines hold on the short edge for every ratio; re-step display so no load-bearing line
drops below 1.4cqw. Mono chrome stays Latin/digit-only.

## Approved Entities

No real customers, logos, or vendors are defined in the source â€” render any such mark as a
placeholder. Trend names, signals, and figures are content; the system supplies the grid and chrome.

## Numerals & Claims (hard rule)

Never invent figures, deltas, dates, or signal counts at frame scale. Render slots as `â€” figure â€”`,
`{metric}`, `â†‘ â€”`. Pixel-stack bar heights and ledger deltas especially carry placeholders until the
script supplies values. Mono catalogue ordinals (001, 002â€¦) are decorative and may be sequential.

## Pre-Render Self-Audit

- **Squint** â€” one Newsreader element dominates at 3â€“5Ã— its neighbor.
- **Silence** â€” declarative frames 45â€“60% empty; only index/data run dense.
- **Two-color** â€” cream + cobalt only; no second hue anywhere.
- **Furniture** â€” grid present, top/bottom hairlines present, page chrome above the hairline.
- **Type** â€” Newsreader 400 negative-tracked, fit-to-measure; Hanken labels 0.16em; â‰¥1.4cqw floor.
- **Depth** â€” 0 shadow (QR outset excepted), 0 rounded corner.
- **Anchor** â€” left on index/chapter/cover, centered on quote/closer; no 3 consecutive frames share an anchor.
- **Fabrication** â€” every numeral/delta traces to the script, else placeholder.

## Known Gaps

- **Motion intentionally out of scope.** frame.md specifies composition only; the 280ms cross-fade in the source is a deck mechanic.
- **Pixel-glitch is rendered in CSS here** (stacked scanline blocks) rather than the source's inline SVG, to keep the showcase SVG-free; fidelity is preserved.
- **Three Google Fonts** (Newsreader, Hanken Grotesk, DM Mono); CJK pairing (Noto Serif SC 700/400) carries over from the source.
- **9:16 / 1:1 are guidance**; verify the legibility floor and grid density per ratio.
- The QR mosaic and glitch step patterns are hand-authored; there is no generative layer.
