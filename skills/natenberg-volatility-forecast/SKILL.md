---
name: natenberg-volatility-forecast
description: Builds a volatility forecast for a specific option horizon and converts it into a long-volatility, short-volatility, or no-trade call, with a strategy class and a position size attached. Use when the user asks "is implied vol cheap right now", "what vol should I use for a 60 day option", "should I be long or short vol", "build a volatility cone", "is 22% high for this name", "historical or implied, which do I trust", "what percentile is today's realized vol", "should I sell straddles or buy butterflies here", or "why is IV high when realized vol is low". Produces a numeric volatility input, a percentile read of today's implied against the instrument's own history, and a documented trade or stand-aside decision. From Sheldon Natenberg, Option Volatility and Pricing, Chapter 14.
---

# Natenberg Volatility Forecast

## What this decides

Given one instrument and one expiration, this produces three outputs in order: a numeric volatility forecast to feed a theoretical pricing model, a read of where today's implied volatility sits inside that instrument's own historical volatility distribution, and a directional volatility call (long vol, short vol, or no position) with a strategy class and size.

The framing constraint Natenberg sets at the top of the chapter governs everything below: "in theory the value of an option depends on only one volatility, the volatility of the underlying contract which will occur over the life of the option." Every historical number computed here is a proxy for that one unknowable number.

## Step 1. Build the volatility cone

The cone is the artifact. Build it before forming any opinion.

1. Pick the horizons you care about, expressed as weeks to expiration. Natenberg's printed cone runs 2 weeks to 50 weeks on the x-axis.
2. For each horizon, compute realized volatility over **every overlapping window of that length** in the history, not just the most recent window.
3. Across those windows, take the 10th, 25th, 50th (median), 75th, and 90th percentiles plus the mean.
4. Plot all six series against time remaining to expiration. Y-axis on Natenberg's Deutschemark cone: 6% to 18%.

Natenberg's printed cone (Figure 14-3, Deutschemark Volatility Distribution 1982-1991):

| Horizon | 10th pctl | 25th pctl | Mean | 75th pctl | 90th pctl |
|---|---|---|---|---|---|
| Two weeks | 6.0% | 7.6% | 9.7% | 13.0% | 17.3% |
| 50 weeks | 9.8% | 10.6% | approx. 11.5% | 12.7% | 14.0% |

Stated as probabilities in the text: at two weeks there is a 20% chance volatility is less than 6.0% or greater than 17.3%, and a 50% chance it is less than 7.6% or greater than 13.0%. At 50 weeks there is a 20% chance it is less than 9.8% or greater than 14%, and a 50% chance it is less than 10.6% or greater than 12.7%.

**How to read it.** Three readings, all decidable:

- **Percentile of today.** Locate the tenor you are trading on the x-axis, drop today's implied volatility onto that column, and report which band it falls in. Above the 75th means rich against the instrument's own history at that tenor. Below the 25th means cheap.
- **Width of the cone at your tenor.** The distance between the low and high percentile lines at your tenor is the volatility move you must survive. This number feeds Step 7, not Step 6. Width sets size and structure, not direction.
- **Convergence.** "As one moves further out in time the percentile lines tend to converge towards the mean, and the mean becomes stable." Take the equilibrium level from the stable long-horizon mean, never from the latest single reading.

Supporting facts from the same section, for calibrating expectations about what a cone looks like: over 1982-1991 Deutschemark 50-day volatility ranged from a low of 5% to a high of 20% while price ran from 29 to 63 cents per DM. Prices are open-ended, volatility is not: "no matter how much it fluctuated, at some point volatility always reversed itself and retraced almost all of its previous rise or fall." The DM equilibrium volatility is "about 11% to 12%."

Do not carry those Deutschemark numbers to another market. Build the cone per market.

## Step 2. Mean reversion, and how far you can lean on it

Definitions Natenberg sets, used as decision rules downstream:

- *mean volatility*: "a typical long-term average."
- *mean reverting*: "When volatility rises above the mean, one can be fairly certain that it will eventually fall back to its mean; when volatility falls below the mean, one can be fairly certain that it will eventually rise to its mean. There is a constant gyration back and forth through this mean."
- *serial correlation*: "The volatility over any given period is likely to depend on, or correlate with, the volatility over the previous period, assuming that both periods cover the same amount of time. If the volatility of a contract over the last four weeks was 15%, the volatility over the next four weeks is more likely to be close to 15% than far away from 15%."

