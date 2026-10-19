---
name: natenberg-position-analysis
description: "Read my options position: greeks, risk, fix trade"
---

# Natenberg Position Analysis

## What this decides

Three questions, stated by Natenberg on book p353: "What are the risks to the position? What are the rewards? And what action should be taken if market conditions change either in the trader's favor or against him?"

The output is a decision artifact, not a description. Every worked example in the chapter terminates in an action: sell or buy roughly 89 shares per point to stay neutral, sell off some of the long 195 or 200 puts, buy back the 18 short stock contracts and replace them with a three way or a conversion, sell four underlying contracts to hedge between your delta and the implied delta.

Why the greeks alone will not do it (p353, near verbatim):

> "The first step in analyzing a position is to determine how the position will react to changing market conditions. One way to accomplish this is by looking at the total risk sensitivities of the position (delta, gamma, theta, vega, rho). Unfortunately, the risk sensitivities are only reliable under narrowly defined market conditions. Since it is often dramatic changes in market conditions about which a trader must be concerned, simply looking at the risk sensitivities rarely enables a trader to grasp fully the risks associated with a position. Moreover, most traders find it easier to interpret graphic information than a series of numbers."

**Boundary.** `options-payoff` takes a structure name and draws its payoff curve. This skill runs the other way, taking a raw list of legs and naming the structure plus its danger zones, which is what Natenberg's rules exist for (he wrote them for when a computer is unavailable to do the graphing): "Sometimes, if a computer is unavailable to do the graphing for us, we might have to mentally visualize such a graph. From the foregoing examples, perhaps we can formulate some rules which will enable us to do this." (p358 to p359)

Footnote 1 (p353): "The analyses in this chapter were done using either the Black-Scholes model for stock options or the Black model for futures options."

## Step 0 to 3: build the table, then verify it

**Step 0. State the market context row.** Underlying price, time to each expiration, volatility, interest rate, dividend. Every example opens with exactly this line, e.g. "Stock price = 98.75; Time to June expiration = 7 weeks / Volatility = 20%; Interest rate = 6%; Dividend = 0".

**Step 1. Tabulate every leg.** Simple positions: `Position | Option Price | Option Th. Val. | Option Delta | Option Imp. Vol.` Complex positions: `Contract | Position | Price | Th. Value | Delta | Gamma | Theta | Vega | Imp. Vol.` plus `Implied Delta` for futures. Express the underlying leg in **contracts**, not shares. Footnote 2 (p363): "Since the number of shares in an underlying stock contract varies from market to market, we simply express the underlying in terms of contracts. In U.S. markets where one option contract typically controls 100 shares of stock, this position would be short 1,000 shares." Deltas are quoted on a 0 to 100 scale (a 76 delta call, not .76).

**Step 2. Total theoretical edge. Identity:**

```
edge = SUM( signed_quantity x (theoretical value - price) )
```

Worked, and confirmed to reproduce Natenberg's printed totals exactly:

- Ex. 1: `-10 x (6.25-5.82) + 30 x (1.63-1.08) = +12.20`
- Ex. 2: `-20 x (1.88-1.35) + 20 x (3.13-2.22) = +7.60`
- Ex. 3: `20 x (1.02-.75) + 20 x (1.38-1.12) = +10.60`
- Complex position (Fig 17-5): reproduces his printed `P&L +18.82` leg by leg.

**Step 3. Aggregate the greeks. Identity:**

```
position_total_G = SUM( signed_quantity x per-contract G )     for G in {delta, gamma, theta, vega}
```

The per-option rows in Natenberg's tables are **per contract**; the totals row is quantity weighted. This identity reproduces every "position totals" row printed in the chapter. Ex. 1 gamma: `10 x 4.3 - 30 x 4.4 = -89.0`. Ex. 1 theta: `10 x (-.0344) - 30 x (-.0278) = +.4900`. Ex. 1 vega: `10 x .113 - 30 x .117 = -2.380`.

If your totals do not reproduce from the leg rows by these two identities, the table is wrong. Fix the table before reading anything off it.

## What each aggregate tells you

| Aggregate | What it tells you | Anchor |
|---|---|---|
| Theoretical edge | Where the graph crosses the current underlying price, measured above the zero P&L line. "This is the first thing a trader should look for." | p359 |
| Delta | The slope at the current underlying price. Positive = long the underlying, negative = short. Magnitude sets steepness. Neutral = exactly horizontal. | p359 to p360 |
| Gamma | Curvature, and the per point rehedge size. Position gamma of -89 means "for each point decline in the stock price we will need to sell approximately 89 shares of stock... If the stock begins to rise, for each point rise in the stock price, we will need to buy approximately 89 shares of stock." | p354, p360 to p361 |
| Theta | Vertical shift per day. -.2160 means "for each day that passes with no movement in the underlying stock price, our position will deteriorate by approximately .216." | p357, p361 |
| Vega | Vertical shift per volatility point. | p361 to p363 |
| Contract (lot) position | The tail slopes: how many contracts you are naked long or short after a large move. | p360 |
| Position implied volatility | The volatility at which the position approximately breaks even. | p355 |

