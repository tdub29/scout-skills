---
name: natenberg-choosing-a-strategy
description: "Turn a direction and vol view into an option trade"
---

# Natenberg Choosing a Strategy

## What this decides

Input: two opinions. Output: a candidate set of option structures, with strike placement, or the instruction to sit out.

Natenberg's own framing of the matrix: "designed to help the reader choose the types of strategies which are most likely to be profitable given a trader's opinion on market direction and volatility."

Boundary, stated plainly: `options-payoff` consumes structure names and emits curves; this skill consumes opinions and emits structure names, so it sits strictly upstream and does not overlap. A prompt that already names the structure ("draw me a 100/110/120 call butterfly") is not this skill. A prompt that names only a view is.

The natural chain is: this skill (select candidates) then `natenberg-volatility-spread-classification` (differentiate the candidates by risk profile) then `options-payoff` (curve) then position sizing.

## The two inputs (and how to get each one right)

**Input 1: market direction.** Bearish, Neutral, or Bullish. "Neutral" means genuinely no directional opinion, not "mildly bullish." Do not round a weak lean into Neutral and do not round Neutral into a lean.

**Input 2: implied volatility, Low / Moderate / High.**

READ THIS BEFORE USING THE MATRIX. The volatility axis is measured against the trader's OWN volatility forecast. It is never an absolute level, never an IV rank, never an IV percentile, never "VIX is at 35 so vol is high." Getting this wrong silently selects the wrong column and reverses the recommendation.

Natenberg's definition, verbatim from book p453:

> "The implied volatility component, whether low, moderate, or high, is in comparison to a trader's own volatility forecast. If the trader believes that 15% is a reasonable forecast, but implied volatility is 13%, then implied volatility is low. If the trader believes that 20% is a reasonable forecast, but implied volatility is 24%, then implied volatility is high. If the trader's volatility forecast is approximately the same as the implied volatility, then implied volatility is moderate."

So:

| Comparison | Column |
|---|---|
| Your forecast above implied (forecast 15%, implied 13%) | Low |
| Your forecast approximately equal to implied | Moderate |
| Your forecast below implied (forecast 20%, implied 24%) | High |

If the user has not given a volatility forecast, ask for one. Without it there is no vol axis and the matrix cannot be read. Route to `natenberg-volatility-forecast` to build the forecast and `natenberg-break-even-volatility` to sanity-check it against what the market is charging.

## Figure D-1: the strategy matrix

Legend line as printed: ITM = in-the-money, ATM = at-the-money, OTM = out-of-the-money.

Axis labels as printed: column-group spanner IMPLIED VOLATILITY over columns Low / Moderate / High; row-group spanner MARKET DIRECTION over rows Bearish / Neutral / Bullish.

| MARKET DIRECTION \ IMPLIED VOLATILITY | Low | Moderate | High |
|---|---|---|---|
| **Bearish** | buy naked puts<br>bear vertical spreads<br>&nbsp;&nbsp;&nbsp;&nbsp;buy ATM call/sell ITM call<br>&nbsp;&nbsp;&nbsp;&nbsp;buy ATM put/sell OTM put<br>sell OTM (ITM) call (put) butterflies<br>buy ITM (OTM) call (put) time spreads | sell the underlying | sell naked calls<br>bear vertical spreads:<br>&nbsp;&nbsp;&nbsp;&nbsp;buy OTM call/sell ATM call<br>&nbsp;&nbsp;&nbsp;&nbsp;buy ITM put/sell ATM put<br>buy ITM (OTM) call (put) butterflies<br>sell OTM (ITM) call (put) time spreads |
| **Neutral** | backspreads<br>buy straddles/strangles<br>sell ATM call or put butterflies<br>buy ATM call or put time spreads | go on vacation | ratio vertical spreads<br>sell straddles/strangles<br>buy ATM call or put butterflies<br>sell ATM call or put time spreads |
| **Bullish** | buy naked calls<br>bull vertical spreads:<br>&nbsp;&nbsp;&nbsp;&nbsp;buy ATM call/sell OTM call<br>&nbsp;&nbsp;&nbsp;&nbsp;buy ATM put/sell ITM put<br>sell ITM (OTM) call (put) butterflies<br>buy OTM (ITM) call (put) time spreads | buy the underlying | sell naked puts<br>bull vertical spreads:<br>&nbsp;&nbsp;&nbsp;&nbsp;buy ITM call/sell ATM call<br>&nbsp;&nbsp;&nbsp;&nbsp;buy OTM put/sell ATM put<br>buy OTM (ITM) call (put) butterflies<br>sell ITM (OTM) call (put) time spreads |

