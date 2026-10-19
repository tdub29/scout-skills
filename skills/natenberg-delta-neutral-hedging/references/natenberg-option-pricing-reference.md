# Natenberg option pricing reference

Shared reference for the `natenberg-*` skill family. Source: Sheldon Natenberg,
*Option Volatility & Pricing: Advanced Trading Strategies and Techniques*, 2nd edition, Probus,
1994. This document holds the material from the book that did **not** earn its own skill under the
four-test carving rubric: vocabulary, distribution theory, the strategy families whose trigger
phrases already belong to `options-payoff`, the index and intermarket chapters, and the author's
own closing caution. Nothing here is a decision procedure. When a decision is needed, route to the
skill.

Family index:

| Skill | Decides |
|---|---|
| `natenberg-volatility-scaling` | annual volatility to the daily and weekly move it predicts, and the audit backwards |
| `natenberg-volatility-types` | which of the five volatilities a number is, and how to build each one |
| `natenberg-volatility-forecast` | the volatility to use next, and long-vol / short-vol / no-trade |
| `natenberg-theoretical-edge` | theoretical value from first principles, and buy / sell / no trade |
| `natenberg-delta-neutral-hedging` | the hedge, the adjustment schedule, and the break-even volatility |
| `natenberg-greeks-risk-profile` | aggregate greeks and a signed diagnosis of what helps and hurts |
| `natenberg-position-analysis` | what an unfamiliar position actually is and where it blows up |
| `natenberg-volatility-spread-classification` | which of the four gamma/vega categories a structure is |
| `natenberg-choosing-a-strategy` | the structure to use, from a view on direction and implied volatility |
| `natenberg-break-even-volatility` | which candidate spread to trade, and how big |
| `natenberg-spread-adjustments` | whether, how and how often to adjust a spread that moved |
| `natenberg-synthetics-and-arbitrage-risk` | what a locked position is worth and how the lock fails |
| `natenberg-early-exercise` | exercise now or not, and what assignment does to a short position |
| `natenberg-volatility-skew` | what a skew across strikes means and how to trade around it |
| `natenberg-model-assumptions-audit` | where a pricing model is lying to you, and in which direction |

Page-offset note for anyone returning to the scan: the PDF-to-book offset drifts from +12 at the
front of the file to +7 at the back, because pages were dropped in scanning. Locate a chapter
opener before trusting any single offset.


## 1. Contract mechanics and vocabulary (Chapter 1)

**Contract definition (book p1).** "A *call option* is the right to buy or take a *long* position in a given asset (typically a security, commodity, index, or futures contract) at a fixed price on or before a specified date. A *put option* is the right to sell or take a *short* position in a given asset." Contrast with futures: both parties to a futures contract have obligations; with an option, "all rights lie with the buyer and all obligations with the seller."

### Contract specifications

**The four identifying terms (Figure 1-1, book p3).** Underlying, Expiration Date, Exercise Price, Type. Worked both ways: *Crude Oil / October / 21 / Call* and *GE / March / 80 / Put*. Figure footnote: "If this is a futures option, the underlying is a futures contract rather than the physical commodity."

**Contract-size examples (book p2).** A crude oil October 21 call on NYMEX is the right to take a long position in one October crude oil futures contract for **1,000 barrels**, at **$21 per barrel**, on or before October expiration. A GE March 80 put on the CBOE is the right to take a short position in **100 shares** of GE stock at **$80 per share**.

**Serial options (book p2).** Options with different expiration dates sharing identical underlying futures contracts. "When there is no futures contract with the same expiration month as the option, the underlying contract for that option is the nearest futures contract after the expiration of the option." Example: with no October or November Deutschemark futures listed, the underlying for an October *or* November DM option on the CME is one **December** DM futures contract.

**Expiration dates (book p2).** Not uniform; set by each exchange. US stock options: "usually the third Saturday after the third Friday of the expiration month." Futures options need not coincide with the delivery month and can predate it by several weeks: "A crude oil option on the NYMEX will typically expire the first Saturday of the preceding month, so that an October option will actually expire the first Saturday in September."

**Flex options (book p2, footnote 1).** Exchanges "have recently introduced *flex options*, which permit the buyer and seller to negotiate both the exercise price and expiration date. These are still considered exchange traded options since the contracts are guaranteed by the exchange."

**American vs. European (book p6).** American = holder can exercise at any time prior to expiration. European = only on expiration day. "The great majority of exchange traded options throughout the world are American options... Indeed, all U.S. exchange traded stock and futures options are American." Footnote 2: because exchanges need time to process notices, "the holder of an exchange traded option must usually submit an exercise notice no later than the close of business on the day prior to expiration." Footnote 3: certain index options are European, the S&P 500 on the CBOE and the Major Market on the AMEX; "Some foreign currency options traded on the Philadelphia Stock Exchange are also European."

### Premium, moneyness, and long/short language

**Premium decomposition (book p6-7).** "An option's premium is always composed of precisely its intrinsic value and its time value." Time value is also called *time premium* or *extrinsic value*.

- Gold at **$435** per oz: the **$400 call** has intrinsic value **$35**. If that call trades at **$50**, time value is **$15**.
- A stock at **$62**: the **$70 put** has intrinsic value **$8**. If that put trades at **$9**, time value is **$1**.
- "No option can have an intrinsic value less than zero."
- *Parity* = the option's price consists solely of intrinsic value (no time value).
- A European option can have negative time value and trade below parity (deferred to Chapter 12).

**Moneyness (book p7-8).** In-the-money by the amount of the intrinsic value: with a stock at **$44**, a **$40 call is $4 in-the-money**; with Deutschemarks at **57.75**, a **59 put is 1.25 in-the-money**. Out-of-the-money = no intrinsic value, price is all time value. "If a call is in-the-money, a put with the same exercise price and underlying contract must be out-of-the-money" and vice versa. At-the-money strictly means the exercise price is identical to the current underlying price (technically also out-of-the-money, since there is no intrinsic value), but in practice for exchange-traded options it is the strike closest to the underlying: "With a stock at $74 and $5 between exercise prices ($65, $70, $75, $80, etc.), the $75 call and the $75 put would be considered the at-the-money options." The at-the-money option "has the greatest amount of time premium and is usually traded very actively." Figure 1-7 layout: lower exercise prices give in-the-money calls and out-of-the-money puts; higher exercise prices give out-of-the-money calls and in-the-money puts.

**Long/short terminology (book p11-12).** "A trader who has purchased an option is long the option, and a trader who has sold the option is short." A long call is also a **long market position**; a long put is a **short market position**: "A trader who has purchased a put wants the underlying market to decline."

### Exercise and assignment

**Book p4.** Exercising converts the option into a long underlying position (call) or short underlying position (put). "Once an option is exercised it ceases to exist, just as if it had been allowed to expire unexercised." The notice goes to the dealer (over the counter) or the guarantor (exchange); the seller is then *assigned*. Figure 1-4 chain: holder, to the buyer's clearing firm, to the clearing house, to the seller's clearing firm, to the holder of the short position, with **"Clearing house chooses a seller at random."**

### Market integrity

**The progression of responsibility (book p8-9).** Individual trader, then the trader's clearing firm, then the clearing house. "In practical terms, this means a trader must have access to capital at least equal to the option's intrinsic value." No individual may trade on an exchange without first becoming associated with a clearing firm. Once a trade is made, "the connection between the buyer and seller is severed, with the clearing house assuming the role of buyer from every seller, and seller to every buyer." Standing fact: "While individual traders and clearing firms occasionally fail, a clearing house has never failed in the United States."

**The clearing process (Figure 1-8, book p9).** Buyer and seller agree on contract, quantity, and price on the trading floor; each reports to his clearing firm; each firm reports to the clearing house. "If reports from both clearing firms match, the trade becomes official. If the reports do not match, they are returned to each clearing firm, and from there to the individual traders for rectification."

### Margin requirements

Margin is "good faith capital" and may be posted as cash, government treasury instruments, or, less commonly, commercial securities. Interest on margin deposits belongs in theory to the trader; some clearing firms keep it as part of their clearing fee, which "should be settled before an individual begins to trade."

Option margin is not fixed the way futures margin is: it "can change over time since the margin for an option often depends on the amount by which it is in- or out-of-the-money." Combination positions may get reduced margin because one contract's risk offsets another's; exchange members may get reduced professional margin. Footnote 4: professional trader margin in an equity option market is called a ***haircut***.

### Settlement procedures: stock-type vs. futures-type (book p10-11)

This is the trap that silently changes the economics of a hedge.

**Stock-type settlement.** Purchase requires full and immediate payment; profits or losses are unrealized until the position is liquidated. Example: 100 shares of a $50 stock = **$5,000** paid in full; a rise to $60 gives **$10 per share, $1,000 total**, but the money is unspendable until the shares are sold at $60.

**Futures-type settlement.** No initial cash payment from buyer to seller; all profits and losses are realized immediately even if the position is not liquidated. Example: a gold futures contract covering 100 ounces at $450 = **$45,000** full value, but the buyer pays nothing, only depositing good-faith margin. Gold to $470 gives **$2,000 ($20 x 100)** credited that day and immediately usable. Gold to $430 gives an immediate **$2,000** realized loss, and a *variation call* if the account cannot cover it.

**Margin call vs. variation call.** A margin call ensures the trader can meet *future* obligations; it can be met with funds that, though deposited at the clearing house, still belong to the trader and can earn interest for him. A variation call fulfills *current* obligations in the form of realized losses; it must be met with a cash payment immediately deducted from the account. A trader who deposited securities as margin and receives a variation call must either deposit cash or have the clearing house sell the securities. If what remains does not meet current margin, the trader may be forced to liquidate.

**The US mismatch.** "Currently all exchange-traded options in the United States, whether options on stock, futures, indices, or foreign currencies, are settled like stock." But on US futures options markets the *underlying* settles futures-type while the *options* settle stock-type. A trader who hedges a futures position with options can have the option profits exactly offset the futures losses and still face a cash squeeze: the option profits are paper profits, while the futures losses require an immediate cash outlay for a variation call.

**Outside the US.** Many exchanges have made option and underlying settlement identical, so a trader "is unlikely to get a surprise variation call on a position which he thinks is well hedged."

**Failure mode.** Believing a delta-flat or fully offset hedge is cash-flow-flat. It is not, in US futures options: "If a trader is unaware of the different settlement procedures, he can occasionally find himself with unexpected cash flow problems."

## 2. Expiration graph construction (Chapter 2)

This material folds into the existing `options-payoff` skill as its computation engine, and Rule 3, the net-call and net-put tail slopes for ratio positions, is the part that skill most likely lacks.

**The three rules, quoted as Natenberg numbers them (book p23-24):**

> 1. If the graph bends, it will do so at an exercise price. Therefore, we can calculate the profit or loss at each exercise price involved and simply connect these points with straight lines.
>
> 2. If the position is long and short equal numbers of calls (puts), the potential downside (upside) risk or reward will be equal to the total debit or credit required to establish the position.
>
> 3. Above the highest exercise price all calls will go into-the-money, so the entire position will act like an underlying position which is either long or short underlying contracts equal to the number of net long or short calls. Below the lowest exercise price all puts will go into-the-money, so the entire position will act like an underlying position which is either long or short underlying contracts equal to the number of net long or short puts.

**Corollary Natenberg applies but does not number (book p25):** if there are no puts in the position, the maximum downside loss is the total debit required to establish it, and that loss occurs anywhere below the lowest exercise price (symmetrically for no calls and the upside).

**Valuation primitive (book p13).** At expiration an option is worth either zero (if at- or out-of-the-money) or its intrinsic value, that is parity (if in-the-money). Nothing else. That single substitution is what makes the whole method arithmetic rather than model-based.

**Procedure, as executed in the book:**

1. List every exercise price in the position, lowest to highest.
2. At each exercise price, value every leg at zero-or-intrinsic, net against the trade price, multiply by the leg quantity, and sum. Plot that point.
3. Connect the plotted points with straight lines.
4. Extend left of the lowest exercise price using Rule 3's put count, or the no-puts corollary.
5. Extend right of the highest exercise price using Rule 3's call count, or the no-calls corollary.

**Reference chain used throughout Chapter 2 (book p13).** Underlying at 99.00, two months to expiration:

| | 85 | 90 | 95 | 100 | 105 | 110 | 115 |
|---|---|---|---|---|---|---|---|
| Calls | 14.05 | 9.35 | 5.50 | 2.70 | 1.15 | .45 | .20 |
| Puts | .10 | .45 | 1.55 | 3.70 | 7.10 | 11.35 | 16.10 |

**Worked ratio example A (book p24-25, Figures 2-12a/b/c).** Long one 95 call at 5.50, short three 105 calls at 1.15.

- Total debit = 2.05, computed as `-5.50 + 3 x 1.15`.
- At 95: both the 95 and 105 calls are worthless, so a loss of **2.05**.
- At 105: the 95 call is worth 10.00, the 105 calls are worthless, so the position is worth 10 points less the 2.05 debit, **+7.95**.
- Below 95: no puts in the position, so the loss is flat at the 2.05 debit.
- Above 105: long one underlying (via the 95 call) and short three underlying (via three 105 calls) = **net short two underlying contracts**; the position loses two points for every one-point rise.

**Worked ratio example B (book p27, Figures 2-13a/b/c).** Short one 90 call at 9.35, long two 100 calls at 2.70, short four 95 puts at 1.55, long two 100 puts at 3.70.

At 90:

