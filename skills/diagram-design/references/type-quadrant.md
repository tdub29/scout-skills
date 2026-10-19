# Quadrant

**Best for:** prioritization (Impact Ã— Effort), positioning (Reach Ã— Frequency), portfolio maps, 2Ã—2 decision frames.

## Layout conventions
- 2Ã—2 grid. Axis lines: 1px ink cross through the center.
- **Axis labels: Jobs-minimal.** One single word at each arrow tip â€” no glyphs baked into the label (no `â†‘` / `â†’` / `â†` / `â†“`), no parentheticals, no "HIGH / LOW" modifiers. Geist Mono 9px regular weight, tracked 0.18em, uppercase. Flank the arrow tips â€” never sit labels on top of the axis line. Shorten the arrow enough (~60â€“80px inside the viewBox edge) to leave breathing room for the labels beyond the tips.
- Never label at the midpoint.
- Items: small labeled dots (`r=4`) positioned in the quadrants. Labels 8â€“10px away; don't let labels cross axis lines.
- Coral on the "do first" item (typically top-right).
- Limit to ~12 items; cluster or split beyond that.

## Anti-patterns
- Four filled quadrants in different colors â€” position + label does the work; color noise weakens it.
- Items placed on axis lines (ambiguous quadrant).
- Missing axis names.

## Examples
- `assets/example-quadrant.html` â€” minimal light
- `assets/example-quadrant-dark.html` â€” minimal dark
- `assets/example-quadrant-full.html` â€” full editorial
- `assets/example-quadrant-consultant.html` â€” consultant special (see below)

---

## Consultant special (2Ã—2 scenario matrix)

A **layout variant** of the standard quadrant â€” same house skin (warm paper, dot pattern, Instrument Serif title, Geist mono eyebrows, coral focal rule). The grammar shifts: axes hold a **range** rather than a measurement; cells hold **named scenarios** rather than positioned items.

**Use when:** you're framing four futures, archetypes, or strategic options across two independent drivers â€” classic scenario planning, positioning frames, or 2Ã—2 strategy decks (BCG/McKinsey territory). The reader should come away with four named bets, not a point cloud.

**Do not use** for prioritization, density maps, or anything where the *position inside* a cell carries meaning â€” that's the standard quadrant above.

### What makes it the consultant variant

| Move | Standard quadrant | Consultant special |
|---|---|---|
| Axis arrows | single-ended | **double-ended** â€” both axes have `marker-start` + `marker-end` |
| Cell content | small dots with labels | **named scenario + 1â€“3 line description** |
| Quadrant corner | short tag (e.g. DO FIRST) | **numbered tag + axis combination** (`01 Â· DIMENSION-A / DIMENSION-B`) |
| Focal accent | coral on one *item* | coral on one *quadrant* â€” tinted bg + coral stroke + coral corner tag |
| Axes | 1px muted ink | **1.2px ink** (slightly heavier â€” the axes carry more of the figure) |

Both variants use the same Jobs-minimal axis labels: one word at each arrow tip, no glyphs, no parentheticals. The only axis difference is that the consultant variant uses double-ended arrows instead of single-ended.

Everything else â€” paper, dot pattern, typography, legend strip, 4px grid, complexity budget â€” is the house default. Don't invent new colors or fonts for this variant.

### Style tokens (in-house)

- **Paper / bg / pattern**: defaults from `style-guide.md` (`paper`, 22Ã—22 dot pattern at 10% ink).
- **Axis lines**: `ink` (`#2d3142`), `stroke-width: 1.2`, `marker-start` + `marker-end` both pointing outward.
- **Focal quadrant tint**: `rgba(235,108,54,0.04)` full rect behind the focal cell.
- **Focal cell**: `accent-tint` fill, `accent` stroke at 1.2px. Corner tag in `accent`, weight 600.
- **Non-focal cells**: `store` treatment (`ink @ 0.04` fill, `muted @ 0.28` stroke).
- **Cell title**: Geist sans, 16px, weight 600, `ink`.
- **Cell description**: Geist sans, 11px, `muted`, 1â€“3 lines, left-aligned inside the cell.
- **Corner tag**: Geist Mono, 8px, uppercase, tracked `0.18em`, `muted` (or `accent` on focal). Format: `NN Â· DIMENSION-A / DIMENSION-B` â€” the two axis-dimension words must match the axis labels exactly.
- **Axis labels**: Geist Mono 9px **regular weight** (not bold), tracked `0.18em`, uppercase, `ink`. **One word per tip.** No arrow glyphs in the label, no `HIGH / LOW` parentheticals, no multi-line sublabels. The word itself *is* the label. Position labels *beyond* the arrow tips (not on the axis line):
  - Top tip: `text-anchor="middle"`, ~12px above the arrow tip
  - Bottom tip: `text-anchor="middle"`, ~20px below the arrow tip
  - Left tip: `text-anchor="end"`, ~12px left of the arrow tip, `dominant-baseline="middle"`
  - Right tip: `text-anchor="start"`, ~12px right of the arrow tip, `dominant-baseline="middle"`

### Layout conventions

- Four cells, equal size (240Ã—160 or 280Ã—180 are good defaults), arranged with a 40â€“60px gap from the axis cross.
- Axis cross passes *between* the cells, not through them.
- Arrow tips live ~20â€“40px outside the outermost cell edge; single-word axis labels sit ~12px beyond each tip (see Axis labels above).
- Exactly one focal cell. Picking none makes it a placeholder template; picking two erases the signal.
- Keep the legend strip + horizontal rule at the bottom â€” same as the standard quadrant. Legend swatches should show both "headline bet" (coral) and "candidate future" (neutral).

### Anti-patterns (variant-specific)

- Plain white background â€” the warm paper + dot pattern is load-bearing across the skill; dropping it to "look consultant" turns the diagram generic.
- Sans-serif H1 â€” keep Instrument Serif for the page title. The title/diagram contrast is the house signature.
- Unnamed cells ("Scenario 1/2/3/4") in a shipped diagram â€” OK as a blank template; not OK as a finished artifact.
- Coral on more than one cell â€” same focal rule as everywhere else in the skill.
- 3Ã—3 or 2Ã—3 grids â€” those are different diagrams, not this variant.
- Positioning dots *inside* the cells â€” if position matters, use the standard quadrant.
- Bolded axis labels, arrow glyphs in the text (`â†‘ DRIVER`), or "HIGH / LOW" parentheticals â€” all forbidden. Jobs-minimal is non-negotiable on this variant.
- Corner tags that disagree with the axis labels (e.g. axis says `REMOTE / IN-PERSON` but the tag reads `HIGH REMOTE / LOW AI`). Reader parses this as a bug in three seconds.
