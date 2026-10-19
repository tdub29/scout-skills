
# McGilvray DQ Root Cause Remediation

Use this after defects or impacts are known and the team needs to find causes and act. The output is a root-cause and remediation plan.

## Artifact

Produce a remediation plan with:

1. **Issue statement** - defect, affected data, impact, frequency, severity, and affected consumers.
2. **Cause tree** - human, process, system, policy, training, integration, definition, and control causes.
3. **Evidence plan** - logs, samples, process observations, interviews, lineage, and system behavior needed to confirm causes.
4. **Corrective actions** - data repair, process change, system fix, definition update, training, or policy change.
5. **Preventive controls** - validation rules, workflow changes, monitoring, stewardship review, or source-system constraints.
6. **Ownership and sequencing** - accountable owner, dependencies, effort, expected impact, and acceptance criteria.

## Process

1. Triage issues by business impact before root-cause depth. Not every defect deserves the same investigation.
2. Separate symptoms from causes. A null field, duplicate, or mismatch is a symptom until the creation and propagation path is understood.
3. Look across humans, process, and systems. Avoid assuming all defects are technical or all defects are user error.
4. Pair correction with prevention. Cleaning records without changing creation, validation, or monitoring creates recurring work.
5. Define acceptance with the business. Remediation is done when the affected process or decision is improved, not when a ticket closes.

## Failure Modes

- **Fixing the file** - repairing current records while the upstream process continues producing the same errors.
- **Root-cause workshop drift** - brainstorming plausible causes without evidence, owner, or confirmation plan.
- **Technical monocause** - assigning all defects to ETL, schema, or code while ignoring definitions, training, incentives, and process handoffs.
- **No prevention control** - corrective actions have no future check to detect recurrence.
- **Ownerless remediation** - actions are listed but no role has authority to change the source process or system.

## Output Format

Return an issue triage table, cause tree, evidence plan, remediation backlog, preventive controls, and acceptance criteria.

## References

- Danette McGilvray, *Executing Data Quality Projects* (Morgan Kaufmann, 2008), Ten Steps root-cause and improvement stages.
- Sibling skills: `mcgilvray-dq-project-charter`, `mcgilvray-dq-assessment-baseline`, `mcgilvray-dq-monitoring-control-plan`.