## The five graphing rules, as Natenberg numbers them (p359 to p362)

> **1. *Theoretical Edge*** "The graph of a position with a positive theoretical edge will cross the current underlying price at a point above the zero profit & loss line. This is the first thing a trader should look for. When a trader is right about market conditions, he wants to know that his position will be profitable."

> **2. *Delta* (Figure 17-3a)** "A positive delta is theoretically equivalent to a long position in the underlying contract. The graph of such a position will cross the current underlying price at an angle extending from the lower left to the upper right. A negative delta is theoretically equivalent to a short position in the underlying contract. The graph of this position will cross the current underlying price at an angle extending from the upper left to the lower right. The exact slope of the graph as it crosses the current underlying price is determined by the magnitude of the delta. As the delta position becomes larger, the slope becomes more severe; as the delta position becomes smaller, the slope becomes less severe. The graph of a position which is delta neutral will be exactly horizontal as it crosses the current price of the underlying contract."

> **3. *Gamma* (Figure 17-3b)** "A positive gamma position will begin to bend upward as the underlying price moves away from the current price in either direction. This reflects the fact that a positive gamma position likes movement. The graph of such a position will take on a generally convex shape (a smile). A negative gamma position will begin to bend downward as the underlying price moves away from the current price in either direction. This reflects the fact that a negative gamma position prefers for the market to sit still. The graph of such a position will take on a generally concave shape (a frown)."

> **4. *Theta* (Figure 17-3c)** "As time passes a positive theta position will become more valuable, and the graph of such a position will shift upward. As time passes a negative theta position will become less valuable, and the graph will shift downward."

> **5. *Vega* (Figure 17-3d)** "A positive vega position will be helped by increasing volatility and hurt by declining volatility. The graph of such a position will shift upward when volatility increases and downward when volatility decreases. A negative vega position will be hurt by increasing volatility and helped by declining volatility. The graph of this position will shift downward when volatility increases and upward when volatility decreases."

## The contract or lot position (p360 to p361)

Natenberg introduces this as the missing sixth input: "In order to complete a graph there is one other piece of information we need."

> "Suppose the underlying contract makes such a large upward move that all calls go into-the-money and all puts go out-of-the-money, or such a large downward move that all puts go into-the-money and all calls go out-of-the-money. In other words, what will the graph of a position look like at the extreme right or left tail? We can determine this by adding up our ***contract*** or ***lot position***. This is a measure of how many contracts a position will be naked long or short if the underlying market makes such a large move that either all calls or all puts act like underlying contracts."

**Upside, the extreme right tail.** "all puts will collapse to zero while all calls will eventually act like long underlying contracts."

| Upside case | Tail behavior |
|---|---|
| Long more calls than short | Angles up and to the right infinitely far: unlimited upside profit |
| Short more calls than long | Angles down and to the right infinitely far: unlimited upside risk |
| Long calls equal short calls | Flattens out: limited upside risk/reward |
| Position consists only of puts | Flattens out: limited upside risk/reward |

**Downside, the extreme left tail.** "all calls will collapse to zero while all puts will eventually act like short underlying contracts."

| Downside case | Tail behavior |
|---|---|
| Long more puts than short | Angles up and to the left infinitely far: unlimited downside profit |
| Short more puts than long | Angles down and to the left infinitely far: unlimited downside risk |
| Long puts equal short puts | Flattens out: limited downside risk/reward |
| Position consists only of calls | Flattens out: limited downside risk/reward |

Computation, both tails, including any actual underlying leg:

```
upside contract position   = (net long calls) + (actual underlying contracts)
downside contract position = (short puts counted as LONG contracts,
                              long puts counted as SHORT contracts)
                             + (actual underlying contracts)
```

Worked (Ex. 3, p364): "the 20 long calls will act like 20 long stock contracts. These will be partially offset by the actual 10 short underlying contracts, but the total will still be an upside contract position which is long 10... For each point the stock price rises, the position will gain ten points in value." Downside: "Since a short put is a long market position, our short 20 puts will act like 20 long stock contracts. These will be partially offset by the actual 10 short underlying contracts, but the total will still be a downside contract position which is long 10."

