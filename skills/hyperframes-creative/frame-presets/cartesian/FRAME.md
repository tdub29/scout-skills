---
version: alpha
name: Cartesian â€” Frame (video / frame layer)
description: >
  Video-first companion to Cartesian's design.md. The unit is the frame (1920Ã—1080). Atoms are
  identical and sacred â€” the five-tone warm-stone palette, Playfair Display 400 + Inter, the
  universal 1px taupe hairline as the only structural device, compass-drafted geometric rings,
  and zero shadow / zero fill. Composition, frame scale, and aspect-ratio behavior are rewritten
  for the frame. Restraint is the rule; motion is out of scope.
unit: the frame â€” 1920Ã—1080 primary; 9:16 and 1:1 documented
principle: atoms are sacred Â· composition is free Â· numbers come from the script

colors:
  bg-primary: "#EDE8E0"
  bg-secondary: "#E2DBD1"
  text-primary: "#1A1A1A"
  text-secondary: "#5A5A5A"
  accent: "#8A8178"
  line: "#B8B0A4"
  white-overlay: "rgba(255,255,255,0.3)"

typography:
  # â€” reading ramp (Inter) â€”
  body:        { fontFamily: "Inter", cqw: 1.0,  weight: 400, lineHeight: 1.6, color: "text-secondary" }
  body-sm:     { fontFamily: "Inter", cqw: 0.85, weight: 400, lineHeight: 1.6 }
  subtitle:    { fontFamily: "Inter", cqw: 1.3,  weight: 400, lineHeight: 1.5 }
  label:       { fontFamily: "Inter", px: 14, weight: 500, tracking: "3px", upper: true, color: "accent" }
  attribution: { fontFamily: "Inter", px: 15, weight: 400, tracking: "2px", upper: true, color: "accent" }
  micro:       { fontFamily: "Inter", px: 12, weight: 400, tracking: "2px", upper: true, color: "accent" }
  # â€” display / hero ramp (Playfair Display 400, sentence case) â€”
  h3:          { fontFamily: "Playfair Display", cqw: 1.8, weight: 400, lineHeight: 1.1 }
  timeline-headline:{ fontFamily: "Playfair Display", cqw: 1.9, weight: 400, lineHeight: 1.1 }
  card-headline:{ fontFamily: "Playfair Display", cqw: 2.0, weight: 400, lineHeight: 1.15 }
  stat-figure: { fontFamily: "Playfair Display", cqw: 3.0, weight: 400, lineHeight: 1.0 }
  quote-mark:  { fontFamily: "Playfair Display", cqw: 9.0, weight: 400, lineHeight: 0.5, color: "line" }
  h2:          { fontFamily: "Playfair Display", cqw: 4.0, weight: 400, lineHeight: 1.1 }
  h1:          { fontFamily: "Playfair Display", cqw: 6.2, weight: 400, lineHeight: 1.06 }
  display:     { fontFamily: "Playfair Display", cqw: 8.0, weight: 400, lineHeight: 1.04 }

spacing:
  pad-x: "7cqw"
  pad-y: "5cqw"
  gap-xl: "6cqw"
  gap-lg: "5cqw"

components:
  hairline:
    rule: "0.07cqw solid {colors.line}"
    description: "The universal structural device â€” every separator (agenda rule, timeline connector, card border, stats top) is this 1px taupe line. No thick borders exist."
  card:
    backgroundColor: "{colors.white-overlay}"
    border: "0.07cqw solid {colors.line}"
    rounded: "0"
    shadow: "none"
    description: "Faint white-overlay fill (canvas bleeds through) is what makes a card distinct from a bare region."
  card-icon:
    border: "0.07cqw solid {colors.line}"
    rounded: "50%"
    size: "40px circle"
    textColor: "{colors.accent}"
    typography: "Playfair numeral/letter"
    description: "Ringed circle mark."
  agenda-row:
    borderBottom: "0.07cqw solid {colors.line}"
    typography: "{typography.h3} (numeral {colors.accent}, label {colors.text-primary})"
    description: "Numeral left, label right over a taupe rule."
  timeline:
    borderTop: "0.07cqw solid {colors.line}"
    typography: "{typography.timeline-headline} + {typography.body-sm}"
    description: "A single taupe top rule across items â€” no nodes, no dots."
  stats-cluster:
    borderTop: "0.07cqw solid {colors.line}"
    typography: "{typography.stat-figure} + uppercase {colors.accent} labels"
    description: "Inline modest stat figures (no hero numeral)."
  geo-ring:
    border: "1px solid {colors.line} (inner dashed ::before ~70â€“80%)"
    rounded: "50%"
    size: "10â€“50cqw"
    opacity: "0.2â€“0.5"
    description: "Compass-construction rings behind content. 1â€“2 per frame, never more."
  horizontal-accent:
    backgroundColor: "{colors.text-primary}"
    size: "~18cqw Ã— 1px"
    description: "The system's only INK-BLACK rule â€” a strong terminal accent on cover/closing, sparingly."
  vertical-line:
    backgroundColor: "{colors.line}"
    size: "1px Ã— full height, ~5cqw from edge"
    opacity: "0.3â€“0.4"
    description: "Drafting-paper alignment guide. Optional."
  image-placeholder:
    backgroundColor: "{colors.bg-secondary}"
    mark: "crossed +30Â°/âˆ’30Â° 1px taupe diagonals (an X)"
    typography: "small uppercase {typography.micro}"
    description: "The signature image-not-wired mark."
  team-photo:
    backgroundColor: "{colors.bg-secondary}"
    border: "0.07cqw solid {colors.line}"
    rounded: "50%"
    typography: "Playfair initial in {colors.accent}"
    description: "Circular portrait frame."
