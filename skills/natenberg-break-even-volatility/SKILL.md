---
name: natenberg-break-even-volatility
description: Picks which of several profitable-looking spreads to actually trade and how large to do it. Equalize theoretical edge by adjusting size, rank the survivors on break-even implied volatility, then on underlying price break-evens and days to zero edge, then size the winner to the margin for error you can tolerate. Use when asked "which of these spreads should I do", "rank these trades", "how wrong can my vol estimate be before this loses", "what is my break-even vol on this", "how big should this position be", or "is this a good spread". Also carries the risk/reward fraction shortcut for when there is no time to graph, the rho and dividend ladder for stock options, and the liquidity veto that can kill the theoretical winner. From Sheldon Natenberg, Option Volatility and Pricing, Chapters 7 and 9.
---

# Natenberg Break-Even Volatility

## What this decides

Several candidates pass the volatility screen and all show positive theoretical edge. This picks the one
to trade and the size to trade it in. Output: a size-normalized table where every candidate carries the
same theoretical edge so the greeks are comparable; each candidate's break-even implied volatility and
the margin for error in percentage points it buys; its underlying price break-evens and days to zero
edge; and a contract count. Theoretical edge is the entry ticket; the ranking key is how wrong you can
be and still survive.

## Why spread at all (the margin-for-error argument)

**Spreading maintains profit potential but reduces short-term risk.** Chapter 7 argues it twice.
**First, theoretical edge is a long-run claim and you may not get there.** "Probability theory is only
valid over many occurrences or, in the case of options, over long periods of time," and adverse
fluctuations meanwhile may force liquidation on capital requirements, after which "there is no
guarantee that he will profit from the option's mispricing, even if he has accurately estimated all the
inputs." A spread is direction-agnostic by construction, which is what lets you hold. Carry example:
Feb gold $360, rates 9%, financing 9% x 2/12 x $360 = $5.40, so April fair value is $365.40 and the
market's $4.00 Feb/Apr spread is $1.40 too cheap. Buy April at $364, sell February at $360. February
rallying to $370 loses **$10** on the short leg, April at $375.40 gains $11.40, net **+$1.40**. Leg
counts follow from the relationship: 80 oz silver to 1 oz gold, **9 NYSE contracts to 5 S&P**.

> Two errata here. The text prints "$6 loss on the February side," which does not reconcile: short from
> $360 covered at $370 is a $10 loss, and $11.40 - $10 = $1.40, the profit Natenberg states. And the
> printed "(9 NYSE = 4 S&P 500)" contradicts its own sentence, where NYSE 220 and S&P 396 give
> 9 x 220 = 5 x 396. Use $10 and 9:5.

**Second, spreading redistributes outcomes without touching the mean.** A roulette bet with a 95 cent
expected return sells for $1.00, so the house edge is 5%.

| Distribution of the same $2,000 wagered | Casino reward | Casino risk | Casino edge |
|---|---|---|---|
| One bettor, $2,000 on one number | $2,000 | $70,000 ($72,000 payoff less $2,000) | 5% |
| Two bettors, $1,000 each on different numbers | $2,000 | $34,000 ($36,000 payoff less $2,000) | 5% |
| 38 bettors, $1,000 each on all 38 numbers | $2,000 | $0, a sure profit ($38,000 in, $36,000 out) | 5% |

Reward never moves; risk falls to zero. The mechanism is **mutual exclusivity**: "if one wins, the
other must lose," so payoffs cannot stack. **No perfect spread exists for the option trader**, so the
instruction is to "spread off his risk in as many different ways as possible," not to eliminate risk.
**Capacity is a skill, not just capital**: a floor trader long 100 T-bond calls at 2-00 ($2,000 each)
carries a $200,000 position by spreading it off against other options, futures or cash bonds, ending
with less risk "than that of a much smaller trader who does not know how to spread." **The rule inverts
on negative edge**: a bettor who knows the odds are against him should "wager the maximum amount on one
outcome, and hope that in the short run he gets lucky."

