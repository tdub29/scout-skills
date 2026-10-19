# Kohavi/Tang/Xu: Organizational Guardrails

## When to Use

Use when the experiment has a primary goal but the organization must protect other outcomes. Trigger on "guardrail metric," "must not degrade," "latency guardrail," "crashes," "safety," "do no harm," "metric tradeoff," or "how do we decide if the win is worth the cost?"

Do not use for sample ratio mismatch or assignment sanity checks; use `references/kohavi-srm-debug.md` for trust-related guardrails.

## Framework

Organizational guardrails identify what the organization is unwilling to trade away. They are different from the OEC: the OEC captures what you are optimizing; guardrails set boundaries on acceptable harm.

Good guardrails are:

- User- or business-critical: degradation matters even if the OEC improves.
- Sensitive enough to catch harm during ramp or experiment windows.
- Directionally clear: worse means worse.
- Actionable: a failed guardrail changes the launch, ramp, or rollback decision.
- Owned: someone can explain and defend the threshold.

## How to Apply

1. Name the OEC and the intended win.
2. List harms that would make the win unacceptable: latency, crashes, churn, abuse, revenue, satisfaction, compliance, safety, trust, support load.
3. Pick guardrail metrics with thresholds, not vague "monitor this" language.
4. Split guardrails by severity:
   - Stop-ship: unacceptable degradation.
   - Investigate: possible harm that needs segmentation or follow-up.
   - Monitor: track during ramp but not decision-blocking yet.
5. Define tradeoffs before results arrive. If the OEC is positive and one guardrail is negative, decide what evidence is enough to ship, iterate, or stop.
6. Carry guardrails into ramping and post-launch monitoring.

## Output Format

Return:

- Guardrail set: metric, owner, threshold, severity, and rationale.
- OEC relationship: whether each guardrail is outside the OEC or a heavily weighted component.
- Decision policy: ship, no-ship, iterate, rollback, or ramp-hold rules.
- Monitoring plan: what to watch during ramp and after final launch.

## Common Failure Modes

- Calling every secondary metric a guardrail until no decision is possible.
- Using guardrails with no pre-agreed threshold.
- Letting a positive OEC override user trust, crashes, or latency without explicit tradeoff.
- Mixing trust guardrails such as SRM with organizational guardrails; SRM invalidates the read, while organizational guardrails constrain the decision.
- Defining guardrails only after seeing an inconvenient result.

## References

- Ron Kohavi, Diane Tang, Ya Xu, *Trustworthy Online Controlled Experiments* (Cambridge University Press, 2020), Chapters 1, 2, 6, and 21.
- Related: `references/kohavi-oec-metrics.md`, `references/kohavi-srm-debug.md`, `references/kohavi-launch-decision-matrix.md`, `references/kohavi-sqr-ramping.md`.
