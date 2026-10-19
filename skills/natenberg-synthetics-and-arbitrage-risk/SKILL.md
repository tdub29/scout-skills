---
name: natenberg-synthetics-and-arbitrage-risk
description: Prices any supposedly locked option relationship (a synthetic, a conversion, a reversal, a box, a jelly roll, a time box) against put-call parity, then audits it against the five named ways the lock fails. Produces a fair value, a cash-flow table, a locked-in profit number, and a go/no-go plus size decision. Routes here on "what is a conversion worth", "is this arbitrage really riskless", "put call parity check", "what can go wrong with a reversal", "price this box", "what is a jelly roll", "am I short the synthetic here", "pin risk", "back out the fair call price from the put", "can I fill this leg synthetically", "why is my futures conversion not delta neutral". Payoff pictures for these structures belong to `options-payoff`; early exercise belongs to `natenberg-early-exercise`. From Sheldon Natenberg, Option Volatility and Pricing, Chapter 11.
---
# Natenberg Synthetics and Arbitrage Risk
## What this decides
Given a position a trader believes is locked, this produces two things: (1) **a price**, the parity-consistent value of the relationship in the market it actually trades in (futures with futures-type settlement, futures with stock-type settlement, or stock), and therefore the edge in points versus the market in front of you; and (2) **a risk audit**, the five named ways the lock fails, each with its mechanism, its scaling with size, and its remedy.

The headline warning, verbatim (book p223):
> *"New option traders are often instructed to go into the market and concentrate on executing conversions and reversals because these strategies are riskless. Beware: **There are no riskless strategies.** There are only strategies with greater or lesser risk."*

**Scope boundary.** Natenberg's ARBITRAGE RISK section names exactly five risks. **Early exercise is not one of them.** It is deferred to Chapter 12 and appears in Chapter 11 only as two caveats (boxes used as borrowing, and the Figure 11-4 / 11-5 footnote). Do not add a sixth risk to the list below. Payoff pictures route to `options-payoff`.

**The standing habit this skill installs** (book p233): *"Whenever a trader is considering a strategy, he ought to always ask himself whether he can do better by executing some part of his strategy synthetically. Usually he won't be able to because synthetic relationships tend to be very efficient. But every now and then the trader will find that the synthetic position is slightly more favorable. Over a career of trading even small savings can add up."*

## The synthetic equivalences
**Why it works.** Long a June 100 call plus short a June 100 put: above 100 the put expires worthless and he exercises the call (buys at 100); below 100 the call expires worthless and he is assigned on the put (buys at 100). *"He will go long, either by choice ... or by force."*

**The six equivalences, print exact.** Each one carries the same constraint: *"where all options expire at the same time and have the same exercise price."*
```
synthetic long underlying  = long call  + short put
synthetic short underlying = short call + long put
synthetic long call        = long an underlying contract  + long put
synthetic short call       = short an underlying contract + short put
synthetic long put         = short an underlying contract + long call
synthetic short put        = long an underlying contract  + short call
```
Instantiated on a June futures contract (book p214):
```
synthetic long June future    = long June 100 call  + short June 100 put
synthetic short June future   = short June 100 call + long June 100 put
synthetic long June 100 call  = long June future    + long June 100 put
synthetic short June 100 call = short June future   + short June 100 put
synthetic long June 100 put   = short June future   + long June 100 call
synthetic short June 100 put  = long June future    + short June 100 call
```
Any available exercise price works. A long June 110 call plus a short June 110 put is still a synthetic long June future, but the future gets bought at **110** at expiration.

**Delta of a synthetic is approximately 100.** *"the deltas of calls and puts with the same underlying contract, expiration date, and exercise price will always add up to approximately 100"* (ignoring the call's positive and the put's negative sign). June 100 call delta 75 â†’ June 100 put delta about -25. Put delta -60 â†’ call delta about 40. But: *"interest rates, as well as the possibility of early exercise, can cause the delta of a synthetic underlying position to be slightly more or less than 100. But for most practical calculations, traders tend to look at a synthetic underlying position and mentally assign it a delta of 100."*

**The synthetic market.** Base equation, no interest and no dividends:
```
call price - put price = underlying price - exercise price
```
Figure 11-1 as the report reproduces it, underlying 102.00:

| Legs | Debit paid | At 110 | Profit |
|---|---|---|---|
| call 5.00 / put 3.00 | 2.00 | exercised call yields a +10.00 credit | **8.00**, identical to buying the underlying at 102.00 |
| call 4.90 / put 3.05 | 1.85 | exercised call yields a +10.00 credit | **8.15**, .15 better than buying at 102.00 |