| leg | P&L |
|---|---|
| 90 call | +9.35 |
| 100 calls | -2 x 2.70 |
| 95 puts | -4 x 3.45 |
| 100 puts | +2 x 6.30 |
| **Total** | **+2.75** |

At 95:

| leg | P&L |
|---|---|
| 90 call | +4.35 |
| 100 calls | -2 x 2.70 |
| 95 puts | +4 x 1.55 |
| 100 puts | +2 x 1.30 |
| **Total** | **+7.75** |

At 100:

| leg | P&L |
|---|---|
| 90 call | -.65 |
| 100 calls | -2 x 2.70 |
| 95 puts | +4 x 1.55 |
| 100 puts | -2 x 3.70 |
| **Total** | **-7.25** |

- Below 90: all calls worthless, all puts act like short underlying contracts; the position is **net short two puts**, so it behaves like **long two underlying contracts**, losing two points for each point the underlying falls below 90.
- Above 100: all puts worthless, all calls act like long underlying contracts; the position is **net long one call**, so it behaves like **long one underlying contract**, gaining one point per point of rise.

**Scope statement (book p27).** "Using this method we can draw the expiration profit and loss graph of any position, no matter how complex... as long as all options expire at the same time, the value of the position at expiration will be fully determined by the price of the underlying contract."

**Failure modes.** Drawing a bend anywhere other than an exercise price (Rule 1 forbids it). Assuming a ratio position's tails have slope of plus or minus 1; they have slope equal to the *net* call count on the upside or the *net* put count on the downside (example A's upside tail is -2, example B's downside tail is +2 rising as price falls). Applying the method when the options do not all expire at the same time; calendar and diagonal structures break it.

## 3. Elementary strategy classification (Chapter 2)

### The simple buy and sell strike screen (book p13-14)

**Framing.** Three expiration months times several exercise prices times calls and puts means "as many as 40 different contracts"; even after eliminating inactive ones, "15 or 20 different options." The screen exists to reduce that set.

**Rule.** An option position held to expiration is worth **zero** (at- or out-of-the-money) or **intrinsic value, that is parity** (in-the-money). "The purchase of an option will be profitable if its trade price is less than its value at expiration. The sale of an option will be profitable if its trade price is greater than its value at expiration."

Worked off the 99.00 chain with a target of **108**:

- Buy the 100 call at 2.70, intrinsic 8.00, profit **5.30**. Generalized: at 108, *any* call with an exercise price below 110 is profitable to buy, because its intrinsic value at expiration exceeds its current price.
- Sell the 110 call for **.45** (it expires worthless if the underlying never exceeds 110.00, so keep the full .45); sell the 115 call for **.20**, which buys "an additional 5 point margin for error."
- Every put struck at 105 or below is worthless, so the sale keeps the full premium. The 110 put has intrinsic 2.00 against a trade price of 11.35, sale profit **9.35**. The 115 put has intrinsic 7.00 against 16.10, sale profit **9.10**.

**Sensitivity to the target assumption.** Raise the target from 108 to **120** and the 100 call purchase makes **17.30** instead of 5.30. Drop it to **90** and that call loses the full **2.70**, while the 110 put sale that made 9.35 at 108 now loses **8.65** (the put is worth 20.00 against 11.35 received).

**Failure mode.** The entire output is only as good as the single point estimate of the underlying's price at expiration. Natenberg then abandons the method: "in actual practice it is very unlikely that a trader will put on a position and let it go to expiration" (book p31).

### The four-cell limited/unlimited risk-reward classification (book p16-19)

"buyers of options have limited risk and potentially unlimited reward; sellers of options have limited reward and potentially unlimited risk. More specifically, net buyers (sellers) of calls have unlimited upside reward (risk), and net buyers (sellers) of puts have unlimited downside reward (risk)." (book p18)

- Long call: maximum loss = the premium, occurring at and below the exercise price; breakeven = exercise price plus trade price; unlimited above.
- Long put: maximum loss = the premium, occurring at and above the exercise price; breakeven = exercise price minus trade price; profit increases one point per point below that.
- The bend point of every single-option graph is the exercise price; the depth of the flat section is the trade price.

**The probability rule (book p18-19).** "In addition to the potential risk and reward associated with any trade, a trader must also consider the likelihood of the various outcomes. Is the reward, even a limited one, sufficient to offset the risk, albeit an unlimited one? Sometimes it is; sometimes it isn't." Illustrated with the double-your-money-versus-go-broke trade at one-in-a-million odds, which most traders would take despite unlimited risk.

**The range/profit tradeoff, with numbers (book p21).** Widening the profitable range from 93.60 to 106.40 (short the 100 straddle, +6.40 maximum) out to 92.30 to 107.70 (short the 95 put and the 105 call, +2.70 maximum) costs 3.70 of maximum profit. "If a potential reward is big enough, it may be worth taking a big risk. But if the potential reward is small, the accompanying risk should also be small."

**Failure mode.** Treating "unlimited risk" as disqualifying. Natenberg's counter is that almost any stock or commodity position carries unlimited risk from a violent adverse move, yet traders take them constantly, because they judge the probability of catastrophe to be small enough. Also: assuming limited risk because a position has a bounded middle. Positions that are net long or net short options always have an unlimited tail; only equal numbers long and short of the same type give limited risk *and* limited reward.

**Natenberg's italicized maxim (book p31).** "*Every trader reserves the right to make a more intelligent decision today than he made yesterday.*" Context: a trader who sold 105 calls believing the underlying would never exceed 105 "would likewise be foolish not to reassess the situation if the underlying contract were to make a rapid upward move from 99 to 104. He may still believe that the underlying contract will not rise above 105, but he is unlikely to have the same degree of confidence."

## 4. A word on models (Chapter 3)

Section head "A WORD ON MODELS" (book p39-40). Preserve as cautionary prose; it produces no artifact.

- "A model is a scaled down or more easily managed representation of the real world." Physical (a model airplane) or mathematical (a formula).
- Italicized in the original: "*However, it is unwise, and sometimes dangerous, to assume that the model and the real world which it represents are identical in every way.*"
- "All models, if they are to be effective, require us to make certain prior assumptions about the real world... If we feed incorrect data into the model, we can expect an incorrect representation of the real world. Every model user must be aware: **garbage in, garbage out**."
- "An option model is only someone's idea of how options might be evaluated under certain conditions. Since either the model itself, or the data which we feed into the model, might be incorrect, there is no guarantee that model-generated values will be accurate, nor can we be sure that these values will bear any logical resemblance to actual prices in the marketplace."
- **The dark-room analogy.** A new trader without a model gropes in the dark; a trader with a basic understanding of theoretical pricing models "enters the same room with a small candle." He sees the general layout, but the dimness prevents him from distinguishing every detail, and some of what he sees is distorted by the flickering candle. Still better than no illumination at all.
- **The size trap.** "The real problems with theoretical pricing models arise **after** the trader has acquired some sophistication. As he gains confidence he may begin to increase the size of his trades. When this happens, his inability to make out every detail in the room, as well as the distortions caused by the flickering candle flame, take on increased importance. Now a misinterpretation of what he thinks he sees can lead to financial disaster, since any error in judgement will be greatly magnified."
- **Spectrum of trader opinion.** "Some traders feel that models are so much hocus-pocus... Other traders feel that once they have a sheet of theoretical values in hand all their problems are solved. The reality lies somewhere in between."
- Natenberg's conclusion is an attitude, not an output: make use of a model, but with a full awareness of what it can and cannot do.
- Footnote 2 sources on model limitations: Figlewski, Stephen, "What Does an Option Pricing Model Tell Us about Option Prices?", *Financial Analysts Journal*, September/October 1989, pages 12-15. Black, Fischer, "Living Up to the Model," *Risk*, Vol. 3, No. 3, March 1990, pages 11-13.

## 5. Random walks, normal and lognormal distributions (Chapter 4)

### The pinball maze and the random walk (book p51-56)

*Random walk*: the path a ball follows through the maze of nails. "Once the ball enters the maze nothing can be done to artificially alter its course, nor can one predict ahead of time the path the ball will take through the maze." Balls dropped into the maze pile up into the familiar bell-shaped curve of Figures 4-1 through 4-5. The distribution intuition to carry forward: "the value of an underlying contract depends on where the peak of the curve is located, while the value of an option depends on how fast the curve spreads out."

### Mean and standard deviation, the probability table (book p57, restated in Figure 4-6)

| Range | Share of all occurrences | Rough fraction |
|---|---|---|
| plus or minus 1 standard deviation | approximately 68.3% | about 2/3 |
| plus or minus 2 standard deviations | approximately 95.4% | about 19/20 |
| plus or minus 3 standard deviations | approximately 99.7% | about 369/370 |

- Exact complement of 1 standard deviation: 100% less 68.3% = **31.7%**, about 1 chance in 3 outside.
- Standard deviations are additive: if 1 standard deviation = 3, then 2 standard deviations = 6.
- A single specified tail beyond 2 standard deviations is half of the 1-in-20, so approximately **1 chance in 40**. That is the basis for rejecting 30-to-1 odds as a bad bet.
- Figure 4-6 worked frame: mean 7.50, standard deviation 3.00 (exact values 7.51 and 2.99); minus 2 standard deviations = 1.50, minus 1 = 4.50, mean = 7.50, plus 1 = 10.50, plus 2 = 13.50.

Definition to keep exact. *Volatility number*: "a one standard deviation price change, in percent, at the end of a one-year period."

### Why lognormal is the right distribution for underlying prices (book p61-65)

**Why not a normal distribution.** "If we allow for the possibility of a $50 instrument rising $75 to $125, we must also allow for the possibility of the instrument dropping $75 to a price of -$25. Since it is impossible for traditional stocks and commodities to take on negative prices, the normal distribution assumption is clearly flawed." And: "A lognormal distribution... does allow for open ended upside prices (the logarithm of plus infinity is plus infinity), while bounding downside prices by zero (the logarithm of minus infinity is zero)."

**Compounding of a 12% annual rate on $1,000 (book p62), the lognormal argument.**

| Rate of Payment | Value after One Year | Total Yield |
|---|---|---|
| 12% once a year | $1,120.00 | 12% |
| 6% twice a year | $1,123.60 | 12.36% |
| 3% every three months | $1,125.51 | 12.55% |
| 1% every month | $1,126.83 | 12.68% |
| 12%/52 every week | $1,127.34 | 12.73% |
| 12%/365 every day | $1,127.47 | 12.75% |
| 12% compounded continuously | $1,127.50 | 12.75% |

| Rate of Loss | Value after One Year | Total Yield |
|---|---|---|
| -12% once a year | $880.00 | -12% |
| -6% twice a year | $883.60 | -11.64% |
| -3% every three months | $885.29 | -11.47% |
| -1% every month | $886.38 | -11.36% |
| -12%/52 every week | $886.80 | -11.32% |
| -12%/365 every day | $886.90 | -11.31% |
| -12% compounded continuously | $886.92 | -11.31% |

**The lognormal skew, verbatim.** "a continuously compounded rate of return of +12% yields a profit of $127.50 after one year, while a continuously compounded rate of return of -12% yields a loss of only $113.08. If the 12% were a volatility, then a one standard deviation upward price change at the end of one year would be +$127.50, while a one standard deviation downward price change would be -$113.08. Even though the rate of return was a constant 12%, the continuous compounding of the 12% yielded different upward and downward moves."

**Consequence for equidistant strikes.** With the underlying at exactly 100 and no interest considerations, under a normal distribution the 110 call and the 90 put (both 10% out-of-the-money) would have identical theoretical values; "under the lognormal assumption in the Black-Scholes Model, the 110 call will always have a greater value than the 90 put." Footnote 1: "Of course, this is only theory. There is no law that says the price of the 90 put in the marketplace cannot be greater than the price of the 110 call."

### The four Black-Scholes price-movement assumptions (book p64, verbatim)

1. "Changes in the price of an underlying instrument are random and cannot be artificially manipulated, nor is it possible to predict beforehand the direction in which prices will move."
2. "The percent changes in the price of an underlying instrument are normally distributed."
3. "Because the percent changes in the price of the underlying instrument are assumed to be continuously compounded, the prices of the underlying instrument at expiration will be lognormally distributed."
4. "The mean of the lognormal distribution will be located at the forward price of the underlying contract."

Natenberg's own caveats on that list. On assumption 1, technical analysts disagree, but "The important point here is that the Black-Scholes Model makes the assumption that price changes are random and that their direction cannot be predicted... price prediction will focus on the magnitude of the price changes, rather than on the direction of changes." On assumption 3: "there is also good reason to question the third assumption, that prices are lognormally distributed at expiration. This may be a reasonable assumption for some markets, but a very poor assumption for other markets."


Material from Natenberg, "Option Volatility & Pricing" (1994, 2nd ed.) Chapters 13, 15 and 16 that did not earn its own skill. Page numbers are printed book pages. Minus signs are written as plain hyphens.

## 6. Hedging with options (Chapter 13)

Framing (p257 to p258): "Every hedging decision is a tradeoff: what is the hedger willing to give up under one set of market conditions in order to protect himself under another set? A hedger with a long position who wants to protect his downside will almost certainly have to give up something on the upside; a hedger with a short position trying to protect his upside will have to give up something on the downside." Who hedges: *natural longs* (a commodity producer, a lender) and *natural shorts* (a commodity user, a borrower), plus voluntary longs and shorts, such as a portfolio manager who "may find it cheaper to temporarily hedge the stocks with options or futures than to sell the stocks and buy them back at a later date." The synthetic identity set used throughout: `short underlying + long call = long put`; `long underlying + long put = long call`; `long underlying + short call = short put`; `short underlying + short put = short call`.

