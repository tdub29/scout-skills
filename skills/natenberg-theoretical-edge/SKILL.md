---
name: natenberg-theoretical-edge
description: Builds an option's theoretical value from a hand-specified probability distribution of expiration prices, deducts carrying cost, adds dividends, and turns the gap between that value and the market price into a buy / sell / no-trade call plus a validated input vector for the pricing model. Use when the user says "is this option cheap", "what is this option actually worth", "price this call from my own probabilities", "my model disagrees with the market, which input is wrong", "what interest rate should I use", "bid or offer for the underlying", "do I use calendar days or trading days", "the stock goes ex-dividend right before expiration", or "compute the theoretical edge". Produces a dollar theoretical value, a signed theoretical edge, and a per-input go/no-go on what was fed into the model. From Sheldon Natenberg, Option Volatility and Pricing, Chapter 3.
---

# Natenberg Theoretical Edge

## What this decides

Given an underlying price, a set of possible expiration prices with probabilities, a rate, a term, and (for stock) a dividend, this decides three things:

1. The option's theoretical value in dollars.
2. Whether the market price is above or below it, and by how much (the theoretical edge).
3. Whether each input you fed the model was the right number, or whether a wrong input explains the disagreement.

Scope note: `position-sizing-expectancy` already owns generic expectancy and bet-sizing prompts, so this skill stays on option theoretical value and never claims the plain "what is the EV of this bet" surface.

Decide by: if you cannot state a probability for every proposed expiration price, you have not started step 1 and there is no value to compute yet.

## A word on models (read before trusting any number below)

- "A model is a scaled down or more easily managed representation of the real world."
- Natenberg's own italics: "*However, it is unwise, and sometimes dangerous, to assume that the model and the real world which it represents are identical in every way.*"
- "If we feed incorrect data into the model, we can expect an incorrect representation of the real world. Every model user must be aware: **garbage in, garbage out**."
- "An option model is only someone's idea of how options might be evaluated under certain conditions." There is no guarantee model values are accurate, nor that they resemble actual market prices.
- The candle analogy: a trader without a model gropes in a dark room; a trader with a basic grasp of pricing models "enters the same room with a small candle." He sees the layout, but the dimness hides detail and the flicker distorts some of it. Still better than no light.
- The size trap: "The real problems with theoretical pricing models arise **after** the trader has acquired some sophistication." As he gains confidence he raises size, and "any error in judgement will be greatly magnified."
- Spectrum of opinion: some traders think models are "so much hocus-pocus," others think a sheet of theoretical values solves everything. "The reality lies somewhere in between."

Decide by: before you scale size on a model-derived edge, name which input you are least sure of. If you cannot name one, you are in the second camp above and should not scale.

Further reading Natenberg cites (footnote 2): Figlewski, Stephen, "What Does an Option Pricing Model Tell Us about Option Prices?", *Financial Analysts Journal*, September/October 1989, pages 12-15. Black, Fischer, "Living Up to the Model," *Risk*, Vol. 3, No. 3, March 1990, pages 11-13.

## The five steps in developing a model

Natenberg's summary line is "We can now summarize the necessary steps in developing a model:" followed by (book p43):

1. "Propose a series of possible prices at expiration for the underlying contract"
2. "Assign an appropriate probability to each possible price"
3. "Maintain an arbitrage-free underlying market"
4. "From the prices and probabilities in steps 1, 2, and 3, calculate the expected return for the option"
5. "From the option's expected return, deduct the carrying cost"

"If we can accomplish all this, we will finally have a theoretical value from which we can begin to trade."

Decide by: run the five steps in order. If any step is unfilled, stop and say which one; do not output a value.

## Step 4 machinery: expected return

Expected return = sum over outcomes of (probability x payoff).

Die roll paying $1 through $6: 1+2+3+4+5+6 = 21, and 21/6 = 3 1/2. "That is, on average we can expect to get back $3 1/2 each time we roll the die." Pay less than $3.50 and you expect to win in the long run; pay more and you expect to lose; pay exactly $3.50 and you break even. The qualifier matters: the expected return "is a realistic goal only if we are allowed to roll the die many, many times." On a single roll it is impossible to get back exactly $3 1/2, since no face has 3 1/2 spots.