> *"As long as the price of the June 100 call is exactly two points greater than the price of the June 100 put, the profit or loss resulting from a synthetic position will be identical to an actual position taken in the underlying contract at a price of 102.00."*

Rich/cheap tests as printed (book p216):
```
5.00 - 3.00 =  102.00 - 100.00   ->  2.00 = 2.00    no difference; indifferent
4.95 - 3.05 != 102.00 - 100.00   ->  1.90 != 2.00   synthetic cheaper -> go long synthetically   [errata 1]
5.15 - 2.90 != 102.00 - 100.00   ->  2.25 != 2.00   real cheaper -> buy the actual contract;
                                                    to go short, sell the synthetic at 2.25
```
Equivalent statement of balance: *"the synthetic and real markets will be the same when the time value of the call and the time value of the put are identical. ... If this is not true, there is always a synthetic position which is either too cheap or too expensive with respect to its real equivalent."*

**Put-call parity, the three-sided form** (book p216, print exact). *"This three-sided relationship is sometimes referred to as put-call parity."*
```
underlying price = call price - put price + exercise price
call price       = underlying price + put price - exercise price
put price        = call price - underlying price + exercise price
```

**Market-specific parity, which is where the money is.**

**(a) Futures options with futures-type settlement, or zero rates.** *"there is no interest component because no cash changes hands when either the futures contract or the options on that contract are traded. This is currently the procedure on many non-U.S. exchanges."*
```
call price - put price = underlying price - exercise price
```

**(b) Futures options with stock-type (cash) settlement, the U.S. norm.** *"where the carrying costs are calculated on either the difference between the futures price and the exercise price, or the difference between the call price and put price, both of which will be approximately the same."*
```
call price - put price = futures price - exercise price - carrying costs

worked: futures 102.00, r 8%, 3 months -> carry on 2 points = 2% x 2.00 = .04
a reversal done at flat parity loses .04; balance is restored at call 4.98 / put 3.01 / futures 102.01
4.98 - 3.01 = 102.01 - 100.00 - .04   ->   1.97 = 1.97

solving for a missing leg:
call price    = futures price - exercise price + put price - carrying costs = 102.00 - 100.00 + 2.75 - .04 = 4.71
put price     = call price + exercise price - futures price + carrying costs = 5.35 + 100.00 - 101.90 + .04 = 3.49
futures price = call price - put price + exercise price + carrying costs = 3.25 - 1.25 + 100.00 + .04 = 102.04
```

**(c) Stock options, full form** (book p223). *"where the carrying costs are calculated on the exercise price and the dividends are those expected prior to expiration."* (Footnote 1: *"The exact value depends on the discounted price, or present value, of the exercise price. For a more detailed explanation, see Appendix B."*)
```
call price - put price = stock price - exercise price + carrying costs - dividends

worked, no dividend: stock 103, call 6, put 3 -> 6 - 3 = 103 - 100 -> 3 = 3 seems balanced, but a conversion
creates a 100-point debit carried to expiration; at 8% for 3 months that is a 2-point cost, so a "break-even"
conversion loses two points. Balance is restored at call 7 / put 2 1/2 / stock 102 1/2:
7 - 2 1/2 = 102 1/2 - 100 + 2   ->   4 1/2 = 4 1/2

solving for a missing leg:
call price  = stock price - exercise price + put price + carrying costs - dividends = 102 - 100 + 3 1/4 + 2 - 1 1/2 = 5 3/4
put price   = call price + exercise price - stock price - carrying costs + dividends = 6 1/2 + 100 - 101 1/4 - 2 + 1 1/2 = 4 3/4
stock price = call price - put price + exercise price - carrying costs + dividends = 7 - 1 3/4 + 100 - 2 + 1 1/2 = 104 3/4
```
Add a 1 1/2 dividend received on the long stock and *"we can afford to pay up to 1 1/2 points more for the conversion and still do no worse than break even"* (sell the call for 5 1/2, or buy the put for four, or buy the stock for 104, or combine: sell call 6, buy put 3 1/2, buy stock 103 1/2).

### Using synthetics in volatility spreads
A synthetic substitution changes **how a spread gets filled and how it is written down**, not what the spread is or what it risks. Two uses.

**1. The better fill.** Futures market, March futures at 100. Target: buy 20 March 105 calls / sell 10 March 100 calls for a one-point credit. Market: March 100 call 2.70/2.90, March 105 call .85/.95.
```
sell the 100 calls at the 2.90 ask -> willing to pay .95 for the 105s:   2.90 - (2 x .95) = 1.00
buy the 105 calls at the .85 bid   -> willing to sell the 100s at 2.70:  2.70 - (2 x .85) = 1.00
```
He buys the 105 calls at .85. A **2.80 bid then appears on the March 100 put.** Because `synthetic short call = short put + short underlying`, and with the futures at 100 the carrying term is zero:
```
call price     = put price + futures price - exercise price - carrying costs
March 100 call = March 100 put + 100 - 100 - 0
March 100 call = March 100 put
```
Selling the put at 2.80 and the futures at 100.00 **sells the call synthetically at 2.80, which is .10 better** than the 2.70 he intended. Same spread, same risk, better price.

