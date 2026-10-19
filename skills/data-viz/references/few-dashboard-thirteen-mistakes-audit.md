# Few Dashboard: Thirteen Mistakes Audit

## When to use

Trigger for dashboard review, audit, critique, or cleanup. Especially use when the user shares a dashboard screenshot or describes symptoms like clutter, too many gauges, missing context, confusing color, poor KPI choices, or no clear priorities.

## The framework

Few's thirteen mistakes form a practical dashboard QA checklist. They are especially useful because they separate purpose failures, measure failures, encoding failures, layout failures, and visual polish failures.

### Mistake groups

1. **Scope and context failures.** Exceeding one screen, inadequate context, excessive detail or precision.

2. **Measure failures.** Deficient measures or KPIs that do not represent objectives.

3. **Display-media failures.** Inappropriate media, poor media design, meaningless variety, inaccurate quantitative encoding.

4. **Arrangement failures.** Poor organization, weak highlighting, and signals buried away from related context.

5. **Visual noise failures.** Useless decoration, color misuse/overuse, and unattractive or fatiguing display.

## How to apply

1. **Capture the dashboard job.** If purpose is unclear, run `few-dashboard-monitoring-purpose` first.

2. **Audit all thirteen mistakes.** Mark each as pass, minor, major, or critical.

3. **Group defects.** Put findings into scope/context, measure, display-media, arrangement, and visual noise groups.

4. **Sequence repairs.** Fix purpose/scope first, then measures, then display media, then layout, then color/detail polish.

5. **Return a defect report.** Include top 3 fixes, full checklist results, and a before/after direction for the first screen.

## Common failure modes

- **Starting with aesthetics.** A beautiful dashboard with deficient measures or no context is still broken.

- **Treating the thirteen mistakes as equal.** Single-screen failure and wrong measures usually outrank color polish.

- **Auditing charts but ignoring dashboard arrangement.** A set of good charts can still fail if related signals are scattered.

- **Using color as the only alerting mechanism.** Color should reinforce meaning, not be the sole carrier of status.

- **Leaving precision unchallenged.** Too many decimals slow dashboard monitoring and imply false certainty.

## References

- Stephen Few, *Information Dashboard Design*, chapter 3.
- Sibling skills: `few-dashboard-monitoring-purpose`, `few-dashboard-display-media-selector`, `few-dashboard-perception-layout`.
- Complements broader UI/design audits by using Few's dashboard-specific defect categories.
