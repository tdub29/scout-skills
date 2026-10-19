---
name: grimes-trade-management
description: "Open trade: scale out, trail stop, pyramid, partial exit."
---

# Grimes Trade Management

## What this decides

Given an OPEN trade with a defined initial risk (entry, initial stop, R = distance from entry to stop), produce:

1. A **scale-out schedule** in R-multiples with exact limit placement.
2. A **trailing-stop tool** selection matched to how mature/parabolic the trend is.
3. A **partial-profit vs partial-loss verdict** on any proposed partial exit.
4. A **pyramid go/no-go** plus tier sizing if the user wants to add to a winner.
5. A **stop-adjustment ruling**: tighten to breakeven, tighten aggressively, hold, or (rare, gated) widen.

This is not a signal generator. It assumes a trade is already on with a known entry, initial stop, and R.

## When to use

- "I'm up 1R on this trade, what do I scale out and where's the limit?"
- "This trend is accelerating â€” Parabolic SAR or Chandelier stop?"
- "Should I add to this winner? How big should the next tier be?"
- "Do I take a partial loss here or just eat the full stop?"
- "Can I move my stop further away, just this once?"
- "The market gapped through my stop overnight â€” what now?"

Route position **sizing** (how many shares/contracts at entry) to `williams-position-sizing`. Route edge/expectancy math to `risk-metrics-calculation`. This skill starts only after the trade is live.

## Method

### Step 1 â€” Establish the reference frame
Confirm four numbers before doing anything else: entry price, initial stop, R (= |entry âˆ’ stop| in dollars per unit), and current price. Every rule below is expressed as a multiple of R. If any of the four is undefined, stop and get the initial-stop/position-sizing skill run first â€” active management cannot be layered on an undefined risk.

### Step 2 â€” Scale-out schedule (R-multiple exits)
- At **+1R**: exit 25â€“33% of the position on a resting GTC limit order, entered immediately when the entry fills (don't wait). Left working in all sessions â€” pre/post-market fills on a profit-taking limit are a gift from illiquid off-hours order flow, not a risk.
- By **+2R**: be down to one-third to one-half of the original size. Manage the remainder under a different rule set (trailing stop or pyramid logic, not more fixed targets).
- **Limit placement**: never place the limit AT or beyond a visible structure level (prior high/low, swing pivot, session high/low). Place it slightly INSIDE the level â€” a limit at the exact level assumes the market prints through your full size at that price, which backtesting (and reality) won't grant you. If you find yourself resting orders beyond a visible pivot, tighten them to just inside it.
- **Order-queue logic**: get resting limits into the book as early as possible. Electronic order books have heavy cancel-and-replace churn from HFT; a real (non-cancelled) order percolates to the front of the queue over time and gets filled first when price briefly touches the level.

### Step 3 â€” Choose the trailing-stop tool by trend maturity
| Situation | Tool | Why |
|---|---|---|
| Early/developing trend, want to stay in through normal chop | **Chandelier stop** (fixed NÃ—ATR off the trend extreme) | Gives more room; won't flip you out on ordinary pullbacks, at the cost of giving back more on a reversal |
| Mature, established trend | **Parabolic SAR** | Acceleration factor ratchets the stop in fast, tightening protection as the trend ages â€” the opposite tradeoff from Chandelier |
| Parabolic/climactic blow-off | **Stop under previous day's low** (or similarly tight price-action stop) | Deliberately crosses into a profit-taking exit â€” you WANT to be stopped out of climax moves; the small chance of missed further upside is worth removing the emotional/greed risk of holding a blow-off |
| Any of the above | Reject **moving averages and trend lines** as primary stop tools unless you can't do better | Both are arbitrary (why 50-period and not 53? why this trend line and not the other trader's?) and trend-line breaks are frequently reversed immediately â€” a bare trend-line stop puts you on the wrong side of a common, tradable tendency. If used, require "significant price action" under the line (multiple closes, a full consolidation, multiple legs) before honoring it, not the first touch. |

Sub-rule â€” never deploy a trailing-stop tool you haven't internalized (calculation, behavior in chop, behavior at climax) on a test/synthetic series first; the caveat that killed the most accounts in the source material was traders using tools they didn't understand.

### Step 4 â€” Partial profit vs partial loss verdict
- **Partial profits**: acceptable and often correct â€” it's "paying yourself as the market proves the idea correct." Trade-off: consistency (smaller wins, more often) vs full-size exposure to the rare big winner. Verify the partial exits are big enough to matter â€” don't lock in profits inside the market's normal noise level (e.g., quarter-point decisions on a $50 stock with a $2 ATR add nothing but the illusion of activity).
- **Partial losses**: default answer is **no â€” exit the full position at a small loss instead of scaling out on the loss side.** Reason: any partial exit anchors P&L to that side of entry. A partial profit exit anchors P&L favorably (intended). A partial loss exit anchors P&L unfavorably and makes the loss harder to recover even if price later reverses back in your favor â€” the position that remains open lags the market because size was already given up at the low. If a partial exit is being considered specifically because price moved against the trade, override it: take the full loss, don't stagger it.
- Do not confuse a **planned scale-IN** (accumulating toward full size against a level, defined before entry) with an unplanned partial-loss exit mid-trade â€” they are opposite operations that look similar on a screen.