### Cell-by-cell verbatim listing

The grid above and the list below are the same figure twice on purpose. Table markup swallows the indented strike lines under the vertical-spread entries, and those lines are the whole value of the cell. When you quote a cell, quote it from this listing, not from the grid.

- **Bearish / Low**
  - `buy naked puts`
  - `bear vertical spreads` (printed with no colon in this cell)
    - `buy ATM call/sell ITM call`
    - `buy ATM put/sell OTM put`
  - `sell OTM (ITM) call (put) butterflies`
  - `buy ITM (OTM) call (put) time spreads`
- **Bearish / Moderate**
  - `sell the underlying`
- **Bearish / High**
  - `sell naked calls`
  - `bear vertical spreads:`
    - `buy OTM call/sell ATM call`
    - `buy ITM put/sell ATM put`
  - `buy ITM (OTM) call (put) butterflies`
  - `sell OTM (ITM) call (put) time spreads`
- **Neutral / Low**
  - `backspreads`
  - `buy straddles/strangles`
  - `sell ATM call or put butterflies`
  - `buy ATM call or put time spreads`
- **Neutral / Moderate**
  - `go on vacation`
- **Neutral / High**
  - `ratio vertical spreads`
  - `sell straddles/strangles`
  - `buy ATM call or put butterflies`
  - `sell ATM call or put time spreads`
- **Bullish / Low**
  - `buy naked calls`
  - `bull vertical spreads:`
    - `buy ATM call/sell OTM call`
    - `buy ATM put/sell ITM put`
  - `sell ITM (OTM) call (put) butterflies`
  - `buy OTM (ITM) call (put) time spreads`
- **Bullish / Moderate**
  - `buy the underlying`
- **Bullish / High**
  - `sell naked puts`
  - `bull vertical spreads:`
    - `buy ITM call/sell ATM call`
    - `buy OTM put/sell ATM put`
  - `buy OTM (ITM) call (put) butterflies`
  - `sell ITM (OTM) call (put) time spreads`

## The parenthesis convention in Figure D-1

Figure D-1's parentheses are POSITIONALLY-PAIRED SUBSTITUTION. The unparenthesized words form one instruction; the parenthesized words substitute in as a matched pair to form a second, equally valid instruction. Two alternatives, not four combinations, not one hybrid.

Worked example:

`sell OTM (ITM) call (put) butterflies`

- Take the unparenthesized words in order: OTM, call. Reading one is "sell OTM call butterflies."
- Take the parenthesized words in order: ITM, put. Reading two is "sell ITM put butterflies."
- There is no "sell OTM put butterflies" and no "sell ITM call butterflies" in that cell.

Same mechanic: `buy ITM (OTM) call (put) time spreads` = "buy ITM call time spreads" or "buy OTM put time spreads."

THIS IS NOT THE SAME CONVENTION AS FIGURE C-1. In Figure C-1 (Appendix C, characteristics of volatility spreads) the parenthesized word is the decrease case of the same event: `helps (hurts)` means an increase in implied volatility helps and a decrease hurts. Carrying C-1's increase/decrease reading into D-1, or D-1's substitution reading into C-1, reverses the recommendation. Figure C-1 lives in `natenberg-volatility-spread-classification`; read its convention there, not here.

## The five preconditions from the Appendix D prose (book p453)

The matrix does not stand alone. All five paragraphs govern how it is read.