The contract position is invariant: "the contract position remains the same, regardless of the passage of time or changes in volatility."

## Sign triplet to structure name (Step 7)

| Aggregate signs | Structure it acts like | Anchor |
|---|---|---|
| -gamma, +theta, -vega | ratio vertical spread | p354 |
| +gamma, -theta, -vega | short time spread | p357 |
| -gamma, +theta, +vega | long time spread | p363 |
| +gamma, -theta, +vega | backspread | p367 |

Then refine with the contract position. Fig 17-5 is +gamma, -theta, +vega, downside contract position net short 21, upside flat, therefore "unlimited downside reward and limited upside risk/reward... the position can essentially be described as a **put backspread**." (p368)

## The three standard graphs, and four more for complex positions

| Graph | Axes | Question it answers | Figures |
|---|---|---|---|
| a. Value vs underlying price, current conditions | theoretical P&L vs underlying price | What is this position right now, where does it make and lose money, how steep and how curved? | 17-1a, 17-2a, 17-4a, 17-5a (solid line), 17-6a (current line) |
| b. Value vs underlying price at several times to expiration | one curve per time remaining, including the at expiration curve | How does the shape rotate as time passes, where does my delta flip sign, where does gamma concentrate? | 17-1b, 17-2b, 17-4b, 17-5a, 17-6a |
| c. Value vs underlying price at several volatilities | one curve per volatility | Which way does the surface shift on a vol move, and does the shape survive the move? | 17-1c and 17-2c (15/20/25/30%), 17-4c (15/20/25%), 17-5d (18/24/30%), 17-6b (plus or minus 25% relative) |

For a large or complex position, add four more, and these are what make the read diagnostic rather than decorative:

1. Delta position vs underlying price at several times (17-5b)
2. Delta position vs underlying price at several volatilities (17-5e)
3. Gamma position vs underlying price at several times (17-5c)
4. Gamma position vs underlying price at several volatilities (17-5f)

For large stock positions also add value vs interest rate (17-5g: 3/6/9/12%) and value vs dividend (17-5h: 0 / 2.00 / 4.00).

## Position implied volatility

"the position has an implied volatility of approximately 25%, the volatility at which the position approximately breaks even, showing neither profit nor loss. (We can also approximate the implied volatility of the position by dividing the total theoretical edge of 12.20 by the vega of 2.38, and adding the result to the 20% volatility we are currently using.)" (p355)

```
position implied vol ~= (total theoretical edge / position vega) + volatility currently in use
12.20 / 2.38 = 5.1  ->  20% + 5% = 25%
```

It is not constant across underlying prices: "At a stock price of 104, the position has an implied volatility of approximately 20%. At a stock price of 106, the position has an implied volatility of approximately 15%. As the stock price rises, we hope for a lower and lower volatility." (p355 to p356)

## How time and volatility rotate the position

- **Time.** "As time passes the deltas of options tend to move away from 50, with the delta of in-the-money options moving towards 100 and the delta of out-of-the-money options moving towards zero." (p354)
- **Volatility.** "deltas move away from 50 as volatility falls and towards 50 as volatility rises. If volatility falls, the position will become delta positive; if volatility rises, the position will become delta negative." (p356) And: "Falling volatility is similar to the passage of time." (p366)
- **Gamma.** "At-the-money options always have the highest gamma, and the gamma of an at-the-money option can increase rapidly as expiration approaches." (p355) Plus: "the gamma of an at-the-money option falls as volatility rises and rises as volatility falls." (p366) Both effects stack, so a low volatility market near expiration is where gamma risk explodes.

## Gamma and theta are one worry; vega is a second (p363)

> "Note that time and volatility have similar effects on an option position. But unlike time, which can only move in one direction, volatility can either rise or fall. If a trader has a positive (negative) gamma position, he will necessarily have a negative (positive) theta position. He need only worry about one or the other, either gamma or theta. But a trader can have a positive or negative gamma position and still be concerned with volatility. A positive gamma position can still be hurt by a rise in volatility (e.g., a short time spread), while a negative gamma position can still be hurt by a decline in volatility (e.g., a long time spread)."

## Worked example: the position with no recognizable category (p363 to p366)

Stock price = 98.75; Time to June expiration = 7 weeks; Volatility = 20%; Interest rate = 6%; Dividend = 0. Long 20 June 105 calls (price .75, th val 1.02, delta 25), short 20 June 95 puts (price 1.38, th val 1.12, delta -25), short 10 stock contracts. Edge = +10.60. Position totals: gamma -2.0, theta -.1560, vega -.020.

