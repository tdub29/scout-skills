# Tufte: Small Multiples

## When to use

Trigger when the right answer to a visualization problem is *repetition*, not *cramming*. Concrete cues:

- The user has 6+ series on one chart and is asking how to declutter
- The user wants to compare the same metric across many segments (regions, cohorts, time periods, products, subjects)
- The user is building a dashboard with one big chart and asking why it doesn't tell a clear story
- The phrase "faceted plot," "trellis chart," "panel grid," or "ticker layout" comes up
- The user wants to see whether a relationship *changes* across categories â€” interaction effects
- The user has tried color, dashed lines, and legends to differentiate series and the chart is still unreadable
- The chart is a heatmap that's hiding the actual within-cell shape
- The user mentions sparklines, thumbnail grids, or repeated-mini-chart layouts

Don't trigger for: choosing between chart types when there's only one series (general data-viz), aesthetic polish on an already-clean chart (design), filter UX decisions (that's a dropdown/filter problem, not a small-multiples problem). And critically â€” small multiples are not the answer when you only have 2â€“3 categories. The pattern earns its keep at roughly N â‰¥ 4 panels; below that, a single chart with explicit annotation usually wins.

## The framework

### Core thesis

Many visualization failures are not about chart type â€” they're about trying to encode too many variables in one frame. When you have one structural relationship (X vs. Y) repeated across a third variable (region, year, cohort), the human eye does not reliably parse 8 overlapping lines, 12 colors, or a 60-cell heatmap. It reliably parses a *grid* of small, identical panels, each showing one slice. The pattern is "inevitably comparative" â€” the moment you tile the same chart at small scale, the brain starts cross-comparing automatically. The cost is real estate; the payoff is that interaction effects, outliers, and shape differences become visible without any explicit comparison machinery (no callouts, no legends, no animation).

Tufte calls small multiples "shrunken, high-density graphics" â€” they're a high-data-density pattern, but density is a *consequence*, not the goal. The goal is comparison, and the small-multiples layout is the design that makes comparison cheap.

### The four required design decisions

A small-multiples design lives or dies on four choices. Get any one wrong and the comparison fails.

1. **The indexing variable** â€” the dimension you repeat across. Must be a single discrete variable (geography, year, subject, treatment arm, product category). Multi-dimensional indexing (e.g., region Ã— quarter) requires a 2D grid layout (see below). Choose the variable whose *values you want the reader to compare*, not the variable that's incidentally there.

2. **The panel template** â€” the chart that gets repeated. Must be identical in every panel: same encoding, same axes, same axis ranges, same color scale, same annotations. Any variation between panels has to *be data*, not design. The most common failure mode is "free y-axes" in a panel grid; this makes panels incomparable and defeats the entire pattern.

3. **The grid layout** â€” rows Ã— columns. Should follow a meaningful ordering of the indexing variable (geographic adjacency, time order, magnitude, alphabetic only as a last resort). For 2D indexing (region Ã— quarter), use rows for one dimension, columns for the other, and explicitly label both axes of the *grid*.

4. **The shrinkage level** â€” how small each panel can be while still readable. Tufte's empirical finding: each panel can be ~10â€“25% the size of a standalone chart and still convey shape. Below that, only outliers and gross trends remain visible. The smaller you go, the more panels fit, and the more cross-comparison the reader does. Trade panel detail for grid scope.

### The two failure modes that wreck small multiples

Two failures are common enough that they deserve naming:

- **Free axes.** Each panel auto-scales its own y-axis to its own data range. This is the default in most plotting libraries. It makes each panel maximally readable *individually* and minimally comparable *across panels* â€” defeating the entire purpose. Always use a shared scale unless you have a specific, defensible reason and call out the choice in the figure caption.

- **Too many panels.** A 12Ã—12 grid of sparklines is impressive but unreadable. There's a comfortable upper bound around 20â€“40 panels for at-a-glance comparison. Above that, the grid becomes a heatmap (and you'd be better off making it an actual heatmap, or grouping panels into clusters).

### When *not* to use small multiples

Despite being a Tufte favorite, small multiples are wrong when:

- You have 2â€“3 categories. A direct overlay chart with 2â€“3 series, labeled inline, beats a 2-panel grid every time. The grid overhead isn't worth it.
- The shape of each panel is uninteresting on its own. If every panel is "line goes up roughly the same way," small multiples buy nothing. Use a single aggregate chart or an index chart instead.
- Reader attention is single-glance. Dashboards meant for a 2-second look are better served by a single number, gauge, or trend arrow than a 20-panel grid that requires sustained scanning.
- The indexing variable is continuous. Small multiples need a discrete indexing variable. For continuous variables, use a single chart with the continuous variable on an axis.

## How to apply (step-by-step)

