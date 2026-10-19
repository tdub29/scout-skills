# Few Dashboard: Display Media Selector

## When to use

Trigger when a dashboard uses gauges, thermometers, pies, oversized charts, or an inconsistent widget zoo and the user needs the right compact display for each KPI. Also trigger on bullet graph or sparkline questions in dashboard context.

## The framework

Dashboards need media that communicate status, context, and change in little space. Few's display-media discipline favors compact, comparable, low-decoration forms over metaphor-heavy widgets.

### Display decisions

1. **Single current value.** Use text when the number alone is enough; add status encoding only if thresholds matter.

2. **Actual vs target plus qualitative ranges.** Use bullet graphs instead of gauges when comparing performance against target and context bands.

3. **Short trend history.** Use sparklines or compact lines when direction and shape matter more than exact values.

4. **Category comparison.** Use small bars/dots when comparing items on the dashboard.

5. **Detailed lookup.** Use a compact table only when exact values or multiple fields must be scanned.

6. **Alert/status.** Use icons or color sparingly and pair them with labels or position where possible.

## How to apply

1. **List every KPI or data item.** Include current value, target, prior period, range, trend, and action threshold if known.

2. **Determine the required context.** None, target, historical trend, peer comparison, threshold band, or exact detail.

3. **Select the medium.** Map each item to text, bullet graph, sparkline, bar/dot, line, compact table, or status indicator.

4. **Normalize related media.** Use consistent scales and repeated forms for comparable metrics.

5. **Return a media matrix.** Columns: metric, monitoring question, required context, recommended medium, rejected medium, and design notes.

## Common failure modes

- **Gauge addiction.** Gauges waste space, make comparison hard, and often encode one value with too much decoration.

- **Sparkline without scale context.** A sparkline needs enough labeling or reference to prevent ambiguous movement.

- **Bullet graph overload.** Bullet graphs work best for actual vs target/ranges; do not use them for every metric by habit.

- **Meaningless widget variety.** A dashboard should not use different media just to look varied. Similar metrics should look similar.

- **Using pies for dashboard monitoring.** Pies consume space and make close comparisons difficult; use bars or tables for shares.

## References

- Stephen Few, *Information Dashboard Design*, chapter 6.
- Sibling skills: `few-dashboard-thirteen-mistakes-audit`, `few-dashboard-perception-layout`.
- Related: `few-smtn-relationship-chart-selector` for non-dashboard chart selection.
