
# Data Mesh Self-Serve Platform Map

Use this when defining the platform that enables autonomous domain data product teams. The output is a capability map and platform backlog.

## Artifact

Produce a self-serve platform map with capabilities for:

1. **Data product development** - scaffolding, templates, local testing, CI/CD, versioning, and deployment.
2. **Data product operation** - observability, quality checks, incident routing, SLO tracking, cost visibility, and lineage.
3. **Data product consumption** - catalog, discovery APIs, access workflows, query/serve interfaces, examples, and support channels.
4. **Governance automation** - policy-as-code, metadata standards, access control, privacy rules, and interoperability checks.
5. **Developer experience metrics** - lead time, onboarding time, failure rate, reuse, and consumer satisfaction.

## Process

1. Identify the two platform customer groups: data product developers and data product consumers. Capture their top friction points separately.
2. Distinguish self-serve from centralized service. A capability is self-serve only if a domain can use it declaratively without waiting for a central team ticket.
3. Standardize interfaces, not every implementation detail. Preserve domain autonomy while making discovery, governance, access, and operations consistent.
4. Rank capabilities by coordination reduction. Prefer platform work that removes repeated handoffs, approvals, custom integrations, or manual policy checks.
5. Define the platform as a product. Assign ownership, roadmap, support model, adoption metrics, and deprecation rules.

## Failure Modes

- **Central team with a nicer portal** - requests still queue behind specialists, so the platform does not reduce coordination.
- **Capability buffet** - many tools exist, but no coherent paved road exists for building and operating a data product end to end.
- **Autonomy tax** - each domain must reinvent testing, access, deployment, metadata, or monitoring because the platform did not provide standards.
- **Governance bolt-on** - policies are reviewed manually after product creation instead of embedded in the platform workflow.
- **Developer-only bias** - platform improves producer workflows but leaves consumers unable to discover, understand, or access products.

## Output Format

Return the capability map, current gaps, platform backlog, ownership model, and 3-5 metrics for measuring platform product success.

## References

- Zhamak Dehghani, *Data Mesh* (O'Reilly Early Release, 2021), self-serve data platform principle.
- Sibling skills: `data-mesh-domain-ownership-map`, `data-mesh-data-product-usability-scorecard`, `data-mesh-federated-governance-charter`.
