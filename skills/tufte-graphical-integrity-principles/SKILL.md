---
name: tufte-graphical-integrity-principles
description: Apply Edward Tufte's Six Principles of Graphical Integrity from *The Visual Display of Quantitative Information* (2001 2nd ed., ch. 2, pp. 74â€“78) to audit a chart, graphic, or data visualization for truthfulness â€” the obligation that every visual mark must tell the same story as the numbers, labeling must be thorough, and data must never be quoted out of context. Use whenever the user is finalizing a chart for publication, shares a chart and asks "is this honest," worries a visualization might mislead, asks "what makes a graphic lie," debates a design choice that affects how readers perceive data, receives a chart from stakeholders and needs an integrity audit, is building style guides or design systems and wants to codify integrity rules, hears "make this look more dramatic" and feels uncomfortable, debates whether axes should start at zero, questions if truncating the time range is fair, realizes a published visualization may have been deceptive, or wants principles to keep all charts in a dashboard honest. Also trigger for "does this graphic distort the numbers," "why does this visualization feel misleading," "I need an integrity checklist before presenting," "audit this dashboard," "does our sales chart exaggerate growth," or "what are the rules for truthful graphics." Output is a six-principle scorecard (pass/fail per principle), a diagnosis of which principles are violated and the specific mechanism of each violation, and concrete remedies. Do NOT trigger for pure Lie Factor calculation (use `tufte-lie-factor` for the quantitative metric), chart-type selection (general data-viz), or aesthetic style (design skills) â€” this skill owns the prescriptive checklist framework, not the math or the looks.
---

# Tufte: Six Principles of Graphical Integrity

## When to use

Trigger when the core question is "does this graphic tell the truth?" â€” not "is it pretty," not "is it the right chart type," but whether the entire design preserves integrity from data selection through visual encoding to context. Concrete cues:

- The user is about to ship a chart or dashboard and wants a final integrity audit
- A chart looks off, and the user asks whether it's misleading
- The user is worried they (or someone else) accidentally lied with a graphic
- The user is designing a publication and wants principles to govern all charts
- Someone asks the user to make a chart "look more dramatic" or "show the impact better"
- A time-series is missing context (starts mid-trend, hides earlier decline, etc.)
- A chart's labeling is minimal and the user wonders if data might be misunderstood
- The user is auditing a competitor's or stakeholder's chart for credibility
- A dashboard shows many charts at once and the user wants consistency in how data is presented
- The user is building team style guides or publishing standards

Don't trigger for: Lie Factor calculation (that's the quantitative arm; use `tufte-lie-factor` for the math). Chart-type selection (bar vs. line â€” use general data-viz). Aesthetic polish (colors, fonts, spacing â€” use design skills). Small-multiples layout (use `tufte-small-multiples`). Chartjunk removal (use `tufte-chartjunk` or `tufte-data-ink-ratio`). This skill answers "is the entire graphic, as designed, truthful?" once the encoding is locked in.

## The framework

### Core thesis

A graphic is a language. It makes a claim about numbers using visual marks. Like any language, it can lie â€” by distorting encoding, hiding context, or letting design variation obscure data variation. Tufte's six principles are a checklist for *integrity*: the visual encoding must tell the same story as the numbers, labeling must be complete and transparent, and the data must be presented fairly. The principles are not about taste or innovation; they're about truthfulness. A chart can be ugly and honest; it can be beautiful and deceiving. Integrity comes first.

The principles form a system: some catch distortions in *encoding* (1 and 5), some defend against ambiguity (2), some insist on honest *context* (6), and some impose operational rules for specific domains (3 and 4). The test they collectively impose: would a knowledgeable reader, looking at the graphic alone, draw the same conclusion from the visual as they would from the underlying data?

### Principle 1 â€” Proportionality

> "The representation of numbers, as physically measured on the surface of the graphic itself, should be directly proportional to the numerical quantities represented."

The visual change must match the numerical change. A 50% data increase should not show as a 300% taller bar. This is the foundation of the Lie Factor (see `tufte-lie-factor` for the metric). When this breaks, readers misunderstand magnitude and the graphic becomes propaganda.

**Common violations:** Truncated y-axes, area/volume encoding of linear quantities, 3D effects, aspect-ratio manipulation, dual-axis mismatch, cherry-picked windows.

### Principle 2 â€” Clear, detailed, thorough labeling

> "Clear, detailed, and thorough labeling should be used to defeat graphical distortion and ambiguity. Write out explanations of the data on the graphic itself. Label important events in the data."

