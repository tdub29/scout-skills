# Knaflic Storyboard

## When to Use

Use this skill when a data communication needs a planned flow before building slides or visuals.

Trigger when:
- The user is about to create a deck from analysis.
- A presentation has too many disconnected findings.
- A stakeholder wants to approve the structure before production work.
- The user is attached to existing slides that may need to be rearranged or cut.
- The communication needs to coordinate a Big Idea, evidence, visuals, and call to action.

Do not use this for selecting graph types; use `data-visualization`. Do not use for dashboard layout; use `build-dashboard` or `kpi-dashboard-design`. Do not use for Tufte-style chart honesty, chartjunk, or data-ink audits; use `tufte-*`. Do not use for Bertin retinal-variable theory; use `bertin-*`.

## Framework

Knaflic's storyboard is a visual outline of the communication.

1. Start low tech.
   Use a whiteboard, paper, or Post-it notes instead of presentation software.

2. One idea per card.
   Each card represents a slide, section, visual, or transition.

3. Arrange for audience flow.
   Move, add, or remove cards until the order supports the Big Idea and audience action.

4. Get early acceptance.
   When appropriate, review the storyboard with the requester or stakeholder before spending time polishing content.

5. Resist slide-generation mode.
   Presentation software encourages production before thinking; paper keeps edits cheap.

## How to Apply

1. Load the context and Big Idea.
2. Write the planned message, evidence, visual, and action for each card.
3. Arrange cards in the likely audience order:
   - context,
   - tension/problem,
   - evidence,
   - implication,
   - recommendation,
   - action.
4. Try at least two alternate flows:
   - chronological process,
   - lead-with-ending,
   - problem-solution,
   - executive-summary-first.
5. Remove cards that do not support the Big Idea.
6. Mark cards that need a visual, narration, appendix backup, or stakeholder approval.

## Output Format

Return:
- **Storyboard premise:** audience, Big Idea, and desired action.
- **Card sequence:** numbered list with title, purpose, evidence, and format.
- **Flow rationale:** why this order fits the audience.
- **Cuts:** cards or topics to remove or move to appendix.
- **Open questions:** missing evidence or stakeholder decisions.
- **Approval prompt:** concise wording to confirm the structure with the requester.

## Common Failure Modes

- Opening PowerPoint or Slides before the structure is clear.
- Treating the storyboard as a final deck instead of a cheap planning artifact.
- Keeping cards because the analysis was hard, not because the audience needs them.
- Mixing several audience journeys into one deck.
- Failing to revisit the order after the Big Idea changes.
- Using a storyboard for a monitoring dashboard; dashboards need KPI architecture, not narrative sequencing.

## References

- Cole Nussbaumer Knaflic, *Storytelling with Data: A Data Visualization Guide for Business Professionals* (Wiley, 2015), Chapter 1, "Storyboarding."
- Sibling skills: `knaflic-explanatory-context`, `knaflic-big-idea`, `knaflic-deck-logic`, `knaflic-before-after-critique`.
