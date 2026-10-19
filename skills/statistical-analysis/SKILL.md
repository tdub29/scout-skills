---
name: statistical-analysis
description: "Hypothesis tests, outliers, correlation, distributions"
user-invocable: false
---

# Statistical Analysis Skill

Descriptive statistics, trend analysis, outlier detection, hypothesis testing, and guidance on when to be cautious about statistical claims.

## Descriptive Statistics Methodology

### Central Tendency

Choose the right measure of center based on the data:

| Situation | Use | Why |
|---|---|---|
| Symmetric distribution, no outliers | Mean | Most efficient estimator |
| Skewed distribution | Median | Robust to outliers |
| Categorical or ordinal data | Mode | Only option for non-numeric |
| Highly skewed with outliers (e.g., revenue per user) | Median + mean | Report both; the gap shows skew |

**Always report mean and median together for business metrics.** If they diverge significantly, the data is skewed and the mean alone is misleading.

### Spread and Variability

- **Standard deviation**: How far values typically fall from the mean. Use with normally distributed data.
- **Interquartile range (IQR)**: Distance from p25 to p75. Robust to outliers. Use with skewed data.
- **Coefficient of variation (CV)**: StdDev / Mean. Use to compare variability across metrics with different scales.
- **Range**: Max minus min. Sensitive to outliers but gives a quick sense of data extent.

### Percentiles for Business Context

Report key percentiles to tell a richer story than mean alone:

```
p1:   Bottom 1% (floor / minimum typical value)
p5:   Low end of normal range
p25:  First quartile
p50:  Median (typical user)
p75:  Third quartile
p90:  Top 10% / power users
p95:  High end of normal range
p99:  Top 1% / extreme users
```

**Example narrative**: "The median session duration is 4.2 minutes, but the top 10% of users spend over 22 minutes per session, pulling the mean up to 7.8 minutes."

### Describing Distributions

Characterize every numeric distribution you analyze:

- **Shape**: Normal, right-skewed, left-skewed, bimodal, uniform, heavy-tailed
- **Center**: Mean and median (and the gap between them)
- **Spread**: Standard deviation or IQR
- **Outliers**: How many and how extreme
- **Bounds**: Is there a natural floor (zero) or ceiling (100%)?

## Trend Analysis and Forecasting

Load `references/trend-and-forecasting.md` when identifying trends, seasonality, or simple forecasts.

## Outlier and Anomaly Detection

Load `references/outlier-detection.md` when flagging or handling outliers and time series anomalies.

## Hypothesis Testing Basics

### When to Use

Use hypothesis testing when you need to determine whether an observed difference is likely real or could be due to random chance. Common scenarios:

- A/B test results: Is variant B actually better than A?
- Before/after comparison: Did the product change actually move the metric?
- Segment comparison: Do enterprise customers really have higher retention?

### The Framework

1. **Null hypothesis (H0)**: There is no difference (the default assumption)
2. **Alternative hypothesis (H1)**: There is a difference
3. **Choose significance level (alpha)**: Typically 0.05 (5% chance of false positive)
4. **Compute test statistic and p-value**
5. **Interpret**: If p < alpha, reject H0 (evidence of a real difference)

### Common Tests

| Scenario | Test | When to Use |
|---|---|---|
| Compare two group means | t-test (independent) | Normal data, two groups |
| Compare two group proportions | z-test for proportions | Conversion rates, binary outcomes |
| Compare paired measurements | Paired t-test | Before/after on same entities |
| Compare 3+ group means | ANOVA | Multiple segments or variants |
| Non-normal data, two groups | Mann-Whitney U test | Skewed metrics, ordinal data |
| Association between categories | Chi-squared test | Two categorical variables |

### Practical Significance vs. Statistical Significance

**Statistical significance** means the difference is unlikely due to chance.

**Practical significance** means the difference is large enough to matter for business decisions.

A difference can be statistically significant but practically meaningless (common with large samples). Always report:
- **Effect size**: How big is the difference? (e.g., "Variant B improved conversion by 0.3 percentage points")
- **Confidence interval**: What's the range of plausible true effects?
- **Business impact**: What does this translate to in revenue, users, or other business terms?

### Sample Size Considerations

- Small samples produce unreliable results, even with significant p-values
- Rule of thumb for proportions: Need at least 30 events per group for basic reliability
- For detecting small effects (e.g., 1% conversion rate change), you may need thousands of observations per group
- If your sample is small, say so: "With only 200 observations per group, we have limited power to detect effects smaller than X%"

## When to Be Cautious About Statistical Claims

### Correlation Is Not Causation

When you find a correlation, explicitly consider:
- **Reverse causation**: Maybe B causes A, not A causes B
- **Confounding variables**: Maybe C causes both A and B
- **Coincidence**: With enough variables, spurious correlations are inevitable

**What you can say**: "Users who use feature X have 30% higher retention"
**What you cannot say without more evidence**: "Feature X causes 30% higher retention"

### Multiple Comparisons Problem

When you test many hypotheses, some will be "significant" by chance:
- Testing 20 metrics at p=0.05 means ~1 will be falsely significant
- If you looked at many segments before finding one that's different, note that
- Adjust for multiple comparisons with Bonferroni correction (divide alpha by number of tests) or report how many tests were run

### Simpson's Paradox

A trend in aggregated data can reverse when data is segmented:
- Always check whether the conclusion holds across key segments
- Example: Overall conversion goes up, but conversion goes down in every segment -- because the mix shifted toward a higher-converting segment

### Survivorship Bias

You can only analyze entities that "survived" to be in your dataset:
- Analyzing active users ignores those who churned
- Analyzing successful companies ignores those that failed
- Always ask: "Who is missing from this dataset, and would their inclusion change the conclusion?"

### Ecological Fallacy

Aggregate trends may not apply to individuals:
- "Countries with higher X have higher Y" does NOT mean "individuals with higher X have higher Y"
- Be careful about applying group-level findings to individual cases

### Anchoring on Specific Numbers

Be wary of false precision:
- "Churn will be 4.73% next quarter" implies more certainty than is warranted
- Prefer ranges: "We expect churn between 4-6% based on historical patterns"
- Round appropriately: "About 5%" is often more honest than "4.73%"

## References

- `references/trend-and-forecasting.md`: load for trend, seasonality, and simple forecasting methods
- `references/outlier-detection.md`: load for outlier methods, handling choices, and time series anomalies
