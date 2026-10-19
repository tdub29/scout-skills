---
name: refactor-god-file
description: Safely decompose a giant single file (a "god file" / monolith / 5000+ line module) into a clean, layered, DRY module tree without breaking behavior. Use when the user has a huge file to split up, wants to untangle spaghetti, refactor a monolith, extract modules, or says they "vibe-coded into a corner" and need to get out. Runs a documented audit, researches the target architecture, writes a cross-referenced refactor plan, then extracts modules one dependency-ordered step at a time with a smoke test and a component map after each move, verifies functional parity against the original, runs the full test suite, and only then purges the backwards-compat shims. Behavior-preserving and additive: never deletes the original until parity is proven green.
user-invocable: true
allowed-tools: "Read Write Edit Bash Glob Grep"
metadata:
  version: "1.0.0"
  source: local/self
---

# Refactor a God File

Turn one unmaintainable file into a clean layered module tree **without changing what it does**. The whole point is that every step keeps the app running and every move is provably behavior-preserving, so you can stop, resume, or bail at any point and the code still works.

This skill exists because the naive "just split it up" prompt has no net: it moves code, the build silently breaks three files over, and you can't tell whether the split dropped a function or a side effect. The fix is not a bigger prompt, it is a **baseline, a plan, and a parity gate** around each move.

> Honest expectation: a real 5000+ line file is a half-day to a couple of days of careful work, not "an hour or two." The steps below are what make it *safe*, not fast. Do not skip the baseline or the parity check to save time; those two are the entire reason this works.

## When to use / when not

**Use it** for: a single file that is too big to reason about, mixed concerns crammed together (routes + business logic + data access + rendering in one place), a `utils.js` that became a dumping ground, an HTML file with 3000 lines of inline `<script>`, a `main.py` that is the whole app.

**Don't use it** for: adding a feature, fixing a bug, or a rewrite. This is a **behavior-preserving move**, not a redesign. If the code is also wrong, refactor first (this skill), then change behavior in a *separate* pass with its own tests. Mixing the two is how you lose track of what broke.

## Non-negotiables (read before you touch anything)

1. **Additive until proven. Never delete or truncate the original file until parity is verified and the full test suite is green.** Work on a branch or a git worktree. The original is your source of truth for parity the entire time.
2. **Behavior-preserving only.** No logic changes, no renames-for-taste, no "while I'm here" fixes during a move. A move step changes *where* code lives, never *what it does*. Note improvements in the plan for a later pass; do not do them now.
3. **You cannot verify against nothing.** If test coverage of the file is thin, the first real work is writing **characterization tests** that pin current behavior (Phase 0). Parity means "same outputs as the original," and you need something that captures "the original" first.
4. **Dependency order, leaf-first.** Extract the things that depend on nothing first (constants, pure helpers, types), then things that depend only on already-extracted modules, up to the entry points last. Moving a top-level function first drags its whole dependency tree with it and the step never lands.
5. **Keep it green every step.** After each move, the app still builds and the smoke test passes *before* you start the next move. A step that leaves red is not done; fix or revert it, do not stack another move on top.
6. **Separate doing from judging.** The agent that moved the code should not be the sole certifier that parity holds. Use a fresh review pass (a subagent that saw only the parity checklist + old and new symbol lists) for the Phase 5 gate. See [[orchestration-and-loops]].
7. **Checkpoint every step.** This is a long, resumable run. Flush progress to `refactor/CHECKPOINT.md` after every extraction so a usage wall or killed session resumes instead of restarting. See [[durable-progress-and-checkpointing]].

## Working directory

All of this skill's artifacts live in a `refactor/` folder next to the target (or `.refactor/<file-slug>/` if the repo prefers hidden scratch). Templates for each are in [templates/](templates/):

| File | What it holds | Template |
|---|---|---|
| `AUDIT.md` | Every symbol in the god file, described technically | [templates/AUDIT.md](templates/AUDIT.md) |
| `REFACTOR-PLAN.md` | Target architecture, module tree, dependency-ordered extraction sequence | [templates/REFACTOR-PLAN.md](templates/REFACTOR-PLAN.md) |
| `COMPONENT-MAP.md` | The README: which piece of the god file now lives where, and why | [templates/COMPONENT-MAP.md](templates/COMPONENT-MAP.md) |
| `PARITY-CHECKLIST.md` | Old symbol â†’ new home, one row each, checked when verified present | [templates/PARITY-CHECKLIST.md](templates/PARITY-CHECKLIST.md) |
| `CHECKPOINT.md` | Resumable state: done vs remaining steps, next action | [templates/CHECKPOINT.md](templates/CHECKPOINT.md) |

