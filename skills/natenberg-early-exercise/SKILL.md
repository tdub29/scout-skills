---
name: natenberg-early-exercise
description: Gives a go/no-go on exercising an American option early, stated separately for futures options and for stock options, plus an assignment and delta risk flag on any position that is short an American option. Use it for "should I exercise this call before the dividend", "will my short put get assigned", "is it ever right to exercise early", "deep in the money put, exercise or sell", "assignment risk on my conversion", "why did my American option get exercised", and "how much more is the American version worth than the European one". Returns one of three actions on a long option (hold it, exercise it, or sell it and take the underlying position yourself), the corrected non-zero delta on American conversions, reversals, boxes and jelly rolls, and a cash squeeze warning on short deep-in-the-money options. From Sheldon Natenberg, Option Volatility and Pricing, Chapter 12.
---

# Natenberg Early Exercise

## What this decides

Two questions, in Natenberg's order:

> 1. Given the opportunity, under what circumstances might a trader consider exercising an American option prior to expiration?
> 2. How much more should a trader be willing to pay for an American option over an equivalent European option?

Master condition:

> In order for early exercise to be desirable, there must be some positive cash flow which will result from early exercise, and the value of this cash must be greater than the insurance value of the option.

The output on any long in-the-money American option is always one of three actions: **hold the option**, **exercise the option**, or **sell the option and take the position in the underlying market yourself**.

**The two necessary conditions (both must hold before exercise is even a candidate):**

> 1. The option must be trading at parity.
> 2. The option must have a delta close to 100.

Condition 1: "If the option is trading at more than parity, the trader will always do better selling the option and taking a position in the underlying market himself." In practice, "if an option is deeply enough in-the-money to be an early exercise candidate, the bid/ask spread is probably so wide that for practical purposes the option is trading at parity."

Condition 2: exercising swaps the option for the underlying, so you must be sure "the option has no additional insurance value left." Read delta as probability of finishing in-the-money: "A delta close to 100 means that the underlying market has almost no chance of going through the exercise price." The 80-call illustration: underlying at 100, an 80 call available. With no chance of a fall below 80, holding the call and holding the underlying are identical. With any chance of it, prefer the call, because the call caps the loss at the premium while the long underlying loss is unlimited.

**The numeric threshold:** "With a delta above 95, many traders will at least consider early exercise... With a delta of 95 or lower, the risk is probably too great to consider early exercise. There is at least a 5% chance that the underlying market will go through the exercise price. If that happens, a trader will regret having exercised an option early, regardless of the additional benefits to be gained through early exercise."

**The exact rule under a true American model:** "an option is optimally exercised early when its theoretical value is exactly parity and its delta is exactly 100."

**The test moves with your volatility input.** At a 15% volatility the option might have a delta of 98; raise the volatility to 17% and the delta falls to 93. At 15% a trader might consider early exercise, at 17% he might not. "For this reason, options in low-volatility markets are exercised early much more often than options in high-volatility markets."

**Time remaining pulls both ways.** An option with three months left might have a delta of 92 and so not be a candidate; two months later, with the underlying unchanged, the delta might be 99. But "We can earn more interest over three months than over one month, so from this point of view a three-month option is more likely to be an early exercise candidate than a one-month option." These factors can pull in different directions.

**Which component can drive an option below parity:**

| Instrument | Decomposition | The one term that can go negative |
|---|---|---|
| Futures option | option value = intrinsic value + volatility value - interest rate value | interest rate value |
| Stock call | call value = intrinsic value + interest rate value + volatility value - dividend value | dividend value |
| Stock put | put value = intrinsic value - interest rate value + volatility value + dividend value | interest rate value |

A European option with a theoretical value less than parity has a positive theta; its value gradually rises to parity as expiration approaches.

**The rule that holds in all three cases:** "In a market where options are subject to early exercise, no option ought to be trading at less than parity."

## The test for futures options

**Settlement type is the first gate, and it is categorical.**

