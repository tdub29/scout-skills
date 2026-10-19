---
name: katz-breakout-threshold-design
description: "Trading breakout entry: threshold, order, filters."
---

# Katz Breakout Threshold Design

## What this decides

Where to put a breakout threshold, how to enter when it is crossed, and whether
a breakout system deserves to be built at all in the given market.

Start honest: **simple breakout models have decayed.** Tested across a broad
futures portfolio, in-sample 1985-1995 and out-of-sample 1995-1998, no variation
except restricting to currencies cleared transaction costs out of sample, and the
deterioration was not explainable by overoptimization. Treat "breakout system"
as a starting point requiring a specific edge, not as a default.

## The three threshold families

**Trendline / support-resistance breakout.** The chartist's original: buy when
price breaks above a descending trendline, sell below an ascending one.
Thresholds can also come from Gann angles or Fibonacci retracements. Mechanizing
it requires resolving the subjectivity of where the line goes.

**Channel breakout (highest-high / lowest-low).** Buy above the highest high of
the last n bars, sell below the lowest low. Fully mechanical, no drawing
required. Also runs in a close-only variant using the highest and lowest closes.

**Volatility breakout.** Bands set a volatility-scaled distance above and below a
reference value (typically the last close). Bands widen as volatility rises and
contract as it falls. The logic is statistical: if the market moves farther than
normal jitter predicts, something real may have impinged.

### What the tests actually said

- **In sample (1985-1995):** volatility breakout best, highest-high/lowest-low
  in the middle, close-only worst. Consistent across all three order types.
- **Out of sample (1995-1998):** highest-high/lowest-low still slightly beat
  close-only, but **the volatility model deteriorated badly** and its equity
  declined significantly. Plausibly because it was the model sold in every
  $3,000 system since the late 1980s, so the market adapted to it.
- **Prefer support and resistance.** The highest-high/lowest-low breakout held
  up best over time even where it did not produce the largest returns, because
  support and resistance are fundamental verities unlikely to be traded away.
- **Avoid plain volatility breakouts** unless they carry a specific twist that
  survives their own popularity.

## Threshold placement is a noise problem

This is the whole craft. Place thresholds where random, nontrending activity is
unlikely to reach, but a real trend is likely to reach.

- **Too close to price:** noise triggers entries in both directions. False
  breakouts and whipsaws, no follow-through, and the account bleeds out in
  commissions and slippage.
- **Too wide:** few trades, and each one entered late in a move. The occasional
  big trend profit gets erased by losses on reversals.
- **Correctly placed:** frequent small losses from noise-triggered entries, paid
  for by substantial profits on major thrusts. That loss profile is the intended
  behavior, not a defect.

Current market noise around conventional threshold levels is high enough to
generate excessive bad entries, especially in active volatile markets like the
S&P 500 and T-Bonds.

## Entry order: use a limit

The single most important finding, and it is counterintuitive.

> Both in and out of sample, across all models, **the limit order provided the
> greatest edge**; stop and market-at-open orders did poorly.

Expectation would be that waiting for a limit misses too many good trends. It
does not: the market pulls back often enough, even after valid breakouts, to fill
a limit at a better price without missing many good trends. The gain comes from
better entry prices and from controlling transaction costs, whose impact is
dramatic.

Also observed: **stop-entry performance decayed more over time than the other
orders**, plausibly because stops are the conventional trend-following entry, so
the crowding is worst there. The highest-high/lowest-low model sometimes favored
a stop; the volatility model never did.

Even an unsophisticated limit entry improves results markedly. A more
sophisticated one should do better still.

## Restrictions and filters

- **Long-only helps.** Restricting to longs greatly improved the volatility
  breakout in sample and improved it out of sample. Breakout models do better on
  the long side.
- **The ADX trend filter did not.** Small in-sample benefit, **no out-of-sample
  benefit.** Do not rely on ADX to decide whether a market is trendy.
- **Market selection is the biggest lever.** Restricting to currencies hurt in
  sample (fewer markets) but produced dramatic out-of-sample improvement, the
  only combination that was actually profitable out of sample. Currencies are
  huge and driven by powerful fundamental forces, so they did not suffer the
  efficiency gain that killed breakouts elsewhere.
- Consistently positive across both samples: the currencies (Deutschemark, Swiss
  Franc, Japanese Yen, Canadian Dollar) and the oils (light crude, heating oil).
  A basket of all six currencies, all three oils, or both, was profitable in both
  samples. Coffee, live hogs, and random lumber also showed positive returns.
- In-sample and out-of-sample net profit correlated only about 0.15 by market:
  weak, but positive, so past tradeability carries a little information.

## Design checklist

```
[ ] Threshold family chosen (prefer HHLL / support-resistance over volatility bands)
[ ] Threshold distance justified against a noise measure, not a round number
[ ] Entry on a LIMIT (pull-back after the breakout), not a stop, unless there is
    a specific tested reason
[ ] Long-only considered
[ ] Market list restricted to genuinely trending markets (currencies, oils)
[ ] ADX or similar NOT used as the trendiness gate
[ ] A real exit strategy, not the standard exit
[ ] Slippage assumptions realistic for the entry order actually used
```

## Why breakouts fail intraday

Slippage relative to typical trade size is severe when breakout entries are
implemented on an intraday time frame. Longer-term breakout entry may perform
acceptably. A tight stop right after the breakout, relying on momentum to carry
past it, can only be tested properly with tick-level intraday data.

## Related

- [[katz-entry-order-selection]] for the general order-type reasoning behind the
  limit-order finding.
- [[katz-exit-strategy-taxonomy]] because the tests explicitly note a better exit
  is where much of the remaining improvement lives.
- [[katz-optimization-discipline]] for why the in-sample-to-out-of-sample decay
  here is a real market effect, not just overfitting.
