
# Data Mesh Domain Ownership Map

Use this when a data organization needs to decide which domain owns which analytical data products. The output is an ownership map, not a reorg slogan.

## Artifact

Produce a domain ownership map with:

1. **Domain inventory** - business capabilities, operational systems, key entities, and analytical use cases.
2. **Data archetype classification** - source-aligned, aggregate, or consumer-aligned data for each candidate product.
3. **Ownership assignment** - accountable domain, data product owner, producer team, consumers, and escalation path.
4. **Boundary decisions** - what is hidden as internal pipeline implementation versus exposed as stable product interfaces.
5. **Transition slice** - the first domain/product to move, with expected coordination reduction and risk.

## Process

1. Start from business domains, not technical pipeline stages. Use bounded contexts, operational ownership, and decision rights to identify candidate domains.
2. Classify each dataset by archetype. Source-aligned data belongs close to the operational source; aggregate data composes across domains; consumer-aligned data serves a specific use case.
3. Reject universal single-source-of-truth claims when multiple domain models are legitimate. Instead, document connected models, semantic differences, and consumers.
4. Push ownership upstream only when the domain can own quality, documentation, access, and evolution, not merely host a table name.
5. Make pipelines internal. Consumers should depend on data product interfaces and contracts, not on hidden transformation steps.

## Failure Modes

- **Technical partitioning in disguise** - calling ingestion, transformation, and reporting teams "domains" while preserving the old pipeline handoff model.
- **Ownership without authority** - naming a domain owner who cannot prioritize data work, control product changes, or negotiate consumer contracts.
- **Single-model coercion** - forcing all domains into one canonical enterprise model when local domain semantics differ for valid reasons.
- **Pipeline exposure** - making consumers coordinate with internal jobs rather than stable data product interfaces.
- **Big-bang mesh** - trying to redistribute all data at once instead of choosing a bounded transition slice.

## Output Format

Return a table of domains and candidate data products, ownership decisions, contested boundaries, and the recommended first transition slice.

## References

- Zhamak Dehghani, *Data Mesh* (O'Reilly Early Release, 2021), Chapter 4.
- Sibling skills: `data-mesh-data-product-usability-scorecard`, `data-mesh-self-serve-platform-map`, `data-mesh-federated-governance-charter`.
