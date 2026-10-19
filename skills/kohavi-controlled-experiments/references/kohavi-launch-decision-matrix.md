# Kohavi/Tang/Xu: Launch Decision Matrix

## When to Use

Use after results are available and the user needs a decision. Trigger on "ship or not," "launch decision," "statistically significant but small," "practically significant," "confidence interval crosses zero," "rerun with more power," or "what should we do with this A/B result?"

## Framework

Launch decisions combine measurement evidence with business judgment. Statistical significance asks whether the effect is likely noise. Practical significance asks whether the effect is big enough to matter. Confidence intervals show the plausible range of true effects.

Decision regions:

- Clearly negative: do not launch, unless external constraints dominate.
- Statistically significant and practically meaningful positive: launch or ramp, after trust and guardrail checks.
- Statistically significant but not practically meaningful: usually do not launch for metric impact; consider cost/risk/context.
- Practically meaningful estimate but not statistically significant: rerun or add power unless a decision must be made under uncertainty.
- Wide interval spanning meaningful positive and negative effects: underpowered; no strong launch decision.
- Neutral with narrow interval inside practical bounds: safe to treat as no meaningful effect.

## How to Apply

1. Confirm trust checks passed: SRM, instrumentation, invariants, and relevant segments.
2. State the OEC delta, confidence interval, p-value, and practical significance boundary.
3. Classify the result into one of the decision regions above.
4. Check organizational guardrails and severe segment harms.
5. Consider implementation cost, maintenance cost, risk, strategic value, and reversibility.
6. Recommend launch, no-launch, rerun with more power, iterate, or ramp cautiously.

## Output Format

Return:

- Result classification: statistical/practical significance region.
- Evidence table: OEC, CI, p-value, practical threshold, guardrails, key segments.
- Decision: launch, no-launch, rerun, iterate, or ramp.
- Rationale: why this decision follows from evidence and business context.
- Next step: ramp plan, follow-up experiment, or debug requirement.

## Common Failure Modes

- Launching because p < 0.05 even though the effect is too small to matter.
- Calling no effect when the experiment is underpowered and the interval is wide.
- Ignoring guardrails after the OEC wins.
- Treating every non-significant positive as "ship anyway."
- Making the launch decision before checking SRM and Twyman-style anomalies.

## References

- Ron Kohavi, Diane Tang, Ya Xu, *Trustworthy Online Controlled Experiments* (Cambridge University Press, 2020), Chapter 2.
- Related: `references/kohavi-oec-metrics.md`, `references/kohavi-organizational-guardrails.md`, `references/kohavi-power-duration-design.md`, `references/kohavi-sqr-ramping.md`, `references/kohavi-srm-debug.md`.
