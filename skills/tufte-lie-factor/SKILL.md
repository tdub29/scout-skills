---
name: tufte-lie-factor
description: Apply Edward Tufte's Lie Factor metric from *The Visual Display of Quantitative Information* to detect and quantify visual distortion in charts â€” the ratio of (size of effect shown in the graphic) to (size of effect in the data), which should land between 0.95 and 1.05 for an honest graphic. Use whenever the user wants a chart audited for misleading scaling, asks "is this graph honest," debates whether a truncated y-axis, 3D effect, area encoding, or aspect-ratio change is fair, says "this looks dramatic but the numbers are barely different," "the bars look 10x taller but it's only a 20% increase," "audit my dashboard for distortion," "did our CEO's earnings chart lie," or wants a publication-readiness check before a chart ships. Also trigger when the user shares a screenshot of a chart from news, social media, an annual report, or a competitor and asks if it's misleading, or when they're worried their *own* chart accidentally distorts. Output is a numerical Lie Factor score per visual element + a flagged list of the specific distortion mechanism (truncated axis, area-amplified linear quantity, perspective tilt, aspect-ratio compression, dual-axis mismatch, etc.) + a corrected redraw spec. Do NOT trigger for chart *type* selection (use a general data-viz skill) or pure aesthetic critique (use a design skill) â€” this skill is exclusively about whether the visual encoding tells the numerical truth.
---

# Tufte: Lie Factor

## When to use

Trigger when the question on the table is "does this chart tell the truth about its numbers" â€” not "is it pretty," not "is it the right chart type." Concrete cues:

- The user shares a chart and asks "is this misleading?" / "is this honest?" / "is this fair?"
- The user is about to publish a graphic and wants a sanity-check
- A chart's visual effect looks bigger than the underlying numbers ("this spike looks crazy but it's only 8%")
- A y-axis is truncated, starts above zero, or is broken
- The chart uses 3D, perspective, isometric, or shaded-volume effects to encode 1D quantities
- The chart uses area or volume (pie wedges, bubble sizes, pictograms) to encode a single number
- Two y-axes with different scales suggest a correlation that may not exist
- The user is debating whether to start the axis at zero or at the data minimum
- A competitor or news article shows a chart that "feels off"

Don't trigger for: choosing between bar vs. line vs. dot plot (general data-viz), color palette decisions (design), label microcopy (UX writing), or dashboard layout (kpi-dashboard-design). Those are upstream of integrity. The Lie Factor only kicks in once the encoding choice is made and you're checking whether the encoding visually matches the data.

## The framework

### Core thesis

Every chart visually encodes numerical change as physical change â€” a bar gets taller, a line steeper, an area larger. Integrity requires that the *physical* change be proportional to the *numerical* change. The Lie Factor measures that proportion in one number. When the visual change is bigger than the numerical change, the graphic exaggerates; when smaller, it suppresses. Tufte's standard is Lie Factor between 0.95 and 1.05. Anything outside that band is a distortion that requires either correction or an explicit justification (e.g., a log scale that's clearly labeled and serves the reader's reasoning, not the author's agenda).

The Lie Factor is a *metric*, not a taste judgment. Two designers can disagree about color or chart type; they cannot disagree about whether a 4% revenue change is shown as a 40% taller bar. That is what makes this skill carveable as its own audit tool.

### The formula

```
Lie Factor = (size of effect shown in the graphic) / (size of effect in the data)
```

Where "size of effect" is measured as a percent change:

```
size of effect = (later value âˆ’ earlier value) / earlier value
```

Apply to whichever visual quantity the chart uses to convey the effect â€” bar height, line slope, wedge area, bubble diameter, perspective-corrected length, etc.

**Worked example.** A bar chart showing 1980 = 100 and 2020 = 110 (data effect: +10%). In the graphic, the 1980 bar is 50px tall and the 2020 bar is 200px tall (visual effect: +300%). Lie Factor = 3.00 / 0.10 = **30**. That is the same mechanism as Tufte's best-known case, the New York Times fuel-economy chart, which he scored at 14.8. The chart claims a tripling-of-effort when the data shows a 10% improvement.

