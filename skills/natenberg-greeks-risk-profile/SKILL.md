---
name: natenberg-greeks-risk-profile
description: Compute the aggregate delta, gamma, theta, vega (kappa) and rho of an arbitrary multi-leg option position, total its theoretical edge, and emit a signed diagnosis of which market changes help the position and which hurt it, plus a forward estimate of the delta after a specified underlying move. Also covers where each sensitivity is largest and how each one shifts with price, time and volatility, including the gamma/theta tradeoff that governs every position. Use when asked "what are the greeks on this position", "am I long or short gamma", "how much does this position lose per day", "what happens to my position if vol drops 2 points", "what will my delta be if the stock moves 5", "is my gamma exposure too big", or "which of these positions has the most theoretical edge". From Sheldon Natenberg, Option Volatility and Pricing, Chapter 6.
---

# Natenberg Greeks Risk Profile

## What this decides

Given a position (any mix of long and short calls, puts and underlying), produce five totals and a diagnosis: total
theoretical edge, total delta, total gamma, total theta, total vega, plus a signed statement of what the position needs
the market to do. Then answer the forward question: where the delta lands after a stated move, and how many contracts
flatten it. `options-payoff` draws payoff curves for named structures; this skill consumes a position and emits numbers
and a diagnosis, never a chart. Hedging that delta over time is [[natenberg-delta-neutral-hedging]].

## The delta

**Definition.** How an option's value changes with respect to a change in the price of the underlying. **Units:** percent
format, so a delta of 1.00 is written **100**. Calls run 0 (far out-of-the-money) to 100 (deeply in-the-money), puts 0 to
**-100**, and an underlying contract is always 100.

**Sign.** Long calls positive, short calls negative, long puts negative, short puts positive (grid in Figure 6-26). A
delta 25 call rises (falls) .25 when the underlying rises (falls) 1.00; a delta 75 call gains (loses) .45 on a .60 move;
a delta -10 put loses (gains) .05 on a .50 up (down) move. **At-the-money calls are approximately 50, at-the-money puts
approximately -50**, moving at about half the rate of the underlying.

### The three interpretations

Mathematically identical. Which one you use is a routing decision driven by the strategy. For a delta position of **+500**:

| Interpretation | Reading of +500 | Used when |
|---|---|---|
| Hedge ratio | Sell five underlying contracts to flatten | You intend to stay delta neutral |
| Theoretical or equivalent underlying position | You are in theory long five underlying contracts | You hold a view and want to keep the exposure |
| Rate of change | Position value changes at five times, or 500%, the rate of the underlying | You are sizing the P&L swing of a move |

Hedge ratio arithmetic is `100 / delta`. Delta 50: `100/50 = 2/1`, sell one underlying per two options bought. Delta 40
call: `100/40 = 5/2`. Delta -75 put: `100/75 = 4/3`, and puts are hedged by **buying** the underlying. General rule: any
hedge is delta neutral as long as all deltas add to zero, so four 50-delta calls plus ten -20-delta puts is
`(+4 x +50) + (+10 x -20) = 0`.

Equivalent-position arithmetic: each 100 deltas is one underlying contract. Ten 50-delta options is +500 deltas is five
contracts; selling 20 puts of delta -25 is also +500, since `-20 x -25 = +500`. Natenberg's caveat: an option is not a
surrogate for an underlying position, which is almost exclusively sensitive to direction. The delta is an equivalent
underlying position **only under very narrowly defined market conditions.** A fourth, approximate reading: ignoring sign,
the delta is roughly the probability of finishing in-the-money (25-delta call, about 25%), distorted by rates and
dividends, and silent on how far in-the-money the option finishes.

### How the delta changes, and two traps

Underlying moves: by the gamma. Time passes, or volatility falls: deltas move **away** from 50 (-50 for puts),
in-the-money further in and out-of-the-money further out. Volatility rises, or more time remains: all options become more
at-the-money, calls toward 50 and puts toward -50. At-the-money options near 50 hold their delta through changes in time
or volatility (the flat 100-strike line in Figures 6-11 through 6-14).