### Protective calls and puts (p258 to p260)

**Construction.** Buy a call to protect a short underlying position, a put to protect a long one. "if the market moves adversely, the hedger is insulated from any loss beyond the exercise price." **Risk removed:** loss beyond the exercise price. **Risk kept:** the gap between the current price and the exercise price, mapped explicitly to insurance: "The difference between the exercise price and the current price of the underlying is analogous to the **deductible** portion of an insurance policy. And the price of the option is analogous to the **premium** which one has to pay for the insurance policy." **Preserved:** "the hedger still maintains open-ended profit potential." **Cost:** the premium, paid in full whatever happens.

**Worked example (DM protective call).** An American firm takes delivery of DM 1,000,000 of German goods in six months with payment due in DM, so it is automatically short DM against USD. At .60 the goods cost $600,000; at .70 they cost $700,000. The exact hedge is an underlying contract of DM 1,000,000 expiring on the delivery date.

| Call struck at | Price | Cash cost | Protection |
|---|---|---|---|
| .62 | .015 (1 1/2 cents) | $15,000 | any rise above .62 |
| .64 | .0075 (3/4 cent) | $7,500 | any rise above .64 |
| .66 | .0025 (1/4 cent) | $2,500 | only above .66; bear all loss up to .66 |

Upside kept: if DM falls to .55 the firm lets the .64 call expire and buys DM 1,000,000 for $550,000, "an unexpected windfall of $150,000." Strike choice is deferred in this section ("That depends on the amount of risk the hedger is willing to bear, something which each market participant must determine individually"); the selection procedure is in Complex hedging strategies below.

### Covered writes (p260 to p263)

Synonyms *overwrites* and *buy/write* (the latter when the underlying is bought and the calls sold simultaneously). **Construction:** sell a call against a long underlying position, or a put against a short one. **Risk removed:** only as much adverse movement as the credit covers. "This strategy does not offer the limited risk afforded by the purchase of a protective option but, in its favor, the strategy results in a cash credit rather than a debit. This credit offers some, though not unlimited, protection against an adverse move in the underlying market." **Risk kept:** everything below `underlying price - premium`. **Cost:** not cash, but forgone upside above the strike. Strike ladder: an in-the-money call gives "a high degree of protection, but will eliminate most upside profit potential," an out-of-the-money call "less protection but leaves room for large upside profit potential."

**Worked numbers, stock at 100.** Sell the 95 call at 6 1/2: break even down to 93 1/2, and even if the stock rises and is called away the manager keeps the 1 1/2-point time premium. Sell the 105 call at two: protected only to 98, participates point for point to 105, called away above that. At-the-money default: "An at-the-money option is pure time premium. If the market sits still, a portfolio of at-the-money options ... sold against an existing position in the underlying instrument will show the greatest appreciation in value."

### Fences (p263 to p265)

Aliases *range forwards*, *tunnels*, *cylinders*, *split-price conversions and reversals*; in the rate market *cap*, *floor*, *collar*. **Construction:** "A popular strategy, known as a *fence*, is to simultaneously combine the purchase of a protective option with the sale of a covered option." Long underlying at 50, sell a 55 call and buy a 45 put: "The hedger is insulated from any fall in price below 45, since he can then exercise his put. At the same time, he can participate in any upward move to 55, at which point his underlying position will be called away." **Risk removed:** all downside below 45. **Risk kept:** the band from 45 up to the entry price, plus all upside above 55. **Cost:** the net of the two premiums, possibly a credit. With the 45 put at 1.25 and the 55 call at 1.75 the hedger receives .50, reducing his break-even on the underlying to 49.50. "Fences are popular hedging tools because they offer known protection at a low cost, or even a credit."

Synthetic reduction, verbatim derivation:

```
long 45 put   = short underlying + long 45 call
45/55 fence   = long underlying + long 45 put + short 55 call
              = long underlying + (short underlying + long 45 call) + short 55 call
              = long 45 call + short 55 call
```

So a long fence is "simply a **bull vertical spread** done synthetically," and a short fence (short underlying, protective call, covered put) "is simply a **bear vertical spread**." Rate mapping (p265): a variable-rate borrower is short interest rates and buys an interest rate call to *cap* his cost, "thereby establishing a maximum amount it will have to pay for borrowed funds"; a variable-rate lender is long rates and buys an interest rate put for a *floor*, "thereby establishing a minimum amount it will receive for loaned funds." Buying a cap and selling a floor, or the reverse, is a *collar*, "simply a fence done in the interest rate market."

### Complex hedging strategies (p265 to p269)

**The three intake questions (p266, verbatim list):** 1. "Does the hedge need to offer protection against a 'worst case' scenario?" 2. "How much of the current directional risk should the hedge eliminate?" 3. "What additional risks is the hedger willing to accept?"

**Price versus value (p261).** "In theory, the hedger ought to base his decision on the same criteria as the pure trader: **price versus value**. In general, **if the price of an option is lower than its value, then the purchase of a protective call or put makes the most sense. If the price of an option is higher than its value, then the sale of a covered call or put makes the most sense.** By comparing implied volatility to a forecast volatility, a hedger ought to be able to make a sensible determination as to whether he wants to buy or sell options." Practical override (p263): "If a hedger knows that he will be forced out of business if the underlying contract moves beyond a certain price, then the purchase of a protective option at that exercise price may be the most sensible strategy, **regardless of whether the option is theoretically overpriced**." Insurance answer to "why pay premium I will probably lose" (p263): "If a hedger needs the protection afforded by the option, the purchase makes sense in spite of the fact that it is likely to be a losing proposition in the long run." Exit to no options (p266): "If his sole purpose is to hedge his downside risk without regard to upside profit potential, he ought to avoid options and hedge himself in the futures or forward market."

**The implied-volatility master rule (p266, italicized in the book):** "*All other factors being equal, in a high implied volatility market a hedger should buy as few options as possible and sell as many options as possible. Conversely, in a low implied volatility market a hedger should buy as many options as possible and sell as few options as possible.*"

**Delta-target sizing (p266).** To retain 50% of a long position, buy puts with a total delta of -50, either one at-the-money put at -50 or several out-of-the-money puts summing to -50. "But in a high implied volatility market one usually tries to buy as few options as possible and sell as many options as possible. (This is analogous to constructing a ratio vertical spread.) Hence, purchasing one put with a delta of -50 will be less costly, theoretically, than purchasing several options with a total delta of -50." To eliminate 75%, buy one put with a delta of -75. The sell-side mirror is the *ratio write*: hedging 50% of a long position by selling several out-of-the-money calls totalling 50 deltas rather than one at-the-money call.

Restrict unlimited risk to one direction (p267): "Most hedgers want to restrict their unlimited risk to one direction, usually the direction of their natural position ... **But a true hedger ought not lose sight of what his ultimate goal is: to protect an existing position, and to keep the cost of this protection as low as possible.**" Selling more calls than the underlying covers adds unlimited upside risk on top of the covered call's unlimited downside risk. Volatility spreads as hedges (p267): protecting 50% of a short underlying position means buying or selling time spreads or butterflies with a total delta of +50, which "offer partial protection within a range." In low implied volatility, market at 100, buy the 110 call time spread: "If the 110 call time spread has a delta of +25, to hedge 50% of his directional risk the hedger can buy two time spreads for each short underlying position." In high implied volatility, sell the 90 call time spread instead, keeping delta and edge both positive: "If he wants to protect 75% of his position, and the spread has a delta of +25, he can sell the spread three times for each underlying position." Vertical spreads as hedges (p267): work around the at-the-money option. "If implied volatility is high, he will prefer to sell an at-the-money option and buy an out-of-the-money option. If implied volatility is low, he will prefer to sell an in-the-money option and buy an at-the-money option." Presentation rule (p268): the adviser "should lay out a limited number of strategies (perhaps four or five) which make sense, and compare the various risk/reward characteristics of the strategies."

**Figure 13-7, "Summary of Hedging Strategies" (p269). CAVEAT: the page is printed sideways in the scan and the multi-line rows cannot be aligned to their strategies with certainty, so this figure is deliberately NOT reproduced as a table. The strategy inventory is certain; the advantage and disadvantage wording below is verbatim and in source order only, and must not be read as a per-strategy mapping.**

- Long underlying: buy a protective put; sell a covered call; long fence (buy a put, sell a call); ratio put purchase; ratio call write; bear vertical spread; bear time spread.
- Short underlying: buy a protective call; sell a covered put; short fence (buy a call, sell a put); ratio call purchase; ratio put write; bull vertical spread; bull time spread.

Advantages column, verbatim in source order: limited downside risk/unlimited upside profit Â· potential positive theoretical edge Â· potential positive theoretical edge Â· limited downside risk Â· potential credit if call price exceeds put price Â· unlimited upside profit/unlimited downside profit Â· potential positive theoretical edge Â· unlimited upside profit Â· potential positive theoretical edge Â· unlimited upside profit Â· potential positive theoretical edge Â· limited upside risk/unlimited downside profit Â· potential positive theoretical edge Â· limited upside risk Â· potential credit if put price exceeds call price Â· unlimited downside profit/unlimited upside profit Â· potential positive theoretical edge Â· potential positive theoretical edge Â· unlimited downside profit Â· potential positive theoretical edge Â· unlimited downside profit Â· potential positive theoretical edge

Disadvantages column, verbatim in source order: potential negative theoretical edge Â· unlimited downside risk Â· potential negative theoretical edge Â· limited upside profit Â· potential debit if put price exceeds call price Â· potential negative theoretical edge Â· unlimited downside risk/unlimited upside risk Â· potential negative theoretical edge Â· unlimited downside risk Â· potential negative theoretical edge Â· unlimited downside risk Â· potential negative theoretical edge Â· potential negative theoretical edge Â· unlimited upside risk Â· potential negative theoretical edge Â· limited downside profit Â· potential debit if call price exceeds put price Â· potential negative theoretical edge Â· unlimited upside risk/unlimited downside risk Â· potential negative theoretical edge Â· unlimited upside risk Â· potential negative theoretical edge Â· unlimited upside risk Â· potential negative theoretical edge

The compound descriptors joined by "/" are unambiguous and pair with confidence: protective put gives limited downside risk / unlimited upside profit; ratio put purchase gives unlimited upside profit / unlimited downside profit; ratio call write carries unlimited downside risk / unlimited upside risk; protective call gives limited upside risk / unlimited downside profit; ratio call purchase gives unlimited downside profit / unlimited upside profit; ratio put write carries unlimited upside risk / unlimited downside risk.

### Portfolio insurance (p268 to p272)

Definition (p271): "This process of continuously rehedging an underlying position to replicate an option position is often referred to as ***portfolio insurance***." Step 1, reduce the protection to a replicable option: the hedger wants `long underlying + long put`, which equals `long call`, so "the hedger really wants to own a **call with the same exercise price as the put**." Step 2, price that call and read its delta. Inputs (p268): `exercise price = 100`, `time to expiration = 10 weeks`, `underlying price = 101.35`, `interest rate = 8%`, `volatility = 18.3%`. Call delta = 57, so owning the call equals owning 57% of the asset and the hedger "must **sell off 43%** of his holdings in the asset." Step 3, rehedge to the new delta each period.

**Figure 13-8, the full replication schedule (p271):**

| Week | Asset Value | Delta of 100 call | % of Asset Needed for Replication | Required Adjustment |
|---|---|---|---|---|
| 0 | 101.35 | 57 | 57% | sell 43% |
| 1 | 102.26 | 62 | 62% | buy 5% |
| 2 | 99.07 | 46 | 46% | sell 16% |
| 3 | 100.39 | 53 | 53% | buy 7% |
| 4 | 100.76 | 56 | 56% | buy 3% |
| 5 | 103.59 | 74 | 74% | buy 18% |
| 6 | 99.26 | 45 | 45% | sell 29% |
| 7 | 98.28 | 35 | 35% | sell 10% |
| 8 | 99.98 | 50 | 50% | buy 15% |
| 9 | 103.78 | 93 | 93% | buy 43% |
| 10 | 102.54 | 100 | 100% | buy 7% |

Terminal rule (p270): this is Figure 5-1 run in reverse, so every adjustment is the opposite of that example, and at week ten "instead of liquidating the position, as we did in Figure 5-1, **we plan to buy in the remainder of the asset. It was always our intention to retain our entire holding of the asset at expiration.**"

**The cost (p270).** The unfavorable adjustments, buying high and selling low, are the cost. "If the replication process offers the same protection as owning a 100 put, then one might expect the cost of the replication process to be the same as the theoretical value of the ten week 100 put. **This is indeed the case. Using the previously listed inputs, the Black-Scholes model yields a theoretical value for the 100 put of 2.55. This is identical to the cost of the replication process described in Figure 13-8.**" Gamma interpretation (p270): an option "automatically rehedges itself" through its gamma, and "**The cost of the option, or the cost of the rehedging process, is the price the hedger pays for the option's gamma characteristics.**" Volatility-error argument (p271): "**notice that the cost of replication will always be the right cost.** If the market is more volatile than expected, the cost will be greater in terms of required adjustments. But the value of the option would also have been greater."

