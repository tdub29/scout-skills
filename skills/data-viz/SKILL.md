---
name: data-viz
description: "Chart critique theory. Tufte, Bertin. No code"
---

# data-viz

This hub collapses 30 atomic data-visualization skills â€” drawn from Tufte, Bertin, Few (Ã—2 books), and Knaflic â€” into one router plus references. Route by user cue, read the referenced file(s) in full, and apply that framework exactly.

## When to use

Use this hub when the user wants principled **critique, audit, or redesign** of a chart, table, dashboard, or data presentation â€” and the right answer comes from data-visualization theory rather than from writing plotting code. Typical intents: "is this chart honest / too busy / well-designed," "which chart type fits this question," "fix this dashboard," "make this slide tell a story," "what should I erase," "where should the eye land."

## Guardrails

- This hub is the **theory / critique / design-principle** router (Tufte / Bertin / Few / Knaflic). For hands-on chart **code** (matplotlib, seaborn, plotly, ggplot, Vega) use `data-visualization`. For dashboard **scaffolding / build-out** use `build-dashboard`.
- Do **not** steal requests owned by `kpi-dashboard-design`, `d3-viz`, `data-storytelling`, or `pitch-deck-visuals`. Those are pre-existing skills outside this hub.
- Do **not** trigger for unrelated UI/frontend design, generic copywriting, SEO, or analytics-engineering work unless the user explicitly asks for these authors' principles.
- Do **not** answer from router memory alone; load the selected reference file(s) first and follow their process and output format.
- Keep routing tight: start with 1â€“2 references; combine families only when the user asks for a multi-lens pass (e.g., Tufte erasure + Bertin encoding for a design-system audit).

## Quick routing table

| User cue (examples) | Route to reference(s) |
|---|---|
| what can I erase, too much ink, axes/frames/gridlines/baselines, "Tufte-ify", reduce structural ink | `references/tufte-data-ink-ratio.md` |
| decorative noise, 3D, moirÃ©/vibration, hatching, gratuitous color, ducks, remove decoration | `references/tufte-chartjunk.md` |
| is this chart honest, distorted, truncated axis, area-encodes-linear, lie factor, exaggerated effect | `references/tufte-lie-factor.md` |
| audit truthfulness, graphical integrity, design variation vs data variation, the six integrity principles | `references/tufte-graphical-integrity-principles.md` |
| pack in more data, sparse chart, data-points per area, shrink/multiply, data density | `references/tufte-data-density.md` |
| width:height proportion, too tall/wide, line-weight hierarchy, which axis to elongate | `references/tufte-aspect-ratio.md` |
| one busy multi-series chart, split into a grid of panels, faceting, small multiples | `references/tufte-small-multiples.md` |
| which visual variable encodes this, size/value/texture/hue/orientation/shape, retinal variables | `references/bertin-retinal-variables.md` |
| is this a single-glance image or read-piece-by-piece, image vs figuration, perceptual instant | `references/bertin-image-vs-figuration.md` |
| what's the invariant vs the components, decompose the information being mapped | `references/bertin-invariant-components.md` |
| is the data nominal/ordinal/quantitative, levels of organization, match variable to encoding capacity | `references/bertin-levels-of-organization.md` |
| will the marks merge / is it legible, separation thresholds, too dense to read, legibility rules | `references/bertin-legibility-rules.md` |
| reorder rows/columns to reveal clusters, permute a matrix, reorderable matrix, find pattern in a table | `references/bertin-reorderable-matrix.md` |
| what's the dashboard for, audience/scope/cadence, is this really a monitoring dashboard | `references/few-dashboard-monitoring-purpose.md` |
| organize a single screen, grouping/proximity/hierarchy/whitespace, dashboard layout for scanning | `references/few-dashboard-perception-layout.md` |
| which KPI display widget, bullet graph/sparkline/icon/bar, pick a dashboard display medium | `references/few-dashboard-display-media-selector.md` |
| audit a dashboard against the thirteen common mistakes, single-screen fit, context, encoding errors | `references/few-dashboard-thirteen-mistakes-audit.md` |
| drilldown/filtering/follow-up action without overloading screen 1, dashboard usability & launch-pad | `references/few-dashboard-usability-launchpad.md` |
| should this be a table or a graph (or both), table-vs-graph decision | `references/few-smtn-table-graph-fit.md` |
| redesign a hard-to-read business table, pivot/report/financial table for lookup & comparison | `references/few-smtn-business-table-design.md` |
| what graph fits this business question, time series/ranking/part-to-whole/deviation, chart selection | `references/few-smtn-relationship-chart-selector.md` |
| replace a donut/radar/circle/unit/funnel chart, forsaken chart types | `references/few-smtn-forsaken-chart-replacement.md` |
| right chart type but hard to read, fix marks/scales/axes/legends/labels, component-level audit | `references/few-smtn-graph-component-audit.md` |
| reduce this to a single so-what / action sentence, 3-minute story, big idea | `references/knaflic-big-idea.md` |
| who/what/how before building, audience, action, communication mechanism, explanatory context | `references/knaflic-explanatory-context.md` |
| plan order & flow before opening the slide tool, low-tech storyboard | `references/knaflic-storyboard.md` |
| fix deck narrative, action titles, executive summary, horizontal/vertical logic, reverse-storyboard | `references/knaflic-deck-logic.md` |
| this visual is busy/default/cluttered, remove cognitive load, declutter | `references/knaflic-declutter.md` |
| the eye doesn't land where intended, first/second/third read, preattentive attention hierarchy | `references/knaflic-preattentive-hierarchy.md` |
| concrete chart or deck, want a practical makeover, before-and-after critique | `references/knaflic-before-after-critique.md` |

