---
name: goal-planning
description: Turn a broad ambition into an outcome, a definition of done, success criteria, milestones, supporting habits, and a concrete next action, then write it into the life KB and tracker together. Use when Trevor says he wants to get better at something, states a goal in vague terms, asks to break a goal down, asks what to do today to move a goal, asks to restructure or reprioritize goals, or when a goal has stalled and needs re-scoping.
version: 1.0.0
tags: [goals, planning, milestones, habits]
---

# Goal planning

Root: `C:\Users\TrevorWhite\Downloads\Big Projects\life`. Template: `system/templates/goal.md`.

## The hierarchy

```
life area
â””â”€â”€ goal
    â”œâ”€â”€ definition of done
    â”œâ”€â”€ success criteria (few, measurable)
    â”œâ”€â”€ milestones
    â”‚   â””â”€â”€ projects / workstreams
    â”‚       â””â”€â”€ next actions
    â””â”€â”€ supporting habits
```

A goal may need only a checklist. Another needs three projects and two habits. Fit the structure to the goal; do not inflate it to fill the template.

## Procedure

1. **Outcome first.** One sentence: what is different when this is done. If it cannot be said in one sentence, it is a theme, not a goal â€” say so and pick the goal inside it.
2. **Definition of done.** If two people could disagree about whether it happened, it is not specific enough yet.
3. **Baseline.** Where it stands today, with today's date. No baseline means no progress, only activity.
4. **Constraints.** Time, money, dependency on another person, anything that makes the plan fiction.
5. **Success criteria.** Few and measurable. These are what progress is computed from.
6. **Next milestone only.** One. Planning milestone six is procrastination wearing a plan's clothes.
7. **Supporting habits** â€” the recurring behavior that feeds it. Create them in the tracker, linked by goal id.
8. **One next action** that could be done today. If none exists, name the blocker instead of inventing a task.
9. **Review cadence** and `next_review` date.
10. **Adjustment trigger** â€” the condition that means change the plan rather than push harder.

## Write it once, in both places

- Canonical note: `kb/goals/goal-<slug>.md` from the template, plus its `index.md` line.
- Tracker: `POST /api/entity { type: 'goal' }` with criteria, milestones, `next_action`, `next_review`, and any `hab-` ids.

The note holds the reasoning. The tracker holds the state. Do not duplicate the reasoning into the tracker or the state into the note.

## Rules

- Progress = met criteria Ã· total, or completed milestones Ã· total. **Never elapsed time, never task count.** A goal with neither has no percentage, and saying so is the honest answer.
- No fake precision. Some goals are binary. Some are milestone-based. Some only get a qualitative review.
- Status is one of `not_started | active | blocked | paused | completed | abandoned`, and pausing or abandoning **requires a written reason**. That reason is often the most useful thing in the file a year later.
- Preserve Trevor's priorities. Do not add goals he did not ask for, and do not reorder his.
- Outcome progress and activity volume are different numbers. Never report the second as the first.
- Cap active goals. If a new one arrives and the list is already long, ask which one pauses.

## Verify

`node scripts/validate-kb.mjs` clean, the goal is the top `find.mjs` hit for its own keywords, and `GET /api/data` shows it with a real `basis` (not `none`) if it has criteria.
