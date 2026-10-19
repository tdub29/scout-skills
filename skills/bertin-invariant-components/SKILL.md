---
name: bertin-invariant-components
description: Apply Jacques Bertin's Invariant + Components analytical framework from *Semiology of Graphics* (1967; ch. I.A, pp. 16â€“28) â€” every information system has one INVARIANT (the unchanging central notion that all data points share â€” "what's being measured, always the same") and N COMPONENTS (the dimensions that vary â€” "what changes"). At least two components are required for graphic representation. The invariant defines the legitimate scope of the data and belongs in the title/legend; the components map onto visual variables. Use whenever the user is about to design a chart and hasn't articulated what's *constant* across all data points, says "this chart is confusing â€” what's it actually showing," mixes data that might not share a measurement basis (old vs. new currency, before vs. after a definitional change, different exchanges, different methodologies), can't write a precise title for their chart, has a vague chart heading like "Sales Data" instead of "Q4 2023 US SaaS Revenue, Inflation-Adjusted to 2020 USD," or is auditing why a competitor's chart implies a story the underlying data doesn't support. Also trigger for "what's the title of this chart," "how do I describe what this chart shows," "I have data that might not be comparable," "components vs. invariant," "Bertin analysis," "data scope," "what's the unit of analysis," "are these measurements comparable," or "this chart's scope is fuzzy." Output is a clarification artifact: a precise one-sentence invariant statement + an enumerated list of components with their organizational levels + a scope-validation check (does every data point genuinely share this invariant?). Do NOT trigger for visualization choice once the analysis is done (route to `bertin-retinal-variables`, general data-viz). This skill owns the pre-visualization analysis step â€” "what am I actually showing, and is the scope honest?"
---

# Bertin: Invariant + Components

## When to use

Trigger when the question is "what is this chart actually about, and are all the data points genuinely comparable under that scope?" â€” the analytical hygiene that prevents subtle data-comparability mistakes. Concrete cues:

- The user can't write a precise chart title in one sentence (or the title is generic: "Sales Data," "Q4 Results")
- A dataset combines measurements from different time periods, currencies, exchanges, methodologies, or definitions
- The user is unsure if two data series belong on the same chart
- A chart's readers consistently misinterpret it and the user is debugging *what's being shown*
- The user is preparing a chart for a regulatory submission, board deck, or any context where scope ambiguity has consequences
- A chart shows "growth over time" but the underlying business definition changed mid-series (e.g., new product line added, acquired company merged in, definition of "revenue" updated)
- The user is auditing a stakeholder's chart for hidden scope issues
- "Should this be one chart or two?" â€” often a question of whether the data share an invariant

Don't trigger for: chart-type selection (general data-viz), aesthetic title formatting (copywriting / typography), or encoding choice once scope is clear (route to `bertin-retinal-variables`). This skill is the analytical preamble â€” what data is comparable to what, and how do we describe it precisely.

## The framework

### Core thesis

Information lives in *correspondences* between variables. To represent it graphically, you need at least two variables (the COMPONENTS) and a third anchor that fixes what those variables are measuring (the INVARIANT). The invariant is constant across every data point in the system â€” it's the answer to "what's being measured here, always the same way?" The components are the things that vary â€” the answer to "what changes from data point to data point?"

This sounds trivial but it is the most-frequently-skipped step in chart design. A revenue chart titled "Sales" doesn't say what's being measured. Are these gross or net? Booked or recognized? US dollars or local currency? Quarterly or trailing-twelve-month? Including or excluding the divested business unit? Every one of those decisions defines the invariant. If two data points in the series were measured under different invariants (e.g., one quarter pre-divestiture, one quarter post-) they don't belong on the same chart â€” or if they do, the chart needs to disclose it.

### What the invariant is

The invariant is a precise sentence (often one sentence, sometimes a short paragraph) that names:

