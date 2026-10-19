---
name: grimes-pullback
description: Build a with-trend continuation trade off a pullback (flag/pennant/wedge/ABCD retracement) â€” qualify the trend via impulse-retracement-impulse, classify the pullback as simple, complex/ABCD, or hidden-complex, pick one of two entry triggers (trendline/channel failure-and-reverse, or direct support/resistance test), set a near-vs-far stop with jitter, and stack a three-tier profit target (prior swing / AB=CD measured move / R-multiple). Use whenever the user is trading, backtesting, or reviewing a with-trend pullback, a countertrend retracement inside an established trend, a flag/pennant/wedge continuation setup, buying support or shorting resistance mid-trend, an ABCD or two-legged pullback, a "buying support in a pullback" entry, or asks where to place stops/targets on a pullback trade, whether a pullback is still tradable after multiple tests, or how to size a second attempt after a stopped-out pullback.
---

# Grimes Pullback (With-Trend Continuation)

Source: Adam Grimes, *The Art and Science of Technical Analysis* (2012, Wiley), Ch. 3 "On Trends" (trend qualification) and Ch. 6 "Practical Trading Templates" (pullback, complex pullback, lower-time-frame-breakout entry templates), illustrated in Ch. 10 "Trend Continuation."

## What this decides

Given a market believed to be trending, and a countertrend retracement ("pullback") currently forming against that trend, this skill decides:

1. Whether the trend/pullback is even tradable (qualification gate).
2. Which entry trigger to use.
3. Whether the pullback is simple, complex (ABCD), or a hidden complex pullback â€” because that classification changes where the stop goes and what the second-leg target is.
4. Where the stop goes (near vs. far school, with jitter).
5. Where profits come off (three-tier stack).
6. What to read into the setup if it's already failing (avoid-condition + loss-sequencing risk).

