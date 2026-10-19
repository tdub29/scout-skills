# Kohavi/Tang/Xu: Triggering

## When to Use

Use when only some assigned users could experience a treatment difference. Trigger on "triggered analysis," "only users who saw the feature," "conditional exposure," "affected population," "diluted impact," "trigger rate," "counterfactual triggering," or "improve sensitivity."

## Framework

Triggering includes users in analysis only when there is potentially some difference between the variant they received and a counterfactual variant. This can greatly improve power by removing unaffected users, but it must preserve trust and report overall impact.

Key distinctions:

- Optimal triggering: include exactly users who could differ between actual and counterfactual variants.
- Conservative triggering: include extra users; valid but less sensitive.
- Overall treatment effect: dilute triggered-population effects to the full population when making business decisions.
- Trustworthy triggering: check SRM in triggered analysis and verify never-triggered users behave like an A/A test.

## How to Apply

1. Define the triggering event: the moment a user could have experienced a difference.
2. Confirm triggering is not affected by treatment in a way that biases inclusion.
3. Decide whether counterfactual logging is available; if not, choose a conservative trigger.
4. Analyze the triggered population for sensitivity.
5. Report overall impact, not only triggered lift. Convert triggered-population gains into site-wide/user-base impact.
6. Run trust checks: triggered SRM and complement analysis for never-triggered users.
7. State limitations for ratio metrics, skewed triggered populations, shared controls, and client-side logging.

## Output Format

Return:

- Trigger definition: event, unit, timing, and whether it is optimal or conservative.
- Analysis plan: triggered metric read plus diluted overall impact.
- Trust checks: triggered SRM and never-triggered complement status.
- Instrumentation needs: runtime logging, counterfactuals, or client-side assignment tracking.
- Decision caveats: what cannot be generalized from the triggered read.

## Common Failure Modes

- Reporting a 5% triggered lift when only 0.1% of users triggered, without dilution.
- Triggering on behavior that treatment itself changes.
- Fetching assignment for many experiments and treating fetch as exposure.
- Ignoring SRM that appears only inside the triggered population.
- Assuming direct trigger-rate dilution works for skewed ratio metrics.
- Using triggering to hide that the product impact is negligible overall.

## References

- Ron Kohavi, Diane Tang, Ya Xu, *Trustworthy Online Controlled Experiments* (Cambridge University Press, 2020), Chapter 20.
- Related: `references/kohavi-power-duration-design.md`, `references/kohavi-srm-debug.md`, `references/kohavi-launch-decision-matrix.md`.
