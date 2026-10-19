---
name: kleppmann-data-intensive-systems
description: Apply Kleppmann's Designing Data-Intensive Applications to OLTP and distributed-systems internals: storage/index choice, replication topology, partitioning/hotspot audits, transaction isolation/anomaly audits, consensus and coordination boundaries, schema evolution compatibility, stream/batch derived data, and reliability/scalability/maintainability tradeoffs. Triggers: storage engine choice, LSM vs B-tree, index design, replication, leader/follower, multi-leader, leaderless, partitioning, sharding, hotspot, transactions, isolation levels, serializability, anomalies, consensus, coordination, linearizability, schema evolution, backward/forward compatibility, stream vs batch, derived data, CDC, event sourcing, distributed systems design. Distinct from kimball-dimensional-modeling (analytics/warehouse star schemas). Sibling hubs: fde-data-lifecycle and data-mesh-principles for platform/engineering; dama-data-management, nigd-non-invasive-governance, and mcgilvray-data-quality-project for governance and quality. Load the matching reference file when a specific framework is needed.
---

# kleppmann-data-intensive-systems

Book provenance: **Martin Kleppmann - Designing Data-Intensive Applications**. Load the matching `references/*.md` file when a specific framework is needed.

## When to use

Use this hub when the user's question matches any sub-framework trigger in the frontmatter description. Route to **one** reference file, read it fully, then execute that framework's process and output format.

Do not improvise a hybrid of multiple frameworks unless the user explicitly asks for a combined pass.

## Quick routing

| User cue (examples) | Reference |
| Reliability/scalability/maintainability tradeoffs, system-level architecture audit, nonfunctional goals in tension | `references/kleppmann-rsm-tradeoff-audit.md` |
| Storage engine or index choice, LSM vs B-tree, OLTP vs analytics storage, secondary indexes, query pattern fit | `references/kleppmann-storage-index-choice.md` |
| Schema/encoding evolution, backward/forward compatibility, Avro/Protobuf/Thrift, rolling upgrades, message format changes | `references/kleppmann-schema-evolution-compatibility.md` |
| Replication topology, single-leader/multi-leader/leaderless, sync vs async, replication lag, read-your-writes | `references/kleppmann-replication-topology-choice.md` |
| Partitioning/sharding strategy, hotspots/hot keys, rebalancing, partition by hash vs range, skew | `references/kleppmann-partitioning-hotspot-audit.md` |
| Transaction isolation levels, anomalies, dirty/non-repeatable/phantom reads, write skew, serializability needs | `references/kleppmann-transaction-isolation-anomaly-audit.md` |
| Consensus/coordination boundary, linearizability, leader election, distributed locks, where to require agreement | `references/kleppmann-consensus-coordination-boundary.md` |
| Stream vs batch derived data, CDC, event sourcing, materialized views, reprocessing, dataflow design | `references/kleppmann-stream-batch-derived-data-choice.md` |

## How to apply

1. Match the user request to a row in **Quick routing** (or the description triggers).
2. Read the corresponding file under `references/`.
3. Follow that reference's artifact, process, failure modes, and output format.
4. Return the reference's output artifact; add hub-level manipulation-risk or cross-reference notes only when the reference requires it.

## Common failure modes (hub-level)

- **Wrong reference** - loading one sub-framework when another row in Quick routing fits better.
- **Router-only answer** - summarizing the hub without loading the reference's full framework.
- **Retired atomic names** - legacy per-framework skill folders were collapsed into this hub; use `references/` only.
- **Skipping evidence** - each reference requires evidence-backed scores and explicit unknowns; do not default to parity.

## References

- [references/kleppmann-rsm-tradeoff-audit.md](references/kleppmann-rsm-tradeoff-audit.md)
- [references/kleppmann-storage-index-choice.md](references/kleppmann-storage-index-choice.md)
- [references/kleppmann-schema-evolution-compatibility.md](references/kleppmann-schema-evolution-compatibility.md)
- [references/kleppmann-replication-topology-choice.md](references/kleppmann-replication-topology-choice.md)
- [references/kleppmann-partitioning-hotspot-audit.md](references/kleppmann-partitioning-hotspot-audit.md)
- [references/kleppmann-transaction-isolation-anomaly-audit.md](references/kleppmann-transaction-isolation-anomaly-audit.md)
- [references/kleppmann-consensus-coordination-boundary.md](references/kleppmann-consensus-coordination-boundary.md)
- [references/kleppmann-stream-batch-derived-data-choice.md](references/kleppmann-stream-batch-derived-data-choice.md)

- **Book:** Martin Kleppmann - Designing Data-Intensive Applications