**2. Rewriting a spread into familiar form.** A call butterfly into puts:

| Contract | Synthetic equivalent |
|---|---|
| long 1 March 95 call | long 1 March 95 put / long an underlying contract |
| short 2 March 100 calls | short 2 March 100 puts / short 2 underlying contracts |
| long 1 March 105 call | long 1 March 105 put / long an underlying contract |

Underlyings cancel, leaving **long 1 March 95 put / short 2 March 100 puts / long 1 March 105 put**. Call and put butterflies at the same strikes are the same position. Likewise `long 2 March 100 calls + short an underlying contract`: rewrite one call as `long March 100 put + long underlying contract`, the underlyings cancel, and what remains is a **long straddle** (long 1 March 100 call + long 1 March 100 put).

## Conversions and reversals
**Construction** (book p218, print exact). *"As before, we assume that the call and the put have the same exercise price and expiration date."*
```
conversion  =  long underlying  + synthetic short underlying
            =  long underlying  + short call + long put
reversal    =  short underlying + synthetic long underlying
            =  short underlying + long call  + short put
```
In prose: *"A conversion involves buying the underlying instrument, whether a stock or commodity, in the underlying market, and selling the underlying instrument, synthetically, in the option market. A reversal involves selling the underlying instrument in the underlying market, and buying the underlying instrument, synthetically, in the option market."*

**The conversion cash-flow table** (book p217, the teaching artifact). Underlying 102.00, June 100 call 5.10, June 100 put 2.85; the synthetic market is 2.25 but should be 2.00.

| Transaction | Cash flow |
|---|---|
| underlying purchase | -102.00 |
| call sale | +5.10 |
| put purchase | -2.85 |
| exercise or assignment (at 100) at expiration | +100.00 |
| **total** | **+.25** |

> *"No matter what happens in the underlying market, the underlying position will do exactly .25 better than the synthetic position. The entire position will therefore show a profit of .25, regardless of movement in the underlying market."*

**The reversal mirror.** Underlying 102.00, call 4.90, put 3.05, so the synthetic is bought at 1.85 and the underlying sold at 102.00, locking in **+.15**. The table below is that arithmetic laid out in the same form; the book prints the numbers, not this table.

| Transaction | Cash flow |
|---|---|
| underlying sale | +102.00 |
| call purchase | -4.90 |
| put sale | +3.05 |
| exercise or assignment (at 100) at expiration | -100.00 |
| **total** | **+.15** |

**Which one, and why size is the trap.** *"If the synthetic is overpriced, all traders will want to execute a conversion (buy the underlying, sell the call, buy the put). If the synthetic is underpriced, all traders will want to execute a reversal (sell the underlying, buy the call, sell the put)."* Consequence: *"imbalances in the conversion/reversal market are usually small and rarely last for more than a few seconds."* Because the risk is low, traders do them **in very large size**, which is exactly what magnifies every risk below. Natenberg's analogy: buy gold in New York at $389 and sell it in London at $392, since *"an arbitrageur hopes to make a small profit on a large number of trades."* Figures 11-2 and 11-3 are cited as belonging to this section (book p217 to p228); the source report does not reproduce their contents beyond the p217 table above.

## The five ways a locked position is not locked
### 1. Interest Rate Risk
*"Whenever there is a cash flow associated with a trade, the value of the trade depends on the interest which can be earned on a credit or which must be paid to carry a debit over the life of the trade."* If part of the expected profit assumes earning 8% on a credit, a fall to 6% cuts or erases it; if it assumes paying 7% on a debit, a rise to 10% does the same.

Magnitude: *"large changes in interest rates over the limited life of most options are the exception rather than the rule. For this reason the interest rate risk associated with conversions and reversals is relatively small."* Footnote 2 bounds that to exchange-traded options out to roughly nine months: *"Long-term options with expirations of up to several years will obviously be much more sensitive to changes in interest rates."* Stock is far worse than futures on this axis: *"A stock option conversion or reversal includes the cash flow from the underlying stock, while a similar trade in the futures option market includes no such cash flow. The cash flow from a stock trade is always greater than the cash flow from an option trade since the price of stock is always greater than the price of the options."*

