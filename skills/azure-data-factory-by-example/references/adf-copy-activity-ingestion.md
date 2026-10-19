# ADF Copy Activity Ingestion

Use this when designing or reviewing an ADF Copy activity, metadata-driven ingestion pattern, or CDC ingestion flow. The output is a copy design that makes source, sink, schema, conversion, performance, and operational behavior explicit.

## Artifact

Produce a copy activity ingestion design containing:

1. **Source contract** - linked service, dataset, path/table/query, file format, schema expectation, late/missing data behavior, and secrets strategy.
2. **Sink contract** - target table/file, write mode, pre-copy script or truncate policy, schema mapping, key/idempotency expectation, and validation query.
3. **Schema handling** - mapping mode, collection reference for nested data, schema drift tolerance, and explicit type conversions where source and sink types differ.
4. **Performance settings** - data integration units, copy parallelism, partitioning/file batching, and why the default is or is not enough.
5. **Repeatability pattern** - whether this is a one-off copy, reusable parameterized copy, metadata-driven copy, or CDC pipeline.

## Trigger checks

- Blob/file to Azure SQL or Synapse load.
- Copy activity mapping, schema drift, JSON/CSV/Parquet, or collection reference issues.
- Questions about DIUs, copy parallelism, or slow copy performance.
- Metadata-driven data copy or change data capture in ADF.
- A pipeline needs to copy many similar sources using shared configuration.

## How to apply

1. Classify the movement: unstructured blob copy, structured file to table, semi-structured flattening, format conversion, metadata-driven extract, or CDC.
2. Specify source and sink datasets separately from linked services. Do not bury path, table, or schema decisions in connection setup.
3. Decide whether schema is inferred, persisted, mapped manually, or drift-tolerant. For nested JSON, state the collection reference and flattening rule.
4. Choose the write behavior. Truncate-before-load, append, upsert, CDC, or history-preserving copy are different contracts.
5. Add validation at the sink: row count, rejected/skipped rows, key uniqueness, type conversion checks, and spot checks against source.
6. Tune only after correctness is stable. Adjust DIUs or parallelism when the bottleneck is copy throughput, not source limits or sink contention.

## Sub-rules

- Copy is primarily data movement. Use Data Flow, SQL, or Power Query when row-level transformations become the core problem.
- Treat type conversion as a data contract, not an incidental UI setting.
- For reusable ingestion, parameterize locations and table names deliberately instead of cloning activities.
- Metadata-driven copy needs a control table that is itself governed and validated.
- CDC should state polling/checkpoint behavior, target merge semantics, and monitoring path.

## Common failure modes

- **Truncate without recovery.** A pre-copy truncate runs before the source is validated or before the sink can be rebuilt.
- **Implicit schema drift.** The pipeline "works" until a new column, nested field, or type arrives and silently lands wrong.
- **Over-tuned copy.** DIUs or parallelism are raised before checking source throttling, sink locks, and file sizing.
- **Cloned activities.** Dozens of almost-identical copies create drift; use parameters or metadata-driven copy.
- **CDC without semantics.** Change detection is enabled without defining deletes, updates, replay, or idempotency.

## Output format

Return:

1. **Copy pattern:** one sentence naming the selected pattern.
2. **Source-to-sink contract:** table of source, activity, sink, schema, and validation choices.
3. **ADF configuration:** linked services, datasets, activity settings, parameters, and performance knobs.
4. **Risks and tests:** the failure modes to verify before publishing.

## References

- Richard Swinbank, *Azure Data Factory by Example* (Apress, 2024), chapters 3 and 13.
- Sibling refs: `adf-dynamic-control-flow.md`, `adf-transformations.md`, `adf-runtime-networking-security.md`.
