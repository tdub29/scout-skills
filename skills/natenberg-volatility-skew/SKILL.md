---
name: natenberg-volatility-skew
description: Reads an implied-volatility curve across exercise prices, names its shape in Natenberg's own vocabulary, states what distribution the marketplace is implying, and converts that into strike selection, butterfly relative value, and risk estimates under changing conditions. Use when the user says "why are the out of the money puts so expensive", "read this vol skew for me", "is this a smile or a smirk", "which strike is actually cheap", "my model says this option is cheap but everyone is bidding it", "what does a skewed distribution do to option prices", "how do I feed a skew into my pricing model", or "the underlying moved and vol rose, where does my skew sit now". Produces a fitted and normalized skew curve, a per-strike cheap/rich verdict against neighboring strikes, and the adjustment rules for shifting the curve. From Sheldon Natenberg, Option Volatility and Pricing, Chapter 18.
---

# Natenberg Volatility Skew

## What this decides

Every exercise price in a chain prints a different implied volatility, yet the underlying can have only one volatility over its life. This skill decides what to do about that gap.

Natenberg's licensing move (book p405): assume the marketplace is using the same model you are, then ask how the marketplace is dealing with the weaknesses in that model. Implied volatility asks what volatility the market is implying. The skew asks what *weaknesses* the market is implying, and Natenberg flags this as "a more difficult question to answer."

The chapter reaches the skew as the practical alternative to buying a fancier model. Verbatim, book p405: "A model might be better in the sense that it gives slightly more accurate theoretical values. But if the model is extremely complex and difficult to use, or if it requires additional inputs of which a trader cannot always be certain, then the model may merely substitute one set of problems for another. Given the fact that most traders are not theoreticians, a more realistic solution might be to use a less complex model and somehow fine-tune it so that it is consistent with the realities of the marketplace."

Outputs of this skill:

1. A named shape, using only Natenberg's vocabulary.
2. A normalized curve (percent of at-the-money volatility on y, `ln(E/U)/sqrt(t)` on x) that is comparable across expirations, price levels, and vol levels.
3. A per-strike relative-value verdict against its neighbors, with the butterfly that expresses it.
4. A rule for re-pricing every strike when your volatility opinion changes, when the underlying moves, or when time passes.

What this skill does **not** own: the full six-assumption audit of the pricing model, the alternative models (stochastic volatility, jump-diffusion, CEV), and expiration straddles all live in [[natenberg-model-assumptions-audit]].

## Skewness and kurtosis: what a shape change does to prices by strike

**The two descriptors** (book p402, Figures 18-6a and 18-6b). "A perfectly normal distribution can be fully described by its mean and standard deviation. But two other numbers, the skewness and kurtosis, are often used to describe the extent of the difference between an actual frequency distribution and a true normal distribution."

- **Skewness** is "the lopsidedness of the distribution, or the extent to which one tail is longer than the other tail." Positively skewed means the right-hand tail is longer than the left. Negatively skewed means the left-hand tail is longer than the right. "A true normal distribution has a skewness of zero."
- **Kurtosis** is "the extent to which the peak of the distribution is unusually tall and pointed, or low and flat." Positive kurtosis gives a tall pointed peak (leptokurtic). Negative kurtosis gives a low flat peak (platykurtic). "A perfectly normal distribution has a kurtosis of zero (mesokurtic)."

**The discriminator you must not skip.** A low standard deviation also produces a pointed peak. The difference is the tails: a low-standard-deviation distribution has *narrow* tails, a positive-kurtosis distribution has *long* tails. A positive-kurtosis distribution is also "narrower, or squeezed inward, in the midsection between its peak and tails."

**The empirical universal.** Real markets show positive kurtosis, "as do almost all underlying markets": higher peaks (more days with small moves), more elongated tails (more days with big moves), and narrower midsections (fewer days with intermediate moves) than a true normal predicts.

**Figures 18-5a, 18-5b, 18-5c, percent daily price changes 1989 to 1993**, bars to the nearest quarter percent with an exact normal curve overlaid from the mean and standard deviation of the same daily changes.

| Statistic | 18-5a S&P 500 Stock Price Index | 18-5b German Bonds | 18-5c Soybeans |
|---|---|---|---|
| Total number of days | 1265 | 1261 | 1262 |
| Largest upward move | +3.73% | +2.323% | +7.75% |
| Largest downward move | -6.12% | -1.930% | -7.12% |
| Mean | +.044% | +.0038% | -.020% |
| Standard deviation | .795% | .3265% | 1.202% |
| Annualized volatility | 12.653% | 5.183% | 19.084% |
| Skewness | -.352 | -.009 | +.152 |
| Kurtosis | +4.343 | 6.473 | +4.606 |

