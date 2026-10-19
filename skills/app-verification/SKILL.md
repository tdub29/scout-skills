---
name: app-verification
description: "Drive the real app headlessly to prove a UI fix"
---

# App verification

**The bottleneck is not the agent's coding, it is the human's checking.** An agent that cannot
run the app cannot close its own loop, so a person has to open the page, click around, and paste
back a screenshot. That person is the ceiling on how many agents can work at once.

This skill removes the ceiling. It gives an app a **feature map** (how to reach every feature) and
a **runner** (drives it headlessly, asserts it, captures errors). Once those exist, "it works now"
is a command, not an opinion.

## Two modes

| Mode | When | Go to |
|---|---|---|
| **Create** | Project has no `.agents/feature-map.json` | [Â§ Create](#create-a-feature-map) |
| **Maintain** | Map exists but drifted, or a feature was added | [Â§ Maintain](#maintain-the-map) |

## The runner

Already built, key-free, uses the local Playwright Chromium. Never write a bespoke script.

```bash
python .agents/scripts/verify-app.py <project>            # verify every feature
python .agents/scripts/verify-app.py <project> --list     # what features exist + notes
python .agents/scripts/verify-app.py <project> -f <id> --shots --headed   # debug one
python .agents/scripts/verify-app.py <project> --json     # machine-readable
python .agents/scripts/verify-app.py --selftest           # prove the runner itself
```

Exit 0 = verified. Exit 1 = a feature failed, a console error fired, or a request failed. It is a
gate, so it belongs in a pre-push hook and in CI, not just in your terminal.

## Create a feature map

1. **Find the entry.** A standalone `.html`, a dev server, or a hosted URL. Read the manifest
   (`package.json` scripts) rather than guessing the command.
2. **Enumerate features from the UI, not the source tree.** The map is written from the *user's*
   point of view: what a person would call the thing, and how they reach it. A map keyed on module
   names is useless for triaging "the left sidebar is laggy".
3. **Reach each one.** Open it headed (`--headed`) once and record the real click path and the
   selector that proves the feature rendered. Prefer a stable id or `data-*` hook. If none exists,
   **add one to the app** - a selector that breaks on a CSS tweak is a false alarm generator.
4. **Assert something specific.** Presence is weak. `textMatches` on a value, `minCount` on a list,
   or a JS `assert` expression catches an empty render that still mounts.
4b. **When a real click hangs, click through JS.** On an app that keeps the main thread busy - a
   map refreshing live sources, a canvas render loop - Playwright's click waits for actionability
   and never returns, so a working control reads as broken. Use `{"eval": "document.querySelector(
   'sel').click()"}` and say so in the notes: it still proves the handler is wired, it does not
   prove the element is reachable by a human. Same trick for a control that only exists at another
   width, though a per-feature `viewport` is the better answer there.
5. **Write notes.** Keyboard shortcut, what the feature is for, what usually breaks. This is what
   lets an agent map a screenshot with no words onto a real feature.
6. **Run it, and make it fail on purpose.** Break a selector, confirm FAIL, restore. A verification
   that has never failed is not known to work. See
   [`verification-and-evidence`](../../rules/verification-and-evidence.md): a skipped check must
   never read as a passed one.
7. **Wire it.** Add the command to the project's `CLAUDE.md` and, where the project has one, to
   its pre-push hook.

Schema and every field: [`references/feature-map-schema.md`](references/feature-map-schema.md).

Minimal example:

```json
{
  "app": "finances",
  "entry": { "type": "file", "path": "finances.html" },
  "features": [
    {
      "id": "net-worth",
      "name": "Net worth headline",
      "path": ["#tab-overview"],
      "selector": "[data-verify=net-worth]",
      "expect": { "textMatches": "\\$[0-9,]+" },
      "notes": "First tile on load. Blank here usually means the accounts JSON failed to parse."
    }
  ]
}
```

## Maintain the map

The map rots the moment a feature ships without an entry. Treat drift as a defect.

- **Adding a feature to the app means adding it to the map, in the same change.** Not a follow-up.
- **Audit for gaps:** list the app's user-facing surfaces, diff against `--list`, and report what is
  unmapped rather than silently covering less.
- **A flaky feature is a bug in the map or in the app.** Fix the selector or the app; never delete
  the feature to get green. Deleting a check to pass is the failure this whole layer exists to stop.
- **When a real bug slips through, add the feature that would have caught it** before fixing the bug.

## Reproducing a bug report

With a map, a low-quality report ("screenshot + ???") becomes tractable:

1. `--list` to match the screenshot or phrase to a feature id.
2. `-f <id> --shots --headed` to watch it happen.
3. Compare the shot to the report. If it already passes, the bug is fixed or environment-specific -
   say which, with the evidence.

## Where this sits

Verification is layer 3 of the enforcement ladder. It proves the code is *correct*; it does not
keep the code *good*. For that, see
[`hard-enforcement-over-review`](../../rules/hard-enforcement-over-review.md) - if you find yourself
enforcing an invariant by reading the diff, convert it to a lint rule or a CI failure instead.
