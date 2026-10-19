---
name: bertin-retinal-variables
description: Apply Jacques Bertin's framework of the seven retinal (visual) variables from *Semiology of Graphics* (1967; English 1983; Esri 2011 ed., ch. II.C, pp. 60â€“97) â€” the six retinal marks elevated above the plane (SIZE, VALUE, TEXTURE, COLOR/HUE, ORIENTATION, SHAPE) plus the two planar dimensions (X, Y), each with measurable perceptual properties (SELECTIVITY, ASSOCIATIVITY, ORDERED PERCEPTION, QUANTITATIVE PERCEPTION) that determine which data types each variable can honestly encode. Use whenever the user is choosing how to encode a data variable in a chart, debating "should I use color, size, or shape for this dimension," asks why a chart's color isn't communicating order, wonders why a shape-encoded category doesn't visually group, debates ordinal vs. categorical encoding, is building a custom data-viz library and wants to ground encoding choices in perception theory, asks "what's the right visual variable for ranked data," or is reading Tufte / Wilkinson / Munzner / Few / Ware and needs the original Bertin theory underneath them. Also trigger for "visual variables," "Bertin's framework," "encoding channels," "selectivity," "associativity," "ordered perception," "perceptual hierarchy of visual variables," "why doesn't this chart's color show ranking," "is shape ordered," "can I use texture for ratios," "which channel for which data type," or "perceptual hierarchy of encoding." Output is an encoding-decision artifact: for each data component to be displayed, the recommended retinal variable + the four-property check (selectivity / associativity / order / quantitation pass-or-fail) + a warning if the chosen variable's perceptual capacity doesn't match the data's organizational level. Do NOT trigger for chart-type selection (bar vs. line â€” general data-viz), aesthetic color choice (design), or implementation in a specific plotting library (use the library's docs). This skill owns the foundational perception theory â€” the layer underneath every modern grammar-of-graphics tool.
---

# Bertin: The Retinal Variables

## When to use

Trigger when the question is "which visual channel should encode this variable, and will it actually be perceived correctly?" â€” not "what chart type should I use," not "what color palette is pretty." Concrete cues:

