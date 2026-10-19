---
name: kohavi-controlled-experiments
description: Router hub for the RIGOROUS-STATISTICS layer of online controlled experimentation, from Kohavi, Tang & Xu's *Trustworthy Online Controlled Experiments*. Covers OEC and metric design, organizational guardrail metrics, statistical power / sample size / duration design, SQR (Speed-Quality-Risk) ramping, sample ratio mismatch (SRM) debugging, triggering and sensitivity, Twyman's Law trust skepticism, when NOT to run an experiment, and the launch/no-launch decision matrix. Triggers: OEC, overall evaluation criterion, guardrail metric, statistical power, MDE, minimum detectable effect, sample size, experiment duration, ramp/ramping, SRM, sample ratio mismatch, A/A test, triggered analysis, trigger rate, dilution, Twyman's Law, "too good to be true," "can we trust this result," "should we even A/B test this," network interference, carryover, launch decision, "ship or not," practical vs statistical significance. GUARDRAILS: this hub is the rigorous statistics/trustworthiness layer (trust checks, power, SRM, OEC, guardrails). For lighter-weight, hands-on practitioner test setup â€” writing a hypothesis, planning variants, basic significance â€” use the pre-existing `ab-testing` skills instead; this hub does NOT modify or replace them. Load the matching references/<name>.md file and apply that framework exactly.
---

# kohavi-controlled-experiments

This hub collapses the nine atomic Kohavi/Tang/Xu skills into one router plus references. Route by user cue, read the referenced file(s) in full, and apply that framework's process and output format exactly.

Book provenance: **Ron Kohavi, Diane Tang & Ya Xu, *Trustworthy Online Controlled Experiments* (Cambridge University Press, 2020)**. Load the matching `references/*.md` file when a specific framework is needed.

## When to use

Use this hub when the question is about **experiment trustworthiness and statistical rigor**, not just getting a test running: choosing an OEC, defining guardrail metrics, sizing for power and duration, designing a ramp, debugging an SRM, deciding whether to use triggered analysis, applying Twyman's Law skepticism to a surprising result, judging whether an experiment is even appropriate, or turning results into a launch decision.

## Guardrails

- This hub is the **rigorous-statistics / trustworthiness** layer â€” trust checks (SRM, Twyman's Law), power and duration, OEC and guardrail design, triggering, ramping, and launch decisions.
- For the **lighter-weight practitioner layer** â€” writing a hypothesis, planning variants, basic split-test setup and significance â€” use the pre-existing `ab-testing` skills. This hub does **not** modify or replace them; route there when the user just wants to stand up a test.
- Do **not** answer from router memory alone; load the selected reference file(s) first and follow their process and output format.
- Order matters for trust: before interpreting or shipping a surprising result, run SRM/Twyman trust checks first (`references/kohavi-srm-debug.md`, `references/kohavi-twymans-law.md`), then the launch decision (`references/kohavi-launch-decision-matrix.md`).

## Quick routing table

| User cue (examples) | Route to reference |
|---|---|
| OEC, overall evaluation criterion, success metric, "is revenue enough," proxy metric, gameable metric, align metrics to strategy, combine metrics | `references/kohavi-oec-metrics.md` |
| guardrail metric, must-not-degrade, latency/crashes/safety constraint, metric tradeoff, "is the win worth the cost" | `references/kohavi-organizational-guardrails.md` |
| power, sample size, MDE, duration, "run for a week," 80% power, underpowered, traffic split, day-of-week effect | `references/kohavi-power-duration-design.md` |
| ramp, ramping, 1%â†’5%â†’50%, auto-ramp, internal beta, rollback, blast radius, Speed-Quality-Risk, "how fast can we roll out" | `references/kohavi-sqr-ramping.md` |
| SRM, sample ratio mismatch, variant counts off, allocation imbalance, A/A failed, triggered SRM, "can we trust this experiment" | `references/kohavi-srm-debug.md` |
| triggered analysis, only users who saw the feature, conditional exposure, diluted impact, trigger rate, counterfactual, improve sensitivity | `references/kohavi-triggering.md` |
| "too good to be true," huge lift, breakthrough result, weird segment, unexpected drop, "can we trust this result," Twyman | `references/kohavi-twymans-law.md` |
| "should we A/B test this," can we experiment, not enough users, M&A, network effects, ethics risk, cannot randomize, complementary techniques | `references/kohavi-when-not-to-experiment.md` |
| ship or not, launch decision, "significant but small," practically significant, CI crosses zero, rerun with more power | `references/kohavi-launch-decision-matrix.md` |

## Workflow

1. Confirm the intent is about **statistical rigor / trust**, not basic test setup (`ab-testing`).
2. Pick the closest row(s) in the routing table. For results interpretation, do trust checks (SRM, Twyman) before the launch decision.
3. Read those `references/*.md` files completely.
4. Apply the framework's process, failure modes, and output format exactly.
5. Combine references only when the question genuinely spans them â€” e.g., OEC + guardrails for a metrics charter, or SRM + Twyman + launch decision for a contested result.

## Common failure modes (hub-level)

- **Wrong layer** â€” pulling this rigorous hub for a simple "help me set up a quick A/B test" that belongs to `ab-testing`.
- **Skipping trust checks** â€” interpreting or shipping a surprising result before running SRM and Twyman's Law.
- **Router-only answer** â€” summarizing the hub without loading the framework's full reference.
- **Treating significant as trustworthy** â€” p < 0.05 is not the same as a valid, well-powered, SRM-clean read.
- **Retired atomic names** â€” the nine per-framework skill folders were collapsed into this hub; use `references/` only.

## References

- [references/kohavi-launch-decision-matrix.md](references/kohavi-launch-decision-matrix.md)
- [references/kohavi-oec-metrics.md](references/kohavi-oec-metrics.md)
- [references/kohavi-organizational-guardrails.md](references/kohavi-organizational-guardrails.md)
- [references/kohavi-power-duration-design.md](references/kohavi-power-duration-design.md)
- [references/kohavi-sqr-ramping.md](references/kohavi-sqr-ramping.md)
- [references/kohavi-srm-debug.md](references/kohavi-srm-debug.md)
- [references/kohavi-triggering.md](references/kohavi-triggering.md)
- [references/kohavi-twymans-law.md](references/kohavi-twymans-law.md)
- [references/kohavi-when-not-to-experiment.md](references/kohavi-when-not-to-experiment.md)

- **Book:** Ron Kohavi, Diane Tang & Ya Xu, *Trustworthy Online Controlled Experiments* (Cambridge University Press, 2020)