---

# Cartesian â€” Frame (video / frame layer)

## Overview

Cartesian at frame scale is a **quiet museum-catalog editorial system** â€” restraint through 1px
lines. Every structural separator is a single 1px taupe hairline; there are no thick borders, no
fills (save the faint white-overlay card), no shadows, no rounded rectangles. Hierarchy comes from
**type contrast and negative space**, and atmosphere from **compass-drafted geometric rings**
drifting behind content.

The voice is a literary pairing: **Playfair Display** at weight 400 (the thin-stroke didone, never
bold, always sentence case) carries every headline, numeral, and quote mark in ink; **Inter**
carries body in warm gray and labels in uppercase taupe with 2â€“3px tracking. The palette is five
warm stones plus ink â€” no populist accent color exists. The correct density is **sparse and
breathing**: one clear idea, well-framed, on stone paper.

**Key characteristics at frame scale:**

- **1px taupe hairline** as the universal structural device â€” every separator is this one line.
- **Playfair Display 400** (ink, sentence case) for display; **Inter** body (gray) + labels (taupe, tracked).
- **Five warm stones + ink** â€” no red/blue/green; the only "color" is type contrast.
- **Compass-drafted geometric rings** (solid + dashed, 20â€“50% opacity) behind content for mood.
- **Flat** â€” zero shadow, zero rounded rectangle (circles only); the lone ink line is the `horizontal-accent`.
- **Sparse and breathing** â€” generous negative space; crowding reads as broken.

## The Frame

### Frame Craft Bar

Three eyeball tests gate every frame before any structural check:

- **Squint** â€” one Playfair element dominates at **3â€“6Ã— its nearest neighbor**; the serif/sans + size contrast carries hierarchy, not weight.
- **Silence** â€” declarative frames read **55â€“60% empty**; Cartesian has **no dense frame** â€” even the agenda/index breathes (the system breaks when crowded).
- **Restraint** â€” **at most two geo rings** per frame; the single INK-BLACK `horizontal-accent` rule used sparingly; no populist accent color ever.
- **Reference** â€” aim at a **Vignelli editorial / Cooper Hewitt catalogue / pencil-and-tracing-paper plan**; failure looks like a **shadowed, rounded-card SaaS deck**.

- **Primary:** 1920Ã—1080 (16:9). Display authored in **`cqw`** (`px Ã· 1920 Ã— 100 = cqw`).
- **Vertical:** 1080Ã—1920 (9:16). **Square:** 1080Ã—1080 (1:1).
- **Safe area:** `pad-x` (7cqw) generous gutters; geometry may bleed off an edge.

**The container law (load-bearing).** Every frame ground sets `container-type: size`; ALL
frame-relative units are `cqw`/`cqh` against it â€” never `vw`. The 1px hairlines and geo rings hold
their proportion against the frame at any render size.

## Colors

Tokens identical to the source. `{colors.bg-primary}` is the ground; `{colors.text-primary}` ink is
headlines and the one black accent rule; `{colors.text-secondary}` gray is body; `{colors.accent}`
taupe is labels, numerals, small text; `{colors.line}` taupe is every 1px structural border.
`{colors.bg-secondary}` is the only secondary fill (placeholders, photo frames). **No populist
accent** â€” when emphasis is needed, grow the type, switch sansâ†’serif, or add a single
`horizontal-accent` ink line. Headlines are never taupe; small text is never ink.

## Typography

Two ramps. The **reading ramp** (Inter body 1.0cqw gray, labels in px taupe) carries copy + chrome;
the **display ramp** (Playfair `h3` 1.8cqw â†’ `display` 8.0cqw, all weight 400) carries every headline.

