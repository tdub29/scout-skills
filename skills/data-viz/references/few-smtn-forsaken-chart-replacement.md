# Few SMTN: Forsaken Chart Replacement

## When to use

Trigger when the current or proposed chart is a donut, radar/spider chart, circle chart, unit chart, funnel chart, decorative waterfall, or stacked area chart trying to do too much. Also trigger when the user says a chart looks slick but nobody understands it.

## The framework

Few's Chapter 12 is not a blanket dislike of novelty; it is a replacement discipline. Certain chart types ask readers to compare angles, areas, shapes, or segmented paths that business readers interpret poorly. The artifact is a replacement spec that preserves the analytical intent while removing the weak display medium.

### Forsaken forms and replacements

1. **Donut and pie-like charts.** Replace with bars, sorted bars, or a compact table when comparing parts or exact shares matters.

2. **Radar/spider charts.** Replace with grouped bars, dot plots, heatmaps, or small multiples so each measure has a readable scale.

3. **Circle/unit charts.** Replace with bars or tables unless the literal count of units is the message.

4. **Funnel charts.** Replace with bars or a step table that shows stage counts, conversion rates, and drop-offs clearly.

5. **Stacked area charts combining time and part-to-whole.** Replace with lines for trends, stacked bars for composition snapshots, or small multiples for component trends.

6. **Waterfalls for simple part-to-whole.** Use waterfalls for additive bridge logic; use bars/tables for simple composition.

## How to apply

1. **Identify the intended relationship.** Part-to-whole, ranking, time series, deviation, conversion path, or multivariate profile.

2. **Name the chart's perceptual burden.** Angle, area, radial scale, overplotting, stacked baseline, or path decoding.

3. **Choose the replacement.** Select the simplest chart family that exposes the relationship.

4. **Specify the redesign.** Include sort order, scale, labels, grouping, and whether a table should accompany the chart.

5. **Write the stakeholder rationale.** One plain-English sentence explaining why the replacement is easier to read.

## Common failure modes

- **Replacing novelty with a different novelty.** The goal is clarity, not a more fashionable chart.

- **Keeping a funnel because the business process is a funnel.** A process metaphor does not make the funnel chart the best quantitative display.

- **Using stacked areas for component trends.** Moving baselines make all but the bottom series hard to compare.

- **Defending radar charts as compact.** Compactness is not success if each spoke uses weak comparison.

- **Overusing waterfalls.** Waterfalls are useful for explaining additive bridges, not every before/after comparison.

## References

- Stephen Few, *Show Me the Numbers*, chapter 12.
- Sibling skills: `few-smtn-relationship-chart-selector`, `few-smtn-graph-component-audit`.
- Complements `data-visualization` by providing a named replacement workflow for specific weak chart forms.
