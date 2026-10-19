
# McGilvray DQ Assessment Baseline

Use this when a team needs a measured current state of data quality. The output is an assessment baseline plan and findings structure.

## Artifact

Produce a baseline plan with:

1. **Critical data and uses** - the data elements, processes, decisions, and consumers being assessed.
2. **Quality dimensions** - accuracy, completeness, consistency, timeliness, uniqueness, validity, integrity, or other dimensions relevant to the use.
3. **Assessment methods** - profiling, rule checks, sampling, reconciliation, interviews, process walk-throughs, and business impact techniques.
4. **Baseline metrics** - measures, thresholds, population, calculation logic, and confidence limits or caveats.
5. **Impact interpretation** - what each issue costs, delays, risks, or prevents.
6. **Prioritized findings** - defects ranked by business value, severity, frequency, and feasibility of remediation.

## Process

1. Select quality dimensions from the business use. Do not assess every possible dimension because it is available.
2. Combine quantitative and qualitative evidence. Profiling finds patterns; interviews and process review explain how they affect work.
3. Define rules before running counts. Each metric needs a population, pass/fail logic, owner, and reason it matters.
4. Translate defects into business impact. Baselines should support decisions about investment, priority, and remediation.
5. Preserve repeatability. Baseline calculations should be reusable for monitoring after remediation.

## Failure Modes

- **Profile dump** - presenting hundreds of column stats without business interpretation or action priority.
- **Dimension mismatch** - measuring completeness when the real issue is timeliness, semantic accuracy, or process fitness.
- **No denominator clarity** - defect rates lack population definitions, making trends and comparisons meaningless.
- **Ignoring qualitative causes** - assuming data values alone reveal process, training, system, or policy causes.
- **Non-repeatable baseline** - one-off SQL or spreadsheet work cannot become ongoing monitoring.

## Output Format

Return the baseline plan, rule catalog, measurement table, business-impact summary, and prioritized issue list.

## References

- Danette McGilvray, *Executing Data Quality Projects* (Morgan Kaufmann, 2008), Ten Steps assessment stages.
- Sibling skills: `mcgilvray-dq-project-charter`, `mcgilvray-dq-root-cause-remediation`, `mcgilvray-dq-monitoring-control-plan`.
