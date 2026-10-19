
# McGilvray DQ Monitoring Control Plan

Use this when data quality must be maintained after assessment or remediation. The output is a monitoring and control plan.

## Artifact

Produce a control plan with:

1. **Monitored data and rules** - critical elements, dimensions, checks, calculation logic, and baseline values.
2. **Thresholds and actions** - acceptable range, warning level, failure level, and required response.
3. **Ownership** - steward, technical owner, business owner, escalation path, and communication audience.
4. **Control mechanism** - automated check, dashboard, report, workflow gate, reconciliation, sampling, or manual review.
5. **Response process** - triage, correction, prevention, exception handling, root-cause trigger, and closure evidence.
6. **Review cadence** - daily/weekly/monthly monitoring, trend review, control tuning, and continuous-improvement backlog.

## Process

1. Reuse the baseline where possible. Monitoring should track the same high-value dimensions and rules used to justify action.
2. Monitor what will be acted on. Do not create metrics with no owner, threshold, or response path.
3. Include correction and prevention. A control should address current errors and feed changes that prevent recurrence.
4. Fit controls into existing operations. Prefer checks in ingestion, source workflows, release gates, stewardship routines, or BI health reviews over standalone reports.
5. Communicate quality in business terms. Explain whether quality is improving, what changed, and which decisions or processes remain at risk.

## Failure Modes

- **Dashboard-only control** - metrics are visible but nobody is accountable to respond.
- **Threshold-free monitoring** - charts show defects without defining acceptable, warning, and failure ranges.
- **Alert fatigue** - every defect triggers noise instead of severity-based response.
- **No recurrence learning** - incidents close after correction but do not update rules, process, training, or ownership.
- **Stale controls** - rules remain after data use, system behavior, or business definitions change.

## Output Format

Return the control plan, rule table, threshold/action matrix, escalation path, and continuous-improvement review cadence.

## References

- Danette McGilvray, *Executing Data Quality Projects* (Morgan Kaufmann, 2008), improvement cycle and monitoring approach.
- Sibling skills: `mcgilvray-dq-project-charter`, `mcgilvray-dq-assessment-baseline`, `mcgilvray-dq-root-cause-remediation`.