The operative qualifier: reversion is horizon-dependent. "The mean reverting characteristics of volatility are much less certain over short periods of time than over long periods." Therefore never build a mean-reversion trade in a short-dated option on the strength of the mean alone. There may be no time for the reversion to happen.

Volatility charts do trend (Figure 14-4: down July 1989 to June 1990, up July 1990 to April 1991, down April 1991 to October 1991, with minor trends inside the majors), and Natenberg notes they resemble price charts. He then abandons the idea rather than developing it: he claims no expertise in technical analysis and leaves the reader to his own devices, so do not apply technical-analysis rules to volatility charts on his authority. Likewise ARCH and GARCH are named, footnoted, and declared out of scope, "mathematically complex and not widely used among traders," framed only as the formalized version of mean reversion plus serial correlation.

## Step 3. Compute the horizon-matched historical forecast

Natenberg's standing data set, and every weight vector he prints against it:

| Reading period | Vol | Equal | Recency x2 | Regressive | 6-month (120d peak) | 10-week (60d peak) |
|---|---|---|---|---|---|---|
| last 30 days | 24% | 25% | 40% | 40% | 15% | 25% |
| last 60 days | 20% | 25% | 20% | 30% | 25% | 35% |
| last 120 days | 18% | 25% | 20% | 20% | 35% | 25% |
| last 250 days | 18% | 25% | 20% | 10% | 25% | 15% |
| **Forecast** | | **20%** | **20.8%** | **21.0%** | **19.4%** | **20.2%** |

Arithmetic as printed:

- Equal weight: (24% + 20% + 18% + 18%) / 4 = 20%.
- Recency, double weight to the most recent reading: (40% x 24%) + (20% x 20%) + (20% x 18%) + (20% x 18%) = 20.8%.
- *Regressive weighting*, "giving more distant volatility data progressively less weight": (40% x 24%) + (30% x 20%) + (20% x 18%) + (10% x 18%) = 21.0%.
- Six-month options: (15% x 24%) + (25% x 20%) + (35% x 18%) + (25% x 18%) = 19.4%.
- Ten-week options: (25% x 24%) + (35% x 20%) + (25% x 18%) + (15% x 18%) = 20.2%.

**The rule that overrides the others.** Weight by horizon match, not by recency: "we might logically choose to give the greatest weight to the volatility data covering a time period closest to the life of the options in which we are interested. That is, if we are trading very long-term options, the long-term data should get the most weight. If we are trading very short-term options, the short-term data should get the most weight. And if we are trading intermediate-term options, the intermediate-term data should get the most weight."

The resulting weight vector is a hump centered on the horizon-matched reading, not a monotone decay. Recency weighting is only the special case where the option traded is very short-dated.

Degenerate long-horizon case, stated explicitly: "over very long periods of time the most reasonable volatility forecast is simply the long-term mean volatility of the instrument." Use the cone's stable long-horizon mean and stop.

More-data rule: more reading periods produce a better forecast because they let you match the traded expiration more closely. "Ideally, we would like historical data covering exactly a six-month period and exactly a 10-week period." The 60-day and 120-day windows are approximations for 10-week and six-month options; compute the exact windows if the data allows.

Trading-day to calendar mappings Natenberg actually uses: 30 trading days is about six weeks, 50 trading days is about ten weeks, 95 trading days is about 19 weeks, 120 trading days is about six months, 250 trading days is about one year.

## Step 4. Blend in implied volatility, 25% to 75%

Why look at implied at all: no individual trader knows everything affecting the underlying, so read the option market for the *consensus volatility*.

The band, verbatim: "Typically, a trader might give the implied volatility a weighting somewhere between 25% and 75% in making a volatility forecast."

The setting rule is confidence, not habit: "If a trader feels very confident about his forecast, he might give the implied volatility as little as a 25% weight; if he feels uncertain about his forecast, he might give the implied volatility as much as a 75% weight." Confidence depends on experience and on how conclusive the historical data is.

Worked blends, historical forecast 20% and implied 24%:

| Implied weight | Arithmetic | Blended forecast |
|---|---|---|
| 75% | (75% x 24%) + (25% x 20%) | 23% |
| 50% | (50% x 24) + (50% x 20) | 22% |
| 25% | (25% x 24%) + (75% x 20%) | 21% |

Output of Step 4 is the single number you type into the pricing model. Never 0% implied and never 100% implied. The 100% case is the pure efficient-market position that "most traders" reject; the 0% case throws away the consensus information.

## Step 5. Score the six factors

Natenberg's printed checklist, in his order. Answer all six before deciding.

