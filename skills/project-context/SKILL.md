---
name: project-context
description: Create and maintain personal project notes in the life KB, and retrieve current project state before planning or executing. Use when Trevor asks "what do we know about this project", "where did I leave off", "what's blocking X", asks to break a project into milestones or next actions, records a decision and its rationale, or when a session is about to act on a personal project and needs its current state rather than a stale summary.
version: 1.0.0
tags: [projects, decisions, milestones, context]
---

# Project context

Root: `C:\Users\TrevorWhite\Downloads\Big Projects\life`. Template: `system/templates/project.md`.

Scope: **personal** projects. Code projects in this workspace carry their own `CLAUDE.md` and are the authority on themselves â€” link to them, do not restate them here.

## Retrieve before planning

1. `node scripts/find.mjs "<project keywords>"` then open `kb/projects/prj-<slug>.md`.
2. **Check for newer dated records before trusting the summary.** `kb/events/<year>/` sorted by date, and the project's own decision links. A summary written three weeks ago is a hypothesis about today.
3. `GET /api/data` for live status, milestone counts, blockers, and the next action.
4. Report current state, then the one next executable action. Not a status essay.

## Capture

Per project, keep:

- Purpose and desired outcome
- Status, phase, and the single next executable action
- Owner, collaborators, who it is for
- Scope and **non-goals** (the list that stops scope creep)
- Operating model â€” architecture, stack, or how the work runs
- Milestones, workstreams, tasks, dependencies
- Decisions with rationale, each in its own `dec-` note
- Constraints, risks, metrics, deadlines, review triggers
- Links: repos, docs, `src-` source records

**Keep facts, assumptions, forecasts, decisions, and experiments in separate sections.** A forecast that migrates into the facts list is how a project starts lying to itself. Every time-sensitive metric carries `as_of` and a source.

## Decisions

One `dec-` note per real decision: what was chosen, what was rejected, why, what would reverse it. Link it from the project. The rationale outlives the decision, and it is the thing you will actually want in six months.

## Progress

Completed milestones Ã· total. No milestones means **no percentage** â€” say "no milestones defined" rather than inventing one from elapsed time or task counts. Blockers are named with what they are waiting on, and who owns the unblock.

## Archiving

A completed project keeps its decisions and history and stays retrievable. Archive tasks, never decisions. Set `status: completed` or `archived`; do not delete the note or drop its index line.

## Rules

- One writable copy per fact. If a code project's `CLAUDE.md` owns it, link, do not copy.
- Next action must be executable today, or it is a blocker with a name.
- `index.md` line in the same write as the note.
- No secrets, ever â€” not in links, not in notes, not "temporarily".

## Verify

`node scripts/validate-kb.mjs` clean, and `find.mjs` returns the project note top for its own name.