**The sizing example this skill generalizes.** Volatility estimate 13%. A CME Deutschemark call worth
1.75 trades at 2.00, delta 25. Sell four calls, buy one futures: edge = 4 x .25 = 1.00, and each CME
currency point is $1,250, so 4 x 1 carries $1,250 of edge; 40 x 10 is $12,500; 400 x 100 is $125,000.
Run the loss side at the same multiple: at 17% actual volatility those calls are worth 2.25, so
400 x 100 turns the $125,000 profit into a **$125,000 loss** (.25 x 400 calls = 100 points x $1,250).
Survive to 15%, a two-point margin, and you might do 40 x 10; push break-even volatility to 19%, a
six-point margin, and you might do 400 x 100. "No trader will survive very long if his livelihood depends
on estimating each input with 100% accuracy."

## Step 0: screen before you rank

Fix the sign of the vega bet first. In Figure 9-1 every implied volatility runs 16.87 to 18.39 against
a 15% input, so everything is overpriced and the trader wants **negative vega**: call and put ratio
verticals, short straddles and strangles, long butterflies, short time spreads. **Figure 9-1**, May
futures **49.50**, 56 days, volatility **15%**, interest **8.00%**

| Exercise | Call Price | Call Theo | Delta | Gamma | Theta | Vega | Call IV | Put Price | Put Theo | Delta | Gamma | Theta | Vega | Put IV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 48 | 2.19 | 2.02 | 70 | 11.6 | -.0083 | .066 | 17.53 | .72 | .54 | -29 | 11.6 | -.0087 | .066 | 17.70 |
| 49 | 1.56 | 1.40 | 57 | 13.3 | -.0097 | .075 | 17.08 | 1.05 | .91 | -42 | 13.3 | -.0098 | .075 | 16.87 |
| 50 | 1.07 | .92 | 44 | 13.4 | -.0099 | .076 | 16.96 | 1.59 | 1.42 | -55 | 13.4 | -.0098 | .076 | 17.30 |
| 51 | .77 | .57 | 31 | 12.1 | -.0090 | .068 | 17.89 | 2.22 | 2.06 | -68 | 12.1 | -.0087 | .068 | 17.44 |
| 52 | .53 | .33 | 21 | 9.8 | -.0073 | .055 | 18.39 | 2.99 | 2.80 | -78 | 9.8 | -.0068 | .055 | 18.24 |

July futures **50.11**, 112 days, volatility **15%**, interest **8.00%**

| Exercise | Call Price | Call Theo | Delta | Gamma | Theta | Vega | Call IV | Put Price | Put Theo | Delta | Gamma | Theta | Vega | Put IV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 48 | 3.03 | 2.82 | 70 | 8.0 | -.0056 | .092 | 17.20 | 1.00 | .76 | -28 | 8.0 | -.0060 | .092 | 17.50 |
| 49 | 2.40 | 2.20 | 61 | 8.9 | -.0064 | .103 | 16.92 | 1.34 | 1.12 | -37 | 8.9 | -.0066 | .103 | 17.14 |
| 50 | 1.88 | 1.67 | 52 | 9.3 | -.0069 | .108 | 16.92 | 1.78 | 1.57 | -46 | 9.3 | -.0069 | .108 | 16.98 |
| 51 | 1.46 | 1.24 | 42 | 9.2 | -.0069 | .106 | 17.09 | 2.33 | 2.11 | -56 | 9.2 | -.0067 | .106 | 17.11 |
| 52 | 1.12 | .89 | 34 | 8.6 | -.0065 | .100 | 17.28 | 2.98 | 2.73 | -64 | 8.6 | -.0061 | .100 | 17.44 |

## Step 1: never rank by raw theoretical edge

**Figure 9-2**, three candidates at their original sizes:

| | Legs | Delta Position | Theoretical Edge |
|---|---|---|---|
| **Spread 1** short straddle | -10 May 50 calls @ 1.07, -8 May 50 puts @ 1.59 | (-10 x +44) + (-8 x -55) = **0** | (10 x +.15) + (8 x +.17) = **+2.86** |
| **Spread 2** call ratio vertical | +10 May 51 calls @ .77, -15 May 52 calls @ .53 | (+10 x +31) + (-15 x +21) = **-5** | (10 x -.20) + (15 x +.20) = **+1.00** |
| **Spread 3** long put butterfly | +10 May 49 puts @ 1.05, -20 May 50 puts @ 1.59, +10 May 51 puts @ 2.22 | (+10 x -42) + (-20 x -55) + (+10 x -68) = **0** | (10 x -.14) + (20 x +.17) + (10 x -.16) = **+.40** |

> Erratum, Figure 9-2. Spread 2's delta and edge cells for the long May 51 calls print as duplicates of
> Spread 1's ("+10 x +44" and "10 x +.15") and do not foot to the printed -5 delta and +1.00 totals.
> Figure 9-1 gives that call a delta of 31 and an edge of .20 (price .77 against theoretical .57), and
> Figure 9-3 confirms +31 and -.20. The table above is recomputed.

If edge were the ranking key, "we could simply do each spread in bigger and bigger size to make the
theoretical edge as large as we want." Spread 2 at 50 x 75 instead of 10 x 15 shows 5.00 of edge, which
"ostensibly makes spread 2 a better strategy than spreads 1 and 3. Clearly, theoretical edge can't be
the only consideration." Edge "is only an indication of what we expect to earn if we are right."

## Step 2: equalize theoretical edge by scaling size

Triple spread 2 to **30 x 45**; increase spread 3 **sevenfold** to **70 x 140 x 70**. **Figure 9-3**:

| | Legs | Theoretical Edge | Delta Position | Gamma Position | Theta Position | Vega Position |
|---|---|---|---|---|---|---|
| **Spread 1** | -10 May 50 calls | 10 x +.15 | -10 x +44 | -10 x 13.4 | -10 x -.0099 | -10 x .076 |
| | -8 May 50 puts | 8 x +.17 | -8 x -55 | -8 x 13.4 | -8 x -.0098 | -8 x .076 |
| | | **+2.86** | **0** | **-241.2** | **+.1774** | **-1.368** |
| **Spread 2** | +30 May 51 calls | 30 x -.20 | +30 x +31 | +30 x 12.1 | +30 x -.0090 | +30 x .068 |
| | -45 May 52 calls | 45 x +.20 | -45 x +21 | -45 x 9.8 | -45 x -.0073 | -45 x .055 |
| | | **+3.00** | **-15** | **-78.0** | **+.0585** | **-.435** |
| **Spread 3** | +70 May 49 puts | 70 x -.14 | +70 x -42 | +70 x 13.3 | +70 x -.0098 | +70 x .075 |
| | -140 May 50 puts | 140 x +.17 | -140 x -55 | -140 x 13.4 | -140 x -.0098 | -140 x .076 |
| | +70 May 51 puts | 70 x -.16 | +70 x -68 | +70 x 12.1 | +70 x -.0087 | +70 x .068 |
| | | **+2.80** | **0** | **-98.0** | **+.0770** | **-.630** |

"With all three spreads having approximately the same theoretical edge, we can now focus on the risks
associated with each spread."

## Step 3: rank on break-even (implied) volatility

Simulate the spread's value at increasingly greater volatilities and graph edge against volatility.
Where the curve crosses zero is the spread's break-even or implied volatility: "the volatility which
would have to occur over the life of an option, or options, such that a position would show neither a
profit nor a loss." Traders determine it for a spread position just as they do for a single option.