### 2. Execution Risk
*"Since no market participant wants to give away money, a trader is unlikely to be offered a profitable conversion or reversal all at one time. Consequently, he will have to execute one or two legs of the strategy, and hope to be able to execute the final leg(s) at a later time."* Buy the underlying and the puts, plan to sell the calls, and if call prices fall he *"may never be able to profitably complete the conversion."* Even a floor trader gets fooled: he buys the call and sells the put at good prices, then finds the underlying much lower than he thought. *"Anytime a strategy is executed one leg at a time, there is always the risk of an adverse change in prices before the strategy can be completed."*

### 3. Pin Risk
Setup: a June 100 conversion (short June 100 call, long June 100 put, long underlying). Above or below 100 at expiration there is no problem. *"But what will happen if the underlying market is exactly equal, or pinned, to the exercise price at the moment of expiration?"*

**Mechanism.** He must decide whether to exercise his put, and that depends on whether he is assigned on the call. *"Unfortunately, he won't know this until the day after expiration, when he either does or does not receive an assignment notice. But then it will be too late because the call will have expired."*

**Why at-the-money options do get exercised despite zero theoretical value.** *"Since most exchanges where options are traded include the right of exercise in the original transaction cost, it is almost always cheaper to exercise the call. Even if there is a charge for exercise, it will be less than the cost of trading the underlying contract. Anyone owning an at-the-money option, and choosing to take a long or short position at expiration, will find that it is cheaper to exercise the option than buy or sell the underlying contract."*

**Guessing is a coin flip in both directions.** Market strong on the last trading day â†’ assume assignment â†’ do not exercise the put â†’ if wrong, wake up long underlying he does not want. Market weak â†’ assume no assignment â†’ exercise the put â†’ if wrong and assigned anyway, wake up **short**. Amplification: *"conversions and reversals, because of their low risk, are usually done in large size. If the trader guesses wrong, he may find himself naked long or short not one, but several hundred underlying contracts."*

**Remedies, in Natenberg's order of preference.**
1. There is no clean fix: *"There can be no certain solution to the problem of pin risk."* Some at-the-money options get exercised, some do not.
2. Primary, do not be there: *"The practical solution is to avoid carrying conversions and reversals to expiration when there is a real possibility of expiration right at the exercise price."* With expiration approaching and the underlying near 100, *"the sensible course is to reduce the pin risk by reducing the size of the position."*
3. Liquidate at market. Works, but *"likely to be a losing proposition since the trader will be forced to trade each contract at an unfavorable price, either buying at the offer or selling at the bid."*
4. Best late option, cross with the opposite position at even money. A trader with an at-the-money conversion can be fairly certain there are traders with at-the-money reversals equally worried. *"If the trader with the conversion could find a trader with a reversal and cross positions with him, both traders would eliminate the pin risk associated with their positions. This is why, on option exchanges, one often finds traders looking for other traders who want to trade conversions or reversals at even money."* The give-up is acceptable because *"Whatever profit a trader expected to make from the conversion or reversal presumably resulted from the initial trade, not from the closing trade."*
5. Structural escape: *"Certain options, such as stock indices and Eurodollars, are settled at expiration in cash rather than with the delivery of an actual underlying contract. ... There is no pin risk associated with options which settle in this manner because no underlying position results from exercise or assignment."*

### 4. Settlement Risk in the Futures Market
*"Interest rate risk, execution risk, and pin risk are common to all markets, regardless of the underlying contract. There are, however, certain risks which are unique to a market depending on the characteristics of the underlying market."* Fair value first: June futures 102.00, 3 months, r 8%, options stock-type (cash) settled.
```
futures price - exercise price - carry on 2 points for 3 months = 102 - 100 - (2 x 3/12 x 8%) = 1.96
sell the June 100 call at 5.00, buy the put at 3.00, sell the futures at 102.00
-> the conversion is done .04 better than value -> expected profit .04
```
**The mismatch.** Futures settle futures-type (immediate cash); the options settle stock-type (paper until expiration). Futures fall to 98.00 and the synthetic short side gains four points **on paper only**, while the long futures leg produces an **immediate four-point cash debit**. *"To cover this four point debit, the trader will either have to borrow the money or take the money out of an existing, interest-bearing account. In either case there will be a loss in interest, and this interest loss will not be offset by the paper profit from the option position."* Extreme case: *"where the trader does not have access to the funds required to feed the futures position, the trader may be forced to liquidate the position. Needless to say, forced liquidations are never profitable."* It cuts both ways: futures at 106.00 gives an immediate cash credit earning interest, raising the profit above .04.

**Therefore a futures conversion is not delta neutral.**

| Option position | Delta position |
|---|---|
| short June 100 call | -60 |
| long June 100 put | -38 |
| long June futures contract | +100 |
| **total** | **+2** |