- **Legibility floor:** any load-bearing line â‰¥ **1.4cqw**; px labels are chrome only.
- **Fit-to-measure:** size the headline to its length. Cap the block at **â‰¤ 78cqw**; â‰¤3 words â†’ `display`/`h1`; 4â€“6 â†’ `h2`; 7+ â†’ `h3`. Cartesian has no hero-stat numeral â€” stats stay modest (`stat-figure` 3cqw).
- **Playfair at 400, ink, sentence case** â€” never bold, never uppercase, never taupe. **Inter labels uppercase, 2â€“3px tracked, taupe.** Italic via Playfair italic for emphasis only.

## Depth & Surface

The flat plane is the only technique. Hierarchy from:

- **Type contrast** â€” Playfair serif vs Inter sans; the 8cqwâ†’0.7cqw scale.
- **1px taupe hairlines** â€” every divider, card outline, timeline rule, photo ring.
- **Tone** â€” ink vs gray vs taupe.
- **Negative space** â€” generous padding.
- **Geometric atmosphere** â€” compass rings that suggest depth without creating it.

**Ceiling:** no box-shadow, no elevated card, no gradient, no rounded rectangle. The single ink line
(`horizontal-accent`) is the only non-taupe rule.

## Shapes

- **50% (circle)** â€” card-icon, team-photo, nav-dot, every geo ring.
- **0** â€” everything else; soft-rounded corners do not exist.

## Components

- **hairline** â€” the universal 1px taupe separator (the identity).
- **card** (1px taupe + white-overlay) / **card-icon** (ringed circle) / **agenda-row** / **timeline** (line, no nodes) / **stats-cluster** â€” all built on the hairline.
- **geo-ring** â€” compass decoration (solid + dashed), 1â€“2 per frame. **horizontal-accent** â€” the one ink line, sparingly. **vertical-line** â€” drafting guide.
- **image-placeholder** (crossed-X) / **team-photo** (ringed initial) â€” the stone-fill placeholders.

## Frame Treatments

> Recipe: ground Â· container Â· composes Â· focal Â· chrome Â· accent Â· silence Â· Fixed/Free Â· density.
> Every frame is sparse and breathing; 1â€“2 geo decorations max.

### 1 Â· Cover (identity Â· move: serif + compass ring Â· left)

**Ground** `{colors.bg-primary}`, `pad-x`. **Composes** geo-ring (right, ~34cqw, solid+dashed), vertical-line (left), label, display/h1. **Focal** a 2â€“3 line Playfair `display`/`h1` headline in ink (italic on the key word), left-anchored, with a taupe `label` above and an Inter subtitle below. **Chrome** optional bottom meta row (Playfair value + taupe label). **Accent** the geo ring; optionally one `horizontal-accent` ink line (if it clears the meta). **Silence** ~55% empty. **Fixed** Playfair 400 ink sentence-case, â‰¤2 geo elements, 1px lines. **Free** title, ring placement, meta. **Density** sparse.

### 2 Â· Agenda / Index (index Â· move: hairline list Â· left)

**Ground** `{colors.bg-primary}`, `pad-x`. **Composes** label, h2, agenda-rows. **Focal** a Playfair `h2` over 4â€“6 agenda rows (Playfair numeral in taupe + Playfair label in ink), each on a 1px taupe rule. **Chrome** taupe `label` eyebrow. **Accent** none â€” taupe numerals carry it. **Silence** moderate; rows generously spaced. **Fixed** 1px taupe rules, Playfair 400. **Free** items, count. **Density** standard (sparse rows).

### 3 Â· Pull Quote (quote Â· move: centered statement Â· compass ring)

**Ground** `{colors.bg-primary}`, centered. **Composes** geo-ring (centered dashed, ~26cqw), quote-mark, h2/display-quote, attribution. **Focal** a 2-line Playfair quote in ink, centered, under a 50%-taupe Playfair quote-mark; a taupe uppercase attribution beneath. **Accent** the faint centered ring. **Silence** ~60% â€” deliberately open. **Fixed** Playfair 400, one ring, centered. **Free** quote, attribution. **Density** sparse.

### 4 Â· Closing Plate (closer Â· move: centered ring Â· centered)

**Ground** `{colors.bg-primary}`, centered. **Composes** geo-ring (centered, ~40cqw, solid+dashed), label, h1/display, horizontal-accent. **Focal** a 1â€“2 line Playfair sign-off in ink (italic key word), centered inside the largest compass ring; a short ink `horizontal-accent` beneath. **Accent** the ring + the one ink line. **Silence** ~60%. **Fixed** Playfair 400, centered, â‰¤2 geo. **Free** sign-off, ring scale. **Density** sparse.

