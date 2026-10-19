# Few Dashboard: Monitoring Purpose

## When to use

Trigger when the dashboard's reason for existing is unclear: too many pages, unclear audience, mixed strategic/tactical/operational needs, no monitoring cadence, or a dashboard that behaves like a report. Cues: "is this really a dashboard," "dashboard scope," "single screen," "executive dashboard is messy," or "what should this dashboard include."

## The framework

Few defines dashboards by use: visual display of the most important information needed to achieve objectives, consolidated on a single screen so it can be monitored at a glance. The dashboard is a monitoring instrument, not a general report repository.

### Purpose tests

1. **Objective test.** Every item must connect to a specific objective or decision domain.

2. **Audience test.** A dashboard for executives, managers, analysts, or operators has different scope and latency needs. Mixed audiences usually create clutter.

3. **Single-screen test.** The essential monitoring view should fit within eye span without scrolling or paging. Details can live behind it.

4. **Cadence test.** Measures should refresh at a frequency that matches action. Real-time noise is not better if decisions are weekly.

5. **At-a-glance test.** The first screen should reveal status, exceptions, and where attention is needed before exploration.

## How to apply

1. **Name the dashboard job.** Write: "This dashboard helps [audience] monitor [objective] every [cadence] so they can [action]."

2. **Inventory current items.** Classify each KPI/chart/table as essential monitor, diagnostic detail, navigation/control, or unrelated.

3. **Choose dashboard type.** Strategic, tactical, operational, or analytical support. Note if multiple types are being forced into one view.

4. **Trim or relocate.** Keep essential monitoring items on the first screen; move drilldowns and explanatory reports behind the dashboard.

5. **Return a purpose brief.** Include audience, objective, cadence, essential measures, excluded measures, and follow-up detail paths.

## Common failure modes

- **Calling a report a dashboard.** A multi-page collection of charts may be useful, but if it cannot be monitored at a glance it is not fulfilling the dashboard role.

- **Mixing audiences.** Executives need direction and exceptions; operators may need immediate queues. Combining both often satisfies neither.

- **Treating every available KPI as important.** Availability is not relevance. Each measure must earn screen space.

- **Ignoring cadence.** Daily operational dashboards and quarterly strategy dashboards should not use the same data rhythm.

- **Making details compete with signals.** Diagnostics belong behind the signal, not on top of it.

## References

- Stephen Few, *Information Dashboard Design*, chapters 1-2.
- Sibling skills: `few-dashboard-thirteen-mistakes-audit`, `few-dashboard-perception-layout`, `few-dashboard-display-media-selector`, `few-dashboard-usability-launchpad`.
- Complements `build-dashboard` and `kpi-dashboard-design` by defining the monitoring job before building.