*"The two extra deltas reflect the fact that the trader would prefer the market to rise rather than fall, so that cash will flow into his account from the futures position."* Scale it: *"A trader who executes 500 conversions has a risk delta equal to 500 x +2 = +1000. This is the same as being naked long 10 futures contracts."* Sizing the gap: *"The amount by which the delta of a synthetic futures position will differ from 100 depends on the interest risk ... the general level of interest rates and the amount of time remaining to expiration. The higher the interest rate and the more time remaining to expiration, the greater the risk. ... A 10% interest rate with nine months to expiration represents a much greater risk than a 4% interest rate with one month remaining. In the former case, the deltas of a synthetic position may add up to 94, while in the latter case the deltas may add up to 99."*

**No settlement risk when both legs settle the same way.** All stock-type: no cash flows from pre-expiration price moves. All futures-type: any futures credit or debit is offset by an equal and opposite option cash flow.

### 5. Dividend Risk in the Stock Market
Stock 102 1/2, 3 months to June, r 8%, expected dividend 1 1/2.
```
stock price - exercise price + carry on 100 to expiration - expected dividends
= 102 1/2 - 100 + (100 x 3/12 x 8%) - 1 1/2 = 3
sell the June 100 call at 7 3/4, buy the put at 4 1/2, buy stock at 102 1/2
-> synthetic sold at 3 1/4 against a value of 3 -> expected profit 1/4
```
Mechanism: *"part of his profit comes from the 1 1/2 point dividend which he expects to receive when the stock goes ex-dividend."*

| Dividend outcome | Effect on the conversion | Result |
|---|---|---|
| cut in half to 3/4 | worth 3/4 less | *"his profit of 1/4 will turn into a loss of 1/2"* |
| raised to two points | worth 1/2 more | *"the trader's profit will increase from 1/4 to 3/4"* |
| multiple dividends before expiration | *"the impact of a change in the company's dividend policy can be greatly magnified"* | scales with the number of payouts |

## Boxes and jelly rolls
**Motivation: kill the underlying leg.** *"a conversion or reversal entails risk because these strategies combine a synthetic position in options with a position in the underlying contract. The risk arises because a synthetic position in options and an actual position in the underlying contract can have different characteristics, either in terms of settlement procedure, as in the futures option market, or in terms of the dividend payout, as in the stock option market. How might we eliminate this risk?"*

**First attempt: the three-way.** *"This type of position, where the underlying instrument in a conversion or reversal is replaced with a deeply in-the-money option, is known as a three-way."*
```
conversion:            short a call / long a put / long an underlying contract
three-way (variant 1): short a call / long a put / long a deeply in-the-money call
three-way (variant 2): short a call / long a put / short a deeply in-the-money put
```
Its own problem: *"If a trader sells a deeply in-the-money option to complete his three-way, he still has the risk of the market going through the exercise price. Indeed, as the underlying market moves closer and closer to the exercise price of the deeply in-the-money option, the option will act less and less like a position in the underlying contract. The combination of contracts will then act less and less like a true conversion or reversal."*

**The box: a conversion at one strike plus a reversal at another.**
```
100 conversion:  short a June 100 call / long a June 100 put  / long an underlying contract
90 reversal:     long a June 90 call   / short a June 90 put  / short an underlying contract
underlyings cancel, leaving the June 90/100 BOX:
      long a June 90 call        short a June 100 call
      short a June 90 put        long a June 100 put
```
Definition: *"A trader is long (short) the box when he is synthetically long (short) the lower exercise price and synthetically short (long) the higher exercise price."* Expiration value is exactly the amount between exercise prices: *"At expiration, regardless of the price of the underlying contract, a trader who has a box will simultaneously buy the underlying contract at one exercise price and sell the underlying contract at the other exercise price."* The June 90/100 box is worth exactly 10. Value today, under stock-type settlement, is that less carrying costs:
```
box value (today) = (higher strike - lower strike) - carrying costs = 10 - (10 x 3/12 x 8%) = 10 - .20 = 9.80
```
**A box is a loan.** *"When all options are European (there is no risk of early exercise), and the options are settled in cash rather than through delivery of the underlying contract (there is no pin risk), the purchase or sale of a box is identical to lending or borrowing funds over the life of the options."* Selling a 10-point box at 9.80 is borrowing at 8% for three months. *"If a trader were willing to pay a higher rate to borrow funds, he could sell the box at a lower price, for example 9.70. This corresponds to a rate over three months of 12%."* Use and caveat: *"When no other method is available, a trading firm might be able to raise needed short-term cash by selling boxes"*, but they sell below theoretical value, which raises the borrowing cost, *"and if the options can be exercised early, or if there is a danger of pin risk at expiration, this method of borrowing may not be without its own risks."*

