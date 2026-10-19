---
name: natenberg-volatility-spread-classification
description: Classifies any approximately delta neutral option structure into Natenberg's four gamma/vega categories and states exactly how it behaves under three shocks, a large move in the underlying, a change in implied volatility, and the passage of time. Use when the user asks "am I long or short volatility with this", "what does a backspread do if vol drops", "classify this spread", "which of these is short gamma", "what happens to my time spread as expiration comes", "long gamma short vega, what structure is that", "is a short butterfly a backspread", "which volatility spreads have positive gamma", or "I'm delta neutral with gamma -1500 and vega +3000, what am I actually running". Works from the structure name alone with no strikes, prices, volatility input, or days to expiration, and answers at the sign level only. From Sheldon Natenberg, Option Volatility and Pricing, Chapter 8 and Appendix C.
---

# Natenberg Volatility Spread Classification

## What this decides

Given any position that is approximately delta neutral, this decides which of four
gamma/vega categories it is really in, and what will help it and hurt it. The output
is a verdict plus a signed exposure ledger, not a picture and not a dollar figure.

Two directions of use:

1. Forward. "I hold X." Name the category, give the four greek signs, then state the
   behaviour under a large move, under an implied volatility increase and decrease,
   and under the passage of time.
2. Reverse. "I want short gamma and long vega." Return every structure whose signature
   matches, here the long time spread, then hand off for context and sizing.

Boundary: `options-payoff` takes a structure name and draws its payoff curve. This
skill takes a structure and emits its behaviour under three shocks, which is downstream
of the curve and a different question.

## The shared property of every volatility spread

Natenberg's definition (book p137). Every volatility spread will:

1. be approximately delta neutral;
2. be sensitive to changes in the price of the underlying instrument;
3. be sensitive to changes in implied volatility;
4. be sensitive to the passage of time.

Delta neutrality is a tolerance, not an equality (book p161). "Note also that a
volatility spread need not be exactly delta neutral. (Indeed, as we saw in Chapter 6,
no trader can say with any certainty whether he is delta neutral.) A practical guide is
for the delta to be close enough to zero so that the volatility considerations are more
important than the directional considerations." If the delta is large enough that
direction outranks volatility, the position has left the volatility spread family and
this classification no longer applies.

Terminology warning Natenberg attaches to the whole chapter (book p137): "spreading
terminology is not uniform. Traders sometimes use different terms when referring to the
same spread; they sometimes use the same term when referring to different spreads." So
classify by gamma and vega sign, never by the name on the ticket.

## The four categories

Book p160, reproduced verbatim.

| Category | Gamma | Vega |
|---|---|---|
| Backspread | Positive | Positive |
| Ratio Vertical Spread | Negative | Negative |
| Long Time Spread | Negative | Positive |
| Short Time Spread | Positive | Negative |

Rule of use, verbatim: "If a trader is approximately delta neutral, no matter how
complex the position, even if it includes options of different types, at many different
exercise prices, and with several different expiration dates, he can always place the
position in one of these four general categories based on the gamma and vega of the
position."

Degree scales with magnitude. Gamma -100 with vega +200 is a long time spread, "but not
nearly to the degree" of gamma -1500 with vega +3000.

The three sub-rules that generate the categories:

- Helped by movement means positive gamma. Hurt by movement means negative gamma.
- Positive gamma necessarily implies negative theta, and negative gamma necessarily
  implies positive theta, of similar magnitude. "An option trader can't have it both ways."
- Helped by a rise in implied volatility means positive vega. Helped by a decline means
  negative vega.

Positive gamma is called being **long premium**, hoping for a volatile market with large
moves. Negative gamma is called being **short premium**, hoping for a quiet market with
only small moves.

Time spreads are the only category where realized and implied volatility pull in
opposite directions.

### Which named spreads land in which category

Figure 8-19, Characteristics of Volatility Spreads (book p161), reproduced verbatim.
`+` is positive, `-` is negative, `0` is zero.

