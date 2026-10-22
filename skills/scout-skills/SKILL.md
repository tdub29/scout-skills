---
name: scout-skills
description: Find and read local skill guidance for a task, report coverage and gaps, and route bounded decisions to optional Jev support.
---

# Scout Skills

Find what installed skills teach before choosing an approach. Return cited guidance for each
sub-question, keeping every contributor. This bundle is self-contained; no slash command or
user-specific workspace is required.

## 1. Set extent and locate the library

The first token sets extent: `mid` (default) covers direct guidance; `high` also covers applicable
analogies; `max` also closes uncovered questions by finding or building skills. The remaining
text is the task. If empty, use the current task.

Locate the Scout Skills checkout from the user's setup. Run its ranker by absolute path from
the owning project root. The ranker searches its checkout and home Claude tree, not the current
project. Also search the actual project's configured skill directories. If the ranker is absent,
search those directories directly and report that limitation. Never guess an installation path.

## 2. Search descriptions AND bodies

Split the task into sub-questions first. Search two or three phrasings:

```sh
python /absolute/path/to/scout-skills/scripts/find-local-skill.py "task in plain words" --top 12
```

This command uses deterministic local code, needs no key, and makes no network calls.
Names and descriptions produce leads, not a coverage verdict. Context listings may omit
descriptions; use files on disk. Search concrete nouns and synonyms across bodies and references:

```sh
rg -n -i --glob '*.md' 'footer|colophon|contact section' /absolute/path/to/skills
```

Read matching sections and linked references. Extract concrete rules, defaults and anti-patterns
with `path:line` citations. Search beyond the initial top results when a sub-question lacks coverage.
A zero-result description search does not prove a skill is missing.

## 3. Keep contributors and verify discovery

Read overlapping candidates. Choose at most one lead workflow, and retain every other skill with
useful guidance. Report conflicting rules rather than silently discarding one. There is no quota
on contributors. A rank is a lexical match, not proof of quality or truth.

The ranker's `invocable` flag recognizes only its checkout's and home Claude skill trees. It does
not inspect an active session, Codex, Cursor, or a different project's discovery state. Verify
discovery with the actual agent's supported mechanism. If installing, copy the whole selected
bundle, preserve notices and existing local changes, and follow that agent's current setup docs.

## 4. Route work by phase

Keep file reads, retrieval, arithmetic, exact matches, validation and orchestration in code.
Keep research, generation, explanations and open-ended reasoning with the agent.
When optional Jev is configured and external data transfer is authorized, use it for repeated
bounded judgments over evidence already collected: yes/no checks, choices among known options,
and ratings against an explicit rubric. It cannot retrieve missing evidence or produce prose.
Keep decisions already settled by exact code in code.

Read [Jev setup and routing](references/jev.md) before the first Jev call. The bundled
`scripts/jev.py` supports single items, JSONL batches and offline `--dry-run`. It reads only
`TYPESAFE_API_KEY` from the environment. It never searches another project's credentials.
Without a key or transfer permission, continue locally and name that mode; installation itself
does not authorize API spend or sharing data. Preserve uncertain and failed rows for agent review.
Typed answers constrain shape, not truth. They do not certify a skill or replace source checking.

## 5. Return coverage, then act

Return the extent, optional lead, contributor count, per-question cited rules, conflicts and gaps.
Mark uncovered judgments as such. At `mid`/`high`, give each gap a concrete closure route.
Then apply the guidance to the original task. If delegating scouting, wait for its report before
making the decisions it is supposed to inform; use the owning project's root as the worker cwd.

At `max`, search the registry for every gap and read actual candidate bundles before deciding
fit. If none fits, research primary sources and relevant papers, then build a complete skill
with cited rules and references. Use at least three independent sources, including primary docs
or research where available. Screen papers for retractions, design and conflicts; keep uncertainty
visible. A fresh reviewer checks the draft against its sources before installation. Build at most
three skills per run; report remaining gaps explicitly and use the user's queue if authorized.
If research, installation or review is unavailable, report the incomplete gap rather than claiming
`max` completion. This procedure does not require a private home-directory command.