**The model's at-the-money is the forward price, not the spot.** It is the exercise price most likely to be closest to
the underlying at expiration. Rates 12%, stock $100, five months: the forward is $100 plus $5 of carry, so **the 105 call
is the 50-delta option**, not the 100.

**Delta neutrality is only as good as the volatility input.** Sell four 25-delta calls, buy one underlying, call it
neutral. Raise the volatility assumption and the call delta rises toward 50, say to 35, leaving the position 40 deltas
short having executed no trade.

## The gamma

**Definition.** The gamma, sometimes called the **curvature** of an option, is the rate at which an option's delta changes
as the price of the underlying changes. **Units:** deltas gained or lost per one point change in the underlying (in
decimal delta format, gamma is quoted the same way).

**Sign rule, the most confused point in the chapter:**

> Both calls and puts must have positive gammas. Regardless of whether we are working with calls or puts, we always add
> the gamma to the old delta as the underlying rises, and subtract the gamma from the old delta as the underlying falls.
> When a trader is long options, whether calls or puts, he has a long gamma position. When he is short options, he has a
> short gamma position.

Rationale: zero is greater than -50 in the same way that -50 is greater than -100. Worked, both gamma 5: a 50-delta call
and a -50-delta put go to 55 and -45 on a one-point rise, 45 and -55 on a one-point fall. **The gamma of an underlying
contract is zero**, since its delta is always 100.

**Where gamma is largest, and how it changes.** Greatest at-the-money, smaller as the option moves either into or
out-of-the-money (Fig 6-8). At-the-money gamma increases dramatically as expiration approaches: the 100-strike runs about
4 at 60 days and exceeds 20 inside about 5 days, while the 90 and 110 strikes decay toward 0 (Fig 6-9). Raise volatility
and in- or out-of-the-money gamma rises while at-the-money gamma falls; lower volatility (or shorten time) and the
reverse happens, the at-the-money gamma sometimes rising dramatically, from about 2 at 40% vol to over 20 at about 5% vol
on the 100 strike (Fig 6-10). Gamma must itself change, because a constant gamma continuously added would push the delta
outside 0 to 100.

**Gamma is the risk number.** A large gamma, positive or negative, indicates a high degree of risk. Worked: sell ten
30-delta calls, so `-10 x 30 = -300` deltas, about three short contracts, inside the limits of a trader who deals in lots
of five or less. Gamma is 6 per call. The market rises ten points, each call gains 60 deltas to a delta of 90, and the
position is **-900 deltas**, triple the directional risk and well beyond the stated limits. **COMEX 1985 (Volume
Investors)** is the printed case: several traders clearing through one firm built extremely large negative gamma
positions selling out-of-the-money gold options, profitable while gold was quiet and low-volatility. A violent upward
move left them, having been delta neutral, short thousands of deltas in a rising market. The losses collapsed the
clearing firm and caused a crisis in the COMEX clearing association. New traders are advised to avoid large gamma
positions, particularly negative ones.

**The delta forward estimate:**

```
new delta  ~=  current delta  +  (gamma x points moved)
```

Worked, computable with no machine: delta **+500** before the open, gamma **+100**, market expected to open **two points
higher**. Delta at the open is `500 + (100 x 2) = +700`, so flattening takes **seven** contracts sold, not five.

## The theta

**Definition.** The theta, or **time decay factor**, is the rate at which an option loses value as time passes. **Units:**
points lost per day, all else constant. Theta .05 on an option worth 2.75 today gives 2.70 tomorrow, 2.65 the day after.

**Sign convention.** Technically theta is positive, since time runs one way, but Natenberg writes it negative as a
reminder of the loss, so the option losing .05 per day has theta **-.05**. Therefore **a long option position always has
negative theta and a short option position always has positive theta**, exactly the opposite of gamma.

