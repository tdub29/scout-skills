---
name: dual-momentum-investing
description: Builds and evaluates a systematic momentum allocation using Gary Antonacci's Global Equities Momentum (GEM), combining absolute (trend) momentum against T-bills with relative (cross-sectional) momentum between US and non-US equities on a monthly rebalance. Use when the user mentions dual momentum, absolute momentum, relative momentum, GEM, Global Equities Momentum, time-series momentum, cross-sectional momentum, trend filter, monthly rebalance, momentum anomaly, drawdown reduction, look-back period, tactical asset allocation, or trend-following equity/bond switching.
---

# Dual Momentum Investing (GEM)

Operating skill for building or auditing a rules-based momentum allocation from Gary Antonacci's *Dual Momentum Investing* (2015). The distinct contribution is GEM: pairing two momentum signals so each covers the other's blind spot. Absolute momentum answers "should I be in the market at all?" (trend). Relative momentum answers "which market is strongest right now?" (selection). Neither alone is enough. Together they nearly doubled the world equity index return over 1974 to 2013 while cutting max drawdown by roughly two thirds.

Use this to design an allocation, generate this month's signal, or grade a proposed momentum model for faithfulness and overfitting risk. It does not compute Sharpe or drawdown for you (see `risk-metrics-calculation`), draw charts (see `technical-analysis`), or reason about the value factor (see `us-value-investing`). It owns the allocation logic.

## The two momentum types

- **Absolute (time-series / trend) momentum.** An asset's own return over the look-back window versus the risk-free rate (T-bills). Positive excess return means uptrend, stay invested. Negative means downtrend, step aside to safety. This is the drawdown killer. It sidestepped both 2000 to 2002 and 2007 to 2008. Applied to the S&P 500 alone (1974 to 2013) it added over 200 bps of annual return, dropped standard deviation by over 3%, and pulled max drawdown from above 50% to under 30%. It stays dormant in bull markets, acting like a stop loss that also knows how to re-enter.
- **Relative (cross-sectional) momentum.** Rank two or more assets against each other and hold the strongest. This is the return booster: relative strength on the world index added 556 bps of annual return versus buy-and-hold, but with slightly higher volatility and only a modest drawdown cut. It adds value exactly when absolute momentum is dormant (long bull runs).

Why both: their monthly returns correlate only 0.69, and US vs non-US equity correlation flips from -0.17 in bull markets to 0.76 in bear markets. Relative momentum cannot protect you when everything falls together, absolute momentum can. That complementarity is the whole thesis.

## The GEM method, step by step

Three assets only: a US equity index (S&P 500), an all-world-ex-US equity index (ACWI ex-US), and US aggregate bonds (Barclays US Aggregate, ~78% AAA, average maturity under five years, the safe harbor). Signal generation each month:

1. **Look-back window: trailing 12 months of total return** (dividends reinvested, not price only). This is GEM's single parameter. 6 to 12 months works across markets; 12 minimizes turnover and transaction cost. In charting terms, 252 trading days.
2. **Relative step.** Compare S&P 500 vs ACWI ex-US over the trailing 12 months. Select whichever performed better.
3. **Absolute step (the trend filter).** Check whether the selected index beat US Treasury bills over the same 12 months. If yes, invest fully in that equity index for the coming month. If no, invest 100% in US aggregate bonds instead.
4. **Rebalance monthly.** Recompute at each month-end and switch only if the signal changed. Hold otherwise.

