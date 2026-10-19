# Report Automation Patterns

## Report Automation Patterns

**Scheduled report (cron-style):**
```yaml
report:
  name: Weekly Sales Report
  schedule: "0 8 * * MON"
  recipients: [sales-team@company.com, leadership@company.com]
  format: PDF
  pages: [Executive Summary, Pipeline Analysis, Rep Performance]
```

**Threshold alert:**
```yaml
alert:
  name: Revenue Below Target
  metric: daily_revenue
  condition: "actual < target * 0.9"
  channels:
    email: finance@company.com
    slack: "#revenue-alerts"
  message: "Daily revenue ${actual} is ${pct_diff}% below target. Top factors: ${top_factors}"
```

**Automated generation workflow (Python):**
```python
def generate_report(config: dict) -> str:
    """Generate and distribute a scheduled report."""
    # 1. Refresh data sources
    refresh_data_sources(config["sources"])
    # 2. Calculate metrics
    metrics = calculate_metrics(config["metrics"])
    # 3. Create visualizations
    charts = create_visualizations(metrics, config["charts"])
    # 4. Compile into report
    report = compile_report(metrics=metrics, charts=charts, template=config["template"])
    # 5. Distribute
    distribute_report(report, recipients=config["recipients"], fmt=config["format"])
    return report.path
```