| Spread Type | Delta Position | Gamma Position | Theta Position | Vega Position |
|---|---|---|---|---|
| Backspread | 0 | + | - | + |
| Long Straddle | 0 | + | - | + |
| Long Strangle | 0 | + | - | + |
| Short Butterfly | 0 | + | - | + |
| Ratio Vertical Spread | 0 | - | + | - |
| Short Straddle | 0 | - | + | - |
| Short Strangle | 0 | - | + | - |
| Long Butterfly | 0 | - | + | - |
| Long Time Spread | 0 | - | + | + |
| Short Time Spread | 0 | + | - | - |

Equivalences Natenberg states explicitly:

- Long straddles and long strangles are special types of **backspreads** (only long
  options, all expiring in the same month, so more long than short market contracts).
- Short straddles and short strangles are special types of **ratio vertical spreads**.
- A long butterfly "tends to act like a ratio vertical spread"; a short butterfly
  "tends to act like a backspread."
- A long iron butterfly (buy the straddle, sell the strangle) is equivalent to a
  **short** butterfly; a short iron butterfly is equivalent to a **long** butterfly.
- A long Christmas tree done delta neutral is a particular type of ratio vertical
  spread; a short Christmas tree is a particular type of backspread.

## Master table: construction, volatility view, greek signs

One row per named spread. Realized volatility column is what the spread needs the
underlying to actually do, relative to the implied volatility priced into the options.

