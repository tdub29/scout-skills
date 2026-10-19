
# Kleppmann - Stream, Batch, and Derived Data Choice

## The Framework

Use this skill to produce: **A derived-data flow decision with freshness SLA, source of truth, replay/backfill plan, event-time semantics, and failure recovery.**

This is not a summary route. It should fire only when the user needs the artifact above and the request matches the trigger surface in the frontmatter.

## Trigger Checks

- A batch job is too stale but streaming may be overkill
- A streaming pipeline cannot be backfilled
- Dashboards need both historical correction and fresh events
- Exactly-once language is hiding idempotency gaps
- Materialized views drift from source data

## How To Apply

- State the freshness requirement and business consequence of delay.
- Identify source of truth, derived outputs, and whether outputs can be rebuilt.
- Choose batch, stream, microbatch, or hybrid and define replay semantics.
- Specify event time, late data, idempotency, and backfill behavior.

## Sub-Rules

- Batch processing is excellent for complete, repeatable recomputation.
- Stream processing reduces latency but must still handle replay and late events.
- Derived data systems should be rebuildable or have explicit repair procedures.
- Exactly-once effects usually require idempotent writes, deduplication, and transactional boundaries.

## Common Failure Modes

- Freshness theater: streams are adopted although daily decisions are enough.
- No replay path: bug fixes cannot correct previously emitted derived data.
- Processing-time mistake: late events are treated as current reality.
- Dual-pipeline drift: batch and stream code compute the same metric differently.

## Overlap Guardrails

Overlaps with fde-batch-streaming-fit; use this only when the artifact is a DDIA-derived data/replay/materialization decision, not general pipeline freshness advice.

## Output Format

Return the artifact in this order:

1. **Decision context:** one paragraph naming the business/system decision.
2. **Working table or checklist:** the concrete rows, columns, scores, or mappings required by the artifact.
3. **Recommendation:** the chosen design or next action and why.
4. **Risks and tests:** the top failure modes to verify before adoption.

## References

- Martin Kleppmann - Designing Data-Intensive Applications, 2nd ed. early release (O'Reilly, 2025/2026), Chapters 10-11.
- Sibling skills: references/kleppmann-rsm-tradeoff-audit.md, references/kleppmann-storage-index-choice.md, references/kleppmann-replication-topology-choice.md, references/kleppmann-partitioning-hotspot-audit.md, references/kleppmann-transaction-isolation-anomaly-audit.md, references/kleppmann-consensus-coordination-boundary.md, references/kleppmann-schema-evolution-compatibility.md.
