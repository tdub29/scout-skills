---
name: bertin-legibility-rules
description: "Chart legibility limits: density, angle, mark size"
---

# Bertin: Rules of Legibility

## When to use

Trigger when the question is "can readers actually perceive what I'm encoding here?" â€” the quantitative thresholds beyond which the eye fails. Concrete cues:

- The user has a dense chart (many points, many marks, many small cells) and wonders if it's too packed
- A chart that looked fine in design fails on a phone, projector, or print at small size
- "How small can I make these symbols and still have them readable?"
- The user is preparing a chart for print at known dimensions and wants to verify it'll work
- A heatmap or scatterplot is sparsely filled and the user wonders if marks are too small / too few
- The user is auditing a chart for accessibility (low-vision readers, small viewing distances)
- "Why does this chart look muddy when I zoom out?"
- A chart with many distinct shapes (point, dash, cross, circle, square, ...) and the user wonders how many are too many
- "Should I increase the contrast?" or "Why does the chart look gray instead of high-contrast?"

Don't trigger for: ink-economy decisions about structural elements (`tufte-data-ink-ratio`), decorative noise (`tufte-chartjunk`), chart-type selection. This skill is specifically about quantitative perceptual thresholds â€” graphic density, angular legibility, retinal legibility â€” at which the eye stops being able to do its job.

## The framework

### Core thesis

Visual perception has hard limits. A mark below a certain size is invisible. A grid of marks above a certain density merges into texture. A figure with less than ~5% black ink fades into the background; with more than ~10% it inverts (black becomes the figure, white becomes the marks). These thresholds aren't matters of taste â€” they're functions of human visual acuity, retinal spacing, and Gestalt closure mechanisms.

Bertin's three rules give *quantitative* guidance: numbers, percentages, sizes in mm. Most modern data-viz advice is qualitative ("don't make it too small," "use enough contrast"). Bertin tells you the actual thresholds. Use them as design guardrails â€” if your chart violates them, the chart will silently fail for some readers.

### Rule 1: Graphic Density (~10 marks/cmÂ² upper limit for figuration)

**The rule.** In figuration (a chart made of heterogeneous, discrete marks â€” symbols on a map, points on a scatterplot, cells in a sparse matrix), the upper limit for legible individual marks is roughly **10 marks per cmÂ²** of meaningful diagram area.

**Why.** At 10 marks/cmÂ², the average inter-mark spacing is ~3.2 mm. At normal print/screen viewing distance (~30 cm), this approaches the angular resolution of the eye for separating distinct marks. Beyond this density, marks merge optically into texture â€” the reader can still see *something* but no longer perceives individual marks.

**What this means.**
- Above ~10 marks/cmÂ², the chart is no longer a figuration â€” it becomes an *image* (a textured field) and elementary reading (looking up specific marks) fails.
- Image-level reading (overall pattern, gradients, regions) can still work at higher densities â€” that's why dense scatterplots become useful as heatmaps even when individual points are unreadable.
- A chart that's intended as a figuration (lookup is required) must respect this density.

**Practical conversion.** A chart's "meaningful area" is the inner data region, excluding margins. For a typical 10Ã—15 cm print chart: meaningful area â‰ˆ 150 cmÂ² â†’ max ~1500 marks. For a 600Ã—400 pixel screen chart at typical screen density: meaningful area â‰ˆ ~14 cmÂ² â†’ max ~140 marks. Beyond these counts, the chart should be reframed as an image (color-density encoding) or aggregated.

### Rule 2: Angular Legibility and Shape Minimum

**The angular rules.**
- **Elementary level** (single-mark reading): ~70Â° orientation is optimum for shape distinction. A line tilted at 70Â° from horizontal is easier to distinguish from one tilted at 0Â° than two lines at, say, 5Â° vs. 15Â°.
- **Overall level** (whole-image reading), when the chart approaches a square in proportions: ~45Â° (the diagonal) is optimum. The eye prefers diagonal scan paths in roughly-square images.

**The shape-size rule.** A shape needs at least ~2 mm linear dimension (height or width) to register as a SHAPE â€” to be perceived as "a circle" vs. "a square" vs. "a triangle." Below 2 mm, the eye sees a point and shape is lost.

**The shape-cardinality limit.** At maximum reduction (small shapes near the legibility floor), only ~3 distinct shapes remain reliably distinguishable: **point, dash, cross**. Above that scale, more shapes work (5â€“7 reliable shapes at normal size: point, dash, cross, circle, square, triangle, asterisk).

