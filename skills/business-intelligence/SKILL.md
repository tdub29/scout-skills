---
name: business-intelligence
description: "BI dashboards, KPI frameworks, scheduled reporting."
license: MIT + Commons Clause
metadata:
  version: 1.0.0
  author: borghei
  category: data-analytics
  updated: 2026-03-31
  tags: [bi, dashboards, visualization, reporting, insights]
---
# Business Intelligence

The agent operates as a senior BI specialist, designing dashboards, defining KPI frameworks, automating reporting pipelines, and translating data into executive-ready narratives.

## Workflow

1. **Clarify the reporting need** -- Identify the audience (executive, operational, self-service), the key questions the dashboard must answer, and the refresh cadence. Validate that required data sources exist and are accessible.
2. **Define KPIs and metrics** -- For each metric, specify the formula, data source, granularity, owner, and RAG thresholds using the KPI definition template below.
3. **Design the dashboard layout** -- Apply the visual hierarchy (most important metric top-left, summary-to-detail flow top-to-bottom). Select chart types using the chart selection matrix. Limit to 5-8 visualizations per page.
4. **Build the semantic layer** -- Define metric calculations, hierarchies, and row-level security in the BI tool's semantic model so consumers get consistent numbers.
5. **Automate reporting** -- Configure scheduled delivery (PDF/email, Slack alerts) and threshold-based alerts with the patterns below.
6. **Validate and iterate** -- Confirm KPI values match source-of-truth queries. Check dashboard load time (<5 s target). Gather stakeholder feedback and refine.

## KPI Definition Template

```yaml
# Copy and fill for each metric
kpi:
  name: "Monthly Recurring Revenue"
  owner: "Finance"
  purpose: "Track subscription revenue health"
  formula: "SUM(subscription_amount) WHERE status = 'active'"
  data_source: "billing.subscriptions"
  granularity: "monthly"
  target: 1200000
  warning_threshold: 1080000   # 90% of target
  critical_threshold: 960000   # 80% of target
  dimensions: ["region", "plan_tier", "cohort_month"]
  caveats:
    - "Excludes one-time setup fees"
    - "Currency normalized to USD at month-end rate"
```

## Design and Automation

Dashboard design principles are in `references/dashboard-design.md`; report automation patterns are in `references/report-automation.md`.


## Data Storytelling Structure

The agent frames every insight using Situation-Complication-Resolution:

1. **Situation** -- "Last quarter we targeted 10% retention improvement."
2. **Complication** -- "Enterprise churn rose 5%, driven by 30-day onboarding delays."
3. **Resolution** -- "Reducing onboarding to 14 days correlates with 40% lower churn and could save $2M annually."

## Governance

```yaml
security_model:
  row_level_security:
    - rule: region_access
      filter: "region = user.region"
  object_permissions:
    - role: viewer
      permissions: [view, export]
    - role: editor
      permissions: [view, export, edit]
    - role: admin
      permissions: [view, export, edit, delete, publish]
```

## Scripts

```bash
python scripts/kpi_tracker.py --definitions kpis.json --data sales.csv
python scripts/kpi_tracker.py --definitions kpis.json --data sales.csv --json
python scripts/dashboard_spec_generator.py --definitions kpis.json --title "Sales Dashboard"
python scripts/dashboard_spec_generator.py --definitions kpis.json --layout 3-column --json
python scripts/metric_validator.py --definitions metrics.json --strict
python scripts/metric_validator.py --definitions metrics.json --json
```

## Tool Reference

| Tool | Purpose | Key Flags |
|------|---------|-----------|
| `kpi_tracker.py` | Calculate KPIs from data against targets; report RAG status and variance | `--definitions <json>`, `--data <csv/json>`, `--json` |
| `dashboard_spec_generator.py` | Generate dashboard layout specs (chart types, positions, filters) from KPI definitions | `--definitions <json>`, `--title`, `--layout 2-column/3-column`, `--json` |
| `metric_validator.py` | Validate metric definitions for completeness, naming, threshold logic, and consistency | `--definitions <json>`, `--strict`, `--json` |