### Step 5 â€” Pyramid go/no-go and tier sizing
- **Reverse pyramid (increasing size at higher/worse average prices: 1, 2, 4, 8, 16 units) â€” REJECTED.** It is top-heavy: the average cost basis rises to near the top, so a small retracement erases all accumulated profit, and the position size at the point of maximum exposure is also the point of maximum psychological pressure (an account-sized "swing" on a single day). Do not build this even if backtested trend examples make it look attractive â€” those are survivorship-selected trends.
- **Proper pyramid (decreasing size, front-loaded: e.g., 20 â†’ 16 â†’ 12 units) â€” the only pyramid form to use.** Average cost stays close to the first, largest tier, so volatility near the end of the trend is tolerable. Still adds variance to the bottom line; confirm the added upside is worth it on a risk-adjusted basis before doing it, not just "it feels right because the trade is working."
- **Add-back-after-partial-exit** (a distinct, better-behaved pattern than pyramiding into new highs): after taking a partial profit, if price returns to a level that re-establishes the setup (e.g., back to entry, or a new leg in trend direction), add back only up to the original full size and original total risk â€” never above it. This can be repeated to build a larger position "essentially for free" as a trend extends through multiple legs; do not increase size on later re-entries even though it's tempting â€” overconfidence near the end of an extended trend is exactly when volatility expands.
- **Scale-in risk cap**: any scale-in (into a mean-reversion setup, into a decline/rally) must have an absolute dollar risk amount defined BEFORE the first add, plus a hard drop-dead stop level past which the position will not be held, and the average price/size must be tracked continuously against that stop. Scaling into a trade going the wrong way is the mechanism by which "a small planned loss" becomes an account-threatening one â€” the ability to keep scaling in at all is itself a sign the market disagrees with you.

### Step 6 â€” Stop-adjustment ruling
- **Tighten to breakeven**: once the trade reaches an R-multiple that mirrors the initial risk (e.g., initial risk was $2.50, trade is now +$2.50 / +1R), or once a fixed profit-target multiple (e.g., 2R) has been hit and partial profits banked, move the stop on the remainder to at least breakeven. The logic: the trade has already proven itself at that level; a failure from there usually signals a larger-scale failure, so there's no reason to still be risking a full loss.
- **Tighten aggressively (parabolic run)**: in a genuine climactic/parabolic move, trail a stop under the previous day's low (see Step 3 table) even though this is really a profit-taking exit dressed as a stop. Justified because climax moves carry high reversal risk and holders get emotionally compromised extrapolating the move to infinity.
- **Hold, don't tighten, in a range**: tightening a stop while the market is genuinely ranging (not trending) is effectively a disguised time stop â€” it's a decision to get taken out, since ranges have larger random spikes and lower liquidity than trends. If that's not the actual intent, leave the stop near the original risk point until a new trend actually develops, then tighten.
- **Never widen a stop** â€” except three narrow, pre-defined cases, and even then the stop may never move past the original 1R boundary set at entry:
  1. Tightening the stop earlier was a clear error â€” move it back out, but no further than the day the error was made.
  2. Emerging market structure genuinely calls for a slightly wider stop (new traders should not use this exception â€” too easy to rationalize as the market approaches the stop).
  3. Scaling into a position and volatility clearly expands mid-buildup (e.g., a news shock) â€” stop the buying program early and widen the stop for the smaller-than-planned size already on, so *total dollar risk* stays at or below the original allocation. This is not an increase in risk; it's fewer units against a wider stop for the same total dollars at risk.
  If a widen request doesn't match one of these three, and stay inside the original 1R, the answer is no â€” a stop moved to allow more room defeats the position sizing that was calculated against the original risk.
- **Gap-through-stop handling**: when price gaps beyond a stop (overnight news, shock), don't act on reflex. Check (a) the market's typical gap behavior (e.g., equity gaps often partially fill/reverse) and (b) how price trades off the open. If price gaps against the position but immediately trades back toward it, a new stop under/over the day's extreme (giving the reversal a chance) can be reasonable. If price gaps against the position and presses further in that direction (or breaks the opening range against you), exit immediately at market â€” don't wait for the original stop level, it's already been violated with a much larger loss than intended.

## Worked mini-example

Long $50.00 stock, initial stop $47.50 (R = $2.50), 10,000 shares.
1. On fill, immediately enter a GTC limit to sell 2,500â€“3,300 shares at $52.49 (inside the $52.50 level if $52.50 is a visible pivot; otherwise at exactly +1R = $52.50) â€” Step 2.
2. Trend is young â€” trail the remainder with a Chandelier stop (NÃ—ATR off the swing high) rather than Parabolic SAR, since Parabolic would whipsaw in early chop â€” Step 3.
3. Price pulls back to $49.00 (a loss of $1.00, or 0.4R). No partial exit here â€” either hold full remaining size against the original $47.50 stop, or if forced to reduce, exit the entire remaining position rather than shaving off a slice at this small loss â€” Step 4.
4. Price reaches $55.00 (+2R). Bank another slice down to one-third to one-half of original size (per Step 2's 2R checkpoint), then move the stop on the remainder to breakeven ($50.00) â€” Step 6.
5. Trend keeps extending; price pulls back to $50.25 near breakeven. No widening of the stop is permitted â€” it stays at $50.00 unless one of the three named exceptions applies (none do here) â€” Step 6.
6. New leg develops; add back size only up to the original 10,000-share equivalent risk, never beyond it, and don't increase size on the next re-entry even though the trade "feels" like a winner â€” Step 5.

## References

- Source: Adam Grimes, *The Art and Science of Technical Analysis* (Wiley, 2012), Chapter 8 "Trade Management," pp. 231â€“251.
- Siblings (carved from the same book): `grimes-four-trades`, `grimes-pullback`, `grimes-failure-test`, `grimes-the-anti`, `grimes-breakout-trade`.
- Adjacent skills: `williams-position-sizing` (initial stop + position size at entry), `risk-metrics-calculation` (edge/expectancy statistics across a trade sample).
