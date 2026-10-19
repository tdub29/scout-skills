---
name: williams-position-sizing
description: Compute how many contracts or shares to trade using Larry Williams' money-management formula â€” (account balance Ã— risk%) / largest historical loss â€” and flag when the chosen risk% is dangerous. Use when sizing a futures/stock position from account balance, a risk percentage, and a system's largest loss; when picking a risk-per-trade percentage by risk personality (Tommy Timid, Normal Norma, Leveraged Larry, Swashbuckling Sam); when asked whether a risk% will blow up an account; or when asked why raw Kelly or Optimal F is unsafe for position sizing. Triggers: "how many contracts should I trade", "size my position", "risk % per trade", "will this risk percent blow up my account", "Kelly formula for trading", "Optimal F", "money management formula", "largest loss position sizing".
---

# Williams Position Sizing

## What this decides

Given an account balance, a chosen risk percentage, and a trading system's
**largest historical loss (per contract/share)**, produce:

1. A specific number of contracts/shares to trade on the next trade.
2. A blow-up warning: how many consecutive max-losses would wipe out
   40-80% of the account at that risk%, so the trader can see the tail risk
   before it happens, not after.

This is not a forecasting or entry-signal skill. It answers exactly one
question: *how big should the next bet be?*

## When to use

- User gives (or can get) account balance, a risk%, and the system's worst
  losing trade, and wants a contract/share count.
- User names a risk-personality tier ("I'm Leveraged Larry") and wants the
  matching risk% and resulting size.
- User proposes a risk% (e.g., 25%, 40%) and wants to know if it's reckless.
- User asks why not just use Kelly or Optimal F for sizing.

Do not use for stop-placement, entry timing, or system design â€” this
consumes a system's largest loss as an input, it doesn't produce one.

## Method

1. **Get the three inputs.** Account balance (B), risk percent (R, as a
   decimal), largest loss per contract (L) â€” this must be the system's
   actual worst historical losing trade, not the average loss and not the
   stop distance you *hope* holds.
2. **Apply the formula:**

   ```
   contracts = floor( (B Ã— R) / L )
   ```

   Floor, don't round up â€” round up quietly increases R.
3. **Run the blow-up check.** Consecutive max-losses to lose ~40-80% of
   the account at this R:

   ```
   n such that (1 - R)^n â‰ˆ 0.6 to 0.2   â†’   n = ln(0.2..0.6) / ln(1 - R)
   ```

   State it plainly: "N max-losses in a row costs you X% of the account."
   Two or three consecutive max losses is not a tail event â€” Williams notes
   losing streaks of 20 happen in real trading careers.
4. **Map risk% to personality tier if the user hasn't chosen one** (see
   sub-rule 2), then recompute step 2 with that R.
5. **Flag if R is outside the empirical sweet spot** (see sub-rule 4) â€”
   still give the number, but say so.

## Sub-rules / failure modes

1. **The denominator must be the LARGEST loss, not average loss, win rate,
   or win/loss ratio.** Williams' core insight: a 90%-accurate system can
   still go broke, because it's the one outsized losing trade â€” combined
   with position size having grown after a winning streak â€” that erases
   everything. Sizing off average loss or accuracy hides the exact risk
   that kills accounts. If the user gives you an average loss, ask for the
   largest loss instead (or explicitly flag that you're substituting
   average-loss as a weaker proxy).

2. **Risk-personality tiers** (percent of account balance to risk per
   trade, i.e., the R in the formula):

   | Tier | Risk % |
   |---|---|
   | Tommy Timid | 5% |
   | Normal Norma | 10-12% |
   | Leveraged Larry | 15-18% |
   | Swashbuckling Sam / Dangerous Danielle | 20%+ |

   These are Williams' own labels from the book. Higher tiers are not
   "more sophisticated" â€” they're a straightforward trade of faster
   compounding for a much fatter blow-up tail. Always pair a tier
   recommendation with its blow-up number from step 3.

3. **Do not substitute raw Kelly or Optimal F.** Both assume you're
   re-betting a *fixed-size* chip (like a poker hand) and compute the
   growth-optimal fraction of bankroll per bet. Trading breaks that
   assumption: position size (contracts) itself scales up with account
   equity as you win, so a "fixed fraction" formula compounds an
   already-growing bet size on top of its own fraction, and the
   contract-adding accelerates (Williams' own example: 5 months to add
   the 2nd contract, 16.5 days to add the 10th). One outsized loss then
   lands on the largest position you've ever carried. Kelly/Optimal F
   were flawed precursors in the book specifically because of this
   blow-up dynamic, not because the math is wrong â€” the math is right for
   chips, wrong for compounding position sizes. Recommend the largest-loss
   formula instead every time this comes up.

4. **Empirical sweet spot is roughly 14-21% risk.** Below that, drawdown
   grows slower than profit as R rises â€” worth pushing R up. Above ~21-25%,
   drawdown starts outpacing profit growth â€” each extra point of R buys
   less upside for a lot more downside. Above 25% Williams says you'll
   likely make more money but take a "sharp increase" in drawdown â€” flag
   this explicitly rather than silently sizing to whatever R the user names.

5. **Floor to a whole number, and re-check margin.** Fractional contracts
   don't exist; floor to be conservative. If the resulting size costs more
   margin than the account holds, that's a hard stop, not a sizing
   footnote â€” say so before returning a number.

## Worked mini-example

Inputs: account balance $50,000, risk% 12% (Normal Norma), largest loss
$2,000/contract.

```
contracts = floor( (50,000 Ã— 0.12) / 2,000 ) = floor(6,000 / 2,000) = 3
```

Blow-up check at 12%: `(1 - 0.12)^n = 0.4` â†’ `n = ln(0.4)/ln(0.88) â‰ˆ 7.2`
â†’ about 7 consecutive max-losses cuts the account 60%; 2 consecutive
max-losses alone cost `1-0.88^2 â‰ˆ 22.6%`.

Output to the trader:

> Trade **3 contracts**. At 12% risk, 2 max-losses in a row cost ~23% of
> the account; ~7 in a row would cost ~60%. That's within Williams'
> empirical sweet spot (14-21% is where drawdown starts outrunning profit
> growth â€” 12% is a notch below it, i.e. still on the conservative side).

If the user had instead said "I'm Swashbuckling Sam, use 25%": contracts =
floor(12,500/2,000) = 6; flag that 25%+ is explicitly past the sweet spot
per Williams â€” 2 max-losses in a row already costs 44% of the account.

## References

- Source: Larry Williams, *Long-Term Secrets to Short-Term Trading* (1999,
  Wiley), Chapter 13.
- Siblings in this skill family: `williams-volatility-breakout`,
  `williams-tdw-tdm-seasonality`, `williams-greatest-swing-value`,
  `williams-reversal-setups`, `williams-bailout-exit`.