Roulette worked example (the edge definition). A US wheel has 38 slots, numbered 1 through 36 plus 0 and 00. The player picks one number; a hit pays $36, a miss pays nothing.

| Quantity | Value |
|---|---|
| Slots | 38 (1 through 36, plus 0 and 00) |
| Payout on a hit | $36 |
| Expected return | $36 / 38 = $.9474, "or about 95 cents" |
| Casino's price | $1 |
| Casino edge | 5 cents per dollar bet |
| If a casino sold the same bet at 88 cents | Player edge = 7 cents |

"In the long run, for every dollar bet at the roulette table, the casino can expect to keep about 5 cents." A profit-seeking player would rather switch places and be the house, or find the casino selling the bet at 88 cents.

For a call, expected return can never be negative, because a call can never be worth less than zero.

Decide by: compute sum(probability x payoff). Compare it to the price. Whoever is on the cheap side of that comparison owns the edge, and you take that side or pass.

## Step 5: carrying cost, dividends, and theoretical value

Definition (book p37): "The theoretical value of a proposition is the price one would expect to pay in order to just break even in the long run."

Carrying cost applied to the roulette bet: the player pays 95 cents today, but the $36 of winnings arrives in two months. Interest rates are 12% annually, which the chapter treats as 1% per month, so two months = 2%. 2% x 95 cents is about 2 cents.

| Step | Amount |
|---|---|
| Expected return | 95 cents |
| Less two months of carry at 2% | -2 cents |
| Theoretical value | **about 93 cents** |
| Plus a 1 cent bonus paid over the two months (the dividend analogue) | +1 cent |
| Theoretical value with the bonus | **94 cents** |

"The two most common considerations in a financial investment are the expected return and carrying costs." The 1 cent bonus "is similar to the dividend paid to owners of stock in a company."

Insurance framing Natenberg uses for the same arithmetic: the actuary computes the likelihood of paying out, factors in what the company earns on premiums, arrives at a theoretical value, then offers the policy at an additional cost that "represents the theoretical edge to the insurance company."

Decide by: theoretical value = expected return - carrying cost + dividends. Carrying cost = rate x time x amount. If you stopped at expected return, your number is wrong by the carry.

## Step 3: the arbitrage-free constraint and the forward price

A positive expected return on the underlying is not free money. Under stock-type settlement there is a carrying cost on the purchase. If carrying cost exactly equals the expected return, the trade just breaks even. "If we assume that any stock trade will just break even, the expected return must be equal to the carrying costs." With a dividend, expected return = carrying costs less dividends.

Worked: carrying cost over the period $3.50, dividend expected $1.00, therefore the required expected return at the end of the period is **$2.50**. The $3.50 interest debit is offset by the $1.00 dividend plus the $2.50 expected return. (Footnote 3: the trader also earns interest on the dividend from receipt to the end of the holding period; usually very small, ignored.)

"In an *arbitrage-free* market, where no profit can be made by either buying or selling a contract, all credits and debits, including the expected return, must exactly cancel out."

Forward price = "the average price of the contract at the end of the holding period" = the current price plus an expected return that exactly offsets all other credits and debits.

| Case | Forward price |
|---|---|
| $100 stock, $4 holding cost over the period | $104 |
| Same stock, also pays a $1 dividend | $103 |
| Futures contract at $100 (no cash outlay, no dividends) | $100, same as current price |

Inputs to a stock forward price: "the price of the stock, the length of the holding period, interest rates, and dividends." Buy a futures at $100 and the break-even price at the end of the holding period is $100; expected return is zero.

Model lineage, which is how you pick the right forward-price form: 1973 Black-Scholes (European options on non-dividend-paying stocks, introduced concurrently with the opening of the CBOE; a dividend component was added shortly after); 1976 the Black Model for options on futures; 1983 the Garman-Kohlhagen Model for options on foreign currencies (footnote 5: on a physical foreign currency, not on a foreign currency futures contract, which uses the Black futures model). "The various forms of the model differ primarily in how they calculate the forward price of the underlying contract, and an option trader will simply choose the form appropriate to the underlying instrument."