1. **Confirm small multiples is the right pattern.** Re-read the "when not to use" list. If the situation matches one of those, route to the right alternative (overlay, index chart, heatmap, single-number summary) and stop.

2. **Name the indexing variable.** What is the *one* dimension being compared across? If you cannot name it in one phrase ("by region," "by quarter," "by cohort age"), the design isn't a small-multiples design â€” you need to resolve the framing first.

3. **Specify the panel template.** Write out, in one sentence, what each panel will show: "Each panel shows daily revenue (y) vs. day of month (x) as a line chart, with the y-axis fixed across all panels from $0 to $X." Pin down: chart type, x-axis variable + range, y-axis variable + range, color encoding (if any), annotations (if any). Identical across panels.

4. **Decide the grid.** Count distinct values of the indexing variable. Pick rows Ã— columns that produce roughly equal aspect â€” for N panels, sqrt(N) rounded. For 2D indexing, use a true 2D grid. Order the panels meaningfully: geographic adjacency > time order > magnitude > alphabetic. State the ordering explicitly.

5. **Choose shrinkage.** Estimate the smallest each panel can be while still showing the *shape* the reader needs. If the question is "where are the outliers," shape resolution is low â€” go small. If the question is "what's the within-panel pattern," shape resolution is high â€” go bigger and accept fewer panels per screen.

6. **Decide annotation strategy.** Most small-multiples designs annotate only the *first* panel and rely on the reader to infer the pattern across the rest. Each panel labels only its indexing-variable value ("California," "Texas," "Florida," ...). Avoid per-panel callouts unless an outlier panel needs an explicit note. Axis labels appear once on the bottom-left panel, not on every panel.

7. **Produce the spec.** A small-multiples spec is: indexing variable + panel template + grid dimensions + ordering rule + shrinkage level + annotation rule. Either render the result (if the user is in a notebook / plotting library) or hand off the spec to a downstream rendering skill.

8. **Sanity-check the comparison.** Before declaring done, ask: "Looking across this grid, which panel jumps out? Which two panels look most alike? Which look most different?" If the answers are obvious, the design is working. If every panel looks the same or every panel looks different in an indistinguishable way, the indexing variable or the shrinkage level is wrong â€” iterate.

## Common failure modes

- **Free y-axes.** Each panel auto-scales to its own data, which kills cross-panel comparison. Default to a shared scale. If one panel has an outlier that compresses the others, use a fixed scale anyway and let the outlier panel break out visually â€” that's a *signal*, not a problem. Free axes are the single most common reason small-multiples designs feel wrong.

- **Wrong indexing variable.** Choosing the variable that's incidentally available rather than the one that drives the comparison. If you're trying to detect cohort behavior shifts, index by cohort, not by day. If you're trying to compare regions, index by region, not by product. Wrong index = right pattern applied to the wrong cut of the data.

- **Decorative grid lines / per-panel legends / per-panel titles.** Every visual element that repeats across all panels is wasted ink that the reader has to mentally suppress. Move legends, axes labels, source notes, and title to the *figure* level â€” once. Let the panels be data.

- **Too few panels (N â‰¤ 3).** Small multiples have overhead â€” grid layout, per-panel labels, the visual rhythm of repetition. Below 4 panels that overhead outweighs the benefit. Use overlay charts instead. Above ~40 panels you're in heatmap territory.

- **No meaningful ordering.** Panels arranged alphabetically when the natural order is geographic or temporal. The grid IS the comparison â€” its order encodes meaning. Don't waste the encoding by defaulting to alphabetic.

- **Using small multiples to disguise that you have no story.** The pattern reveals comparisons; it does not create them. If the underlying data has no interesting variation across the indexing variable, a small-multiples design just makes that boring conclusion more visible. Don't reach for small multiples to make a flat dataset look richer. Either find an indexing variable that does show variation, or accept that a single aggregate chart is the right answer.

- **Confusing small multiples with chart juxtaposition.** A small-multiples design has *one* repeated template under *one* indexing variable. A multi-chart layout with a bar chart next to a line chart next to a map is a *figure*, not a small-multiples design. Don't apply the small-multiples rules to mixed-template layouts â€” they don't fit.

## References

- *The Visual Display of Quantitative Information*, 2nd ed., chapter 8 (book pages 161â€“176). The small-multiples discussion starts on page 165; canonical examples include the repeated weather maps and the brain-scan grid.
- Companion skill: `tufte-data-density` (the parent principle small multiples instantiates).
- Related: `tufte-data-ink-ratio` (small multiples succeed by maximizing data-ink within each tiny panel).
- Bertin theoretical foundations: `bertin-image-vs-figuration` (each panel of a small-multiples grid is its own "image" in Bertin's sense â€” that's *why* the pattern works); `bertin-reorderable-matrix` (the conceptual ancestor â€” same idea of "compare across a third dimension by repeating structure").