**A box is also two vertical spreads.** Split it top and bottom instead of left and right: the top side is a **bull vertical call spread** (long June 90 call / short June 100 call) and the bottom side is a **bear vertical put spread** (long June 100 put / short June 90 put).
> *"Since a box is a combination of two vertical spreads, the combined prices of the vertical spreads must add up to the value of the box."*
```
call vertical price + put vertical price = box value
9.80 - 6 = 3.80      <- fair market price of the put vertical, given the call vertical trading at six
```
*"If the trader believes he can either buy or sell the call vertical spread at six points, and he is asked for a market in the put spread, he will probably make his market around an assumed value of 3.80. He might, for example, make a market of 3.50 bid/4.10 ask."* Buy the put vertical at 3.50 then the call vertical at 6.00 â†’ **paid 9.50 for a 9.80 box**. Sell the put vertical at 4.10 then the call vertical at 6.00 â†’ **sold a 9.80 box at 10.10**.

**The jelly roll: the same trick across expiration months.**
```
June reversal:         long a June 100 call  / short a June 100 put / short an underlying contract
September conversion:  short a Sept 100 call / long a Sept 100 put  / long an underlying contract
underlyings cancel, leaving the June/September 100 JELLY ROLL:
      long a June 100 call        short a September 100 call
      short a June 100 put        long a September 100 put
```
*"These combined long and short synthetic positions taken at the same exercise prices but in different expiration months is known as a jelly roll, or simply a roll. The strategy is most common in the stock option market where the underlying for both months is the same."* (Footnote 3: *"This very unscientific sounding term seems to have originated among traders on the Chicago Board Options Exchange."*)

**Value is the cost of holding the underlying between the two expirations.** Selling the June/September 100 roll means buying stock at 100 at June expiration and selling it at 100 at September expiration. The formula is book p232, print exact.
```
jelly roll = long term synthetic - short-term synthetic
           = cost of carry - expected dividends
100 x 3/12 x 8% = 2.00        <- the roll is worth two points
2 - 3/4 = 1 1/4               <- less a quarterly dividend of 3/4 received while holding the stock June to September
```
*"where the cost of carry is calculated on the exercise price over the period between expiration months."*

**A roll is the difference between two time spreads.** The same four legs are a short June/September 100 **call** time spread plus a long June/September 100 **put** time spread.
```
jelly roll = long-term synthetic - short-term synthetic
           = (long-term call - long-term put) - (short-term call - short-term put)
           = (long-term call - short-term call) - (long-term put - short-term put)
           = carrying costs - expected dividends
```
> *"The difference between the call and put time spreads should therefore be equal to the cost of carry on the exercise price less the expected dividends."*

Worked: roll worth 1 1/4, call time spread trading 3 1/4, so the put time spread should be trading **2**. Direction of the risk: *"If interest rates rise, or the dividend is cut, a jelly roll will become more valuable. If interest rates fall, or the dividend is increased, a jelly roll will become less valuable."*

**The time box: opposing synthetics at different strikes and different months.** *"The value of this position is the combined value of purchasing the June 90/100 box and selling the June/September 100 jelly roll."*
```
      long a June 90 call        short a September 100 call
      short a June 90 put        long a September 100 put
time box = box +/- jelly roll
June 90/100 box worth 9 3/4, June/September 100 roll worth 1 1/4  ->  time box = 8 1/2
```

## Reference chains: Figures 11-4 and 11-5
Two full Chapter 11 chains. Use them to check parity, box additivity (adjacent verticals must sum to the box) and roll additivity (call time spread less put time spread equals carry less dividends) against printed prices. **Figure 11-4.** Stock price = 100; March = 13 weeks, June = 26 weeks; Interest = 8.00%; Dividend = 0; Volatility = 25%. Verticals, butterflies and time spreads sit between or at the adjacent strikes. `*` marks a value that may be less than parity because European pricing is assumed.