Decide by: compute the forward price for your instrument. If your distribution's mean does not sit at the forward price, your probabilities violate step 3 and must be reshaped before step 4.

## Worked distributions: Figures 3-1, 3-2, 3-3

All three assume the underlying is trading at $100 and price the $100 call, with two months to expiration and 12% annual interest (2% over the period) under stock-type settlement.

**Figure 3-1 (book p40), flat distribution:**

| $80 | $90 | $100 | $110 | $120 |
|---|---|---|---|---|
| 20% | 20% | 20% | 20% | 20% |

Long underlying at $100, expected return:
`-(20% x $20) -(20% x $10) +(20% x 0) +(20% x $10) +(20% x $20) = 0`

Long the $100 call, expected return:
`(20% x 0) +(20% x 0) +(20% x 0) +(20% x $10) +(20% x $20) = +$6`

"The call can never be worth less than zero, so the expected return from the call position is always a non-negative number, in this case $6." Deduct the 2% carrying cost, "about 12 cents": **theoretical value = $5.88**.

**Figure 3-2 (book p42), concentrated and symmetric:**

| $80 | $90 | $100 | $110 | $120 |
|---|---|---|---|---|
| 10% | 20% | 40% | 20% | 10% |

$100 call expected return:
`(10% x 0) +(20% x 0) +(40% x 0) +(20% x $10) +(10% x $20) = $4.00`

After the 2% carry, **theoretical value = $3.92**. The underlying's expected return is still zero because the distribution is symmetric.

Why reshape from 3-1 to 3-2: "most traders would probably agree that extreme price changes which are far away from today's price are less likely than small changes which remain close to today's price." Natenberg's test case: with the underlying at $100, is $110 or $250 the more likely expiration price? $110.

**Figure 3-3 (book p42), skewed:**

| $80 | $90 | $100 | $110 | $120 |
|---|---|---|---|---|
| 10% | 20% | 30% | 25% | 15% |

Long underlying expected return:
`-(10% x $20) -(20% x $10) +(30% x 0) +(25% x $10) +(15% x $20) = +$1.50`

$100 call expected return:
`(10% x 0) +(20% x 0) +(30% x 0) +(25% x $10) +(15% x $20) = +$5.50`

Real-world fidelity requires an infinite probability line, not five buckets. "This may seem an impossible task, but it is the basis for all theoretical pricing models."

Decide by: run your own distribution through the same arithmetic. If a flat line and a concentrated line give materially different values ($6 versus $4.00 on the identical five prices), the shape of your distribution is doing more work than any other assumption, and that is where to spend the scrutiny.

## The trade rule and the theoretical edge

Natenberg's rule (book p46): "If a call can be purchased (sold) for less (more) than its theoretical value, it will, in the long run, be more profitable to take a long (short) market position by purchasing (selling) calls than by purchasing (selling) the underlying contract. In the same way, if a put can be purchased (sold) for less (more) than its theoretical value, it will, in the long run, be more profitable to take a short (long) market position by purchasing (selling) puts than by selling (buying) the underlying contract."

| Situation | Action |
|---|---|
| Call priced below theoretical value | Buy the call rather than buy the underlying |
| Call priced above theoretical value | Sell the call rather than sell the underlying |
| Put priced below theoretical value | Buy the put rather than sell the underlying |
| Put priced above theoretical value | Sell the put rather than buy the underlying |

Theoretical edge is the gap between the market price and the theoretical value, taken in your favor. It is the same quantity as the casino's 5 cents on a 95 cent bet priced at $1, and the same quantity as the player's 7 cents when the bet is offered at 88 cents.

The goal, in Natenberg's words: "the goal of option evaluation is to determine, through the use of theoretical pricing models, the theoretical value of an option. The trader can then make an intelligent decision whether the option is overpriced or underpriced in the marketplace, and whether the theoretical edge is sufficient to justify going into the marketplace and making a trade."

The hedge is not optional. "For every option position there is a theoretically equivalent position in the underlying contract such that, for small price changes in the underlying contract, the option position will gain or lose value at exactly the same rate as the underlying position." The proportion required is the *hedge ratio*. It is required because theoretical value depends on the probabilities, and those probabilities move as the underlying moves: "if the underlying price is currently $100 and we assign a 25% probability to $120, we might drop the probability for $120 to 10% if the price of the underlying contract falls to $80." A call is a substitute for a long position; a put is a substitute for a short position. Chapter 3 names the hedge ratio but gives no numeric method for it.