Read those signs: the S&P 500 and German Bunds are slightly negatively skewed (longer left tail), soybeans slightly positively skewed (longer right tail). All three are strongly leptokurtic.

**How this reaches prices by strike, and how it does not.** Natenberg does not convert a skewness or kurtosis number into a per-strike valuation adjustment anywhere in this chapter. He presents them as descriptors: "If one is trying to make decisions based on the characteristics of a distribution, it might be useful to know how the actual distribution differs from the normal." The calculation itself is exiled to Appendix B. The one live channel from distribution shape to option prices runs through **kurtosis and the wings**: the outliers in Figures 18-5a/b/c are the evidence he reuses at book p407, where the market's inflated wings mean "the marketplace appears to believe there is a better chance for a large price move in the real world than is predicted by the Black-Scholes model," and "It is the possibility of these large moves which apparently causes the marketplace to inflate the prices of options which are far out-of-the-money or deeply in-the-money."

So the disciplined statement of direction is:

- **Positive kurtosis (fat tails, thin midsection) inflates the wings**, calls and puts alike, at exercise prices far out-of-the-money and deeply in-the-money, relative to a Black-Scholes value computed off the at-the-money volatility.
- **Skewness sign is a property of the underlying's return distribution, not a derivation of the option skew's tilt.** Natenberg keeps the two arguments separate on purpose. Where he does discuss an asymmetric option skew, in stock index markets, he notes "the extreme inflation of downside exercise prices, both for calls and puts" and leaves the cause unadjudicated between two candidates: "it may indicate that the marketplace believes stock markets go down faster than they go up, as witness October 1987, or it may reflect the fact that stock index options are often used to hedge long stock portfolios." His operative conclusion either way is only that "the marketplace seems to be giving greater relative value to lower exercise prices." Do not upgrade a negative return skewness into a claim about which side's options are rich. Read the implieds.

## Reading a skew

**Step 1. Check the vertical arbitrage consistency first.** In a well-arbitraged market "the implied volatilities for calls and puts at the same exercise price are always the same. If this were not true, the prices would reflect an arbitrage opportunity." Overpriced calls versus puts means a profitable conversion, overpriced puts versus calls means a profitable reverse conversion. Calls and puts lining up "indicates an efficient market with respect to arbitrage relationships." Caveat from the footnote: settlement prices are intended to reflect this, but intraday, with a bid/ask spread on every option and non-simultaneous trades, "markets may appear less efficient."

**Step 2. Confirm the anomaly is across strikes, not across call/put.** Figure 18-7, the printed Bund table. Header as printed: July 27, 1992, German Government Bond (Bund) Futures, December Futures Contract = 87.86, Days to Expiration = 119, Interest Rate = 0%. (The body text on book p405 dates the same data July 17, 1992. The two disagree in the scan.)

| Exercise Price | Call Price | Call Implied Volatility | Put Price | Put Implied Volatility |
|---|---|---|---|---|
| 84.50 | 3.40 | 3.98 | .04 | 3.98 |
| 85.00 | 2.92 | 3.82 | .06 | 3.82 |
| 85.50 | 2.46 | 3.76 | .10 | 3.76 |
| 86.00 | 2.02 | 3.68 | .16 | 3.68 |
| 86.50 | 1.61 | 3.62 | .25 | 3.62 |
| 87.00 | 1.25 | 3.62 | .39 | 3.62 |
| 87.50 | .93 | 3.58 | .57 | 3.58 |
| 88.00 | .67 | 3.58 | .81 | 3.58 |
| 88.50 | .46 | 3.56 | 1.10 | 3.56 |
| 89.00 | .31 | 3.60 | 1.45 | 3.60 |
| 89.50 | .20 | 3.62 | 1.84 | 3.62 |
| 90.00 | .13 | 3.69 | 2.27 | 3.69 |
| 90.50 | .08 | 3.73 | 2.72 | 3.73 |
| 91.00 | .05 | 3.81 | 3.19 | 3.81 |
| 91.50 | .03 | 3.87 | 3.67 | 3.87 |

Interest rate is zero because "Since options on LIFFE are settled like futures contracts, the effective interest rate for theoretical calculations is zero. As a result, there is no economic value to early exercise, and one can calculate all implied volatilities using the Black-Scholes model."

