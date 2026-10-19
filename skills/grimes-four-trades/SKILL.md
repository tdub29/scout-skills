---
name: grimes-four-trades
description: Classify any technical setup into exactly one of Wyckoff's four trade categories (trend continuation, trend termination, support/resistance holding, support/resistance breaking), read off that category's expectancy and failure modes, and map the current market phase (accumulation/markup/distribution/markdown) to which category to favor. Use when deciding whether a setup fits your edge, when comparing reward:risk across setup types, when a specialist keeps forcing one pattern into every market, or when auditing a watchlist for concentration risk. Triggers - "which of the four trades is this", "is this a continuation or termination trade", "market looks like distribution, what trade fits", "classify my setups", "why do my breakouts fail more than my pullbacks", "reward risk for fading this rally vs riding the pullback".
---

# Grimes' Four Trades

## What this decides

Every technical trade a trader can construct falls into exactly one of four categories.
This skill forces that classification, attaches the category's known probability/reward-risk
profile and failure modes, and cross-checks the classification against the current Wyckoff
market-cycle phase (accumulation, markup, distribution, markdown) to judge whether the
setup fits the environment. Output is a decision: **trade it as classified, resize it, or skip it
because the category doesn't fit the current phase.**

Do not use this to predict direction. It classifies a setup you already have in front of you
and tells you what kind of bet you're actually making.

## When to use

- A specific chart/setup needs to be graded before sizing or entry.
- You keep taking one kind of trade (e.g., breakouts) and want to know if the market phase
  supports it right now.
- You're comparing two competing ideas on the same instrument (e.g., short the rally vs. buy
  the pullback) and need their structurally different expectancy profiles made explicit.
- Auditing a watchlist or open-position book for category concentration.
- A trade lost and you want to know whether it failed *for its category* (expected) or failed
  in a way that says your classification was wrong.

## The four categories (exhaustive)

Wyckoff's cycle (accumulation -> markup -> distribution -> markdown) produces exactly two
trend trades and two support/resistance trades:

| # | Category | Direction relative to trend | Typical phase | Probability | Reward:Risk |
|---|---|---|---|---|---|
| 1 | **Trend continuation** | With the trend | Markup / markdown (also the accumulation->markup or distribution->markdown transition) | High | Modest, but compounds over multi-leg trends |
| 2 | **Trend termination** | Against the trend | End of markup / end of markdown | Low | Large â€” near-perfect trade location when right |
| 3 | **Support/resistance holding** | Fade a level, expect it to hold | Accumulation / distribution (range chop) | Moderate-high | Low â€” the weakest R:R of the four |
| 4 | **Support/resistance breaking** | Trade the level failing | End of accumulation / end of distribution | Low (most breakouts fail) | Can be large when it works, but slippage/gap risk cuts into it |

Note the pairing: continuation and termination are the two trend trades; holding and
breaking are the two ways a level can resolve. There is no fifth category â€” this is a closed
set, not a suggestive one.

## Method

1. **Identify the current phase.** Is price in a sideways range with a flat intermediate
   moving average and no public attention (accumulation)? An established uptrend with
   public participation (markup)? A sideways range after an uptrend, into which the smart
   money is selling (distribution)? An established downtrend (markdown)? If you cannot tell
   accumulation from distribution yet, say so explicitly â€” don't force a label.
2. **State what the setup is actually betting on**, in one sentence: "this bets the trend
   continues," "this bets the trend is done," "this bets the level holds," or "this bets the
   level fails." Whichever verb matches is the category. If two verbs seem to apply (e.g.,
   "buying support in an uptrend" is both continuation and holding), that's legitimate overlap
   â€” name both and use whichever framing matches your stated risk point.
3. **Pull that category's profile** from the table above and its failure modes below. State
   the expected win rate character (high/low) and reward:risk character (modest/large) before
   looking at the chart's specifics â€” this is the prior, not the conclusion.
4. **Check phase fit.** Cross-reference step 1 against the category:
   - Continuation trades belong in markup/markdown (or the breakout moment out of
     accumulation/distribution). Continuation setups appearing deep inside a range are
     low-conviction â€” the range hasn't resolved yet.
   - Termination trades belong at the end of an extended markup/markdown. A termination
     bet three bars into a fresh trend has no basis â€” there's nothing extended to terminate.
   - Holding trades belong inside accumulation/distribution. A holding trade against a level
     mid-trend is really a continuation trade wearing a support-holding costume (see step 2).
   - Breaking trades belong at the accumulation/distribution boundary. A breakout attempted
     in the middle of an established trend is usually a lower-timeframe entry into the
     higher-timeframe trend, not a true regime-change breakout â€” reclassify or flag as
     "with-trend, not phase-defining."
   If the category doesn't fit the phase, that's a reason to skip or downsize, not a reason
   to relabel until it fits.
