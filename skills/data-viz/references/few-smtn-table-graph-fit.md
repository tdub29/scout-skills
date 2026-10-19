# Few SMTN: Table vs Graph Fit

## When to use

Trigger when the user has quantitative information and the first question is the medium: table, graph, or both. Typical cues: "should this be a table or chart," "how should I present these numbers," "this spreadsheet is hard to read," "do I need a graph," or "make this business report easier to understand."

Do not trigger for choosing between specific chart encodings after the graph decision is already made; use `few-smtn-relationship-chart-selector` for that.

## The framework

Few's core distinction is task fit. Tables serve precise lookup, many individual values, and mixed units. Graphs serve visual patterns, comparisons, shapes, exceptions, and relationships. Many weak business visuals fail because the author chose the medium that was easiest to produce rather than the medium that matches the reader's task.

### Four fit tests

1. **Lookup vs pattern.** If readers must retrieve exact values, rankings, IDs, or multiple attributes for a specific item, favor a table. If they must see trends, outliers, relative size, distribution, or correlation, favor a graph.

2. **Single value vs relationship.** One number or a short KPI statement rarely needs a graph. A relationship among values often does.

3. **Precision vs shape.** Tables preserve exactness; graphs trade exactness for shape recognition. Use both only when both are genuinely needed.

4. **Heterogeneous vs comparable units.** Mixed units, text labels, and long descriptions belong in a table. Comparable measures across categories, time, or paired variables usually belong in a graph.

## How to apply

1. **State the reader task.** Write one sentence: "The reader needs to..." Use verbs like look up, compare, rank, monitor, spot, explain, or decide.

2. **Classify the data.** Note whether values are exact lookup records, comparable quantitative series, mixed-unit business attributes, or a single KPI.

3. **Run the fit tests.** Decide table, graph, or paired table+graph.

4. **Specify the output.** For a table: identify row grain, column groups, sort order, and highlighting. For a graph: identify the relationship type and hand off to `few-smtn-relationship-chart-selector`. For both: say which artifact carries the story and which supports lookup.

5. **Return a fit verdict.** Include: recommended medium, why the rejected medium is weaker, and the minimum redesign needed.

## Common failure modes

- **Graphing lookup tasks.** A bar chart with 80 product IDs may look visual but makes exact lookup and scanning harder than a sorted table.

- **Tabulating pattern tasks.** A 12-month sales table can hide seasonality or trend breaks that a line graph would reveal immediately.

- **Using both without role separation.** A chart pasted above a table that says the same thing doubles clutter. Pair them only when the graph shows the pattern and the table supports exact lookup.

- **Letting available software decide.** If the BI tool defaults to a pie, gauge, or crosstab, ignore the default and re-run the reader-task test.

- **Confusing executive brevity with graphical display.** Sometimes the right answer is a sentence with one number, not a miniature chart.

## References

- Stephen Few, *Show Me the Numbers*, chapters 3-4.
- Sibling skills: `few-smtn-relationship-chart-selector`, `few-smtn-business-table-design`, `few-smtn-graph-component-audit`, `few-smtn-forsaken-chart-replacement`.
- Complements `data-visualization` by deciding the medium before chart construction.