**Where theta is largest, and how it changes.** At-the-money options have greater thetas than in- or out-of-the-money
options with identical specifications. At-the-money theta increases as expiration approaches, so a short-term
at-the-money option always decays faster than a long-term one: the 100-strike is about 0.02 at 200 days and past 0.25
near expiration, while 90 and 110 fall toward 0 (Fig 6-17). Raise (lower) volatility and theta rises (falls), since
higher volatility means more time value and each day of no movement costs more.

### The gamma/theta tradeoff

> As a general principle, an option position will have a gamma and theta of opposite signs. Moreover, the relative size
> of the gamma and theta will correlate. A large positive gamma goes hand in hand with a large negative theta, while a
> large negative gamma goes hand in hand with a large positive theta. We saw that as expiration approaches, the gamma of
> an at-the-money option becomes increasingly large. The same is also true of the theta. As we get closer to expiration
> the rate at which an option decays begins to accelerate. If the option is exactly at-the-money, its theta at the moment
> of expiration becomes infinitely large.
>
> Every option position is a tradeoff between market movement and time decay. If price movement in the underlying
> contract will help a trader (positive gamma), the passage of time will hurt (negative theta). And vice versa. The
> trader can't have it both ways. Either he wants the market to move, or he wants it to sit still.

Just as a large negative gamma is high risk with respect to market movement, a large negative theta is high risk with
respect to the passage of time.

**The positive-theta exception set.** Under stock-type settlement the carrying cost on a deeply in-the-money futures
option (call or put) can exceed the volatility component. If so, and the option is **European**, it is worth less than
parity and rises to parity as expiration approaches, giving **positive theta**. A deeply in-the-money **European** put on
stock does the same if rates are high enough. In both cases the option must be European: **American options, where early
exercise is possible, can never be worth less than parity and so can never have positive thetas.** (Footnote case: a put
on a stock about to pay a large dividend.) Otherwise assume options lose value as time passes.

## The vega or kappa

**Naming.** No generally accepted term exists for volatility sensitivity. The trading community says **vega**; academic
literature, preferring Greek letters, often says **kappa (K)**. **Definition and units:** Point change in theoretical value per one percentage point change in volatility. **Vega is
positive for both calls and puts**, because all options gain value with rising volatility; long options carry positive
vega, short options negative. Vega .15 on an option worth 3.25 at 20% volatility gives 3.40 at 21% and 3.10 at 19%.

**Where vega is largest, and how it changes.** An at-the-money option always has a greater vega than an in- or
out-of-the-money option of the same type and expiration, so **the at-the-money option is the most sensitive in total
points**. The corollary: **the out-of-the-money option is the most sensitive in percent terms.** At 15% vol an
at-the-money and an out-of-the-money option are worth 2.00 and .50; at 20% they might be 3.00 and 1.00. Points favor the
at-the-money (1.00 vs .50), percent favors the out-of-the-money (50% vs 100%), and strategies trading unequal numbers of
options are decided on the percent basis. Vega for all options **declines as expiration approaches**, so a four-month
option is more volatility sensitive than a one-month option. Against volatility itself, at-the-money vega is relatively
constant (flat at about 0.16 across 0 to 40% in Fig 6-21), making at-the-money values easy to re-estimate across
volatility scenarios, while the 90 and 110 strikes rise from 0 to about 0.13.

**Time and volatility are interchangeable. Decreasing volatility is similar to decreasing time to expiration.** If you
cannot recall what the passage of time does to a position, ask what a volatility cut would do. Natenberg pairs Figures
6-15/6-18 (value), 6-11/6-13 (delta) and 6-9/6-10 (gamma) to make the point.

## The rho

**Definition and units.** Sensitivity of theoretical value to a change in interest rates, per one percentage point of
rate. Unlike the others, **you cannot generalize about rho**: it depends on the instrument and the settlement procedure.

| Case | Call rho | Put rho |
|---|---|---|
| Underlying and options both futures-type settlement | zero | zero |
| Options on futures, stock-type settlement | negative | negative |
| Stock options | positive | negative |