1. **What is being measured.** Revenue. Closing stock price. Number of patients. Population density.
2. **Under what conditions.** Reported in fiscal-quarter financials. Closing-bell price on the NYSE. Patients admitted to general medicine. Population per square kilometer.
3. **In what units.** Millions of US dollars. New francs at face value. People. People/kmÂ².
4. **Adjusted how (if at all).** Inflation-adjusted to 2020 USD. Currency-adjusted at the year-end exchange rate. Seasonally adjusted. Raw.
5. **Across what scope.** US-based SaaS companies with >$1M ARR. Listed on the Paris Bourse. Diagnosed between 2010 and 2020. Excluding overseas territories.

Bertin's own example (stock prices, p. 16): the invariant is "the quotation in new francs, cash payment, closing price on the Paris exchange." That single sentence excludes data points measured in old francs, on forward contracts, opening prices, or other exchanges â€” and the chart's whole interpretation depends on that exclusion holding.

### What the components are

Components are the dimensions that vary. Each component has:

- **A name** (Time, Region, Product, etc.)
- **A range** (1990â€“2024; 5 regions; 12 product lines)
- **An organizational level** (Q / O / Qn â€” route to `bertin-levels-of-organization`)
- **A length** (how many distinct values)

A graphic represents *correspondences between components*. The simplest case: 2 components â€” Time vs. Revenue, X vs. Y on a line chart. Three components â€” Time, Revenue, Region â€” gets you a multi-series chart or a heatmap. More than three components and you start hitting Bertin's limit of what a single "image" can carry (route to `bertin-image-vs-figuration`).

**At least two components are always required.** A single-number display ("Total Revenue: $4.2M") is not a graphic in Bertin's sense â€” it has one component, no correspondence to display. That doesn't make it bad; it makes it a different artifact (a label, a KPI, a number).

### Why this matters: scope drift and silent comparability failures

The most expensive chart bugs are the ones where the invariant *seems* to hold but doesn't:

- A revenue chart spanning 2015â€“2025 where the company's definition of "revenue" was tightened in 2020 to exclude certain ancillary income. The pre-2020 and post-2020 values aren't comparable. The chart shows them on the same axis.
- A patient-volume chart pre- and post-EHR migration. The data sources changed; counts differ for non-clinical reasons.
- A stock-price chart that splices old-currency and new-currency quotes without adjustment.
- A revenue chart that adds an acquired company's history retroactively for some years but not others.

The chart looks coherent â€” same axes, same units â€” but the invariant *changed* mid-series. The visual story is false even though every individual data point is "correct." This is the failure mode the invariant catches.

### Where the invariant goes

The invariant lives in the **title and legend** of the chart, not in the visual encoding. It's the *unchanging context* against which the components are read. A good title states the invariant in one sentence; a vague title hides it. Bertin's rule: "Sales Data" is not a title; "Quarterly Recognized Revenue (GAAP), US-Reported, Inflation-Adjusted to 2020 USD, 2015â€“2024" is a title.

### Components â‰  data series

A common confusion: "I have two stocks to compare â€” that's two components, right?" No. The two stocks share an invariant (closing price on the same exchange, same conditions). They are two values of *one* component: "stock identity." The components are still Time and Price; stock identity is a third component that varies discretely.

This matters for encoding: a multi-series line chart has 3 components (Time-X, Value-Y, Series-color), not 2 + 2.

## How to apply (step-by-step)

1. **Write the invariant in one precise sentence.** "What's being measured, always the same way, across every data point?" Include: what / how / unit / adjustment / scope. If you can't fit it in two sentences, the invariant probably isn't actually invariant â€” find what's drifting.

2. **List every component.** For each: name, range, organizational level (Q/O/Qn), length. Confirm each one *varies* across the dataset (if it doesn't vary, it's part of the invariant, not a component).

3. **Validate the invariant against every data point.** For each row in the dataset, check: does this row share the invariant exactly as written? If any row has a different measurement basis, definitional scope, methodology, currency, adjustment policy â€” you have an invariant violation. Either:
   - (a) Narrow the chart's scope to data that genuinely shares the invariant (drop the non-conforming rows)
   - (b) Adjust the data to make it conform (e.g., inflation-adjust historical dollars)
   - (c) Disclose the discontinuity explicitly in the title or via annotation

