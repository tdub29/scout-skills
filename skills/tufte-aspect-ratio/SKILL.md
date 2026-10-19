---
name: tufte-aspect-ratio
description: Apply Edward Tufte's rules for chart aspect ratio and proportion from *The Visual Display of Quantitative Information* (2001 2nd ed., ch. 9, pp. 177â€“190) â€” the width:height ratio of a graphic, plus the closely-linked decisions about line-weight hierarchy and which axis to elongate when emphasizing causality. Default: wider than tall (~1.5:1 to 2.2:1), anchored in the horizon-line analogy â€” humans detect deviations from a long horizontal baseline more reliably than from a vertical one. Time-series and trend graphics fit horizontal naturally; the "floating snake" (narrow tall chart) almost always fails. Tufte discusses the Golden Rectangle (~1.618:1) but argues data shape and intent override formal proportions. Use whenever the user asks "what shape should this chart be," wants to know how wide vs. tall their time-series should run, debates whether to make a chart square or stretched, is preparing a chart for a slide deck / print figure / dashboard slot and asking about proportions, wonders if their hockey-stick growth chart's slope is exaggerated by aspect ratio, hears a designer say "let's make it square / portrait / 16:9" and feels it doesn't fit the data, is reviewing a chart whose lines all look the same weight, debates how to emphasize a causal variable's axis, or is auditing chart consistency across a report. Also trigger for "wrong aspect ratio," "this chart looks too tall," "Golden Rectangle," "stretch this chart," "should this be horizontal," "line weight in chart," "which axis to elongate," "cause vs. effect axis." Output is a recommended width:height ratio + axis orientation + line-weight hierarchy spec. Do NOT trigger for axes-as-distortion-mechanism (use `tufte-lie-factor` for aspect-ratio *manipulation* used to lie). This skill is the *honest* aspect-ratio decision for clarity, not the *adversarial* detection of distortion.
---

# Tufte: Aspect Ratio and Proportion

## When to use

Trigger when the question is "what shape should this chart be" â€” proportionally, in width:height, with what line hierarchy, with which axis dominant. Concrete cues:

- The user is laying out a time-series and asking how wide to make it
- A chart's slope looks too dramatic or too flat and the user suspects aspect ratio is the cause
- The user is preparing a chart for a slot of fixed dimensions (slide, print figure, dashboard cell) and asking how to fill it
- A designer or stakeholder is pushing for square, portrait, or 16:9 and the user wants to push back with rationale
- The user is reviewing a chart whose data marks all look the same weight and asking if hierarchy should be applied
- A cause/effect chart needs to emphasize the explanatory variable
- "Golden Rectangle?" comes up in a design discussion
- Auditing a multi-chart report for consistent proportions

Don't trigger for: detecting aspect-ratio manipulation used to lie about growth rates â€” that's `tufte-lie-factor`'s job (the lie-factor mechanism #4). This skill is the *constructive* aspect-ratio decision, not the *adversarial* audit. If the user's question is "is this chart's stretched aspect ratio dishonest," route to lie-factor.

## The framework

### Core thesis

The shape of a graphic should follow the shape of the data. Most quantitative data â€” especially time-series, trend, and causal sequences â€” has a natural horizontal axis: time goes left to right; cause precedes effect. Wider-than-tall charts (~1.5:1 to 2.2:1) align with this natural flow and with human perceptual biases: we detect deviations from a long horizontal baseline more easily than from a tall vertical one (the "horizon" analogy). The "floating snake" (a tall, narrow time-series) compresses the time axis, exaggerates short-term slope, and almost always fails its purpose.

The Golden Rectangle (~1.618:1) gets cited as a default; Tufte mentions it but argues *context* â€” what the data is and what the reader needs to see â€” overrides any formal proportion. The right ratio is the one that lets the data tell its story without distortion.

### Sub-rule 1 â€” The horizontal default