**What this means.**
- If you're encoding categories by shape, count them. >7 shape categories â†’ eye fails. Switch to color, or aggregate.
- If marks are rendered below 2 mm linear dimension (e.g., on a thumbnail or phone view of a dense chart), only "is there a mark here or not" reads; shape distinctions disappear.
- Charts that need to work across viewing contexts should be designed for the worst-case mark size (smallest expected viewing context).

### Rule 3: Retinal Legibility (5â€“10% black-ink area)

**The rule.** Within a meaningful diagram region, the proportion of "black" (ink, mark, foreground) should fall between **~5% and ~10%** of the area for optimal figure/ground separation.

**Why.**
- **Below 5%:** marks are too sparse against the white background; figure/ground contrast is weak; the eye doesn't reliably separate the marks from the surface.
- **Above 10%:** Gestalt closure inverts. The eye reads the BLACK as the figure and the WHITE between it as the marks. This is the same perceptual flip that makes a starry night sky read as "white dots on black" rather than "black between stars." Inversion is fine *if intentional* (dark-background charts) but accidental inversion confuses readers.

**The wider point.** Figure/ground perception is the FIRST step in reading any graphic â€” before the eye perceives shape, color, or position, it must separate figure from ground. If that fails, nothing else works.

**Practical conversion.**
- Sparse scatterplots (e.g., 50 dots on a large canvas): often <5% â€” boost contrast by enlarging dots, adding light reference structure, or using a darker color.
- Dense scatterplots (e.g., 10,000 dots): often >>10% â€” Gestalt has inverted; either accept the dark-figure read (treat the cloud as the data shape), reduce point size to come back below 10%, or use a density encoding instead of individual points.
- Heatmaps with strong contrast (deep blue on white, deep red on yellow): the rule still applies, just measured per color rather than literal black.

### The three rules in concert

These rules are independent â€” a chart can pass one and fail another:

- A scatterplot with 50 large dots: passes density (well below 10/cmÂ²), might fail shape if dots are >2 mm but you've also encoded shape variation that's now lost in the size; might fail figure-ground if dots are tiny enough that <5% of canvas is filled.
- A dense heatmap: fails density (treats as image), passes shape (no shape variation to fail), the figure/ground rule applies to the gradient instead of literal black.
- A 200-point chart with 8 shape categories: density fine, angular fine, shape-cardinality FAILS (>7 shapes â†’ some indistinguishable).

Run all three.

### Where the numbers come from

Bertin's thresholds are empirical â€” derived from typographic standards, cartographic practice, and visual-physiology research extant in the 1960s. They're guidelines, not natural constants:

- The 10 marks/cmÂ² density limit is approximate; depending on mark size, shape contrast, and viewing distance, the real limit ranges roughly 5â€“20 marks/cmÂ².
- The 2 mm shape-minimum assumes ~30 cm viewing distance. For posters viewed from 2 m, minimums scale up; for tablets held at 25 cm, they scale slightly down.
- The 5â€“10% figure/ground band shifts depending on contrast strength (pure black on pure white tolerates wider extremes than blue on light yellow).

Treat the numbers as Bertin intends: design defaults, with override when the viewing context warrants.

## How to apply (step-by-step)

1. **Determine the meaningful diagram area in cmÂ² at the smallest expected viewing size.** This is the inner data region, not the full chart frame. Use the smallest size the chart will be viewed at (thumbnail, phone, projected slide) â€” design for worst case.

2. **Run the density check.**
   - Count the marks in the diagram area.
   - Compute marks / cmÂ². If >10, the chart is image-level only; figuration / lookup will fail.
   - Decision: accept image-level reading and drop figuration claims, or reduce density (aggregate, sample, filter, separate into multiples).

3. **Run the angular / shape checks.**
   - At the smallest expected rendering, measure mark size in mm (or pixels converted to mm using viewing-distance / DPI).
   - If shapes are below 2 mm linear dimension: shape distinctions fail. Either enlarge or stop relying on shape for encoding.
   - Count shape categories. If >7 distinct shapes (or >3 at extreme small size): re-encode with color or position.
   - Check orientation: if categories are encoded by orientation, ensure adequate angular separation (60Â°+ between categories ideal).

