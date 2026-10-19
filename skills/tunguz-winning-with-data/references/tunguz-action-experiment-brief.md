
# Tunguz: Action Experiment Brief

## When to use

Trigger when a team has a debated idea and wants to run a practical data-backed test: pricing tweak, sales script, onboarding change, email timing, feature smoke test, workflow change, or operational experiment. Cues: "how do we test this," "data-backed experiment," "turn this opinion into a test," or "quick experiment brief."

## The framework

Tunguz emphasizes experiments as a cultural muscle: converting opinion into hypotheses that can surprise the organization and change operations. This skill produces a lightweight brief. It does not replace rigorous online controlled experiment design when statistical validity is the central risk.

### Brief components

1. **Decision first.** The experiment exists to decide keep, stop, change, or scale.

2. **Hypothesis and counter-hypothesis.** State what you believe and what would prove you wrong.

3. **Primary metric and guardrails.** Choose a metric tied to the decision plus constraints that must not degrade.

4. **Bounds and exposure.** Define who is included, how long it runs, and how much traffic/customer exposure is acceptable.

5. **Action rule.** Before launch, define what result leads to ship, iterate, rerun, or kill.

## How to apply

1. **Translate the opinion.** Convert "we should do X" into a falsifiable hypothesis.

2. **Define the decision.** What action will be taken if the result is positive, negative, or ambiguous?

3. **Pick metrics.** Primary metric, guardrails, segments, and qualitative signals if needed.

4. **Set practical bounds.** Audience, exposure, duration estimate, operational risk, and owner.

5. **Return the brief.** Include hypothesis, design, metrics, decision thresholds, analysis owner, and review meeting date.

6. **Escalate when needed.** If the test affects many users, money, safety, or product launch decisions, hand off to `kohavi-power-duration-design`, `kohavi-oec-metrics`, or `kohavi-launch-decision-matrix`.

## Common failure modes

- **Running tests with no action rule.** If nobody knows what result will change the decision, the experiment becomes trivia.

- **Testing opinions too vaguely.** "Improve onboarding" is not a hypothesis; "shortening step 2 increases completion without raising support tickets" is.

- **Ignoring guardrails.** A test that improves clicks while harming retention, trust, latency, or revenue may be a bad trade.

- **Overclaiming from weak designs.** Lightweight tests can guide operations but may not prove causality strongly. Say what confidence is warranted.

- **Waiting for perfect statistics on low-risk choices.** Some operational experiments are valuable because they are fast and reversible.

## References

- Tomasz Tunguz and Frank Bien, *Winning with Data*, chapter 9.
- Sibling skills: `tunguz-data-decision-meeting`, `tunguz-data-culture-maturity`.
- Related rigorous experiment skills: `kohavi-oec-metrics`, `kohavi-power-duration-design`, `kohavi-launch-decision-matrix`, `ab-testing`.