Calls and puts agree at every strike. Strikes do not agree with each other: the 89 implies 3.60 while the 85 implies 3.82. A pure Black-Scholes adherent would sell the rich ones and buy the cheap ones until every implied lined up, "Yet this almost never happens in any market." The inference: "the marketplace does not think the Black-Scholes model is one hundred percent efficient." Identifying *which* weakness (frictions, gaps, non-constant volatility, non-lognormality) "may not be possible," and Natenberg does not require you to. "Whatever the reason, the marketplace believes that options at any moment are priced efficiently, even if those prices happen to differ from model-generated values."

**Step 3. Plot and fit.** Plot implied volatility against exercise price and draw a curve that fits the points (Figure 18-8a).

**Step 4. Read the shape.** For the Bund: "The low point of the graph is close to the price of the underlying contract (87.86), and the tails of the graph rise as we move to exercise prices further away from the underlying price."

**Step 5. Name it in his vocabulary.** The Bund shape is "probably the most common skew shape, a smile which is approximately symmetrical." The general taxonomy: "Skews can be symmetrical or asymmetrical, and they can reflect inflated or deflated implied volatilities across exercise prices, depending on how the marketplace sees the possibility, and consequences, of various moves in the underlying market." Wings are described as raised or lowered, inflated or reduced. The stock index case is named by description, "extreme inflation of downside exercise prices, both for calls and puts."

> Vocabulary guard: the terms **"investment skew"** and **"forward skew"** do not appear anywhere in this edition, and neither do "smirk," "volatility surface," "term structure of volatility," "risk reversal," or "sticky strike / sticky delta." If the user asks about a smirk, answer in his terms (asymmetrical skew, inflated downside exercise prices) and say plainly that the modern label is not Natenberg's.

**Step 6. Relative value against neighbors, which is the actual trade read.** Verbatim, book p407: "We may not know exactly what the 88.50 call is worth, but we can see that it is clearly too cheap with respect to the 88 and 89 calls. In the same way, we may not know what the 87 put is worth. But it is clearly too expensive with respect to the 86.50 and 87.50 puts. In the former case, a trader might try to sell the 88.50/89.00/89.50 butterfly. In the latter case, a trader might try to buy the 86.50/87.00/87.50 butterfly. Whatever we think of the skew, there ought to be a smooth progression of implied volatilities from one exercise price to the next."

Mechanically: selling the 88.50/89.00/89.50 butterfly buys the wings, which includes the too-cheap 88.50 call. Buying the 86.50/87.00/87.50 butterfly sells two of the too-expensive 87 put body. The skew is a **relative** value tool. A strike sitting on your fitted curve is not thereby fairly priced in absolute terms.

## Adjusting for a skew

**Normalize the x-axis before you compare anything.** All moves are relative, to price and to time. A 4 point move is 5% with the underlying at 80 and 4% at 100. A four-point move over two weeks is larger than the same move over two months. Black-Scholes measures underlying movement on a logarithmic scale and time by a square-root relationship, so the relative amount of movement required to reach an exercise price is:

> **[natural logarithm (exercise price / underlying price)] / square root (time)**, time in years.

Printed on the charts as `ln(ex. price/fut. price)/sqrt(time)`, range -0.15 to +0.15 in Figure 18-8d. "With our new x-axis measurements the skews start to look very much alike."

**Normalize the y-axis, and use the right normalization.** With the underlying at 87.86, the implied volatility of a theoretically at-the-money option struck at 87.86 is about 3.57%.

- Difference method, shown then rejected: 3.81 minus 3.57 = .24, and 3.68 minus 3.57 = .11. It fails the moment the vol level moves. If Bund implied doubled to 7.00%, each strike's implied roughly doubles too: 3.81 becomes 7.62 and 3.68 becomes 7.36. A fixed difference does not survive.
- Percent-of-at-the-money method, adopted: 3.81 / 3.57 = **106.7%**, and 3.68 / 3.57 = **103.1%**.

Combining the percent-of-ATM y-axis (Figure 18-8e axis runs 90 to 140) with the log/time x-axis makes the 2, 5, 11 and 17 week Bund skews nearly coincide, all passing through 100% at x = 0.

**Do not assume the skew is stationary.** Figure 18-8c is the counter-evidence: "The skew changed its shape, generally becoming more severe, as time passed. It also changed its position as both the price of the underlying contract and implied volatility changed." Printed snapshots: 17 weeks to expiration with Bund futures at 87.86, 11 weeks at 89.23, 5 weeks at 91.57, and 2 weeks at 91.57, on an implied-vol axis of 3.50 to 6.00. The 2-week skew is by far the most severe.

**The three legitimate shifts.**