The $100 million example (p271): a manager insuring a $100 million portfolio against a drop below $90 million "can either buy a **$90 million put**, or he can replicate the characteristics of a **$90 million call** ... **In effect, he has created his own put.**" Transaction costs and the workaround (p271 to p272): "the costs of buying and selling a large number of securities in odd amounts may be quite high ... **One common method involves using futures contracts as a substitute for the portfolio holding.**" The usual vehicle is the S&P 500 futures contract at the Chicago Mercantile Exchange, and its cost is basis risk: "the S&P 500 index is unlikely to exactly duplicate the holdings of any one portfolio. Still, the risk may be acceptable given the reduced transaction costs." Four reasons to replicate even when the option exists (p272): the option looks theoretically overpriced; there is insufficient liquidity for the size needed; the available expirations do not match the horizon; or a hybrid, buying the available option and replicating over the period after it expires.

## 7. Stock index futures and options (Chapter 15)

### Calculating an index (p302 to p305)

Natenberg presents two weighting schemes, price weighted and capitalization weighted. **No equal-dollar-weighted index appears anywhere in this chapter, so none is reproduced here.** The four-stock worked example:

| Stock | Price | Total Shares Outstanding | Total Capitalization |
|---|---|---|---|
| 1 | 125 | 10,000 | 1,250,000 |
| 2 | 80 | 5,000 | 400,000 |
| 3 | 52 | 25,000 | 1,300,000 |
| 4 | 17 | 40,000 | 680,000 |

**Price weighted:** "the total value of the index is simply the sum of the prices of all the stocks in the index," `125 + 80 + 52 + 17 = 274`, weights 45.6%, 29.2%, 19.0%, 6.2%. Consequence: "If a trader were monitoring a price weighted index for possible changes, he would do well to look for movement in the higher priced stocks in the index." **Capitalization weighted:** `(125 x 10,000) + (80 x 5,000) + (52 x 25,000) + (17 x 40,000) = 3,630,000`, weights 34.5%, 11.0%, 35.8%, 18.7%. Consequence: "the stocks which will have the greatest effect on the index are those with the greatest market value. These are often stocks which are very widely held, even though they may not be the highest priced stocks." The example is engineered to show the reversal: stock 1 is the highest priced at a 45.6% price weight, but stock 3 is the largest cap weight at 35.8%.

**The divisor.** An index is rebased to a round number, usually 100, by dividing: `274/x = 100, x = 2.74`, and `3,630,000/x = 100, x = 36,300`. "An index divisor is not constant ... If stocks in the index split or declare special stock dividends, or if stocks are replaced by other stocks due to buyouts, liquidations, or bankruptcies, the index value might go up or down, even though the market prices of the stocks making up the index remain unchanged. To offset this effect, when any capitalization change occurs in the stocks making up the index, the divisor is changed." **Price source.** Where a stock trades on more than one exchange, the prospectus specifies which print is used, "most commonly the primary marketplace for that stock." "A trader who follows a stock index should always know the source of the stock prices used to calculate that index."

### Replicating an index (p304 to p305)

Price weighted, point value $100, divisor 2.74: the index is worth `100.00 x $100 = $10,000`, while 100 shares of each stock is $27,400, nearly three times too big. Dividing each 100-share purchase by 2.74 gives about 36 1/2 shares of each: `(125 + 80 + 52 + 17) x 36.5 = $10,000`. Footnote: "one cannot trade fractional shares of stock ... a trader attempting to replicate the sample index would have to buy either 36 or 37 shares of each stock." Capitalization weighted, point value $500, divisor 36,300, index dollar value `100.00 x $500 = $50,000`:

| | Outstanding Shares | | Point Value | | Divisor | | Required Shares |
|---|---|---|---|---|---|---|---|
| stock 1: | 10,000 | x | 500 | / | 36,300 | = | 137.7 |
| stock 2: | 5,000 | x | 500 | / | 36,300 | = | 68.9 |
| stock 3: | 25,000 | x | 500 | / | 36,300 | = | 344.4 |
| stock 4: | 40,000 | x | 500 | / | 36,300 | = | 551.0 |

Check: `(137.7 x 125) + (68.9 x 80) + (344.4 x 52) + (551.0 x 17) = 50,000`. Summary block (p305): for a price weighted index, `point value / index divisor`; for a capitalization weighted index, `outstanding shares x point value / index divisor`.

### The fair value formula (p305 to p307)

Carrying cost rule: "The amount of interest saved by purchasing a stock index futures contract rather than the actual stocks in the index can be calculated by multiplying the current index value by the risk-free interest rate, and then multiplying this number by the amount of time remaining to expiration of the futures contract." Three months, index 274.00, rate 8%: `8% x 3/12 x 274.00 = 2% x 274.00 = 5.48`. Expected dividends `$1.80 + $.90 + $.35 = $3.05`. **Exactly as printed (p307):**

```
274.00 (index value) + 5.48 (carrying costs) - 3.05 (expected dividends) = 276.43
```

Interest on the dividends (`1.80 x 2/12 x 8% = about .02`) is real but "so small in relation to the actual index that most traders simply deduct the dividend payments themselves." The dividend total depends on the weighting scheme: price weighted means equal shares of each stock, so the total is the plain sum; cap weighted means "the dividend payout for each stock multiplied by the number of shares required for replication." Approximate fair value, the desk shortcut: nine weeks (63 days), index 425.00, rates 8%, average annual dividend payout 6% gives `(8% - 6%) x 63/365 x 425.00 = 1.47`, so 426.47. Its stated failure condition is a window with many missed dividends or an unusually large payout, which makes the estimate "far from accurate." Figures 15-1 and 15-2 document the lumpiness: a spike near 0.25 index points in early May against near-zero days through April, with cumulative dividends starting near 3.25 index points and dropping sharply in the first two weeks of May. Implied index value runs the calculation backwards; futures 432.70 assumed fair, 42 days, rates 6%, expected dividends 2.23: `432.70 + 2.23 = 434.93`, then `434.93 x 42/365 x 6% = 3.00`, so the implied index value is `434.93 - 3.00 = 431.93`. Futures delta: index 300.00, three months, 8%, dividends 4.50 gives fair value 301.50; index up 10% to 330.00 gives 332.10. "The index rose 30.00 while the futures contract rose 30.60. The delta of the futures contract is therefore 102." A 50-lot program hedged one-for-one leaves `(50 x 102) - (50 x 100) = +100` residual deltas, one index contract's worth.

### The arbitrage decision rule and its bands (p309 to p312)

"If the futures price doesn't reflect the fair value, a trader can execute a profitable arbitrage by purchasing the undervalued asset, either the basket of stocks or the futures contract, and selling the overvalued asset." At $500 per point a .65 mispricing is $325 per contract and a .80 mispricing is $400 per contract. The unwind uses *market on close* orders so the liquidation price equals the print that sets the settlement index. *Program trading*: "A buy program consists of buying the stocks and selling the futures contract, and a sell program consists of selling the stocks and buying the futures contract."

**The asymmetric no-trade band (p310).** With a round-trip execution cost of about 1/2 index point and a wider requirement on the side that needs short stock, "With the fair value of the futures contract at 386.75, the trader will initiate a program trade only if the price of the futures contract is outside the range" `386.75 - .75 and 386.75 + .50`, "or less than 386.00 and more than 387.25." The asymmetry is the point: the sell-program side needs the wider edge.

Four execution frictions, each with its mechanism. 1. **Short-sale availability and the borrow rate:** borrowable stock may not exist and the market may not permit shorting, and "If the actual interest earned is less than the interest rate used to calculate the fair value of the futures contract, the fair value of the futures contract, for trading purposes, may be less than the presumed fair value of 386.75." Your fair value is not the printed fair value. 2. **Bid/ask against the index print:** the index is built from last trades struck at bids, asks and in between, so "If a trader wants to immediately execute a buy program, he will have to purchase every stock in the index at the ask price, and this may be at a price well above the quoted index value." 3. **Stale or halted prints:** "The last sale in a stock may have been at 38 1/4, but if the market in the stock is falling very quickly, the offered price for the stock may be 37 3/4." 4. **Settlement-type (variation) risk:** stock legs settle stock-type as paper profit while futures legs settle futures-type in cash, so an adverse index move can force borrowing to meet variation and "the arbitrage which initially appeared profitable actually turns into a loss." Hence the standing preference: "a program trade always wants the market to move in the direction of the futures contract so that cash will flow into the trader's account."

Interest rates: a buy program is effectively borrowing cash, so rate rises hurt and falls help; a sell program is effectively lending, so the signs reverse. The effect scales with time to expiration and is negligible on short-dated futures. Dividends: in a buy program an increase helps and a decrease hurts, and the reverse in a sell program; irrelevant in a broad index, decisive in a narrow one where "a change in the expected dividend payout of even one firm can alter the potential profitability of the trade." Standing humility line: "Most traders have learned through experience that the apparent mispricing of a stock index futures contract is often illusory, or at least smaller than it appears."

### The phantom variable (p314 to p320)

In the United States most stock indices are fixed at 4:00 PM Eastern when the NYSE closes, but component stocks keep trading on regional exchanges and index futures and options keep trading. "The fact that the underlying index may be fixed while options and futures on the index continue to trade results in an anomaly concerning early exercise." **The exercise rule (p317):** "Anytime after the index value has been fixed for the day, a trader who finds that the next day's presumed theoretical value is less than parity will be better off exercising an index option early rather than holding it." Worked with the index fixed at 400.00 and the market pricing a 10-point lower open: a holder of 380 calls loses 8.74 per call by holding and only 2.44 by exercising, a saving of 6.30; the 390 calls save 2.90. Stress the decision at a higher implied volatility before acting, because even at 18% the 380 and 390 calls price at 15.06 and 8.84, still below parity.

**The parity floor (p319):** "In a market where early exercise is a possibility, options should never trade for less than parity ... If the 390 call were really trading at 7.04 as a result of the negative news, a trader would buy as many calls as possible and immediately submit exercise notices, in the process collecting 10 points per option. He would realize an immediate profit of 2.96 per option." **The offset rule:** "Regardless of what happens the following morning, a trader will always be better off exercising as long as he takes action to offset the effects of the exercise." Exercise turns option deltas into cash and cash has no delta, so the vanished deltas must be replaced by closing the other option leg, buying stock in the correct proportion, or buying futures at roughly 100 index deltas each. In the worked ratio spread, doing nothing loses 12.30 while exercising and buying back the 410 calls at .98 gains 16.70.

**The phantom variable itself (p319):** "This value arises because under some circumstances a trader can exercise index options and replace them with other instruments at more favorable prices ... It is doubtful that anyone really knows how to quantify that probability, and traders tend to regard the possibility of a significant event occurring as a *phantom variable*. No one knows how to evaluate it, but everyone agrees that it exists." Its observable price is read off boxes: a European 10-point box at four weeks and 6% is `10.00 - (28/365 x 6% x 10.00) = 9.95`, a binomial American value with a normal dividend payout is about 10.05, and OEX boxes "often trade for as much as 10 1/4 to 10 3/8." The excess, roughly .20 to .33 of a point on a 10-point box, is the market's quote for the phantom variable. The seller's side is asymmetric: assignment on a cash index option removes deltas outright rather than replacing them with stock deltas, and "exercise notices are processed overnight, so the trader will not find out that he has been assigned until the next trading day."

### Finding a substitute for the index (p320 to p326)

The index is not deliverable: "If the trader exercises the call, or is assigned on the put, there is a cash transfer. But the trader is still left holding the basket of stocks." Mispriced index synthetics therefore "not only ... occur more frequently in index option markets, they can persist for long periods of time." The ladder:

1. **The complete basket.** Reasonable for a 20 or 30 stock index, impractical for several hundred.
2. **The pseudo-basket:** "a selection of stocks in the index which can be easily bought or sold, and which will react to changing market conditions in a way which is almost identical to the actual index." Sizing rule (p322): "if the index is at 400.00 and a trader executes a conversion with the synthetic market mispriced by 1.00, the 99% correlation means he could be wrong by as much as 1% of 400.00, or 4.00. Under some conditions, his presumed profit of 1.00 might turn into a loss of 3.00." Generalized: correlation error in index points = `(1 - correlation) x index level`, judged against the edge in index points, never against the correlation percentage.
3. **A futures contract on the same index.** The best substitute: lower cost, 100% correlation, automatic cash settlement. Conditional: "Providing that the futures contract and the options expire at the same time, a futures contract on the same index which underlies the cash option market is a perfect substitute for the basket." Still not free money, because "if contracts are mispriced in one index market, they are often mispriced by an equal amount in other index markets."
4. **Futures on a different but similar index.** No S&P 100 future existed, so traders reached for S&P 500 futures, taking two independent risks. Risk A, spread drift: Figure 15-3 shows the S&P 500 minus S&P 100 spread over 1992 and 1993 with "a range of almost 20 index points," and it "was not uncommon for the spread to change by as much as five points over a period of several weeks." Risk B, settlement mismatch: "S&P 100 options are settled from the closing stock prices on the last trading day, while the S&P 500 futures are settled from the opening stock prices on the same day." Hence "using S&P 500 futures contracts as a hedge against S&P 100 options is a short-term solution at best."
5. **Do not substitute.** "The best solution for most index option traders is to avoid using substitute index contracts whenever possible, and to attempt to execute all strategies within the same index market," meaning boxes, jelly rolls, and the time spreads, vertical spreads and butterflies they are built from. Residual problem: both carry early-exercise risk, and a jelly roll still leaves a near-term synthetic to deal with at the near expiration.

### Biases in the index market (p326 to p329)

The observation being calibrated for: "synthetic markets always seem to be under pressure. That is, the synthetic market tends to trade at less than theoretical value."