Under **futures-type settlement**, exercising credits the intrinsic value from the futures settlement and simultaneously debits the same amount as the option value disappears. "Since the cash credits and debits exactly offset each other, no additional interest earnings can accrue. In futures markets where the options are subject to futures-type settlement there is never any economic justification for early exercise, and early exercise can never be an optimal choice. A trader will always be better off either holding the option or selling it, rather than exercising it early."

Under **stock-type settlement**, run the cash-flow case below.

**Worked case.** Futures at 100, you own an 80 call, two months to expiration, stock-type settlement, theoretical value 20, delta 100. Interest 6%.

| Choice | Cash flow |
|---|---|
| 1. Hold the option | No change to the account. |
| 2. Exercise the option | Equivalent to buying futures at 80 while futures settles at 100, so 20 points are credited and earn interest: `20 x 2/12 x 6% = .20`. |
| 3. Sell the option and buy a futures contract | Identical to exercise if the call is exactly at intrinsic 20. Better than exercise if the call is above parity. |

If the call is at **19.50**: buying an 80 call for 19.50 is buying the futures at 99.50, so all traders would buy the call, sell the futures, and immediately exercise, for a riskless profit of **.50**, the amount below parity. That price cannot survive in an American market.

If the call is at **20.50**: sell the call, buy futures at 100, end with the same position and 20.50 credited instead of 20, "an additional profit of .50 ... as well as the slight additional interest earnings which go with it." Selling wins.

**Scale of the effect.** With a futures underlying under futures-type settlement, the carrying cost of either position is in theory zero, so there is no difference between European and American values at all. With stock-type settlement the difference is small and "only likely to show up in deeply in-the-money options. Even in this case, the difference between European and American values is often less than the minimum price increment."

## The test for stock options

### Calls: only for the dividend, only on one day

**Worked case.** Stock at 100, goes ex-dividend 2 points tomorrow, 90 call expiring in two weeks, theoretical value 10, delta 100.

| Choice | Cash flow |
|---|---|
| 1. Hold the option | Stock opens ex-dividend at 98, the at-parity option opens at 8 instead of 10, so "if we hold the option we can be certain of losing two points on our position." |
| 2. Exercise the option | Pay the 90 exercise price and discard the 10-point option value, effectively buying stock at 100. Lose 2 when the stock opens ex-dividend, receive the 2-point dividend, break even. |
| 3. Sell the option and buy stock | Identical to exercise if the call is at parity (10). At 10 1/2 you collect the dividend and capture an extra 1/2 point, which makes this the optimum choice. |

On choice 2: "Clearly, we are better off exercising the option than holding it, not because we will show some additional profit, but because we will avoid a two-point loss. We must exercise the option to ensure that we break even."

At **9 1/2** the call is below parity, which cannot persist: "all traders would buy the call, sell the stock, and immediately exercise the call. This would result in a riskless profit of 1/2 point."

Note that quoted prices already have the dividend deducted, so a 100 stock paying a 2-point dividend that opens at 98 "would be deemed to have opened unchanged."

**Timing rule:** "Since the only reason a trader would ever consider exercising a stock option call early is to receive the dividend, if a stock pays no dividend there is no reason to exercise a call early. If the stock does pay a dividend, the only time a trader ought to consider early exercise is the day before the stock goes ex-dividend. At no other time in its life is a stock option call an early exercise candidate."

**The European counterpart.** That same 90 call, two weeks to expiration, interest 8%, volatility 20%, is worth about **8 1/4** as a European option, **1 3/4 under parity**, "due to the fact that a call option, no matter how deeply in-the-money, does not carry with it the right to the dividend. Only ownership of the stock carries that right."

### Puts: for the interest on the exercise price

**Worked case.** Stock price 100, 8 weeks to expiration, volatility 20%, interest rate 8.00%, dividend 0. The 110 call is worth about .70.

```
put value = call value + exercise price - stock price - carrying costs
carrying costs on 110 at 8% for 56 days:  110 x 56/365 x 8% = 1.35
European 110 put:  .70 + 110 - 100 - 1.35 = 9.35    (vs 10 if exercised today)
```

"Since the 110 put is only worth 9.35 if we hold it to expiration, but is worth 10 points if we exercise it today, the option is apparently worth more dead (exercised) than alive (unexercised). When we exercise the 110 put we get to sell stock at 110, and we can earn interest on this 110-point credit to expiration."

