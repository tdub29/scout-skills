
# FDE Source Ingestion Contract

Use this before implementing or repairing ingestion from a source system. The output is a contract between the data producer, ingestion owner, and data consumer.

## Artifact

Produce a source-ingestion contract containing:

1. **Source profile** - system owner, operational purpose, source type, data entities, write patterns, retention, and change cadence.
2. **Delivery contract** - extraction method, schema/version rules, freshness target, completeness expectation, backfill policy, and failure notification path.
3. **Operational constraints** - source load limits, query windows, API quotas, privacy constraints, cost limits, and disaster recovery expectations.
4. **Quality gates** - checks for schema, volume, nulls, referential integrity, duplicates, timeliness, and semantic validity.
5. **Consumer promises** - serving targets, allowed uses, documented caveats, and escalation path when the source changes.

## Process

1. Identify whether the source is operational, analytical, external, event-driven, file-based, or human-maintained. Different source classes fail differently.
2. Ask how the source generates state. Capture insert/update/delete semantics, event ordering, late data, idempotency keys, and history requirements.
3. Decide the ingestion style: batch extract, CDC, event stream, API sync, file drop, manual upload, or hybrid. Explain the tradeoff rather than naming a vendor.
4. Define schema evolution rules. Specify backward compatibility, deprecation period, versioned topics/files/tables, and who approves breaking changes.
5. Attach tests to promises. Every freshness, completeness, and quality promise needs a measurable check and owner.

## Failure Modes

- **Unowned upstream change** - the application team changes fields, meaning, or cadence without notifying downstream consumers.
- **Source overload** - analytical extraction harms the operational system because query windows, indexes, quotas, or replicas were not agreed upfront.
- **Backfill blindness** - the pipeline handles today's data but has no repeatable way to rebuild history after fixes or late-arriving source changes.
- **Schema-only contract** - fields are documented, but semantics, freshness, deletion behavior, and failure handling are not.
- **Consumerless ingestion** - data is copied because it exists, not because a named downstream outcome requires it.

## Output Format

Return the contract in sections, followed by a risk register with severity, owner, and mitigation for each unresolved source or ingestion risk.

## References

- Joe Reis and Matt Housley, *Fundamentals of Data Engineering* (O'Reilly, 2022), Chapters 2, 5, and 7.
- Sibling skills: `fde-lifecycle-architecture-map`, `fde-batch-streaming-fit`.