Time-series and trend charts default to wider than tall. The recommended band is 1.5:1 to 2.2:1, with 1.6:1 (close to the Golden Rectangle) and 2:1 as common landings. This default holds because:

- Time reads left to right; horizontal width gives time room to breathe
- The eye detects slope deviations more reliably against a long horizontal baseline (horizon perception)
- Labels along the time axis fit horizontally without rotation
- Comparison across long time spans needs horizontal length, not vertical compression

### Sub-rule 2 â€” The horizon-line analogy

Why wider-than-tall? Tufte's perceptual argument: human visual systems evolved to detect deviations from a horizontal baseline (the horizon). We're far more sensitive to a bump that rises *off* a long horizontal line than to one that pokes sideways from a vertical line. Charts that mimic this â€” long horizontal baseline, modest vertical variation â€” leverage the perceptual hardware. Charts that fight it (narrow vertical with exaggerated slope) feel jumpy or alarmist even when the data is calm.

### Sub-rule 3 â€” Override the default when data demands

The horizontal default is a starting point, not a rule. Override when:

- The data's natural range is more vertical than horizontal (e.g., a profile of altitude over a short distance)
- The chart needs to fit a vertical slot (sidebar in print, narrow phone screen) and information loss is acceptable
- The reading task is precise comparison of vertical values (in which case taller helps)
- The chart is one panel of a small-multiples grid whose overall layout dictates panel shape

When you override, *say why*. Default proportions need no defense; overrides need explicit justification.

### Sub-rule 4 â€” Line-weight hierarchy (folded in from Ch 9)

A chart whose lines are all the same weight flattens visual hierarchy. Tufte's rule: vary stroke weight to encode importance. The primary data line carries the heaviest stroke; secondary lines (axes, gridlines, reference marks) are noticeably lighter (30â€“50% of the primary's weight). The contrast directs the eye to what matters without explicit annotation.

Sub-rule sub-rules:
- Don't use more than 3 weight levels (more = noise)
- The contrast should be visible at the chart's intended viewing distance â€” not extreme
- Map weight to *information importance*, not to design preference

### Sub-rule 5 â€” Causal-axis emphasis (folded in from Ch 9)

When a chart implies cause-and-effect (treatment â†’ response, dose â†’ effect, time â†’ outcome), elongate the axis representing the *cause*. The longer axis gets visual prominence and gives room for annotations, breakpoints, and reference markers along the causal mechanism. Squeezing the causal axis suggests the cause is incidental; stretching it signals "follow this dimension to understand the relationship."

Practical: in a time-series, time is causal â€” make it the longer axis (horizontal). In a dose-response chart, dose is causal â€” make it the longer axis. In a treatment-comparison chart, treatment is the indexing variable, not strictly causal â€” small-multiples may be the better pattern.

## How to apply (step-by-step)

1. **Identify the data's natural orientation.** Where does time/cause/independence run? That direction wants the longer axis.

2. **Compute the data's intrinsic aspect ratio.** Take the range of the x-data and divide by the range of the y-data, both scaled to a common unit. This gives the *data-shape* ratio. A 30-year time-series with values from 0 to 100 has very different intrinsic shape than a 1-week series with values from 0 to 100.

3. **Start with the horizontal default.** Default to width:height between 1.5:1 and 2.2:1. Time-series, trend charts, cause-effect charts: default applies.

4. **Test for override conditions.** Walk through:
   - Is the data's natural range more vertical than horizontal? Override toward square or slightly taller.
   - Does the layout slot dictate dimensions? Adapt â€” but flag the cost.
   - Is the reading task precise vertical comparison? Slightly taller may help.
   - Is this a panel in a small-multiples grid? Match the grid's panel shape.

5. **Choose the final ratio.** Pick a specific number (e.g., 1.8:1, or 2:1) â€” not a range. State the value.

6. **Apply line-weight hierarchy.** Identify the primary data line(s). Heaviest weight. Secondary structural ink (axes, ticks): 30â€“50% of primary weight. Tertiary (reference lines, light gridlines if any): even lighter. No more than 3 levels.

