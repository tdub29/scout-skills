---
name: natenberg-spread-adjustments
description: Decides whether to adjust a delta neutral option spread that has drifted, which of the three adjustment routes to take (underlying contracts, selling more options, buying the opposing options), how often to rehedge, and how to submit the order so the market does not take the edge back. Produces an executable order set, the resulting position delta, and a stated adjustment policy with its delta limit. Routes here on "my spread moved against me, what now", "should I adjust or leave it", "how often should I rehedge", "my delta drifted, fix it", "should I leg into this or use a spread order", "I keep getting bigger every time I adjust". From Sheldon Natenberg, Option Volatility and Pricing, Chapters 8 and 9.
---

# Natenberg Spread Adjustments

## What this decides

You already hold an approximately delta neutral spread. The underlying moved, or time passed, or implied volatility shifted, and the position is no longer neutral. This skill answers four questions in order:

1. Adjust at all, or let it drift?
2. Adjust with what: underlying contracts, more of the options you are already short, or the opposing options?
3. How often, as a standing policy set before the trade?
4. How is the order actually communicated so the fill does not cost you the edge?

Inputs you need: the current delta of every leg, the position gamma and vega, whether options in that market still look generally overpriced or underpriced, your delta limit, and your capitalization.

Output: a specific order set, the resulting position delta, and a written adjustment policy.

Natenberg scopes this against the prior chapter himself: "In the last chapter we considered the question of when a trader should adjust a position to remain delta neutral. The trader must also consider how best to adjust."

## The three ways to adjust

Worked example, Natenberg's numbers. The underlying is at 99.25 and all options appear overpriced. The trader sells the 95/105 strangle, 20 times. The 95 put has a delta of -36, the 105 call a delta of +36, so the position starts neutral:

```
(-20 x -36) + (-20 x +36) = 0
```

Several days pass and the market falls to 97.00. The 95 put is now -41, the 105 call is now +30:

```
(-20 x -41) + (-20 x +30) = +220
```

The trader is 220 deltas long. "If the trader now decides to make an adjustment he has three basic choices":

```
1. sell underlying contracts
2. sell calls
3. buy puts
```

Every delta adjustment on any delta neutral position collapses to those three. The choice among them is not about the delta, which all three fix. It is about what each one does to gamma, theta, vega, theoretical edge, and position size.

## The governing law: risk neutral in the underlying

Two laws, both italicized in the book, decide the whole question.

**Law 1.** *"A delta adjustment made with the underlying contract is essentially a risk neutral adjustment."* The reason: "the gamma, theta, and vega associated with an underlying contract are zero. Therefore, if a trader wants to adjust his delta position, but wants to leave the other characteristics of the position unaffected, he can do so by purchasing or selling an appropriate number of underlying contracts."

**Law 2.** *"An adjustment made with options may reduce the delta risk, but will also change the other risk characteristics associated with the position."* "Every option, in addition to having a delta, also has a gamma, theta, and vega. When an option is added to or subtracted from a position, it necessarily changes the total delta, gamma, theta, and vega of the position. This is something which new traders sometimes forget."

Law 1 is the governing constraint because it is the only route that changes nothing except the delta. Every option adjustment is therefore a deliberate decision to alter the volatility position as well, and has to be justified on those grounds, not just on the delta.

**Law 3, the intent rule.** "All other considerations being equal, whenever a trader makes an adjustment he should do so with the intention of improving the risk/reward characteristics of the position."

## When each choice is correct

**Buy the opposing options (buy puts, in the example).** Reduces the delta and reduces the other risks at the same time, because "the gamma, theta, and vega associated with the put purchase are opposite in sign to the gamma, theta, and vega associated with his existing short strangle position." The cost: "Since implied volatility can remain high or low for long periods of time, it is quite likely that if all options were overpriced when the trader initiated his position, they will still be overpriced when he goes back into the market to make his adjustment. Even though the purchase of puts to become delta neutral will reduce his other risks, such an adjustment will also have the effect of reducing the theoretical edge." Correct when cutting risk outranks edge.

**Sell more of the overpriced options (sell calls).** "If all options are overpriced and the trader decides to sell additional calls to reduce the delta, the sale of the overpriced calls will have the effect of increasing the theoretical edge." Correct when "adding to his theoretical edge is of primary importance." Selling seven more 105 calls:

```
(-20 x -41) + (-27 x +30) = +10
```

**Adjust in the underlying.** The fallback, and the only correct answer in one specific case: "If a trader finds that any delta adjustment in the option market that reduces his risk will also reduce his theoretical edge, and he is unwilling to give up any theoretical edge, his only recourse is to make his adjustments in the underlying market. An underlying contract has no gamma, theta, or vega, so the risks of the position will remain essentially the same."

