
# Data Mesh Federated Governance Charter

Use this when governance must scale across autonomous domains without reverting to central approval bottlenecks. The output is a federated governance charter and policy automation backlog.

## Artifact

Produce a charter containing:

1. **Federated body** - participating domain product owners, platform representatives, governance leads, decision rights, and meeting cadence.
2. **Global policies** - interoperability, privacy, access, quality, metadata, lineage, retention, and naming standards that all products must satisfy.
3. **Local autonomy rules** - decisions domains can make independently, such as internal models, implementation choices, and product-specific SLOs.
4. **Computational enforcement** - which policies become automated checks, templates, deployment gates, catalog requirements, or runtime controls.
5. **Exception process** - how domains request temporary exceptions, who approves them, and how debt is tracked.

## Process

1. Separate governance intent from governance mechanism. Ask which risks require consistent behavior across all data products.
2. Put domain owners in governance, not outside it. Federated governance requires policy authors who understand local data products and consumer needs.
3. Convert policies into computational controls where possible: metadata requirements, CI checks, access workflows, schema rules, quality thresholds, and lineage publication.
4. Preserve autonomy explicitly. Document which choices remain local so governance does not become hidden centralization.
5. Track policy outcomes. Measure reduction in access delays, quality incidents, privacy exceptions, interoperability failures, and manual approvals.

## Failure Modes

- **Committee centralization** - a renamed central governance board still approves every meaningful data decision.
- **Policy without code** - standards exist in documents but are not embedded in product creation, deployment, or access workflows.
- **Autonomy without interoperability** - domains move fast but produce incompatible, undiscoverable, or untrustworthy products.
- **No exception lifecycle** - exceptions become permanent shadow standards because expiry and remediation are not tracked.
- **Governance as compliance only** - policy focuses on control while ignoring discoverability, usability, and consumer trust.

## Output Format

Return the charter, decision-rights table, policy-to-control backlog, open exceptions, and the first 30/60/90-day governance rollout plan.

## References

- Zhamak Dehghani, *Data Mesh* (O'Reilly Early Release, 2021), federated computational governance principle.
- Sibling skills: `data-mesh-domain-ownership-map`, `data-mesh-data-product-usability-scorecard`, `data-mesh-self-serve-platform-map`.