### The six distortion mechanisms

Most lies come from one (or a stack) of these:

1. **Truncated baseline.** Y-axis starts above zero, magnifying small differences. A change from 99 to 101 is a 2.0% data change. Against a baseline of 98 the bars are 1 unit and 3 units tall, a 200% visual change. Lie Factor = 2.00 / 0.0202 â‰ˆ 99.

2. **Area or volume encoding of a linear quantity.** A pie wedge whose *radius* doubles has *area* quadruple; a pictogram of a dollar bill drawn 2Ã— wider also gets drawn 2Ã— taller, so visual area is 4Ã—. If the underlying change is 2Ã— and the visual is 4Ã—, Lie Factor = 2. Tufte's "shrinking dollar" examples are this mechanism.

3. **Dimensional inflation (1D data, 2D or 3D visual).** Encoding a single number with depth, perspective, or 3D extrusion. Adding the third dimension multiplies visual change without adding information. Lie Factor explodes with the cube.

4. **Aspect-ratio manipulation.** Stretching the chart vertically or compressing horizontally to make slopes look steeper (or vice versa). The data values don't change, but the visual encoding of *rate of change* does. Particularly common in stock charts and "hockey-stick" growth slides.

5. **Dual-axis mismatch.** Two y-axes with different scales, chosen to make two unrelated series appear correlated or to make one series dominate. The lie is in the *choice of scaling* â€” the data on each axis is honest, but the visual juxtaposition implies a relationship.

6. **Cherry-picked time window.** Trimming the x-axis to a range that hides contrary trends or noise. Not strictly an encoding lie â€” the *encoding* is honest within the window. But it produces the same effect (an exaggerated visual story) and Tufte includes it under integrity. Flag it separately, not via the LF formula.

### What counts as "size of effect in the data"

For a time series, usually the percent change between the two endpoints being visually emphasized. For a categorical comparison, the percent difference between the two highest-contrast categories. For a distribution, the range or interquartile range. Use whichever quantity the *visual* is most directly encoding â€” if the chart emphasizes a peak, measure the peak's percent change from baseline; if it emphasizes a difference between groups, measure that difference.

### Acceptable distortions

A Lie Factor outside 0.95â€“1.05 is not automatically wrong if it serves the reader, not the author:

- **Log scale**, clearly labeled, when the data spans multiple orders of magnitude
- **Broken axes**, clearly marked with a break symbol, when there's a long gap of empty range
- **Detail zooms** on a small region, clearly labeled as a zoom and presented alongside the full-range view
- **Index series** (everything normalized to a baseline = 100) when comparing growth rates of different-magnitude series

The rule isn't "LF must equal 1." The rule is "if LF â‰  1, the reason must be explicit, in the reader's interest, and labeled in the graphic itself."

## How to apply (step-by-step)

1. **Get the data.** You can't compute a Lie Factor without the underlying numbers. If the user has only a screenshot, ask for the data behind it, OR extract the visible numbers from the chart's labels and treat those as the data baseline. If neither is available, you can flag *suspected* distortion mechanisms qualitatively, but you cannot report a Lie Factor number â€” say so explicitly.

2. **Identify the dominant visual claim.** What is this chart trying to make the reader feel? "Sales surged." "Revenue collapsed." "This is way bigger than that." Pinpoint the single comparison the visual is built around. The Lie Factor only applies to that comparison â€” running it over every minor variation in the chart produces noise.

3. **Measure the visual effect.** In the rendered graphic, measure the physical change that encodes the dominant claim. For a bar chart: pixel heights of the two bars being compared. For a line: vertical position of the two endpoints. For an area: pixel area (width Ã— height for rectangles, Ï€Â·rÂ² for circles). Express as percent change.

4. **Measure the data effect.** From the underlying numbers, compute the same percent change between the same two points.

5. **Compute LF = visual / data.** Round to two significant figures.