The read, in his order: edge +10.60 so the graph crosses 98.75 at 10.60 above the zero line; delta neutral so it is exactly horizontal there; near gamma neutral so no curvature; upside contract position +10 and downside contract position +10, so both tails take on a slope of +10.

Then the dynamics. As time passes the 25 and -25 deltas go to zero, so "our position will act more and more like a position which is naked short 10 stock contracts." As the stock approaches 95 "the position begins to act like a short straddle (negative gamma), and as it approaches 105 the position begins to act like a long straddle (positive gamma)."

**The theta anomaly, a finding no payoff chart produces.** Gamma is near zero but theta is -.1560. "The reason is that the sale of stock has resulted in a cash credit, a credit on which we can earn interest. As time passes the amount of interest which we expect to earn declines, so the expected profit also declines. **This would not be the case if the underlying instrument were a futures contract, since the sale of a futures contract does not result in a cash inflow, and consequently no interest can be earned. The theta of such a position would therefore be close to zero.**"

## Worked example: A COMPLEX POSITION (Figure 17-5, p367)

Stock price = 202.50; Time to June expiration = 6 weeks; Volatility = 24.0%; Interest rate = 6.00%; Dividend = 0

| June Contract | Position | Price | Th. Value | Delta | Gamma | Theta | Vega | Imp. Vol. |
|---|---|---|---|---|---|---|---|---|
| 190 call | | 15.50 | 15.50 | 82 | 1.6 | -.077 | .18 | 24.0 |
| 195 call | -23 | 11.63 | 11.80 | 72 | 2.0 | -.088 | .23 | 23.3 |
| 200 call | +55 | 8.25 | 8.63 | 61 | 2.3 | -.094 | .26 | 22.6 |
| 205 call | -35 | 5.75 | 6.06 | 49 | 2.4 | -.094 | .27 | 22.9 |
| 210 call | -20 | 4.00 | 4.08 | 37 | 2.3 | -.086 | .26 | 23.7 |
| 215 call | +41 | 2.63 | 2.63 | 27 | 2.0 | -.074 | .23 | 24.0 |
| 190 put | -42 | 1.63 | 1.70 | -18 | 1.6 | -.046 | .18 | 23.6 |
| 195 put | +85 | 2.75 | 2.95 | -28 | 2.0 | -.056 | .23 | 23.1 |
| 200 put | +8 | 4.5 | 4.76 | -39 | 2.3 | -.062 | .26 | 23.0 |
| 205 put | -18 | 6.88 | 7.15 | -51 | 2.4 | -.060 | .27 | 23.0 |
| 210 put | | 10.00 | 10.13 | -63 | 2.3 | -.052 | .26 | 23.5 |
| 215 put | -30 | 13.75 | 13.65 | -73 | 2.0 | -.039 | .23 | 24.5 |
| stock | -18 | | | 100 | | | | |

| | Stock | Calls | Puts | Delta | Gamma | Theta | Vega | P&L |
|---|---|---|---|---|---|---|---|---|
| **totals** | -18 | +18 | +3 | -277 | +50.5 | -2.244 | +6.10 | +18.82 |

Blank position cells are zero. All six totals reproduce from the leg table by the Step 3 identity.

His conclusions in order (p367 to p370):

1. "Since the position has a positive gamma, negative theta, and positive vega, it will initially act like a backspread."
2. "the downside contract position is net short 21 (short 18 stock contracts, long 3 puts) while the upside contract position is flat (short 18 stock contracts, long 18 calls). The position has unlimited downside reward and limited upside risk/reward. Based on these characteristics, the position can essentially be described as a **put backspread**."
3. Time: "as expiration approaches the position will act more and more like a long June 195/200 strangle... Consequently, as time passes the gamma of the position will become very large with the stock price between 195 and 200."
4. Volatility: "Even if we increase or decrease volatility by 20%, to 30% or 18%, the shape of the position remains essentially the same... these numbers are not as sensitive to a change in volatility as they are to the passage of time."
5. Interest rate risk: `1% x 42/365 x 202.50 = .233`, then `.233 x 18 = 4.19` per percentage point. A 6% to 4% drop costs roughly 8.38.
6. Dividend risk: `contracts x dividend`. A 2.00 dividend on 18 short stock contracts reduces the position by roughly 36.00.

**Structure name plus protective trade.** The theta remedy (p370): "Each day that passes is costing him 2.244 (the theta) in potential profit, and this number will accelerate as time passes... If he decides to take some protective action, he will have to sell some options, either calls or puts. If he considers a large move in the underlying stock a possibility, he may not want to sell calls since this will leave him net short contracts on the upside. This will probably lead him to sell off some of the puts which he is long, either the 195 or 200 puts." The rate and dividend remedy (p372): "he can eliminate most of his risk by eliminating the 18 short stock contracts... by buying back the short stock and replacing it with either deeply in-the-money options (buy deeply in-the-money puts or sell deeply in-the-money calls), or by selling synthetic stock contracts (sell calls and buy puts at the same exercise price). The former strategy would be the same as executing a **three-way**; the latter strategy would be the same as executing a **conversion**."