7. **Apply causal-axis emphasis if relevant.** If the chart implies cause-effect, confirm the cause is on the longer axis. If not, swap orientation or annotate why you didn't.

8. **Cross-check against `tufte-lie-factor`.** Aspect-ratio choices can become Lie Factor violations when manipulative. Run a quick check: does your chosen aspect ratio make the data's effect look proportionally honest, or does it exaggerate slope to "make the point pop"? If the latter, dial back.

9. **Deliver the spec.** Final output: width:height ratio + axis orientation + line-weight hierarchy + brief rationale per choice (default vs. override, why this weight on the primary line, etc.).

## Common failure modes

- **The "hockey-stick" stretch.** Compressing the time axis or stretching the value axis to make growth look more dramatic than it is. The chart now lies about rate of change. This is where `tufte-aspect-ratio` and `tufte-lie-factor` collide â€” and lie-factor wins. If your goal is "make the growth look bigger," stop and re-route.

- **Template-driven proportions ignoring data shape.** Slide-deck templates default to 16:9 or 4:3 panels; dashboard frameworks default to square cards. Filling those slots with data of a different intrinsic shape produces distortion. Either resize the slot or accept a partly-empty panel â€” don't stretch.

- **Vertical orientation for time-series (the classic mistake).** A vertical time-series compresses time into a narrow column. It looks jumpy, slopes look exaggerated, labels rotate awkwardly. Almost never the right choice. Default to horizontal.

- **One uniform line weight across all marks.** Without hierarchy, the eye doesn't know where to land. Data, axes, gridlines, reference marks all read at the same priority. Apply 2â€“3 weight levels mapped to importance.

- **Squeezing the causal axis to fit a layout.** A dose-response chart with the dose axis compressed into 1/4 of the chart width signals "dose is incidental." Even if the layout demands compression, lengthen the dose axis at the cost of vertical room.

- **Treating the Golden Rectangle as mandatory.** Tufte mentions ~1.618:1 as a defensible default â€” not a rule. The ratio should follow the data and the reading task. Don't reach for the Golden Rectangle when the data wants 2.2:1 or 1.3:1.

- **Ignoring viewing context.** A print figure and a phone screen tolerate different aspect ratios. A 3:1 chart looks fine in a wide PDF figure and unreadable on a vertical phone. Design for the worst-case viewing context.

- **Adding line-weight variation without mapping to importance.** Random thick/thin variation is decorative â€” chartjunk territory. Hierarchy means weight encodes importance. Always anchor weight choices to "what does this line mean to the reader."

## References

- *The Visual Display of Quantitative Information*, 2nd ed., chapter 9: "Aesthetics and Technique in Data Graphical Design" (book pages 177â€“190). Discusses proportion, the horizon analogy, the Golden Rectangle, line-weight differentiation, and causal-axis elongation.
- Tufte's perceptual argument for the horizontal default draws on the visual system's bias toward horizon-detection â€” explicit in Ch 9.
- Sibling carved skills:
  - `tufte-lie-factor` â€” the adversarial counterpart. Aspect ratio is distortion mechanism #4 in lie-factor's six-mechanism taxonomy. This skill is the constructive side; lie-factor is the audit side.
  - `tufte-data-density` â€” wider charts often enable higher density; the two decisions interact.
  - `tufte-graphical-integrity-principles` â€” Principle 1 (proportionality) is the integrity-side statement; this skill is the layout-side decision that, done right, supports it.
  - `tufte-small-multiples` â€” when panel shape in a multiples grid is the question, route there.
  - `tufte-data-ink-ratio`, `tufte-chartjunk` â€” orthogonal but worth running in concert for a full chart review.
- Bertin theoretical foundation: `bertin-legibility-rules` â€” Bertin's angular-legibility rule (70Â° elementary, 45Â° overall, 2mm shape minimum) is the perception-science underneath Tufte's slope-and-proportion practice.