1. **Your own volatility opinion.** Figure 18-7 at-the-money implied is about 3.58. A trader who thinks that is .25 points too low (a more reasonable 3.83) and still believes the skew captures relative value **raises the whole skew .25 volatility points** and prices every exercise price off the new curve. That reflects the vol opinion while keeping the relative value the skew encodes.
2. **Underlying movement.** If the underlying rises 2.00, hold the shape and **shift the whole skew up 2 points**, then raise or lower it against the at-the-money reference point for your vol view. Figure 18-8b plots the three states: current skew, skew with all volatilities raised .25, skew with underlying contract 2.00 higher.
3. **Disagreement about large moves.** "There is no law that says a trader must agree with the skew implied in the option market." Believe a large move is unlikely and you **lower the wings**. Believe one is likely and you **raise the wings**. Figure 18-10 labels these "wings inflated (better chance of a large move)" and "wings reduced (smaller chance of a large move)." Note the intervention point: a disagreement about tail size moves the wings, not the whole curve.

**Make the skew the sixth model input.** Figure 18-9: instead of the five usual variables (time to expiration, exercise price, underlying price, interest rates, volatility) the model takes six, with **volatility skew** added, feeding the theoretical pricing model to a theoretical value.

**Express the skew as a function so the model can eat it.** "While this may sound difficult, many skews can be expressed as simple equations." The function Figure 18-10 graphs as an approximation of the Figure 18-8 skews:

> **f(x) = 30 \* (x^2) + 1**, where **x = ln(ex. price / fut. price) / sqrt(time)**

applied as:

> **volatility at an exercise price = the at-the-money volatility times f(x)**, with the exercise price E always expressed against its underlying price U and time to expiration t as **ln(E/U) / sqrt(t)**.

At x = 0 this returns the at-the-money volatility exactly, and it lifts both wings symmetrically as the strike moves away in normalized terms, which is why it fits a symmetrical smile.

**This is also how the greek estimates get adjusted.** Natenberg's stated reason for the function is risk, not just valuation: "Pricing models are not only used to evaluate options under current conditions. They are also used to evaluate risk under changing market conditions. If a trader wants to fully incorporate a skew into his model, he needs to know how the skew is likely to change with changing market conditions." Once the skew is a function, "To analyze the value of an option position under changing assumptions about underlying price, time to expiration, and volatility, we need only express the volatility at each exercise price using this function." So the procedure is: re-evaluate the position by feeding each strike its own `ATM vol times f(x)` instead of one flat volatility, and recompute x whenever the underlying price or time to expiration changes. That is the adjustment. This chapter does not publish per-strike delta or gamma corrections beyond this, so do not manufacture one.

**Market-maker use of the same lever.** Long a large positive gamma position and wanting to sell options to cut risk, the market maker **shifts the skew slightly downward**, which lowers his bids and offers on all options. Short a large number of out-of-the-money calls or puts, he **raises the wings**, which raises his bids and offers on out-of-the-money options.

**Stock index special case.** Two changes from the Bund procedure. First, "in stock index markets, because it is not always possible to take advantage of a mispriced arbitrage relationship, calls and puts with the same exercise prices do not necessarily trade at the same implied volatility. For this reason, many traders in stock index markets prefer to evaluate call and put skews separately." Step 1 above does not hold here. Second, normalize to the **forward** price, not the index price, because index prices are assumed lognormally distributed around the forward, which is the current index price plus carrying costs less dividends:

> **ln(exercise price / forward price) / sqrt(time)**

OEX March 1993 data as printed on Figures 18-11a to 18-11d: 11 weeks to expiration OEX = 396.64 (forward 397.28), 5 weeks OEX = 406.26 (forward 406.79), 1 week OEX = 412.67 (forward 412.89). Raw axes in 18-11a/b are implied volatility 5 to 30% against exercise prices 360 to 430, with downside strikes extremely inflated for both calls and puts. Normalized axes in 18-11c/d are implied volatility 80 to 220 (percent of at-the-money) against x from -0.3 to +0.3. Result: "there is considerably more consistency than one would expect from Figures 18-11a and 18-11b. If a trader wanted to find functions, one for calls and one for puts, by which the skews could be expressed, he could use these functions to analyze a position under a wide variety of market conditions." Because early exercise is possible, OEX implied volatilities were calculated with the Cox-Ross-Rubenstein model, not Black-Scholes.

