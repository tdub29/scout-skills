
# Kleppmann - Partitioning and Hotspot Audit

## The Framework

Use this skill to produce: **A partitioning audit with key candidates, skew risks, query locality impact, rebalancing plan, and hotspot mitigations.**

This is not a summary route. It should fire only when the user needs the artifact above and the request matches the trigger surface in the frontmatter.

## Trigger Checks

- A tenant or customer causes one shard to melt
- Choosing hash vs range partitioning
- A query needs data from many partitions
- Rebalancing threatens downtime
- Secondary indexes behave differently after sharding

## How To Apply

- List dominant access paths and whether they need co-located data.
- Profile key cardinality, skew, temporal clustering, and hot-key risk.
- Choose hash, range, composite, or hierarchical partitioning with a reason.
- Define rebalancing, routing metadata, and secondary-index behavior.

## Sub-Rules

- Hash partitioning balances load but weakens range locality.
- Range partitioning supports ordered scans but risks time or key hotspots.
- Composite keys can combine locality and spread if the prefix is chosen carefully.
- Rebalancing is part of the design, not a later operational detail.

## Common Failure Modes

- Tenant-id-only shard key: one large tenant dominates a partition.
- Timestamp range hotspot: all current writes go to the newest partition.
- Scatter-gather surprise: every user query fans out to all shards.
- Manual split panic: no rebalancing strategy until the cluster is already overloaded.

## Overlap Guardrails

Do not use for analytics table partition pruning alone; use when the system architecture shards ownership or load across nodes.

## Output Format

Return the artifact in this order:

1. **Decision context:** one paragraph naming the business/system decision.
2. **Working table or checklist:** the concrete rows, columns, scores, or mappings required by the artifact.
3. **Recommendation:** the chosen design or next action and why.
4. **Risks and tests:** the top failure modes to verify before adoption.

## References

- Martin Kleppmann - Designing Data-Intensive Applications, 2nd ed. early release (O'Reilly, 2025/2026), Chapter 6.
- Sibling skills: references/kleppmann-rsm-tradeoff-audit.md, references/kleppmann-storage-index-choice.md, references/kleppmann-replication-topology-choice.md, references/kleppmann-transaction-isolation-anomaly-audit.md, references/kleppmann-stream-batch-derived-data-choice.md, references/kleppmann-consensus-coordination-boundary.md, references/kleppmann-schema-evolution-compatibility.md.
