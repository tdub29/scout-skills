# Kohavi/Tang/Xu: Twyman's Law

## When to Use

Use when a number is anomalous enough that excitement or panic may outrun skepticism. Trigger on "too good to be true," "huge lift," "breakthrough result," "weird segment," "unexpected drop," "can we trust this result," "interesting metric," or "Twyman."

## Framework

Twyman's Law: any figure that looks interesting or different is usually wrong. In online experiments, surprising results often come from instrumentation bugs, assignment problems, logging differences, denominator shifts, bot traffic, segment bugs, carryover, triggering mistakes, or underpowered reads.

The posture is not "ignore surprising wins." It is "earn the right to believe them."

## How to Apply

1. State the surprising figure and why it is surprising: size, direction, segment, timing, or business implication.
2. Pause interpretation until trust checks pass.
3. Run the basic validity stack:
   - SRM or allocation sanity.
   - Invariant and trust guardrail metrics.
   - Logging and instrumentation changes.
   - Segment splits by browser, platform, country, traffic source, time, bot/user class.
   - Carryover, cookie, cache, or exposure effects.
   - Power and confidence interval width.
4. Look for a mechanical explanation before a product explanation.
5. If checks pass, decide whether the result should replicate, ramp cautiously, or launch.

## Output Format

Return:

- Anomaly summary: what is surprising and how large it is.
- Trust checklist: pass/fail/unknown for SRM, invariants, instrumentation, segments, carryover, and power.
- Most likely explanations: ranked mechanical/product hypotheses.
- Recommended action: debug, rerun, segment, replicate, ramp, launch, or stop.

## Common Failure Modes

- Celebrating a breakthrough before checking assignment and logging.
- Treating "statistically significant" as "trustworthy."
- Ignoring small imbalances because the percentage difference looks tiny.
- Explaining a segment effect with user psychology before checking browser/platform bugs.
- Suppressing anomalies that could reveal real product opportunities after trust checks pass.

## References

- Ron Kohavi, Diane Tang, Ya Xu, *Trustworthy Online Controlled Experiments* (Cambridge University Press, 2020), Chapter 3.
- Related: `references/kohavi-srm-debug.md`, `references/kohavi-triggering.md`, `references/kohavi-launch-decision-matrix.md`, `references/kohavi-power-duration-design.md`.