Futures-type settlement on both sides produces no cash flow from either trade, so rho must be zero. Under stock-type
settlement a rate rise raises the cost of carrying the options, so both calls and puts lose value. For stock options a
rate rise makes calls a more desirable alternative to buying the stock and puts a less desirable alternative to selling
it. Foreign currency options requiring delivery have **two** sensitivities: **rho-1** (domestic) and **rho-2** (foreign,
sometimes written phi). Intuition check for any case: ask whether a call (put) is a better or worse substitute for the
outright purchase (sale) of the underlying.

**How rho changes.** Largest for **deeply in-the-money** options, which require the greatest cash outlay, and larger the
**more time** remains. Stock-option rho is far larger in magnitude than futures-option rho, because stock trades produce
far larger cash flows: roughly 0 to -0.09 for futures options (Fig 6-22) against roughly -0.4 to +0.4 for stock options
(Fig 6-23), about a ten-times vertical scale. The chapter gives no rule for rho against changes in volatility; do not
assert one. Rates are usually the least important input, so rho takes a back seat to delta, gamma, theta and vega and
Natenberg generally disregards it in strategy analysis. Compute it, then deprioritize it.

## Position aggregation

**All these numbers are additive.** Total each greek as the sum over legs of `signed quantity x per-contract greek`, buys positive and sells negative.

```
gamma:  five bought at gamma 2.5, two sold at gamma 4.0    (+5 x 2.5) + (-2 x 4.0) = +4.5
theta:  nine bought at theta -.05, four sold at theta -.08 (+9 x -.05) + (-4 x -.08) = -.13
```

**Theoretical edge scorecard.** Same arithmetic: multiply each option's edge (the difference between its trade or
settlement price and its theoretical value) by the number of contracts and sum. The total is the position's potential
profit or loss. Sign convention: for a **long**, edge is theoretical value minus price; for a **short**, edge is price
minus theoretical value. Underlying legs contribute delta only, since an option trader assigns the underlying no
theoretical value, so they carry zero edge, zero gamma, zero theta and zero vega.

Natenberg makes **no** claim that a trader captures only a fraction of theoretical edge, and no capture percentage
appears anywhere in this material. What he shows is the Chapter 5 hedge realizing **+62.81** against a model-predicted
**+63.00**, plus the general statement that with correct inputs a trader can expect a profit or loss approximately equal
to the model's prediction. Do not invent a capture rate.

## Figures 6-26 and 6-27: the sign table and the diagnosis table

| If you are ... | Delta (hedge ratio) | Gamma (curvature) | Theta (time decay) | Vega (volatility) |
|---|---|---|---|---|
| long the underlying | positive | 0 | 0 | 0 |
| short the underlying | negative | 0 | 0 | 0 |
| long calls | positive | positive | negative | positive |
| short calls | negative | negative | positive | negative |
| long puts | negative | positive | negative | positive |
| short puts | positive | negative | positive | negative |

Figure 6-27 is the output half of the skill. Read each total off the aggregation, then read its row and state it in words.

| Your position is ... | Positive means ... | Negative means ... |
|---|---|---|
| Delta | you want the underlying to rise in price | you want the underlying to fall in price |
| Gamma | you want the underlying to move very swiftly, regardless of direction | you want the underlying to move slowly, regardless of direction |
| Theta | the passage of time will increase the value of your position | the passage of time will decrease the value of your position |
| Vega | you want volatility to rise | you want volatility to fall |
| Rho | you want interest rates to rise | you want interest rates to fall |

## Figure 6-28: the worked scorecard

Evaluation table (hypothetical futures options):

| Exercise | Call price | Call theo | Call delta | Call gamma | Call theta | Call vega | Put price | Put theo | Put delta | Put gamma | Put theta | Put vega |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 90 | 10.35 | 10.22 | 90 | 2.0 | -.009 | .07 | .46 | .35 | -9 | 2.0 | -.011 | .07 |
| 95 | 6.26 | 6.18 | 74 | 3.9 | -.020 | .13 | 1.34 | 1.25 | -25 | 3.9 | -.021 | .13 |
| 100 | 3.13 | 3.19 | 51 | 4.9 | -.026 | .16 | 3.12 | 3.19 | -48 | 4.9 | -.026 | .16 |
| 105 | 1.38 | 1.38 | 28 | 4.1 | -.022 | .14 | 6.29 | 6.31 | -70 | 4.1 | -.021 | .14 |
| 110 | .55 | .50 | 13 | 2.6 | -.014 | .08 | 10.44 | 10.36 | -86 | 2.6 | -.012 | .08 |

