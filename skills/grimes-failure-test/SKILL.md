---
name: grimes-failure-test
description: "Trade a false breakout that closes back inside"
---

# Failure Test (Wyckoff Spring / Upthrust / Sperandeo "2B")

## What this decides

Given a bar (or two) that presses beyond a defined support/resistance level or trend
extreme and closes back inside it, this skill decides: (1) whether it qualifies as a failure
test at all, (2) the exact entry, stop, and first-target prices, (3) how to manage the trade
bar-by-bar, and (4) â€” if it stops out or stalls â€” which failure mode it is and what that
mode obligates you to do next (re-enter, scratch, or hold).

Output is not "this looks like a false breakout." Output is a numbered trade plan with
entry price, stop price, 1R partial-exit price, a runner rule, and a named failure
classification the moment the trade stops behaving.

## When to use

- Price trades beyond a clearly defined support/resistance level, prior swing high/low,
  or trend extreme, then reverses and closes back on the other side, same bar or next bar.
- You are evaluating whether a stop-out on a failure test entry obligates a second attempt.
- A failure test entry has gone sideways instead of reversing sharply, and you need to
  decide whether to hold, reduce, or scratch.
- A failure test position gapped hard overnight and you need a same-morning hold/exit call.
- You are looking for a countertrend entry after a parabolic climax, after a long
  consolidation near a trend extreme, or as a lower-timeframe entry into higher-timeframe
  structure (weekly base + daily failure test at the low).

Do not use for: a level that price approaches but never actually trades beyond (that's a
simple support/resistance bounce, not a failure test); a breakout that holds and
consolidates above/below the level without a same/next-bar reversal close (see
`grimes-breakout-trade` â€” this is the opposite outcome, a *successful* breakout); ordinary
with-trend pullbacks that never probe beyond a level (`grimes-pullback`).

## Method

1. **Confirm the setup context.** The market should be overextended or otherwise primed
   for reversal â€” a mature, extended trend (ideally with momentum divergence on the
   trading timeframe), or an extended consolidation sitting just under a resistance level
   (or over a support level) that many traders are watching for a breakout. Do not
   pre-position ahead of the level; you need the actual press-and-reject, not an
   anticipation of one.
