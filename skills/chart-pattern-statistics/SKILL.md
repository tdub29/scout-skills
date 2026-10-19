---
name: chart-pattern-statistics
description: >
  Weight chart patterns by their MEASURED reliability, not their names. Distilled from Thomas
  Bulkowski's Encyclopedia of Chart Patterns (2nd ed., 2005), which measured 38,500+ real
  pattern occurrences and reports, per pattern, the break-even failure rate, average rise or
  decline, throwback/pullback rate, change after trend ends, performance rank, and the
  measure-rule hit rate. Use when a chart pattern has been identified and you must decide how
  much to trust it, size it, or set a price target. Triggers: chart pattern, pattern statistics,
  break-even failure rate, throwback, pullback, performance rank, measure rule, head and
  shoulders, double top, triangle, flag, pattern reliability, Bulkowski, price target,
  how reliable is this pattern, does this pattern work, pattern failure rate.
---

# Chart Pattern Statistics (Bulkowski reliability layer)

## What this skill is for

The `technical-analysis` skill covers how to IDENTIFY patterns (the geometry of a head and
shoulders, a double top, a triangle). This skill is the layer above it: which identified
patterns actually WORK, how often they fail, and how far price typically travels. Do the
identification with `technical-analysis`, then come here to grade the setup. Do not re-teach
identification here.

The source is Thomas Bulkowski's Encyclopedia of Chart Patterns, 2nd edition (2005). His
contribution is empirical, not descriptive: he catalogued over 38,500 real occurrences and
reported hard numbers for each pattern. A pattern name alone ("it's a head and shoulders")
carries no edge. The edge is in the measured statistics attached to that name and breakout
direction. Two patterns with the same shape but opposite breakout directions have completely
different numbers, so always pair a pattern with its breakout direction before quoting a stat.

## The core metrics Bulkowski defines

Every metric is measured from the breakout price to the ultimate high or ultimate low.

- **Breakout**: price closing outside the pattern boundary (a trend line, or the highest
  high / lowest low, depending on the pattern). Everything is measured from here.
- **Ultimate high / ultimate low**: the extreme price reached before a reversal of 20% or
  more. This is the endpoint used for every performance number, so the stats already assume
  you exit near the true turn, not the first wiggle.
- **Break-even failure rate**: the percentage of patterns that fail to move more than 5% in
  the breakout direction. The 5% threshold stands in for round-trip trading cost. This is the
  single most important reliability number. A 4% break-even failure rate means only 4 in 100
  of these patterns died before covering costs. Anything in the 20%+ range is a coin flip.
- **Average rise or decline (ARD)**: the mean move from breakout to ultimate high (up
  breakouts) or ultimate low (down breakouts), across all occurrences. Reported as a positive
  percent for rises and a negative percent for declines.
- **Change after trend ends**: how far price moves in the opposite direction after the
  ultimate high or low. A large value flags a sharp reversal, which is why Bulkowski treats a
  bigger change-after-trend as a positive contribution to rank (it marks a clean turning point
  worth exiting into).
- **Throwback (up breakouts) / pullback (down breakouts)**: price returning to or near the
  breakout price within 30 days, then resuming. Bulkowski's data repeatedly shows that
  patterns WITH a throwback or pullback UNDERPERFORM those without. A high throwback/pullback
  rate is a caution flag, and a throwback in progress is often a chance to enter on the retrace
  rather than the breakout.
- **Performance rank**: Bulkowski's composite. He ranks each pattern on average rise/decline,
  break-even failure rate, and change after trend ends, sums the three ranks, and re-sorts.
  Rank 1 is best; the chart-pattern universe is ranked 1 to 21 within each breakout direction.
  Use this as the fast "is this a top-tier pattern" lookup.
- **Percentage meeting price target**: how often price reached the measure-rule target (below).
- **Busted pattern**: a pattern that moves less than 5% in the breakout direction and then
  reverses hard the other way. Busted patterns can themselves be tradable in the new direction.

## The measure rule (price targets)

Bulkowski's default measure rule: take the pattern height, then add it to the breakout price
for an upward breakout or subtract it for a downward breakout. That gives the predicted target.
The height is the highest high minus the lowest low inside the pattern. Some patterns use a
fraction of the height (for example, half-height variants for very tall patterns) because the
full-height target is hit too rarely; the chapter's "percentage meeting price target" tells you
which. Treat the target as a probability, not a promise: even strong patterns hit the full
measured target only roughly 40% to 65% of the time (head-and-shoulders tops: about 55%). If the
hit rate for a pattern is low, scale the target down or use the average rise/decline as the more
honest expectation.

## How an agent should weight a pattern

Given an identified pattern and its breakout direction, grade it in this order:

1. **Break-even failure rate first.** Under ~5% is high conviction, 5% to 12% is workable,
   above ~15% treat as low conviction and demand extra confirmation. This is the go/no-go gate.
