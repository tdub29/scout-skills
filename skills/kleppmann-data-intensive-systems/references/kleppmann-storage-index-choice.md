
# Kleppmann - Storage and Index Choice

## The Framework

Use this skill to produce: **A storage/index decision matrix mapping workload reads/writes/ranges/aggregations to candidate structures and rejected alternatives.**

This is not a summary route. It should fire only when the user needs the artifact above and the request matches the trigger surface in the frontmatter.

## Trigger Checks

- Choosing between Postgres indexes, Elasticsearch, ClickHouse, or a KV store
- Write amplification or compaction is hurting a workload
- Range scans and point lookups have different needs
- A dashboard workload is slow on row-oriented storage
- Secondary indexes make writes unexpectedly expensive

## How To Apply

- Inventory query shapes: point lookup, range scan, join, search, aggregate, time-series.
- Inventory write pattern: insert-only, update-heavy, delete-heavy, random vs sequential.
- Map each pattern to storage/index candidates and operational costs.
- Choose the simplest structure that satisfies the dominant access paths.

## Sub-Rules

- Log-structured storage favors high write throughput but pays compaction/read-amplification costs.
- B-trees support ordered ranges and stable point lookups with page-update tradeoffs.
- Secondary indexes are separate data structures with write and consistency costs.
- Column-oriented storage and materialized aggregates fit analytical scans, not arbitrary OLTP mutation.

## Common Failure Modes

- Index everything: write path and storage balloon without a workload reason.
- Search engine as database: full-text convenience hides transactional and source-of-truth gaps.
- Analytics on row-store defaults: scans too many irrelevant columns for wide historical queries.
- Average-query design: ignores tail queries that require different indexes.

## Overlap Guardrails

Do not use for Prisma API syntax or SQL tuning in a single query; use for architecture-level storage/index choice.

## Output Format

Return the artifact in this order:

1. **Decision context:** one paragraph naming the business/system decision.
2. **Working table or checklist:** the concrete rows, columns, scores, or mappings required by the artifact.
3. **Recommendation:** the chosen design or next action and why.
4. **Risks and tests:** the top failure modes to verify before adoption.

## References

- Martin Kleppmann - Designing Data-Intensive Applications, 2nd ed. early release (O'Reilly, 2025/2026), Chapter 3.
- Sibling skills: references/kleppmann-rsm-tradeoff-audit.md, references/kleppmann-replication-topology-choice.md, references/kleppmann-partitioning-hotspot-audit.md, references/kleppmann-transaction-isolation-anomaly-audit.md, references/kleppmann-stream-batch-derived-data-choice.md, references/kleppmann-consensus-coordination-boundary.md, references/kleppmann-schema-evolution-compatibility.md.