| # | Position | Theo edge | Delta | Gamma | Theta | Vega |
|---|---|---|---|---|---|---|
| 1 | long 20 100 calls / short 10 futures | +1.20 | +20 | +98.0 | -.520 | +3.20 |
| 2 | long 10 95 puts / short 25 90 puts | +1.85 | -25 | -11.0 | +.065 | -.45 |
| 3 | short 10 95 calls / short 15 100 puts | -.25 | -20 | -112.5 | +.590 | -3.70 |
| 4 | long 10 105 calls / short 10 110 calls | +.50 | +150 | +15.0 | -.080 | +.60 |
| 5 | short 10 95 calls / long 20 100 calls / short 10 105 calls | +2.00 | 0 | +18.0 | -.100 | +.50 |
| 6 | short 12 90 calls / long 12 90 puts / short 7 95 calls / long 10 100 puts / long 15 105 calls / long 8 110 calls / short 3 110 puts / long 12 futures | +1.34 | -204 | +96.2 | -.550 | +3.19 |

Arithmetic for position 1 (simplest) and position 6 (the general case):

```
1) Theo edge  20 x +.06 ; 0                                                              = +1.20
   Delta      +20 x +51 ; -10 x +100                                                     = +20
   Gamma      +20 x 4.9 ; 0                                                              = +98.0
   Theta      +20 x -.026 ; 0                                                            = -.520
   Vega       +20 x .16 ; 0                                                              = +3.20
6) Theo edge  12x+.13 ; 12x-.11 ; 7x+.08 ; 10x+.07 ; 15x0 ; 8x-.05 ; 3x+.08 ; 0          = +1.34
   Delta      -12x+90 ; +12x-9 ; -7x+74 ; +10x-48 ; +15x+28 ; +8x+13 ; -3x-86 ; +12x+100 = -204
   Gamma      -12x2.0 ; +12x2.0 ; -7x3.9 ; +10x4.9 ; +15x4.1 ; +8x2.6 ; -3x2.6 ; 0       = +96.2
   Theta      -12x-.009 ; +12x-.011 ; -7x-.020 ; +10x-.026 ; +15x-.022 ; +8x-.014 ; -3x-.012 ; 0 = -.550
   Vega       -12x.07 ; +12x.07 ; -7x.13 ; +10x.16 ; +15x.14 ; +8x.08 ; -3x.08 ; 0       = +3.19
```

Position 3 read through Figure 6-27 is the method in miniature: gamma -112.5 and theta +.590 says it wants the market to
sit still and time to pass, vega -3.70 says it wants volatility to fall, and edge -.25 says it is theoretically a losing
trade at these prices regardless.

## Two printed evaluation tables

The sensitivities as vendors print them, and the two sign conventions you must reconcile before summing.

**Figure 6-24. 22 May 1992, Black model. September 1992 Deutschemarks = 60.71; time to expiration 105 days; volatility
10.5%; interest rate 4.50%. Put deltas and thetas printed negative.**

