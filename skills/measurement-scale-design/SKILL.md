---
name: measurement-scale-design
description: "Turn raw signals into a sound 0-10 score or index."
license: MIT
metadata:
  version: 1.0.0
  origin: Distilled from a real DR-monitoring scale rebuild (media-attention 0-10 + cross-hazard severity 1-5).
---

# Measurement Scale Design

Turning raw signals into a score people trust. The score is a **measurement instrument**: it has a
construct (what it measures), validity (does it measure that), and reliability (consistently). Most
bad scores fail not on math but on **construct** â€” they measure the wrong thing convincingly.

Work the gates in order. Do not skip to picking thresholds.

## Gate 1 â€” Define the construct in one sentence, and say what it is NOT

Write: *"This score measures ____, which is distinct from ____."* If you can't name what it is **not**,
you don't have a construct yet, you have a vibe. The "is not" is where scores die.

- A **severity** score measures *how hard each affected unit was hit* (depth). It is NOT *how many*
  were hit (that is impact/exposure â€” a separate axis). Keep them separate columns; never let one
  silently stand in for the other.
- An **attention/salience** score measures public interest. It is NOT importance, severity, or need.
- A **risk** score is *probability x consequence*. It is NOT either factor alone.

If two "different" scores will always move together on your data, you have one axis with two labels.
Orthogonality is a feature: a Cat-5 hurricane over empty ocean is high-severity / low-impact; a broad
shallow flood is high-impact / low-severity. A good design lets that show.

## Gate 2 â€” Choose the scale TYPE from the data's nature, not aesthetics

| Underlying quantity | Right scale | Why |
|---|---|---|
| Continuous, orders-of-magnitude range (counts, $, views, magnitudes) | **Continuous score** (e.g. 0-10) on a transform | Tiers throw away within-tier distinction; the thing varies smoothly |
| Genuinely categorical / from a hard ordinal scale (Saffir-Simpson 1-5, MMI, Likert) | **Ordinal band** matching the source scale | A finer number would be **false precision** â€” there is no real "7.3" of hurricane |
| A handful of qualitatively different states | **Named states**, not numbers | Numbers imply distance that isn't there |

**Tiering is usually the lazy answer.** Three tiers (low/med/high) collapse a 100x-range quantity into
3 buckets, so a national catastrophe and a regional event read identically. If the complaint is "not
enough distinction," the fix is almost always **go continuous** (a log-scaled 0-10), keeping a color
band only as a *visual* cue layered on top of the number. Conversely, do NOT invent a 0-100 for
something with 5 real states â€” that is false precision in the other direction.

## Gate 3 â€” Transform heavy-tailed inputs before scaling

Counts, dollars, pageviews, populations, magnitudes are typically **log-normal / power-law**. On a raw
scale, the top 1% swamps everything and the bottom 90% is indistinguishable mush.

- **Log-transform** (`log10` or `ln`) is the default variance-stabilizer for positive heavy-tailed
  data. Map the log linearly to your score range with **interpretable anchors** (e.g. 100/day -> 1,
  ~300k/day -> 10). Box-Cox / sqrt are alternatives; log is usually enough and explains itself.
- Decide **fixed anchors vs empirical quantiles**:
  - **Fixed anchors** (constants): reproducible across time and re-runs; a "9" means the same thing
    next quarter. Best for monitoring/longitudinal scores. (You pick the anchors from one calibration
    snapshot, then freeze them.)
  - **Empirical quantile / percentile rank**: every score is relative to the current set; great for
    "rank within today's batch," but it **drifts** â€” the same event scores differently as the set
    changes, and a quiet week inflates everyone. Never use percentile-within-set as a stable label.
- **Zero-inflation is normal and honest.** Many items legitimately have *no signal* (no article, no
  award, no event). Send them to a clean **0 / "none"**, do not impute. Report the zero share; a score
  that is 54% zeros is fine if 54% genuinely had no signal. Diagnose the non-zero part separately.

## Gate 4 â€” Construct validity: the confounds that fake a good score

The score can be perfectly distributed and still measure the wrong thing. Hunt these:

- **Count x depth confound (the big one).** A **total** (total $, total articles, total people) is
  `how_many x how_hard` â€” it conflates two axes. To measure **depth/intensity per unit**, use an
  **average or rate** (avg award *per household*, $ per capita), not the total. Example: FEMA total
  IHP dollars ranks the biggest disasters first â€” but that is mostly breadth; the per-household
  average reveals that a broad event paid ~$3k/home (minor) while a concentrated one paid ~$20k/home
  (devastating). Total would have called the shallow event "severe."
