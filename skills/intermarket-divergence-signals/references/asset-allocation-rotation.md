# Intermarket Relative-Strength Asset-Allocation Rotation (Ch.16)

Use this when the ask is portfolio-level rotation across asset classes/ETFs
rather than a single-pair divergence signal.

## Core idea

Static buy-and-hold asset allocation (fixed weights across stocks, bonds,
commodities, forex) relies on historical returns and historical correlations
that are unlikely to repeat â€” correlations between asset classes are
demonstrably unstable over time (e.g. stock/bond correlation has flipped sign
across multi-year windows). A dynamic approach instead measures which asset
classes are *currently* strongest and rotates capital toward them.

## Method (as documented in the source)

1. **Benchmark**: relative strength of each candidate asset/ETF is measured
   against the S&P 500 as the common benchmark.
2. **Universe**: build a broad candidate universe â€” commodity index futures,
   international equity indices, interest-rate futures, currencies, and
   individual commodity futures (or, for an equity-only implementation,
   commodity/country/sector/bond/currency ETFs). Breadth matters: the point is
   to always have a genuinely uncorrelated strong performer to rotate into.
3. **Rank** candidates by relative strength (price of asset Ã· benchmark,
   smoothed) and rotate capital toward the strongest.
4. **Compare against a static baseline**: hold a fixed diversified weight
   (example baseline used in the source: ~40% broad equity, 5% emerging
   market, 5% European equity, 10% bonds, 30% commodities, 10% currency) and
   against 100% S&P 500 buy-and-hold, to confirm the dynamic method actually
   adds value over both a naive diversified portfolio and a naive single-asset
   benchmark.
5. **Static vs. dynamic rebalance**: the dynamic model's edge over the static
   one is precisely that it re-ranks and re-allocates as relative strength
   changes, rather than locking in a fixed weight set at inception.

## Known gap in this reference

The source chapter's full ranking formula (exact relative-strength lookback
window, the specific rank-cutoff for "strongest" â€” e.g. top-N by RS â€” and the
rebalance cadence/trigger rule) was not present in the available source
excerpt for this skill family. Before implementing this rotation approach
literally, either source the full Chapter 16 text for the exact
parameterization, or treat the above as a design pattern and choose your own
ranking lookback (e.g. 3-6 month relative strength, a common momentum-rotation
default) and rebalance cadence (e.g. monthly) empirically, validating with the
system-design method in `system-design-and-validation.md`.

## Practical notes

- This is a rotation/momentum strategy, not a mean-reversion divergence
  signal â€” it deliberately buys strength, the opposite intent of the
  divergence formulas in the main skill.
- Multi-account/regulatory friction is real: a full implementation spanning
  domestic stocks, futures, and forex may require a broker built for
  cross-asset trading (the source names Interactive Brokers, Saxo Bank,
  Internaxx as examples) â€” flag this to the user if the rotation universe
  spans asset classes with different account requirements.