### 5 Â· Two-Column Editorial (content Â· move: asymmetric split Â· left)

**Ground** `{colors.bg-primary}`, `pad-x`, two columns with `gap-xl`. **Composes** label, h2, body, image-placeholder (crossed-X) or card. **Focal** a Playfair `h2` + Inter body in the text column; an image-placeholder or card in the other. **Accent** none. **Silence** generous gutter. **Fixed** 1px taupe card/placeholder borders, white-overlay fill. **Free** which side is text, body copy. **Density** standard.

### 6 Â· Stats / Timeline (data Â· move: hairline rail Â· left)

**Ground** `{colors.bg-primary}`, `pad-x`. **Composes** label, h3, stats-cluster or timeline. **Focal** a modest Playfair stat row (or a 1px-rule timeline with year + headline + body, no nodes), framed by a 1px taupe top rule. **Accent** none. **Silence** moderate. **Fixed** modest stat scale, hairline rule, no nodes. **Free** figures, phases. **Density** standard.

## Composition Rules

### Do

- Use a **single 1px taupe line** for every separator â€” the hairline is the identity.
- Set every **Playfair headline at 400, ink, sentence case**; render labels taupe, uppercase, 2â€“3px tracked.
- Layer **one or two compass rings** (solid + dashed, 20â€“50% opacity) behind content for atmosphere.
- Let frames **breathe** â€” sparse, generous negative space; 55â€“60% empty on declarative frames.
- Lean centered on quote/closer; asymmetric/left on cover/agenda/editorial. Use `bg-secondary` for placeholder fills.

### Don't

- Don't introduce a populist accent color â€” stone and ink only.
- Don't bold Playfair, render headlines in taupe, or use thick (2px+) borders.
- Don't add shadows, elevated cards, or rounded rectangles (circles only).
- Don't crowd the frame â€” packed layouts read as broken.
- Never more than two geo decorations per frame; don't blow a headline edge-to-edge.

## Aspect-Ratio Behavior

| Treatment            | 16:9                       | 9:16                                | 1:1                         |
| -------------------- | -------------------------- | ----------------------------------- | --------------------------- |
| Cover                | headline left, ring right  | headline top, ring below            | headline upper, ring behind |
| Agenda / Index       | h2 + rows                  | h2 + rows (tighter)                 | h2 + rows                   |
| Pull Quote           | centered, ring behind      | centered, taller                    | centered                    |
| Closing Plate        | centered in ring           | centered, ring scaled               | centered                    |
| Two-Column Editorial | text + visual side-by-side | stacked (collapse)                  | stacked                     |
| Stats / Timeline     | horizontal rail            | vertical stack (drop timeline rule) | compact                     |

Generous `pad-x` holds on the short edge; re-step display per ratio above the 1.4cqw floor. On
9:16, the timeline rule loses meaning when stacked â€” switch to a vertical list (per source).

## Approved Entities

No real customers, logos, or vendors are defined in the source â€” render any such mark as a
placeholder (the crossed-X image-placeholder, or a ringed initial for portraits).

## Numerals & Claims (hard rule)

Never invent figures, dates, or counts at frame scale. Render slots as `â€” figure â€”`, `{metric}`.
Stats and timeline years carry placeholders until the script supplies them. Agenda ordinals
(01, 02â€¦) are decorative and may be sequential.

## Pre-Render Self-Audit

- **Squint** â€” one Playfair element dominates; the serif/sans contrast carries hierarchy.
- **Silence** â€” declarative frames 55â€“60% empty; nothing is crowded.
- **Palette** â€” five stones + ink only; no populist accent; headlines ink, labels taupe.
- **Lines** â€” every separator is a 1px taupe hairline; the only ink line is `horizontal-accent`.
- **Type** â€” Playfair 400 sentence-case, fit-to-measure; labels uppercase 2â€“3px; â‰¥1.4cqw floor.
- **Depth** â€” 0 shadow, 0 rounded rectangle; â‰¤2 geo rings per frame.
- **Anchor** â€” centered on quote/closer, left/asymmetric on cover/agenda/editorial; no 3 in a row alike.
- **Fabrication** â€” every numeral traces to the script, else placeholder.

## Known Gaps

- **Motion intentionally out of scope.** frame.md specifies composition only; the 0.6s fade in the source is a deck mechanic.
- **Playfair Display + Inter via Google Fonts.** CJK pairing (Noto Serif SC 700/400) carries over; Playfair has no Hanzi italic â€” substitute weight/taupe for emphasis.
- **9:16 / 1:1 are guidance**; verify the legibility floor and that the timeline collapses to a vertical list.
- Geo rings, the crossed-X placeholder, and the dashed inner ring are CSS-only; no external imagery is required.
