# ADF Deployment and Operations

Use this when moving ADF work from development to production, selecting triggers, monitoring runs, exporting logs, or designing alerts.

## Artifact

Produce an ADF deployment and operations plan containing:

1. **Promotion path** - Git branch, publish state, ARM template or factory JSON, deployment parameters, service connection, and target factory.
2. **Environment differences** - linked service endpoints, Key Vault names, IR names, trigger state, global parameters, and secrets.
3. **Trigger model** - manual, schedule, tumbling window, storage event, custom event, or external invocation, with parameter values and replay behavior.
4. **Monitoring model** - trigger runs, pipeline runs, activity runs, annotations, user properties, metrics, diagnostic settings, Log Analytics, and alerts.
5. **Runbook** - start/stop triggers, validate deployment, triage failures, and disable noisy alerts after test activity.

## Trigger checks

- Publishing ADF resources from Studio, Git, ARM template, PowerShell, or Azure DevOps.
- A development factory needs a production factory.
- Schedule, tumbling window, storage event, custom event, or external trigger selection.
- Monitoring pipeline failures, trigger runs, metrics, Log Analytics, or alert rules.
- The user asks how to operationalize a pipeline after debug succeeds.

## How to apply

1. Name the state transition. Saving to Git, publishing to the development factory, and deploying to another factory are different operations.
2. Inventory deployable resources and dependencies: pipelines, datasets, linked services, data flows, triggers, integration runtimes, global parameters, and factory-level settings.
3. Externalize environment-specific values into deployment parameters or per-environment configuration. Do not hard-code dev storage, Key Vault, IR, or SQL endpoints.
4. Choose the trigger type from the business timing semantics. Use schedule for clock time, tumbling window for windowed/replayable intervals, event triggers for storage events, and external invocation when another orchestrator owns timing.
5. Publish or deploy with triggers intentionally stopped or started. Production deployments should not accidentally activate stale or test triggers.
6. Add monitoring before calling the pipeline production-ready: annotations, activity user properties, diagnostic settings, Log Analytics queries, metrics, and alert routing.

## Sub-rules

- Deployment parameters are part of the artifact, not afterthoughts.
- Resource dependencies can break automated deployment when an object references a resource not yet created or not exported.
- Tumbling window triggers carry interval state; schedule triggers do not provide the same replay semantics.
- Storage event triggers depend on Event Grid registration and event filtering.
- Log-based alerts should target actionable failure signatures, not every noisy debug artifact.

## Common failure modes

- **Published in dev, not deployed to prod.** The pipeline works in the development factory but production never received the resources.
- **Trigger surprise.** A deployment starts a trigger with test parameters or leaves production triggers stopped.
- **Environment leakage.** Dev Key Vault, storage accounts, IR names, or database endpoints are embedded in published resources.
- **No diagnostic sink.** Failures can be seen in Studio but are not exported to Blob, Event Hub, or Log Analytics for operations.
- **Alert fatigue.** Metric or log alerts are created from test activity and then left enabled.

## Output format

Return:

1. **Promotion plan:** source, target, deployment mechanism, parameters, and dependency order.
2. **Trigger spec:** trigger type, timing/event rule, parameters, and start/stop handling.
3. **Monitoring spec:** logs, metrics, annotations/user properties, Log Analytics queries, and alerts.
4. **Runbook checks:** validation steps and rollback or disable steps.

## References

- Richard Swinbank, *Azure Data Factory by Example* (Apress, 2024), chapters 10-12.
- Related context: chapter 13 for metadata-driven copy, CDC, Synapse pipelines, and Fabric Data Factory.
- Sibling refs: `adf-pipeline-resource-model.md`, `adf-runtime-networking-security.md`.