| # | Factor | What it pushes |
|---|---|---|
| 1 | What is the long-term mean volatility of the underlying contract? | Sets the reference line. Read it off the cone's stable long-horizon mean. |
| 2 | What has been the recent historical volatility in relation to the mean volatility? | Above the mean pushes short vol, below the mean pushes long vol. |
| 3 | What is the trend in the recent historical volatility? | Trend toward the mean confirms the factor-2 push; trend away from it contradicts and downgrades conviction. |
| 4 | Where is implied volatility and what is its trend? | Implied above historical and falling reinforces short vol; implied moving opposite to historical is a conflict. |
| 5 | Are we dealing with options of shorter or longer duration? | Longer duration gives reversion time and strengthens the mean-reversion trade. Shorter duration weakens it. |
| 6 | How stable does the volatility tend to be? | Does not set direction. Sets structure and size, via Step 7. |

Match the historical window to the time remaining: 50-day historical for ten-week options, 30-day for six-week, 95-day for 19-week. Plot exactly three series plus one reference line: horizon-matched historical volatility, implied volatility, and a horizontal long-term mean.

## Step 6. Decide direction from alignment

| Case | Printed configuration | Decision |
|---|---|---|
| Aligned (Fig 14-5A) | 50-day HV approx. 20.6%, long-term mean approx. 18.7%, IV 22.1% (about 1.5 points above HV), both HV and IV declining | "A short volatility position (negative gamma/negative vega) is strongly indicated." |
| IV ahead of HV (Fig 14-5B) | HV above mean and declining, IV already moved ahead of HV | Short vol still available, but "he is unlikely to have the same degree of confidence." Cut size. |
| HV rising (Fig 14-5C) | HV above the long-term mean but increasing | Contradiction between factors 2 and 3. Downgrade conviction. |
| IV opposed (Fig 14-5D) | IV moving in the opposite direction of HV | Contradiction between factors 3 and 4. Downgrade conviction. |
| No trade (Fig 14-6A) | Six-week / 30-day options. HV 15.8%, mean 11.2%, IV 14.6% (above the mean, below HV), both HV and IV trending up, and no telling how long reversion takes | "With so many contradictory signals, a trader is unlikely to have a strong opinion about whether he should buy or sell volatility. He may choose to take no position at all, preferring to wait for clearer indications." |
| Longer horizon preferred (Fig 14-6B) | 19-week / 95-day options. HV 12.6%, mean 11.2%, 19-week IV 14.5%, above both | "There is a much better chance that the volatility will revert to its mean over a 19-week period than over a six-week period, so there are much stronger reasons for taking a short volatility position in 19-week options than in six-week options." |

Reframe that licenses all of this: "Rather than asking what the correct volatility is, a trader might instead ask, given the current volatility climate, what's the right strategy?" Point forecasts are "often incorrect, and sometimes to a large degree," so the climate read is the fallback, not a shortcut.

**Two-expiration combination.** When the short-dated read is ambiguous and the long-dated read is short vol, take both: "By creating a short time spread (buy six-week options / sell 19-week options) we can take a position which should be profitable based on our knowledge of volatility characteristics, but which also has acceptable risk characteristics if we are wrong." Name the residual risk before entering: the worst case for a short time spread is historical volatility dropping quickly to or below its mean while implied volatility stays high.

## Step 7. Map stability to structure and size

Same direction, two different structures, decided by the cone width at your tenor against the implied edge:

| Cone width at tenor | Implied edge | Structure |
|---|---|---|
| 50-day vol "can easily vary by as much as 10 percentage points" | IV 22.2%, only slightly above the 50-day HV | Buy butterflies. "If a riskier strategy is chosen, perhaps it should be done only in small size." |
| Vol "varying only five or six percentage points for any 50-day period" | IV 25% | "A trader may be willing to take on a much riskier position, perhaps selling straddles or strangles." |

Decision rule: wide cone plus thin edge equals defined-risk structure or small size. Narrow cone plus fat edge equals naked premium. Skipping factor 6 is what puts a naked short straddle on top of a 10-point vol range for 1.5 points of edge.

Closing principle on structure choice: "a trader who is familiar with the greatest number of strategies will have the best chance of surviving and prospering."

## Step 8. Choose the expiration using the implied-versus-historical rules

Implied volatility is "a consensus volatility among all market participants with respect to the expected amount of underlying price fluctuation over the remaining life of an option." Five rules that decide where to express the view:

1. **Implied follows historical in direction.** "As the market becomes more volatile, implied volatility can be expected to rise; as the market becomes less volatile, implied volatility can be expected to fall." Confirmed on Treasury Bond futures 1989-1991, including the August 1990 to January 1991 Iraqi invasion of Kuwait period.
2. **Damping.** "The fluctuations in implied volatility were usually less than the fluctuations in historical volatility." Never model implied as moving point for point with historical.
3. **Term structure.** Long-dated implied stays "closer to the mean volatility" and moves less in both directions. Evidence in January 1991 T-Bond options: March rose most, then June, then September; on the late-January decline the order reversed, with March falling most rapidly. Decision: express a view that depends on a large implied move in the shorter expiration; express a view that depends on stability in the longer one.
4. **Event premium.** "Over long periods of time the historical volatility of the underlying contract will be the dominant factor affecting implied volatility. Over short periods of time, however, other factors can also play a significant, perhaps even a dominant, role." Named events: government economic reports for interest rates and currencies ("going into government reports, there is a strong tendency for implied volatility to rise, even in the face of low historical volatility"), finance-minister meetings for currencies, OPEC meetings for energy, and for stock options earnings news, new-product success or failure, and takeover possibility, "regardless of the historical volatility of the stock." Decision: discount that portion of implied rather than treating it as a forecast.
5. **Post-event collapse.** "This is why implied volatility sometimes drops right after large moves in the underlying contract. Once the big event has occurred, there may be a perception that all the uncertainty has been removed from the market." Implied can fall while historical is still high.

## Step 9. Run the overwhelm check before trading implied alone

Do not enter a trade whose entire thesis is "implied volatility will rise." Natenberg's worked delta-neutral example: futures 97.73, 60 days to expiration, 6% interest rate, 20% implied volatility, the 100 call trading at 2.17 with an implied delta of 40. Position: buy ten 100 calls at 2.17, sell four futures at 97.73.

| Scenario | New call price | P&L |
|---|---|---|
| IV immediately rises 20% to 22% | 2.47 | 10 x (2.47 - 2.17) = +3.00 |
| IV rises 20% to 22% slowly over 20 days, underlying still 97.73 | 1.87 | 10 x (1.87 - 2.17) = -3.00 |
| IV immediately drops 20% to 18% | 1.86 | 10 x (1.86 - 2.17) = -3.10 |
| IV drops to 18% and futures falls to 93.00 | .59 | 4 x (97.73 - 93.00) - 10 x (2.17 - .59) = +3.12 |
| IV drops to 18% and futures rises to 102.50 | 4.32 | 4 x (97.73 - 102.50) + 10 x (4.32 - 2.17) = +2.42 |

Conclusion, verbatim: "The important point is that the volatility of the underlying contract, whether the contract moves or sits still over time, will eventually overwhelm any changes in implied volatility." And: "we need to know value as well as price. The value of an option is determined by the volatility of the underlying contract over the life of the option." Natenberg prints the caveat that these are simplified: a trader rehedging to stay delta neutral will see P&L affected by the cash flow of the adjustment process.

Decision rule: pair every implied-volatility view with a view on whether the underlying actually moves, and check the time it will take for the implied move to arrive.

## Step 10. Price in the chance the consensus is simply wrong

Measurement procedure Natenberg gives for grading implied as a forecast: "record the implied volatility at any moment in time and then, when expiration arrives, look back and calculate the actual volatility of the underlying contract between the time we recorded the implied volatility and expiration. We can do this every day during an option's life."

Printed results on T-Bond options: "there is no guarantee that the marketplace will have the correct implied volatility. The implied volatility is a guess, and guesses carry with them the possibility of error, sometimes very large error."

| Series | Error pattern | Magnitude |
|---|---|---|
| March 1993 (Fig 14-9B) | Implied too high over almost all of the option's life; "had a trader sold premium at any time, he would have shown a profit" | Almost four percentage points at its most extreme, in October 1992 |
| December 1993 (Fig 14-9C) | Too high early, too low late | Too low by as much as three percentage points in the few weeks before expiration |
| June 1992 (Fig 14-9A) | Relatively accurate early, too high late | Not stated in the report |

**Near-expiry instability.** With a lot of time left, volatility to expiration is relatively stable, so implied is too. Close to expiration it becomes "much less stable": "One large move in the underlying contract with only several days remaining to expiration will result in a sharp increase in the volatility to expiration," and "if the underlying contract is relatively quiet over the last several days in an option's life, the volatility to expiration will collapse." The reason given: "The marketplace knows that the laws of probability are more likely to balance out over many occurrences than over only a few occurrences." Decision: treat near-expiration implied volatility as an unstable signal and do not build a percentile read on it.