Decide by: edge = |market price - theoretical value|, signed in your favor. Trade only if that edge is large enough to justify entering, and only alongside the opposing underlying position.

## Model inputs and per-input hygiene

"In order to calculate an option's theoretical value using the Black-Scholes Model, we need to know at a minimum five characteristics of the option and its underlying contract" (book p44):

1. The option's exercise price
2. The amount of time remaining to expiration
3. The current price of the underlying contract
4. The risk-free interest rate over the life of the option
5. The volatility of the underlying contract

Figure 3-4 draws Exercise Price / Time to Expiration / Underlying Price / Interest Rates / Volatility feeding a **Theoretical Pricing Model** which outputs a **Theoretical Value**. Dividends are deliberately left out of Figure 3-4 "since they are only a factor in the theoretical evaluation of stock options, and then only if the stock is expected to pay a dividend over the life of the option." That makes six inputs for a dividend-paying stock option.

"Since the theoretical value obtained from a theoretical pricing model is no better than the inputs into the model, a few comments on each of the inputs will be worthwhile."

### Exercise price

Fixed in the contract terms and does not vary over the contract's life. "A Deutschemark March 58 call traded on the Chicago Mercantile Exchange cannot suddenly turn into a March 59 call or a March 57 call. An IBM July 55 put traded on the Chicago Board Options Exchange cannot turn into a July 50 put or a July 60 put." Footnote 6: an exchange may adjust the exercise price on a stock split, but in practical terms this is not a change, because the exercise price retains the same relationship to the stock price.

Decide by: read it off the contract. If this input is in dispute, the dispute is a data error, not a modeling question.

### Time to expiration

The expiration date is fixed by the exchange; only the remaining time shrinks. "Time to expiration, like all inputs in the Black-Scholes Model, is entered as an **annualized number**."

| Days remaining | Annualized input |
|---|---|
| 91 | .25 (91/365) |
| 36 | .10 (36/365) |

Most evaluation programs do this transformation internally, so you enter days remaining.

The calendar-versus-trading-day conflict, and Natenberg's resolution: time is needed for two purposes. Interest accrues **every** day, business day or not. But for the likelihood of movement, the "speed" of the market, "we are only interested in trading days. Only on those days can the price of the underlying contract actually change." The resolution: "In calculating the 'speed' of the market we observe only the price changes that occur on business days. But we can make slight changes to this observed value and annualize the number before feeding it into the theoretical pricing model. The result is that we can feed into our model the **actual number of days remaining to expiration** knowing that the model will interpret the number correctly."

Decide by: feed the actual calendar days remaining to expiration. The trading-day adjustment lives inside the volatility number, not in the day count.

### Price of the underlying: bid versus asked

"The underlying price we feed into our theoretical pricing model ought to be the price at which we believe we can make the opposing trade," because correct use of a theoretical value requires hedging the option with an opposing trade in the underlying.

| Intended option trade | Market position | Hedge in the underlying | Price to feed |
|---|---|---|---|
| Buy calls, or sell puts | Long | Sell the underlying | **Bid** |
| Sell calls, or buy puts | Short | Buy the underlying | **Asked** |

Why the last trade price is unsafe: "the last trade price may not always reflect the present market. Even the settlement price quoted in a newspaper may not accurately reflect the market at the close of business." Worked case: the last trade prints 75 1/4, but the close was 75 1/4 bid and 75 1/2 offered. A trader hoping to buy at 75 1/4 has very little chance of being filled, and even 75 3/8 may be unlikely "if the market is very unbalanced with many more contracts being bid for at 75 1/4 than offered at 75 1/2." Conclusion: "an experienced trader will rarely enter an option market without knowing the exact bid and offer in the underlying market."

Decide by: name your hedge direction first, then pick the side of the market you would actually get filled on. Never feed a last trade or a newspaper settlement price.

### Interest rates: two roles, one or two inputs

"The interest rate component plays two roles in the theoretical evaluation of options."

