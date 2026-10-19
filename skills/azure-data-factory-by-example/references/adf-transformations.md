# ADF Transformations

Use this when deciding whether and how to transform data in ADF using Mapping Data Flows, Power Query activity, SQL, or Copy activity configuration.

## Artifact

Produce an ADF transformation design containing:

1. **Transformation placement decision** - Copy activity mapping, SQL/stored procedure, Mapping Data Flow, Power Query, or external Spark/Databricks/Synapse compute.
2. **Data Flow graph** - source streams, transformations, joins/lookups, derived columns, filters, selects, aggregates, exists checks, sinks, and reusable flowlets/functions.
3. **Execution plan** - debug requirement, Spark/Data Flow runtime implications, parameterization, sink behavior, and validation checks.
4. **Reuse boundary** - what should become a user-defined function, data flow library item, flowlet, or separate pipeline.

## Trigger checks

- The user is manipulating rows, combining/separating datasets, or doing low-code transformations in ADF.
- Mapping Data Flow transformations such as Filter, Lookup, Derived Column, Select, Sink, Aggregate, or Exists are involved.
- A Power Query mashup is being considered inside ADF.
- The user asks whether Copy activity is enough for a transformation.
- A dimension maintenance or lookup enrichment pattern is being built.

## How to apply

1. Decide if Copy activity is still appropriate. Use Copy for movement and light mapping; use Data Flow or SQL when row-level transformation, joins, or reusable transformation logic matter.
2. Choose Data Flow when the work benefits from visual Spark-backed transformation inside ADF and the runtime cost/startup is acceptable.
3. Choose Power Query when the user needs exploratory wrangling or already knows M, while noting ADF does not support every connector or M function.
4. Draw the transformation graph in source-to-sink order. Name each data stream and transformation's job.
5. Define data quality checks at the sink: row counts, duplicates, unmatched lookups, aggregate totals, rejected rows, and schema expectations.
6. Extract reuse only when the same transformation logic appears in multiple places. Prefer flowlets/functions over copy-pasting similar transformations.

## Sub-rules

- Data Flow debug mode is a development requirement, not a production guarantee.
- Lookups and exists checks should state expected match cardinality.
- Derived columns should carry business-readable names and avoid burying opaque rules in expressions.
- Select transformations are often where schema shape becomes the contract; document renames and exclusions.
- Dimension maintenance requires key, current-state, and history semantics before implementation.

## Common failure modes

- **Copy doing too much.** Complex row logic is squeezed into mappings or source queries where lineage and tests disappear.
- **Data Flow for tiny logic.** A Spark-backed Data Flow is used where SQL or Copy mapping would be simpler and cheaper.
- **Power Query portability assumption.** M copied from Power BI or Excel uses unsupported connectors/functions in ADF.
- **Lookup cardinality surprise.** Duplicate matches or missing reference rows change row counts without a visible guard.
- **Reusable logic copied by hand.** Similar flows drift because a flowlet or function was not extracted.

## Output format

Return:

1. **Placement decision:** Copy vs SQL vs Data Flow vs Power Query vs external compute.
2. **Transformation graph:** ordered table of inputs, transformations, outputs, and checks.
3. **Runtime/config notes:** debug, parameters, runtime cost, sink behavior.
4. **Validation plan:** tests and diagnostics before publication.

## References

- Richard Swinbank, *Azure Data Factory by Example* (Apress, 2024), chapters 7 and 9.
- Sibling refs: `adf-copy-activity-ingestion.md`, `adf-runtime-networking-security.md`.
