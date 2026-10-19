# System Design & Profitability Validation Method (Ch.10)

Use this after building any intermarket divergence system (see SKILL.md) to
decide whether it's genuinely tradable or an artifact of curve-fitting.

## 1. Validate out-of-sample, not just in-sample

- **Out-of-sample holdout**: optimize on one data segment, test unseen on a
  segment set aside. Minimum bar before trusting a system.
- **Walk-forward testing** (more rigorous): optimize on a window (e.g. 5
  years), test the next slice (e.g. 1 year), then roll the whole window
  forward by that slice and re-optimize. Repeat until data is exhausted;
  merge all out-of-sample slices into one combined result and judge the
  system on that. Walk-forward period is typically 12-20% of the
  optimization period.
- **Cluster spotting / profit mapping**: don't keep the single best-performing
  parameter set from an optimization grid. Plot profit as a 3D surface over
  the two parameters you're most sensitive to; prefer parameter sets sitting
  in a broad plateau of similar profitability over an isolated spike â€” spikes
  are much more likely to be curve-fit noise.
- **Monte Carlo on trade order**: reshuffle trade sequence randomly to get a
  more realistic drawdown estimate than the single historical sequence gives.
  Check trade-return autocorrelation first â€” Monte Carlo assumes independence.
- **Keep parameter count low.** More free parameters make it trivially easy to
  fit a system to noise; fewer, well-motivated parameters (ideally derived
  from real intermarket relationships, not fitted knobs) generalize better.
- **Diversify inputs across data sources.** An intermarket system already
  buys some robustness for free: unlike single-market indicators (all derived
  from the same price series and vulnerable to one bad print or gap), an
  intermarket system draws on â‰¥2 independent data sources.

## 2. The profitability metrics (Katsanos/Harris/Vince)

Compute these on the back-tested/out-of-sample trade log:

| # | Metric | Formula / definition | Good value |
|---|---|---|---|
| 1 | % profitable trades (P) | winners / total trades | context-dependent, says nothing about size |
| 2 | Profit factor (PF) | gross wins / gross losses | > 1 profitable |
| 3 | Avg profit / avg loss (Rwl) | avg winning trade / avg losing trade | higher is better |
| 6 | **Profitability Rating** (Harris, Ã—10 by Katsanos) | `10 * (P - 1/(1+Rwl))` | >2 tradable, >4 very good, negative = net loss; always a bit more conservative than PF |
| 10 | **Luck Coefficient** | `MAXW / AVGW` (largest win / average win) | lower = less luck-dependent |
| 11 | **Pessimistic Rate of Return (PRR)** | `[(W - sqrt(W))/N * AVGW] / [(L - sqrt(L))/N * ABS(AVGL)]` â€” penalizes winners and rewards losers by sqrt(count) to stress-test the edge | >2 good, >2.5 excellent |
| 12 | **Entry/Exit/Total Efficiency** | Entry: `(High - Entry)/(High-Low)` long (mirror for short). Exit: `(Exit - Low)/(High-Low)` long (mirror for short). Total: `Entry Eff + Exit Eff - 100`, or `(Exit-Entry)/(High-Low)` | entries/exits should each capture â‰¥55% of the high-low range; total efficiency should exceed 30% |
| 13 | **t-test vs. benchmark** | compare mean trade P/L (or system return) against zero or a buy-and-hold benchmark | see caveats below |

## 3. t-test caveats â€” check before trusting the p-value

- **Normality**: profit/loss distributions are often not normal, especially
  with a hard stop-loss (trades cluster at the max loss). Run a
  Kolmogorov-Smirnov or Shapiro-Wilk test; visually inspect. Minor violations
  can be tolerated for large samples (central limit theorem) or by trimming
  outliers.
- **Autocorrelation**: trade P/L must be roughly independent for the t-test
  to be valid. Check by correlating the P/L series against itself shifted by
  n bars. Autocorrelation above ~0.2-0.3 should make you discount the p-value.
- **Sample size**: need more than 30 trades for the statistic to mean
  anything. Fewer trades (a common problem with divergence systems, which can
  be sparse) â€” don't run a t-test at all; rely on efficiency/PRR/profitability
  instead, or add a volatility-breakout condition to raise trade count (see
  `forex-application.md` for a worked example of doing exactly this).

## 4. Practical checklist before calling a system "validated"

1. Out-of-sample or walk-forward tested, not just curve-fit in-sample.
2. Parameter surface checked for a plateau, not a spike.
3. Profitability Rating > 2, PRR > 2, efficiency > 30% total.
4. If running a t-test: normality, autocorrelation, and n>30 all checked and
   not badly violated.
5. Data quality checked (splits/dividends adjusted, no zero-filled gaps).
6. Paper-traded forward before committing real capital â€” market dynamics
   drift even after a system passes every backward-looking test.