## The expiration versus current value trap

Natenberg demonstrates this rather than heading a section on it, so treat it as evidence from his examples rather than as a named rule. He overlays the at expiration curve against the current curve in every figure pair (17-1b, 17-2b, 17-4b, 17-5a, 17-6a), and each time the two disagree about what the position is.

- The Figure 17-5 position reads as a **put backspread** right now and as a **long June 195/200 strangle** at expiration. Same legs, two different structures.
- Fig 17-4b: the expiration curve peaks near +50 around 94, while the two weeks to expiration curve dips to about -15 near 105, a loss region the expiration curve never shows at that price.
- Fig 17-6a: the current five week curve sits around +20 near May futures 50, while the at May expiration curve plunges to roughly -95 at that same price.
- The general form in his words: "not only does the position's potential profit change as time passes, **the risks associated with the position also change**." (p354)

Practical consequence: the expiration graph gives the terminal payoff and nothing about the path. Draw the intermediate time family, never a single curve.

## Futures underlyings: what changes (p372)

> "The foregoing positions have all consisted of stock options, but delta, gamma, and vega characteristics are similar whether a trader is dealing with stock or futures options. Except for the effect of interest rates and dividends, the analyses of the positions would be essentially the same for futures options. While futures options are not subject to dividend considerations, nor are they as sensitive to changes in interest rates as stock options, there is an additional dimension to the analysis of a futures option position because the relationship between futures months is often less well defined than with stock options."

Six adjustments:

1. No dividend exposure at all.
2. Materially lower interest rate sensitivity than stock options.
3. Selling futures creates no cash credit, so a short underlying leg earns no interest and its theta collapses to roughly zero, versus -.1560 on the identical stock position (p365).
4. The inter month relationship is not well defined, so declare a spread assumption. Cost of carry is `days/365 x rate x price`, worked as `56/365 x 6% x 49.40 = .45`, the observed May/July spread, equivalently July always .92% above May. But "many markets, particularly in energy and agricultural products, are subject to supply and demand forces which often distort the cost of carry relationship between futures months. For this reason, traders often choose to assume a **fixed spread relationship**." In the example the spread between May and July futures is assumed always .45.
5. Different months carry different volatility assumptions (May 15%, July 16%) and are totaled **per month and then all months**.
6. Residual risk gets expressed in futures equivalents.

## Worked example: FUTURES OPTION POSITIONS (Figure 17-6, p372 to p380)

May futures = 49.40; Time to expiration = 5 weeks; Volatility = 15.0%; Interest = 6.00%

| Contract | Position | Price | Theoretical Value | Delta | Gamma | Theta | Vega | Implied Volatility | Implied Delta |
|---|---|---|---|---|---|---|---|---|---|
| 46 call | -28 | 3.46 | 3.44 | 93.5 | 5.1 | -.0033 | .018 | 16.03 | 92.3 |
| 47 call | | 2.56 | 2.55 | 85.8 | 9.5 | -.0067 | .033 | 15.37 | 85.3 |
| 48 call | -39 | 1.76 | 1.76 | 73.5 | 14.1 | -.0103 | .049 | 15.01 | 73.5 |
| 49 call | +36 | 1.10 | 1.12 | 57.5 | 17.0 | -.0126 | .059 | 14.68 | 57.7 |
| 50 call | +156 | .62 | .65 | 40.4 | 16.8 | -.0125 | .059 | 14.53 | 40.1 |
| 51 call | -135 | .32 | .34 | 25.2 | 13.9 | -.0104 | .049 | 14.61 | 24.6 |
| 52 call | -15 | .15 | .16 | 13.9 | 9.6 | -.0072 | .034 | 14.72 | 13.4 |
| 53 call | -60 | .07 | .07 | 6.8 | 5.7 | -.0043 | .020 | 15.15 | 7.0 |
| 54 call | | .03 | .03 | 2.9 | 2.88 | -.0022 | .010 | 15.46 | 3.3 |
| 46 put | | .08 | .06 | -5.9 | 5.1 | -.0039 | .018 | 16.05 | -7.2 |
| 47 put | -114 | .17 | .16 | -13.6 | 9.5 | -.0071 | .033 | 15.26 | -14.0 |
| 48 put | +41 | .36 | .37 | -25.9 | 14.1 | -.0105 | .049 | 14.84 | -25.7 |
| 49 put | -93 | .70 | .72 | -41.9 | 17.0 | -.0126 | .059 | 14.64 | -41.8 |
| 50 put | +36 | 1.21 | 1.24 | -59.0 | 16.8 | -.0124 | .059 | 14.42 | -59.5 |
| 51 put | | 1.91 | 1.93 | -74.2 | 13.9 | -.0101 | .049 | 14.59 | -74.8 |
| 52 put | -24 | 2.74 | 2.74 | -85.5 | 9.6 | -.0068 | .034 | 14.87 | -85.7 |
| 53 put | | 3.65 | 3.65 | -92.7 | 5.7 | -.0037 | .020 | 15.18 | -92.4 |
| 54 put | | 4.61 | 4.60 | -96.5 | 2.8 | -.0014 | .010 | 15.99 | -95.6 |
| futures | -28 | | | 100.0 | | | | | |

