---
name: katz-exit-strategy-taxonomy
description: Classify and combine exit types (money-management stop, trailing stop, profit target, time exit, barrier/critical-threshold exit, volatility exit, signal exit, shrinking target) for a trading system, and set stop/target tightness against the tightness-vs-win-rate tradeoff. Use when asked to design, choose, or critique an exit strategy â€” "what exit should I use for a trend-following system," "barrier stop vs volatility exit," "how tight should my stop be," "classify types of trading exits," "design a coordinated trailing + target + time exit." From Katz & McCormick, The Encyclopedia of Trading Strategies, Part Three Introduction / Ch. 13-14.
---

# Katz Exit-Strategy Taxonomy

## What this decides

Given a trading system's character (trend-following vs. countertrend, entry
frequency, reentry capability, market volatility), which exit types to
combine into one coordinated exit strategy, and roughly how tight to set
each stop/target. Output is a named exit stack, not a single number: e.g.
"money-management stop (1.5Ã—ATR) + MEMA trailing stop + catastrophe barrier
stop + 10-day time exit, no fixed profit target" for a trending system.

An exit strategy is a *portfolio of exits acting together*, not one order
type. Every complete design needs at minimum a money-management stop; the
rest is chosen by system character.

## When to use

- Building or reviewing the exit rules for any system (discretionary or
  mechanical) once entries are already decided.
- Someone asks whether to use a stop, a target, a time limit, or some
  combination â€” or claims "tighter is always safer."
- Reviewing a backtest where an exit design change is on the table.
- Not for entry-signal design (see sibling skills) and not for position
  sizing â€” this is exit *type and placement* only.

## Method

1. **Classify the system.** Trend-following with reentry capability, or
   countertrend / mean-reversion, or unknown/mixed. This single fact drives
   most of the rest.
2. **Always start with a money-management stop.** Non-negotiable â€” no exit
   strategy is complete without one. Set placement by one of: fixed dollar
   risk, volatility multiple (e.g. 1-2.5Ã— average true range), or a
   support/resistance barrier if one exists close enough to entry to keep
   risk acceptable. A barrier-based stop can usually be tighter than a
   dollar- or volatility-based one for the same protection.
3. **Add a catastrophe stop with the broker**, placed far outside the
   working stop, as a backstop for wide gaps and phone/system failure â€” not
   as the primary risk control (see sub-rule 2).
4. **Pick the profit-taking leg by system type:**
   - Trend-following, reentry-capable â†’ trailing stop (HHLL, ATR-relative,
     or MEMA â€” see "Dynamic trailing-stop variants" below), no fixed profit
     target (or a very wide one), and a loose/generous time limit. Riding
     the trend to maturity is the point; a tight target amputates it.
     "The trend is your friend" â€” cutting a big winner short to bank a
     small one defeats the system's edge.
   - Countertrend / no-reentry / choppy market â†’ tight fixed profit target
     (raises win rate, a Katz stated preference) paired with a tighter
     money-management stop, since the trade thesis expires quickly if
     wrong.
   - Trade going nowhere (neither stop nor target triggers) â†’ add a
     **shrinking target**: set the target far away initially, then
     continuously pull it in toward the current market price as the trade
     ages, so a small favorable wiggle late in a stalled trade exits
     cleanly instead of tying up margin indefinitely.
5. **Add a time-based exit as a backstop in all cases** â€” if nothing has
   triggered after N bars, exit at market. It never replaces the other
   exits; it catches what they miss.
6. **Layer in volatility/signal/barrier exits only if the system has a
   specific hazard to hedge:** a volatility exit for blow-off-top /
   event-risk conditions (sell into the frenzy â€” this is also a
   contrarian, into-liquidity exit); a signal exit when a (possibly less
   reliable) contrary indicator fires â€” exits can tolerate more false
   alarms than entries because a missed exit risks the account while a
   missed entry just waits for the next opportunity; a barrier/
   critical-threshold exit whenever a trendline, support/resistance level,
   or Fibonacci/Gann line sits close enough to serve as a tight, principled
   stop or trail point.
7. **State the tradeoff explicitly, don't just pick a number.** For every
   stop or target width chosen, name what's being traded: tighter stop =
   more, smaller losses + more sacrificed winners; wider stop = fewer
   losses hit but each is bigger. There is no free tightening.
8. **Output the final design as a labeled stack** (money-mgmt stop type +
   width, catastrophe stop, trailing type if any, target type if any, time
   limit, any volatility/signal/barrier overlays) plus one sentence per leg
   naming why it's there.

## Sub-rules / failure modes

1. **Tight stops raise the loss rate even as they cap per-loss size â€” say
   so, don't hide it.** A $50 stop on the S&P can produce ~95% losing
   trades even in a system with real edge, because it stops out on noise
   before the move develops. Report win-rate impact alongside per-loss
   savings whenever you tighten a stop.