**Timing rule:** "Whereas a stock option call can only be an early exercise candidate on the day prior to the stock's ex-dividend date, a stock option put can become an early exercise candidate anytime the interest which can be earned through the sale of the stock at the exercise price is sufficiently large. Determining exactly when this happens is a difficult problem, but if the stock pays a dividend it is most likely to occur on the day after the stock goes ex-dividend. Since a put is a substitute for a short stock position, one of the advantages of holding a put is to avoid paying the dividend. Hence, a trader will almost always want to hold the put through the ex-dividend date. Then, if the interest considerations are sufficient, the trader will exercise his put."

**Sub-parity arbitrage:** "In an American (early exercise) market no put option can be trading at less than parity. Otherwise there is an immediate arbitrage opportunity available by purchasing the stock, purchasing the put, and immediately exercising the put. The profit will be equal to the amount by which the put is trading at less than parity."

**But a European put can trade below parity.** With the 110 put at 9.35 theoretical (.65 under parity), the European market might be 9 1/4 to 9 1/2. A market maker will sell at 9 1/2, half a point under parity, because he can hedge by selling stock and will not have to buy it back until expiration; the interest he earns on the stock to expiration more than offsets the discount.

**European vs American put values (Figure 12-1).** Stock price 100.00, volatility 25%, interest rate 8.00%, dividend 0.

*4 weeks to expiration:*

| | BS Value | BS Delta | Cox-Ross Value | Cox-Ross Delta |
|---|---|---|---|---|
| 80 put | .00 | 0 | .00 | 0 |
| 90 put | .15 | -5.0 | .15 | -5.1 |
| 100 put | 2.46 | -45.1 | 2.51 | -46.4 |
| 110 put | 9.67 | -89.5 | 10.03 | -95.3 |
| 120 put | 19.28 | -99.4 | 20.00 | -100.0 |

*13 weeks to expiration:*

| | BS Value | BS Delta | Cox-Ross Value | Cox-Ross Delta |
|---|---|---|---|---|
| 80 put | .11 | -2.2 | .11 | -2.3 |
| 90 put | .97 | -14.3 | 1.00 | -14.9 |
| 100 put | 4.00 | -41.2 | 4.20 | -44.0 |
| 110 put | 10.00 | -70.6 | 10.71 | -78.2 |
| 120 put | 18.25 | -89.2 | 20.00 | -100.0 |

*26 weeks to expiration:*

| | BS Value | BS Delta | Cox-Ross Value | Cox-Ross Delta |
|---|---|---|---|---|
| 80 put | .46 | -5.7 | .50 | -6.1 |
| 90 put | 1.89 | -18.1 | 2.02 | -19.6 |
| 100 put | 5.11 | -37.7 | 5.55 | -42.1 |
| 110 put | 10.43 | -58.9 | 11.58 | -68.8 |
| 120 put | 17.56 | -76.4 | 20.04 | -94.8 |

The American value gaps up and the American delta runs toward -100 as the put goes deep in-the-money, and the effect grows with time to expiration.

## Note on pricing the American premium

Natenberg gives this no section head of its own; it is the answer to chapter question 2, so treat it as a note, not as a named framework.

The premium always exists: "Even an out-of-the-money option, which no one would consider exercising today, might someday go deeply enough into-the-money so that it could become an early exercise candidate. This possibility should always make an American option more valuable than a European option."

**Pseudo-American call value.** Compute the Black-Scholes value of the call twice: (1) as if the call expires the day before the stock goes ex-dividend, and (2) with its customary expiration date but using an underlying stock price equal to the current price less the expected dividend. Whichever value is greater is the pseudo-American call value. The companion pre-model kludge for futures options and stock puts was to use Black-Scholes values but raise any option with a theoretical value less than parity to exactly parity.