**1. It is a candidate set, not a ranking.** "The following chart is designed to help the reader choose the types of strategies which are most likely to be profitable given a trader's opinion on market direction and volatility. Even though several strategies may be appropriate under the same market conditions, each strategy will have its own unique risk/reward characteristics. The reader should refer to the text for a more detailed analysis of each strategy." Return the whole cell. Do not present one entry as the answer.

**2. The vol axis is relative to your own forecast.** Restated in full in "The two inputs" above, with Natenberg's 15/13 and 20/24 examples. This is the paragraph agents skip and the reason they land in the wrong column.

**3. Every listed strategy has a synthetic equivalent.** "Any of the listed strategies can be done synthetically. Instead of buying (selling) a call, a trader can buy (sell) a put with the same exercise price and buy (sell) an underlying contract (synthetic long (short) call). Instead of buying (selling) a put, a trader can buy (sell) a call with the same exercise price and sell (buy) an underlying contract (synthetic long (short) put)." So the entries in a cell are economically equivalent expressions of the same view. Choosing among them is an execution, margin, borrow, and liquidity question, not a view question.

**4. No opinion on either axis means no trade.** "The only scenario for which there is no appropriate strategy is one in which a trader has no opinion on either implied volatility or market direction. In such a case a disciplined trader will choose to sit on the sidelines until trading conditions become more opportune." The Neutral/Moderate cell reads "go on vacation." That is a real output. Return it.

**5. ITM and OTM on butterflies and time spreads are defined against spot, not per leg.** "In-the-money call butterflies and time spreads, and out-of-the-money put butterflies and time spreads, are those in which all exercise prices are lower than the current price of the underlying contract. Out-of-the-money call butterflies and time spreads, and in-the-money put butterflies and time spreads, are those in which all exercise prices are higher than the current price of the underlying contract." Restate every butterfly and time-spread recommendation as "all strikes above spot" or "all strikes below spot" so it cannot be misread. Invert this and a bearish recommendation becomes a bullish position.

## Chapter 8: "Choosing an Appropriate Strategy"

The matrix is the lookup. Chapter 8 is the reasoning that produces the same answer from the volatility side, and it adds an input the matrix does not carry: a view on where implied volatility is heading.

**Inputs Natenberg requires.**

1. Your own volatility estimate for the underlying over the life of the option.
2. The implied volatility currently in the option marketplace.
3. A view on whether implied volatility is likely to rise or fall.
4. Whether you also have a directional lean, which selects within a category (call versus put backspread, and so on).
5. Your tolerance for unlimited risk.

**Decision procedure.**

1. First and foremost, choose spreads with a positive theoretical edge: ideally buy underpriced options and sell overpriced options. Compare estimate versus implied. Implied below your estimate means everything looks underpriced, so shop the positive-vega categories: backspread, long time spread. Implied above your estimate means everything looks overpriced, so shop the negative-vega categories: ratio vertical spread, short time spread.
2. Use the implied-vol-direction corollary to choose between the two same-signed categories. "Long time spreads are likely to be profitable when implied volatility is low but expected to rise; short time spreads are likely to be profitable when implied volatility is high but expected to fall."
3. Use the realized-movement view within the same-expiry categories: expect movement, take the backspread family; expect stillness, take the ratio vertical family.
4. Use direction to pick the type. Backspreads: great upside potential means call backspread, great downside potential means put backspread, and avoid backspreads entirely in quiet markets. Ratio verticals: primarily worried about a swift rise means put ratio vertical, worried about a swift fall means call ratio vertical, because the wrong-way legs can only collapse to zero, which caps the loss.
5. Use risk tolerance last. Straddles and strangles maximize theoretical edge on both legs but are "among the riskiest of all strategies"; a trader will often prefer another spread in the same category "even if such spreads entail buying some overvalued options or selling some undervalued options." Butterflies are the limited-risk substitute for the same view: a trader considering selling 25 straddles "might decide instead to buy 100 butterflies (100 x 200 x 100)."

**The Figure 8-21 / 8-22 demonstration (book p166-p168).** Theoretical values computed at a 20% volatility estimate, then repriced at two implied volatilities.

At implied volatility 17%, below the 20% estimate, only spreads with a positive vega have a positive theoretical value: call and put backspreads, long straddles and strangles, short butterflies, long time spreads.