## The phases

Run them in order. Each phase writes its artifact to disk before the next begins.

### Phase 0 â€” Baseline & safety net

The net goes up before anything moves.

1. **Isolate.** Create a branch (`refactor/<file>`) or a git worktree. Confirm the working tree is clean first (`git status`). Never refactor on top of uncommitted unrelated changes.
2. **Inventory.** Record the file's line count, and list every top-level symbol: functions, classes, constants, exported names, routes/handlers, event listeners, top-level side effects. `scripts/find-god-files.ps1` / `.sh` finds the biggest files in a repo if you're still choosing a target.
3. **Capture the baseline behavior.**
   - If a test suite exists: run it, save the exact pass/fail output to `refactor/baseline-tests.txt`. This is the bar every later run must still clear.
   - If coverage is thin (common for vibe-coded files): write **characterization tests** â€” tests that assert the *current* output for representative inputs, whatever it is, right or wrong. You are pinning behavior, not judging it. For a web page/UI, a smoke test can be "it renders without console errors and the key elements exist." For a CLI/library, capture outputs for a spread of inputs.
   - If the thing genuinely cannot be tested automatically, define a written **manual smoke checklist** (the exact clicks/commands and expected results) and run it by hand at each gate. Say so in the checkpoint; a manual gate is weaker and the human should know.
4. **Commit the baseline.** `refactor/` folder + any new characterization tests, one commit. Now you can always get back here.

### Phase 1 â€” Documented technical audit

Write `AUDIT.md`: a complete, technical description of everything the file does. For each symbol capture: what it does, its inputs and outputs, its side effects (I/O, DOM, network, globals, mutation), what it depends on (other symbols in the file, imports, globals), what depends on it, and a flag for anything that looks like dead code, duplication, or a distinct concern. Group symbols by the concern they belong to (data access, business logic, presentation, config, etc.) â€” that grouping becomes the module boundaries in Phase 2. This audit is a deliverable in its own right even if you stop here.

### Phase 2 â€” Research the target architecture, then plan