| | 80 | 85 | 90 | 95 | 100 | 105 | 110 | 115 | 120 |
|---|---|---|---|---|---|---|---|---|---|
| March calls | 21.68 | 17.04 | 12.74 | 9.00 | 5.97 | 3.72 | 2.17 | 1.19 | .61 |
| March puts | .11 | .37 | .97 | 2.13 | 4.00 | 6.65 | 10.00 | 13.92* | 18.24* |
| March call verticals | 4.64 | 4.30 | 3.74 | 3.03 | 2.25 | 1.55 | .98 | .58 | |
| March put verticals | .26 | .60 | 1.16 | 1.87 | 2.65 | 3.35 | 3.92 | 4.32 | |
| March butterflies | | .34 | .56 | .71 | .78 | .70 | .57 | .40 | |
| March straddles | 21.79 | 17.41 | 13.71 | 11.13 | 9.97 | 10.37 | 12.17 | 15.11 | 18.85 |
| June calls | 23.57 | 19.30 | 15.40 | 11.95 | 9.02 | 6.63 | 4.74 | 3.30 | 2.25 |
| June puts | .47 | 1.00 | 1.90 | 3.25 | 5.12 | 7.53 | 10.44 | 13.80* | 17.55* |
| June call verticals | 4.27 | 3.90 | 3.45 | 2.93 | 2.39 | 1.89 | 1.44 | 1.05 | |
| June put verticals | .53 | .90 | 1.35 | 1.87 | 2.41 | 2.91 | 3.36 | 3.75 | |
| June butterflies | | .37 | .45 | .52 | .54 | .50 | .45 | .39 | |
| June straddles | 24.04 | 20.30 | 17.30 | 15.20 | 14.14 | 14.16 | 15.18 | 17.10 | 19.80* |
| Call time spreads | 1.89 | 2.26 | 2.66 | 2.95 | 3.05 | 2.91 | 2.57 | 2.11 | 1.64 |
| Put time spreads | .36 | .63 | .93 | 1.12 | 1.12 | .88 | .44 | -.12* | -.69* |

The **negative put time spreads** at the 115 and 120 strikes are the European-pricing artefact the footnote warns about, not a mispricing to trade. **Figure 11-5.** Futures price = 50 [errata 2]; May = 4 weeks, July = 12 weeks; Interest = 8.00%; Volatility = 15%.

| | 46 | 47 | 48 | 49 | 50 | 51 | 52 | 53 | 54 |
|---|---|---|---|---|---|---|---|---|---|
| May calls | 3.99* | 3.04 | 2.16 | 1.41 | .82 | .43 | .20 | .08 | .04 |
| May puts | .03 | .07 | .18 | .42 | .82 | 1.42 | 2.18 | 3.05 | 4.00 |
| May call verticals | .95 | .88 | .75 | .59 | .39 | .23 | .12 | .04 | |
| May put verticals | .04 | .11 | .24 | .40 | .60 | .76 | .87 | .95 | |
| May butterflies | | .07 | .13 | .16 | .20 | .16 | .11 | .08 | |
| May straddles | 4.02 | 3.11 [errata 3] | 2.34 | 1.83 | 1.64 | 1.85 | 2.38 | 3.13 | 4.04 |
| July calls | 4.13 | 3.32 | 2.58 | 1.94 | 1.41 | .99 | .67 | .44 | .27 |
| July puts | .21 | .38 | .62 | .96 | 1.41 | 1.97 | 2.63 | 3.38 | 4.19 |
| July call verticals | .81 | .74 | .64 | .53 | .42 | .32 | .23 | .17 | |
| July put verticals | .17 | .24 | .34 | .45 | .56 | .66 | .75 | .81 | |
| July butterflies | | .07 | .10 | .11 | .11 | .10 | .09 | .06 | |
| July straddles | 4.34 | 3.70 | 3.20 | 2.90 | 2.82 | 2.96 | 3.30 | 3.82 | 4.46 |
| Call time spreads | .14 | .28 [errata 4] | .42 | .53 | .59 | .56 | .47 | .36 | .23 |
| Put time spreads | .18 | .31 | .44 | .54 | .59 | .55 | .45 | .33 | .19 |

**Figure 11-4 / 11-5 footnote, verbatim:** *"Since all options are assumed to be European, with no early exercise permitted, some theoretical values may be less than parity and some spreads may have negative values. The effect of early exercise on spread values will be discussed in Chapter 12."* That is why the 46-strike May call sits at 3.99, **below** its 4.00 parity.

