# Model Ladder

Climb only with walk-forward evidence on the primary metric.

1. **Constant / mean** â€” floor.
2. **Single domain factor** â€” home, rest, or rating diff.
3. **Regularized linear / logistic on clean features** â€” often production winner on medium sports tabular problems.
4. **Tree ensembles (HistGBM, XGBoost, LightGBM)** â€” when nonlinear interactions are real and validated across folds.
5. **Specialized architectures** â€” tracking/sequence/graph models only with enough data and clear failure of rungs 3â€“4.

## Promotion rule

A higher rung must improve primary metric on multiple time folds, not one lucky season.

## Demotion rule

If a simpler rung matches the complex model within noise, keep the simpler model.
