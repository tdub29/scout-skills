# ADF Runtime, Networking, and Security

Use this when selecting or troubleshooting integration runtimes, private connectivity, self-hosted access, or SSIS lift-and-shift in ADF.

## Artifact

Produce an ADF runtime and network decision containing:

1. **Runtime choice** - AutoResolve Azure IR, region-specific Azure IR, managed VNet Azure IR, self-hosted IR, Azure-SSIS IR, or external compute activity.
2. **Data movement geography** - source region, sink region, compliance constraints, latency/cost concerns, and data egress risk.
3. **Network path** - public endpoint, managed private endpoint, private storage/database, local file system, or hybrid network.
4. **Operational ownership** - who patches, monitors, scales, starts/stops, and grants access to the runtime.

## Trigger checks

- Integration runtime selection or AutoResolve behavior is unclear.
- Data movement region, managed VNet, private endpoint, or disabled public access matters.
- ADF must access a local/network file system or on-prem/private resource.
- Self-hosted IR or linked self-hosted IR is involved.
- SSIS packages need to run in Azure through Azure-SSIS IR.

## How to apply

1. Separate orchestration from execution. ADF manages activities through an IR, but actual work may occur in ADF-managed compute, a self-hosted node, SQL, Spark, Databricks, or SSIS.
2. Start with AutoResolve unless geography, private network access, local access, SSIS, or compliance constraints require a different runtime.
3. For cloud private access, prefer managed VNet plus managed private endpoints and confirm the target service approves the endpoint.
4. For local or private network access, use self-hosted IR and state where it runs, what it can reach, and how it is maintained.
5. For SSIS packages, decide whether Azure-SSIS IR is a transition strategy or a long-term operating model. Include start/stop cost discipline.
6. Tie every runtime decision to a specific linked service or activity setting.

## Sub-rules

- Region-specific Azure IR is about control over where data movement compute runs.
- Managed private endpoints are factory-managed network links, but they still require target-side approval.
- Self-hosted IR introduces machine ownership, service account, patching, local permissions, and availability concerns.
- Azure-SSIS IR is not just "ADF runs SSIS"; it is a managed cluster with deployment, package catalog, and cost implications.
- Data Flow runtime sizing belongs with transformation design but depends on runtime settings.

## Common failure modes

- **Assuming AutoResolve is neutral.** It may choose a region that is acceptable technically but poor for compliance, cost, or data gravity.
- **Private endpoint half-configured.** ADF creates the endpoint but the storage/database side has not approved or DNS is wrong.
- **Self-hosted IR as a black box.** Local permissions, service account, firewall, and machine uptime are undocumented.
- **SSIS cost drift.** Azure-SSIS IR is left running after package execution or testing.
- **Runtime setting omitted.** The right IR exists but the linked service or activity still points at the default.

## Output format

Return:

1. **Runtime decision:** selected IR type and why alternatives were rejected.
2. **Connectivity path:** source -> runtime -> sink path and authentication.
3. **Configuration checklist:** ADF settings plus Azure/network approvals.
4. **Operational risks:** ownership, cost, monitoring, and recovery checks.

## References

- Richard Swinbank, *Azure Data Factory by Example* (Apress, 2024), chapter 8.
- Sibling refs: `adf-copy-activity-ingestion.md`, `adf-deployment-operations.md`.
