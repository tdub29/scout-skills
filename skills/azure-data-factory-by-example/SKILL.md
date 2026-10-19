---
name: azure-data-factory-by-example
description: Apply Richard Swinbank's Azure Data Factory by Example implementation playbook to design, build, deploy, and operate ADF pipelines. Use when the user is working in Azure Data Factory, Synapse pipelines, or Fabric Data Factory and needs a practical pipeline design, copy activity configuration, linked service and dataset model, dynamic content expression, parameterization scheme, Key Vault secret pattern, control-flow design, Data Flow or Power Query transformation, integration runtime decision, private endpoint or self-hosted IR setup, Git publishing workflow, ARM or Azure DevOps deployment, trigger selection, monitoring, Log Analytics, alerts, metadata-driven copy, or CDC ingestion plan. This is tool-specific and operational: output is a routed ADF implementation artifact plus risk checks. Do not trigger for pure SQL query tuning, dimensional modeling, warehouse architecture in the abstract, or Power BI DAX unless the ADF pipeline itself is the work surface.
---

# Azure Data Factory by Example

Book provenance: **Richard Swinbank - Azure Data Factory by Example: Practical Implementation for Data Engineers (Apress, 2024)**. Load the matching `references/*.md` file when a specific ADF implementation surface is needed.

## When to use

Use this hub when the user is designing, debugging, documenting, or deploying an Azure Data Factory pipeline or a close sibling surface such as Synapse pipelines or the Fabric Data Factory experience. Route to **one** reference file, read it fully, then produce the reference's concrete artifact.

Prefer the broader sibling skills when the user is not asking about ADF mechanics:

- `fde-data-lifecycle` for source contracts, ingestion architecture, batch vs streaming, and platform-level lifecycle decisions.
- `kimball-dimensional-modeling` for star schemas, grain, dimensions, fact tables, and slowly changing dimensions.
- SQL skills for T-SQL correctness, Synapse view definitions, and query optimization.

## Quick routing

| User cue (examples) | Reference |
|---|---|
| New factory, ADF Studio, Git mode, resource groups, linked services, datasets, pipelines, activities, debug runs, "how are ADF objects related?" | `references/adf-pipeline-resource-model.md` |
| Copy activity, blob to SQL, file ingestion, source/sink datasets, schema mapping, schema drift, type conversion, DIUs, copy parallelism, metadata-driven copy, CDC | `references/adf-copy-activity-ingestion.md` |
| Dynamic content, expressions, system variables, activity output, Lookup, variables, parameters, Key Vault, Execute Pipeline, dependency conditions, If/Switch/ForEach, Fail activity | `references/adf-dynamic-control-flow.md` |
| Mapping Data Flows, low-code Spark transformation, Filter/Lookup/Derived Column/Select/Sink, dimension maintenance, locals, aggregate, exists, Power Query mashups, flowlets | `references/adf-transformations.md` |
| Integration runtimes, AutoResolve, region-specific Azure IR, managed VNet, managed private endpoint, self-hosted IR, local file system, Azure-SSIS IR, SSIS package lift, managed Airflow | `references/adf-runtime-networking-security.md` |
| Publish, Git collaboration, production factory, ARM template, deployment parameters, Azure DevOps pipeline, resource dependencies, schedule/tumbling/event triggers, monitoring, Log Analytics, alerts | `references/adf-deployment-operations.md` |

## How to apply

1. Match the user's ADF problem to a row in **Quick routing**.
2. Read the selected reference file completely before answering or editing.
3. Produce the reference's artifact, not a generic summary.
4. Add a short boundary note when the request crosses into SQL, warehouse modeling, Power BI, governance, or data quality, and route that part to the relevant sibling skill.

## Common failure modes

- **Router-only answer.** Do not stop after saying which reference applies. Load the reference and produce the concrete plan, checklist, or design.
- **Feature inventory instead of implementation.** ADF has many resource types. The answer must resolve the next configuration decision and call out the risk checks.
- **Secret leakage.** Treat linked service credentials and connection strings as Key Vault references or managed identity decisions, not text to paste into a skill response.
- **Ignoring environment split.** Debug mode, Git artifacts, published factory resources, and production triggers are different states. Name which one the user is changing.
- **Overlapping SQL work.** If the issue is a Synapse view, stored procedure, or query plan rather than the ADF orchestration around it, hand off to the SQL repo conventions or SQL skills.

## References

- [references/adf-pipeline-resource-model.md](references/adf-pipeline-resource-model.md)
- [references/adf-copy-activity-ingestion.md](references/adf-copy-activity-ingestion.md)
- [references/adf-dynamic-control-flow.md](references/adf-dynamic-control-flow.md)
- [references/adf-transformations.md](references/adf-transformations.md)
- [references/adf-runtime-networking-security.md](references/adf-runtime-networking-security.md)
- [references/adf-deployment-operations.md](references/adf-deployment-operations.md)

- **Book:** Richard Swinbank - Azure Data Factory by Example: Practical Implementation for Data Engineers (Apress, 2024).