It does **not** decide whether to trade *countertrend* against the retracement (that's a failure-test / reversal question â€” see `grimes-failure-test`) or how to size positions in general (see `grimes-trade-management`).

## When to use

- A market is in an established trend and has pulled back (flag, pennant, wedge, continuation triangle â€” treat all of these as the same functional pattern).
- The user is asking "do I buy this dip / short this bounce" inside a trend.
- The pullback has legs that look like two down/up moves separated by a small counter-move (possible ABCD complex pullback).
- The user just lost on a pullback trade and the market is setting up again nearby.
- The user wants to time entry using a lower-time-frame breakout inside the pullback.

Do not use for: entries at the *first* pullback after a suspected trend change (that's the Anti / `grimes-failure-test` territory), for breakout-from-range trades with no prior trend (see `grimes-breakout-trade`), or for exit/scaling mechanics once already in a trade beyond what's specified here (see `grimes-trade-management`).

## Method

### 1. Qualify the trend and the setup leg (gate â€” do not skip)

A pullback is only a with-trend continuation trade if the underlying structure is genuinely `impulse â†’ retracement â†’ impulse` (i.e., the pullback is expected to resolve into a third leg with the trend). Check:

- The **setup leg** (the impulse immediately preceding the pullback) must be at least as strong as prior trend legs in the same direction â€” no momentum divergence, no visible break in the pattern of the trend.
- No standard countertrend preconditions are present (momentum divergence, overextension on higher time frames, climax exhaustion â€” see step 3's exception).
- The pullback itself shows **reduced activity**: smaller bar ranges and absence of strong countertrend momentum on the trading time frame (lighter volume is common but not the defining test â€” activity/momentum is).
- Market character matters: some instruments/time frames trend cleanly through many legs (grains, petroleum, currencies, rates on higher time frames, high-news individual equities); others rarely extend past ~3 legs (many intraday index products) and meats tend not to trend well. Calibrate expectations for how many legs you should expect before treating a "pullback" as instead a top/bottom.

If any qualification fails â†’ do not take this as a with-trend continuation trade. Reroute: if setup instead looks like a trend-change signature (loss of momentum on successive thrusts, double top/bottom, failure test, followed by a stronger-than-usual countertrend move), see `grimes-failure-test` (the Anti pattern) instead.

If qualified, stay responsive after entry too: if developing price action after entry suggests the trend is losing integrity, scratch the trade for a small win/loss rather than holding to the original stop â€” do not treat the stop as the only exit trigger.

### 2. Classify the pullback: simple / complex (ABCD) / hidden complex

- **Simple pullback**: one clean countertrend leg into support/resistance.
- **Complex pullback**: a complete ABCD structure in miniature â€” countertrend leg (AB), retracement of that lower-time-frame move back toward the higher-time-frame trend direction (BC), then a second countertrend leg (CD). Very common in mature trends; some of the *best* pullbacks (cleanest follow-through) are complex ones.
- **Hidden complex pullback**: on the trading time frame it looks like a simple pullback, but one or two with-trend-colored candles sit buried in the middle of it â€” an aborted attempt to resume the primary trend. Candle-color cue: pullback candles are normally colored *against* the trend that set them up (uptrend pullback = red/filled candles); a red candle appearing mid-pullback-in-an-uptrend is the tell that this is really an ABCD hiding under the trading time frame. Confirm on a lower time frame if uncertain, though experienced reading from the trading time frame alone is usually sufficient.

**Climax-avoidance exception, with an escape hatch:** normally avoid entering a with-trend pullback right after a buying/selling climax (parabolic expansion) â€” climaxes frequently cap trends outright. But if price does *not* immediately reverse hard and instead consolidates as a **complex** pullback in that same area, a with-trend entry off that complex consolidation is back on the table (evaluate trend integrity on the higher time frame, where the trading-time-frame complex pullback usually reduces to a simple one).

### 3. Pick the entry trigger

Two valid triggers (same two apply to simple, complex, and hidden-complex pullbacks):

**Trigger A â€” trendline/channel failure-and-reverse.** Draw a trendline on both sides of the pullback, or a parallel trend channel if a clean two-sided trendline isn't available. Entry fires when price penetrates the line/channel and then recovers back above (below, for shorts) it within a few bars. This washes out the traders who bought/sold the literal touch of support/resistance and often coincides with a small lower-time-frame climax (a single long-shadow candle at the exhaustion point is the visual tell). Best trade location of the two triggers, often very near the actual pullback extreme â€” but it demands real skill to read in real time, since the exhaustion shows up on a single bar. Not a "set and forget" entry.

**Trigger B â€” direct support/resistance test.** Buy against support / sell against resistance at the pullback extreme itself, without waiting for a failure-and-reverse. Easier to spot on historical charts than to execute live. Stop placement is the weak point: support can still drop and wash you out before the recovery (which is exactly Trigger A's setup) â€” so risk must be explicit and respected.

Sub-rule â€” **avoid the 3rd+ test of support/resistance in one pullback.** Successive bounces making lower highs into the level (uptrend case) signal fewer willing buyers each time and skew toward failure. Multi-test complex pullbacks with 3+ legs exist but are uncommon and less reliable â€” don't make them a plan focus. If you're looking at a pullback that has already tested the level three or more times, treat it as lower-probability and either skip it or size down.

Sub-rule â€” **lower-time-frame-breakout entry variant.** Instead of triggers A/B, time entry into the pullback using a breakout of structure inside the pullback visible on a lower time frame (e.g., resistance break on a 78-minute chart confirming entry into a daily pullback). Trade-off: worse trade location, but you get momentum confirmation, so use a wider, geometry-respecting stop (not a hair-trigger stop with a plan to reenter repeatedly â€” that just stacks transaction costs and spread with no edge improvement). Same profit targets as any other pullback trade apply.

Sub-rule â€” **"buying support in a pullback" that behaves like a snap-back entry.** If you're deliberately entering the moment price is testing (not yet failing) a sloping support/resistance level inside a pullback, that is functionally a failure-test / spring-upthrust style entry â€” cross-reference `grimes-failure-test` for the stop-and-plan discipline that pattern requires, since the mechanics (buy the wash-out, not the level) are shared.

### 4. Place the stop

Support/resistance in pullbacks usually **slopes** â€” do not treat it as a flat line, and do not exit a trade still living inside the sloping level just because price moved further than "expected."

Two schools, pick deliberately (this is a plan decision, not an in-the-moment one):

- **Near stop**: tight, just past the pattern. Minimizes loss magnitude but raises the probability of getting stopped, so in expected-value terms it is not automatically the "lower-risk" choice.
- **Far stop**: placed with more room, deliberately away from the obvious level. Add a small random **jitter** (a few ticks/cents beyond the obvious stop cluster) â€” markets tend to seek out the stops that "everyone" places at the exact obvious level.

For **complex pullbacks specifically**, the stop is easier and more defensible: placing it just beyond the termination of the second (CD) leg is often an excellent risk point â€” an advantage complex pullbacks have over simple ones, where a stop right under the consolidation is usually a bad idea.

Every trade of this type should carry an equivalent, pre-sized risk â€” there is no such thing as a structurally "low risk" trade just because the stop is tight; size the position to the stop, not the other way around. Active management still applies on top of whichever school you pick: stops may be tightened a few bars into the trade, and a time stop can be layered on.

### 5. Stack the profit target (three tiers, not one)

1. **Prior-swing target (conservative)**: the pivot high of the setup leg (longs) or pivot low (shorts). Take partial profit here; strongest trends will clear this level and extend into another leg, so don't take everything off.
2. **AB=CD measured-move objective (MMO)**: take the length of the setup leg (Aâ†’B), project it forward from pivot C, expect the Câ†’D leg to run roughly the same distance. Treat this as a *zone*, not an exact print â€” if the market stalls near it without quite touching it, take partial or full profits anyway rather than waiting for the exact number.
3. **R-multiple target**: take partials at 1R or 2R off initial risk. Reconcile this against tiers 1â€“2: if the R-multiple target lands close to the conservative swing target, collapse to that level; if it lands well beyond it, recognize you're skewing reward/risk and decide deliberately rather than by default.

For **complex pullbacks**, it's reasonable to hold a larger share past tier 1, expecting a stronger move â€” but weigh that against the discipline benefit of a simple, consistent rule (e.g., always take 1/3 off at tier 1) before overriding it.

### 6. Read failure

- A pullback that has tested support/resistance 3+ times without resolving is a **failure warning**, not just lower-probability â€” treat continued waiting as the default, not continued entries.
- **Loss-sequencing risk**: a complex pullback often shows up right after a *loss* on a simple pullback in the same area (the failed simple pullback often *is* the AB leg of the complex one). Before re-entering, have a pre-set answer for how much risk you allow yourself to re-deploy in the same spot â€” this is a risk-management decision to make in the trading plan, not in the moment.
- If price breaks the far side of what should have been a complex pullback's second leg with strong countertrend momentum, stop treating it as a pullback â€” the higher-time-frame trend itself may be over; hand off to trend-change analysis (`grimes-failure-test`) rather than forcing a continuation read.

## Worked mini-example

EURUSD is in a clean uptrend; the setup leg into the pullback shows no divergence. Price retraces: down-leg (Aâ†’B) on the trading time frame, small up-bounce (Bâ†’C), then a second down-leg (Câ†’D) â€” visible as three separate legs. **Classification: complex (ABCD) pullback**, not simple.

- **Trigger**: price tests support at D, breaks it briefly, then snaps back above within a few bars â†’ Trigger A (failure-and-reverse).
- **Stop**: placed just beyond D (the termination of the second leg) â€” the complex-pullback advantage of a clearly defined risk point. Add a few pips of jitter beyond the obvious swing low.
- **Targets**: Tier 1 = prior swing high (pivot before A). Tier 2 = C + (length of Aâ†’B), the AB=CD projection for the next leg up. Tier 3 = 1.5R off entry, cross-checked against tiers 1â€“2 and collapsed toward whichever is closer.
- **Failure read check**: this is the first test of this support zone (not a 3rd+ test), and no buying-climax preceded the pullback, so no override is triggered â€” trade is a go long with a pre-sized position at the far+jitter stop.

## References

- Adam Grimes, *The Art and Science of Technical Analysis*, Ch. 3 "On Trends" (trend qualification, impulse-retracement-impulse), Ch. 6 "Practical Trading Templates" â€” "Pullback, Buying Support or Shorting Resistance," "Pullback, Entering Lower Time Frame Breakout," "Trading Complex Pullbacks" â€” illustrated in Ch. 10 "Trend Continuation."
- Sibling skills: `grimes-four-trades` (where pullback sits among the four core trade types), `grimes-failure-test` (spring/upthrust "2B" pattern; the "buying support" wash-out variant and the Anti trend-change pattern both live here), `grimes-the-anti` (first pullback after a suspected trend change â€” the countertrend cousin of this skill), `grimes-breakout-trade` (breakout-from-range entries, no prior trend required), `grimes-trade-management` (general position sizing, scaling, and stop-management discipline referenced but not fully specified above).