Closing caution to attach to any output: "Every market has its own characteristics, and knowing the volatility characteristics of a particular market, whether interest rates, foreign currencies, stocks, or a physical commodity, is at least as important as knowing the technical characteristics of volatility. And this knowledge can only come from careful study of a market combined with actual trading experience."

## Failure modes

- Reading a single recent volatility window instead of the whole distribution, so you hold a point estimate with no sense of range.
- Treating the cone's mean as a price-style support or resistance level, or applying technical-analysis rules verbatim to a volatility chart.
- Transferring the Deutschemark numbers (5% to 20% range, 11% to 12% equilibrium) to another market.
- Using too little history. Natenberg's own hedge: "we have looked at a limited number of examples, making the generalizations even less reliable."
- Trusting the short-tenor end of the cone as if it were as stable as the long end.
- Defaulting to recency weighting on long-dated options, where the correct forecast collapses to the long-term mean.
- Using approximate windows (60-day for ten weeks, 120-day for six months) when exact-horizon windows are computable.
- Giving implied volatility 0% weight, or 100% weight, or setting the weight by habit rather than by measured confidence in the historical forecast.
- Treating GARCH output as categorically better than the weighted blend.
- Forcing a position when the six factors disagree. The printed correct answer in the Figure 14-6A case is no position.
- Comparing implied volatility to a historical window that does not match the time remaining to expiration.
- Selling straddles or strangles when the cone says vol can swing 10 points and the implied edge is about 1.5 points.
- Taking a mean-reversion short-vol trade in a short-dated option, where there may be no time for the reversion.
- Treating the short time spread as riskless. Its worst case is historical volatility collapsing to or below the mean while implied stays high.
- Ignoring factor 6, the factor that sets size and structure rather than direction.
- Buying options because implied is rising, with no view on whether the underlying moves. The 20-day slow-rise scenario turns a nominal +3.00 into an actual -3.00.
- Reading elevated implied as a forecast when it is event premium that will be removed once the event passes.
- Expressing a volatility view in the wrong expiration, given that short-dated implied over-reacts in both directions.
- Expecting implied to move point for point with historical.
- Treating implied as correct because it is the consensus. It was wrong by about four points too high in the 14-9B case and about three points too low in the final weeks of 14-9C.
- Trusting near-expiration implied as a stable signal.

## Working checklist

```
[ ] Build the cone: every overlapping window per horizon, 10/25/50/75/90 percentiles plus mean, plotted against weeks to expiration
[ ] Read the long-horizon stable mean off the cone; that is the long-term mean volatility, not the latest reading
[ ] Record the cone width at the tenor you are trading; this is the vol move you must survive
[ ] Place today's implied inside the cone at that tenor and name the percentile band
[ ] Compute horizon-matched historical readings (exact windows if possible; else 30/60/120/250 day)
[ ] Apply a hump-shaped weight vector peaking on the reading closest to the option's life; if very long-dated, use the long-term mean instead
[ ] Rate confidence in the historical forecast; set implied weight in the 25% to 75% band accordingly
[ ] Blend to a single number and record it as the model input
[ ] Answer all six factors, in order, in writing
[ ] Classify the configuration: aligned, conflicted, or contradictory; contradictory means no position
[ ] If trading, pick structure from cone width vs implied edge: wide and thin means butterflies or small size; narrow and fat allows straddles or strangles
[ ] Check duration: prefer the longer expiration for a mean-reversion trade; consider the short time spread when only the long end is clear
[ ] Screen implied for event premium (reports, finance ministers, OPEC, earnings, takeover) and discount it rather than forecasting from it
[ ] Run the overwhelm check: state how far and how fast the underlying must move for the trade to pay
[ ] Name the residual risk of the chosen structure before entering
[ ] Discount any read taken close to expiration; volatility to expiration is unstable there and so is implied
[ ] Record today's implied for later grading against realized volatility to expiration
```

## Related

- [[natenberg-volatility-scaling]] for converting a volatility number between annual, daily, and per-period terms before it enters any of the tables above.
- [[natenberg-volatility-types]] for the definitions of future, historical, forecast, implied, and seasonal volatility that Steps 3, 4, and 8 assume.
- [[natenberg-volatility-spread-classification]] for the mechanics of the butterflies, straddles, strangles, and time spreads that Step 7 and the two-expiration combination select.
- [[natenberg-break-even-volatility]] for the price-side version of the same question, when you want the volatility that makes a specific option a fair trade rather than a forecast for the instrument.
