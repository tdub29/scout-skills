# Few Dashboard: Usability Launchpad

## When to use

Trigger when a dashboard is meant to launch deeper analysis or action: drilldowns, filters, links, detail pages, alerts, or operational workflows. Cues: "dashboard interactions," "drilldown design," "too many filters," "what happens after someone sees an exception," or "make this dashboard usable."

## The framework

Few's launch-pad idea keeps the dashboard as a monitoring surface while allowing deeper details one step away. The dashboard should not become the detail environment; it should point clearly to it.

### Usability rules

1. **Keep monitoring separate from diagnosis.** First screen signals status; drilldowns explain causes.

2. **Make controls earn space.** Filters, selectors, and buttons belong only when they serve frequent monitoring tasks.

3. **Preserve orientation.** Drilldowns should keep metric names, filters, time periods, and breadcrumbs clear.

4. **Maintain consistency.** Similar interactions and displays should behave the same way across the dashboard.

5. **Test real questions.** Usability is proven by whether users answer monitoring questions quickly and accurately.

## How to apply

1. **List user follow-up actions.** For each signal, define what the user should inspect or do next.

2. **Map drill paths.** Decide which details are tooltips, inline expansion, linked reports, filtered detail tables, or external workflows.

3. **Prune controls.** Remove controls that support rare exploration rather than regular monitoring.

4. **Define orientation cues.** Breadcrumbs, selected filters, time period labels, and return paths.

5. **Return a launch-pad spec.** Include signal -> detail path -> user action for each major dashboard area.

## Common failure modes

- **Turning the first screen into the drilldown.** Too many controls and details destroy monitoring.

- **Dead-end signals.** A red KPI with no way to investigate creates anxiety, not action.

- **Hidden filter state.** Users cannot trust dashboard readings if current filters and dates are unclear.

- **Inconsistent interactions.** If clicking a chart means different things in different sections, users slow down.

- **Testing with designers instead of users.** Real users should attempt real monitoring questions under realistic time pressure.

## References

- Stephen Few, *Information Dashboard Design*, chapter 7.
- Sibling skills: `few-dashboard-monitoring-purpose`, `few-dashboard-perception-layout`, `few-dashboard-display-media-selector`.
- Complements dashboard-building skills by specifying interaction behavior after the first-screen design.
