---
name: erlanger-seasonal-validation
description: Test whether a security's seasonal pattern is real before trading it, using Erlanger's split-half Cycle-R method â€” build seasonal cycles from two exogenous halves of history, correlate them, and treat the correlation as the validity statistic; then optimize the look-back to maximize Cycle-R, track in-year conformity with a running current-year R, and trade only the fastest-moving long and short zones of the cycle. Use when asked "is this seasonal pattern real or noise," "does this stock have a tradeable seasonality," "how many years of history should a seasonal study use," "how do I know a seasonal is still working this year," "sell in May / Santa rally, is it real," or when someone presents an averaged-by-month chart as evidence. From Philip B. Erlanger in Paul Ciana (ed.), New Frontiers in Technical Analysis, Chapter 3.
---

# Erlanger Seasonal Validation

## What this decides

Whether a seasonal cycle is a real, tradeable tendency or an artifact of
averaging, and if real, which weeks of it are worth acting on.

The default assumption should be skepticism: **for many securities there are no
meaningful seasonal influences at all.** Averaging price by calendar date always
produces a wiggly line. The line is not evidence.

## The core test: Cycle-R (split-half correlation)

The method is a hold-out test disguised as a correlation.

1. Take the look-back window, say the most recent 15 complete years.
2. Build a seasonal cycle from the **first half** of that window.
3. Build a second seasonal cycle from the **second half**.
4. **Cycle-R is the correlation between those two cycles.**

The two cycles come from totally separate, exogenous portions of price history.
If they still agree, some genuine seasonal influence persists across the whole
data set. If they disagree, the pretty averaged cycle is a coincidence of
whichever years happened to be included.

Read it as any correlation: 1 is perfect, 0 is none, -1 is perfectly inverse. In
the worked example, Starbucks over the 15 years before 2010 scored **0.76**,
which is high enough to treat the cycle as valid. And that year's actual price
action did track it: the seasonal lows in late January and late August matched
real lows, and the cycle's weak late-June to late-August window was the stock's
weakest stretch of 2010.

The other structural feature worth noting: **the cycle is plotted entirely in
advance.** Built on January 1, it is fixed for the whole year, so it can be
verified honestly rather than fitted as the year goes.

## Optimizing the look-back

Cycle-R can be computed for any look-back from 15 years down to about 2 (2 is
unreliable, too short a span). Each look-back yields a slightly different cycle
with its own Cycle-R.

**Optimize by choosing the look-back that maximizes Cycle-R**, because that is
where the two exogenous halves agree most, which is the most valid cycle
available.

Worked example: American Express on a standard 15-year look-back scored 0.54 and
put the yearly high in late August with strength holding into year end. Optimized
to a 5-year look-back it scored **0.66** and put the high in late April/early
May with strength falling off at year end. The 2010 peak came in late April, and
December's rally faded even while the broad market made higher highs.

**But optimized is not automatically better.** A shorter window is a more local
statistic and less time-tested. That is a real tradeoff, not a free lunch. Use
both, and treat agreement between them as the strong signal: for American Express
both cycles put the seasonal low in March with the sharpest rise right after, and
that is where the year's largest advance occurred.

The reason a local window can beat a long one is that fundamentals change.
Taxation changes shift the seasonal profile of a financial company. Seasonality
is not a law of nature; it is a residue of fundamental forces applied at regular
intervals, and it expires when those forces change.

## Monitoring conformity within the year

A valid cycle can still be swamped by exogenous events in any given year. So
track a **current-year R**: the correlation between this year's actual price
action to date and the seasonal cycle, updated daily.

Starbucks in 2010 ran a 2010-R of 0.80, meaning the stock was closely following
its cycle and the cycle's forward implications deserved weight. A collapsing
current-year R is the signal to stop acting on the seasonal, regardless of how
good Cycle-R was.

## Trading only the aggressive parts

Do not trade the whole cycle. Trade its steepest segments.

- **Long zones** are the strongest rapidly-rising portions of the cycle (for
  example, the four strongest stretches of 14 days or more).
- **Short zones** are the weakest rapidly-falling portions.
- Minimum days per zone and the number of zones are parameters; set them
  deliberately rather than accepting a default.

The flat parts of a seasonal cycle carry no information worth transacting on.

## The causality caveat, stated plainly

Seasonal cycles **do not cause** price movement. They reflect tendencies produced
by fundamental influences that recur at regular intervals. Any exogenous factor
can overwhelm them at any time. Treat a seasonal as a prior with a decay rate,
never as a forecast.

## Workflow

```
[ ] Choose look-back (start at 15y)
[ ] Split-half: build cycle from each half of the window
[ ] Compute Cycle-R. Low correlation -> STOP, there is no seasonality here
[ ] Sweep look-backs 2y..15y; record Cycle-R for each; pick the max
[ ] Compare standard vs optimized cycle. Where they AGREE, weight it more
[ ] Mark long zones and short zones; ignore the flat middle
[ ] Build the cycle BEFORE the year starts; do not refit inside the year
[ ] Track current-year R daily; abandon the seasonal if it decays
[ ] Ask what fundamental mechanism would produce this timing. No story, less size
```

## Failure modes this catches

- A pattern driven by two or three extreme years inside the window (the halves
  will disagree).
- A pattern that was real and has expired after a fundamental change (the
  optimized short window will disagree with the long one, and the current-year R
  will be poor).
- Fitting the cycle to the year in progress, which is the most common way a
  seasonal study fools its author.

## Related

- [[rrg-relative-rotation]] as a second, independent lens on relative strength in
  the same window.
- [[katz-optimization-discipline]] for the general form of this argument: the
  look-back sweep is an optimization, and Cycle-R is its hold-out test.