July futures = 49.85; Time to expiration = 13 weeks; Volatility = 16.0%; Interest = 6.00%

| Contract | Position | Price | Theoretical Value | Delta | Gamma | Theta | Vega | Implied Volatility | Implied Delta |
|---|---|---|---|---|---|---|---|---|---|
| 46 call | | 4.10 | 4.10 | 84.0 | 5.7 | -.0043 | .057 | 15.94 | 84.0 |
| 47 call | | 3.29 | 3.32 | 77.0 | 7.3 | -.0058 | .072 | 15.60 | 77.5 |
| 48 call | +15 | 2.56 | 2.62 | 68.6 | 8.7 | -.0071 | .086 | 15.35 | 69.2 |
| 49 call | | 1.93 | 2.01 | 59.2 | 9.6 | -.0080 | .095 | 15.20 | 59.5 |
| 50 call | | 1.40 | 1.49 | 49.3 | 9.9 | -.0084 | .098 | 15.03 | 49.2 |
| 51 call | -35 | .99 | 1.08 | 39.7 | 9.6 | -.0082 | .095 | 15.05 | 38.9 |
| 52 call | +90 | .67 | .76 | 30.8 | 8.8 | -.0075 | .087 | 14.98 | 29.5 |
| 53 call | -45 | .45 | .52 | 23.0 | 7.6 | -.0065 | .075 | 15.12 | 21.6 |
| 54 call | +111 | .30 | .34 | 16.6 | 6.2 | -.0054 | .062 | 15.34 | 15.5 |
| 46 put | | .31 | .31 | -14.6 | 5.7 | -.0049 | .057 | 15.99 | -14.5 |
| 47 put | -66 | .48 | .51 | -21.5 | 7.3 | -.0063 | .072 | 15.57 | -21.0 |
| 48 put | +174 | .74 | .79 | -29.9 | 8.7 | -.0074 | .086 | 15.38 | -29.3 |
| 49 put | +8 | 1.09 | 1.17 | -39.3 | 9.6 | -.0081 | .095 | 15.17 | -39.0 |
| 50 put | +28 | 1.55 | 1.64 | -49.2 | 9.9 | -.0083 | .098 | 15.05 | -49.4 |
| 51 put | -21 | 2.12 | 2.21 | -58.8 | 9.6 | -.0080 | .095 | 15.02 | -59.6 |
| 52 put | -30 | 2.79 | 2.88 | -67.7 | 8.8 | -.0072 | .087 | 15.00 | -69.0 |
| 53 put | +15 | 3.55 | 3.62 | -75.5 | 7.6 | -.0060 | .075 | 15.07 | -77.0 |
| 54 put | | 4.38 | 4.43 | -81.9 | 6.2 | -.0047 | .062 | 15.20 | -83.3 |
| futures | +6 | | | 100.0 | | | | | |

| Totals | Futures | Calls | Puts | Delta | Gamma | Theta | Vega | Theoretical P&L | Implied Delta |
|---|---|---|---|---|---|---|---|---|---|
| May | -28 | -85 | -154 | +382.5 | -1526.2 | +1.1205 | -5.357 | +3.54 | +484.4 |
| July | +6 | +136 | +108 | -635.5 | +2052.5 | -1.7545 | +20.346 | +17.34 | -726.7 |
| **All Months** | **-22** | **+51** | **-46** | **-253.0** | **+526.3** | **-.6341** | **+14.989** | **+20.89** | **+242.3** |

Book footnote: "Totals may not sum exactly due to rounding."

**The classification (p376):** "The position acts like a long straddle with the underlying close to 50, but it acts like a long time spread with the underlying close to 46 or 53. This is typical of how difficult it can sometimes be to classify complex positions. If the position is large enough, even small changes in market conditions can cause the position to change its characteristics radically."