## Workflow

1. Confirm the intent is data-visualization **theory/critique/design** â€” not chart code (`data-visualization`) or dashboard build-out (`build-dashboard`).
2. Pick the closest row(s) in the routing table.
3. Read those `references/*.md` files completely.
4. Apply the framework's process, failure modes, and output format from the reference(s) exactly.
5. Combine families only when the user asks for a multi-lens pass â€” e.g., Tufte erasure + Few graph-component audit for a chart cleanup, or Bertin encoding + Knaflic preattentive hierarchy for a design-system review.

## References

- [references/bertin-image-vs-figuration.md](references/bertin-image-vs-figuration.md)
- [references/bertin-invariant-components.md](references/bertin-invariant-components.md)
- [references/bertin-legibility-rules.md](references/bertin-legibility-rules.md)
- [references/bertin-levels-of-organization.md](references/bertin-levels-of-organization.md)
- [references/bertin-reorderable-matrix.md](references/bertin-reorderable-matrix.md)
- [references/bertin-retinal-variables.md](references/bertin-retinal-variables.md)
- [references/few-dashboard-display-media-selector.md](references/few-dashboard-display-media-selector.md)
- [references/few-dashboard-monitoring-purpose.md](references/few-dashboard-monitoring-purpose.md)
- [references/few-dashboard-perception-layout.md](references/few-dashboard-perception-layout.md)
- [references/few-dashboard-thirteen-mistakes-audit.md](references/few-dashboard-thirteen-mistakes-audit.md)
- [references/few-dashboard-usability-launchpad.md](references/few-dashboard-usability-launchpad.md)
- [references/few-smtn-business-table-design.md](references/few-smtn-business-table-design.md)
- [references/few-smtn-forsaken-chart-replacement.md](references/few-smtn-forsaken-chart-replacement.md)
- [references/few-smtn-graph-component-audit.md](references/few-smtn-graph-component-audit.md)
- [references/few-smtn-relationship-chart-selector.md](references/few-smtn-relationship-chart-selector.md)
- [references/few-smtn-table-graph-fit.md](references/few-smtn-table-graph-fit.md)
- [references/knaflic-before-after-critique.md](references/knaflic-before-after-critique.md)
- [references/knaflic-big-idea.md](references/knaflic-big-idea.md)
- [references/knaflic-deck-logic.md](references/knaflic-deck-logic.md)
- [references/knaflic-declutter.md](references/knaflic-declutter.md)
- [references/knaflic-explanatory-context.md](references/knaflic-explanatory-context.md)
- [references/knaflic-preattentive-hierarchy.md](references/knaflic-preattentive-hierarchy.md)
- [references/knaflic-storyboard.md](references/knaflic-storyboard.md)
- [references/tufte-aspect-ratio.md](references/tufte-aspect-ratio.md)
- [references/tufte-chartjunk.md](references/tufte-chartjunk.md)
- [references/tufte-data-density.md](references/tufte-data-density.md)
- [references/tufte-data-ink-ratio.md](references/tufte-data-ink-ratio.md)
- [references/tufte-graphical-integrity-principles.md](references/tufte-graphical-integrity-principles.md)
- [references/tufte-lie-factor.md](references/tufte-lie-factor.md)
- [references/tufte-small-multiples.md](references/tufte-small-multiples.md)

- **Books:** Edward Tufte, *The Visual Display of Quantitative Information* (tufte-*); Jacques Bertin, *Semiology of Graphics* (bertin-*); Stephen Few, *Information Dashboard Design* (few-dashboard-*); Stephen Few, *Show Me the Numbers* (few-smtn-*); Cole Nussbaumer Knaflic, *Storytelling with Data* (knaflic-*).
