---
name: trend-following-system
description: "Build any trend system. Covel five questions"
---

# Trend-Following System Builder

## What this decides

Whether a trading plan is a *complete, mechanical system* â€” not a forecast,
not an indicator, not a hunch â€” and if not, which of five required answers
is missing. Output is a filled-in rule set (market universe, sizing formula,
entry trigger, loss-exit rule, profit-exit rule) plus a pass/fail on the
expectation and robustness gates. This skill does not predict market
direction; it forces the *process* that lets you trade without predicting.

## When to use

- User wants to build a trend-following (or any systematic breakout) trading
  system from scratch.
- User has an indicator, a hunch, or a partial rule and wants it turned into
  a complete plan.
- User wants to audit an existing system for gaps ("is my system complete?").
- User is deciding how to size a position, when to cut a loss, or when to
  take profit and is reasoning from discretion/feel rather than a rule.
- User presents a backtest and asks if it's trustworthy.

Not for: fundamental/news-driven strategies, discretionary trading advice,
or picking which specific market will trend next (the system is
market-agnostic by design â€” see Sub-rule 1).

## Method

1. **Answer the Five Questions, in order, with a written rule for each.**
   Do not proceed to the next question until the current one has a testable
   rule (a number, a formula, or an unambiguous condition â€” not a feeling).

   | # | Question | Rule must specify |
   |---|----------|--------------------|
   | 1 | What to buy/sell? | The market universe and the selection criterion (liquidity, diversification across uncorrelated sectors) |
   | 2 | How much to buy/sell? | The %-of-equity risked per position and the total portfolio heat cap |
   | 3 | When to enter? | The exact breakout condition (price level, in the direction of the move) |
   | 4 | When to exit a loser? | The predefined stop â€” price level or %-loss, set *before* entry |
   | 5 | When to exit a winner? | Confirmation there is **no fixed profit target** â€” exit only on a trend-reversal signal |

2. **Run the expectation gate.** Compute
   `Expectation = (Win% x Avg Win) âˆ’ (Loss% x Avg Loss)`.
   If Expectation â‰¤ 0, the system has no edge â€” stop and fix sizing/exits
   before anything else. A system can be right on only 30-40% of trades and
   still have a strong positive expectation if average winners are several
   multiples of average losers; a system right 80% of the time can still
   have negative expectation if the 20% losses are large. Verdict must be
   computed, never eyeballed.

3. **Run the robustness gate ("loose-fitting suit").** For every numeric
   parameter (breakout lookback, stop %, heat cap):
   - Does it still perform reasonably at Â±10-20% of its value? If a
     parameter works at 20 but breaks at 19 or 21, it is curve-fit â€” reject.
   - Does it hold out-of-sample (data not used to select the parameter)?
   - Does it hold across markets structurally different from the one it was
     tuned on (e.g., tuned on bonds, tested on grains)?
   A suspiciously clean backtest (smooth equity curve, few whipsaws, tightly
   optimized parameters) is a red flag, not a reassurance â€” "you'll never
   see a bad backtest" until you deliberately hunt for the fragility.

4. **Run the personal inventory** before allowing the system to go live.
   Have the user (not the system) answer: nature/suitedness to trading,
   money-and-goal target, effort willing to invest, prior experience,
   resources available, and known strengths/weaknesses/discipline level.
   A mechanically sound system operated by someone who will override it
   under stress is not yet a complete system â€” the inventory is part of
   the spec, not a soft add-on.

5. **Issue the verdict.** State each of the five answers explicitly, the
   expectation number, the robustness result per parameter, and whether the
   personal inventory surfaced a disqualifying mismatch (e.g., user cannot
   tolerate double-digit drawdowns but the system's heat implies them).
   If any of the five questions is unanswered, or either gate fails, the
   system is **not complete** â€” name exactly which piece is missing.

## Sub-rules and failure modes

- **Price only, never fundamentals/news.** The market-selection and entry
  rules must be price-derived (breakouts, volatility). A system that
  requires forecasting earnings, macro data, or "what the market should be
  worth" is not this kind of system and re-introduces the forecasting bias
  the mechanical rules exist to remove.
- **Heat re-bases off current equity, not starting equity.** If a $100,000
  account draws down to $75,000, all subsequent position sizing runs off
  $75,000. Sizing off the original balance after a drawdown silently
  increases real risk beyond the stated tolerance. Portfolio heat = sum of
  each open position's %-risk (e.g., five positions risking 2% each = 10%
  heat); the cap is on the total, not per-trade only.
  Rule of thumb from the text: rarely below 1%, rarely above 5% risked per
  trade.
- **Never average down on a loser.** A losing position gets the predefined
  stop, not a second entry at a worse price to "improve the average." That
  is a discretionary override wearing a system's clothes, and it inverts
  the loss-cutting rule that makes the system's math work.
  Never wait for a retracement to add to a winner either â€” the entry price
  stops mattering the moment you're in ("a big concern before it happens, a
  small concern thereafter").
- **No profit target on winners, ever.** A fixed profit target caps the
  rare large winners that pay for the majority of small losing trades
  (often 60-70% of trades lose small). Removing the cap means tolerating
  round-trip whipsaws on paper profits â€” that discomfort is a designed
  cost of the system, not a signal something is broken.
- **An indicator is not a system.** A single technical indicator (MACD,
  Bollinger Bands, ADX) is roughly 10% of overall system performance at
  best. If Step 1's answer is "I use indicator X," the system is
  incomplete â€” indicator choice must be folded into a full entry rule with
  the other four questions still answered independently.
- **Curve-fit backtests fail forward.** A system tuned so tightly it only
  works at one exact parameter value, on one exact dataset, is describing
  the past, not a strategy. Reject any system whose builder cannot show
  Â±10-20% parameter tolerance and out-of-sample / cross-market performance.

## Worked mini-example

User: "I trade breakouts on the 20-day high with a MACD confirmation. I
close for a profit at +25% and let losers run if I 'still believe' in the
trade."

Apply the method:

1. Five Questions â€”
   - Q1 (what): unanswered â€” no stated market universe/diversification rule.
   - Q2 (how much): unanswered â€” no position-sizing or heat rule at all.
   - Q3 (when in): partially answered â€” 20-day-high breakout is a valid
     price-only entry; MACD confirmation is fine as a filter but not
     required.
   - Q4 (exit loser): **inverted** â€” "let losers run if I still believe" is
     the opposite of a predefined stop. This is the most severe defect.
   - Q5 (exit winner): **inverted** â€” a fixed +25% target caps the very
     winners the system needs to offset its losers.
2. Expectation: cannot be computed â€” no stop means loss size is unbounded,
   so Avg Loss is undefined. Gate fails by default.
3. Robustness: N/A until the rules exist.
4. Personal inventory: not yet reached.

Verdict: **Not a complete system.** Two of five questions are answered
backwards (losers should be cut fast and predefined; winners should have no
cap) and two are missing entirely (market universe, position sizing).
Fix order: define the stop-loss rule first (unblocks expectation
calculation), then sizing/heat, then the market universe, then drop or
loosen the profit target and replace it with a trend-exit signal.

## References

- Covel, Michael. *Trend Following* (Updated Ed., 2009, FT Press), Chapter
  10: "Trading Systems" â€” Five Questions for a Trading System; Seykota on
  portfolio heat; Ken Tropin and Barbara Dixon on the "loose-fitting suit";
  Andrew Lo on backtest bias; the Melamed silver-trade case study as the
  canonical failure mode (fundamentals-driven entry, profit-target exit).
- Siblings: none.