2. **Identify the trigger bar.** Price trades beyond the level â€” same bar or within 2-3
   bars of first breaching it â€” then closes back on the origin side of the level. This is
   close-based, not intrabar: a bar that pokes beyond the level and comes back intrabar
   without a close beyond it is not yet a failure test (there was no breach to fail from);
   a bar that closes beyond the level and stays beyond it on subsequent closes is not a
   failure test either (it's a live breakout â€” reclassify accordingly).
3. **Enter on the close of the reversal bar.** Short on the close of the bar that closes
   back below a resistance level after trading above it; long on the close of the bar that
   closes back above a support level after trading below it (symmetrical). Waiting for the
   close sacrifices some price in exchange for confirmation â€” an acceptable, disciplined
   trade-off. Do not chase an intrabar reversal unless you accept a materially higher
   loss rate.
4. **Place a hard stop at or just beyond the test extreme.** Use the high (for a short) or
   low (for a long) of the most extreme bar in the excursion beyond the level â€” not
   necessarily the trigger/entry bar itself if an earlier bar in the same excursion poked
   further. Placing the stop a few cents/ticks *inside* the extreme (rather than clearly
   outside it) trades a rare premature stop-out for meaningfully less slippage on the much
   more common clean exits â€” net favorable. Respect this stop without question; do not add
   to a losing failure test.
5. **Take a partial at 1R, manage the remainder discretionarily.** Close roughly a third to
   half the position when open profit equals initial risk (distance from entry to stop).
   Run the rest with a plan for either quick continuation into a full reversal or a
   let-it-breathe exit at the next structural level. Some failure tests become major trend
   reversals; that is the tail outcome, not the base case â€” do not plan the trade sizing
   around it.
6. **Watch for consolidation near the level in the first 1-3 bars after entry.** If the
   1R target is not hit within roughly three to four bars, that is itself a warning sign â€”
   reduce exposure or scratch near breakeven rather than waiting for the stop.
7. **Classify any failure the moment it happens**, and act on the classification (see
   sub-rules below): failure by consolidation â†’ scratch, don't wait for the stop; failure
   with a same/next-bar reversal back inside the level â†’ treat the second failure as an
   (effectively obligatory) re-entry at reduced size; failure by large adverse gap â†’ take
   the loss at the print, do not average or hope for a retrace.

## Sub-rules and failure modes

- **Failure by consolidation.** If price does not move sharply away from the level within
  1-3 bars â€” instead grinding sideways near it â€” this is inconsistent with a genuine
  failure test (a working failure test produces immediate, visible price rejection) and
  is instead consistent with an impending breakout/continuation of the original trend.
  Reduce or exit once the first-target window has passed without a hit; don't wait for the
  stop to be touched. Worst acceptable outcome here is a scratch near entry, not a full
  stop-loss.
- **Obligatory second entry after a stop-out.** If the stop is hit and then, on the same
  or the very next bar, price falls back inside the level again, take the second failure
  test entry. This setup recurs often enough that Grimes calls it "virtually obligatory."
  Size both attempts so their *combined* risk does not meaningfully exceed the risk budget
  of a single normal trade (i.e., roughly half-size each) â€” skipping the stop-out
  discipline on the first attempt because "it'll probably come back" is the mistake to
  avoid; too many first failures blow through the extreme by a lot instead of reversing.
- **Failure by large adverse gap.** Because this is a countertrend entry positioned right
  at a trend extreme, a trend-continuation gap against the position is a real tail risk â€”
  rarer than a gap toward the first target, but more damaging when it happens. Take the
  loss at the gap price; do not add or wait for a retrace. This is the specific reason to
  trade failure tests at reduced size (roughly half of normal with-trend position size)
  as a default, not just when a setup looks marginal.
- **Named variants â€” same trigger/stop/target rules, different context clues:**
  - *Second-day entry:* the extreme is made and closed slightly beyond the level on day
    one; day two trades higher/lower still, then reverses to close back inside. Entry is
    on the close of day two, stop above/below day two's intrabar extreme.
  - *Following a long consolidation:* a consolidation 3-4x the length of the market's
    normal consolidations, sitting near the trend extreme, is a good countertrend
    candidate â€” don't be talked out of it by its apparent "coiling for continuation" look.
  - *Following a climax* (three pushes, parabolic expansion, multiple wide-range bars):
    do not front-run the climax itself; wait for the first reversal off the climactic
    structure, then watch for a failure test on the retest of that extreme.
  - *As entry into higher-timeframe structure:* a daily/hourly failure test at a level
    that aligns with bullish (or bearish) weekly structure is a higher-quality version of
    the same trade â€” prefer these when available.
- **Not a failure test until the close confirms it.** An intrabar poke beyond a level that
  never closes beyond it has nothing to fail from â€” that's just the level holding, not a
  failure test entry (no new trigger, no new stop logic beyond ordinary support/resistance
  trading).

## Worked mini-example

Stock in a multi-month uptrend, showing a clear change of character (a sharp sell-off
that breaks the pattern of prior pullbacks) â€” this is the justification needed before
considering a countertrend short at all.

1. Setup: price presses to a marginal new high, then reverses hard intraday and closes
   well below the prior swing high.
2. Entry: short on the close of that reversal bar.
3. Stop: at (or a few cents inside) the high of the reversal bar / the highest point of
   the excursion above the prior swing high.
4. Management: next bar gaps down and quickly exceeds the 1R target â€” take the partial.
   A subsequent 1-2 bar consolidation that then breaks down further is a green light to
   hold the runner; a consolidation that does *not* break down cleanly, or that eats
   into 3-4 bars without new lows, is the "failure by consolidation" tell â€” cut the
   remainder near breakeven-to-small-gain rather than giving it back to a full stop.
5. If instead the stop had been hit by one tick and price closed back below the level on
   the very same or next bar, re-enter short there at reduced size â€” the obligatory
   second-failure entry â€” with a fresh stop above that bar's high.

## References

- Grimes, Adam. *The Art and Science of Technical Analysis* (Wiley, 2012) â€” Ch. 6
  "Practical Trading Templates," Failure Test template (pp. 150-153); Ch. 10 "Trend
  Termination," Failure Test / Failure Test, Second-Day Entry / Failure Test, Other
  Variations / Failure Test Failures / Failure Test, Other Failures (pp. 313-323);
  glossary entries "failure test," "upthrusts," "spring," "2B" (Sperandeo).
- Sperandeo, Victor (1993) â€” originator of the "2B" trade terminology for this same
  pattern.
- Sibling skills in this family: `grimes-four-trades`, `grimes-pullback`, `grimes-the-anti`
  (parabolic climaxes can set up an Anti trade instead of a failure test â€” see that
  skill for the distinguishing criteria), `grimes-breakout-trade` (the complementary
  outcome when the level does *not* fail), `grimes-trade-management` (general partial-profit
  and risk-sizing rules that this skill's 1R-partial step draws on).