2. **Stops get gunned; the fix is a catastrophe stop, not a tighter working
   stop.** Floor/algo flow can push price to trigger visible tight stops
   for a few ticks. The real stop lives only in the trader's system
   (alerts, doesn't route to the exchange); a catastrophe stop is placed
   with the broker far from price purely as a disaster backstop. Confusing
   the two â€” making the *broker-side* stop the tight one â€” reintroduces
   the exact gunning risk the design is meant to avoid.
3. **Stops slip, limits don't â€” cost the difference in, don't ignore it.**
   A stop order in a fast market can execute far worse than its trigger
   price (a $500 stop can fill at $700-800 loss in a fast tape); a limit
   order (profit target) fills at its price or better but can simply not
   fill during a gap or halt. When comparing a stop-based exit to a
   limit-based one, price in slippage on the stop side and fill risk on the
   limit side â€” don't compare their nominal levels as if they were
   equivalent.
4. **Exit into liquidity, not into the same panic everyone else is
   selling/buying into.** Profit targets and volatility exits (selling a
   blow-off top, "buy the rumor sell the news") naturally exit into
   liquidity â€” into a crowd doing the opposite â€” which improves fills. A
   design that only exits on stops (selling into a crash alongside
   everyone else) misses this free edge; add at least one liquidity-side
   exit leg when the system allows it.
5. **Entries conservative, exits liberal â€” asymmetric tolerance for false
   alarms.** A missed entry costs nothing (another will come); a missed
   exit can cost the account. Signal exits are allowed to use a less
   reliable indicator than the one used for entry, and are allowed more
   false positives, because the asymmetric cost of a missed exit outweighs
   the cost of a slightly early one.
6. **Don't test one exit leg in isolation and call it validated.** Unlike
   entries, exit legs must be tested as a coordinated strategy â€” pulling
   one leg (e.g. removing the money-management stop to "isolate" the
   profit target) changes the risk profile of every other leg, because
   exposure is otherwise unbounded until some exit fires.

## Dynamic trailing-stop variants (detail from Ch. 14)

All three are trailing-leg implementations parameterized in volatility
(ATR) units, applied once a trade is favorable â€” pick by how responsive the
trail should be to noise vs. trend structure:

- **HHLL (highest-high/lowest-low) stop:** trails the highest high (long)
  or lowest low (short) achieved since entry, offset by a multiple of ATR.
  Simplest, jumps only when a new extreme prints; good default for clean
  trends.
- **ATR-based dynamic stop:** stop level = current price minus (money-mgmt
  parameter Ã— ATR), recalculated every bar and only allowed to move in the
  favorable direction (ratchets, never loosens). More continuously
  responsive than HHLL.
- **MEMA (modified exponential moving average) stop:** stop tracks a
  smoothed moving average of price, offset by an ATR-based amount, with an
  adaptation-rate coefficient controlling how fast the average â€” and
  therefore the stop â€” catches up to price. In Katz's own tests this was
  the best-performing of the three; treat it as the default when a
  smoother trail than HHLL is wanted and the extra parameter (adaptation
  rate) can be tuned/optimized.

Any of the three can double as a barrier exit if the offset happens to
align with a real trendline or support/resistance level â€” that alignment
is a bonus, not a requirement.

## Worked mini-example

**System:** breakout entry on the S&P 500, trend-following, single-contract
(no reentry), tested to hold winners for many days when a trend develops.

1. Classify: trend-following, no reentry â†’ protect against amputating a
   big winner.
2. Money-management stop: 1.5Ã— ATR below entry (volatility-based, since no
   nearby support/resistance barrier exists at entry).
3. Catastrophe stop: placed with the broker at 4Ã— ATR, pure backstop.
4. Profit-taking leg: MEMA trailing stop, initial parameter 2.5Ã— ATR, ATR
   offset 1, adaptation rate ~0.30 (Katz's best-tested MEMA configuration)
   â€” no fixed profit target, since the system can't reenter and a target
   would cap the trend capture that is the system's entire edge.
5. Time exit: 10 days with neither stop nor trail triggered â†’ exit at
   market (catches languishing, non-trending chop).
6. Shrinking target: not needed here since the trailing stop already
   handles languishing trades by tightening as price stalls near the
   trail; would add one if the trail were HHLL-based and thus slower to
   react to sideways drift.
7. Overlay: no signal or volatility exit added â€” no independent reversal
   indicator or event-risk calendar in scope for this system.
8. Tradeoff stated: 1.5Ã— ATR money-mgmt stop will sacrifice some winners
   to whipsaw versus a 2.5Ã— ATR stop, in exchange for materially smaller
   average loss; this is accepted because the MEMA trail, not the initial
   stop, is expected to do most of the profit-capturing work.

**Output:** "1.5Ã—ATR money-mgmt stop + 4Ã—ATR catastrophe stop + MEMA trail
(2.5 ATR init / 1.0 ATR offset / 0.30 adapt) + 10-day time exit, no fixed
target."

## References

- Katz & McCormick, *The Encyclopedia of Trading Strategies* (2000,
  McGraw-Hill), Part Three Introduction "The Study of Exits," Chapter 13
  "The Standard Exit Strategy," Chapter 14 (dynamic stops, MEMA, shrinking
  target).
- Siblings in this book-carve family: `katz-component-isolation-testing`,
  `katz-system-significance-test`, `katz-filter-bank-cycles`,
  `katz-ga-rule-discovery`.