4. **Run the figure/ground check.**
   - Estimate the % of meaningful area filled with figure (ink, marks, dark color).
   - If <5%: too sparse; figure/ground perception weak. Enlarge marks, add light grid for context, or accept low contrast (but warn the user).
   - If >10%: Gestalt inversion has happened. Decide: is the dark-figure read intentional (and labeled as such), or accidental? If accidental, reduce ink (smaller marks, fewer marks, opacity reduction).

5. **Identify failures and remedies.**
   - Density violation â†’ aggregate, sample, or split
   - Shape-size violation â†’ enlarge marks or drop shape encoding
   - Shape-cardinality violation â†’ reduce categories or re-encode
   - Figure/ground violation â†’ adjust contrast, mark size, or inversion strategy

6. **Produce the audit document.** Per rule: PASS / FAIL with the measured number and the threshold. For each FAIL, name the specific remedy.

7. **Re-test at expected viewing contexts.** If the chart will be viewed at multiple scales (web preview thumbnail, full-size print, projected slide), run the audit at the worst-case size. A chart that passes at design size but fails at thumbnail size has only conditionally passed.

## Common failure modes

- **Designing at one scale and shipping at another.** A chart designed at full-size desktop view fails when embedded as a thumbnail in an email or shown on a projector at 30 ft. Always design for the worst-case viewing context.

- **Treating density as a soft preference.** "It looks crowded but I think it's fine" â€” Bertin's number is empirical. Above ~10 marks/cmÂ² individual lookup genuinely fails for most readers. Don't rely on your familiarity with the chart to overestimate readability.

- **Ignoring shape cardinality.** Encoding 12 product categories by 12 distinct shapes. The reader can't reliably distinguish more than ~7. Either reduce to a meaningful subset, group similar categories, or re-encode by color.

- **Conflating size with shape.** Making marks bigger doesn't help shape distinction if the shapes are similar in form. A 3 mm circle vs. 3 mm square is distinguishable; a 3 mm hexagon vs. 3 mm octagon is not.

- **Hidden Gestalt inversion.** A dense scatterplot where >10% of the canvas is ink â€” the eye now reads the dark mass as the figure (e.g., "the data cloud") and the white as the marks. Sometimes useful (point-cloud analysis); often misleading (readers think they're seeing scattered points and they're not).

- **Skipping the audit on dashboards.** Dashboards often combine charts at different rendering scales. Each chart was probably designed full-size; in the dashboard they render at thumbnail. Run the audit on each at its rendered size.

- **Treating the numbers as universal.** Bertin's thresholds assume normal-sighted readers at ~30 cm viewing distance, normal lighting, decent print/display quality. For accessibility (low-vision readers), poor projection conditions, or moving displays, scale conservatively (larger marks, lower density, higher contrast).

- **Not labeling intentional rule violations.** Sometimes a dense chart IS the right design (clustering reveals via image-level reading). Don't pretend the chart respects figuration density; explicitly say "this is a density visualization, individual points are not distinguishable" so readers calibrate their reading.

- **Confusing this skill with `tufte-data-density`.** Bertin: quantitative thresholds at which the eye fails. Tufte: efficiency principle for ink-per-area. They're related but distinct â€” Tufte argues *for* density as efficiency; Bertin says *how much* density before perception breaks. Run both: density first (does the chart pass legibility), then data-density (is the chart making good use of the ink it does have).

## References

- Jacques Bertin, *Semiology of Graphics* (1967; English 1983; Esri 2011 ed.), Chapter III.E â€” "General Rules of Legibility (or Rules of Separation)," book pages 175â€“190.
  - Graphic density: pages 176â€“178
  - Angular legibility: pages 178â€“180
  - Retinal legibility: pages 180â€“190
  - Summary of the rules: page 190

- Sibling Bertin skills:
  - `bertin-retinal-variables` â€” what gets encoded; this skill answers whether that encoding will remain perceivable
  - `bertin-image-vs-figuration` â€” the perceptual layer; density violations are how a figuration becomes an image-level-only chart
  - `bertin-reorderable-matrix` â€” applied technique that operates near these legibility limits

- Related Tufte skills:
  - `tufte-data-density` â€” argues *for* density as efficient; this skill bounds that argument with the perceptual ceiling
  - `tufte-aspect-ratio` â€” angular considerations in the slope domain; Bertin's angular legibility is the shape-recognition domain
  - `tufte-data-ink-ratio` â€” chooses what ink to spend; this skill quantifies when there's too much ink

- Modern research: Cleveland & McGill (1984), "Graphical Perception" â€” empirical studies extending Bertin's perceptual rules with controlled experiments; the foundation of much modern viz-perception research.