A chart with no labels invites misreading even when the encoding is honest. Labeling is a *defense*: it gives the reader the numbers to check, the units to interpret magnitude, the source to judge credibility, and the events to understand discontinuities. A graphic should stand alone â€” readable without surrounding prose, footnotes, or captions that may not travel with it.

**Common violations:** Missing axis labels / units / zero-line markers. Source attribution absent. Legend missing or hard to parse. No data-currency note. Important events (recessions, product launches, definitional changes) not annotated on the data itself.

### Principle 3 â€” Show data variation, not design variation

> "Show data variation, not design variation."

Every visual element â€” color, line style, marker shape, fill pattern, 3D effect â€” should encode data, not decoration. Variation in the visual should *correspond* to variation in the numbers. If you change a color, it should be because the data changed; if you add a marker, it should be because there's a new variable. Otherwise the reader's attention is spent on ornament instead of information.

**Common violations:** Chartjunk (3D effects, drop shadows, pictogram inflation, decorative textures). Color variations that don't encode anything. Heavy gridlines competing with data. Shading or pattern fills chosen for aesthetics. This principle is the integrity-side statement of `tufte-data-ink-ratio` and `tufte-chartjunk`.

### Principle 4 â€” Deflated and standardized monetary units

> "In time-series displays of money, deflated and standardized units of monetary measurement are nearly always better than nominal units."

A revenue chart showing $1M in 1980 vs. $100M in 2020 looks like a 100Ã— explosion â€” but inflation alone explains much of that. Nominal dollars hide the real story. Use deflated (inflation-adjusted to a base year) or indexed (everything normalized to baseline = 100) series instead. This logic generalizes to *any* quantity where scale or adjustment matters â€” per-capita rates, share of growing totals, ratios across changing populations.

**Common violations:** Nominal dollars across decades without inflation note. Aggregate metrics that should be per-capita. Comparisons across organizational structures that changed between periods.

### Principle 5 â€” Information-carrying dimensions â‰¤ data dimensions

> "The number of information-carrying (variable) dimensions depicted should not exceed the number of dimensions in the data."

Two variables, two visual dimensions. Three variables, three (e.g., x, y, color). Adding extra channels â€” bubble size that's redundant with x-position, perspective tilt on a 2D quantity, color that re-encodes what position already shows â€” adds noise without information. Tufte's test: if you remove a visual dimension, does the chart lose a variable or just lose clutter? If clutter, it was design variation, not data.

**Common violations:** Redundant encoding (size *and* position for the same variable). Gratuitous color when there's no categorical variable. 3D extrusion of a 1D quantity. Decorative pictograms whose area inflates beyond the data magnitude.

### Principle 6 â€” Don't quote data out of context

> "Graphics must not quote data out of context."

A spike in March 2020 is truthful only if the chart shows the surrounding trend or notes why March was unusual. A "50% growth last quarter" claim is deceptive if it omits that the prior three quarters had losses. Context includes the full time range (not cherry-picked), comparables (this vs. similar cases), and explanations of structural shifts (definitional changes, M&A, divestitures). The chart must not imply a story the data does not support when the full picture is available.

**Common violations:** Arbitrary time windows hiding earlier trends. Ignoring seasonality. Comparing across changed organizational structures. Hiding baseline anomalies (Year 1 was a disaster, so Year 2 looks like a normal recovery rather than the rebound it really is). Not disclosing data quality issues.

## How to apply (step-by-step)

1. **Gather the graphic AND the underlying data.** Both. If only a screenshot is available, ask for the numbers or extract them from labels. You cannot audit Principles 1 or 4 without the data â€” only flag *candidates* qualitatively.

2. **Name the central claim.** In one sentence: what is the chart trying to make the reader feel? "Sales surged in Q4." "Region A beats Region B." Pin down the dominant message the visual is built around. Multiple competing messages = likely Principle 6 or Principle 3 failure.

3. **Test Principle 1 (proportionality).** Measure visual change for the dominant claim. Compare to numerical change. Within ~5%? Pass. Otherwise, identify the mechanism (truncated axis, area encoding, 3D, aspect-ratio squeeze, dual-axis mismatch). For a numerical Lie Factor score, route to `tufte-lie-factor`.

4. **Test Principle 2 (labeling).** Confirm all of: axis labels, units, zero/baseline marker, source, currency date, key event annotations, legend (if categorical encoding). Can a reader understand and verify the chart *from the graphic alone*? If not, list missing labels.

