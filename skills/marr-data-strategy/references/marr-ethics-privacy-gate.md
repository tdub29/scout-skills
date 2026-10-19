
# Marr: Ethics and Privacy Gate

## When to Use

Use before approving a data/AI use case that collects, processes, predicts, recommends, automates, or monetizes data in ways that could affect people, law, trust, or reputation.

## Do Not Use For

Legal advice or full enterprise governance design. This is a strategic gate with escalation.

## Framework

Marr's gate checks purpose legitimacy, minimization, consent, quality, bias, representativeness, transparency, explainability, security, accountability, and the ethics of underusing available data when non-use creates harm.

## How to Apply

1. State the use case and affected parties.
2. Identify personal, sensitive, employee, child, health, financial, location, or behavioral data.
3. Check whether each data element is necessary.
4. Confirm consent, permission, supplier rights, and jurisdictional obligations.
5. Score quality and bias risks against the intended decision.
6. Determine whether the decision must be explainable or contestable.
7. Specify security controls and access boundaries.
8. Decide green, yellow, red, or stop.

## Output Format

- Gate decision: green/yellow/red.
- Use case and affected parties.
- Risk table for privacy, consent, quality, bias, security, transparency, accountability.
- Minimization changes.
- Required mitigations and owners.
- Escalation path and review cadence.

## Common Failure Modes

- Treating anonymization as foolproof.
- Collecting more personal data than needed.
- Checking legal compliance while ignoring trust, bias, or explainability.
- Confusing quality with representativeness.
- Buying third-party data without verifying original permissions.
- Leaving accountability vague after launch.

## References

- Bernard Marr, Data Strategy, Second Edition, Chapter 11.
- Related carved skills: `marr-data-use-case-template`, `marr-data-strategy-canvas`, `marr-data-needs-inventory`, `marr-data-monetization-scan`, `marr-ethics-privacy-gate`, `marr-strategy-execution-risk-audit`.
