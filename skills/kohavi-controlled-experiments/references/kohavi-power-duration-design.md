# Kohavi/Tang/Xu: Power and Duration Design

## When to Use

Use before or during experiment design when the question is "how much traffic and time do we need?" Trigger on "power," "sample size," "MDE," "minimum detectable effect," "duration," "run for a week," "80% power," "underpowered," "traffic split," or "day-of-week effect."

## Framework

Power is the probability of detecting a meaningful difference when one exists. Good design starts with a practical significance boundary, a baseline metric distribution, and realistic traffic. Duration is not only sample size; it also covers weekly cycles, ramping, novelty/primacy, and shared traffic constraints.

Design levers:

- Effect size that matters: smaller effects require more units.
- Metric variance: noisier metrics require more units.
- Significance threshold: stricter p-value thresholds require more units.
- Allocation: equal splits are common, but many treatments may justify larger Control.
- Target population: analyzing affected users can increase sensitivity.
- Calendar time: run long enough for day-of-week and behavior cycles.

## How to Apply

1. Define the OEC and practical significance boundary before estimating sample size.
2. Estimate baseline mean, variance, traffic arrival rate, and eligible population.
3. Choose desired power, commonly 80-90%, and significance threshold.
4. Decide randomization unit, target population, and variant allocation.
5. Translate required sample into calendar duration, accounting for traffic sharing and ramp.
6. Add minimum calendar constraints: full week when day-of-week matters; longer if novelty, primacy, delayed effects, or repeated behavior matter.
7. If already run, classify whether inconclusive results are truly neutral or underpowered.

## Output Format

Return:

- Design inputs: metric, baseline, variance, MDE/practical boundary, alpha, power, units.
- Traffic plan: allocation, eligible population, expected sample per day, duration.
- Calendar constraints: day-of-week, novelty/primacy, ramp, and delayed effect concerns.
- Risk notes: underpowering, overpowering, segment power, and shared traffic.
- Recommendation: run length, split, and whether triggering or better metrics could improve sensitivity.

## Common Failure Modes

- Picking duration by habit instead of MDE and traffic.
- Treating non-significant as no effect when the interval is wide.
- Ignoring day-of-week effects by stopping after a few high-traffic days.
- Forgetting that segment reads need their own power.
- Choosing tiny exposure for safety, then forgetting the final experiment still needs enough total units.
- Letting ramp tactics change the designed final sample size.

## References

- Ron Kohavi, Diane Tang, Ya Xu, *Trustworthy Online Controlled Experiments* (Cambridge University Press, 2020), Chapters 2, 17, and 18.
- Related: `references/kohavi-oec-metrics.md`, `references/kohavi-triggering.md`, `references/kohavi-launch-decision-matrix.md`, `references/kohavi-sqr-ramping.md`.