| Spread | Break-even (implied) volatility | Margin for error vs the 15% estimate |
|---|---|---|
| 1 (short straddle) | about 17% | 2 percentage points |
| 2 (ratio vertical) | about 20% | 5 percentage points |
| 3 (long butterfly) | about 22% | 7 percentage points |

"The higher the implied volatility of the spread, the greater the margin for error in our volatility
estimate and, consequently, the greater the likelihood of showing a profit." Read the slope too: "the
slope of spread 1 is most severe. It loses its value very quickly as volatility increases."

**Equal averages are not equal strategies.** All three average about 2.80. Spread 1 gets there through
-3.95 at 20% volatility, -1.21 at 18%, +2.86 at the 15% estimate, +6.95 at 12%, +9.64 at 10%. "How the
end result comes about may be an equally important practical consideration." The bankroll case: +$7,000
half the time and -$5,000 the other half averages +$1,000 and is worthless to a trader with $3,000 who
draws the loss first. "No experienced trader will initiate a strategy where short-term bad luck might
terminate his trading career. This is the reason an experienced option trader will tend to avoid spread 1."

## Step 4: rank on underlying price break-evens (gamma risk)

Graph edge against underlying price. Figure 9-6, underlying at 49.50: spread 1 loses all theoretical
edge on a swift move up to **51.05** or down to **47.90**; spread 2 up to **51.75** and never on the
downside, where "in the most extreme downward move the theoretical edge of spread 2 will collapse to
approximately zero"; spread 3 up to **52.75** or down to **47.50**. No spread wins every category, so
state the tradeoff: "considering the vega and gamma risk, spread 3 seems to have the best risk
characteristics. Only when we consider the possibility of a large downward move does spread 3 not
display the best risk characteristics. In this case spread 2 comes in first." If spread 3 turns out to
be impractical to execute, "spread 2 is the clear winner" over the straddle on both vega and gamma.

## Step 5: rank on days to zero edge (theta risk)

Positive gamma has no gamma risk and pays for it in theta. **Figure 9-7**, sizes already adjusted to
roughly equal edge (each row: legs with their per-leg edge, then the position totals):

| | Legs | Theoretical Edge | Delta | Gamma | Theta | Vega |
|---|---|---|---|---|---|---|
| **Spread 4** ratio vertical | +20 July 50 calls (20 x -.21), -30 July 52 calls (30 x +.23) | **+2.70** | **+20** | **-72.0** | **+.0570** | **-.840** |
| **Spread 5** short time spread | +50 May 48 puts (50 x -.18), -50 July 48 puts (50 x +.24) | **+3.00** | **-50** | **+180.0** | **-.1350** | **-1.850** |
| **Spread 6** diagonal spread | +10 May 48 calls (10 x -.17), -20 July 52 calls (20 x +.23) | **+2.90** | **+20** | **-56.0** | **+.0470** | **-1.340** |

> Print ambiguity, Figure 9-7. Spread 5's short leg is the July 48 put, whose vega in Figure 9-1 is
> **.092**, not the **.103** printed in the vega column; on the .092 reading the vega position totals
> **-1.30**, not -1.850. The book's own p186 calculation uses **-1.850**, so -1.850 is carried here and
> in every fraction below. Every other cell in Figure 9-7 foots.

| | Break-even vol (Fig 9-8) | Underlying break-evens (Fig 9-9) | Time (Fig 9-10) |
|---|---|---|---|
| Spread 4 | about 18.1%, best vol cushion | loses all theoretical value below 46.50 or above 52.20, narrowest range | gains with time (negative gamma) |
| Spread 5 | about 17.0%, worst vol cushion | positive gamma, any large move increases value, no gamma risk | **loses all theoretical edge after about 18 days** with no movement |
| Spread 6 | about 17.2% | very little downside risk, stands an immediate up move to about 52.30 | gains with time (negative gamma) |

