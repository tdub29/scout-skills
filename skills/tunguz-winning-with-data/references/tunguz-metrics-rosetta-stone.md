
# Tunguz: Metrics Rosetta Stone

## When to use

Trigger when the organization needs shared metric language: "define our metrics," "everyone calculates churn differently," "one equation that defines the business," "metric glossary," "KPI definitions," or "why do dashboards disagree."

## The framework

Tunguz uses the Rosetta Stone metaphor for shared business language. Data becomes useful when people agree what metrics mean and how they compose into the business model. The One Equation makes the operating model explicit enough to debate and improve.

### Metric alignment rules

1. **Define terms operationally.** A metric definition must say inclusion/exclusion, time window, source, grain, and formula.

2. **Connect metrics to the business equation.** Revenue, retention, usage, acquisition, margin, and satisfaction should compose into a model of how the business works.

3. **Assign ownership.** Each metric needs a business owner and a data owner.

4. **Publish one canonical version.** Definitions scattered across slides, dashboards, and spreadsheets invite brawls.

5. **Track interpretation notes.** Known caveats, seasonality, lag, and data quality limits should travel with the metric.

## How to apply

1. **Inventory disputed metrics.** List names, current formulas, dashboards using them, and teams relying on them.

2. **Draft definitions.** For each metric, specify formula, source, grain, filters, window, refresh, owner, and caveats.

3. **Build the business equation.** Show how the core metrics relate mathematically or causally.

4. **Resolve conflicts.** Decide canonical names, deprecated variants, and migration notes.

5. **Return the Rosetta Stone.** Provide a compact glossary plus the one-equation diagram in text form.

## Common failure modes

- **Defining metrics only by formula.** A formula without source, grain, exclusions, and timing still leaves ambiguity.

- **Letting every team keep local definitions.** Local nuance may be valid, but canonical metrics need canonical names and variants clearly labeled.

- **Choosing a vanity equation.** The one equation should explain how the business creates value, not merely restate a dashboard.

- **No owner.** Ownerless metrics decay when products, systems, and business models change.

- **Hiding caveats.** Caveats not documented in the glossary reappear as mistrust in meetings.

## References

- Tomasz Tunguz and Frank Bien, *Winning with Data*, chapter 5.
- Sibling skills: `tunguz-data-decision-meeting`, `tunguz-data-culture-maturity`, `tunguz-data-supply-chain-audit`.
- Complements KPI/dashboard skills by making definitions stable before visualization.