1. It may affect the **forward price of the underlying contract**. Under stock-type settlement of the underlying: as we raise interest rates we raise the forward price, **increasing the value of calls and decreasing the value of puts**.
2. It may affect the **cost of carrying the option**. If the option is subject to stock-type settlement: as we raise interest rates we **decrease the value of the option**, both calls and puts.

Usually the same rate serves both roles, so the model takes one interest-rate input. When different rates apply, as with foreign currency options where the foreign rate plays one role and the domestic rate the other, the model requires **two** interest rates. That is the Garman-Kohlhagen version.

Relative importance: "interest rates have a much greater impact on the value of stock options than on futures options. As we raise interest rates, we increase the forward price of stock, but leave the forward price of a futures contract unchanged." The carry-on-the-option effect exists too, but the option price "is usually very small in relation to the price of the underlying contract."

Which rate to use: in theory it depends on whether the trade creates a debit (borrowing rate) or a credit (lending rate), since most traders cannot borrow and lend at the same rate. "In practice, however, the most common solution is to use the *risk-free* interest rate, i.e., the most secure rate." In the US the government is the most secure borrower, so use the yield on a government security with a term equivalent to the life of the option.

| Option life | Rate to feed |
|---|---|
| 60 days | Yield on the 60-day treasury bill |
| 180 days | Yield on the 180-day treasury bill |

Decide by: match the treasury term to the option term, then check whether your instrument needs a second rate (foreign currency options do).

### Dividends

Relevant only to **stock** options, and only if a dividend falls within the life of the option. You must know both the amount of the dividend and the **ex-dividend date**, "the date on which a trader must own the stock in order to receive the dividend." Ownership is the operative test: "A deeply in-the-money option may have many of the same characteristics as stock, but only ownership of the stock carries with it the right to collect the dividend."

Estimation default: "In the absence of other information, most traders tend to assume that a company will continue the same dividend policy it has had in the past. If the company has been paying a 75 cent dividend each quarter, it will probably continue to do so." Companies do sometimes increase, decrease, or omit dividends, and a possible policy change must be factored into option values.

The near-expiration ex-date trap, stated exactly: "if the ex-dividend date is expected just prior to expiration, there is the danger that a delay of several days will cause the ex-dividend date to fall after expiration. For purposes of option evaluation, this is the same as eliminating the dividend completely. In such a situation a trader ought to make a special effort to ascertain the exact ex-dividend date."

Decide by: if the projected ex-dividend date sits within a few days of expiration, stop and confirm the exact date. If it can slip past expiration, price the option with the dividend removed entirely.

### Volatility

"Of all the inputs required for option evaluation, volatility is the most difficult for traders to understand. At the same time, volatility often plays the most important role in actual trading situations. Changes in our assumptions about volatility can have a dramatic effect on an option's value, and the manner in which the marketplace assesses volatility can have an equally dramatic effect on an option's price." Volatility "is related to the speed of the market."

Decide by: take the volatility number from the volatility skills below. Do not derive volatility mechanics from this chapter; Natenberg defers the whole subject to Chapter 4.

### Directional effects: only these exist in Chapter 3

| Change | Condition | Effect |
|---|---|---|
| Raise interest rates | Underlying is stock-type settled | Forward price up, call value up, put value down |
| Raise interest rates | Option is stock-type settled | Option value down, calls and puts alike |
| Raise interest rates | Underlying is a futures contract | Forward price unchanged |
| Raise volatility | Any | Dramatic effect on value; direction not stated in this chapter |

Chapter 3 contains no full call/put directional table across all five inputs. Do not synthesize the missing rows.

Decide by: if a question needs a directional row not in the table above, say the chapter does not supply it and route to the later-chapter skill.

## Failure modes