Routing when the categories disagree: greatest fear is rising implied volatility, choose spread 4;
greatest fear is a large move in the underlying, choose spread 5; "willing to settle for partial
protection against both," choose spread 6. A trader may give up "the extra volatility cushion offered by
spread 4 over spread 6 (18.0% vs. 17.2%) for the additional downside protection" of the latter. The 18
days is "the price one has to pay for the privilege of having a positive gamma."

## Step 6: the fraction shortcut when there is no time to graph

For when "a trader may not have the necessary computer support at his disposal, or market conditions
may be changing so rapidly that if he fails to make an immediate decision opportunity may quickly pass
him by." Construction: "the ideal risk/reward fraction would be 0 divided by infinity (zero risk,
infinite reward). But that equals 0, so that if we express the risk/reward characteristics of each
spread as a fraction, risk/reward, then in theory the spread whose fraction is closest to zero has the
best tradeoff." Denominator is theoretical edge; numerator is the one sensitivity you fear most.

```
vega / theoretical edge              gamma / theoretical edge (spread 5 skipped,
  Spread 4:   -.840 / 2.70  = -.311     positive gamma has no gamma risk)
  Spread 5:  -1.850 / 3.00  = -.617    Spread 4:  -72.0 / 2.70  = -26.7
  Spread 6:  -1.340 / 2.90  = -.462    Spread 6:  -56.0 / 2.90  = -19.3  <- best
       ^ spread 4 best on vega
```

**Size independence.** "When we divide the sensitivity of a spread by its theoretical value, the result
is independent of the size of the spread." Do spread 4 at 40 x 60 and both vega and edge double, so the
fraction is still -.311, which is why the shortcut can legitimately skip Step 2.

**It is an estimate and it can rank wrongly**, "because an option's sensitivities are only well defined
within a narrow range." First set: spread 1 = -1.368/2.86 = -.478, spread 2 = -.435/3.00 = -.145,
spread 3 = -.630/2.80 = -.225. The fraction calls spread 2 best; the graph gave spread 3 the highest
break-even volatility. "Even so, this method would have at least warned us away from spread 1."

**No time even for the fraction?** ***Straddles and strangles are the riskiest of all spreads***, buying
or selling. "It can be just as painful to lose money day after day when one buys a straddle or strangle
and the market fails to move, as it is to lose the same amount of money all at once when one sells."

## Step 7: extend the ladder to rho and dividend for stock options

Rate and dividend risk bite hardest on time spreads, "since options with different expirations react
differently to changes in these inputs." **Figure 9-11.** Stock **98 1/2**; March **56 days**, June **147 days**; ex-dividend in **28 and 119
days**; volatility **27%** both months; interest **8.00%**; expected dividend **1.25**. Implied
volatilities all sit well below 27%, so "it makes sense to look for spreads with positive vegas."

| | Exercise | Call Price | Call Theo | Delta | Gamma | Theta | Vega | Call IV | Put Price | Put Theo | Delta | Gamma | Theta | Vega | Put IV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MARCH | 95 | 5 | 5.79 | 64 | 3.6 | -.0436 | .142 | 25.0 | 2 1/4 | 2.66 | -36 | 3.6 | -.0281 | .142 | 24.1 |
| | 100 | 2 7/8 | 3.29 | 45 | 3.8 | -.0430 | .151 | 24.3 | 4 3/4 | 5.12 | -55 | 3.8 | -.0267 | .151 | 24.6 |
| | 105 | 1 3/8 | 1.69 | 28 | 3.3 | -.0350 | .128 | 24.5 | 8 1/8 | 8.47 | -72 | 3.3 | -.0180 | .128 | 24.3 |
| JUNE | 95 | 7 5/8 | 8.22 | 61 | 2.3 | -.0298 | .233 | 24.4 | 4 1/4 | 4.93 | -39 | 2.3 | -.0145 | .233 | 24.1 |
| | 100 | 5 | 5.85 | 50 | 2.4 | -.0292 | .243 | 23.5 | 6 1/2 | 7.43 | -50 | 2.4 | -.0132 | .243 | 23.2 |
| | 105 | 3 1/4 | 4.03 | 38 | 2.3 | -.0268 | .233 | 23.6 | 9 3/4 | 10.49 | -62 | 2.3 | -.0099 | .232 | 23.8 |

