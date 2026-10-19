# Knaflic Explanatory Context

## When to Use

Use this skill when the user needs to turn analysis into an explanatory communication and has not yet pinned down the communication context.

Trigger when:
- A chart or deck shows data but the "so what" is unclear.
- The audience is vague, such as "stakeholders" or "leadership."
- The user needs a recommendation, decision, or action from a data communication.
- A live presentation, leave-behind deck, email, or report needs the right level of detail.
- A requester has asked for "a chart" but has not supplied the decision context.

Do not use this for choosing among bar, line, scatter, or other chart types in the abstract; use `data-visualization`. Do not use for dashboard KPI layout; use `build-dashboard` or `kpi-dashboard-design`. Do not use for truthfulness, data-ink, chartjunk, or graphical integrity; use the appropriate `tufte-*` skill. Do not use for visual encoding theory; use `bertin-*`.

## Framework

Knaflic's context pass converts exploratory analysis into explanatory communication.

1. Distinguish exploratory from explanatory.
   Exploratory analysis is the hunt for useful findings. Explanatory communication is the deliberate presentation of the one or two findings the audience needs.

2. Answer who.
   Name the specific audience or decision maker. Account for what they know, what they care about, what biases they bring, and how they perceive the communicator.

3. Answer what.
   State what the audience needs to know or do. If no action or decision can be articulated, revisit whether communication is needed.

4. Answer how.
   Identify the data that supports the point, including relevant opposing context. Choose the communication mechanism: live presentation, written document, email, or hybrid.

5. Set tone and evidence boundaries.
   Decide whether the communication should feel celebratory, urgent, clinical, exploratory, or serious. Include enough context to avoid a one-sided or misleading story.

## How to Apply

1. Write the audience as a named group or role, not a broad category.
2. Write the desired audience response as a verb: approve, decide, invest, change, remember, support, stop, start, or similar.
3. Identify the communication mechanism and adjust detail accordingly:
   - Live presentation: sparse visual support, presenter supplies narrative and answers.
   - Written report/email: more explicit labels, context, narrative, caveats, and next steps.
   - Hybrid slideument: separate what must appear on the page from what can be spoken.
4. List supporting evidence and counter-evidence.
5. If context came from a requester, interview them for missing background, decision maker, risks, success criteria, and the one-sentence message.

## Output Format

Return:
- **Audience:** specific decision maker or group.
- **Desired action:** what they should know, decide, or do.
- **Mechanism:** live, written, email, dashboard handoff, or hybrid, with detail implications.
- **Tone:** the intended emotional posture.
- **Evidence:** supporting data and opposing context to acknowledge.
- **Context gaps:** questions to ask before building visuals.
- **Draft context statement:** one concise paragraph that can guide the rest of the work.

## Common Failure Modes

- Starting in charting software before the audience and action are clear.
- Showing all exploratory work instead of the explanatory "pearls."
- Treating "leadership" or "all stakeholders" as a usable audience.
- Asking the audience to infer the action.
- Using the same dense slide for live presentation and circulated report.
- Hiding counter-evidence that a discerning audience will notice.
- Letting a dashboard request masquerade as a story request; dashboards need a KPI and monitoring design skill.

## References

- Cole Nussbaumer Knaflic, *Storytelling with Data: A Data Visualization Guide for Business Professionals* (Wiley, 2015), Chapter 1, "the importance of context."
- Sibling skills: `knaflic-big-idea`, `knaflic-storyboard`, `knaflic-deck-logic`, `knaflic-before-after-critique`.