| Exer | Call price | Call theo | Delta | Gamma | Theta | Vega | ImpVol | Put price | Put theo | Delta | Gamma | Theta | Vega | ImpVol |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 52 | n/a | 8.71* | 99 | .2 | 0 | 0 | n/a | .01 | 0 | 0 | .2 | 0 | .004 | 12.1 |
| 53 | n/a | 7.71* | 98 | .6 | 0 | 0 | n/a | .02 | .01 | -1 | .6 | -.0003 | .009 | 11.8 |
| 54 | n/a | 6.71* | 97 | 1.3 | 0 | 0 | n/a | .04 | .02 | -2 | 1.3 | -.0007 | .017 | 11.6 |
| 55 | n/a | 5.71* | 95 | 2.4 | 0 | 0 | n/a | .07 | .05 | -4 | 2.4 | -.0013 | .030 | 11.2 |
| 56 | 4.78 | 4.77 | 92 | 4.0 | -.0016 | .044 | 10.9 | .13 | .11 | -7 | 4.0 | -.0022 | .044 | 10.9 |
| 57 | 3.89 | 3.88 | 87 | 6.0 | -.0028 | .066 | 10.7 | .23 | .22 | -12 | 6.0 | -.0033 | .066 | 10.7 |
| 58 | 3.07 | 3.07 | 79 | 8.1 | -.0041 | .090 | 10.6 | .40 | .39 | -20 | 8.1 | -.0045 | .090 | 10.6 |
| 59 | 2.32 | 2.34 | 70 | 10.0 | -.0053 | .111 | 10.3 | .64 | .65 | -29 | 10.0 | -.0055 | .111 | 10.4 |
| 60 | 1.72 | 1.72 | 59 | 11.2 | -.0060 | .125 | 10.5 | 1.02 | 1.02 | -40 | 11.2 | -.0061 | .125 | 10.5 |
| 61 | 1.20 | 1.21 | 47 | 11.5 | -.0063 | .128 | 10.4 | 1.49 | 1.50 | -52 | 11.5 | -.0062 | .128 | 10.4 |
| 62 | .83 | .82 | 36 | 10.9 | -.0059 | .121 | 10.6 | 2.11 | 2.09 | -63 | 10.9 | -.0058 | .121 | 10.7 |
| 63 | .56 | .53 | 26 | 9.5 | -.0052 | .105 | 10.8 | 2.82 | 2.79 | -73 | 9.5 | -.0050 | .105 | 10.8 |
| 64 | .34 | .33 | 18 | 7.6 | -.0042 | .085 | 10.7 | 3.60 | 3.57 | -81 | 7.6 | -.0039 | .085 | 10.8 |
| 65 | .21 | .19 | 12 | 5.7 | -.0032 | .064 | 10.8 | 4.46 | 4.43 | -87 | 5.7 | -.0027 | .064 | 11.0 |
| 66 | .13 | .11 | 7 | 4.0 | -.0022 | .044 | 11.0 | 5.37 | 5.33 | -92 | 4.0 | -.0016 | .044 | 11.3 |
| 67 | .08 | .06 | 4 | 2.6 | -.0015 | .029 | 11.2 | n/a | 6.29* | -95 | 0 | 0 | 0 | n/a |
| 68 | .06 | .03 | 2 | 1.6 | -.0009 | .018 | 11.9 | n/a | 7.29* | -97 | 0 | 0 | 0 | n/a |

\* Using an unadjusted Black model these options would have a theoretical value less than parity. Since they are in fact
American rather than European, their values have been adjusted upward to parity. Confirming reads: gamma peaks at the 61
strike (11.5), the strike closest to the underlying 60.71; vega peaks at the same strike (.128); theta is most negative
there (-.0063); calls and puts at the same exercise price have identical gamma and vega and near-identical theta.

**Figure 6-25. 22 May 1992, Cox-Ross-Rubenstein model. General Electric = 76 5/8; time to expiration 28 days (June), 119
days (September), 210 days (December); Volatility = 20.5%; interest rate 4.50%; dividend .55 on 3 June 92, .55 on 22
September 92, .55 on 3 December 92. Put deltas and thetas printed positive, the opposite convention from Figure 6-24.**

