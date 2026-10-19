---
name: fde-data-lifecycle
description: Apply Reis and Housley's data engineering lifecycle, source-ingestion contracts, and batch/streaming fit from Fundamentals of Data Engineering. Triggers: data platform design, pipeline audit, lifecycle map, source systems, ingestion contract, schema evolution, batch vs streaming, Kafka/Flink, CDC, real-time data, freshness requirements, microbatch, data contract, upstream ownership. Load the matching reference file when a specific framework is needed.
---

# fde-data-lifecycle

Book provenance: **Joe Reis and Matt Housley - Fundamentals of Data Engineering (O'Reilly, 2022)**. Load the matching `references/*.md` file when a specific framework is needed.

## When to use

Use this hub when the user's question matches any sub-framework trigger in the frontmatter description. Route to **one** reference file, read it fully, then execute that framework's process and output format.

Do not improvise a hybrid of multiple frameworks unless the user explicitly asks for a combined pass.

## Quick routing

| User cue (examples) | Reference |
| Lifecycle map, platform design, end-to-end architecture, undercurrents | `references/lifecycle-architecture-map.md` |
| Source system, ingestion contract, CDC, schema evolution, upstream | `references/source-ingestion-contract.md` |
| Batch vs streaming, real-time, latency, Kafka, microbatch | `references/batch-streaming-fit.md` |

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

- [references/lifecycle-architecture-map.md](references/lifecycle-architecture-map.md)
- [references/source-ingestion-contract.md](references/source-ingestion-contract.md)
- [references/batch-streaming-fit.md](references/batch-streaming-fit.md)

- **Book:** Joe Reis and Matt Housley - Fundamentals of Data Engineering (O'Reilly, 2022)