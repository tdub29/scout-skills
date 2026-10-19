# ADF Pipeline Resource Model

Use this before building or explaining an Azure Data Factory instance, especially when the user needs to understand how factory resources fit together before editing a pipeline.

## Artifact

Produce an ADF resource model brief containing:

1. **Factory workspace state** - Azure subscription/resource group, factory instance, ADF Studio mode, and whether the work is in live mode, Git mode, debug, or published runtime.
2. **Resource graph** - linked services, datasets, pipelines, activities, and integration runtimes, with each resource's responsibility and owner.
3. **Debug path** - how the pipeline will be run before publication, what input data it uses, and what output proves the graph is wired correctly.
4. **Promotion implication** - which resources live only in Git, which are published to the factory, and which values must vary by environment.

## Trigger checks

- The user is creating a new ADF instance or needs to orient a repo or factory.
- The question is "where does this connection/dataset/pipeline/activity live?"
- A debug run works in ADF Studio but the published factory behaves differently.
- The user is trying to document an existing ADF pipeline for another engineer.

## How to apply

1. Separate Azure resource setup from ADF resource authoring. Resource groups and factory instances are Azure resources; pipelines, datasets, linked services, triggers, and data flows are factory resources.
2. Identify the editing state. In Git mode, saved work is source-controlled but not necessarily published. In debug, execution uses the development factory's compute. In published runtime, triggers and manual runs use published resources.
3. Draw the smallest useful graph: source linked service -> source dataset -> activity -> sink dataset -> sink linked service, with the pipeline and integration runtime around it.
4. Name the dependency direction. Pipelines use activities; activities reference datasets and linked services; linked services and some activities use integration runtimes.
5. Define the proof of correctness. A debug run should show activity status, input/output counts or files, and a sink-side verification query or file check.

## Sub-rules

- Linked services describe connections; datasets describe data shape/location within those connections.
- Pipelines orchestrate activities; they should not hide all environment-specific values inside activities.
- Git save, debug execution, and publish are separate actions. Do not treat one as proof of the others.
- Keep sample data and resource naming conventional enough that the same graph can be promoted later.

## Common failure modes

- **Live/Git confusion.** A user edits in Git mode and expects the published factory to change before publishing.
- **Dataset as connection.** The dataset carries path/table/schema details, but the linked service owns the connection.
- **Debug equals production.** A debug run proves the design can run, not that production triggers, parameters, private endpoints, or permissions are correct.
- **Invisible resource dependency.** A pipeline export misses linked services, integration runtimes, or factory-level parameters needed in the target environment.

## Output format

Return:

1. **Resource graph:** compact table of ADF resources and dependencies.
2. **Execution state:** live/Git/debug/published distinction and current risk.
3. **Debug proof:** exact evidence to collect.
4. **Next action:** the one setup or authoring move to make next.

## References

- Richard Swinbank, *Azure Data Factory by Example* (Apress, 2024), chapters 1-2.
- Sibling refs: `adf-copy-activity-ingestion.md`, `adf-deployment-operations.md`.