**The tail trap (p376):** "if one were to look only at the delta and gamma, it might seem that the best thing which could happen to this trader would be a swift decline in the underlying market (negative delta, positive gamma). If, however, the decline is too violent, with the market falling five or six points, the trader will have to consider his net contract position. All calls will collapse to zero, but the net total of 46 puts which he is short will begin to act like long futures. These will be partially offset by the 22 futures which he is actually short. But the result will be a position which is net long 24 contracts, leaving the trader with unlimited downside risk. Of course, a violent upside move will never be a problem since the trader has an upside contract position which is net long 29 contracts (long 51 calls, short 22 futures)."

**Implied delta and the protective trade (p380):** here the presumed delta (-253) and implied delta (-242) barely differ, but "If the trader's volatility assumption is dramatically different than the implied volatility in the marketplace, the presumed delta position might be significantly different than the implied delta position... it is not uncommon among traders to hedge a position somewhere between the trader's own delta and the implied delta. If, for example, a trader calculated his delta position as +600, but found that the implied delta was +200, he might treat the position as if it had a delta of +400. If he wanted to get delta neutral, the trader might sell four underlying contracts."

**Spread risk in futures equivalents (p380):** "With a July delta of -635 and a May delta of +382, the trader would prefer July to go down faster than May... In futures equivalents, we might describe the position as being roughly short three July/May futures spreads, and short an additional 2 1/2 July futures."

## More than one underlying: normalize to standard deviations (p380 to p384)

Problem: "because the two stocks are trading at different prices, and because they are expected to have different volatilities, a one-point move in ABC is unlikely to be matched by a one-point move in XYZ."

Fix, weekly standard deviation = annual volatility divided by the square root of 52 (Natenberg computes it as 7.2), times the price:

```
ABC:  20% / 7.2 x 99 = 2.75
XYZ:  23% / 7.2 x 62 = 1.98

ABC 95 call:   (95 - 99)  / 2.75 = about -1.5 st. devs.
ABC 105 call:  (105 - 99) / 2.75 = about +2.2 st. devs.
XYZ 60 put:    (60 - 62)  / 1.98 = about -1   st. dev.
XYZ 65 call:   (65 - 62)  / 1.98 = about +1.5 st. devs.
```

Then plot position value against standard deviation price changes in each underlying, and switch from raw greeks to the `$delta, $gamma, $theta, $vega` sensitivities "introduced in Chapter 16" (those are defined in Chapter 16, not here). Figures 17-7b through 17-7e assume each point is worth $100.

Hard stop (p384): "If a trader had option positions in several different underlying markets, a detailed analysis of the total position would require multidimensional graphs. Even if they could be constructed, such graphs would be too complex for most traders to interpret. Under such circumstances the only practical solution is to separate positions by the underlying instrument and do an individual analysis of each market."

## Failure modes

1. **Reading only the risk sensitivities.** They "are only reliable under narrowly defined market conditions" and it is dramatic changes you must worry about (p353).
2. **Reading delta and gamma and skipping the contract position.** Fig 17-6 is the demonstration: negative delta plus positive gamma says a swift decline is the best outcome, but a five or six point decline leaves the trader net long 24 contracts with unlimited downside risk (p376).
3. **Reading only the expiration graph.** See the trap section above. Draw the intermediate time family.
4. **Assuming neutral means safe.** "a trader should not make the assumption that if he is delta neutral, gamma neutral, and vega neutral, there is nothing that can go wrong... A position is only delta neutral, or gamma neutral, or vega neutral if the theoretical pricing model is itself correct, and if all the information which the trader has fed into the model is also correct." (p367)
5. **Trusting your own delta when your vol assumption differs from the market's.** "Since no one can be sure what the right volatility is, no trader can be sure that his delta calculations are correct." Hedge between your delta and the implied delta (p380).
6. **Forgetting that gamma risk compounds near expiration in a low vol market.** ATM gamma rises as expiration approaches and rises as volatility falls, both at once (p355, p366).
7. **Treating gamma against theta as two worries while ignoring vega.** They are one worry, always opposite signed. Vega is the separate one (p363).
8. **Ignoring rate and dividend risk on a large stock position carrying an underlying leg.** 18 short stock contracts against a 2.00 dividend costs about 36.00; a two point rate drop costs about 8.38 (p370 to p372).
9. **Cutting theta with the wrong leg.** Selling calls on a position already flat on the upside "will leave him net short contracts on the upside." Check the contract position before choosing which options to sell (p370).
10. **Adding cross underlying positions in raw points.** Normalize to standard deviations and switch to dollar greeks; beyond two underlyings, analyze each market separately (p380 to p384).
11. **Assuming a cost of carry futures spread holds.** Supply and demand distort it in energy and agricultural markets. Declare a fixed spread assumption and state it (p376).

