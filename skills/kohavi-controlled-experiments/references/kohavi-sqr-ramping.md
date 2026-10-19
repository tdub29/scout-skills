# Kohavi/Tang/Xu: SQR Ramping

## When to Use

Use when a treatment may ship or expand but exposure must be controlled. Trigger on "ramp," "ramping," "increase exposure," "1% to 5% to 50%," "auto-ramp," "internal beta," "rollback," "blast radius," "launch risk," or "how fast can we roll this out?"

## Framework

SQR ramping balances three forces:

- Speed: learn and deliver value quickly.
- Quality: protect users by catching defects and metric regressions.
- Risk: limit blast radius when uncertainty is high.

Ramping is not a substitute for a powered final read. It is a release and learning tactic layered around experiment design and launch decisions.

## How to Apply

1. Classify risk: user harm, revenue impact, technical complexity, reversibility, novelty, and dependency surface.
2. Define ramp phases: internal/beta, small external exposure, broader exposure, final ramp, post-final monitoring.
3. Assign entry and exit criteria for each phase: trust checks, organizational guardrails, OEC movement, error budgets, latency, support tickets, and segment health.
4. Decide speed: skip or compress phases only when risk is low, reversibility is high, and monitoring is strong.
5. Define stop/rollback rules before increasing exposure.
6. Preserve analysis correctness across phases; segment by ramp period when needed to avoid aggregate distortions.

## Output Format

Return:

- Risk profile: low/medium/high with rationale.
- Ramp schedule: phases, exposure levels, duration, and owners.
- Entry/exit criteria: checks needed to advance, hold, or roll back.
- Monitoring: metrics, alert thresholds, segments, and post-final watch period.
- Analysis caveats: ramp-period segmentation, SRM checks, and Simpson's paradox risks.

## Common Failure Modes

- Treating ramping as proof of impact instead of safety-controlled exposure.
- Moving from tiny exposure to broad launch before trust and guardrails stabilize.
- Combining ramp phases without segmenting when traffic mix changes.
- Spending too long in early ramp phases for low-risk work, slowing learning.
- Skipping internal beta or small external ramp for high-risk work.
- Not defining rollback criteria until after an alert fires.

## References

- Ron Kohavi, Diane Tang, Ya Xu, *Trustworthy Online Controlled Experiments* (Cambridge University Press, 2020), Chapter 15.
- Related: `references/kohavi-launch-decision-matrix.md`, `references/kohavi-organizational-guardrails.md`, `references/kohavi-srm-debug.md`, `references/kohavi-power-duration-design.md`.