5. **State the decision**: trade as classified at normal size; trade at reduced size because
   phase fit is weak; or pass, and note which category *would* fit once the phase confirms.
6. **Log the category alongside the trade.** Over a run of trades, tally category
   distribution. A book that is 90% one category is a specialist book (fine if chosen
   deliberately) or a hammer-looking-for-nails problem (not fine if it happened by accident).

## Sub-rules and failure modes (per category)

- **Trend continuation** â€” high-probability, statistically grounded (trend persistence is
  a real edge), but risk is hard to define tightly: the stop has to sit at the point the trend
  is "conclusively wrong," which is often far from entry. Failure mode #1: not enough
  with-trend pressure for another leg, so the market rolls into a range instead â€” usually a
  polite, small loss. Failure mode #2: pullbacks in strong trends are frequently complex,
  two-legged consolidations, not simple V-shapes â€” plan for that shape before entry, don't
  discover it mid-trade. Failure mode #3 (rare but severe): everyone is leaned the same
  way in an overextended trend, and the unwind is violent when it comes.
- **Trend termination** â€” low-probability by design; true reversals (selling the exact high)
  are rare, and the correct win condition is narrower: "the trend stopped," not "the trend
  reversed." Redefine success before entry or you'll misjudge good trades as failures.
  Reward:risk can be excellent because trade location is precise. Failure mode: this is a
  countertrend trade, and countertrend traders who add to losers as the trend keeps going
  are the classic account-blowing pattern; gap risk against overnight swing positions is real.
  Iron discipline on stops is non-negotiable here â€” more than in any other category.
- **Support/resistance holding** â€” as a group, the *lowest* reward:risk of the four, because
  the market sits in near-equilibrium just above/below the level that "holds," so most
  favorable entries are in a suboptimal, choppy zone. Failure mode: support/resistance rarely
  holds cleanly â€” dropouts below support (stop runs) are part of *why* it holds, not evidence
  it's broken, which creates a scale-in dilemma (sell on every undercut and eat small losses
  repeatedly, or hold through undercuts and occasionally eat a large one). Exception that
  breaks the low-R:R rule: failed breakouts are a high-probability subset of this category,
  because a failed breakout means the crowd was leaning the wrong way.
- **Support/resistance breaking** â€” most breakouts fail; this is a low base-rate category
  despite being the most heavily marketed pattern in trading literature. Failure mode: breakout
  zones are high-volatility, low-liquidity, and crowded (everyone watches the same level), so
  slippage and thin execution erode edge more here than in any other category. Realized losses
  on failed breakouts can be multiples of intended risk â€” factor that into position sizing, not
  just the ideal stop distance. The best breakouts are pre-built (higher lows into resistance
  before the break, trapped counterparty flow forced to chase after) â€” reactive, unplanned
  breakout entries are a weak version of the category, not the category itself.

## Worked mini-example

Setup: a stock has rallied for eight weeks, is up 40%, public chatter about it is loud, and
today it gapped up sharply intraday before stalling and closing near the day's low.

1. Phase: the extended rally plus heavy public attention argues this is late markup, possibly
   transitioning into distribution.
2. What's the bet: fading today's stall for a short â€” this bets the trend (or at least this
   leg) is done. Verb = "terminates." Category = **trend termination**.
3. Profile: low probability, potentially large reward:risk if right, precise trade location
   (today's high) if the stall holds.
4. Phase fit: strong â€” trend termination trades are specifically expected at the
   markup-to-distribution boundary, and this rally is extended enough to plausibly be there.
5. Decision: trade is well-classified and phase-appropriate. Size for a countertrend bet
   (smaller than a continuation trade would get), stop just above today's high (the point the
   termination thesis is conclusively wrong), and treat "the rally simply stops going up" as
   the win condition â€” do not require a full reversal to call it a success.
6. Contrast: if instead the plan had been "buy the next pullback in this rally," that setup
   would classify as **trend continuation**, phase-appropriate too (markup), but with a
   different profile entirely â€” higher probability, tighter definition of "wrong," smaller
   individual reward. Neither is more correct; they are different bets with different
   expectancy shapes, and conflating them (sizing a termination trade like a continuation
   trade, or vice versa) is the actual error this skill exists to catch.

## References

- Adam Grimes, *The Art and Science of Technical Analysis* (Wiley, 2012), Ch. 2 "The Market
  Cycle and the Four Trades" (pp. 31-45), with the first-principles recap in Ch. 5.
- Siblings in this carve: `grimes-pullback`, `grimes-failure-test`, `grimes-the-anti`,
  `grimes-breakout-trade`, `grimes-trade-management`.
