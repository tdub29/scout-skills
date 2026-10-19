# Few SMTN: Relationship Chart Selector

## When to use

Trigger when the user asks "what chart should I use" and the answer depends on the quantitative relationship being communicated. Use for business presentations, reports, analyses, and chart critiques where the current chart type may not match the relationship.

## The framework

Few treats graph choice as a relationship problem. The same data table can support different charts depending on which relationship the reader must understand. The artifact is not a chart gallery; it is a mapping from question -> relationship -> display form.

### Core relationship families

1. **Nominal comparison.** Compare values across unordered categories. Usually bars or dots.

2. **Time series.** Show change through ordered time. Usually lines for continuous trends, bars for discrete periods when magnitude comparison is primary.

3. **Ranking.** Show ordered magnitude from high to low. Usually sorted bars or dot plots.

4. **Part-to-whole.** Show components of a total. Use bars, stacked bars only with restraint, or tables when exact shares matter; avoid pies when precision or many slices matter.

5. **Deviation.** Show difference from a norm, target, prior period, or zero baseline. Use bars around a reference line, variance columns, or slope/line displays.

6. **Distribution.** Show spread, frequency, concentration, or outliers. Use histograms, box plots, strip plots, or frequency tables depending on audience sophistication.

7. **Correlation.** Show paired quantitative variables. Use scatterplots and make correlation limits explicit.

8. **Geospatial.** Show location-based patterns only when geography is analytically relevant; otherwise prefer non-map comparisons.

## How to apply

1. **Name the question.** Convert the business request into a relationship sentence: "Compare X across categories," "show X over time," "show how X relates to Y," etc.

2. **Classify the relationship.** Pick one primary family. If there are two, decide which is dominant and whether a second view is needed.

3. **Choose the display.** Recommend the simplest chart family that expresses that relationship with position/length before angle/area/color.

4. **Reject tempting alternatives.** Name at least one chart type that would be weaker and why.

5. **Specify the construction.** Include sort order, baseline/reference line, scale treatment, label strategy, and whether exact values belong in labels or a companion table.

## Common failure modes

- **Choosing by data shape instead of question.** A table with categories and values does not automatically mean pie, bar, or map. The relationship determines the graph.

- **Combining relationship types in one overloaded chart.** A stacked area chart that tries to show time series, part-to-whole, and ranking often serves none well.

- **Using maps for non-geographic questions.** If location is merely a category label, a bar chart usually beats a choropleth.

- **Using correlation charts to imply causation.** A scatterplot can show association, not causal proof. Say what evidence is missing.

- **Encoding many precise shares with pies.** Angle and area are weak for close comparisons; use bars or a table when precision matters.

## References

- Stephen Few, *Show Me the Numbers*, chapters 3 and 6.
- Sibling skills: `few-smtn-table-graph-fit`, `few-smtn-graph-component-audit`, `few-smtn-forsaken-chart-replacement`.
- Complements Bertin skills by applying relationship classification in business-report terms.
