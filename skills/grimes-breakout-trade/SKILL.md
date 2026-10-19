---
name: grimes-breakout-trade
description: Judge and trade the transition from trading range to trend around a support/resistance breakout â€” Adam Grimes' breakout-quality screen, breakout-base pre-entry (three trigger options with an adverse-selection tradeoff), two-stage stop, and the failed-breakout ("turkey shoot") read of the first reaction. Use when a market is coiling into a well-tested level and the question is whether a breakout is worth trading before it happens; when deciding whether to bid the base, wait for a spring/upthrust, or just get filled; when a breakout just occurred and the question is where the stop goes; or when the first bar after a breakout reverses hard and you need to read whether it's failing or just a normal pullback. Triggers: breakout trade, breakout base, turkey shoot, failed breakout, spring, upthrust, trading range to trend, is this breakout real, prebreakout accumulation, gap through resistance.
---

# Grimes Breakout Trade: Trading Range to Trend

## What this skill decides

Three linked decisions around a support/resistance level:

1. **Go/no-go**: is this breakout structurally set up to work, or is it a "turkey shoot" that eats small accounts?
2. **Pre-breakout entry**: if trading the base *before* the level breaks, which of three entry triggers, and what does that choice cost you?
3. **Post-breakout stop and failure read**: once the level breaks, where is risk, and â€” if the first reaction reverses hard â€” is that a failure or a normal pullback?

Output is not a probability estimate. It is a specific trade plan: enter/skip, trigger, stop price (two stages), and a profit-branch call.

## When to use

- Price has pressed the same support/resistance level multiple times and hasn't broken it yet â€” you're asking "is a breakout setting up."
- You want to position *inside* the range before the breakout, not chase the breakout bar itself.
- A breakout just happened and you need a stop that won't get clipped by a normal shakeout.
- The first bar(s) after a breakout reverse hard and you need to know: failing, or just the first pullback.
- Someone proposes a simple channel-breakout system (e.g., 20-day-high entries) â€” this skill's "real level" requirement explains why systematic channel breakouts are a different animal from discretionary level breakouts (see Sub-rule 5).