**Cox-Ross-Rubenstein versus Whaley.** Neither is closed form; both are loops. "The Cox-Ross-Rubenstein model may require 40 or 50 passes through the loop to reach the same degree of accuracy as the Whaley model achieves with four or five passes." Whaley is faster. Cox-Ross-Rubenstein is easier to understand, handles a lumpy one-time dividend correctly (Whaley treats the dividend as if it were a continuous interest payment over the life of the option), and can evaluate path dependent options, which Whaley cannot.

**When it is worth using an American model at all:** "American option values are most important when there is a significant difference between the carrying cost associated with the option and the carrying cost associated with the underlying contract. The greater the difference between the two carrying costs, the greater the value of early exercise." Largest for a stock or physical commodity underlying, especially for puts, where the model is worth the trouble. Also relevant in foreign exchange when the domestic and foreign interest rates differ significantly.

**Input quality outranks model choice:** "The American model may produce less error, but that will be small consolation if the incorrect inputs lead to a large trading loss."

## What early exercise does to a strategy you are short

**Delta relation:** "The delta of an American option will always be greater than the delta of an equivalent European option. The extent to which it is greater will depend on how deeply in-the-money the option is, as well as the interest considerations resulting from early exercise."

**Arbitrage strategies built from American options are not delta neutral.** Stock price 100, volatility 25%, interest rate 8.00%, dividend 0, March = 3 months, June = 6 months:

| Option | Euro Value | Euro Delta | Amer Value | Amer Delta |
|---|---|---|---|---|
| March 95 call | 9.00 | 73.7 | 9.00 | 73.7 |
| March 95 put | 2.13 | -26.3 | 2.24 | -27.8 |
| March 100 call | 5.97 | 58.8 | 5.97 | 58.8 |
| March 100 put | 4.00 | -41.2 | 4.20 | -44.0 |
| June 95 call | 11.96 | 72.7 | 11.96 | 72.7 |
| June 95 put | 3.24 | -27.3 | 3.49 | -29.9 |
| June 100 call | 9.03 | 62.3 | 9.03 | 62.3 |
| June 100 put | 5.11 | -37.7 | 5.55 | -42.1 |

With dividend 0, every call is identical European versus American; the whole American premium sits in the puts.

```
Reversal (buy call, sell put, sell stock)
European:  +58.8 + 41.2 - 100 = 0
American:  +58.8 + 44.0 - 100 = +2.8
```

"The positive delta of 2.8 reflects a slight preference for the market to rise so that the trader will avoid being assigned on the put." A reversal loses its interest earnings if the stock falls far enough that the trader is assigned on the put and has to buy the stock back; if the call value does not cover that interest loss, a profitable reversal becomes unprofitable. The conversion (sell call, buy put, buy stock) is the mirror at **2.8 deltas short**: "He wants the stock to fall so that he can exercise his put early and thereby avoid the interest costs of carrying a long stock position."

**The general warning:** "Because the desirability of early exercise, and therefore the likelihood of early exercise, can increase or decrease as the underlying market rises or falls, conversions and reversals using American options are not delta neutral. While these strategies may be unbalanced by only two or three deltas, the fact that they are often done in large size can result in an additional risk that the trader cannot afford to ignore. This also applies to boxes and jelly rolls, which are simply combinations of conversions and reversals."

**Box and jelly roll move in opposite directions.** Stock at 100, volatility 25%, interest 8.00%, dividend 0, March = 3 months, June = 6 months:

| Strategy | Euro Value | Euro Delta | Amer Value | Amer Delta |
|---|---|---|---|---|
| March 95/100 box | 4.90 | 0 | 4.99 | -1.3 |
| June 95/100 box | 4.80 | 0 | 4.99 | -1.8 |
| March/June 95 jelly roll | 1.85 | 0 | 1.71 | +1.1 |
| March/June 100 jelly roll | 1.95 | 0 | 1.71 | +1.6 |

Box: American is worth **more**. A long 95/100 box is long a 95 call and a 100 put, short a 95 put and 100 call. "The 100 put will become an early exercise candidate before the 95 put, making the American box more valuable than the same European box. The delta of the box is negative with American options because a trader who owns the box would like the market to decline so that he will be able to exercise the 100 put as quickly as possible."

