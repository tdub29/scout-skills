# Knaflic Before-After Critique

## When to Use

Use this skill when the user has an existing analytical visual, slide, report page, or deck and wants to improve it.

Trigger when:
- The user asks for a makeover of a chart or slide.
- A visual needs a before/after critique grounded in audience action.
- The chart is technically correct but not communicating.
- A deck needs practical edits across context, display, clutter, attention, design, and story.
- The user wants a step-by-step transformation plan rather than a theory discussion.

Do not use this for generic chart selection without a concrete communication; use `data-visualization`. Do not use for dashboards; use `build-dashboard` or `kpi-dashboard-design`. Do not use for formal Tufte data-ink, lie-factor, chartjunk, or graphical-integrity audits; use `tufte-*`. Do not use for Bertin encoding theory; use `bertin-*`.

## Framework

Knaflic's before-and-after process applies the full storytelling-with-data sequence to a concrete artifact.

1. Understand the context.
   Identify who, what, how, tone, and Big Idea before changing the visual.

2. Choose an appropriate display.
   Confirm whether the current form supports the audience's task. If chart-type choice is the main question, hand off to `data-visualization`.

3. Eliminate clutter.
   Remove, mute, or redesign elements that do not increase understanding.

4. Draw attention.
   Use preattentive attributes to make the intended point visually obvious.

5. Think like a designer.
   Apply affordances, accessibility, alignment, white space, and aesthetics so the audience knows how to read the artifact.

6. Tell a story.
   Add narrative, action titles, annotations, sequence, and a clear call to action.

## How to Apply

1. Describe the current artifact and its likely current message.
2. Reconstruct the intended audience, decision, and Big Idea.
3. Audit the artifact in six passes:
   - context fit,
   - display fit,
   - clutter,
   - attention hierarchy,
   - design/accessibility,
   - story and action.
4. Separate fixes into:
   - must fix for comprehension,
   - should fix for persuasion,
   - optional polish.
5. Produce a revised artifact spec:
   - title,
   - chart or layout,
   - labels and annotations,
   - color and hierarchy,
   - narrative sequence,
   - appendix/backups.
6. If the user supplied an image, cite the visible issue in plain language and avoid inventing unseen data.

## Output Format

Return:
- **Current read:** what the artifact appears to say now.
- **Intended story:** audience, Big Idea, and action.
- **Six-pass critique:** context, display, clutter, attention, design, story.
- **Before-after plan:** ordered edits from rough artifact to improved version.
- **Revised title/narrative:** action title and supporting annotation text.
- **What to remove:** clutter or unsupported claims.
- **What to add:** context, labels, emphasis, caveats, or call to action.
- **Verification:** how to test with a fresh viewer.

## Common Failure Modes

- Beautifying a chart before deciding what it should communicate.
- Over-focusing on chart type when the real issue is audience, action, or narrative.
- Removing necessary context in the name of simplicity.
- Highlighting a point that the data does not support.
- Making a live-presentation slide too dense or a leave-behind too sparse.
- Applying Tufte or Bertin theory when the user asked for a practical business makeover.
- Treating a recurring dashboard as a before/after story; dashboards need ongoing monitoring design.

## References

- Cole Nussbaumer Knaflic, *Storytelling with Data: A Data Visualization Guide for Business Professionals* (Wiley, 2015), Chapters 8-9, "pulling it all together" and "case studies."
- Sibling skills: `knaflic-explanatory-context`, `knaflic-big-idea`, `knaflic-declutter`, `knaflic-preattentive-hierarchy`, `knaflic-deck-logic`.