- **Bias 1, one-sided hedging demand.** "the vast majority of equity portfolio managers take only long positions in equities ... a portfolio manager is almost always trying to hedge a long position in the market. This means that the manager is either buying protective puts, selling covered calls, or pursuing some combination of these strategies. The result is that there is constant selling pressure on calls and constant buying pressure on puts." The same pressure reaches futures through dynamic hedging and portfolio insurance selling futures.
- **Bias 2, the offsetting arbitrage is structurally blocked.** The market maker on the other side ends up long calls, short puts or long futures, and hedging that requires selling stock short: the uptick rule applies (a 1994 US specific), "there is no guarantee that an uptick will occur in even one stock, let alone several hundred," and short-sale interest earnings differ from borrowing costs. The era's partial workaround was the Chicago Stock Exchange's Chicago Basket (CMX), 20 major US stocks tradeable at once and exempt from the uptick rule. Conclusion: "In stock index markets around the world, there tends to be constant downward pressure on derivative products."
- **Bias 3, the premium-level bias.** Figure 15-4 compares OEX 30-day historical volatility with the OEX implied volatility index (VIX, the implied volatility of a theoretical at-the-money OEX option with 30 days remaining) from 1989 to 1992 on a roughly 5% to 35% axis: "the implied volatility is almost always greater than the historical volatility." The mechanism keeping it alive is rational insurance demand, not irrationality: a homeowner knowingly pays more than theoretical value for peace of mind, and a manager who expects his portfolio to outperform "may be willing to overpay since the options will protect him, while at the same time leaving him ahead in the long run."

## 8. Intermarket spreading (Chapter 16)

### The volatility relationship between two markets

Definitions (p331): most spreading is *intramarket spreading*, within one underlying. "If a trader can identify a relationship between contracts in two different markets, and finds that the instruments are mispriced relative to each other, it is possible to spread one instrument or its derivative products against another instrument or its derivative markets (*intermarket spreading*)." Market selection is the front-end filter (p334 to p335): "While a trader might find it difficult to identify a relationship between corn and Deutschemarks, he might very well find a relationship between corn and soybeans, or between Deutschemarks and Swiss Francs ... The closer the relationship, the more such instruments lend themselves to intermarket spreading." The core claim (p336): "A close price relationship between markets may also mean that the markets have similar volatility characteristics. This may enable the trader to identify mispriced options without the necessity of picking the right volatility for either market." And the claim that follows it: "Note that the trader has not made any attempt to predict the right volatility for either ABC or XYZ. He has simply made the assumption that the implied volatilities do not reflect his view of market conditions."

**State plainly: Natenberg prints NO correlation formula and NO spread-volatility formula in this chapter.** There is no correlation coefficient, no correlation-adjusted volatility expression, and nothing of the form `sqrt(s1^2 + s2^2 - 2 x rho x s1 x s2)` anywhere in it. His entire cross-market adjustment is one empirically read **volatility ratio**, estimated from a chart rather than a statistic. Figure 16-7 plots the 50-day historical volatilities of the S&P 100 (OEX) and the NYSE Composite (NYA) from July 1988 to August 1992 on an 8% to 26% axis with OEX consistently the higher line; Figure 16-8 plots NYA volatility as a percent of OEX volatility on a 75% to 100% axis. "We can see that NYA volatility is typically somewhere between 80% and 95% of OEX volatility. As a rough estimate we might decide that on average NYA volatility is approximately 87% of OEX volatility." Both numbers are load-bearing: the 87% average sets the ratio, the 80% to 95% band sets the risk. The invariance this buys (p342): "The important consideration in an intermarket spread is not necessarily the volatility of each individual contract, but the volatility relationship between the contracts ... if we determine that XYZ is always 25% more volatile than ABC, the actual volitilities of ABC and XYZ don't really matter. The ratio is the same whether the volatility of ABC is 20% and XYZ is 25%, or ABC is 12% and XYZ is 15%, or ABC is 28% and XYZ is 35%."

### Constructing an intermarket volatility spread

Balance in points, not contracts: a 1:1 spread pays on point differences, so a market can outperform in percent terms and still lose. "In order to equalize the percent price changes, his spread must be long and short an equal number of points." Then balance in dollars, because point values differ. ABC at 50 with a $400 point against XYZ at 100 with a $100 point: a two-for-one spread is $40,000 against $10,000, and ABC can fall 6% against XYZ falling 10% and still lose `[-2 x (50 - 47) x $400] + [1 x (100 - 90) x $100] = -$2,400`. The dollar-balance rule and the ratio it implies:

```
(ABC contracts) x (price of ABC) x (point value of ABC)
    = (XYZ contracts) x (price of XYZ) x (point value of XYZ)
balanced ratio = (price ABC / price XYZ) x (point value ABC / point value XYZ)
               = (50 / 100) x (40/10) = 2   (2:1)
```

**The dollar sensitivities (p332, p346 to p347):**

```
$delta        = (contract price x point value) / 100
option $delta = underlying $delta x option's delta
$gamma        = underlying $delta x option's gamma x underlying point value / 100
$theta        = underlying point value x option's theta
$vega         = underlying point value x option's vega
```

$delta is "the dollar value change for a one-percent change in the price of the underlying contract"; $gamma is the change in $delta for a one-percent price change; $theta is the dollar change with the passage of one day; $vega is the dollar change per percentage point of volatility. ABC $delta = `50 x $400 / 100 = $200`, XYZ $delta = `100 x $100 / 100 = $100`, so each ABC delta is worth two XYZ deltas. The at-the-money trick removes the need to pick a volatility at all: "No matter what the volatility, he knows that an at-the-money option will have a delta of approximately 50." Move off that strike and you have implicitly taken a second position, on the absolute level of implied volatility in at least one market: buying lower-delta options and selling higher-delta ones creates an *intermarket call backspread*, the mirror creates an *intermarket put ratio vertical spread*, and "A backspread wants the market to become more volatile; a ratio vertical spread wants the market to become less volatile."

**The two balance equations (p341):**

```
ABC contracts x $delta of ABC x ABC option delta
    = XYZ contracts x $delta of XYZ x XYZ option delta

ABC contracts x $delta of ABC x ABC option delta x ABC volatility
    = XYZ contracts x $delta of XYZ x XYZ option delta x XYZ volatility
```

Worked: `40 x $100 x .50 x .25 = $500` against `$200 x .50 x .20 = $20` per ABC call, so 25 ABC contracts, and `25 x $200 x .50 x .20 = 40 x $100 x .50 x .25`.

**The OEX/NYA trade.** OEX and NYA options trading at roughly the same implied volatility while NYA is expected to run at 87% of OEX. Balance: `number of OEX straddles x OEX $delta x .87 = number of NYA straddles x NYA $delta`, with `OEX $delta = 440 x $100 / 100 = $440` and `NYA $delta = 260 x $100 / 100 = $260`. Per NYA straddle sold, buy `.87 x 260/440 = about .51` OEX straddles, so 20 OEX 440 straddles against 39 NYA 260 straddles (`39 x .51 = 20`). "if both contracts move in the same direction and, as we expect, NYA volatility is 87% of OEX volatility, the position shows a constant profit equal to the expected 13% difference in the volatilities. Even if we double or triple volatility, the profit to the position will be identical, as long as NYA volatility is 87% of OEX volatility." Per-option dollar sensitivities at OEX 440.00, NYA 260.00, 70 days, 11% volatility, 5% rates (Cox-Ross-Rubenstein, no dividends, rounded):

| Option | $delta | $gamma | $theta | $vega |
|---|---|---|---|---|
| OEX 425 call | 364 | 23 | -8.57 | 49 |
| OEX 440 call | 259 | 36 | -9.29 | 75 |
| OEX 455 call | 140 | 33 | -6.87 | 69 |
| OEX 425 put | -81 | 25 | -3.09 | 51 |
| OEX 440 put | -196 | 42 | -4.00 | 74 |
| OEX 455 put | -339 | 43 | -2.36 | 54 |
| NYA 250 call | 221 | 13 | -4.93 | 27 |
| NYA 260 call | 152 | 21 | -5.49 | 44 |
| NYA 270 call | 75 | 18 | -4.05 | 39 |
| NYA 250 put | -41 | 13 | -1.85 | 28 |
| NYA 260 put | -117 | 24 | -2.36 | 44 |
| NYA 270 put | -211 | 26 | -1.26 | 28 |

**Position 1, straddle against straddle (p348):**

| Position | $delta | $gamma | $theta | $vega |
|---|---|---|---|---|
| long 20 OEX 440 calls | 5180 | 720 | -185.80 | 1500 |
| long 20 OEX 440 puts | -3920 | 840 | -80.00 | 1480 |
| short 39 NYA 260 calls | -5928 | -819 | 214.11 | -1716 |
| short 39 NYA 260 puts | 4563 | -936 | 92.04 | -1716 |
| **Totals** | **-105** | **-195** | **+40.35** | **-452** |

The $delta of -105 is "essentially $delta neutral," short about 24% of an OEX contract. The punchline is the correction: the raw totals read like a short straddle, but that only holds if the two markets move at the same rate, which is not the assumption. `$gamma: (720 + 840) - .87 x (819 + 936) = about 33`; `$vega: (1500 + 1480) - .87 x (1716 + 1716) = about -6`. General form (p349):

```
total $gamma = OEX $gamma + (NYA $gamma x [NYA volatility / OEX volatility])
total $theta = OEX $theta + (NYA $theta x [NYA volatility / OEX volatility])
total $vega  = OEX $vega  + (NYA $vega  x [NYA volatility / OEX volatility])
```

"our intermarket spread is insensitive to price movement, to the passage of time, and to changes in volatility, *as long as the NYA moves at 87% the rate of the OEX.*" Natenberg italicizes that closing clause because it carries all the risk.

**Position 2, straddle against strangle, layering an "implieds are too high" view (p349 to p350).** OEX 440 call $delta 259 against NYA 270 call $delta 75 gives 3.45 NYA calls per OEX call; OEX 440 put $delta -196 against NYA 250 put $delta -41 gives 4.78 NYA puts per OEX put. Buy 20 OEX 440 straddles, sell 69 NYA 270 calls and 96 NYA 250 puts.

| Position | $delta | $gamma | $theta | $vega |
|---|---|---|---|---|
| long 20 OEX 440 calls | 5180 | 720 | -185.80 | 1500 |
| long 20 OEX 440 puts | -3920 | 840 | -80.00 | 1480 |
| short 69 NYA 270 calls | -5175 | -1242 | 279.45 | -2691 |
| short 96 NYA 250 puts | 3936 | -1248 | 177.60 | -2688 |

```
$delta = 5180 - 3920 - 5175 + 3936                  = +21
$gamma = 720 + 840 - .87 x (1242 + 1248)            = -606
$theta = -185.80 - 80.00 + .87 x (279.45 + 177.60)  = +131.83
$vega  = 1500 + 1480 - .87 x (2691 + 2688)          = -1700
```

Negative $gamma, positive $theta and negative $vega mean the spread "will act like a short straddle," and the trader is also betting that implied volatilities in both markets are too high. Positions 1 and 2 check out exactly as printed.

**Position 3, strangle against straddle, layering an "implieds are too low" view (p350).** Ratio derivation: OEX 455 call $delta 140 against NYA 260 call $delta 152 gives about .92 NYA calls per OEX call; OEX 425 put $delta -81 against NYA 260 put $delta -117 gives about .69. Against 20 OEX 425/455 strangles, sell approximately 18 NYA 260 calls and 14 NYA 260 puts.

| Position | $delta | $gamma | $theta | $vega |
|---|---|---|---|---|
| long 20 OEX 455 calls | 2800 | 660 | -137.40 | 1380 |
| long 20 OEX 425 puts | -2736 | 500 | -61.80 | 1020 |
| short 18 NYA 260 calls | -1620 | -378 | 98.82 | -792 |
| short 16 NYA 260 puts | 1638 | -336 | 33.04 | -616 |

Corrected totals (see the misprint notes immediately below):

```
$delta = 2800 - 2736 - 1620 + 1638                 = +82
$gamma = 660 + 500 - .87 x (378 + 336)             = +539
$theta = -137.40 - 61.80 + .87 x (98.82 + 33.04)   = -84.48
$vega  = 1380 + 1020 - .87 x (792 + 616)           = +1175
```

> **MISPRINT NOTES, book p350, Position 3. Three separate defects, all carried here rather than silently fixed.**
>
> 1. **Sign errors in the printed totals.** The book prints $gamma = -1781, $theta = +84.48 and $vega = -1175. Working the printed expressions gives $gamma = 1160 - 621.18 = **+539**, $theta = -199.20 + 114.72 = **-84.48**, and $vega = 2400 - 1224.96 = **+1175**. The corrected signs are what Natenberg's own conclusion sentence requires, verbatim: "The positive $gamma, negative $theta, and positive $vega suggest that the spread will act like a long straddle: any large move in the underlying market or increase in volatility will help the position, and the passage of time or a decline in volatility will hurt the position. If we do such a spread, we are not only taking a position on the relative volatilities of the two underlying markets, we are also taking a position that the implied volatilities in the two markets are too low." Use the corrected values; do not reproduce the printed totals.
> 2. **Strike swap.** The position line in the text reads "buy 20 OEX 425 calls / buy 20 OEX 455 puts," while both the sensitivity table and the ratio derivation use the **455 calls and the 425 puts**. Use 455 calls and 425 puts.
> 3. **Contract count mismatch.** The text says sell 14 NYA 260 puts; the sensitivity table uses 16, and the table is what the totals are built from.