Do not use for: reading the failure-test *pattern itself* as a standalone fade trade at an untested level (that's `grimes-failure-test`); trend-continuation pullback entries once a breakout has already had one clean confirming pullback (that's `grimes-pullback` â€” at that point it's just a trend trade); position sizing and generic stop mechanics (`grimes-trade-management`).

## Method

### Step 1 â€” Screen for breakout quality (go/no-go)

The base rate is against you: **most breakouts fail**. Small excursions beyond a level are usually met by offsetting pressure and pushed back into the range; indiscriminate breakout entries lose to transaction costs and failed breakouts by a thousand small cuts. Only trade breakouts that show the precursor and signature patterns below â€” everything else is a pass.

**Precursor patterns (look for these BEFORE the breakout, while still in the range):**
- **Higher lows into resistance** (or lower highs into support, inverted) â€” a mild feedback loop where large buyers use each decline to accumulate, declines get shallower, and the pattern coils into the level. Classic ascending-triangle signature of institutional accumulation.
- **Tight range near the extreme of a larger range** â€” a sub-range less than ~25% of the height of the larger range, sitting right at the edge. Traders paying up to hold near the edge (rather than drifting back to the middle) signals urgency and conviction.
- **Prebreakout accumulation (springs/upthrusts)** â€” short-lived excursions beyond the range edge that immediately reverse. Repeated springs/upthrusts at the edge are evidence large players are positioning, not that support/resistance is "clean."
- **A visible, real level** â€” one that's been tested cleanly multiple times and is obvious to a casual chart reader. Levels nobody's eye would be drawn to (e.g., a mechanical 20-day high) don't carry the same order-flow significance â€” see Sub-rule 5.

**Signature patterns (confirm AT the breakout bar itself):**
- **High volatility** â€” bar ranges expand, volume/activity jumps. A market that gently lifts through resistance on low energy is a bad sign, not a good one.
- **Desirable slippage** â€” you should have to pay UP to get filled (or receive DOWN on a short). A surprisingly *good* fill (positive slippage) means someone was eager to sell into your breakout â€” treat it as an early warning of failure, not a bonus.
- **Immediate satisfaction** â€” the trade should give fast feedback in the trade's own time frame (seconds for intraday, days for weekly). A breakout that slowly grinds sideways/against you with no confirming energy is "no breakout at all."

**Decision**: precursor + signature patterns present â†’ tradeable breakout, proceed to Step 2 or Step 3. Missing most of these â†’ turkey shoot risk is high; skip the breakout entry and wait for either a first-pullback confirmation or a failure-test fade instead.

### Step 2 â€” If entering the base BEFORE the breakout: pick a trigger and price the tradeoff

This positions you inside the pre-breakout consolidation ("breakout base": a tight range, often <25% of the larger range's height, sitting at the resistance/support edge) instead of chasing the breakout bar. Three trigger options, long-side wording (invert for shorts):

1. **Bid near the bottom of the base.** Best trade location when filled. Drawback: fills only in a declining/against-momentum tape, and may never fill at all if the market breaks out without revisiting the bottom â€” you'll miss some winners entirely.
2. **Wait for a spring (drop below base support that immediately recovers) and enter on the close of that bar.** Enters with short-term momentum instead of against it. Drawback: not every base prints a spring, and reading it well is a high-maintenance, detail-sensitive execution skill.
3. **Unconditional fill â€” just get the position on anywhere in the range.** Ugly but simple; appropriate when the base is small relative to the move's potential (e.g., a 1.5-point base inside a 5-point range with 10 points of upside â€” squeezing an extra half point isn't worth missing the trade).

**The adverse-selection tradeoff (why "just bid the bottom" isn't automatically optimal):** a trader who only fills on limit orders at the bottom of the range will be filled on *every losing trade* that revisits the bottom, but will miss some *winning* trades that break out without ever printing a low enough print to fill the limit. Better trade location on the trades you do get is real, but it must outweigh the profits foregone on the winners you never got filled on. There is no universally correct answer â€” it depends on whether the incremental price improvement per trade exceeds the expected value of the missed winners over a large enough sample (Grimes: run ~500 trades and check objectively).

### Step 3 â€” Set the two-stage stop

**Stage 1 (in the base, pre-breakout):** stop below the lowest point reached while in the base â€” if hit, treat as a temporary stop-out and be willing to reenter. Alternative: a wider stop for position-sizing purposes, set to trigger before price reaches the base low if developing price action already contradicts the trade (e.g., the market consolidates *below* support rather than snapping back â€” Grimes' rule of thumb: a quick poke below support that snaps right back is normal; consolidation below support is not, and that changes the stop logic before the hard level is even touched).

**Stage 2 (post-breakout):** do NOT tighten the stop to the exact breakout level. Excellent breakouts routinely dip back to retest or briefly violate the breakout level to shake out weak-hand shorts/longs before extending â€” placing a stop right at the level puts you in that shakeout. General principle: a stop belongs at a price the market "should not reach if the trade thesis is correct" â€” for a fresh breakout, that is usually the prebreakout reference level (the base's support, or the highest low preceding the breakout), not the breakout line itself. If price closes back below the prebreakout base's pivot low, that's a materially different, weaker signal than a shakeout at the breakout line and is more consistent with a genuine failure.

**Gap handling:** a breakout that gaps through the level on the open is not a reason to skip the trade â€” a gap through an important level often signals a real shift in dynamics ("gap and go"). It does mean you must accept a worse entry price and a wider initial stop distance than planned; don't chase by tightening the stop to compensate.

### Step 4 â€” If the first reaction after the breakout reverses hard: read failure vs. pullback

The first pullback after a breakout is the highest-information moment: if the breakout is real, this is the best entry for the new trend; if it's going to fail, it fails here.

**Read the CHARACTER of the reaction, not just its existence:**
- **Good failure signature ("turkey shoot")**: price closes back on the wrong side of the level within roughly 2â€“3 bars of your time frame, accompanied by strong momentum away from the level. This is the "head poked above the fencerow and shot off" pattern â€” sharp, decisive, high-conviction reversal.
- **Weak/ambiguous signature**: the reversal bar closes near the level with no real momentum, or lower-timeframe price action shows the market "goes down a lot easier than it goes up" (grinding lack of conviction rather than sharp rejection) â€” expect sharp failure momentum to show up within the next few bars; if it doesn't, this was probably just an ordinary pullback, not a failure, and does not need to hold outside the breakout level to remain valid.
- **Pullback holds cleanly outside the level**: easiest to manage (breakeven stop at entry) but has no particular logical requirement to happen â€” don't assume it's the default case.
- **Pullback violates the level but then resumes**: also normal. Large players who accumulated in the base are not obligated to defend the exact line; naive short-term traders panicking out at the violation are often selling to the same large players, who then resume buying once that selling dries up. A level violation on the pullback is NOT automatically a failed breakout.

**Zero-tolerance stop for the failed-breakout trade itself:** if you are fading the breakout (trading the failure), the stop goes above the extreme of the failed thrust â€” the far side of the poke beyond the level. Any close back beyond that extreme means the "failure" was itself wrong; treat it as a hard stop, not a level to average against.

**Two-branch profit plan once failure is confirmed:**
1. **Absorbed into a larger consolidation** â€” the market fails the breakout but doesn't collapse; it grinds back into range. Manage as a range/mean-reversion trade, not a trend trade.
2. **Wholesale collapse** â€” sharp momentum away from the failed level continues into a genuine reversal leg (the classic "failure pullback" setup: point A breakout, point B pullback, point C sharp momentum break of the pullback low against the breakout direction). This is the higher-payoff branch and the one worth holding for; it typically shows up as a longer, steeper trend leg than the prior trend in that direction.

## Sub-rules and failure modes

1. **Precursor absence is a skip signal, not a "trade smaller" signal.** No higher-lows-into-resistance, no tight sub-range, no springs/upthrusts at the edge = no evidence of institutional positioning = treat the level as a coin-flip breakout and don't trade the breakout itself (wait for confirmation or a failure-test fade instead).
2. **Positive slippage on entry is a red flag, not a lucky fill.** If you paid better than expected to get long a breakout, someone with size was happy to sell there â€” that is evidence against the breakout, log it as an early warning, don't celebrate the fill.
3. **Don't put the stop at the breakout level itself.** This is the single most common beginner error this skill exists to prevent â€” good breakouts frequently revisit or pierce the exact line to clear out weak hands before extending. The stop belongs at the prebreakout reference level (base low / prior swing), not the line traders are watching.
4. **Level violation on the pullback â‰  failed breakout.** Only escalate to "failed" when the reaction shows the turkey-shoot character (fast close-back-through, real momentum) or the failure-pullback continuation (sharp break of the pullback's own extreme against the breakout direction). A slow violation with no momentum is usually still a live trade.
5. **Mechanical channel-breakout systems (e.g., 20-day-high entries) are a different discipline than this skill.** They deliberately trade levels with no visible chart significance and accept many small losses in exchange for never missing a trend; this skill's precursor/signature screen assumes a level real market participants are actually watching. Don't apply the "most breakouts fail, so skip weak setups" logic to a systematic channel system â€” that system's edge depends on taking every signal.
6. **This skill borders `grimes-failure-test`.** Failure-test is the standalone tactic of fading a brief, sharp excursion beyond ANY level (doesn't require a prior "good breakout" setup). This skill's Step 4 uses the same character-read but specifically as a post-breakout diagnostic after you (or the market) already treated the level as a breakout candidate. Don't merge the two â€” cross-link instead.

## Worked mini-example

Setup: Stock has tested $50 resistance three times over six weeks, each decline shallower than the last (higher lows into resistance â€” precursor present). In the final week it prints a 40-cent range pinned at $49.60â€“$50.00, about 15% of the six-week range's height (tight range near the extreme â€” precursor present). Two minor pokes above $50.00 in that final week snapped back within a bar (prebreakout springs/upthrusts â€” precursor present). Screen result: go.

Trade the base (Step 2): base is small (40 cents) relative to a projected 8-point measured move â€” not worth chasing an extra dime of entry price. Use the unconditional-fill trigger, buy at $49.85 inside the base.

Stop (Step 3, stage 1): base low is $49.55; initial stop at $49.45.

Breakout: stock gaps to $50.60 on heavy volume (signature confirmed: high volatility, negative/normal slippage â€” no surprise good fill). Stage-2 stop moves to just under the prebreakout base low ($49.45), NOT to $50.00.

First reaction (Step 4): stock pulls back to $49.70 â€” briefly violates $50.00 â€” on light volume with no sharp momentum, then bar closes at $50.10. This is a level violation without turkey-shoot character: treat as a normal pullback, not a failure. Hold the stop at $49.45 and manage the position as a trend trade from here (hand off to `grimes-pullback` / `grimes-trade-management` for the next leg).

## References

- Grimes, Adam. *The Art and Science of Technical Analysis* (Wiley, 2012), Ch. 5 "Interfaces between Trends and Ranges" â€” "Breakout Trade: Trading Range to Trend" section (precursor patterns, signature patterns, pullback-holds vs. pullback-violates, failure test / turkey shoot, failure pullback).
- Grimes, Ch. 6 "Practical Trading Templates" â€” "Breakout Base" and "Breakouts, Entering on First Pullback Following" templates (trigger options, adverse selection, two-stage stop, profit target logic, Turtles/channel-breakout caveat).
- Sibling skills: `grimes-four-trades` (where breakout trades sit in the four-trade taxonomy), `grimes-pullback` (post-breakout trend pullback management once one clean confirming pullback has occurred), `grimes-failure-test` (standalone failure-test fade at any level, not just post-breakout), `grimes-the-anti`, `grimes-trade-management` (position sizing, generic stop/target mechanics).
