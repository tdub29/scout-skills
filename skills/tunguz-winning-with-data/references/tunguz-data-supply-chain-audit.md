
# Tunguz: Data Supply Chain Audit

## When to use

Trigger when the problem is how data flows through the organization, not one specific query. Cues: "data pipeline bottleneck," "analyst backlog," "rogue spreadsheets," "data fragmentation," "single source of truth," "semantic layer," or "why does it take so long to answer questions."

## The framework

Tunguz argues that modern companies need a data supply chain: collection, storage, modeling, access, literacy, and decision use. Breaks in any link create breadlines, obscurity, fragmentation, or brawls.

### Supply-chain links

1. **Collection.** Are events, transactions, CRM fields, and product behaviors captured with enough completeness and quality?

2. **Movement and storage.** Is data reliably delivered into a warehouse or equivalent shared environment?

3. **Modeling and definition.** Are key entities and metrics modeled once, with shared business logic?

4. **Access and tooling.** Can business users explore trusted data without creating uncontrolled copies?

5. **Use in operations.** Does the data feed meetings, alerts, experiments, forecasts, and frontline workflows?

## How to apply

1. **Map the path.** Source systems -> ingestion -> warehouse -> modeling layer -> BI/analysis -> decision forum.

2. **Mark ownership.** Name the owner of each link and the SLA/freshness expectation.

3. **Identify failure mode.** Breadline, obscurity, fragmentation, brawl, stale data, or trust gap.

4. **Prioritize bottlenecks.** Score each by decision impact and repair effort.

5. **Return a repair plan.** Include quick fixes, structural fixes, owners, and one metric that proves the supply chain improved.

## Common failure modes

- **Optimizing ingestion while definitions are broken.** Faster pipelines do not solve metric brawls.

- **Self-service without governance.** Giving everyone raw access can amplify fragmentation.

- **Centralizing every question.** A data team that answers every simple request becomes the bottleneck it was meant to remove.

- **Ignoring operational use.** A beautiful model that never changes decisions is supply-chain inventory sitting unused.

- **No freshness contract.** Users distrust data when they do not know whether it is current enough for the decision.

## References

- Tomasz Tunguz and Frank Bien, *Winning with Data*, chapters 2-4 and 7.
- Sibling skills: `tunguz-data-culture-maturity`, `tunguz-metrics-rosetta-stone`, `tunguz-data-literacy-program`.
- Complements warehouse and SQL skills by staying at the workflow/ownership layer.