## The size creep trap: a 20 lot becomes 42 x 27

Continue the example. The market rebounds to 101.50. The 95 put is now -26, the 105 call is now +40:

```
(-20 x -26) + (-27 x +40) = -560
```

Three choices again: buy underlying, buy calls, or sell puts. Still intent on increasing theoretical edge, the trader sells an additional 22 of the 95 puts:

```
(-42 x -26) + (-27 x +40) = +12
```

Natenberg's verdict: "If all options remain overpriced and the trader is always intent on increasing his theoretical edge, he will continue to make whatever adjustments are necessary by continuously selling overpriced options. This method of adjusting may indeed result in the greatest profit to the trader. But notice what is happening. The strangle, which the trader was initially prepared to sell 20 times, has now increased in size to 42 x 27. If the market now makes a violent move in either direction, the negative consequences will be greatly magnified. ... If the market makes a very swift move, the trader may not survive."

Two adjustments, each locally correct on the edge criterion, more than doubled a position the trader had sized deliberately at 20.

**Prohibition for new traders.** "A new trader who is unfamiliar with all the subtleties of an option market should avoid making adjustments which increase the size of his position."

**Escalation rule.** "No trader can afford to ignore the effect his adjustments will have on the total risk to his position. If he has a positive (negative) gamma position, buying (selling) any additional options will increase his gamma risk. Likewise, if he has a positive (negative) vega position, buying (selling) any additional options will increase his vega risk. A trader cannot afford to sell overpriced options or buy underpriced options ad infinitum."

**The two choices rule when the position is too big.** "At some point the size of the spread will simply become too large, and any additional theoretical edge will have to take a back seat to risk considerations. When that happens there are only two choices: decrease the size of the spread or adjust in the underlying market."

**The ego rule.** "A disciplined trader knows that sometimes, because of risk considerations, the best course is to reduce the size of the spread, even if it means giving up some theoretical edge. This may be hard on the trader's ego, particularly if he must personally go back into the market and either buy back options which he originally sold at a lower price, or sell out options which he originally purchased at a higher price. However, if a trader is unwilling to swallow his pride from time to time, and admit that he made a mistake, his trading career is certain to be a short one."

## How often to adjust

A spread that is delta neutral today may not be neutral tomorrow even if nothing else changes, because volatility changes and the passage of time also move the delta. Optimum use of a theoretical pricing model requires maintaining delta neutrality continuously, which is impossible in practice, so the frequency is a policy decided in advance. Natenberg gives exactly three methods.

**1. Adjust at regular intervals.** Match the interval to the interval over which you measured volatility. A volatility estimate built from daily price changes means adjust daily; one built from weekly price changes means adjust weekly. "This is a trader's best attempt to emulate the assumptions built into the theoretical pricing model."

**2. Adjust at a predetermined delta count.** Very few traders insist on being delta neutral all the time, and no one can be certain the model's assumptions and inputs are correct anyway. Even with perfect deltas a trader might accept some directional risk, "But a trader ought to know just how much directional risk he is willing to accept." Set the number and adjust when the position reaches it. The worked limit is 500 deltas long or short. The limit scales with position size and capitalization: "A small, independent trader may find that he is uncomfortable with a position which is even 200 deltas long or short, while a large trading firm may consider a position which is several thousand deltas long or short as being approximately delta neutral."

**3. Adjust by feel.** "This suggestion is not made facetiously." Underlying at 50.00, position delta neutral with a gamma of -200. The market falls to 48.00, so the position is approximately 400 deltas long. If 400 is the risk limit he might adjust, but if he also knows 48.00 is strong support he might choose not to, expecting a rebound. "If the trader is right more often than not, there is no reason why he shouldn't take advantage of this skill." The cost is named: if the market keeps going through the level, skipping the adjustment was the wrong call.

**The reusable arithmetic:** new delta is approximately the starting delta plus (gamma x price change). A -200 gamma position is +400 deltas after a 2 point fall and -400 deltas after a 2 point rally.

**What you gain and what you pay.**

- Adjusting more often buys you closer conformity to the model's continuous hedging assumption, which is what the theoretical edge is predicated on, and less accumulated directional risk. You pay for it in what each adjustment does to you directionally: with a negative gamma you are forced to buy as the market rises and sell as it falls.
- Adjusting less often lets the position's own gamma carry the directional exposure. You pay for it by accepting directional risk you have not sized, and under method 2 you cannot know in advance how often you will trade: "sometimes very frequently, sometimes not for long periods."

