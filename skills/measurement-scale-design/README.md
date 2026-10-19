# measurement-scale-design

A reusable skill for designing, calibrating, and validating a measurement **scale / score / rating /
composite index** so it is statistically sound and measures what you claim.

See `SKILL.md` for the full guidance. The core is six gates, in order:

1. **Define the construct** in one sentence â€” and say what it is NOT (the orthogonal axis it must not
   absorb).
2. **Choose the scale type** from the data's nature: continuous (0-10) for wide-range quantities,
   ordinal (1-5) for hard categorical scales. Tiers are usually too coarse; false precision is the
   opposite error.
3. **Transform** heavy-tailed inputs (log), map to range with fixed interpretable anchors, send
   genuine no-signal to 0 (zero-inflation is honest).
4. **Construct validity** â€” hunt the confounds: count x depth (use averages, not totals), proxies that
   anti-correlate with the construct, denominator dilution, small-N noise.
5. **Cross-domain equivalence** â€” anchor each domain to its native scale; call the result
   rank-comparable, not unit-comparable; flag soft proxies.
6. **Validate** with distribution diagnostics, known-pair tests, and an independent adversarial review
   before shipping.

## Origin

Distilled from a real rebuild of two scales on a disaster-monitoring report:

- A **media-attention** score that was three coarse tiers (a national catastrophe and a regional storm
  both read "high") -> rebuilt as a log-scaled continuous **0-10** from peak Wikipedia pageviews.
- A cross-hazard **severity** scale that confused depth with extent (burned acreage ranked a remote
  megafire above a catastrophic urban fire; total FEMA dollars conflated severity with how-many) ->
  redefined as **per-person harm depth** (how hard each affected unit was hit), distinct from impact
  (how many), with hazard-native signals (Saffir-Simpson, PAGER/MMI, footprint-population, average aid
  award per household).

Pairs with: `quantitative-research`, `statistical-analysis`, `validate-data`, `data-storytelling`.