At implied volatility 23%, above the 20% estimate, only spreads with a negative vega have a positive theoretical value: call and put ratio vertical spreads, short straddles and strangles, long butterflies, short time spreads.

**Named overrides Natenberg allows.** A long time spread can still be right in a high implied-volatility market if the market stagnates and implied volatility is expected to stay high, because the short-term option decays while the long-term option keeps its value. A short time spread can still be right in a low implied-volatility market if the underlying is expected to make a large move with no commensurate increase in implied volatility. The override is licensed only when the trader has an explicit prediction of how implied volatility will move, not as a general escape hatch.

**Sunk-cost rule.** Once the spread is established, the market conditions that help or hurt it "are determined by its type, not by the initial prices." Do not let the entry price or previous trading activity change the current risk assessment.

## Failure modes

- Reading the vol axis as an absolute level or an IV percentile. This is the primary failure mode and it silently selects the wrong column.
- Mis-expanding the paired parentheses. `sell OTM (ITM) call (put) butterflies` is two alternatives, not four combinations and not one hybrid.
- Importing Figure C-1's increase/decrease parenthesis convention into Figure D-1, or the reverse.
- Inverting the ITM/OTM butterfly and time-spread definition by reading it per leg instead of as "all strikes above/below spot."
- Refusing to return "go on vacation" because a no-trade output feels unhelpful. It is the appendix's own recommendation.
- Treating the Moderate column as weak or degenerate. "Sell the underlying" and "buy the underlying" is the correct answer when you have a directional view but no volatility edge: express it in the underlying, not in options.
- Presenting one cell entry as the answer. The cell is an unranked candidate set and the prose says so.
- Emitting "sell naked calls" or "sell naked puts" without the undefined-risk framing. They are listed as the purest expression of the view, not as appropriate sizing for an arbitrary account.
- Selecting only on the realized-movement forecast and ignoring the implied-volatility level. That picks the right gamma sign and the wrong vega sign.
- Requiring every leg to be individually mispriced the right way. Once your estimate differs from implied across the board that is impossible; accept buying some overvalued options or selling some undervalued options to get the category right.
- Overriding the guidelines without an explicit prediction of how implied volatility will move.
- Answering a prompt that already names a structure. That is `options-payoff` or `risk-metrics-calculation`, not this skill.

## Working checklist

```
[ ] Elicited the user's own volatility forecast (a number, not a vibe)
[ ] Compared forecast to current implied and set the column: Low / Moderate / High
[ ] Confirmed I did NOT use IV rank, IV percentile, or a historical level for the column
[ ] Set the row: Bearish / Neutral / Bullish, with Neutral meaning genuinely no view
[ ] Checked the no-opinion-on-both case; if it holds, returned "go on vacation" and stopped
[ ] Quoted the cell from the verbatim listing, including every indented strike line
[ ] Expanded any parentheses as positionally-paired substitution, two alternatives
[ ] Restated butterfly and time-spread entries as "all strikes above/below spot"
[ ] Offered synthetic equivalents where execution, margin, or borrow matters
[ ] Attached the undefined-risk warning to any naked-option entry
[ ] Presented the cell as an unranked candidate set, not a single pick
[ ] Asked for a view on implied-vol direction if the choice is between two same-signed categories
[ ] Handed off for risk profile, payoff curve, and sizing
```

## Related

- [[natenberg-volatility-spread-classification]] owns Figure C-1 and its separate increase/decrease parenthesis convention; use it to differentiate the candidates inside a cell by gamma, vega, theta, and tail behavior.
- [[natenberg-volatility-forecast]] produces input 1, the trader's own volatility forecast, without which the vol axis cannot be set.
- [[natenberg-break-even-volatility]] cross-checks that forecast against the volatility the market is charging before you commit to a column.
- [[natenberg-greeks-risk-profile]] quantifies the chosen structure once the cell has named it.
- `options-payoff` draws the curve for a structure this skill has already named. `risk-metrics-calculation` computes the numbers. Both are downstream.