## A question of style: gamma sign against your directional habit

Most pricing models assume movement in the underlying is random, so a purely theoretical trader should hold no prior directional opinion. In practice many traders start out trading the underlying, where direction is the primary consideration, and carry a directional style with them. Natenberg names two: the **trend follower**, "adhering to the philosophy that 'the trend is your friend'", and the **contrarian**, "preferring to 'buy weakness, sell strength'."

The way to incorporate style is to fix the adjustment plan before the trade: "One way to do this is to consider beforehand the adjustments which will be required for a certain strategy if the underlying market begins to move."

**Short straddle, negative gamma, neutral at inception.** "As the market moves higher his delta position is getting shorter, and as the market moves lower his delta position is getting longer. If this trader likes to trade against the trend, he will avoid adjustments as much as possible because his position is automatically trading against the trend. Whichever way the market moves, the position always wants a retracement of this movement." The same trader, if he prefers to trade with the trend, "will adjust at every opportunity. In order to remain delta neutral, he will be forced to buy underlying contracts as the market rises and sell underlying contracts as the market falls."

**Long straddle, positive gamma.** "As the market rises his delta is becoming longer, and as the market falls his delta is becoming shorter. If this trader likes to trade with the trend, he will want to adjust as little as possible in the belief that the market is likely to continue in the same direction. However, if he prefers to trade against the trend, he will want to adjust as often as possible. Every adjustment will represent a profit opportunity if the market does in fact reverse direction."

**The two laws, both italicized in the book.** *"A trader with a negative gamma is always adjusting with the trend of the underlying market. A trader with a positive gamma is always adjusting against the trend of the underlying market."*

**The selection matrix.**

| Trader's preference | Option A | Option B |
|---|---|---|
| Prefers to trade **with** the trend | positive gamma + **less** frequent adjustments | negative gamma + **more** frequent adjustments |
| Prefers to trade **against** the trend | negative gamma + **less** frequent adjustments | positive gamma + **more** frequent adjustments |

"If a trader prefers to trade with the trend or against the trend, he should choose a strategy and an adjustment process that is appropriate to his preference."

**The exception.** "The purely theoretical trader will not have to worry about this since for him there is no such thing as a trend. However, for most traders old habits, such as trading with or against the trend, die hard."

## Entering the order: the spread is one contract

**The core rule.** "In sophisticated option markets, spreads are traded as if they are one, single contract. This means that a spread is quoted with a single bid price and a single offer price." A market maker quotes a straddle 3.45 / 3.55. Sell it at 3.45, buy it at 3.55. If the trader pays 3.55, "neither he nor the market-maker care whether the trader pays 1.75 for the call and 1.80 for the put, or 1.55 for the call and 2.00 for the put, or some other combination. The only consideration is that the prices of the call and put taken together add up to 3.55."

A market maker "will always endeavor to give one bid price and one ask price for an entire spread." Common structures (straddle, strangle, butterfly, time spread) get a two sided quote very quickly. A complex spread in unusual ratios "may take a market-maker several minutes to calculate the value of the spread," but he will still make an effort to give his best two sided market.

**Spread order versus individual legs.** Natenberg does not use the words "leg" or "legging risk" in this section. What he gives instead is the structural defence: quote and trade the package at one net price, and attach **All Or None** so the order cannot be partially filled. Do not attribute an explicit legging risk doctrine to Chapter 8. The practical consequence is the same, which is that working the legs separately against separate limits is not how the market prices or fills the package.

**Order types.** The two most common qualifying instructions are **market orders** (filled at the current market price) and **limit orders** (filled at a specified price). Beyond those, **contingency orders** specify how the order is to be executed. The list he gives as commonly used in option markets, all defined in his Appendix A:

```
All Or None            Market On Close
Fill Or Kill           Not Held
Immediate Or Cancel    One Cancels The Other
Market If Touched      Stop Limit Order
                       Stop Loss Order
```

**What must be on the order.** Expiration months, exercise prices, option type, buy or sell, the ratio, the spread price, and the direction of that price (debit or credit).

**Worked ticket 1 (futures).** Buy 25 Crude Oil Jan 19 C, sell 25 Crude Oil Feb 19 C. Written under the legs: .24 on the buy side, .44 on the sell side, annotated as "an indication of the prices the broker should look at", so the leg prices are guidance and not the order. Then spread ratio 1 x 1, spread price .20 Credit, All Or None on the sell side.