## Troubleshooting

| Problem | Likely Cause | Resolution |
|---------|-------------|------------|
| Dashboard loads slowly (> 5 s) | Too many visualizations or live-connection queries hitting raw tables | Reduce widgets to 5-8 per page; switch to extracts or materialized views for heavy dashboards |
| KPI values differ between dashboard and source query | Dashboard applies additional filters, currency conversion, or calculated fields not in the semantic layer | Centralize all metric logic in the semantic layer; remove dashboard-level computed fields |
| RAG thresholds trigger false alerts | Warning/critical percentages are miscalibrated for seasonal patterns | Adjust thresholds per season or use rolling baselines; validate with `metric_validator.py --strict` |
| Stakeholders ignore dashboards | Dashboard answers the wrong questions or lacks actionable context | Redesign using the Situation-Complication-Resolution storytelling framework; add annotations and targets |
| Row-level security hides data unexpectedly | Security rules are too broad or user-role mapping is incorrect | Audit RLS rules; test with a sample user from each role; log filtered row counts |
| Scheduled report emails land in spam | Large PDF attachments or sender reputation issues | Reduce attachment size; switch to embedded links; work with IT to whitelist the sender domain |
| `metric_validator.py` reports formula-aggregation mismatch | The `formula` field (e.g., "SUM(...)") does not match the declared `aggregation` | Align the two fields; the aggregation field drives the tool while the formula documents intent |

## Success Criteria

- Dashboard load time is under 5 seconds for 95% of page views.
- KPI definitions pass `metric_validator.py --strict` with zero errors before production deployment.
- Executive dashboards follow the visual hierarchy: summary cards at top-left, trends in the middle, detail tables at the bottom.
- Every KPI has a defined owner, target, and RAG thresholds documented in the definitions file.
- Self-service BI adoption reaches Level 2 (Explorers) for at least 60% of target users within 90 days.
- Scheduled reports are delivered within 15 minutes of the configured schedule window.
- Data storytelling follows the What / So What / Now What structure with quantified impact in every insight.

## Scope & Limitations

**In scope:** Dashboard design and layout, KPI framework definition, report automation patterns, data storytelling, self-service BI enablement, row-level security configuration, and visualization best practices.

**Out of scope:** Data warehouse infrastructure, ETL/ELT pipeline development, raw data ingestion, machine learning model building, and BI tool installation or licensing.

**Limitations:** The Python tools (`kpi_tracker.py`, `dashboard_spec_generator.py`, `metric_validator.py`) operate on local JSON and CSV files only -- they do not connect to live databases or BI platforms. All scripts use the Python standard library with no external dependencies. Dashboard specifications are platform-agnostic and require manual translation to specific BI tools (Tableau, Power BI, Looker, etc.).

## Integration Points

- **Analytics Engineer** (`data-analytics/analytics-engineer`): Provides the mart models and semantic-layer metrics that dashboards consume; schema changes require dashboard updates.
- **Data Analyst** (`data-analytics/data-analyst`): Creates ad-hoc analyses that may evolve into repeatable dashboards; shares visualization standards.
- **Product Team** (`product-team/`): Defines product KPIs and user-facing analytics requirements.
- **C-Level Advisor** (`c-level-advisor/`): Executive dashboards translate strategic objectives into measurable KPIs.
- **Finance** (`finance/`): Financial KPIs (MRR, CAC, LTV) require alignment between BI dashboards and finance team definitions.

## References

- `references/dashboard-design.md`: load when laying out a dashboard or choosing visuals
- `references/report-automation.md`: load when configuring scheduled reports and alerts
- `references/maturity-and-performance.md`: load for the self-service maturity model and the performance checklist
- `references/planned-reference-files.md`: index of reference docs named by the original skill; those files are not on disk
