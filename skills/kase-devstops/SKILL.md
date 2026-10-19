---
name: kase-devstops
description: Place volatility stops using Kase's DevStop method â€” TrueRange Double (two-bar range) as the volatility unit, stop distances at 1, 2.2 and 3.6 standard deviations above mean TRD (the fractional levels correct for the right skew in range distributions), giving stop amounts calculable in advance so position size can be solved from a risk budget, plus the square-root-of-time rule for trading bigger size on a shorter bar. Use when asked "where do I put my stop," "how wide should an ATR stop be," "why do I keep getting stopped out on noise," "how do I size a position against a stop," "2 ATR or 3 ATR," "how do I trade more contracts without more risk," or when reviewing any volatility-based stop. From Cynthia A. Kase in Paul Ciana (ed.), New Frontiers in Technical Analysis, Chapter 4.
---

# Kase DevStops

## What this decides

How far away a protective stop belongs, expressed so the dollar risk is known
before the trade, which in turn determines position size.

## The problem with a plain ATR stop

Average TrueRange gives you the mean bar range and nothing else. Two markets can
share an identical ATR while behaving completely differently:

- one moves in very regular bar-to-bar increments,
- the other is erratic, with the same average but far more spread.

In the regular market, a stop does not need to be wide to survive noise. In the
erratic market, **under identical ATR conditions**, the stop may need to be much
wider. A mean alone cannot express that. The statistic that does is **standard
deviation**.

The green-bean analogy in the source makes it concrete: two growers can have the
same average bean length while one varies by two inches and the other by
0.20 inches. Same mean, entirely different tolerance requirement.

## Build 1: standard deviations over the mean, not multiples of the mean

DevStops are set at 1, 2, and 3 standard deviations over the mean range. The stop
then adjusts to both the average **and** the variability of ranges, rather than
scaling only with the average.

## Build 2: use the TrueRange Double, not a single bar

A one-bar reversal is usually not significant enough to justify exiting. So the
unit of measurement is the **TrueRange Double (TRD)** â€” the range across two
bars, not one. The stop is therefore built to survive a normal single-bar poke
and to respond to genuine two-bar reversals.

## Build 3: correct for skew (this is the distinctive part)

A bar's range cannot be negative. Range distributions are bounded at zero on the
left and can spike arbitrarily far to the right, so they are **right-skewed**.
Back to the beans: the grower whose largest beans run about 5.2 inches will still
occasionally produce a freak 8-inch bean.

Measured on real futures data (ten years of daily TRD), the observed skew is:

| Nominal level | Observed skew | Skew-corrected multiple used |
|---|---|---|
| 1 std dev | little to none | **1.0** |
| 2 std dev | about 10% | **2.2** |
| 3 std dev | about 20% | **3.6** |

So Dev1, Dev2, Dev3 sit at **1, 2.2 and 3.6 standard deviations over the average
TRD**. Those odd fractions are not fudge factors; they are the skew correction.

Roughly, the levels correspond to the 85th, 95th, and 99th percentiles of the
TRD distribution.

**The general lesson beyond this indicator:** any volatility band derived from
standard deviations of a range or volatility series and applied symmetrically is
understating the upside tail. Ranges are not normally distributed.

## Why calculable-in-advance matters more than the placement

Because the levels come from defined statistics rather than a chart-reading
judgment, three things become possible before entry:

1. **Risk per unit is known ahead of time**, so volume can be matched to risk
   appetite instead of discovered afterward.
2. **The probability of being stopped out can be estimated ahead of time**, since
   the levels are percentiles of an empirical distribution.
3. The likelihood of hitting subsequent stop levels once the first is hit is
   itself measurable, which is what makes staged stops rational rather than
   arbitrary.

The reversal amounts (the dollar distance to each Dev level) are the number to
size from.

## Sizing worked through

The source's example: on the system's exit day, Dev3 implied roughly 6 cents of
risk, about $3,000 per contract.

- Risk budget $300,000 per trade, divided by $3,000 per contract, gives
  **100 contracts**.

Now the trader wants 200 contracts on the same budget. The lever is the bar
length, because **risk is proportional to the square root of time**:

- Doubling volume by a factor of 2 requires cutting the time unit by a factor of
  4 (since 2 squared is 4).
- A daily chart becomes a **quarter-day chart, about 83 minutes**. In practice
  set up a 75 or 80 minute bar and re-verify the risk at that bar length.

That square-root relation is the reusable piece: **to trade k times the size at
the same dollar risk, shorten the bar to 1/k-squared of its length**, then
recompute rather than assume.

## Application checklist

```
[ ] Volatility unit = TrueRange DOUBLE, not single-bar range
[ ] Levels at 1 / 2.2 / 3.6 std dev over mean TRD (skew-corrected)
[ ] Stop distance converted to dollars per unit BEFORE entry
[ ] Position size = risk budget / dollar distance to the chosen Dev level
[ ] Chosen Dev level matches intent:
      Dev1 tight, expect frequent stop-outs (~85th pct)
      Dev2 normal (~95th pct)
      Dev3 let profits run, maximum normal risk (~99th pct)
[ ] Need more size at the same risk? shorten the bar by 1/k^2 and RECHECK
[ ] Never apply a symmetric std-dev band to a range series without skew correction
```

## Related

- [[katz-exit-strategy-taxonomy]] for where a volatility stop sits among the
  other exit types and how tight to run it.
- [[erlanger-seasonal-validation]] and [[rrg-relative-rotation]] for the entry
  side of the same book.
