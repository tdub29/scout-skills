# Kohavi/Tang/Xu: When Not to Experiment

## When to Use

Use before committing to an A/B test when the premise may be wrong. Trigger on "should we A/B test this," "can we experiment," "not enough users," "M&A," "network effects," "ethics risk," "carryover," "long-term effect," "cannot randomize," "use survey instead," or "complementary techniques."

## Framework

Online controlled experiments are powerful when necessary ingredients exist: reliable randomization, enough units, measurable key metrics, reliable telemetry, and changeability. When those ingredients fail, an A/B test may be impossible or misleading.

Do not experiment, or do not rely on an experiment alone, when:

- Counterfactual cannot exist concurrently, such as M&A or one-time strategic moves.
- Traffic or effect size makes useful power infeasible.
- Metrics cannot be observed in the decision window.
- Randomization or exposure cannot be controlled reliably.
- Users in variants interfere with each other.
- Carryover, learning, cookie, or residual effects contaminate future reads.
- Ethical risk, data sensitivity, deception, or lack of consent exceeds the organization's threshold.
- The idea is too expensive to build before cheaper learning methods prune it.

## How to Apply

1. Test the necessary ingredients: randomization, sample size, metrics, telemetry, and changeability.
2. Check contamination: interference, leakage, carryover, novelty/primacy, long-term effects, or network spillovers.
3. Check ethics: respect, beneficence, justice, data sensitivity, consent expectations, and escalation path.
4. Estimate expected value of information: will the experiment reduce enough uncertainty to justify cost and risk?
5. Choose the right method:
   - Run A/B test now.
   - Run A/B test after instrumentation or design fixes.
   - Use complementary techniques first: UX research, survey, logs-based analysis, human evaluation, painted door, or quasi-experiment.
   - Do not experiment; make a judgment call or governance decision.

## Output Format

Return:

- Experimentability verdict: run, fix first, complement first, or do not experiment.
- Ingredient checklist: randomization, units, metrics, telemetry, changeability.
- Risk checklist: interference, carryover, long-term effects, ethics, data sensitivity.
- Alternative method: recommended non-A/B or pre-A/B technique.
- Decision note: what uncertainty remains and who owns it.

## Common Failure Modes

- Treating every product question as an A/B nail because the platform exists.
- Building an expensive treatment before cheaper complementary research.
- Running underpowered tests that create false confidence.
- Ignoring network interference or variant leakage.
- Running ethically sensitive experiments with no review or escalation path.
- Using short-term metrics for effects that are mostly long-term.

## References

- Ron Kohavi, Diane Tang, Ya Xu, *Trustworthy Online Controlled Experiments* (Cambridge University Press, 2020), Chapters 1, 9, 10, 22, and 23.
- Related: `ab-testing`, `references/kohavi-power-duration-design.md`, `references/kohavi-triggering.md`, `references/kohavi-twymans-law.md`.
