# Few SMTN: Business Table Design

## When to use

Trigger when the artifact is a table and the user wants it easier to read, compare, or publish. Cues: "clean up this table," "make this spreadsheet readable," "table design," "financial table formatting," "too many gridlines," or "how should I organize these rows and columns."

## The framework

A good business table is an interface for either lookup or comparison. Few's table discipline removes decorative noise, organizes values by meaning, and makes the reader's scan path obvious. The table is successful when readers can answer the intended question with minimal eye travel and no decoding.

### Five table design rules

1. **Set the row grain.** Each row should represent one consistent entity, period, transaction, account, or category. Mixed grain creates false comparisons.

2. **Group by meaning.** Columns should be clustered by semantic role: identifiers, measures, variances, percentages, notes. Do not interleave unrelated units.

3. **Sort by use.** Alphabetical order helps lookup; descending quantitative order helps comparison; process order helps workflows; time order helps sequence.

4. **Reduce non-data ink.** Thin or remove gridlines, heavy borders, zebra clutter, redundant symbols, and repeated units. Use whitespace and alignment first.

5. **Control precision and emphasis.** Show only useful decimals; align numbers by decimal; reserve highlighting for values the reader should notice.

## How to apply

1. **Identify the primary use.** Lookup, comparison, exception finding, reconciliation, or presentation summary.

2. **Audit structure.** Check row grain, column grouping, sort order, and unit consistency.

3. **Audit formatting.** Check alignment, precision, repeated labels, gridlines, color, negative numbers, totals/subtotals, and whitespace.

4. **Design the repair.** Provide a rewritten structure: row order, column order, grouping headers, number formats, and emphasis rules.

5. **Return a table spec.** Include one sentence explaining how the revised table changes the reader's scan path.

## Common failure modes

- **Overformatting.** Thick borders, shaded cells, zebra stripes, and centered numbers compete with the values.

- **Decorating totals like data.** Totals, subtotals, and calculated rows need clear hierarchy, not arbitrary color.

- **False precision.** Four decimals in an executive table imply accuracy and importance that may not exist.

- **Mixed units without grouping.** Dollars, percentages, counts, dates, and status text in one visual stream make comparison error-prone.

- **Sorting against the task.** Alphabetical rows are useful for lookup but often terrible for ranking or exception detection.

## References

- Stephen Few, *Show Me the Numbers*, chapters 4 and 8.
- Sibling skills: `few-smtn-table-graph-fit`, `few-smtn-relationship-chart-selector`.
- Complements `business-intelligence` by turning BI tables into readable communication artifacts.