**The four-quadrant menu (p351)**, for layering an absolute-volatility view on top of the ratio view: positive $gamma / positive $vega is a backspread; negative $gamma / negative $vega is a ratio vertical spread; negative $gamma / positive $vega is a long time spread; positive $gamma / negative $vega is a short time spread.

### The crack-spread intermarket hedge (p335 to p336)

"since both heating oil and gasoline are derived from crude oil one would expect price movements in these three markets to be closely correlated." *Crack spreads* are "the spread between the price of crude oil and its derivative products." Products are quoted in cents per gallon and a barrel holds 42 gallons, so the product price is multiplied by 42.

```
crude/gasoline crack, crude $19.00/bbl, gasoline $.5400/gal:
    ($.54 x 42) - $19.00 = $3.68 per barrel
3:2:1 crack, crude $19.00, gasoline $.5400, heating oil $.5800:
    [(2 x 42 x $.5400) + (1 x 42 x $.5800) - (3 x $19.00)] / 3 = $4.24 per barrel
```

A refiner satisfied with the $4.24 margin can buy crude futures and sell gasoline and heating oil futures 3:2:1. Options substitution rule: "If he feels that implied volatility in crude oil is unusually low (high), he can take his long position by purchasing calls (selling puts). If he feels that implied volatility in gasoline is unusually low (high), he can take his short position by purchasing puts (selling calls)." Natenberg's footnote 2 is why the $delta machinery exists at all: "Although this is not a $delta neutral position, since the dollars at risk in crude oil are not equal to the dollars at risk in gasoline, it is still an intermarket spread since one market is being spread off against another market."

### Options on spreads (p351 to p352)

Forward-looking only: "such spreads are not currently traded on exchanges." ABC at 175 and XYZ at 150 puts the ABC over XYZ spread at 25, and a call on the spread struck at 25 pays 35 if the spread widens to 60 at expiration. Use case: a manager who believes one country's stock market will outperform another's buys a call on the spread between the two indexes, with unlimited profit potential and loss limited to the premium; a footnote adds that the currency risk between the two markets has to be offset separately. The modelling problem: "if ABC rises to 185 while XYZ rises to 200, the spread will have a value of -15. Most traditional theoretical pricing models, with their assumption of a lognormal distribution, do not allow for negative prices for the underlying contract ... a more realistic assumption might be a normal distribution, which does allow for negative prices. Such a variation on the Black-Scholes model has been suggested in a paper prepared by Darrell Wilcox." That variation is in Appendix B, outside this material.

### When the relationship breaks

- The volatility ratio is a band, not a point, so read the position at both edges. With NYA at 95% of OEX "our position will begin to act like a short straddle, and any increase in volatility will reduce the value of the position"; at 80% "our position will begin to act like a long straddle." Natenberg's own risk statement: "the risk would be that NYA volatility would increase relative to OEX volatility."
- Name the risk correctly. It is never "volatility rises," because the spread is insensitive to that. It is always a move in the ratio.
- The precondition is a shared driver. Corn and soybeans yes, corn and Deutschemarks no; gold and silver yes, gold and General Motors no. Closeness of relationship is the entry filter, not an output.
- Even highly correlated pairs drift in price as well as in volatility. Chapter 15's Figure 15-3 is the standing evidence: the S&P 500 minus S&P 100 spread ranged almost 20 index points over 1992 and 1993 and moved five points in a few weeks.
- Acting on uncorrected greeks means hedging a risk you do not have. Position 1 reads $gamma -195 and $vega -452 raw, and about +33 and about -6 once the .87 factor is applied.


## 9. Bull and bear spreads (Chapter 10)

Routing note: the phrase "bull call spread" routes to the existing `options-payoff` skill, which owns the payoff picture for every named structure below. That single leak is why this material lives in the reference doc rather than in a skill of its own. What follows is the part `options-payoff` does not own: strike selection, edge, greeks behaviour, and delta inversion. Canonical pages: book p199 to p211 (PDF p209 to p221), Figures 10-1 through 10-7.

### 9.1 The four ways to build directional exposure

| Construction | How the bias is built | Volatility view it embeds | Can the delta invert? |
|---|---|---|---|
| Naked positions | buy calls / sell puts = bullish; sell calls / buy puts = bearish | sell options if all overpriced (high IV); buy options if all underpriced (low IV) | no, but no margin for error |
| Bull/bear ratio spreads | run the ratio away from delta neutral | ratio vertical = short volatility (negative gamma); backspread = long volatility | yes |
| Bull/bear butterflies and time spreads | put the inside exercise price (butterfly) or the spread's exercise price (time spread) above/below the current underlying | long butterfly / long time spread = short volatility (negative gamma) | yes |
| Vertical spreads | buy the lower strike (bullish) / buy the higher strike (bearish) | secondary, but it decides *which* strikes | no |

Natenberg's routing rule, verbatim (book p202): *"It is common for traders to take bull or bear market positions by choosing appropriate ratio spreads, butterflies, or time spreads, but in each of these positions **volatility is still the primary concern**. A trader can be right about market direction, but if he is wrong about volatility, the spread may not retain the directional characteristics that the trader intended. If a trader focuses initially on the direction of the underlying market, he might look for a spread where the directional characteristics of the spread are the primary concern, and volatility is of secondary importance."* In one line: **volatility first, use a ratio spread, butterfly or time spread with a skewed bias; direction first, use a vertical spread.**

- **(a) Naked positions.** Bullish = buy calls or sell puts. Bearish = sell calls or buy puts. Pick the side that also expresses the volatility view: all options overpriced, sell puts to be bullish and sell calls to be bearish; all options underpriced, buy calls to be bullish and buy puts to be bearish. "As with all non-hedged positions, there is very little margin for error." Long options lose if the market moves the wrong way or simply fails to move enough to cover time premium; short options carry unlimited risk.
- **(b) Ratio spreads.** Bias by changing the ratio. Underlying 100, June 100 call delta 50, June 110 call delta 25. Delta-neutral ratio vertical: buy 1 June 100 call (50) / sell 2 June 110 calls (25); bullish version: buy 2 June 100 calls / sell 3 June 110 calls, total delta **+25**. Delta-neutral backspread: buy 2 June 110 calls (25) / sell 1 June 100 call (50); bullish version: buy 3 June 110 calls / sell 1 June 100 call, total delta **+25**.
- **(c) Butterflies.** Market at 100, a delta-neutral trader buys the June 95/100/105 call butterfly (buy a 95 call, sell two 100 calls, buy a 105 call), hoping the market sits at 100 so the butterfly "will widen to its maximum value of five points." Bullish butterfly = inside exercise price **above** the underlying (buy the June 105/110/115 call butterfly with the market at 100). Bearish butterfly = inside exercise price **below** the underlying.
- **(d) Time spreads.** "A long time spread always wants the near-term contract to expire exactly at-the-money. A long time spread will be initially bullish if the exercise price of the time spread is above the current price of the underlying market." Market at 100: the June/March 110 call time spread is bullish, the June/March 90 call time spread is bearish. Futures footnote (book p201, fn 1): different futures months may trade at different prices, so instead of a traditional time spread "the trader may have to choose a diagonal spread to ensure that the position is either bullish (delta positive) or bearish (delta negative)."

### 9.2 Every delta-inversion case the report records

1. **Ratio vertical, negative-gamma inversion.** If the market rises too quickly, to 130 or 140, all options go deeply in-the-money, both deltas approach 100, and the trader is left **-100 deltas**. "Even though the trader was correct in his bullish sentiment, the position was primarily a volatility spread."
2. **Backspread inversion, the mirror case.** A backspread inverts when the market is *less* volatile than expected. As time passes with no movement the June 100 call delta stays 50 but the June 110 call delta decays; when the 110's delta falls to 10, the +25 delta position becomes **-20**.
3. **Butterfly inversion.** A long butterfly has negative gamma. If the market runs from 100 to 120, the 105/110/115 butterfly now wants the market to fall back to 110. "Whenever the underlying market is below 110, the position will be bullish; whenever the underlying market is above 110, the position will be bearish."
4. **Time-spread inversion.** A long time spread also has negative gamma. 100 to 120 turns the bullish 110 time spread bearish; 100 to 80 turns the bearish 90 time spread bullish.
5. **Verticals cannot invert.** "Two options which have different exercise prices but which are identical in every other respect cannot have identical deltas." Long June 100 call / short June 105 call: the 100 call always has the greater delta, even when both are deeply in-the-money or far out-of-the-money. The vertical therefore "remain[s] bullish or bearish no matter how market conditions change."
6. **Delta drift, not inversion, but still unpriced risk.** "If volatility turns out to be lower than our estimate, the deltas will move away from 50. If volatility turns out to be higher than our estimate, the deltas will move towards 50." Mitigation: work around the at-the-money option and hold the strike gap constant, since spreads with the same gap keep roughly the same delta.

### 9.3 Vertical spreads: definition, sign rule, bounds

Definition (book p202): *"A vertical spread always consists of one long (purchased) option and one short (sold) option, where both options are of the same type (either both calls or both puts) and expire at the same time. The options are distinguished only by their different exercise prices."* The sign rule (book p204, italicized in the original): ***"Regardless of whether a vertical spread consists of calls or puts, whenever a trader buys the lower exercise price and sells the higher exercise price, the position is bullish; whenever a trader buys the higher exercise price and sells the lower exercise price, the position is bearish."*** Call and put verticals with the same strikes and expiration have approximately the same delta (footnote 2: assuming European options, no early exercise).

```
bull call spread:   buy a June 100 call / sell a June 105 call
bull put spread:    buy a June 100 put  / sell a June 105 put
bear call spread:   sell a June 100 call / buy a June 105 call
bear put spread:    sell a June 100 put  / buy a June 105 put
```

- **Expiration bounds.** "At expiration, a vertical spread will have a minimum value of zero, if both options are out-of-the-money, and a maximum value of the amount between exercise prices, if both options are in-the-money." A 100/105 call vertical trades somewhere in 0 to 5; a 95/105 put vertical somewhere in 0 to 10.
- **Two factors set total directional exposure** (book p205): the delta of the specific vertical spread, and the size in which the spread is executed. 500 deltas long = one 50-delta spread times 10, or one 25-delta spread times 20.
- **Delta scales with strike distance.** "The greater the distance between exercise prices, the greater the delta value associated with the spread. A 95/110 bull spread will be more bullish than a 100/110 bull spread, which will, in turn, be more bullish than a 100/105 bull spread." Figure 10-3 labels these *slightly bullish / moderately bullish / very bullish*.

### 9.4 The strike-selection rule

Derived from the Chapter 6 property (book p208): *"If we consider three options, an in-the-money, at-the-money, and out-of-the-money option which are identical except for their exercise prices, the at-the-money option is always the most sensitive in total points to a change in volatility."* Therefore, book p208, italicized, quote it verbatim: ***"If implied volatility is too low, vertical spreads should focus on purchasing the at-the-money option. If implied volatility is too high, vertical spreads should focus on selling the at-the-money options."***

- **The other leg is then forced.** Buy the ATM 100 call to be bullish and you must sell the OTM 105 call; sell the ATM 100 call to be bullish and you must buy the ITM 95 call.
- **Which option counts as at-the-money.** "It is usually best to focus on the option which is closest to at-the-money." Underlying at 103 with 95/100/105/110 available, focus on the 105 call. For **stock** options it is "the one whose delta is closest to 50", which is the strike closest to the **forward price** = current stock price + carrying costs - expected dividends.
- **Far-out spreads obey the same rule.** "Regardless of the exercise prices chosen, if implied volatility is low, the trader will attempt to buy the closer-to-the-money option, and if implied volatility is high, the trader will attempt to sell the closer-to-the-money option." A strongly bullish trader can buy the 115/120 call spread with the underlying at 100: very low delta, very low cost, executed many times, maximum 5 points if right.

Worked (Figures 10-4 and 10-5, futures at 100, 12 weeks, volatility 20%, interest 8%):

| | value at 20% | delta | price at 16% | edge if bought at 16% | price at 24% | edge if bought at 24% |
|---|---|---|---|---|---|---|
| 95/100 call spread | 2.87 | +20 | 3.01 | -.14 | 2.77 | +.10 |
| 100/105 call spread | 1.88 | +20 | 1.78 | +.10 | 1.94 | -.06 |

Same delta, opposite verdicts. At 16% (implied too low) buy the 100/105, because that buys the at-the-money 100 call. At 24% (implied too high) buy the 95/100, because that sells the at-the-money 100 call. Put example: a bear put spread with implied too low means buying the at-the-money 100 put, forced to sell the out-of-the-money 95 put; pay about 1.90 for a spread worth 2.04, giving **delta -20, edge +.14**.

### 9.5 Delta, gamma, theta and vega behaviour

**Figure 10-4.** Futures price = 100; Time = 12 weeks; Volatility = 20%; Interest = 8.00%.

| Option | Theoretical Value | Delta | Gamma | Theta | Vega |
|---|---|---|---|---|---|
| 95 call | 6.63 | 71 | 3.4 | -.017 | .16 |
| 100 call | 3.76 | 51 | 4.1 | -.022 | .19 |
| 105 call | 1.88 | 31 | 3.7 | -.020 | .17 |
| 95 put | 1.72 | -27 | 3.4 | -.019 | .16 |
| 100 put | 3.76 | -47 | 4.1 | -.022 | .19 |
| 105 put | 6.79 | -67 | 3.7 | -.019 | .17 |

**Figure 10-5.** Same contract at three implied volatilities, deltas in parentheses.