2. **Performance rank** as a sanity check. Rank 1 to 5 in its direction is a premier pattern;
   ranks in the high teens are weak even if the shape is textbook.
3. **Average rise/decline** sets the reward side. Pair it with the failure rate for a crude
   expectancy: a low failure rate plus a large average move is the combination to want.
4. **Throwback/pullback rate** adjusts entry and expectation. High rate means expect a retrace,
   plan to enter on it, and shade the expected move DOWN because retraced patterns underperform.
5. **Measure rule** for the target, discounted by the pattern's percentage-meeting-price-target.
6. **Market regime.** Every number has a bull-market and a bear-market version; declines run
   larger and fail less in bear markets. Bulkowski's bear-market window is a specific 2.5-year
   period (Mar 2000 to Oct 2002), so bear stats rest on fewer samples. Quote the version that
   matches the current regime, and note when you are extrapolating.

Do not let a pretty shape override the numbers. A textbook broadening top with an upward
breakout still ranks near the bottom (19 of 21) and is a weak trade; a plain high-and-tight flag
is the single best-performing pattern in the book.

## Worked example

Suppose `technical-analysis` identifies a head-and-shoulders top with a completed downward
breakout below the neckline, in a bull market. Grade it:

1. Break-even failure rate is 4%. That clears the go/no-go gate with high conviction: only about
   1 in 25 of these fail to fall at least 5%.
2. Performance rank is 1 of 21 for down breakouts. This is the best-ranked bearish pattern, so
   the shape and the odds agree.
3. Average decline is 22%, so the reward side is large relative to the ~5% cost hurdle.
4. Pullback rate is 50%. Expect a coin-flip chance of price returning to the neckline within
   30 days. Plan to short into that pullback, and shade the expected decline down because
   patterns that pull back underperform.
5. Measure-rule target is the breakout price minus the pattern height. Price hits the full
   target about 55% of the time, so treat the full target as the optimistic case and the 22%
   average decline as the base case.

Contrast: an ascending scallop with an upward breakout is a clean, appealing curve, but its
break-even failure rate is 10% and its rank is 16 of 21. Same effort to spot, far worse odds.
The numbers, not the aesthetics, decide the size.

## Reference table: highest-reliability patterns (bull market, as Bulkowski reports)

Columns: average rise/decline, break-even failure rate, change after trend ends,
throwback-or-pullback rate, overall performance rank (of 21 in that breakout direction).

Upward breakouts (bullish, for entries):

| Pattern (up breakout) | Avg rise | BE fail | Chg after | Throwback | Rank |
|---|---|---|---|---|---|
| Flags, High and Tight | 69% | 0% | -36% | 54% | 1 |
| Pipe Bottoms | 45% | 5% | -33% | 44% | 2 |
| Scallops, Ascending and Inverted | 43% | 4% | -32% | 61% | 3 |
| Three Rising Valleys | 41% | 5% | -33% | 60% | 4 |
| Rounding Bottoms | 43% | 5% | -31% | 40% | 5 |
| Triangles, Descending (up breakout) | 47% | 7% | -30% | 37% | 5 |
| Double Bottoms, Eve & Eve | 40% | 4% | -31% | 55% | 6 |
| Triple Bottoms | 37% | 4% | -33% | 64% | 7 |
| Head-and-Shoulders Bottoms | 38% | 3% | -31% | 45% | 7 |

Downward breakouts (bearish, for exits or shorts):

| Pattern (down breakout) | Avg decline | BE fail | Chg after | Pullback | Rank |
|---|---|---|---|---|---|
| Head-and-Shoulders Tops | -22% | 4% | 51% | 50% | 1 |
| Diamond Bottoms (down breakout) | -21% | 10% | 59% | 71% | 1 |
| Double Tops, Eve & Eve | -18% | 11% | 63% | 59% | 2 |
| Head-and-Shoulders Tops, Complex | -23% | 4% | 48% | 67% | 3 |
| Bump-and-Run Reversal Tops | -19% | 5% | 53% | 62% | 3 |
| Horn Tops | -21% | 7% | 51% | 33% | 4 |
| Pipe Tops | -20% | 11% | 56% | 41% | 4 |

Notable weak patterns to distrust despite clean geometry: Scallops Ascending (up, rank 16; break-even
failure 10%), Broadening Tops (up, rank 19), Diamond Tops (up, rank 21). Good shape, poor odds.

## Caveats

These are comparative benchmarks from 1991 to 2004 daily US stock data, not guarantees for any
single trade. Numbers hold in aggregate; your one setup can still fail. The bear-market figures
rest on a narrow 2.5-year window and fewer samples than the bull figures. Flags and pennants are
measured to the trend high/low, not the ultimate high/low, so their moves are not directly
comparable to the reversal patterns above. Always tie a stat to a specific pattern plus breakout
direction plus market regime before you quote it. Do the pattern identification with the
`technical-analysis` skill; use this skill only to grade and target what that identifies.
