
# Data Mesh Data Product Usability Scorecard

Use this when a dataset must behave like a product for analytical consumers. The output is a usability scorecard and product contract.

## Artifact

Produce a data product scorecard with ratings and fixes for:

1. **Discoverable** - consumers can find the product, owner, purpose, schema, and usage examples.
2. **Addressable** - the product has a stable identifier, endpoint, location, or access path.
3. **Understandable** - semantics, grain, lineage, quality, caveats, and example queries are documented.
4. **Trustworthy** - freshness, quality metrics, tests, incident history, and SLOs are visible.
5. **Natively accessible** - consumers can use the product through suitable interfaces without bespoke producer intervention.
6. **Interoperable and secure** - shared standards, access controls, policies, and contracts allow safe composition.

## Process

1. Name the product's users and jobs-to-be-done. Product quality is judged by consumer experience, not by pipeline completion.
2. Score baseline usability characteristics from 0-3: absent, partial, usable, excellent. Require evidence for each score.
3. Draft a product contract: owner, purpose, domain, interfaces, schema/version, SLOs, quality checks, access policy, support path, and deprecation policy.
4. Prioritize fixes that reduce consumer friction first: discovery, trust, access, and semantic clarity usually beat internal refactors.
5. Define product health metrics: active consumers, time to discover, time to access, freshness adherence, quality incidents, and consumer satisfaction.

## Failure Modes

- **Table-as-product theater** - relabeling a table or dashboard as a data product without ownership, SLOs, documentation, or support.
- **Producer-centric metrics** - measuring pipeline success while ignoring consumer discovery, comprehension, and trust.
- **Opaque quality** - claiming trustworthiness without visible freshness, validation, incident, and lineage signals.
- **Handcrafted access** - each consumer needs a custom Slack thread or engineer intervention to use the data.
- **No lifecycle management** - breaking consumers because versioning, deprecation, and migration rules were not defined.

## Output Format

Return the scorecard, a product contract draft, the top usability gaps, and a prioritized improvement backlog.

## References

- Zhamak Dehghani, *Data Mesh* (O'Reilly Early Release, 2021), Chapter 5.
- Sibling skills: `data-mesh-domain-ownership-map`, `data-mesh-self-serve-platform-map`, `data-mesh-federated-governance-charter`.