### Errata
Corrected values are printed above; the misprints are recorded here. Nothing was silently corrected and nothing wrong was silently reproduced.
1. **Rich/cheap test, book p216.** The surrounding prose says the call is at **4.90** while the printed equation reads **4.95**. The equation's arithmetic governs: `4.95 - 3.05 = 1.90` against `2.00`. The 4.90 is not an error where it appears in the Figure 11-1 and reversal examples.
2. **Figure 11-5 header.** The futures price prints as **".50"** and must be **50**, which is what every strike and premium in the table implies.
3. **Figure 11-5, 47-strike May straddle.** Prints like **2.11**; correct value **3.11** (3.04 + .07).
4. **Figure 11-5, 47-strike call time spread.** Prints like **.18**; correct value **.28** (3.32 - 3.04).
5. **Out of scope.** Two further defects flagged by the source report belong to Chapter 10 figures (the 20% row 105-call cell in Figure 10-5, and Figure 10-7's mislabelled column heads plus its 28% put values). Those are routed to the shared Chapter 10 reference, not carried here.

## Failure modes
- **Believing the sales pitch.** Conversions and reversals are *"strategies with greater or lesser risk"*, not riskless ones.
- **Doing size because the risk is low.** Pin risk, settlement delta and dividend cuts all scale linearly with size: 500 conversions is naked long 10 futures, and a wrong pin guess is several hundred naked contracts.
- **Carrying an at-the-money conversion or reversal into expiration** with the underlying near the strike. Reduce size *before* the last moment: *"If the trader doesn't reduce the size, he may find that he is under considerable pressure to get out of a large number of risky positions at the last moment."*
- **Legging in with no plan for the last leg.** That is execution risk by construction.
- **Modelling a futures conversion as delta flat.** It is +2 per conversion in the worked case.
- **Treating the expected dividend as certain**, especially with multiple dividends before expiration. Use dividends expected prior to expiration, not declared ones.
- **Mixing exercise prices or expirations** inside a synthetic. Every equivalence requires the same strike and the same expiration.
- **Assuming the synthetic delta is exactly 100.** Interest and early exercise push it off: 94 at 10% with nine months, 99 at 4% with one month.
- **Ignoring settlement type**, and forgetting that stock synthetics are far more interest sensitive than futures synthetics because the stock cash flow is always larger than the option cash flow.
- **Assuming a free lunch.** *"synthetic relationships tend to be very efficient"*, and imbalances *"rarely last for more than a few seconds."*
- **Using a three-way and forgetting it degrades.** As the market approaches the deep option's strike, the substitute stops behaving like the underlying and the conversion stops being one.
- **Pricing a box at the gross distance between strikes** and ignoring carry: 10 rather than 9.80.
- **Selling boxes as a funding source** when it is really an early-exercise plus pin-risk bet in disguise.
- **Quoting a put vertical or a put time spread without checking it against the box or roll identity.** That is the fastest source of a stale, arbitrageable quote.
- **Treating a jelly roll as dividend free.** Roll value is carry less dividends, and rising rates help a long roll while falling rates hurt it.

## Working checklist
```
[ ] Name the structure: synthetic, conversion, reversal, three-way, box, jelly roll, or time box.
[ ] Confirm same exercise price and same expiration on every synthetic pair (different months = a roll).
[ ] Pick the right parity equation for the market:
      futures-type settlement / zero rates:  call - put = underlying - exercise
      futures options, cash settled:         call - put = futures - exercise - carrying costs
      stock options:                         call - put = stock - exercise + carrying costs - dividends
[ ] Compute carry on the correct base (the strike for stock and for boxes/rolls; the 2-point difference in the
    futures example).
[ ] Subtract dividends expected prior to expiration, not declared dividends.
[ ] Price the relationship, compare to the market, state the edge in points.
[ ] Write the cash-flow table: every leg, the exercise-or-assignment line, and a total.
[ ] Before sizing, run the five risks:
      [ ] Interest rate: which side is the cash flow on, and what rate move kills the edge?
      [ ] Execution: which leg goes last, and what if it never fills?
      [ ] Pin: can the underlying finish at the strike? Cash settled or delivery?
      [ ] Settlement (futures): do both legs settle the same way? Compute the residual delta and multiply it by
          the number of conversions.
      [ ] Dividend (stock): how many dividends before expiration, and what does a cut do to the profit?
[ ] Do NOT add early exercise to this list. That is Chapter 12.
[ ] Ask the synthetic-substitution question: can any leg be filled better synthetically at the same risk?
[ ] Cross-check the quote: call vertical + put vertical = box value; call time spread - put time spread =
    carry - dividends.
[ ] At-the-money with expiration near: reduce size now, and look for the opposite position to cross at even
    money.
```

## Related
- [[natenberg-early-exercise]] owns the sixth thing that breaks a lock. Chapter 11 deliberately excludes early exercise from the arbitrage-risk list and defers it, including the Figure 11-4 / 11-5 footnote about European values below parity and negative spread values. Route any American-option assignment question there.
- [[natenberg-greeks-risk-profile]] owns delta, gamma, theta and vega as measures. This skill borrows delta only to show that a futures conversion is +2 rather than flat; reading that residual as an interest exposure lives here, computing greeks lives there.
- [[natenberg-position-analysis]] owns what a book of positions looks like once these are stacked, and the size question. Hand it the +1000 delta from 500 conversions and the pin-risk inventory going into expiration.
- [[natenberg-theoretical-edge]] owns edge measured against a model's theoretical value. This skill produces edge against a **relationship** instead, which is why it still works when no model is available.
- `options-payoff` owns "draw the payoff of a conversion / box / straddle." Route payoff pictures out; keep valuation and hidden-risk questions here.
