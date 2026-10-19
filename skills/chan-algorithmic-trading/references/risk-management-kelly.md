# Risk Management and Kelly Sizing (Chan Ch 8)

The goal is **maximization of long-term equity growth**, not avoiding the feeling of loss.
(Humans need ~$2 upside per $1 downside, which is why a Sharpe of 2 feels good, but loss
aversion itself is not rational.) The core lever is the prudent use of leverage: optimize it
with Kelly or numerical growth-rate maximization, then, if a drawdown cap is required, add CPPI
or a stop loss.

## The constant-leverage requirement (and why it causes contagion)

Every leverage-optimization scheme requires keeping leverage CONSTANT, which is counterintuitive
and means **selling into losses**. Example: $100k equity at leverage 5 = $500k portfolio. Lose
$10k -> equity $90k, portfolio $490k, so you must sell a further $40k to get back to 5 x $90k =
$450k. Gain $20k next day -> target 5 x $110k = $550k, so buy $80k more.

This "sell into losses" is why constant-leverage risk management is contagious in crises: many
funds hold similar positions, one fund's forced liquidation depresses prices, hurting others
who then must liquidate too (the August 2007 quant meltdown; a tragedy of the commons where
each fund's self-preservation harms all).

## The Kelly formula

Under a Gaussian returns assumption, optimal leverage:

    f = m / s^2

where m = mean excess return, s^2 = variance of excess returns. This f maximizes compounded
growth rate if all profits are reinvested. Growth rate at optimal f: `g = f^2 * s^2 / 2` (=
FT C F / 2 in the multi-strategy case).

**Multiple strategies / portfolios**: allocate leverage vector

    F = C^-1 M

C = covariance matrix of portfolio returns, M = mean excess returns. If the broker caps gross
leverage at Fmax < sum|Fi|, the usual scale-everything-by-Fmax/sum|Fi| is NOT growth-optimal.
When Fmax is much smaller than the Kelly total, it is often optimal to put most/all buying
power into the single strategy with the highest mean excess return (Example 8.2: two strategies
with Kelly leverages 4.4 and 4.9; capped at Fmax=2, concentrating gives g 0.96 vs 0.82 for the
naive split).

## Treat Kelly as an upper bound, deploy half-Kelly

Even if returns are truly Gaussian, you estimate m and s^2 with error, and the future may
differ from the past. **Overestimating m or underestimating s^2 overestimates leverage, and
enough of that means eventual ruin** (equity to zero). Underestimating leverage only costs
submaximal growth. So:
- Use **half-Kelly** as the practical deployment.
- Full Kelly is often above the broker's max anyway, or would have hit -100% drawdown in
  backtest due to non-Gaussian tails.
- Kelly as a sanity check: Russell 1000/2000 have Kelly ~1.8, yet 3x ETFs (BGU, TNA) exist by
  design at leverage 3, so their NAV can go to zero; no one should buy-and-hold them.

## Fat tails: optimize growth rate by Monte Carlo

When returns are fat-tailed, do not trust the Gaussian Kelly. Maximize

    g(f) = < log(1 + f*R) >

over simulated per-bar returns R. Fit the empirical mean, std, skew, kurtosis to a **Pearson
system** (7 analytic distributions; MATLAB `pearsrnd`), draw ~100,000 samples, and numerically
find the f that maximizes g (or minimizes -g via `fminbnd`). For Chan's Example 5.1 strategy:
Gaussian Kelly f = 18.4, Monte-Carlo optimum f = 19 (close), but f = 31 gives growth rate -1
(ruin), because the worst simulated per-bar return -0.0331 means any leverage above 1/0.0331 =
30.2 wipes out. Optimizing on the single historical return path also works but suffers
data-snooping bias (too little data); a leverage between the Monte-Carlo and historical answers
is a reasonable compromise.

## Capping maximum drawdown

Scaling leverage down by (allowed DD / backtest DD) does NOT work. Chan's example: unconstrained
optimal f = 19.2 gives max DD -0.999; half of f still gives -0.963; you must cut f by ~7x (to
~2.7) to reach -0.5 DD on simulated returns (or ~1.5x on historical returns). Setting leverage
at this bound only caps the SIMULATED drawdown, not the future. To truly guarantee the cap, use
CPPI or a stop loss.

## Constant Proportion Portfolio Insurance (CPPI)

Maximize growth AND cap drawdown at -D: put only D of total equity in the trading subaccount at
Kelly leverage f, keep 1-D in cash. You then cannot lose more than -D of the total account.
Reset the subaccount to D of equity only at new high-water marks; never add cash on losses.
When the subaccount is exhausted you have hit -D and gracefully wind the strategy down (a
principled exit, not an emotional one).

CPPI is NOT the same as running the whole account at leverage f*D: on any drawdown, CPPI cuts
order size much faster, so it is nearly impossible to approach -D. Growth rate is essentially
the same as f*D (0.002484 vs 0.002525/day in one sim with D=0.5) but drawdown is capped at 0.5
vs 0.9. Apply CPPI to a SINGLE-strategy account only (in a multi-strategy account winners
subsidize losers so the drawdown never trips the shutdown). CPPI, like stop loss, cannot stop
an overnight-gap loss; out-of-the-money options can hedge expected downtime.

## Stop loss: logical for momentum, dangerous for mean reversion

Two uses: (a) exit a losing position, free to re-enter later; (b) shut the strategy at a
drawdown threshold (awkward one-time event; CPPI is preferred for this).

Stop loss only works if the market is open the whole time you hold (gaps blow through the stop;
the 2010 flash crash executed an Accenture stop at $0.01 on stub quotes).

- **Momentum**: stop loss is natural and logical. A losing momentum position means momentum
  reversed, so exiting (or reversing) is correct; the continuously updated signal IS a de facto
  stop. This is why momentum has bounded downside.
- **Mean reversion**: a stop CONTRADICTS the entry (price dropped -> you bought expecting a
  rise -> stopping out at the low is wrong). Chan never found a stop that raised a
  mean-reverting strategy's Sharpe... BUT that is survivorship bias: it only holds while the
  series keeps reverting. A mean-reverting series can regime-change into a trending one
  (possibly permanently), and then a stop prevents catastrophe. **Resolution: set the
  mean-reversion stop BEYOND the backtest max intraday drawdown**, so it never fired in the
  backtest (cannot have hurt reported performance) yet still guards against a future black swan
  / regime change.

## Leading risk indicators (avoid risky periods proactively)

No single indicator fits all strategies (a risky period for one is profitable for another).
Test whether an indicator LEADS (predicts next period) vs merely coincides, and beware
data-snooping (crises are rare).
- **VIX**: buy-on-gap actually does BETTER when prior VIX > 35 (17.2% vs 8.7%); but FSTX
  opening gap does WORSE (2.6% vs 13%). Same indicator, opposite meaning by strategy.
- **TED spread** (3m LIBOR - 3m T-bill): bank-default risk; hit a record 457 bps in 2008.
  Credit-market players are better informed than retail-driven equity indicators; use its
  relative level over time.
- **HYG** (high-yield bonds), **MXN** (emerging-market proxy for risk-on/off), **ONN/OFF**
  (risk-on / risk-off baskets).
- **Order flow**: a sudden large negative order flow in a risky asset (or positive in a safe
  one like Treasuries, USD, JPY, CHF) is the earliest, highest-frequency risk signal.
- Strategy-specific: oil price leads GLD-GDX pair risk; Baltic Dry Index leads
  export-country ETFs/currencies.

## Summary decision

1. Goal = max long-term net worth? Size at HALF-Kelly.
2. Fat-tailed returns? Monte-Carlo (Pearson) growth-rate optimization, not Gaussian Kelly.
3. Hard drawdown cap? CPPI (single-strategy account).
4. Stop loss: natural for momentum; for mean reversion set it beyond the backtest max drawdown.
5. Consider a leading risk indicator, tested for genuine lead and guarded against
   data-snooping.