Jelly roll: American is worth **less**. A long March/June 100 jelly roll is long a March 100 put and a June 100 call, short a March 100 call and a June 100 put. "The June 100 put, being a longer term option, has more potential for early exercise than the March 100 put. The delta of the jelly roll is therefore positive because there is a greater danger of being assigned on the June 100 put."

**Futures option arbitrage is much less affected.** Futures price 100, volatility 25%, interest 8.00%, March = 3 months, June = 6 months, all options under stock-type settlement:

| Option | Euro Value | Euro Delta | Amer Value | Amer Delta |
|---|---|---|---|---|
| March 95 call | 7.60 | 66.9 | 7.67 | 67.5 |
| March 95 put | 2.70 | -31.2 | 2.73 | -31.3 |
| March 100 call | 4.88 | 51.5 | 4.88 | 51.8 |
| March 100 put | 4.88 | -46.6 | 4.88 | -46.9 |
| June 95 call | 9.27 | 62.2 | 9.34 | 63.5 |
| June 95 put | 4.46 | -33.9 | 4.48 | -34.2 |
| June 100 call | 6.76 | 51.4 | 6.80 | 52.2 |
| June 100 put | 6.76 | -44.7 | 6.80 | -45.4 |

| Strategy | Euro Value | Euro Delta | Amer Value | Amer Delta |
|---|---|---|---|---|
| March 95 conversion | 4.90 | +1.9 | 4.94 | +1.2 |
| June 95 conversion | 4.81 | +3.9 | 4.86 | +2.3 |
| March 95/100 box | 4.90 | 0 | 4.94 | +.1 |
| June 95/100 box | 4.81 | 0 | 4.86 | +.1 |

"For practical purposes, unless the options are very deeply in-the-money or are very long-term, the difference between American and European values for futures options is negligible."

**Cash squeeze risk on short deep-in-the-money options.** Margin requirements set by the clearing houses usually require enough funds on hand to cover an early assignment, "But this is not always true. If he is short deeply in-the-money options, an early assignment notice may cause a cash squeeze. If this happens, he will need sufficient capital to cover the situation. Otherwise, he may be forced to liquidate some or all of the remaining position. And forced liquidations are invariably losing propositions."

**The self-test on every short leg:** "If I owned this option, would I logically exercise it now?" If yes, be prepared for assignment. "Early exercise rarely comes as a surprise. If it does, it is probably good for the trader who was assigned. If an option is exercised too early, someone has erroneously abandoned the time value or protective characteristics associated with the option. When that happens, the trader who is assigned will find that he has just received an unexpected gift."

**The three exercise-dependent plays, all of them bets that someone else fails to exercise:**

- **Dividend play.** Buy stock and sell deeply in-the-money calls as the ex-dividend date approaches. Unassigned, you break even on the stock (it falls, you collect the dividend) and profit as the deep in-the-money calls fall by the dividend. Assigned, "as he ought to be," you only break even. Profit is the dividend on each call that goes unexercised. Now viable only for a professional with very low transaction costs, and "Even then, he may find that he is assigned on the great majority of the calls he has sold."
- **Interest play.** Sell stock and simultaneously sell deeply in-the-money puts. Profit is the interest earned on the exercise price (proceeds of the stock sale plus the put sale) and accrues as long as the puts stay unexercised. "If the puts are exercised, the trader does no worse than break even."
- **Futures version** (stock-type settlement required). Buy a futures contract and sell a deeply in-the-money call, or sell a futures contract and sell a deeply in-the-money put. You earn interest only on the difference between the exercise price and the futures price, so it "will not be as profitable as a similar strategy in the stock option market, where the trader will earn interest on the exercise price."

**Deep-in-the-money vertical, the two-sided market.** Stock at 100, ex-dividend approaching, both the 80 and 85 calls deep enough to be exercise candidates. Buy the 80/85 call vertical for five points, exercise the 80 call for the dividend, hope not to be assigned on the 85. "Oddly, if both the 80 and 85 calls are early exercise candidates, the trader should also be willing to sell the 80/85 call vertical for five points. If he does so, he will exercise his 85 call in order to collect the dividend, and at the same time hope not to be assigned on the 80 call." Hence a professional might quote **5 bid / 5 ask**, intending to exercise whichever call he buys while hoping not to be assigned on the one he sells.

