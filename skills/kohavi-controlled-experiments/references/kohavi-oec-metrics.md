# Kohavi/Tang/Xu: OEC Metrics

## When to Use

Use when the decision is what the experiment should optimize. Trigger on "OEC," "overall evaluation criterion," "success metric," "what metric should this experiment use," "is revenue enough," "proxy metric," "metric is gameable," "align metrics to strategy," or "combine metrics."

Do not use for generic A/B planning (`ab-testing`), post-result ship decisions (`references/kohavi-launch-decision-matrix.md`), or trust guardrail failures (`references/kohavi-srm-debug.md`).

## Framework

An OEC is the quantitative measure of the experiment's objective. It must be measurable during the experiment, sensitive enough to move, and believed to causally drive long-term strategic objectives.

Evaluate candidate metrics on:

- Strategic alignment: Does improving this metric plausibly advance the product or business strategy?
- Short-term measurability: Can it move in the normal experiment window?
- Sensitivity: Can realistic traffic detect meaningful changes?
- Directionality: Is higher or lower clearly better?
- Non-gameability: Would optimizing it create obvious perverse incentives?
- Coverage: Does it cover the affected user population without excluding important harm?
- Tradeoff encoding: Should multiple metrics be combined, weighted, or separated into OEC plus guardrails?

## How to Apply

1. State the product strategy and the behavior the experiment is meant to improve.
2. List candidate metrics and reject raw totals when denominators differ; prefer normalized per-unit metrics.
3. Separate goal metrics from organizational guardrails: the OEC says what to improve, guardrails say what must not degrade.
4. Check each metric for latency, sensitivity, and whether short-term movement predicts long-term value.
5. Look for Goodhart/Campbell failure: how would a team improve this metric while making the product worse?
6. Choose one OEC when possible. If multiple metrics matter, define an explicit weighted OEC or a primary metric plus decision guardrails.
7. Write the launch interpretation before the experiment starts: what deltas on the OEC and guardrails imply ship, iterate, or reject.

## Output Format

Return:

- OEC recommendation: the chosen metric or weighted combination.
- Metric scorecard: alignment, measurability, sensitivity, gameability, denominator, and owner.
- Guardrail split: which metrics are not part of the OEC but must be protected.
- Decision rule: how metric outcomes map to ship, iterate, or stop.
- Open validation: evidence needed to prove the proxy predicts long-term goals.

## Common Failure Modes

- Optimizing raw revenue, clicks, or sessions without user normalization.
- Choosing profit or lifetime value when it cannot move or be measured in the experiment window.
- Using a metric that teams can game by degrading user experience.
- Hiding a must-not-degrade metric inside a weak weighted OEC instead of making it a guardrail.
- Treating a proxy as valid because it is convenient, not because it predicts long-term value.
- Letting each team define local metrics that conflict with the shared strategy.

## References

- Ron Kohavi, Diane Tang, Ya Xu, *Trustworthy Online Controlled Experiments* (Cambridge University Press, 2020), Chapters 1, 6, and 7.
- Related: `references/kohavi-organizational-guardrails.md`, `references/kohavi-launch-decision-matrix.md`, `references/kohavi-power-duration-design.md`, `ab-testing`.