1. **Research the right layout for *this* stack**, don't guess. Web-search current best-practice structure for the language/framework in play (e.g. feature-folder vs layered for a React app, blueprint/router split for Flask, service/repository for a Rails model that got fat). Prefer the conventions the rest of *this* repo already uses over a generic ideal â€” consistency beats theoretical purity. Capture the sources and the chosen pattern in the plan.
2. **Write `REFACTOR-PLAN.md`:**
   - The **target directory tree** (the new layered structure), each folder's responsibility in one line.
   - A mapping from each audit concern-group to a target module.
   - The **extraction sequence**: an ordered, leaf-first list of steps, each step = "extract group X into path Y". Order by dependency so every step only depends on already-extracted or not-yet-touched code.
   - The **shim strategy**: how the original keeps re-exporting moved symbols so nothing downstream breaks mid-refactor (see Phase 4).
   - A **later-pass list**: every improvement you noticed but are deliberately *not* doing now (behavior changes, dead-code you suspect but can't yet prove, renames). Parking them here is what keeps the refactor behavior-preserving.

### Phase 3 â€” Cross-reference and lock the plan

Reconcile the three views against each other: **audit â†” plan â†” the original file**. Every symbol in the audit must appear in exactly one extraction step in the plan. Every step in the plan must trace back to real symbols in the file. Walk the original once more and fix anything the audit missed (audits of huge files always miss a few closures or an event handler). Update `AUDIT.md` and `REFACTOR-PLAN.md` until they agree with the file and with each other. Only then start moving code. A plan that disagrees with the file will drop functionality â€” this phase is cheap insurance against that.

### Phase 4 â€” Extract, one dependency-ordered step at a time (the loop)

This is the loop. For **each** step in the plan's extraction sequence, in order:

1. **Create the new module** at its target path and move the group's code there (copy the exact code; no edits to logic).
2. **Leave a shim in the original**: re-export the moved symbols from their new home so every existing caller still resolves (`export { foo } from './new/path'`, `from .new.path import foo`, etc.). The original file shrinks but stays a valid entry point. Nothing downstream changes yet.
3. **Wire imports** inside the new module for anything it needs from already-extracted modules.
4. **Smoke test.** Build + run the smoke test / characterization tests. Green before you continue. Red â†’ fix or revert *this step only*, never proceed on red.
5. **Update `COMPONENT-MAP.md`**: add rows for the symbols you just moved â€” old location, new location, one-line why. This is the README that answers "where did X go."
6. **Commit** the single step. One module per commit keeps the history bisectable and the checkpoint honest.
7. **Update `CHECKPOINT.md`**: mark this step done, record the next step. Flush before starting the next iteration.

Stop condition: every step in the sequence is done and green. Do not declare the loop done on a soft "looks about right" â€” it's done when the checklist is fully checked and the smoke test is green.

### Phase 5 â€” Parity cross-check (fresh eyes)

Now prove nothing was lost. Fill `PARITY-CHECKLIST.md`: one row per symbol from the Phase 1 audit, mapped to its new home, checked only when you've confirmed it actually exists and is wired there. Diff the **set of exported/public names** the original exposed against the union of what the new modules expose â€” they must match (minus anything the plan explicitly retired to the later-pass list). **Have a fresh reviewer do this pass** â€” a subagent given only the audit symbol list, the new module tree, and the checklist, asked "what from the original has no home in the new structure?" The mover is biased toward believing it's complete; a clean reviewer catches the dropped closure. Anything missing goes back to Phase 4 as another step.

### Phase 6 â€” Full verification

Smoke test **and** the actual test suite, both green, compared against `refactor/baseline-tests.txt` â€” same tests pass now as passed at baseline (plus the new characterization tests). If baseline had failures, they should still fail the *same way* (behavior-preserving means preserving the bugs too, until the later pass). Fix any regression before moving on. If verification can only be manual, run the full manual smoke checklist from Phase 0 and record the result.

### Phase 7 â€” Purge the shims and dead weight

Only now, with parity proven and tests green, remove the scaffolding â€” one small step at a time, smoke-testing after each:

1. Pick one shimmed symbol. Update its **callers** to import from the new module directly. Smoke test. Commit.
2. Remove that symbol's shim from the original. Smoke test. Commit.
3. Repeat until the original file has no shims left â€” it's now either empty (delete it) or a slim entry point that just wires the new modules together.
4. **Then** work the later-pass list's dead-code items: each suspected-dead function gets confirmed unreferenced (grep all callers) before removal, removed alone, smoke-tested. Never batch-delete dead code; batch deletes hide the one that wasn't actually dead.

After each removal the smoke test is the tripwire. A red smoke test right after a shim removal means that caller wasn't migrated â€” fix that caller, don't force the removal.

## Running it as a workflow or loop

Phase 4 is a natural bounded loop (one iteration per extraction step) and Phase 7 is a second one. For a large file, drive them with `/loop` or a dynamic Workflow so each step is its own checkpointed iteration:

- **Stop condition** = the extraction sequence / shim list is fully consumed and smoke is green. Not a soft "looks done."
- **Checkpoint** = `refactor/CHECKPOINT.md`, flushed every iteration.
- **Judge separately** = the Phase 5 parity gate uses a fresh reviewer, not the mover.
- **Model tiering** = a capable model does Phases 1â€“3 and 5 (audit, architecture, parity judgment); a cheaper model can execute the mechanical moves in Phase 4. This is the `/improve` shape (capable plans, cheap executes).

See [[orchestration-and-loops]] and [[reference_dynamic-workflows]] for the workflow API and cost gates. Codex has no dynamic workflows â€” run the same phases by hand, one commit per step.

## Failure modes this prevents

| Naive split | What breaks | This skill's guard |
|---|---|---|
| Move code, no baseline | Can't tell if you dropped a function | Phase 0 characterization tests + parity checklist |
| Move top-level function first | Drags whole dep tree, step never lands | Leaf-first dependency ordering (Phase 2/4) |
| Delete original immediately | Nothing to verify parity against | Additive; original retired only in Phase 7 |
| Mix refactor + bug fixes | Can't tell a move-bug from a logic-bug | Behavior-preserving rule; later-pass list |
| One giant commit | Not bisectable, can't resume | One module per commit + checkpoint each step |
| Self-certify completeness | Miss the dropped closure | Fresh-reviewer parity gate (Phase 5) |
| "Done, looks clean" | Silent regressions ship | Full suite vs baseline (Phase 6) before purge |

## Quick start

1. `pwsh scripts/find-god-files.ps1 -Root <repo>` (or `sh scripts/find-god-files.sh <repo>`) to confirm the target if it isn't obvious.
2. Copy the five templates into a new `refactor/` folder next to the target.
3. Phase 0: branch, inventory, capture baseline (write characterization tests if coverage is thin).
4. Work Phases 1 â†’ 7 in order, keeping the app green after every step.
