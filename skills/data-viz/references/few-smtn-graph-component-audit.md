# Few SMTN: Graph Component Audit

## When to use

Trigger when the chart type is roughly right but the implementation is not. Cues: "fix this chart," "make this graph readable," "labels are messy," "axis/legend problem," "too cluttered," or "why is this business chart hard to understand."

## The framework

Few separates a graph into primary data components, secondary data components, and non-data components. Each must serve the quantitative message. The audit artifact is a prioritized repair list, not a redesign from scratch.

### Component groups

1. **Primary data components.** Bars, lines, points, areas, and other marks that encode the values. They must correspond visually to quantity and use the strongest practical encoding.

2. **Secondary data components.** Reference lines, bands, trend lines, comparisons, targets, and annotations. They should clarify context without stealing attention from the primary values.

3. **Non-data components.** Titles, subtitles, axes, tick marks, legends, labels, gridlines, notes, and source lines. They should help decoding and then recede.

4. **Scale and correspondence.** Quantitative scales should be honest, readable, and suited to the comparison. Avoid 3D and any component that breaks visual correspondence to quantity.

## How to apply

1. **Confirm chart-task fit.** If the chart type is wrong, route to `few-smtn-relationship-chart-selector` first.

2. **List components.** Identify primary marks, secondary marks, and non-data components.

3. **Score each component.** Mark keep, revise, remove, or replace.

4. **Prioritize repairs.** Fix visual correspondence and scale first, then clutter, then labeling polish.

5. **Return a repair plan.** Include exact changes: axis baseline, legend placement, direct labels, gridline strength, annotation placement, mark choice, and title rewrite if needed.

## Common failure modes

- **Fixing labels while leaving broken scale.** Scale and quantitative correspondence are higher priority than cosmetic cleanup.

- **Letting legends do work direct labels could do.** Legends force eye travel; direct labels often reduce load.

- **Gridlines overpowering data.** Gridlines are aids, not the chart. Make them light or remove them when labels suffice.

- **Reference lines without purpose.** A target, average, or threshold is useful only if it changes interpretation.

- **Decorative 3D.** 3D bars, beveled lines, shadows, and gradients distort comparison and add decoding effort.

## References

- Stephen Few, *Show Me the Numbers*, chapters 9-10.
- Sibling skills: `few-smtn-relationship-chart-selector`, `few-smtn-forsaken-chart-replacement`.
- For proportional distortion scoring, use `tufte-lie-factor`; this skill produces a practical component repair plan.