| Volatility | 95 Call | 95/100 Spread | 100 Call | 100/105 Spread | 105 Call |
|---|---|---|---|---|---|
| 16% | 6.02 | 3.01 | 3.01 | 1.78 | 1.23 |
| 20% | 6.63 (71) | 2.87 (20) | 3.76 (51) | 1.88 (20) | 1.88 (31) [E1] |
| 24% | 7.28 | 2.77 | 4.51 | 1.94 | 2.57 |

| Volatility | 95 Put | 95/100 Spread | 100 Put | 100/105 Spread | 105 Put |
|---|---|---|---|---|---|
| 16% | 1.11 | 1.90 | 3.01 | 3.13 | 6.14 |
| 20% | 1.72 (-27) | 2.04 (20) | 3.76 (-47) | 3.03 (20) | 6.79 (-67) |
| 24% | 2.37 | 2.14 | 4.51 | 2.97 | 7.48 |

Gamma and theta signature, verbatim (book p211): *"The 100/105 spread has a positive gamma and a negative theta, whereas the 95/100 spread has negative gamma and a positive theta."* So the combined direction-plus-volatility view routes the choice: bullish **and** expecting a big move, buy the 100/105, the out-of-the-money side, positive gamma and negative theta; bullish **but** expecting little movement, buy the 95/100, the in-the-money side, negative gamma and positive theta. "In both cases the trader is trying to maximize the return on his investment when he is right and minimize the loss when he is wrong."

**Cheaper is not better.** "If one leg of our spread always involves an at-the-money option, the vertical spread which includes the in-the-money option always has a higher price than the spread which includes the out-of-the-money option." Three cases with the 95/100 versus the 100/105 bull call spread: market 100 to 110, both win (both widen to 5); market 100 to 90, both lose (both collapse to 0); market stays at 100, the 100/105 collapses to zero while the 95/100 widens to its maximum 5. *"The 95/100 spread is always more valuable than the 100/105 spread because it has time on its side. The 100/105 spread needs the market to rise to show a profit. The 95/100 spread doesn't really need the market to rise; it just needs for the market not to fall."*

**Figure 10-6.** Stock price = 99; Time = 6 months; Volatility = 28%; Interest = 8.00% [E2].

| Option | Theoretical Value | Delta | Gamma | Theta | Vega |
|---|---|---|---|---|---|
| 95 call | 11.97 | 69 | 1.8 | -.031 | .24 |
| 105 call | 6.96 | **50** | 2.0 | -.030 | .27 |
| 115 call | 3.74 | 32 | 1.8 | -.025 | .25 |
| 95 put | 4.25 | -31 | 1.8 | -.013 | .22 |
| 105 put | 9.20 | -50 | 2.0 | -.011 | .26 |
| 115 put | 15.68 | -68 | 1.8 | -.004 | .24 |

The point of Figure 10-6: spot is 99 but the 50-delta option is the **105** strike, six points above spot, because in stock options the at-the-money option is the one nearest the forward price. Verticals therefore focus on the 105 call or put.

**Figure 10-7.** Same stock options at three implied volatilities, deltas in parentheses.

| Volatility | 95 Call | 95/105 Spread | 105 Call | 105/115 Spread | 115 Call |
|---|---|---|---|---|---|
| 23% | 10.77 | 5.20 | 5.57 | 3.05 | 2.52 |
| 28% | 11.97 (69) | 5.01 (19) | 6.96 (50) | 3.22 (18) | 3.74 (32) |
| 33% | 13.21 | 4.85 | 8.36 | 3.34 | 5.02 |

| Volatility | 95 Put [E3] | 95/105 Spread | 105 Put [E3] | 105/115 Spread | 115 Put [E3] |
|---|---|---|---|---|---|
| 23% | 3.05 | 4.41 | 7.46 | 6.56 | 14.02 |
| 28% | 4.25 (-31) | 4.60 (19) | 8.85 (-50) [E4] | 6.39 (19) | 15.24 (-68) [E4] |
| 33% | 5.49 | 4.76 | 10.25 | 6.27 | 16.52 |

- **Vertical versus outright underlying.** 500 deltas = 5 underlying contracts or 25 verticals at delta 20. "A vertical spread has limited risk while the position in the underlying has open-ended risk." Greater risk equals greater reward; the vertical's profits are capped "but he will also be much less bloodied if the market makes an unexpected move in the wrong direction." And by estimating volatility intelligently the option trader chooses whether time works for or against him: with positive theta he can profit where the outright trader breaks even.
- **Time-horizon gate, do this first.** "A trader who wants to use options to take advantage of an expected market move must first determine his time horizon." Foreseeing an upmove unlikely inside two months means June options make no sense; go September or December, accepting that "as he moves further and further out in time, market liquidity may become more of a problem."

### 9.6 Failure modes

- Choosing the spread with the lower price because the deltas match. "This ignores the purpose of option evaluation: to consider not only the initial cost of a strategy, but to compare that to the strategy's expected return."
- Getting the direction right and the volatility wrong, so the position loses its intended sign. That is the whole reason to prefer a vertical over a ratio spread, butterfly or time spread.
- Assuming a put vertical behaves opposite to a call vertical. It does not; see the sign rule.
- Treating the strike nearest spot as at-the-money in **stock** options. Use the delta nearest 50, that is the forward price.
- Legging in and forgetting the rule: "Regardless of how the spread is executed, the trader should focus on the at-the-money option, either buying it when implied volatility is too low, or selling it when implied volatility is too high."
- Going far out in time for the horizon and ignoring liquidity.

### 9.7 Errata for section 9

- **[E1]** Figure 10-5, 105 call on the 20% row. The scan is smudged and reads like `2.57 (31)`. The correct value is **1.88 (31)**, forced by the printed spreads (3.76 - 1.88) and matching Figure 10-4. Every other cell in both Figure 10-5 blocks reconciles against its neighbours.
- **[E2]** Figure 10-6 interest rate. The prose on book p209 says "interest rates of 10%" while the table header says 8.00%. This is a book inconsistency; the correct value is **8.00%** and the header governs.
- **[E3]** Figure 10-7, second block column headings. The source prints "Call" where it must read **"Put"**.
- **[E4]** Figure 10-7, 28% put row. The printed values 8.85 and 15.24 disagree with Figure 10-6 (9.20 and 15.68). Figure 10-7's internal arithmetic is self-consistent (8.85 - 4.25 = 4.60; 15.24 - 8.85 = 6.39), so **8.85 and 15.24 are correct within Figure 10-7** and must not be swapped for the Figure 10-6 numbers when reading Figure 10-7's spreads.

---

## 10. Trading without theoretical values (Chapter 11)

Verbatim section head `TRADING WITHOUT THEORETICAL VALUES`, book p235 to p240 (PDF p244 to p249), Figures 11-4 and 11-5. Premise: *"Synthetic relationships can often enable a trader to make logical trading decisions without the aid of values generated by a theoretical pricing model. Usually all that is required is an ability to calculate the carrying cost on a position and, in the case of stocks, to determine the dividend payout."*

**The governing rule** (book p237, italicized, quote verbatim): ***"Regardless of the exact theoretical value, there ought to be a uniform progression of both individual option prices and spread prices in the marketplace. If this uniform progression is violated, a trader can take advantage of the situation by purchasing the option or spread which is relatively cheap and selling the option or spread which is relatively expensive."***

**The audit order** (book p238, this is the procedure): *"The trader can start with conversions and reversals, then look at vertical spreads and butterflies, and finally consider straddles and time spreads. Usually there will not be any obvious mispricing. But if there is, the trader can exploit the situation by purchasing the cheap side of the relationship and selling the expensive."* Framing: "While the great majority of option traders work with theoretical values, a good habit for the new trader is to quickly check the relationship of option prices and spreads in the market to ensure that there are no obvious mispricings."

### 10.1 The monotonicity laws, each with its worked violation

- **(a) Synthetics first.** Check that `call - put` matches `underlying - strike` plus carry, less dividends, before anything else. In the 99.75 chain below, "we might check to make sure that all the synthetic relationships balance. Since they do, there is no profit opportunity there."
- **(b) A butterfly can never be worth less than zero.** Underlying 101.50: 95 call 8.00, 100 call 4.80, 105 call 1.60, so `(2 x 4.80) - (8.00 + 1.60) = 9.60 - 9.60 = 0`. "Since a butterfly can never be worth less than zero at expiration, and in this case might be worth as much as five points, the purchase of this butterfly represents a riskless trading opportunity." **This is the one genuinely riskless case in the section.**
- **(c) Equidistant vertical spreads.** "As long as there is an equal amount between exercise prices, a vertical call spread with lower exercise prices will always be more valuable than a vertical call spread with higher exercise prices. The opposite is true of vertical put spreads. Those with higher exercise prices are always more valuable than those with lower exercise prices." Same chain: `95/100 = 8.00 - 4.80 = 3.20` and `100/105 = 4.80 - 1.60 = 3.20`. Equal prices, so buy the 95/100 and sell the 100/105. "If he succeeds, he will have purchased the butterfly for zero. While there is no guarantee that this will be profitable (the underlying market could finish below 95 or above 105), the strategy still makes sense because there is no risk associated with it."

**(d) Straddles get more valuable as the strike moves away from the underlying.** Underlying 99.75, interest rate 0:

| | 95 | 100 | 105 |
|---|---|---|---|
| calls | 6.85 | 3.70 | 1.10 |
| puts | 2.10 | 3.95 | 6.35 |
| straddles (call + put) | 8.95 | 7.65 | 7.45 |

Synthetics balance at r = 0 and both butterflies are .55, "so it is not immediately apparent that they represent a good trading opportunity." But: "The 105 straddle, being further away from 99.75, should also be more valuable than the 100 straddle. But here the prices do not reflect the additional value. The 105 straddle is .30 cheaper than the 100 straddle." Trade: **buy the 105 straddle at 7.45, sell the 100 straddle at 7.65.** Honesty clause: "There is no guarantee that this strategy will be profitable. The underlying contract could finish above 105 ... But if we assume that movement is random, then the sale of the 100 straddle and the purchase of the 105 straddle puts the laws of probability heavily on the trader's side."

**(e) The nearer-month butterfly should be worth MORE than the far-month butterfly, and (f) the at-the-money time spread should be the most valuable.** Underlying 100.75, interest rate 0:

| | 95 | 100 | 105 |
|---|---|---|---|
| March calls | 7.50 | 3.85 | 2.35 |
| June calls | 9.65 | 5.70 | 3.30 |
| June call less March call (time spread) | 2.15 | 1.85 | .95 |

March butterfly = `(7.50 + 2.35) - (2 x 3.85) = 2.15`; June butterfly = `(9.65 + 3.30) - (2 x 5.70) = 1.55`. "It may seem that the June butterfly, with more time to expiration, ought to be more expensive. In option evaluation we usually associate more time with greater value. But if the market remains at 100.75, the price of the butterfly will expand towards 4.25 as time passes. Hence, it is logical that the March butterfly is more valuable than the June butterfly." (4.25 = the 5-point maximum less the 0.75 distance from the 100 strike.) On the time spreads: "The 100 time spread, being more at-the-money, is trading for more than the 105 time spread, as one would expect. The 100 time spread should also be more valuable than the 95 time spread. Here the 95 time spread is trading at a greater price, and, again, if we assume random movement in the underlying contract, this is clearly not logical." Verdict: "the 95 call time spread is too expensive **with respect to the 100 call time spread**. If we sell the former and buy the latter we can't be certain of a profit, but we do have the laws of probability on our side."

**The load-bearing qualifier.** Every verdict is relative: *"Even though we don't know the theoretical value of either the 100 or 105 straddle, we do know that the 105 straddle is too cheap **with respect to the 100 straddle**."* The audit never yields a theoretical value; it yields a pair.

### 10.2 The two printed reference chains and the trap inside them

Figure 11-4 (stock price 100; March 13 weeks, June 26 weeks; interest 8.00%; dividend 0; volatility 25%; strikes 80 to 120) and Figure 11-5 (futures price 50 [E5]; May 4 weeks, July 12 weeks; interest 8.00%; volatility 15%; strikes 46 to 54) print full chains with every vertical, butterfly, straddle and time spread already differenced out, so the whole audit runs by eye. Two printed values look like violations and are not: Figure 11-4's put time spreads go **negative** at the 115 and 120 strikes (**-.12** and **-.69**), and Figure 11-5's 46-strike May call sits at **3.99**, below its 4.00 parity. Both are the European-pricing artefact, and a live illustration of where the uniform-progression heuristic needs the early-exercise caveat from Chapter 12. Figure 11-4/11-5 footnote, verbatim: *"Since all options are assumed to be European, with no early exercise permitted, some theoretical values may be less than parity and some spreads may have negative values. The effect of early exercise on spread values will be discussed in Chapter 12."* Every other cell in both figures reconciles against its neighbours (straddle = call + put; vertical = adjacent difference; butterfly = second difference; time spread = far month less near month), apart from the two scan defects at [E6] and [E7].

### 10.3 Failure modes

- Reporting "the butterfly is priced at .55, that's positive, nothing to see" and stopping. A positive butterfly only clears law (b); laws (c) through (f) can still be violated on the same chain.
- Treating (d), (e) and (f) as riskless. Only the zero-or-negative butterfly is riskless; the rest are probability edges under an assumption of random movement, and the book says so explicitly each time.
- Assuming more time means more value for a **butterfly**. It is the reverse when the underlying sits near the inside strike.
- Comparing vertical spreads whose strike gaps are unequal. The monotonicity law requires "an equal amount between exercise prices."
- Running the audit out of order and missing a live conversion or reversal imbalance, which pays first and is the least risky.
- Forgetting carry and dividends when the interest rate is not zero. Both worked chains set r = 0.