**Worked ticket 2 (index options).** Buy 10 OEX Dec 425 puts (7 1/2), sell 20 OEX Dec 410 puts (3 1/4), GTC. Annotations: "order to be executed with OEX between 424-426", spread ratio 1 x 2, and 1 Point Debit as the "spread price for each 1 by 2 ratio".

**Broker discipline and the recheck.** "A broker executing a spread order is responsible for adhering to any special instructions which accompany the order. Unless a trader knows exactly what current market conditions are, or has a great deal of confidence in the broker who will be handling the order, it is always a good practice to submit specific instructions with the order as to how it is to be filled." And because so much has to be communicated, "it is also a good practice to recheck all orders before submitting them for execution. Option trading can be difficult enough without the additional problems of miscommunication."

The 1994 paper ticket layout is an illustration of the required fields, not a form to reproduce. The fields survive into electronic complex order books.

## Failure modes

- Fixing the delta with options and forgetting that gamma, theta and vega moved too.
- Always taking the edge maximizing adjustment (selling more overpriced options) and letting a 20 lot strangle become 42 x 27.
- A new trader making any adjustment that increases position size.
- Adding options on the same side as an already large gamma or vega exposure, which escalates the exposure that is already the biggest risk.
- Refusing to reduce size because it means buying back higher than you sold. Natenberg says this ego failure ends careers.
- Adjusting in the option market when every risk reducing option adjustment also destroys the edge, instead of adjusting in the underlying.
- Assuming the position is still neutral because the underlying did not move. Volatility changes and the passage of time move the delta too.
- Picking an adjustment interval that does not match the interval used to measure volatility, which defeats the whole point of interval adjustment.
- Copying someone else's delta limit. 200 deltas is a limit for one trader and rounding error for a firm.
- Expecting a predictable adjustment frequency under a delta trigger. It is unknowable in advance.
- Using feel as a standing licence to skip adjustments. The licence is conditional on being right more often than not.
- Choosing strategy and adjustment cadence independently, so a contrarian ends up mechanically buying strength and selling weakness to stay neutral.
- Not deciding the adjustment plan before entry, then improvising it under P&L pressure.
- Working the legs individually against separate limits instead of submitting one net spread price.
- Treating the leg prices written on the ticket as the order. They only indicate where the broker should look.
- Omitting the ratio, or omitting debit/credit direction, on the spread price. A 1 x 2 priced "1 point debit" is meaningless without the ratio.
- Sending a naked market order on a complex spread with no contingency instruction when you do not know current conditions or the broker.
- Not rechecking. The failure Natenberg names here is miscommunication, not mispricing.

## Working checklist

```
[ ] Recompute every leg's current delta and total the position delta.
[ ] Compare the total against your stated delta limit. If inside it, stop; no adjustment is due.
[ ] Confirm the position's gamma and vega signs before choosing an instrument.
[ ] List the three choices explicitly for this position (underlying, sell options, buy the opposing options).
[ ] Ask whether options in this market are still generally overpriced or underpriced. That decides which
    option route adds edge and which gives it back.
[ ] For each option route, state what it does to gamma and vega, not just to delta. If it adds to the
    exposure that is already largest, drop it.
[ ] Check the resulting position size against the size you originally chose. If the adjustment grows it,
    justify the growth or take the underlying instead.
[ ] If the position is already too large: only two options remain, reduce the spread or adjust in the
    underlying.
[ ] New trader: reject any adjustment that increases size.
[ ] Confirm the adjustment improves the risk/reward characteristics of the position, per Law 3.
[ ] Confirm the cadence matches the style you chose before entry (gamma sign x adjustment frequency).
[ ] Write the order as one spread at one net price: months, strikes, type, buy/sell, ratio, net price,
    debit or credit.
[ ] Attach the contingency instruction (All Or None on anything that must not fill partially).
[ ] Recheck the whole order before submitting.
[ ] Recompute the position delta after the fill and confirm it landed where you intended.
```

## Related

- [[natenberg-break-even-volatility]] ranks and selects the spread before you own it, using break even implied volatility and the risk/reward fraction. This skill starts once the position exists.
- [[natenberg-volatility-spread-classification]] owns the four category gamma/vega classification that tells you which category a position is in. This skill consumes the gamma and vega signs; it does not derive them.
- [[natenberg-delta-neutral-hedging]] covers hedging a mispriced option with the underlying in the first place, which is the mechanism Law 1 relies on.
- [[natenberg-greeks-risk-profile]] defines delta, gamma, theta and vega and how they move. Read it first if the sensitivity signs here are not already familiar.
- `grimes-trade-management` manages a directional trade against price levels; this manages a delta-neutral volatility spread against greek drift, which is a different decision with different inputs.
