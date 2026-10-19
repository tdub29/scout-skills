# Kohavi/Tang/Xu: SRM Debugging

## When to Use

Use when allocation or invariant checks say the experiment population is not what the design promised. Trigger on "SRM," "sample ratio mismatch," "variant counts off," "allocation imbalance," "trust guardrail failed," "A/A failed," "triggered SRM," or "can we trust this experiment?"

## Framework

An SRM occurs when the observed ratio of randomization units across variants is unlikely under the configured split. SRM is not a small cosmetic issue; even small imbalances can reverse treatment effects when missing users differ systematically.

Common causes:

- Redirect or performance differences.
- Logging/beacon placement or event loss.
- Treatment changes who is observed or triggered.
- Carryover from stopped/restarted experiments.
- Bad randomization hash or bucketing.
- Time-of-day or batch-send differences.
- Bot, crawler, cache, cookie, browser, or platform artifacts.

## How to Apply

1. Confirm the configured allocation, randomization unit, and eligible population.
2. Compute observed counts and SRM p-value for the overall experiment and key triggered analyses.
3. If SRM exists, stop interpreting treatment effects until root cause is found.
4. Localize the imbalance by segment: browser, platform, country, traffic source, time, logged-in state, bot status, app version, and ramp phase.
5. Trace missing or extra units through assignment, exposure, logging, filtering, joining, and analysis.
6. Check whether treatment can affect eligibility, triggering, event capture, or loss rate.
7. Decide whether to fix and rerun, salvage a clean segment, or invalidate the experiment.

## Output Format

Return:

- SRM status: expected split, observed split, p-value, and severity.
- Localization table: segments with the strongest imbalance.
- Root-cause hypotheses: ranked, with evidence to collect.
- Validity decision: interpret, interpret only clean segment, rerun, or invalidate.
- Prevention: instrumentation/platform fixes and future guardrail checks.

## Common Failure Modes

- Saying "0.992 vs 1.0 is close enough" without accounting for huge sample sizes.
- Debugging metrics before debugging allocation.
- Ignoring SRM in triggered analysis when overall allocation looks fine.
- Filtering users after assignment in ways that treatment can affect.
- Restarting experiments without clearing carryover state.
- Treating SRM as a statistics problem when it is often instrumentation or product behavior.

## References

- Ron Kohavi, Diane Tang, Ya Xu, *Trustworthy Online Controlled Experiments* (Cambridge University Press, 2020), Chapters 3, 20, and 21.
- Related: `references/kohavi-twymans-law.md`, `references/kohavi-triggering.md`, `references/kohavi-organizational-guardrails.md`.