## Failure modes

- Exercising an option trading **above** parity. Always strictly worse than selling it and taking the underlying position yourself; you hand away the excess over intrinsic.
- Exercising on a delta below about 95. You abandon real insurance value for a small interest or dividend pickup, and the 5% or greater chance of the market crossing the strike makes you regret it "regardless of the additional benefits."
- Running the delta test off a convenient volatility. A 2-point error (15% to 17%) moved the delta from 98 to 93 and flipped the decision.
- Exercising a futures option under **futures-type settlement**. Zero economic justification, ever; the credit and debit cancel exactly.
- Exercising a stock call on any day but the day before ex-dividend, or exercising a call at all on a stock that pays no dividend.
- Exercising a put **before** the ex-dividend date. Holding through ex-div is how you avoid paying the dividend; exercise the day after if the interest justifies it.
- Assuming a European put cannot trade below parity. It can (9 1/4 to 9 1/2 against a 10-point parity) whenever the market maker can short the stock to expiration.
- Treating Black-Scholes output as an American value. It is a European model and "makes no attempt to answer this question."
- Trusting an American model's extra precision while feeding it bad volatility, interest or underlying price. Both models generate incorrect values because the inputs are incorrect.
- Booking a conversion, reversal, box or jelly roll as delta neutral because the European math says zero. It is 1 to 3 deltas off, and these are done in size.
- Getting the sign of the bias backwards. Derive it from which leg you fear being assigned on: reversal wants the market up (+2.8), conversion wants it down (-2.8), long box wants it down (-1.3 to -1.8), long jelly roll wants it up (+1.1 to +1.6).
- Pricing an American box at the European box value or an American jelly roll at the European jelly roll value. Box: American is greater or equal. Jelly roll: American is less or equal.
- Assuming clearing-house margin covers the assignment. Not always true for short deep-in-the-money options, and a cash squeeze forces liquidation.
- Running a dividend play at retail commissions, or sizing it as if you will not be assigned. The base case is assignment and break-even.
- Attempting the interest play in a futures option market and expecting the stock-market payoff. Interest accrues only on exercise price minus futures price.
- Being surprised by an assignment. Run the self-test on every short leg first.

## Working checklist

```
[ ] Is the option American? If not, stop; there is nothing to decide.
[ ] Futures option under futures-type settlement? Stop. Never exercise; hold or sell.
[ ] Condition 1: is the option trading at parity? Above parity means sell it, do not exercise.
[ ] Condition 2: is the delta close to 100? Below 95, do not exercise.
[ ] Re-run the delta at your honest volatility, not the convenient one.
[ ] Name the positive cash flow: interest on the credit (futures option, stock put) or the dividend (stock call).
[ ] Stock call: is tomorrow the ex-dividend date? If not, or if there is no dividend, do not exercise.
[ ] Stock put: is the interest on the exercise price large enough, and is ex-div behind you?
[ ] Price the third alternative: sell the option and take the underlying position. Any premium over parity means this wins.
[ ] Check for a sub-parity quote; in an American market that is a riskless arbitrage, not a bargain.
[ ] For every short American leg: "If I owned this option, would I logically exercise it now?"
[ ] Re-delta any conversion, reversal, box or jelly roll on American values; do not book it as zero.
[ ] Size short deep-ITM positions against an assignment cash squeeze, not just against margin.
[ ] Deciding whether an American model is worth it: how big is the carrying-cost differential?
```

## Related

- [[natenberg-synthetics-and-arbitrage-risk]] for the synthetic relationships underneath conversions, reversals, boxes and jelly rolls; this skill assumes them rather than restating them.
- [[natenberg-greeks-risk-profile]] for how delta is read as a probability of finishing in-the-money, which is what the delta-95 gate rests on.
- [[natenberg-position-analysis]] for re-hedging a position once the American deltas replace the European ones.
- [[natenberg-theoretical-edge]] for the price-versus-value comparison that decides whether to sell an option instead of exercising it.