| Spread | Leg construction | Wants realized vol | Wants implied vol | Delta | Gamma | Theta | Vega |
|---|---|---|---|---|---|---|---|
| Call backspread | Long more calls at a higher exercise price, short fewer calls at a lower exercise price, same expiration; buy small deltas, sell large deltas; usually done for a credit | Above implied (needs movement; unlimited upside profit) | Up | 0 | + | - | + |
| Put backspread | Long more puts at a lower exercise price, short fewer puts at a higher exercise price, same expiration; usually a credit | Above implied (unlimited downside profit) | Up | 0 | + | - | + |
| Call ratio vertical spread | Short more contracts than long, all same expiration; the opposite side of a call backspread | Below implied (max profit if the underlying finishes right at the short option's exercise price) | Down | 0 | - | + | - |
| Put ratio vertical spread | Short more contracts than long, all same expiration; the opposite side of a put backspread | Below implied (max profit at the short option's exercise price) | Down | 0 | - | + | - |
| Long straddle | Long call plus long put, same exercise price, same expiration | Above implied (more movement than a backspread needs) | Up | 0 | + | - | + |
| Short straddle | Short call plus short put, same exercise price, same expiration | Below implied | Down | 0 | - | + | - |
| Long strangle | Long call plus long put, different exercise prices, same expiration; out of the money unless stated (both in the money is a "guts") | Above implied (even more movement than a straddle needs) | Up | 0 | + | - | + |
| Short strangle | Short call plus short put, different exercise prices, same expiration | Below implied | Down | 0 | - | + | - |
| Long butterfly | Three equally spaced exercise prices, all same type, same expiration; buy the outside prices, sell two of the inside price; ratio always 1 x 2 x 1 | Below implied (max value if the underlying sits at the inside price) | Down | 0 | - | + | - |
| Short butterfly | Sell the outside prices, buy two of the inside price; 1 x 2 x 1 | Above implied (wants to finish outside the extreme prices) | Up | 0 | + | - | + |
| Long time spread (calendar, horizontal) | Buy the long term option, sell the short term option, same type, same exercise price; a debit | Below implied; wants the market to sit still | Up | 0 | - | + | + |
| Short time spread | Buy the short term option, sell the long term option; a credit | Above implied; wants a big move | Down | 0 | + | - | - |
| Diagonal spread | Like a time spread but different exercise prices | Cannot be generalized. See the diagonal section below | Cannot be generalized | n/a | n/a | n/a | n/a |

Aliases Natenberg fixes so the classification survives sloppy naming:

- **Backspread** = "a delta neutral spread which consists of more long (purchased)
  options than short (sold) options where all options expire at the same time." Also
  called a ratio backspread or a long ratio spread.
- **Ratio vertical spread** = short more contracts than long, all options expiring at the
  same time. Also called a ratio spread, short ratio spread, vertical spread, or front
  spread. Natenberg fixes "ratio vertical spread" as the name "in order to avoid later
  confusion."
- **Ratio spread** (general) = "Any spread where the number of long market contracts
  (long calls or short puts) and short market contracts (short calls or long puts) are
  unequal."
- **Time spread** = "opposing positions which expire in different months." Also a
  calendar spread or horizontal spread.
- **Long / short naming convention**: "It is common practice to refer to a spread which
  requires an outlay of capital as a long, or purchased, spread." A long butterfly buys
  the wings; a long time spread buys the long dated option.

Degree of movement ladder (book p144). A backspread needs **some** movement, a long
straddle needs **more**, a long strangle needs **even greater** movement. A strangle is
"usually considered the most highly leveraged of all option positions because out of the
money options are cheap relative to other options." The short side mirrors it: short
strangles carry the greatest risk on an unexpectedly large move.

Computing the ledger for a real position: net greek = sum over legs of (signed contract
count) x (that leg's per contract greek). Figure 8-20 example, long 20 Jun 100 calls
against short 20 Mar 100 calls: delta 0, gamma -52.0, theta +.2940, vega +2.000.

## Figure C-1: Characteristics of Volatility Spreads

Appendix C, book p452. The entire appendix is this one table; there is no prose.
Verbatim subtitle printed under the figure title:

> (all spreads are assumed to be approximately delta neutral)

Cell legend as printed: `0` (zero or flat), `+`, `-`, `helps`, `hurts`, `long`, `short`.

| Spread Type | Initial Delta | Initial Gamma | Initial Theta | Initial Vega | A large move in the underlying generally | An increase(decrease) in implied volatility generally | The passage of time generally | Upside contract position | Downside contract position |
|---|---|---|---|---|---|---|---|---|---|
| Call backspread | 0 | + | - | + | helps | helps (hurts) | hurts | long | 0 |
| Put backspread | 0 | + | - | + | helps | helps (hurts) | hurts | 0 | short |
| Call ratio vertical spread | 0 | - | + | - | hurts | hurts (helps) | helps | short | 0 |
| Put ratio vertical spread | 0 | - | + | - | hurts | hurts (helps) | helps | 0 | long |
| Long straddle | 0 | + | - | + | helps | helps (hurts) | hurts | long | short |
| Short straddle | 0 | - | + | - | hurts | hurts (helps) | helps | short | long |
| Long strangle | 0 | + | - | + | helps | helps (hurts) | hurts | long | short |
| Short strangle | 0 | - | + | - | hurts | hurts (helps) | helps | short | long |
| Long butterfly | 0 | - | + | - | hurts | hurts (helps) | helps | 0 | 0 |
| Short butterfly | 0 | + | - | + | helps | helps (hurts) | hurts | 0 | 0 |
| Long time spread (1:1 ratio) | 0 | - | + | + | hurts | helps (hurts) | helps | 0 | 0 |
| Short time spread (1:1 ratio) | 0 | + | - | - | helps | hurts (helps) | hurts | 0 | 0 |

**Printed row grouping**, preserved because the pairing is the mnemonic. The rows are
printed in blank line separated pairs: {Call backspread, Put backspread} then
{Call ratio vertical spread, Put ratio vertical spread} then {Long straddle, Short
straddle} then {Long strangle, Short strangle} then {Long butterfly, Short butterfly}
then {Long time spread (1:1 ratio), Short time spread (1:1 ratio)}. Each pair is a
structure and its mirror image.

**The parenthesis convention, load bearing.** In the implied volatility column the
unparenthesized word is the effect of an **increase** in implied volatility and the
parenthesized word is the effect of a **decrease**. `helps (hurts)` means an implied
volatility increase helps and a decrease hurts. The parenthesized word is not a synonym,
not an alternative reading, and not a second option; it is the other direction of the
same shock. Reading it any other way inverts half the table. This convention is specific
to Figure C-1 and is **not** the convention used in Appendix D's Figure D-1, where
parentheses are a positionally paired substitution instead; do not carry one convention
into the other.

How to read a row:

1. Confirm the precondition. Approximately delta neutral. If not, `Initial Delta = 0` is
   not a fact about the book, and the tail columns describe the exposure that survives.
2. Name the row. Map the position to one of the 12 canonical rows. A structure that does
   not map (iron condor, broken wing fly) gets decomposed into the rows it is built from
   rather than a new row invented for it.
3. Read the four greeks for the standing exposure signature.
4. Read the three shock columns: move, implied volatility in both directions using the
   parenthesis convention, time.
5. Read the two tail columns. "Upside contract position" and "downside contract position"
   say what the spread converts into if the market runs, which is the question the greeks
   do not answer. A call backspread becomes synthetically long underlying on a rally;
   a short straddle becomes synthetically short.

Structural families visible in the tail columns:

- **One sided tails**: call backspread (long / 0), put backspread (0 / short), call ratio
  vertical (short / 0), put ratio vertical (0 / long). These are asymmetric, unlike
  straddles and strangles which are long/short or short/long. Treating a call backspread
  as a two sided volatility play misreads the row.
- **Bounded family, 0 in both tails**: long butterfly, short butterfly, long time spread
  (1:1), short time spread (1:1). A large move cannot convert them into a directional
  underlying position, which is the structural reason they are the limited risk
  volatility plays.
- **The sign anomaly**: only the two time spread rows have gamma and vega disagreeing in
  sign, and only they pair "a large move hurts" with "an implied volatility increase
  helps." So "long volatility" is an ambiguous instruction for a time spread; say gamma
  or say vega.
- The time spread rows are specified **only at 1:1 ratio**, printed in the row label.
  A ratioed calendar is a different profile.

## Why the time spread signature is what it is

- "A long time spread always wants the underlying market to sit still." An at the money
  option's theta grows as expiration approaches, so the short term option decays faster
  than the long term one and the spread widens. Figure 8-13 walks it out: at 6 months
  against 3 months the options are worth 7 1/2 and 6 for a spread of 1 1/2, and by
  3 months against expiration they are worth 6 and 0 for a spread of 6.
- A large move in either direction collapses the spread. Both options go to parity or to
  zero; 100 calls with the underlying at 150 both trade at 50 points of intrinsic value
  and the spread goes to zero, or to 1/4 if the long term option keeps 1/4 point.
- "A long time spread always benefits from an increase in implied volatility." Vega rises
  with time to expiration, so the long term option gains more. Figure 8-14: at 15%, 20%
  and 25% volatility the long term option is worth 6 1/2, 7 1/2 and 8 1/2 while the short
  term option is worth 5 1/2, 6 and 6 1/2, so the spread is worth 1, 1 1/2 and 2.
- "When implied volatility rises, time spreads tend to widen; when implied volatility
  falls, time spreads tend to narrow," and this effect "can often be great enough to
  offset either a favorable or unfavorable move in the underlying market."
- The apparently contradictory ideal for a long time spread: the market sits still and
  everyone thinks it is about to move. Natenberg's examples are a finance ministers
  meeting on exchange rates, an expected Fed policy statement, and an upcoming earnings
  report, events with no immediate effect on the underlying but significant potential
  repercussions.

## The effect of changing interest rates and dividends

Book p154 to p157. This is the one input that does not respect the four category
classification, because it depends on whether the legs share an expiration.

- **Futures options.** There is no carrying cost on a futures contract, so interest rates
  have only a minor impact and a negligible effect on the value of futures option
  volatility spreads.
- **Stock options where all options expire at the same time** (backspreads, ratio
  vertical spreads, straddles, strangles, butterflies). The forward stock price is the
  same for every option, so the effect of a rate or dividend change is "practically
  negligible."
- **Stock option time spreads** carry two different forward prices and the longer dated
  one is more rate sensitive. Worked example: stock 100, rate 12%, dividend 0, March 3
  months out, June 6 months out, so forwards are 103 and 106. Drop rates to 8% and the
  forwards become 102 and 104; the June option is more affected, so the **call** time
  spread **narrows**. Therefore a long (short) call time spread in the stock option
  market must have a positive (negative) rho.
- **Puts reverse it.** The same rate drop makes the June put gain more than the March
  put, so the **put** time spread **widens**. A long (short) put time spread in the stock
  option market must have a negative (positive) rho.
- Magnitude "depends primarily on the amount of time between expiration dates." March
  against September is far more sensitive than March against April.
- **Dividends run opposite to interest rates.** An increase (decrease) in dividends
  lowers (raises) the forward stock price. If at least one dividend payment is expected
  between the two expiration dates, an increase in dividends makes call time spreads
  narrow and put time spreads widen; a decrease does the reverse.

Figure 8-15 quantifies both (stock 100, volatility 20%, March 6 weeks, June 19 weeks).
With dividend 0, moving interest rates from 0% to 12% takes the call time spread from
2.10 to 3.72 and the put time spread from 2.10 to .82. With interest at 6.00%, moving
the quarterly dividend from 0 to 4.00 takes the call time spread from 2.87 to .95 and
the put time spread from 1.39 to 3.39.

## Diagonal spreads and the other variations

**Diagonal spreads cannot be generalized.** A diagonal spread is like a time spread but
with different exercise prices, and Natenberg refuses to assign it a category. The one
exception he states: when the diagonal is done one to one, with the same option type,
and the deltas of the two options are approximately equal, it "will act very much like a
conventional time spread" and may be read off the time spread rows. Figure 8-20 carries
his own footnote on exactly this case, long 10 Mar 105 calls against short 10 Jun 110
calls: "Although this is technically a diagonal spread, it will tend to act like a time
spread because the options have deltas which are approximately equal."

Variations that do map onto the four categories:

- **Christmas tree** (also called a ladder). Three different exercise prices, same type,
  same expiration. A long call Christmas tree buys one call at the lowest exercise price
  and sells one call at each of the higher exercise prices. A long put Christmas tree
  buys one put at the highest exercise price and sells one put at each of the lower
  exercise prices. Usually done delta neutral; long is a type of ratio vertical spread,
  short is a type of backspread.
- **Iron butterfly.** Buy a straddle and sell a strangle, or the reverse, where the
  straddle is at an exercise price midway between the strangle's exercise prices, all
  expiring at the same time. A long iron butterfly (buy the straddle) is equivalent to a
  **short** butterfly; a short iron butterfly is equivalent to a **long** butterfly.
  Minimum value zero, maximum value the amount between exercise prices.
- **Condor.** A butterfly with the inside exercise price split, so four options at
  consecutive exercise prices, the two outside bought and the two inside sold (long
  condor) or the reverse; all same type, same expiration. Maximum value is the amount
  between consecutive exercise prices, achieved anywhere between the two inside prices,
  so "a condor will usually have a higher value than a butterfly with approximately the
  same exercise prices."

## Failure modes

- **Classifying by leg names instead of by gamma and vega sign.** A short butterfly is a
  backspread. A long butterfly is a ratio vertical spread. A long straddle is a
  backspread. Name matching gets all three wrong.
- **Reading the Figure C-1 parenthesized word as a synonym or an alternative** rather
  than as the decrease case. This inverts half the table. It is also the one place where
  Figure D-1's parenthesis convention, positional substitution, must not be imported.
- **Assuming gamma and vega always agree in sign** because ten of twelve Figure C-1 rows
  do, then getting the time spread pair backwards. This is the single most likely error
  in the table.
- **Reporting positive gamma with positive theta**, or both negative, for the same
  position. Impossible. Theta is always opposite in sign to gamma and of similar magnitude.
- **Treating implied and realized volatility as pulling the same way.** True for
  backspreads and ratio vertical spreads, false for time spreads, where a big move and an
  implied volatility decrease both help the short time spread.
- **Assuming a butterfly is delta neutral.** The 1 x 2 x 1 ratio is fixed, so when the
  exercise prices sit far from the underlying the butterfly becomes unbalanced. Natenberg's
  own printed example carries -220 deltas: "because the ratio of a butterfly is always
  1 x 2 x 1, the butterfly can become unbalanced if the exercise prices are far away from
  the current underlying price."
- **Ignoring that a large delta demotes the position out of the volatility spread
  category entirely.** Direction then outranks volatility and this whole framework stops
  applying.
- **Ignoring the (1:1 ratio) qualifier** on the time spread rows and applying them to a
  ratioed calendar.
- **Applying the negligible rate and dividend rule to a time spread.** It only holds when
  all options expire at the same time.
- **Treating a `0` in a tail column as "no risk"** rather than as "no directional
  underlying position." A long butterfly at 0/0 still loses its debit.
- **Presenting the sign table as if it were quantitative.** It has no magnitudes and needs
  no market inputs; anything requiring a number is a handoff. Same caution near expiration,
  where gamma and theta magnitudes explode and a correct sign level answer is useless for
  sizing.
- **Confusing size with risk.** "A trader should never confuse size and risk. Risk often
  depends on the characteristics of the strategy, not on the size in which the strategy
  is executed." 100 butterflies may be much less risky than 25 straddles.

## Working checklist

```
[ ] Confirm the position is approximately delta neutral (close enough to zero that
    volatility considerations outrank directional ones). If not, stop and say so.
[ ] Compute or collect net delta, gamma, theta, vega: sum of (signed contract count)
    x (per contract greek) across every leg.
[ ] Sanity check the signs: gamma and theta must be opposite, of similar magnitude.
[ ] Place the position in one of the four categories from gamma and vega sign alone,
    ignoring the name on the ticket.
[ ] State the degree from the magnitudes, not just the category.
[ ] Map to a Figure C-1 row; decompose exotics into canonical rows rather than
    inventing a row.
[ ] Read the three shock columns: large move, implied volatility increase and decrease
    (unparenthesized = increase, parenthesized = decrease), passage of time.
[ ] Read both tail columns and say what the position becomes on the upside and on the
    downside.
[ ] If it is a time spread, add: realized and implied volatility pull in opposite
    directions; check the 1:1 ratio qualifier; check rho and dividends if these are
    stock options.
[ ] If it is a diagonal, do not generalize unless it is one to one, same option type,
    and the deltas are approximately equal.
[ ] Hand off anything needing a number, a curve, or a position size.
```

## Related

- [[natenberg-choosing-a-strategy]] runs the opposite direction: given a volatility
  forecast, the market's implied volatility, and a directional view, it selects the
  category and structure to put on, and it owns Appendix D's Figure D-1 strategy matrix.
- [[natenberg-greeks-risk-profile]] supplies the per contract delta, gamma, theta and vega
  that this skill sums into a position level signature.
- [[natenberg-break-even-volatility]] answers how much realized volatility the structure
  actually needs, which is the magnitude behind this skill's "wants realized vol above or
  below implied" column.
- [[natenberg-spread-adjustments]] takes over once the position is classified and drifts:
  re-hedging cadence, delta limits, and the gamma times move arithmetic.
- `options-payoff` draws the expiration payoff curve for a named structure. This skill is
  downstream of the curve and answers a different question, behaviour under three shocks.
- `risk-metrics-calculation` owns anything quantitative. Figure C-1 has no numbers in it.