- **Flat probability line.** Assuming all outcomes are equally likely overprices the option: $6 versus $4.00 on the identical five prices.
- **Skipping the carry deduction.** Under stock-type settlement the expected return is the value at expiration, not today. $6 is not $5.88, and 95 cents is not 93 cents.
- **Treating a positive underlying expected return as free profit.** It is the arbitrage-free offset to carrying costs less dividends, nothing more.
- **Too few discrete outcomes.** The real world has an infinite number of possibilities; five buckets is a teaching device.
- **Treating expected return as achievable on one trial.** "On any one roll it is impossible to get back $3 1/2 since no face of the die has exactly 3 1/2 spots." The edge is a long-run claim.
- **Right on direction, wrong on speed.** Underlying at $100, believed to reach $120 within five months. A three-month $110 call at $4 returns $6 only if $120 arrives before expiration; if the move is late the option expires worthless and the full $4 is lost. Buying the six-month $110 call at $12 guarantees at least $10 of intrinsic value when $120 prints, which is still a loss. "Even though the underlying commodity reaches the target price of $120, there is no guarantee that the $110 call will ever be worth more than its $10 intrinsic value." Natenberg's diagnosis: "This is the primary reason speculators generally lose in option markets... not only must he be right about market direction, he must also be right about market speed. Only if he is right on both counts can he expect to make a profit." Corollary: "if a trader is highly proficient at predicting directional moves in the underlying market, he is probably better advised to stick to the underlying instrument." The minimum factors an option trader must consider (book p36) are the underlying price, the exercise price, time remaining to expiration, expected direction, and expected speed.
- **Feeding a last trade or newspaper settlement price** instead of the executable bid or offer. The hedge cannot be done at that price.
- **Feeding the wrong side of the market** for the hedge direction: the bid when you will be buying the underlying, or the asked when you will be selling it.
- **Mismatching the rate to the option term**, or using one interest rate for a foreign currency option that needs two.
- **Assuming last quarter's dividend continues**, or missing an exact ex-dividend date that sits just before expiration.
- **Applying stock-option interest-rate intuition to futures options**, where raising rates leaves the forward price unchanged.
- **Over-trusting the model, then scaling size.** Errors in judgement are magnified by size.

## Working checklist

```
[ ] Step 1: list the possible underlying prices at expiration
[ ] Step 2: assign a probability to each, concentrated near today's price, summing to 100%
[ ] Step 3: compute the forward price (current price + carry - dividends; futures forward = current price)
[ ] Step 3: confirm the distribution's mean sits at the forward price (arbitrage-free)
[ ] Step 4: expected return = sum(probability x payoff); confirm a call's result is non-negative
[ ] Step 5: deduct carrying cost = rate x time x amount (stock-type settlement)
[ ] Step 5: add any dividend expected within the option's life
[ ] Record the theoretical value in dollars
[ ] Input check: exercise price read off the contract
[ ] Input check: actual calendar days remaining, annualized (91 -> .25, 36 -> .10)
[ ] Input check: underlying price = bid if hedging by selling, asked if hedging by buying
[ ] Input check: treasury yield matched to the option term (60-day option -> 60-day bill)
[ ] Input check: second interest rate present if this is a foreign currency option
[ ] Input check: dividend amount confirmed and exact ex-dividend date verified against expiration
[ ] Input check: volatility sourced from the volatility skills, not from this chapter
[ ] Edge = market price - theoretical value, signed in your favor
[ ] Apply the trade rule: buy calls below value, sell above; buy puts below value, sell above
[ ] State the opposing underlying position (hedge ratio comes from the delta skill)
[ ] Name the least-certain input before sizing the trade
```

## Related

- [[natenberg-volatility-types]] supplies the fifth input this skill deliberately refuses to derive; Chapter 3 defers all volatility mechanics to Chapter 4.
- [[natenberg-volatility-scaling]] carries the trading-day-to-annualized adjustment that lets you feed actual calendar days here without double-counting non-trading days.
- [[natenberg-delta-neutral-hedging]] quantifies the hedge ratio that Chapter 3 only names, and is required to actually capture a theoretical edge.
- [[natenberg-model-assumptions-audit]] is where the "A Word on Models" cautions become a structured audit of which Black-Scholes assumption is failing.
- `position-sizing-expectancy` owns generic expectancy and bet-sizing; send plain "what is the EV of this bet" prompts there, not here.
- `options-payoff` draws expiration payoff diagrams; it does not compute present theoretical value.
- Put-call parity (deriving a put value from the associated call value) is Chapter 11, not this skill. Early exercise and American pricing models are later chapters.