Equivalent one-look formulation (from the book's implementation notes): plot the trailing-12-month total return of three proxies, US stocks, non-US stocks, and T-bills. If either equity has the highest return, hold that equity. If T-bills have the highest return, the equity trend is negative, so hold the aggregate bond fund. This three-way comparison collapses steps 2 and 3 into one ranking.

The allocation is always 100% in a single sleeve, never blended. Over 1974 to 2013 GEM sat in the S&P 500 41% of the time, ACWI ex-US 29%, and aggregate bonds 30%, averaging only 1.35 switches per year, so trading cost is negligible.

**Implementation nuance for an agent building the code.** The book's canonical flow (Chapter 8, Figure 8.4) is relative-first then filter the *selected* index against T-bills, which is what the three-way ranking above encodes. Antonacci later described a variant that gates on the *S&P 500* excess return before doing the relative pick, since the US leads world equity markets (Rapach, Strauss, Zhou 2013). They agree most of the time. State which gate you used when you report a signal, and do not silently mix them across months.

### Do not skip a month here

With individual stocks, practitioners skip the most recent month to avoid the short-term reversal effect contaminating intermediate momentum. GEM uses broad indexes, which are far less noisy and have no meaningful short-term reversal at the index level, so use the full trailing 12 months with no skip.

## Why it beats either signal alone

- Absolute momentum alone gives the risk reduction (lower volatility, far lower drawdown, higher Sharpe) but leaves return on the table in long bull markets.
- Relative momentum alone gives the higher raw return but rides the full bear-market drawdown down.
- GEM captures both: 17.43% annualized, 12.64% standard deviation, 0.87 Sharpe, and 22.7% max drawdown over 1974 to 2013, versus a roughly 9% return and ~60%+ drawdown for the passive world index. The Sharpe roughly quadrupled. Most of the outperformance is earned in bear markets by *not* having to recoup deep losses, so compounding is the real engine.

Robustness the book leans on: GEM beat the world index on Sharpe and max drawdown in each of the four decades tested, and for every look-back from 3 to 12 months. Simplicity is deliberate: one parameter validated in and out of sample across two centuries of data resists the overfitting that kills complex models.

## The academic evidence to cite

- Momentum is the "premier anomaly." Even Fama and French, founders of the efficient market hypothesis, conceded momentum is powerful, persistent, and unexplained by their known risk factors.
- Origin: Jegadeesh and Titman, "Returns to Buying Winners and Selling Losers." Relative strength documented back to 1801, absolute momentum's risk-adjusted profits back to 1903. No other market backtest rests on this much data.
- Behavioral driver: underreaction. Prices drift because analysts and investors adjust slowly to new information (Chan, Jegadeesh, Lakonishok), plus slow-moving arbitrage capital and investor inattention. This is *why* the trend persists rather than being arbitraged away.
- GEM's alpha survives Fama-French-Carhart four-factor and bond-augmented five-factor regressions, with a significant loading on the stock momentum factor, so the edge is not just repackaged market or bond beta.

## Practical pitfalls and how to handle them

1. **Whipsaw.** Trend following gives false signals in choppy, mean-reverting regimes and re-enters late after sharp V-shaped rebounds. GEM lagged the index badly in early 1975, late 2002, and early 2009 (violent bear-market snapbacks), and in the early 1980s when T-bills yielded ~20% and simply out-earned equities. Set expectations: GEM often underperforms in strong bull runs and just after bottoms. The payoff shows up over full cycles, not month to month. A longer look-back near 12 months and index-level (not daily) signals already suppress most whipsaw.
2. **Look-back sensitivity.** The choice of window is the one knob, so do not tune it to a backtest. All of 3 to 12 months beat the benchmark historically, which is evidence *against* fragility, but treat 12 as the default because it is the most cross-validated and lowest-turnover, not because it topped one sample.
3. **Overfitting and data snooping.** Adding assets, filters, or shorter windows to juice a backtest is the trap the book warns against hardest: test 20 configurations at the 5% level and one looks "significant" by luck. Better backtests often mean worse live results (Lopez de Prado). Fifteen years of data is not enough; regimes are nonergodic. Penalize complexity, prefer the parsimonious rule.
4. **Total return, not price.** Signals must use total return (reinvested dividends). Price-only charts distort the ranking, especially for high-yield sleeves. The book flags most free charting tools as price-only.
5. **Tax and cost reality.** GEM is naturally tax-friendly (it sells losers short-term, rides winners into long-term gains) and cheap to run with commission-free index ETFs at ~10 bps blended expense. But equity-to-bond switches in a taxable account still realize gains; prefer a tax-advantaged account or account for the drag.

## Extensions (name them, do not rebuild unasked)

- **Global Balanced Momentum (GBM):** 70% GEM equities plus a 30% fixed-income sleeve that itself rotates by dual momentum across long Treasuries, global government, high yield, and T-bills. Roughly double the Sharpe and half the drawdown of a static 60/40.
- **Dual Momentum Sector Rotation (DMSR):** relative momentum picks the strongest of 11 US equity sectors; absolute momentum moves the whole basket to aggregate bonds when the US market trend turns down.

## When applying this skill

- Building an allocation: default to plain GEM (three assets, 12-month total-return look-back, monthly rebalance) unless the user explicitly wants GBM or DMSR. Resist adding assets.
- Generating a signal: report the trailing-12-month total return of S&P 500, ACWI ex-US, and T-bills; state the winner; name the resulting hold; and disclose which absolute-momentum gate convention you used.
- Auditing someone's momentum model: flag price-only signals, a tuned or sub-3-month look-back, blended (non-100%) sleeves, a skipped month on indexes, and any backtest under ~15 years or with many tested variants.
- Hand Sharpe / drawdown / standard deviation computation to `risk-metrics-calculation`, moving-average and trend mechanics to `technical-analysis`, and value-factor questions to `us-value-investing`. Cross-reference, do not duplicate.