## Working checklist

```
[ ] State the market context row: underlying price, time to each expiration, volatility, rate, dividend
[ ] Tabulate every leg; underlying in contracts not shares; deltas on the 0 to 100 scale
[ ] Edge = SUM(signed qty x (theoretical value - price)); verify it reproduces the printed total
[ ] Each greek total = SUM(signed qty x per-contract greek); verify all four reproduce
[ ] Apply rule 1: does the graph cross the current price above the zero line?
[ ] Apply rule 2: sign and magnitude of delta set the slope at the current price
[ ] Apply rule 3: sign of gamma sets convex (smile) or concave (frown)
[ ] Apply rule 4: sign of theta sets whether the graph shifts up or down over time
[ ] Apply rule 5: sign of vega sets which way the graph shifts on a vol move
[ ] Compute the upside contract position: net long calls + actual underlying contracts
[ ] Compute the downside contract position: short puts as long, long puts as short, + underlying
[ ] Classify each tail into one of the four outcomes (unlimited profit / unlimited risk / flat / flat)
[ ] Read the gamma-theta-vega sign triplet against the structure table, then refine with the tails
[ ] Compute position implied vol = edge / vega + current vol; recheck it at other underlying prices
[ ] Rotate for time: deltas move away from 50; where does the structure become a different structure?
[ ] Rotate for volatility: deltas move toward 50 on a vol rise; ATM gamma rises as vol falls
[ ] Draw or visualize graph a, graph b (time family), graph c (vol family); never a lone curve
[ ] If large or complex, add delta-vs-price and gamma-vs-price at several times and several vols
[ ] If a large stock position with an underlying leg, price rate risk (1% x days/365 x price x contracts) and dividend risk (contracts x dividend)
[ ] If futures: drop dividends, drop most rate sensitivity, set short-underlying theta near zero
[ ] If futures across months: declare the spread assumption, use per-month vols, total per month and all months
[ ] If two underlyings: normalize to weekly standard deviations (vol / 7.2 x price) and use dollar greeks
[ ] If more than two underlyings: stop and analyze each market separately
[ ] Compare presumed delta to implied delta; hedge between them when they diverge
[ ] Name the structure, name the dangerous region, name the protective trade and which leg it uses
```

## Notes on the printed numbers

- **Erratum, Example 2 (diagonal acting like a short time spread, stock 100, June 7 weeks / September 20 weeks, 20% vol).** Legs: June 105 call gamma 4.3 / theta -.0308 / vega .128; September 110 call gamma 2.8 / theta -.0200 / vega .216. Printed position totals are gamma +30.0, theta -.2160, vega -.760. Gamma and theta reconcile exactly by the Step 3 identity. **Vega does not: `20 x .128 - 20 x .216 = -1.760`. Use -1.760.** [^1]
- Example 1 (ratio vertical, stock 99, 7 weeks, 20% vol): June 95 call gamma 4.3 / theta -.0344 / vega .113; June 105 call gamma 4.4 / theta -.0278 / vega .117; position totals -89.0 / +.4900 / -2.380.
- Example 3 (stock 98.75, 7 weeks, 20% vol): June 105 call gamma 4.3 / theta -.0270 / vega .114; June 95 put gamma 4.4 / theta -.0192 / vega .115; position totals -2.0 / -.1560 / -.020.

[^1]: The book prints -.760 for the Example 2 position vega. It appears to be a typo or a dropped leading digit in the scan; the leg values reconcile only to -1.760. Quote -.760 if quoting the book, use -1.760 if the number is recomputed or used downstream.

## Related

- [[natenberg-greeks-risk-profile]] defines delta, gamma, theta, vega and rho per option. This skill only aggregates them across legs and reads the totals; go there for what each one is.
- [[natenberg-volatility-spread-classification]] defines the structures this skill names (ratio vertical, backspread, time spread, straddle, strangle) and when to put them on. This skill recognizes them after the fact in a messy book.
- [[natenberg-spread-adjustments]] carries the adjustment mechanics once this skill has named the dangerous region and the leg to trade.
- [[natenberg-early-exercise]] covers the deep in the money legs that show up in the Figure 17-5 remedy (the three way and the conversion).
- `options-payoff` is the opposite direction: it takes a structure name and draws its payoff curve. Use it after this skill has named the structure, not instead of it.
- Chapter 16 defines `$delta`, `$gamma`, `$theta` and `$vega`, which the multi underlying section uses but does not define.