**Figure 9-12**, the four candidates (each row: legs, then the position totals):

| | Legs | Theoretical Edge | Delta | Gamma | Theta | Vega |
|---|---|---|---|---|---|---|
| **Spread 7** long put time spread | +25 June 95 puts (25 x +.68), -25 March 95 puts (25 x -.41) | **+6.75** | **-75** | **-32.5** | **+.3400** | **+2.275** |
| **Spread 8** long call time spread | +15 June 100 calls (15 x +.85), -15 March 100 calls (15 x -.42) | **+6.45** | **+75** | **-21.0** | **+.2070** | **+1.380** |
| **Spread 9** diagonal put spread | +15 June 95 puts (15 x +.68), -10 March 100 puts (10 x -.37) | **+6.50** | **-35** | **-3.5** | **+.0495** | **+1.985** |
| **Spread 10** diagonal call spread | +18 June 105 calls (18 x +.78), -10 March 95 calls (10 x -.79) | **+6.14** | **+44** | **+5.40** | **-.0464** | **+2.774** |

Rising rates hurt spreads 7 and 9 and help spreads 8 and 10 (Fig 9-13, edge against rates 0.00% to
12.00%). A dividend increase helps spreads 7 and 9 and hurts spreads 8 and 10 (Fig 9-14, edge against a
quarterly dividend 0.00 to 2.50), spread 7 gaining most. Filter on the input you fear, then run the
fraction ladder inside the survivors:

| Branch | Vega risk | Gamma risk |
|---|---|---|
| Rates up: spread 8 | 1.380 / 6.45 = .214, best on volatility risk | negative gamma, -21.0 |
| Rates up: spread 10 | 2.774 / 6.14 = .452 | positive gamma, +5.40 |
| Dividend up: spread 7 | 2.275 / 6.75 = .337 | -32.5 / 6.75 = -4.8 |
| Dividend up: spread 9 | 1.985 / 6.50 = .305 | -3.5 / 6.50 = -.5 |

Rates-up branch: "If volatility risk is our second concern, then spread 8 is probably best. Suppose,
however, that we are more concerned with a large move in the underlying stock. Now we can see that
spread 10 is best because its positive gamma means that a large move in the price of the underlying
stock can only work to our advantage." Dividend-up branch: "since there is not much difference in the
spreads in terms of vega risk, we might choose spread 9 since it has much less gamma risk. At the same
time, if we believe an increase in the dividend is very likely, we may prefer spread 7." And "the
interest rate is the least important of the inputs into a theoretical pricing model."

## Step 8: the practical-considerations veto

"In theory, a trader ought to be more willing to execute spread 3 than either spread 1 or 2. In the
real world, however, practical trading considerations may play a role." **Leg count**: "a three-sided
spread will probably be more difficult to execute in the marketplace, and is likely to cost more in
terms of the total width of the bid/ask." **Legging risk**: execute one leg at a time and "he will be
at risk from adverse changes in the market until the other legs have been executed." **Size against
liquidity**: equalizing edge forced the butterfly to 70 x 140 x 70, and if the May 49, 50 and 51 puts
cannot support that, "as we increase the size, the prices may become less satisfactory." **Transaction
costs**: "for a retail customer the increased size may entail significantly greater transaction costs."

## Step 9: the liquidity screen

- **Reversibility test, an entry criterion.** "An important consideration in deciding whether to enter
  into a trade is often the ease with which the trader can reverse the trade. A spread which consists of
  very liquid options is much less risky than a spread which consists of one or more illiquid options."
- **Hold-to-expiration test.** In a very illiquid market expiration may be the only exit at anything
  resembling a fair price: on nine-month options "the trader may find himself married to the position."