| Exer | Call price | Call theo | Delta | Gamma | Theta | Vega | ImpVol | Put price | Put theo | Delta | Gamma | Theta | Vega | ImpVol |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jun60 | 16 3/4 | 16.69 | 100 | 0 | .006 | 0 | n/a | 1/16 | 0 | 0 | 0 | 0 | 0 | n/a |
| Jun65 | 11 3/4 | 11.70 | 100 | .1 | .008 | 0 | n/a | 1/8 | 0 | 0 | .4 | 0 | .001 | 34.5 |
| Jun70 | 6 7/8 | 6.72 | 98 | 3.2 | .012 | .009 | 28.3 | 1/4 | .10 | 6 | 3.6 | .008 | .023 | 24.9 |
| Jun75 | 2 3/8 | 2.45 | 67 | 7.9 | .037 | .073 | 19.0 | 15/16 | 1.09 | 37 | 7.7 | .026 | .079 | 18.0 |
| Jun80 | 3/8 | .47 | 20 | 6.3 | .023 | .060 | 18.3 | 4 1/8 | 4.20 | 81 | 6.1 | .014 | .056 | 18.6 |
| Jun85 | 1/16 | .04 | 3 | 2.2 | .005 | .014 | 21.7 | 8 3/4 | 8.84 | 99 | 2.0 | 0 | .009 | n/a |
| Sep70 | 8 1/4 | 7.75 | 82 | 3.1 | .017 | .112 | 22.4 | 1 1/4 | 1.04 | 19 | 3.2 | .008 | .114 | 22.6 |
| Sep75 | 4 5/8 | 4.38 | 62 | 4.2 | .019 | .168 | 20.2 | 2 7/16 | 2.73 | 40 | 4.5 | .011 | .169 | 19.3 |
| Sep80 | 2 1/4 | 2.15 | 40 | 4.2 | .017 | .166 | 19.7 | 5 1/4 | 5.54 | 64 | 4.7 | .019 | .157 | 19.5 |
| Sep85 | 7/8 | .91 | 21 | 3.3 | .011 | .125 | 19.0 | 9 | 9.34 | 85 | 3.5 | .003 | .091 | 17.7 |
| Dec70 | 8 7/8 | 8.67 | 77 | 2.7 | .017 | .171 | 21.1 | 2 3/16 | 1.80 | 25 | 2.8 | .006 | .179 | 22.0 |
| Dec75 | 6 | 5.58 | 61 | 3.4 | .018 | .216 | 21.9 | 4 | 3.70 | 41 | 3.3 | .006 | .219 | 21.4 |
| Dec80 | 3 3/8 | 3.33 | 43 | 3.4 | .015 | .221 | 20.2 | 6 3/8 | 6.44 | 58 | 3.5 | .004 | .219 | 19.8 |
| Dec85 | 1 3/4 | 1.86 | 28 | 2.9 | .013 | .190 | 19.5 | 9 3/4 | 9.97 | 74 | 3.3 | .003 | .177 | 19.0 |

**Volatility footnote (source conflict, unresolved).** The Figure 6-25 header prints **Volatility = 20.5%**, the value
reproduced above. The body text on book p120 describing the same table says the calculations are "based on a volatility
assumption of **22%**." Both appear in the book. The header value is the more likely correct one, given that the table's
own implied-volatility column clusters near 19% to 22%, but the conflict is recorded rather than resolved; if the exact
assumption matters to a calculation, flag it. Two further source footnotes: the example uses uniform volatility and
interest rates across expirations where varying them by expiration might be more reasonable, and the binomial model was
used because the quoted options are American and more likely to be exercised early. Confirming reads: vega rises with
expiration month at comparable moneyness (Jun 75 call .073, Sep 75 .168, Dec 75 .216), the printed proof that vega
declines as time to expiration shortens; gamma runs the other way (7.9, 4.2, 3.4), the printed proof that gamma increases
into expiration.

## Chapter summary table

The end-of-chapter summary as one grid, comparing options with otherwise identical specifications.