- **Proxy that anti-correlates with the construct.** Always ask "what else drives this number?"
  Wildfire **acreage** looks like severity but big fires burn *remote* land â€” acreage correlates with
  *remoteness*, i.e. it **anti-correlates with destruction**. A 400k-acre wilderness fire reaching 13
  people is not more severe than a 57k-acre fire that razes a city. Pick a proxy that tracks the
  construct (here: people/structures the footprint reached), and **retire** the misleading one.
- **Denominator dilution / registration inflation.** Averages get diluted when the denominator
  balloons with low-harm members (800k hurricane registrants, most with minor claims, pull the mean
  down). When a hazard has a *hard intensity scale* (Saffir-Simpson, magnitude), prefer it over a
  diluted average for that hazard.
- **Small-N noise.** A 19-item average is volatile (one outlier moves it). Decide deliberately: a
  small *total-loss* group is legitimately high-depth/low-count (keep it â€” that's orthogonality), but
  guard against a single record masquerading as a trend. Winsorize extremes; consider a minimum-N
  before trusting a rate; never let small-N *and* unverified drive a headline.

## Gate 5 â€” Cross-domain equivalence (one scale over apples and oranges)

When one scale spans incomparable domains (hazard types, product categories, business units), you are
making an **equivalence claim**: "a 4 here means the same as a 4 there." Defend it:

- Anchor each domain to its **own native hard scale** where one exists (hurricanes -> Saffir-Simpson;
  quakes -> magnitude/MMI/PAGER), then map each onto the common band. State the mapping.
- Where a domain has **no** hard scale, use a clearly-flagged **soft proxy** and label it as such in
  the output ("soft proxy, not a hazard scale"). Don't pretend it's as hard as the others.
- Accept that cross-domain numbers are **rank-comparable, not unit-comparable** â€” say so. "A severity-4
  flood and a severity-4 quake are similar in rank, not in physical units."
- Hand-curated values for a few marquee items (with cited basis) beat a formula that produces nonsense
  for them â€” but cap how much is hand-set and flag it as provisional.

## Gate 6 â€” Validate before shipping (adversarial, independent)

A scale is an analysis; QA it like one. Never self-review only.

1. **Distribution diagnostics.** Histogram / deciles of the score and of each input. Is it spread or
   piled at an end? Is the non-zero part log-normal as assumed (Q-Q plot)? Did binning saturate (every
   item in one band)?
2. **Magnitude / smell test.** Do the top and bottom items match reality? Is anything implausible vs a
   known reference?
3. **Known-pair tests.** Pick pairs you have strong priors on ("X must outrank Y", "A and B should be
   clearly distinct") and assert them.
4. **Construct re-check.** For a sample, is the score moving with the construct or with a confound?
5. **Independent adversarial review.** Hand the scored table + the construct definition to a
   fresh-context reviewer (or a panel by perspective: statistician lens, domain lens) and have them
   try to *break* it. Verify each flag adversarially before acting. Fix, then re-validate.

Use sibling skills: `quantitative-research` / `statistical-analysis` for the diagnostics and transform
choice; `validate-data` for the pre-delivery QA pass; `code-review` for fresh-context review of the
scoring code; `data-storytelling` / `data-viz` to communicate the scale and its caveats.

## Anti-patterns (match-and-refuse)

- Three tiers on a 100x-range quantity ("not enough distinction" is the tell) -> go continuous.
- A 0-100 (or 1-10) on something with ~5 real states -> false precision; use the ordinal.
- **Total** anything as a severity/intensity/depth measure -> it's count x depth; use the average/rate.
- A proxy you never stress-tested for what *else* drives it (acreage-as-severity is the canonical trap).
- Percentile-within-today's-batch used as a stable, reported label -> it drifts; use fixed anchors.
- Imputing a value for genuine no-signal items instead of a clean 0/none.
- One scale silently standing in for another axis (severity doing impact's job).
- Shipping without an independent adversarial pass on the distribution and the extremes.

## One-paragraph recipe

Name the construct and what it is not. Pick scale *type* from the data (continuous for wide-range
quantities, ordinal for hard categorical scales). Transform heavy-tailed inputs (log) and map to the
range with fixed interpretable anchors; send genuine no-signal to 0. Measure **depth with averages/
rates, not totals**; choose proxies that track the construct, not its confounds; flag soft proxies and
keep axes separate. For cross-domain scales, anchor each domain to its native scale and call the result
rank-comparable. Then run distribution diagnostics, known-pair tests, and an independent adversarial
review before it ships.