6. **Classify the result.**
   - 0.95 â‰¤ LF â‰¤ 1.05 â†’ honest. Note this and stop.
   - 1.05 < LF â‰¤ 2 â†’ mild distortion. Identify the mechanism (which of the six above). Flag for correction unless there's an explicit, labeled, reader-serving reason.
   - 2 < LF â‰¤ 5 â†’ significant distortion. Almost always a correction is needed.
   - LF > 5 â†’ severe distortion. The chart is fundamentally misleading; redraw, don't patch.
   - LF < 0.95 â†’ suppression. The chart hides a real change. Just as much a lie as inflation, but rarer.

7. **Identify the mechanism(s).** Walk the six distortion mechanisms in order. Often there's more than one stacked (e.g., a truncated axis AND a 3D effect). Name each contributor and estimate its share of the total LF.

8. **Specify the corrected version.** For each flagged mechanism, name the fix: "start y-axis at zero," "switch from area to length encoding," "remove the 3D extrusion," "use one y-axis instead of two," "show the full time range, not 2018â€“2023." Don't redraw the chart for the user (that's a redraw skill's job) â€” produce the spec.

9. **Sanity-check by reading the chart out loud.** Read the chart's visual claim, then read the data's claim, in plain English. If a layperson would hear two different stories, the Lie Factor is doing real work. If they'd hear the same story, the chart is honest even if LF is slightly off (e.g., LF = 1.15 in a chart that's clearly labeled and serves the reader).

## Common failure modes

- **Computing Lie Factor without the data.** The temptation is to eyeball the chart and declare it dishonest. Without the numerical baseline, you can only flag *mechanisms* (truncated axis, 3D effect) qualitatively. Don't report a numerical LF you can't compute. Say "this chart shows three of the six distortion mechanisms; we'd need the underlying data to score it." Honest > confident.

- **Applying the formula to the wrong comparison.** A chart usually has one dominant visual claim. Computing LF over every pairwise comparison in a 20-bar chart produces noise. Pick the claim the chart is *built around* and measure that. If the chart has more than one dominant claim, run the analysis once per claim and report separately.

- **Flagging log scales and broken axes as automatic lies.** They aren't, if they're labeled and reader-serving. The rule is intent and labeling, not absence of scale tricks. A log-scale stock chart over 30 years is more honest than a linear one. A broken axis that highlights a 2-unit difference in a 0â€“500 range is dishonest only if the break is hidden.

- **Ignoring stacked mechanisms.** Most lying charts use two or three mechanisms together â€” a truncated axis AND an area encoding AND a 3D effect â€” to compound the visual exaggeration. Identifying only the first mechanism understates the total LF. Walk all six.

- **Reporting LF without the redraw spec.** A score alone is a complaint. The deliverable is a score + the specific design changes that bring LF back to 1.0. Without the spec, the user has a critique but no fix.

- **Treating LF as the only integrity question.** This skill answers "is the encoding proportional?" It does not answer "is the *data* honest" (cherry-picked time windows, selective categories, unlabeled exclusions). Those failures need the broader `tufte-graphical-integrity-principles` skill. If the user is asking about data selection rather than encoding distortion, route over there or run both.

- **Conflating Lie Factor with Chartjunk.** Chartjunk is decorative noise that obscures the data; it can be present in a chart with LF = 1.0. Lie Factor is encoding distortion; it can be present in a chart with zero decoration. They're orthogonal. Don't flag chartjunk findings as integrity violations â€” route to `tufte-chartjunk`.

## References

- *The Visual Display of Quantitative Information*, 2nd ed., chapter 2 (book pages 53â€“78). The Lie Factor formula appears on page 57; the six principles of graphical integrity on pages 74â€“78.
- Tufte's canonical examples: the 1978 New York Times fuel-economy chart (LF â‰ˆ 14.8) and the shrinking-dollar pictograph (LF compounding via area encoding); both are reproduced in chapter 2.
- Companion skill: `tufte-graphical-integrity-principles` (the prescriptive checklist that LF is the quantitative arm of).
- Bertin theoretical foundations: `bertin-levels-of-organization` (Lie Factor math is only meaningful when the data is Qn â€” quantitative); `bertin-retinal-variables` (the encoding-channel choice that determines whether LF applies â€” area-encoded data fails LF differently than position-encoded).
