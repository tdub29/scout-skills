
# FDE Lifecycle Architecture Map

Use this when the user needs to design, audit, or explain a data system end to end. The output is a lifecycle architecture map, not a tool recommendation.

## Artifact

Produce a lifecycle map with these sections:

1. **Consumer outcome** - the analytics, ML, operational, or reverse-ETL use case and its freshness, latency, and trust requirements.
2. **Lifecycle path** - source systems, storage, ingestion, transformation, and serving, with the owner and key design choice at each stage.
3. **Undercurrents** - security, data management, DataOps, orchestration, software engineering, architecture, and observability concerns that cross the whole path.
4. **Bottleneck diagnosis** - the stage most likely to fail the outcome and the evidence needed to confirm it.
5. **Next design decisions** - 3-7 ranked decisions with the tradeoff each decision resolves.

## Process

1. Start from the data consumer and work backward. Name who uses the data, what decision or product it supports, and what service level makes it useful.
2. Inventory each lifecycle stage. For each stage record the current system, owner, data grain, expected volume, failure modes, and downstream dependencies.
3. Treat storage as a lifecycle foundation, not a single stop. Call out every place data is persisted: source, queue, lake, warehouse, feature store, cache, mart, or export.
4. Overlay undercurrents. Governance, security, orchestration, observability, cost, and data quality must be assigned across stages, not left as generic platform concerns.
5. Decide whether the architecture is coherent. A coherent design has a clear consumer outcome, matching freshness and cost, explicit ownership, and a serving layer fit for use.

## Failure Modes

- **Tool-first architecture** - selecting a warehouse, lakehouse, stream processor, or orchestrator before mapping the lifecycle and consumer outcome.
- **Middle-stage blur** - treating ingestion, storage, and transformation as interchangeable and losing ownership of where validation, schema evolution, and recovery happen.
- **Serving afterthought** - building pipelines without specifying how analysts, ML systems, applications, or external consumers actually consume the data.
- **Undercurrent omission** - mentioning governance, security, or observability but not assigning concrete controls to lifecycle stages.
- **Single-path fantasy** - assuming one golden path serves batch BI, real-time operations, ad hoc analytics, and ML training equally well.

## Output Format

Return a concise architecture brief with a lifecycle table, an undercurrent checklist, a bottleneck diagnosis, and the next decisions. If evidence is missing, list the specific questions needed to complete the map.

## References

- Joe Reis and Matt Housley, *Fundamentals of Data Engineering* (O'Reilly, 2022), Chapters 1-2.
- Sibling skills: `fde-source-ingestion-contract`, `fde-batch-streaming-fit`.
