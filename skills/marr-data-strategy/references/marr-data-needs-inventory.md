
# Marr: Data Needs Inventory

## When to Use

Use when a data initiative needs a practical answer to what data is needed before sourcing, buying, collecting, or integrating data.

## Do Not Use For

Schema design, SQL, warehouse modeling, or detailed data quality remediation.

## Framework

Strategic data collection starts from the use case and asks what exact data will answer the business question at acceptable cost, quality, latency, and governance burden. Inventory dimensions include concepts, internal/external sources, structured/unstructured form, freshness, accessibility, cost, quality, bias, permission, and substitute sources.

## How to Apply

1. Start from the use case objective and success metric.
2. List data concepts needed to answer key questions.
3. Map concepts to internal systems, external datasets, sensors, surveys, partners, public data, or dark archives.
4. Classify each source by structure, freshness, cost, accessibility, and governance burden.
5. Look for simpler substitutes before expensive unstructured or real-time data.
6. Identify gaps and how missing data could be created.
7. Prioritize sources by business value per unit of cost/risk.
8. State what will not be collected.

## Output Format

- Data requirements table.
- Gap list and unlock plan.
- Source prioritization: must-have, nice-to-have, defer, reject.
- Minimization decisions.
- Next steps for access, vendor, instrumentation, or quality work.

## Common Failure Modes

- Inventorying data that exists instead of data the use case needs.
- Choosing expensive unstructured data when a simple structured source works.
- Treating real-time data as inherently better without a real-time action.
- Ignoring dark data or overvaluing it before proving relevance.
- Buying external data without checking permissions and refresh cadence.
- Collecting personal data just in case.

## References

- Bernard Marr, Data Strategy, Second Edition, Chapters 9 and 10.
- Related carved skills: `marr-data-use-case-template`, `marr-data-strategy-canvas`, `marr-data-needs-inventory`, `marr-data-monetization-scan`, `marr-ethics-privacy-gate`, `marr-strategy-execution-risk-audit`.