**The humility clause, keep it attached to every output.** Book p408: "dealing with a volatility skew can be a problem because there is no exact formula to use as a guide. Moreover, each trader tends to use the skew in a way that best serves his ultimate goal. A market maker might treat the skew one way, while a speculator or hedger treats the skew in a different way. Additionally, each trader must determine the relative accuracy of the information reflected in the skew. A trader who disagrees with a skew will find that some strategies will be more attractive than others." And book p416: this material "is intended not as a solution to all the problems that traders encounter in analyzing and using volatility skews, but as an introduction to how traders approach the problem."

## Failure modes

- **Treating the skew as stationary.** Figure 18-8c kills it: shape becomes more severe as expiration approaches, and position moves with both underlying price and vol level.
- **Normalizing the y-axis by difference from at-the-money vol instead of percent of it.** Breaks the instant the overall vol level moves (3.57 doubling to 7.00 doubles every strike).
- **Plotting against raw exercise price** when comparing across expirations or price levels. Use `ln(E/U)/sqrt(t)`, or `ln(E/forward)/sqrt(t)` for indexes.
- **Using the index price rather than the forward price** for stock index normalization.
- **Applying the "calls and puts at the same strike always share an implied" rule in stock index markets**, where the arbitrage is not reliably executable and call and put skews must be fitted separately.
- **Calling a strike that sits on your fitted curve fairly priced in absolute terms.** The skew ranks strikes against each other. Your own volatility opinion enters by shifting the whole curve.
- **Reading the Bund symmetrical smile as universal.** Skews can be symmetrical or asymmetrical, inflated or deflated.
- **Moving the whole curve when your real disagreement is about tail size.** That disagreement moves the wings.
- **Importing modern skew vocabulary.** "Investment skew," "forward skew," "smirk," "volatility surface," "term structure of volatility," "risk reversal," "sticky strike" and "sticky delta" are not in this edition and must not be attributed to Natenberg.
- **Treating a kurtosis or skewness number as a pricing adjustment.** The chapter never does. Distribution statistics are the *evidence* for inflated wings, not the calculation of them.
- **Confusing a low-standard-deviation peak with a leptokurtic peak.** Both are pointed. Only the leptokurtic one has long tails and a squeezed midsection.
- **Deriving the option skew's tilt from the underlying's return skewness.** The S&P is negatively skewed and the index option skew inflates the downside, but Natenberg deliberately leaves that link unresolved.

## Working checklist

```
[ ] Pull implieds for every exercise price, calls and puts separately.
[ ] Verify call and put implieds match at each strike (skip for stock index; fit two curves there).
[ ] Plot implied vol against exercise price and fit a curve through the points.
[ ] Locate the low point relative to the underlying price and describe the wings.
[ ] Name the shape in his vocabulary only: smile, symmetrical or asymmetrical, inflated or deflated, wings raised or lowered.
[ ] Flag any strike breaking the smooth progression from one exercise price to the next.
[ ] Convert each break into the butterfly that expresses it (sell the fly to buy a too-cheap wing strike; buy the fly to sell a too-expensive body strike).
[ ] Re-plot x as ln(E/U)/sqrt(t), or ln(E/forward)/sqrt(t) for stock index.
[ ] Re-plot y as percent of the at-the-money implied volatility, never as a difference from it.
[ ] Overlay the other expirations; confirm they nearly coincide at 100% at x = 0 before trusting a shared shape.
[ ] Fit a function of the f(x) = 30*(x^2)+1 family and record it as the sixth model input.
[ ] Apply it as: volatility at a strike = at-the-money volatility times f(x).
[ ] Apply your volatility opinion by shifting the entire curve, not by re-fitting the shape.
[ ] Apply an underlying move by shifting the curve with the underlying, then recomputing x for every strike.
[ ] Apply a disagreement about large moves by raising or lowering the wings only.
[ ] Re-run the position's risk with per-strike volatilities, not one flat volatility, whenever price, time, or vol assumptions change.
[ ] State explicitly that this is relative value and that no exact formula exists as a guide.
```

## Related

- [[natenberg-model-assumptions-audit]] owns the six-assumption audit of the traditional pricing model, the alternative models (stochastic volatility, jump-diffusion, CEV) and why Natenberg rejects each, and expiration straddles. The skew is the remedy that audit points to: you cannot fix the model, so infer what the marketplace has already priced into each strike.
- [[natenberg-volatility-types]] for what "implied volatility" is before you plot a curve of it, and for the difference between the volatility of the underlying and the volatility a given option is trading at.
- [[natenberg-volatility-forecast]] for forming the volatility opinion that this skill applies by shifting the whole curve up or down.
- [[natenberg-choosing-a-strategy]] for turning a cheap or rich strike verdict into a position, including the butterflies named in the relative-value step.