4. **Count components and consider the chart's perceptual capacity.** â‰¤3 components fit comfortably in a single image. 4 components start requiring careful design (and possibly small multiples). 5+ components usually require either reducing scope or splitting into multiple charts. Route to `bertin-image-vs-figuration` for the cognitive-load decision.

5. **Write the chart title from the invariant.** The title should let a cold reader understand the chart's scope without reading the body copy. State the invariant in plain English; include the time range, units, and any non-obvious adjustments.

6. **Cross-check legend completeness.** Every component encoded visually should be labeled in the legend. The reader should be able to identify which visual channel encodes which component without trial and error.

7. **Sanity-check by reading aloud.** Speak the title + the legend. "This chart shows [invariant] across [component A] and [component B], with [component C] encoded as [retinal variable]." If anything in that sentence feels loose, the analysis isn't tight yet.

## Common failure modes

- **The "Sales Data" title.** A generic title hides the invariant. Readers fill in their own definition, and they're often wrong. Force yourself to write a precise one-sentence invariant; if it sounds overly long, that's because real invariants are specific.

- **Mid-series definitional drift.** Revenue definitions change. Patient counts switch data sources. Currencies redenominate. Acquisitions get added retroactively for some years but not others. The chart shows it all on one axis and looks coherent. The visual story is false. Always check: did the underlying definition change anywhere in this time range?

- **Mixing scopes that look comparable.** "Domestic vs. International revenue" on the same chart â€” fine, IF both are measured the same way (same currency, same recognition timing, same adjustments). If domestic is GAAP and international is local-GAAP, the comparison lies.

- **Treating the invariant as the chart's claim.** The invariant is what's *constant*, not what's *interesting*. The interesting story is in the components â€” how they vary against each other. Charts that try to make the invariant the headline ("we have lots of data!") miss the point.

- **Stuffing the invariant into the legend instead of the title.** The legend identifies components, not invariants. The invariant belongs in the title (or a subtitle). A vague title + a detailed legend is fragile â€” many viewing contexts strip the legend (thumbnail, screenshot, embedded preview).

- **Counting data series as components.** Two products, three regions, four years: the user counts "9 components" when there are really 3 (Product, Region, Year). Confusion here leads to overestimating chart complexity. A component is a *dimension that varies*, not a *value of that dimension*.

- **Ignoring single-component "graphics."** A bare KPI ("Revenue: $4.2M") has one component (Revenue) and no correspondence to display â€” it's not a graphic in Bertin's sense. That doesn't make it bad; just don't treat it as a chart that needs encoding analysis. It's a label.

- **Hiding adjustments.** "Revenue grew 50%" in nominal dollars during a high-inflation period â€” the chart's nominal scale isn't an honest invariant for a 10-year growth story. Either inflation-adjust and disclose, or run the chart in nominal but explicitly title it that way.

- **Confusing this skill with `tufte-graphical-integrity-principles`.** Both are about honest representation. The difference: integrity-principles audits the *finished chart* against truthfulness rules; invariant-components audits the *data scope and chart claim* before encoding. Run this skill first; run integrity second. They compose.

## References

- Jacques Bertin, *Semiology of Graphics* (1967; English 1983; Esri 2011 ed.), chapter I.A â€” "The Invariant and the Components," book pages 16â€“28. Includes the stock-price example that's the canonical illustration.

- Sibling Bertin skills:
  - `bertin-levels-of-organization` â€” once components are listed, classify each one's level (Q/O/Qn)
  - `bertin-retinal-variables` â€” encoding choice once the levels are known
  - `bertin-image-vs-figuration` â€” perceptual-capacity check when component count rises

- Related Tufte skills:
  - `tufte-graphical-integrity-principles` â€” Principle 6 (don't quote data out of context) is the invariant-honesty check in chart-audit form
  - `tufte-lie-factor` â€” orthogonal but worth running together for a publication-ready chart