- **Long-term edge premium.** "A trader who does decide to take a position in long-term options ought
  to expect greater potential profit in the form of larger theoretical edge."
- **New trader against market maker.** New traders start in liquid markets where an error exits cheaply;
  the experienced market maker "will often prefer to deal in less liquid markets" for the wider bid/ask
  and greater edge per trade, conditional on keeping "his mistakes to a minimum."
- **Term and moneyness gradient.** "The most liquid options in any market are those which are short-term
  and which are either at- or slightly out-of-the-money." Further out in term or deeper in the money the
  bid/ask widens: "deeply in-the-money long-term options may not trade for weeks."
- **Check the underlying too.** "The most dangerous market in which to trade is one where both the
  options and the underlying contract are inactively traded."

**Figure 9-15**, end-of-day volume and bid/ask, S&P 500 index options (CBOE), July 9, 1993, index at
448.11. "Note the lower volume and wider bid/ask spread for back month and deeply in-the-money options,
versus front month and at- and out-of-the-money."

| Series | Bid | Ask | Width | Volume |
|---|---|---|---|---|
| July 445 call (near ATM, front month) | 4 5/8 | 4 3/4 | 1/8 | 397 |
| July 450 call (slightly OTM, front month) | 1 1/2 | 1 5/8 | 1/8 | 1,013 |
| July 440 call (slightly ITM, front month) | 8 5/8 | 8 7/8 | 1/4 | 2,532 |
| July 445 put (near ATM, front month) | 4 1/2 | 4 5/8 | 1/8 | 610 |
| August 440 call | 11 1/8 | 11 5/8 | 1/2 | 2,465 |
| September 435 put | 3 7/8 | 4 | 1/8 | 1,775 |
| September 440 call | 13 3/4 | 14 | 1/4 | 1 |
| July 430 call (deep ITM) | 18 | 18 3/4 | 3/4 | 0 |
| July 420 call (deep ITM) | 27 3/8 | 28 3/8 | 1 | 0 |
| December 420 / 425 calls (deep ITM, back month) | 35 1/2 / 29 5/8 | 36 1/2 / 30 5/8 | 1 | 0 |
| December 430 / 440 / 445 / 450 / 455 calls | no listing | asks 24 1/4, 14 7/8, others absent | n/a | 0 to 50 |
| December 455 / 460 / 465 / 470 puts | no listing | 11 3/4 / 14 5/8 / 18 1/4 / 22 1/4 | n/a | 0 |

## Step 10: size the winner to the margin for error

Invert the question: "ask not what is a reasonable margin for error, but rather ask what is the correct
size in which to do a spread given a known margin for error." Margin for error is market-relative, never
absolute: "in some cases, 5 percentage points may be an extremely large margin for error. In other
cases, five percentage points may be almost no margin for error at all." The two-sided rule: always
choose the spread with the best risk/reward characteristics, but "sometimes even the best spread will
have only a small margin for error. In such cases a trader, if he wants to make a trade, ought to do so
in small size. If, however, a trader can execute a spread with a very large margin for error, he ought
to be willing to do the spread in much larger size." Worked: volatility estimate **15%**, implied higher,
best negative-vega structure available is a **1 x 2 ratio vertical spread**.

| Spread's break-even (implied) volatility | Margin for error | Size executed |
|---|---|---|
| 16.5% | 1.5 percentage points | **5 x 10**, "he will almost certainly keep the size of his strategy small" |
| 25% | 10 percentage points | **50 x 100**, "he may have the confidence to execute the spread in much larger size" |

The 25% case carries the qualifier that does the real work: "and the trader has never seen volatility go
that high," so calibrate from a long enough history in the same market. Also "size, of course, is
relative. To a well capitalized, experienced trader even 50 x 100 may be a small trade." The governing
statement: "The size of a trader's positions should depend on the riskiness of the positions, and this in
turn depends on how much can go wrong without the strategy turning against the trader," bounded by the
need to "avoid being ruined by the periods of bad luck which will inevitably occur."

