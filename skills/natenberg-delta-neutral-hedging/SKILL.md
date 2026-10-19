---
name: natenberg-delta-neutral-hedging
description: Capture a theoretical edge by hedging delta neutral and re-adjusting on a cadence, treating the position as a long series of small bets rather than one bet. Covers why adjustments mechanically force buy-low/sell-high, the four-component P&L decomposition (original hedge, adjustments, option carrying costs, variation costs) that reconciles realized profit to model-predicted edge, and the frictionless-market assumptions that fail in practice. Use when asked "how do I actually make money from an underpriced option," "what is delta neutral," "how often should I re-hedge," "why did my delta-neutral position lose money," "how do I check whether the model's predicted edge was realized," or "what does a delta of 57 mean." From Sheldon Natenberg, Option Volatility and Pricing, Chapter 5.
---

# Natenberg Delta-Neutral Hedging

## What this decides

How to convert "this option is theoretically underpriced" into realized profit,
and how to audit afterward whether the edge the model promised actually showed up.

## Delta, and the convention

Delta is the hedge ratio: the fraction of an underlying contract needed to offset
one option. **An underlying contract always has a delta of 1.00.**

Traders drop the decimal, so a call's delta runs **0 to 100** and the underlying
is **100**. (The convention comes from US stock options, where a contract was
100 shares and one delta was equated with one share.)

Worked setup: a 100 call with delta **57**. Buy 100 calls, sell 57 futures (whole
contracts, keeping the neutral ratio).

```
Buy  100 June 100 calls   contract delta  57   delta position  +5700
Sell  57 June futures     contract delta 100   delta position  -5700
                                              total            0
```

Purchases are positive, sales negative; the delta position of each side is
contracts Ã— contract delta. Total zero means **delta neutral**: within a small
range the position has no preference for up or down. **Positive total delta is an
upward bias; negative is a downward bias.**

Delta is the only greek this procedure needs. For gamma, theta, vega and rho,
and for reading a position's full risk profile, see
[[natenberg-greeks-risk-profile]].

## Why one hedge is not enough

A theoretical value is a probability statement. The roulette player who buys a
bet below its theoretical value only expects a profit **over many plays**. On
any single spin he most likely loses, because there is one way to win and 37 to
lose. A single hedge is one spin.

The fix: **treat the initial hedge as a continuing series of small bets.**
Reassess at regular intervals and adjust the position back to neutral, so each
interval is a fresh bet at the same favorable odds. More bets, closer convergence
to the model's predicted profit.

## Adjustments force buy-low / sell-high, mechanically

This is the part worth internalizing. When re-hedging to neutral:

- The underlying **rises** â†’ the option's delta rises â†’ total delta position goes
  **positive** â†’ you must **sell** the underlying.
- The underlying **falls** â†’ delta falls â†’ total delta goes **negative** â†’ you
  must **buy**.

> Because our adjustments depended on the delta position, we were forced to do
> what every trader wants to do: buy low and sell high.

The discipline is structural, not predictive. It requires no view.

## The four P&L components

The worked example (ten weekly adjustments, futures 101.35 at entry, 18.3%
volatility, 8% rates) decomposes to:

| Component | Value |
|---|---|
| Original hedge | **-138.83** |
| Adjustments | **+205.27** |
| Option carrying costs | **-4.99** |
| Variation costs (interest on futures variation) | **+1.36** |
| **Total** | **+62.81** |

Predicted edge: bought 100 calls worth 3.88 for 3.25, so 100 Ã— 0.63 = **+63.00**.
The model came very close to predicting the actual profit.

**Carrying costs.** Futures use futures-type settlement and need no initial cash;
the options use stock-type settlement and require full payment. 100 calls at 3.25
is 325.00 outlay; at 8% for 10 weeks the carry is
0.08 Ã— 70/365 Ã— 325.00 = **4.99**, a debit.

**Variation costs.** Futures cash-settle daily, crediting or debiting the account,
which earns or costs interest. Sell 57 at 101.35, price rises to 102.26 â†’ account
debited 57 Ã— (101.35 - 102.26) = -51.87; financing that for 9 weeks at 8% costs
-0.72. Next week the price falls to 99.07 on 62 contracts â†’ credited +197.78,
earning +2.43 over 8 weeks. Net interest over the run: **+1.36**.

**Which components are profitable is not predictable.** Here adjustments and
variation made money while the original hedge and carrying costs lost. It is just
as easy to construct the reverse. The point stands regardless:

> If a trader's inputs are correct, in some combination he can expect to show a
> profit (or loss) approximately equal to that predicted by the theoretical
> pricing model.

That is also the audit: reconcile realized P&L against predicted edge **by
component**. A large gap points at whichever input was wrong.

## Where the volatility input came from

Of all the inputs, **volatility is the only one not directly observable.** In the
example the 18.3% was not a guess: it is the annualized standard deviation of the
logarithmic price changes actually observed over the ten weeks. So it was, by
construction, the correct volatility for that price series, which is why the
model tracked the outcome so well, and exactly what will not be true in advance.

Note also that the Black model assumes interest rate and volatility stay
**constant over the option's life**; the worked example holds both fixed at every
re-hedge.

## The frictionless-market assumptions, and how they break

The example assumes a frictionless market, which underpins Black-Scholes:

1. Traders can freely buy or sell the underlying without restriction.
2. All traders borrow and lend at the same rate.
3. Transaction costs are zero.
4. There are no tax considerations.

Every one is violated in the real world:

- **(1)** Some futures markets have daily price limits. At the limit the market
  is **locked** and no trading occurs until it comes off, so the underlying
  cannot always be bought or sold, precisely when you most need to adjust.
- **(2)** Individuals cannot borrow or lend at institutional rates. There is a
  spread, possibly a large one, between a trader's borrowing and lending rate.
  Mitigating factor: the interest-rate input is usually the **least important**
  input, so this generally causes only small changes to total P&L.
- **(3) and (4)** Transaction costs and taxes are real and scale with the number
  of adjustments, which is the direct tension with "more bets is better."

That tension is the practical design decision: **adjustment frequency trades
convergence-to-theoretical-value against transaction costs.**

## Checklist

```
[ ] Delta position per leg = contracts x contract delta (buys +, sells -)
[ ] Total delta ~ 0 at entry; know your intended bias if not
[ ] Adjustment cadence chosen deliberately (convergence vs transaction costs)
[ ] Re-hedge mechanically to neutral; do not override with a directional view
[ ] Track all FOUR P&L components separately, not just net
[ ] Reconcile realized P&L vs predicted edge; a large gap means an input was wrong
[ ] Note which frictionless assumptions your market actually violates (limits,
    borrow/lend spread, costs, tax)
```

## Related

- [[natenberg-greeks-risk-profile]] for the risks the delta hedge leaves open,
  since neutral today is not neutral after the next move.
- [[natenberg-theoretical-edge]] for where the predicted edge you are
  reconciling against comes from, and how much of it is real.
- [[natenberg-spread-adjustments]] when the adjustment decision is a choice of
  instrument, not just a quantity of underlying.
- [[natenberg-break-even-volatility]] for the realized volatility the hedging
  program has to see before the adjustments pay for themselves.
- [[natenberg-theoretical-edge/references/natenberg-option-pricing-reference.md]]
  for the model inputs and pricing mechanics behind the worked numbers.
