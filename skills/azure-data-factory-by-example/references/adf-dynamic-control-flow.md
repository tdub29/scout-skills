# ADF Dynamic Control Flow

Use this when an ADF pipeline needs runtime values, reusable datasets or linked services, conditional branches, loops, explicit errors, or parent-child pipeline composition.

## Artifact

Produce a dynamic control-flow design containing:

1. **Runtime value map** - expressions, system variables, activity outputs, variables, pipeline parameters, dataset parameters, linked service parameters, global parameters, and Key Vault references.
2. **Control graph** - dependency conditions, branches, loops, failure paths, and child pipeline calls.
3. **Secret boundary** - which values can be logged or parameterized directly and which must be retrieved from Key Vault or managed identity.
4. **Observability hooks** - audit columns, user properties, return values, and error messages that make the run explainable.

## Trigger checks

- Dynamic content or expression builder work.
- Need to reuse one dataset, linked service, or pipeline across multiple folders, files, tables, or environments.
- Activity output from Lookup, Copy, Get Metadata, or a child pipeline drives later steps.
- If Condition, Switch, ForEach, Until, Fail, or dependency conditions are being designed.
- Key Vault or parameterized connection strings are involved.

## How to apply

1. Identify every runtime value and classify it: pipeline-controlled, activity-produced, externally injected, environment constant, or secret.
2. Pick the narrowest parameter level. Use dataset parameters for data location/schema, linked service parameters for connection variation, pipeline parameters for run inputs, and global parameters for factory-wide constants.
3. Use expressions for runtime binding, not for hiding business logic that belongs in SQL, Data Flow, or code.
4. Build the control graph from dependency outcomes: success, failure, skipped, and completed. State what happens on each path.
5. Use variables sparingly. They are useful for run-scoped state, but can make flow harder to reason about when parameters or activity outputs would suffice.
6. Add explicit observability: audit columns, run IDs, activity user properties, meaningful Fail activity messages, and child pipeline return values.

## Sub-rules

- `@` expression handling and string interpolation are syntax risks; verify literal strings and escaped values.
- Lookup output shape matters. State whether the downstream expression reads a first row, a value, or an array.
- Parallel child pipelines require a concurrency and dependency plan, not just Execute Pipeline activities.
- Dependency conditions are part of error handling. Do not leave failure paths implicit.
- Key Vault is the default shape for secrets; parameterization is not a license to expose credentials.

## Common failure modes

- **Wrong parameter level.** Pipeline parameters are used for paths that belong on datasets, or connection secrets are passed as plain strings.
- **Expression-only logic.** Complex business rules are encoded in dynamic content where they are hard to test and review.
- **Activity output shape mismatch.** The expression assumes a scalar but Lookup returns an array or object.
- **Silent skipped path.** An activity is skipped because dependencies do not match, and no failure path records why.
- **Unbounded loop.** Iteration runs too many files/tables without concurrency, retry, or failure aggregation rules.

## Output format

Return:

1. **Runtime value map:** classified list of dynamic values and where each should live.
2. **Control graph:** compact flow description with dependency outcomes.
3. **ADF expressions/settings:** the important expression or setting names to configure.
4. **Failure and audit checks:** what to log, fail, return, or alert on.

## References

- Richard Swinbank, *Azure Data Factory by Example* (Apress, 2024), chapters 4-6.
- Sibling refs: `adf-copy-activity-ingestion.md`, `adf-deployment-operations.md`.