5. **Test Principle 3 (data vs. design variation).** Walk every visual element. Does it encode a variable? If decoration, does it obscure the data? Don't deep-audit chartjunk here â€” that's `tufte-chartjunk`'s job â€” but flag obvious offenders.

6. **Test Principle 4 (monetary/scale context).** If the chart shows money, prices, or anything inflation/scale-sensitive: nominal or deflated? Per-capita or aggregate? If unadjusted, does the graphic explicitly say so?

7. **Test Principle 5 (dimensions).** Count data variables. Count visual channels (axes, color, size, shape, angle, opacity). Channels > variables = redundant or decorative dimensions. List them.

8. **Test Principle 6 (context).** Ask: what's the full data range? Are there structural shifts the chart should disclose? How does this compare to baselines / norms / similar cases? If omitting context would change a reader's interpretation, fail.

9. **Produce the scorecard.** For each principle, Pass or Fail. For each Fail: (a) the violation, (b) why it matters (what the reader will misunderstand), (c) the specific remedy.

10. **Sanity-check by reading aloud.** State the chart's visual claim. State what the data actually shows. Do they match? A layperson hearing both should expect the same numbers.

## Common failure modes

- **Auditing without the data.** Eyeballing alone gets you candidate violations, not confirmed ones. Be explicit about which principles you can verify and which you can only suspect.

- **Focusing only on Principle 1 and ignoring the others.** Proportionality is critical but not sufficient. A chart with Lie Factor = 1.0 can still fail labeling, design-vs-data variation, monetary context, or out-of-context quoting. Run all six.

- **Conflating "honest encoding" with "complete context."** Principle 1 and Principle 6 fail independently. A perfectly proportional chart that shows Janâ€“Mar when the full year would change the story is honest-in-the-small and dishonest-in-the-whole.

- **Accepting minimal labeling because "the data's there."** Principle 2 is about whether the chart stands alone, not whether the data exists somewhere. Charts get shared, screenshotted, embedded â€” the prose may not travel with them.

- **Skipping the "important events" annotation under Principle 2.** A decade-long unemployment chart without recession markers is failing both Principle 2 (labeling) and Principle 6 (context).

- **Treating Principle 4 as financial-only.** "Money" is the example; the logic applies to any quantity where scale, inflation, or population adjustment matters. Crime rates without population adjustment, downloads without app-store growth context, revenue per employee without headcount changes â€” all are Principle 4 territory.

- **Reporting violations without remedies.** A failing scorecard alone is a complaint. The deliverable is principle + violation + remedy. Without the remedy, the user has critique but no path.

- **Treating every failure as fatal.** Some violations are acceptable in some contexts. A newsroom can run a truncated-axis chart if the break is explicit. A regulatory submission probably can't. Score the failures; let the user decide which to accept.

- **Skipping Principle 5 as too abstract.** "Information-carrying dimensions" sounds theoretical until you count. A bubble chart where bubble *size* duplicates the x-axis is a textbook Principle 5 violation. Always count.

## References

- *The Visual Display of Quantitative Information*, 2nd ed., chapter 2 (book pages 53â€“78). The six principles are stated verbatim on pages 74â€“78; surrounding pages cover the Lie Factor formula, labeling examples, monetary context cases, and famous integrity failures.
- Tufte's canonical example: the OPEC fuel-economy chart (Lie Factor â‰ˆ 14.8) â€” a 10% data change shown as ~300% visual change via 3D + aspect-ratio squeeze. Violates Principles 1 and 5 simultaneously.
- Sibling carved skills:
  - `tufte-lie-factor` â€” quantitative arm of Principle 1
  - `tufte-data-ink-ratio` â€” operational sibling of Principle 3
  - `tufte-chartjunk` â€” decorative-noise sibling of Principle 3
  - `tufte-small-multiples` â€” a design pattern that honors Principles 1, 2, and 3
  - `tufte-aspect-ratio` â€” closely linked to Principle 1 (proportionality of slope)
  - `tufte-data-density` â€” efficiency principle that complements integrity
- Bertin theoretical foundations: `bertin-levels-of-organization` (Principle 5 â€” information-carrying dimensions â‰¤ data dimensions â€” is Bertin's level-matching rule restated as integrity); `bertin-invariant-components` (Principle 6 â€” don't quote data out of context â€” is the invariant-honesty check in chart-audit form); `bertin-retinal-variables` (Principles 1, 3, and 5 all reduce to "match the channel's perceptual capacity to the data type").