**Boundary.** `position-sizing-expectancy` owns generic expectancy-based sizing. This sizes a
volatility spread to a tolerable error in the volatility forecast, which is a different input.

## What is a good spread?

1. "Every successful option trader has had his share of disasters. What separates the successful trader
   from the unsuccessful one is the ability to survive such occurrences."
2. Outcome does not grade the choice: "maybe a similar spread, but one with less margin for error, would
   have resulted in an even greater loss, perhaps one from which the trader could not recover."
3. Completeness is impossible and undesirable: "a spread which passed every risk test would probably
   have so little theoretical edge that it wouldn't be worth doing."
4. The survivability bar: "the trader who allows himself a reasonable margin for error will find that
   even his losses will not lead to financial ruin."
5. The definition: "A good spread is not necessarily the one that shows the greatest profit when things
   go well; it may be the one which shows the least loss when things go badly. Winning trades always
   take care of themselves. Losing trades, which don't give back all the profits from the winning ones,
   are just as important."

## Failure modes

- Ranking by raw theoretical edge, which any size increase defeats; or comparing greeks across spreads
  not yet normalized to equal edge.
- Treating equal averages as equal strategies. All three average 2.80; only one hands you -3.95 at 20%.
- Reading one risk axis. Best-on-vega, best-on-upside-gamma and best-on-downside-gamma were three
  different spreads in the same example.
- Using the sensitivity/edge fraction as an answer rather than an estimate; it ranked spread 2 ahead of
  spread 3 when the graph disagreed.
- Choosing a theoretical winner that is a three-legged spread in illiquid series at the size edge
  normalization demands; or ignoring that a rate or dividend move flips a stock-option time spread.
- Sizing off edge instead of margin for error, asking "what margin is enough" instead of "what size does
  this margin justify," or doing the best available spread in normal size on a 1.5 point cushion.
- Believing spreading costs expected profit; the casino edge is 5% in all three distributions. Or
  spreading across outcomes that are not mutually exclusive, so correlated legs that lose together
  rebuild the concentrated risk profile and add costs.
- Chasing a perfect spread position, applying the casino's rule while holding negative edge (where the
  correct play flips to concentration), or judging spread selection by whether the trade won.

## Working checklist

```
[ ] Screen first: implied above or below your forecast fixes the sign of the vega bet
[ ] Scale every candidate to the SAME theoretical edge; record the multiplier
[ ] Break-even (implied) vol per candidate, minus your estimate = margin for error in points; note the
    slope of the edge-vs-vol curve, not just the crossing point
[ ] Upside and downside underlying price break-evens; days to zero edge if gamma is positive
[ ] Stock options: check rho and dividend direction BEFORE vega and gamma
[ ] No time to graph? sensitivity / theoretical edge, closest to zero wins, treated as an estimate that
    can rank wrongly. No time even for that? avoid straddles and strangles, long or short
[ ] Veto pass: leg count, legging risk, size vs series liquidity, transaction costs
[ ] Liquidity pass: can you reverse it, would you hold it to expiration if you could not, is the
    underlying liquid, and are you demanding extra edge for long-dated?
[ ] Size from margin for error, not edge: 1.5 points -> 5 x 10, 10 points -> 50 x 100; check the worst
    single outcome against capital
[ ] Grade the decision on the margin for error bought, never on whether the trade won
```

## Related

- [[natenberg-choosing-a-strategy]] for building the candidate set; this starts once two or more spreads
  already pass the volatility screen.
- [[natenberg-spread-adjustments]] for how to adjust once the position is on, including the size creep
  that silently invalidates the size set here.
- [[natenberg-volatility-forecast]] for the volatility estimate every break-even here is measured against.
- [[natenberg-greeks-risk-profile]] for the delta, gamma, theta, vega and rho definitions behind the ladder.