| | Delta | Gamma | Theta | Vega |
|---|---|---|---|---|
| Range or sign | 0 to 100 calls, 0 to -100 puts; ATM call ~50, ATM put ~-50 | positive for all long options, calls and puts | negative long, positive short | positive for all long options, calls and puts |
| Largest where | monotone in moneyness | ATM | ATM | ATM in points, OTM as a percent of theoretical value |
| Time passes | deltas move away from 50 and -50 | ATM gamma rises, sometimes dramatically; ITM and OTM gamma falls | ATM theta increases; short-term ATM decays faster than long-term ATM | all vegas decrease; long-term options stay more volatility sensitive |
| Volatility rises | call deltas toward 50, put deltas toward -50 | ITM and OTM gamma rises, ATM gamma falls | theta rises (more time value to lose per day) | ATM vega roughly constant, ITM and OTM vega rises |
| Volatility falls | deltas move away from 50 and -50 | ITM and OTM gamma falls, ATM gamma rises | theta falls | ATM vega roughly constant |

## Reference-level only

**Elasticity (omega, sometimes lambda), also called leverage value.** The relative percent change in an option's value per
percent change in the underlying: `elasticity = (underlying price / theoretical value) x delta`, delta in decimal format.
A 2.50 call on a 50 underlying at delta 25 gives `50/2.50 x .25 = 5`: a 2% move in the underlying produced a 10% move in
the call. Higher elasticity, more leverage. Not generally used by traders.

**Implied delta, gamma, theta and vega.** What each sensitivity would be if the implied volatility were the correct
volatility. Implied delta and implied theta appear most often on printouts, the first because some traders prefer to
hedge with it, the second because the rate at which an option's price decays is usually more useful than the rate its
theoretical value decays.

## Failure modes

1. **Giving puts a negative gamma.** Both calls and puts have positive gamma; add on a rise, subtract on a fall.
2. **Reading the delta as an equivalent underlying position and stopping there.** It can hide far larger risks.
3. **Assuming the strike nearest spot is the 50-delta option.** The model's at-the-money sits nearest the forward price.
4. **Believing you are delta neutral.** Raising the volatility assumption alone can leave a "neutral" position 40 deltas
   short with no trade executed.
5. **Judging a delta position without its gamma.** Short ten 30-delta calls is -300 deltas, -900 after a ten-point rally.
6. **Building a large negative gamma position because it has been profitable in a quiet market.** COMEX gold, 1985.
7. **Letting a small gamma become large through time or volatility change alone.** Monitor, do not just size at entry.
8. **Expecting gamma and theta to be independent.** Opposite signs, correlated magnitudes; no cheap gamma without theta.
9. **Assuming an option can never gain value with time.** Deeply in-the-money European options under stock-type
   settlement can trade below parity and carry positive theta. American options never can.
10. **Comparing vega across strikes on the wrong basis.** ATM wins on points, OTM on percent, and unequal-quantity
    strategies are decided on percent.
11. **Confusing sign conventions between vendor tables.** Figure 6-24 prints put deltas and thetas negative, 6-25 positive.
12. **Paralysis through analysis.** These numbers identify risk, they do not eliminate it; use them to decide beforehand
    which risks are acceptable.

## Working checklist

```
[ ] Establish the vendor sign convention for put deltas and thetas before summing
[ ] Per leg: signed quantity (buys +, sells -) x per-contract greek
[ ] Total delta, gamma, theta, vega; rho only where settlement/instrument makes it material (stock, long-dated, deep ITM)
[ ] Total theoretical edge: long edge = theo - price, short edge = price - theo
[ ] Underlying legs contribute delta only; gamma, theta, vega and edge are zero
[ ] Read every total through Figure 6-27 and state the diagnosis in words
[ ] Forward delta = delta + (gamma x expected move); state the flattening trade
[ ] Check gamma against the risk limit, and re-check after a time or volatility change, not just entry
[ ] Confirm which strike the model calls at-the-money (forward price, not spot)
[ ] Note the volatility assumption the deltas came from; changing it changes neutrality with no trade
```

## Related

- [[natenberg-delta-neutral-hedging]] for what to do with the delta once computed: the hedge, the adjustment cadence, and the four-part P&L attribution.
- [[natenberg-position-analysis]] for evaluating the position across price and time rather than at a single instant.
- [[natenberg-volatility-spread-classification]] for choosing which structure to build once you know the greek profile.
- [[natenberg-spread-adjustments]] for repairing a position whose gamma, theta or vega has drifted outside its limits.