- The user is mapping a data variable to a visual channel and unsure which to pick
- A chart's encoding "looks right" but readers can't extract the intended information ("why can nobody tell the difference between these categories")
- The user is debating size vs. color vs. shape for a third dimension on a scatter plot
- A categorical variable is encoded by color and the user is wondering if hue can be ordered (it can't, except via value gradation)
- The user is building a design system or chart library and wants encoding rules grounded in theory
- "Why doesn't this map's color show ranking?" â€” value-vs-hue confusion
- The user is reading Wilkinson's *Grammar of Graphics*, Tufte, Munzner, Few, or Ware and needs the original source theory
- The user wants to defend an encoding choice in a design review

Don't trigger for: chart-type selection (general data-viz), color palette decisions (design / accessibility skills), implementation in a specific library (Vega / D3 / matplotlib docs), or pure aesthetic concerns. This skill answers "is the chosen variable perceptually capable of carrying this data type."

## The framework

### Core thesis

A graphic encodes information by varying *something* the eye can perceive. Bertin's contribution: the eye does not perceive all visual changes equally. Some changes are perceived *selectively* (you can pick out one category from a crowd); some support *order* (red comes after orange comes after yellow only if value varies); some support *quantitative ratios* (a bar twice as tall is perceived as twice the value). Different visual channels have *different* perceptual capacities. Match the channel to the data type or the graphic silently lies.

Modern grammar-of-graphics tools (ggplot, Vega, Plotly, Observable Plot, Tableau's "Show Me") implement Bertin's framework implicitly â€” they map data variables to "aesthetics" or "encodings." But they often don't surface *which encoding is appropriate for which data level*. This skill provides that decision layer.

### The eight variables (six retinal + two planar)

Bertin counts eight variables a designer can use:

**The two planar dimensions:**
1. **X (horizontal position)**
2. **Y (vertical position)**

**The six retinal variables (sometimes called "elevated" because they're added "above" the plane):**
3. **SIZE** â€” area, length, or volume of a mark
4. **VALUE** â€” lightness/darkness, from white through grays to black (sometimes called "tone")
5. **TEXTURE** â€” fineness vs. coarseness of a repeating fill pattern
6. **COLOR / HUE** â€” the chromatic axis (red, blue, green) at equal value
7. **ORIENTATION** â€” angle of a mark (especially a line or asymmetric shape)
8. **SHAPE** â€” the form itself (circle, square, triangle, custom symbol)

### The four perceptual properties

Each variable can be evaluated on four perceptual properties. Bertin's central insight: **no variable has all four equally.**

- **Selectivity (â‰ ).** Can the eye instantly isolate all elements of one category? "Show me all the red dots." If yes, selective.
- **Associativity (â‰¡).** Can the eye instantly *ignore* the variation and group all elements as belonging to one whole? "Treat all marks as one group regardless of color." If yes, associative.
- **Ordered perception (O).** Does the eye perceive an unambiguous, universal order without consulting a legend? "Light-to-dark" reads as an order; "red-to-blue" doesn't (it requires a learned legend).
- **Quantitative perception (Q).** Does the eye perceive numerical ratios â€” "twice as much," "three times as big"? A bar twice as tall is perceived as twice the value; a hue twice as red is not perceived as anything at all.

### The table of properties (Bertin's famous table, p. 97)

Approximate property matrix (Bertin's own table in Ch II.C):

| Variable | Selective â‰  | Associative â‰¡ | Ordered O | Quantitative Q |
|---|:---:|:---:|:---:|:---:|
| X, Y (planar) | âœ“ | âœ“ | âœ“ | âœ“ |
| SIZE | âœ“ | (dominates) | âœ“ | âœ“ |
| VALUE | âœ“ | (dominates) | âœ“ | â€“ |
| TEXTURE | âœ“ | âœ“ | âœ“ | â€“ |
| COLOR (hue) | âœ“ | âœ“ | â€“ | â€“ |
| ORIENTATION | âœ“ (point/line) | âœ“ | â€“ | â€“ |
| SHAPE | âœ“ (limited) | âœ“ | â€“ | â€“ |

Key reads:
- **Only the plane and size are fully quantitative.** Bar height (size), x-position, y-position can carry ratio data honestly. Nothing else can.
- **Value is ordered but not quantitative.** Use value for ranked / ordinal data, not for numerical ratios.
- **Texture is ordered but not quantitative.** Same as value.
- **Color (hue) is neither ordered nor quantitative.** Use color for categorical data, never for order or ratio (unless the color encodes via value gradation â€” i.e., a sequential lightness ramp through one hue).
- **Shape and orientation are selective but not ordered.** Use them for categorical encoding only.

### The hierarchy of variables

Bertin orders the variables by perceptual richness:

```
PLANE > SIZE > VALUE > TEXTURE > COLOR > ORIENTATION > SHAPE
```

The plane carries the most information (it's selective, associative, ordered, AND quantitative). Shape carries the least (only selective, and only at small cardinality). When you must encode an important variable, prefer position; reserve color/shape for ancillary categorical variables.

### Dissociative dominance

**SIZE and VALUE are "dissociative" â€” they visually dominate any other variable combined with them.** A small dot's color is hard to see; large dark areas swamp adjacent fine textures. When you stack encodings, size or value will steal perceptual weight from the others. Don't fight this â€” use it intentionally for hierarchy, or avoid co-encoding with channels that need to remain visible.

### Length (how many distinguishable steps)

Each variable has a maximum number of distinguishable steps:

- **Size (points):** ~20 quantitative steps; ~4â€“5 selective steps
- **Value:** ~7â€“10 ordered steps (limited by contrast against background)
- **Texture (areas):** 3â€“4 selective; many ordered
- **Color (hue):** 7â€“10 categorical steps (more become hard to distinguish)
- **Orientation:** 4 distinct orientations on points/lines (0Â°, 45Â°, 90Â°, 135Â°)
- **Shape:** ~5 reliable categorical shapes (point, dash, cross, circle, square) at normal size; only 3 at extreme reduction

Trying to use more steps than the variable supports â†’ readers can't distinguish them â†’ silent communication failure.

### Implantation (point / line / area)

A variable's behavior changes depending on whether it's applied to a point, a line, or an area:

- **Texture on a tiny point:** invisible â€” texture needs area.
- **Color on a thin line:** nearly invisible â€” color needs area or substantial line weight.
- **Orientation on an area:** generally meaningless â€” orientation needs line or asymmetric point.
- **Size on a line:** length, not area â€” different perceptual properties.

Always check: does this variable work at the size/implantation I'm using it at?

## How to apply (step-by-step)

1. **List the data components.** What variables are you encoding? For each: is it nominal (categorical), ordinal (ranked), or interval/ratio (quantitative)? (If unsure, route to `bertin-levels-of-organization` first.)

2. **For each component, identify the perceptual requirement.** Quantitative data needs quantitative perception. Ordered data needs ordered perception. Categorical data needs selectivity.

3. **Pick a variable that meets the requirement.** Use the property table. For quantitative data: position or size only. For ordered: position, size, value, or texture. For categorical: any selective variable.

4. **Pass through the four-property check.**
   - **Selectivity:** Will readers be able to pick out one category?
   - **Associativity:** Can readers ignore the encoding and see the whole group when needed?
   - **Order:** If the data is ordered, does the variable preserve the order without a legend?
   - **Quantitation:** If the data is ratio, does the variable convey magnitude proportionally?

   Any "no" â†’ the encoding lies silently. Re-pick.

5. **Check the dissociative interaction.** Are you stacking size or value with another variable that needs to remain visible? If so, expect the secondary variable's perceptual weight to drop. Adjust mark sizes / contrasts.

6. **Check the length.** How many distinct categories does the data have? Does the chosen variable support that many distinguishable steps? If the data has 15 categories and you're using shape (5 max), the encoding will fail silently.

7. **Check the implantation.** At the size you'll render the marks, does the variable still function? Tiny points kill texture and color; thin lines kill orientation; etc.

8. **Produce the encoding spec.** One line per data variable: "Variable X (ordinal, 5 levels) â†’ encoded as VALUE (lightness ramp from #f7f7f7 to #252525). Selective âœ“, ordered âœ“, quantitative N/A (data is ordinal). Length supported: âœ“ (5 â‰¤ 7). Implantation: filled area âœ“."

9. **Sanity-check by reading aloud.** State each encoding in plain English: "Color encodes region. Size encodes population. Position-x encodes year." Then re-read the data types and ask: does each encoding *honestly* convey what its variable is? If a reader saw the chart cold, would they extract the right relationships?

## Common failure modes

- **Using hue for quantitative data.** A rainbow-colored heatmap (red-to-blue) implies order to people who learned the convention, but Bertin's property table flatly fails: hue is not ordered. Switch to a value ramp (single-hue lightness gradation) for ordinal/quantitative data. The "rainbow is bad" rule that ScalpedaMcKinsey-style design guides cite is just Bertin's property table being violated.

- **Using shape for ordered data.** "Diamond is bigger than circle is bigger than triangle" â€” except nobody perceives that order. Shape is categorical only. If the data is ordered, encode order via position, size, or value.

- **Stacking too many retinal variables.** A scatter plot using x, y, size, color, AND shape encodes 5 variables. The reader is overloaded â€” most ggplot defaults will draw all 5, but human perception caps around 3 simultaneously legible encodings on a single mark. Drop to the most important 3.

- **Ignoring dissociative dominance.** Color-coding tiny dots: the size dominates and color is invisible. Color-coding behind large filled areas: the area dominates and any layered encoding gets lost. Either reorder (put the dominant channel last in importance) or rescale.

- **Overflowing length.** Color-coding 25 categories with 25 distinct hues. The reader can hold ~7â€“10 distinct hues; beyond that, the encoding fails silently â€” readers can't tell categories apart. Either reduce categories (group) or switch to a strategy where each category is interactively highlighted on hover.

- **Ignoring implantation.** Using texture in a chart where the data marks are tiny dots. Texture needs area to be perceivable. Either enlarge the marks, switch to a variable that works at small implantation (color, value), or restructure the chart.

- **Treating the framework as universal across reader populations.** Bertin assumes a normally-sighted adult reader. Accessibility considerations (color blindness, low vision) modify the framework: don't rely on hue alone for selectivity if some readers can't distinguish red and green; double-encode with value or shape.

- **Confusing "I tested it and it looked fine" with "it works."** A chart looks fine to the designer who knows the legend by heart. Bertin's properties are about *cold* perception â€” what an unfamiliar reader extracts without reading the legend. Test with someone who hasn't seen the chart.

- **Mistaking modern tooling defaults for theory.** ggplot's `aes(color=...)` mapping accepts any data type because the library is flexible â€” not because the encoding is sound. The library doesn't enforce Bertin; the designer must.

## References

- Jacques Bertin, *Semiology of Graphics: Diagrams, Networks, Maps* (SÃ©miologie graphique, 1967; English translation by William J. Berg, 1983; Esri Press edition 2011), chapter II.C â€” "The Retinal Variables," book pages 60â€“97. The "Table of Properties of the Retinal Variables" on page 97 is the canonical reference; consult it directly when designing encodings.

- Downstream skills that *use* Bertin's framework without naming it:
  - `tufte-data-ink-ratio` â€” what counts as "data-ink" depends on which variable is doing the encoding
  - `tufte-chartjunk` â€” chartjunk often violates dissociative-dominance rules (3D over color, etc.)
  - `tufte-graphical-integrity-principles` â€” Principle 5 (information-carrying dimensions â‰¤ data dimensions) is Bertin's length/perceptual-capacity rule restated

- Sibling Bertin skills (same family):
  - `bertin-levels-of-organization` â€” Q/O/Qn taxonomy that this skill's "match variable to data type" decision depends on
  - `bertin-invariant-components` â€” the prior analysis step (what are you encoding?)
  - `bertin-image-vs-figuration` â€” the cognitive/perceptual layer that uses these variables
  - `bertin-legibility-rules` â€” quantitative thresholds for when each variable remains perceivable
  - `bertin-reorderable-matrix` â€” applied technique that leans heavily on value/saturation

- Modern descendants worth knowing: Cleveland & McGill (1984) on graphical perception; Wilkinson's *Grammar of Graphics* (1999); Munzner's *Visualization Analysis & Design* (2014); Ware's *Information Visualization* (2012). All build on Bertin.