### 10.4 Errata for section 10

- **[E5]** Figure 11-5 header. The futures price prints as `.50`. The correct value is **50**, forced by the 46 to 54 strike range and by every price in the table.
- **[E6]** Figure 11-5, 47-strike May straddle. The scan prints like `2.11`. The correct value is **3.11** (3.04 + .07).
- **[E7]** Figure 11-5, 47-strike call time spread. The scan prints like `.18`. The correct value is **.28** (3.32 - 3.04).

---

## 11. Expiration straddles (Chapter 18)

Verbatim subhead `Expiration Straddles` under `TRADING IS CONTINUOUS`, book p398 to p399 (PDF p406 to p407); it depends on the gap mechanics at book p394 to p398 and on Figure 18-4. **What it is:** the deliberate purchase of at-the-money straddles close to expiration, when the market is discounting gap risk and the model is known to be wrong in the buyer's favour.

- **The inversion.** "If it is dangerous to sell at-the-money options going into expiration, perhaps there is some sense in taking the opposite position by purchasing at-the-money options as expiration approaches. This may seem to contradict conventional option wisdom, which contends that a trader should sell at-the-money options in order to take advantage of the rapid time decay associated with such options."
- **The risk and reward argument.** "If one sells at-the-money options, the reward may be an accelerated profit if the market doesn't move (**high positive theta**). But the risk is an increased loss if the market does move (**high negative gamma**). **Because the model does not know about the possibility of a gap in the underlying market, the risk is often greater than the reward.** If one sells at-the-money options, the losses from an occasional gap will more than offset the profits resulting from increased time decay. An experienced trader will therefore tend to do the opposite of conventional wisdom. If conditions are right, he will tend to buy at-the-money options close to expiration."
- **When the opportunity exists.** Not every cycle. "As with any strategy, conditions must make the strategy attractive. But **because so many traders are intent on selling time premium as expiration approaches, it is often possible to find cheap at-the-money options.**"
- **The screen, with the printed numbers.** "Suppose that with three days remaining to expiration the Black-Scholes model generates a value for an at-the-money call of .50, but that it is priced at .45. What can we say about this call? While we may not know the exact value, we can certainly say that the call is likely to be worth more than .50, since **there is always the possibility of a gap in the market**. Clearly, if the call is trading at .45, but has a value in excess of .50, it must be a good buy."
- **Why the straddle and not the call.** "Because of the synthetic relationship, **if the calls are underpriced the puts at the same exercise price will also be underpriced. A logical strategy might be the purchase of at-the-money straddles.** This enables a trader to buy both underpriced calls and underpriced puts, and to profit if the underlying market gaps either up or down."
- **The don't-adjust rule.** "With little time remaining to expiration the model is not only unreliable with respect to theoretical values, **it is also unreliable with respect to deltas. Because it is impossible to say what the right delta is, it is also impossible to say what the correct adjustment is.** For this reason, traders who initiate expiration straddles often forget about trying to adjust, and simply sit on the position to expiration."

**The numbers that size the opportunity, Figure 18-4** (book p396). Implied Volatility = 20%; Interest Rate = 6%. A trader sells the 100 straddle with the future at 100 and the market immediately gaps to 105.

| | 9 months, futures at 100 | 9 months, futures at 105 | 1 day, futures at 100 | 1 day, futures at 105 |
|---|---|---|---|---|
| 100 call price | 6.59 | 9.41 | .42 | 5.00 |
| 100 put price | 6.59 | 4.63 | .42 | 0 |
| 100 straddle price | 13.18 | 14.04 | .84 | 5.00 |

Derived and printed in the text: the straddle rose about **7%** at nine months (14.04 / 13.18 = 1.07), "painful"; and **495%** at one day (5.00 / .84 = 5.95), "devastating". **Gamma of the 100 call and put: 2.2 with nine months to expiration, 38.1 with one day to expiration.** Footnote 8: for simplicity the example assumes no change in implied volatility after the gap, "Admittedly, this is unlikely to be the case."

**The expectancy and sizing rule** (roulette analogy from Chapter 3). A player who buys a number at a roulette table "can expect to win only once in 38 plays. But if the theoretical value of the bet is 95 cents, and the player can buy the bet for less than 95 cents, he expects to be a winner in the long run. If he pays a very low price for the bet, say 50 cents, he still expects to lose 37 times out of 38. But now the bet is very attractive because even if he only wins once in 38 plays, this will still be often enough to more than offset the small losses he takes each time he loses. The same logic is true of expiration straddles." Hence: ***"Because a trader knows that he will lose much more often than he will win, a trader should only invest an amount in expiration straddles which he is prepared to lose. But when conditions are right, a trader ought to be willing to make the investment. Even if he loses several times in succession, in the long run he will encounter gaps in the market, or sudden increases in volatility, often enough to make such strategies profitable."***

**The mirror-image prohibition** (same section, book p398): "it can be very dangerous to sell a large number of at-the-money options close to expiration ... New traders, in particular, are advised to avoid such positions. No risk manager will appreciate even experienced traders being short large numbers of at-the-money options as expiration approaches."

**Failure modes.** Judging the strategy by a single expiration cycle instead of long-run expectancy; buying at-the-money options near expiry indiscriminately rather than only when they are cheap to model value; delta-hedging off model deltas known to be unreliable; sizing it like a normal volatility position rather than as an amount you are prepared to lose outright; buying only the call or only the put when the synthetic relationship says both sides are cheap and the gap can go either way.

---

## 12. A final thought (Chapter 18)

Verbatim section head `A FINAL THOUGHT`, book p416 to p418 (PDF p424 to p426). It is a governing principle, not a framework: no procedure, no sub-rules. Reproduced complete.

> "Because the use of a theoretical pricing model requires a trader to make so many different decisions, both with respect to the inputs into the model and the degree to which the assumptions on which the model is based are likely to be accurate, the new option trader may feel that making the right decisions is simply a matter of luck. While luck undoubtedly plays a role in the short run, in the long run those traders who are willing to put in the effort required to understand how models work always seem to come out ahead. Experienced traders know that using a model, with all its problems, is still the best way to evaluate options and manage risk.
>
> This text, like many others on options, may have left the reader with the impression that option evaluation and trading can be reduced to a series of arithmetic calculations. The science of option evaluation is an important part of any trader's education, but mathematical models are only a tool to help the trader make decisions. Successful option trading is at least as much an art as a science, and a trader must know where science leaves off, and other intangible assets, whether intuition or market feel or experience, begin. This brings us to one final point, and perhaps the most important principle of option trading: **there is no substitute for common sense**. A trader who slavishly uses a model to make every trading decision is heading for disaster. **Only a trader who fully understands what a model can and cannot do will be able to make the model his servant rather than his master.**"

---

## 13. What Natenberg deliberately leaves out (Chapter 14)

Two topics inside "Volatility Revisited" are raised by name and then abandoned by the author. Their absence from the carved skill family is a decision, not an oversight. Do not build a skill on either, and do not route either to an existing skill as a substitute.

### 13.1 ARCH and GARCH: named, footnoted, declared out of scope

Book p280 to p281 (PDF p289 to p290), inside `VOLATILITY FORECASTING`, verbatim: *"Theoreticians have recently tried to take essentially the same approach to volatility forecasting, and this has led to the development of autoregressive conditional heteroskedasticity (ARCH) and generalized autoregressive conditional heteroskedasticity (GARCH) volatility models. A detailed discussion of such models is beyond the scope of this text, since they can be mathematically complex and are **not widely used among traders**. Nevertheless, an option trader should be aware that these models do exist, and that they are simply an attempt to apply the **mean reverting and serial correlation** characteristics of volatility to volatility forecasting."*

His reasoning, in his own terms: the models are mathematically complex, they are not widely used among traders, and they add nothing conceptually new to the two properties he has already taught by hand. The correct treatment is one paragraph inside a volatility-forecasting skill, framed as the formalized version of mean reversion plus serial correlation. The matching failure mode he warns against is "treating GARCH output as categorically better." Footnote 2 citations, as printed:

| Author | Title | Publication | Pages |
|---|---|---|---|
| Engle, R.F. (1982) | "Autoregressive Conditional Heteroskedaticity with Estimates of the Variance of United Kingdom Inflation" | *Econometrica*, Vol. 50, No. 4 | 987 to 1000 |
| Bollerslev, T. (April 1986) | "Generalized Autoregressive Conditional Heteroskedasticity" | *Journal of Econometrics*, No. 31 [E8] | 307 to 327 |
| Bollerslev, T. (August 1987) | "A Conditional Heteroskedastic Time Series Model for Speculative Prices and Rates of Return" | *Review of Economics and Statistics*, No. 69 | 542 to 547 |
| Nelson, David B. (1991) | "Conditional Heteroskedasticity in Asset Returns: A New Approach" | *Econometrica*, No. 59 | 347 to 370 |
| Kuberek, Robert C. (March 1992) | "Predicting Interest Rate Volatility: A Conditional Heteroskedastic Model of Interest Rate Movements" | *Journal of Fixed Income*, Vol. 1, No. 4 | 21 to 27 |

### 13.2 Technical analysis applied to volatility charts: raised, then handed back to the reader

Book p275 (PDF p284), inside `SOME VOLATILITY CHARACTERISTICS`, immediately after Figure 14-4 establishes that volatility itself trends (down July 1989 to June 1990, up July 1990 to April 1991, down April 1991 to October 1991, with minor trends inside the major ones). Verbatim: *"In this respect volatility charts seem to display some of the same characteristics as price charts, and it would not be unreasonable to apply some of the same principles used in technical analysis to volatility analysis. It is important to remember, however, that while price changes and volatility are related, they are not the same thing. If a trader tries to apply exactly the same rules of technical analysis to volatility analysis, he is likely to find that in some cases the rules have no relevance, and that in other cases the rules must be modified to take into account the unique characteristics of volatility."*

He then declines to develop it, verbatim: *"Since the author claims no particular expertise in the area of technical analysis, the reader is left to his own devices in this regard."* There is no method here. The one operative instruction he does give is negative, and it survives as a failure mode: do not treat the volatility cone's mean as a price-style support or resistance level, and do not apply technical-analysis rules to a volatility chart verbatim.

### 13.3 Errata for section 13

- **[E8]** Bollerslev 1986 citation. The chapter footnote prints the journal as *Journal of Economics*. The correct title is ***Journal of Econometrics***.


## 14. Errata across the whole book

Every entry below was found by an extraction pass reading the page images directly. Where a skill
in this family prints one of these numbers, it prints the corrected value with a footnote. None of
these are silently corrected and none are silently reproduced.

| Where | Printed | Correct, or the note |
|---|---|---|
| Ch 6, Figure 6-25 header | Volatility = 20.5% | Body text on book p120 says 22%. The header is more likely right given the implied-volatility column. Both recorded. |
| Ch 7, "Why Spread?" | "$6 loss on the February side" | The consistent figure is $10. |
| Ch 7, spread ratio | "9 NYSE = 4 S&P 500" | Must be 9:5. |
| Ch 9, Figure 9-2 Spread 2 | delta and edge cells | Internally inconsistent. Recomputed from Figure 9-1 to +31 / -.20, confirmed against Figure 9-3. |
| Ch 9, Figure 9-7 Spread 5 | vega .103 / -1.850 | An alternative reading is .092 / -1.30. The book carries -1.850 downstream, so -1.850 stands. |
| Ch 10, Figure 10-5 | 105 call 2.57 | 1.88 (31). |
| Ch 10, Figure 10-6 | prose says 10% interest | The figure uses 8.00%. |
| Ch 10, Figure 10-7 | second-block column heads read Call | They are Put. The 8.85 / 15.24 values govern within 10-7. |
| Ch 11, conversion arithmetic | 4.90 | 4.95. |
| Ch 11, Figure 11-5 header | ".50" | 50 (a futures price, not a decimal). |
| Ch 11, 47-strike May straddle | as printed | 3.11. |
| Ch 11, 47-strike call time spread | as printed | .28. |
| Ch 13, Figure 13-7 | row alignment | Unrecoverable from the sideways scan. Published as a strategy inventory in source order, never as a table. |
| Ch 15, book p350 Position 3 | -1781 / +84.48 / -1175 | Signs contradict the arithmetic and Natenberg's own conclusion sentence. Corrected to +539 / -84.48 / +1175. The same example also swaps the 425 and 455 strikes and disagrees with itself on 14 versus 16 NYA puts. |
| Ch 17, Example 2 | vega -.760 | Computes to -1.760. |
| Ch 18 | (absent terms) | "Investment skew" and "forward skew" do **not** appear in this edition. Natenberg says smile, symmetrical, asymmetrical, inflated, deflated, and wings raised or lowered. |
| Ch 5 | (absence) | Natenberg makes no claim that a trader captures only a fraction of theoretical edge. He shows +62.81 realized against +63.00 predicted. Do not invent a capture percentage. |
| Ch 16 | (absence) | No correlation formula and no spread-volatility formula is printed. The cross-market adjustment is an empirically read volatility ratio, NYA about 87% of OEX, band 80 to 95%. |
| Ch 15 | (absence) | Equal-dollar-weighted index construction is not covered. Only price weighted and capitalization weighted. |
| Ch 14, citation | Bollerslev 1986 | *Journal of Econometrics*. |
