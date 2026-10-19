## Coding Tasks (gstack)

### Rules (non-negotiable)

1. **Always spawn, never redirect.** When user asks to use ANY gstack skill,
   ALWAYS spawn a Claude Code session via sessions_spawn. Never tell user to
   open Claude Code himself. Never say "this needs to run in Claude Code."
   Never say "you'll need to open Claude Code for that." Just do it.

2. **Resolve the repo.** If user names a repo or project, set the working
   directory to that repo path. If the repo path isn't known, ask which
   repo â€” don't punt to telling the user to open Claude Code.

3. **Autoplan runs end-to-end.** For /autoplan specifically: spawn the session,
   let it run the full review pipeline (CEO â†’ design â†’ eng), and when it
   finishes, report the plan back here in chat. Write the plan to memory so
   the user can find it later. User should never have to leave Telegram.

### Dispatch Routing

When asked for coding work, pick the dispatch tier:

**SIMPLE:** "fix this typo," "update that config," single-file changes
â†’ sessions_spawn(runtime: "acp", prompt: "<just the task>")

**MEDIUM:** multi-file features, refactors, skill edits
â†’ sessions_spawn(runtime: "acp", prompt: "<gstack-lite content>\n\n<task>")

**HEAVY:** needs a specific gstack methodology
â†’ sessions_spawn(runtime: "acp", prompt: "Load gstack. Run /qa https://...")
  Skills: /cso, /review, /qa, /ship, /investigate, /design-review, /benchmark, /gstack-upgrade

**FULL:** build a complete feature, multi-day scope, needs planning + review
â†’ sessions_spawn(runtime: "acp", prompt: "<gstack-full content>\n\n<task>")
  Claude Code runs: /autoplan â†’ implement â†’ /ship â†’ report back

**PLAN:** user wants to plan a Claude Code project, spec out a feature, or design
  something before any code is written
â†’ sessions_spawn(runtime: "acp", prompt: "<gstack-plan content>\n\n<task>")
  Claude Code runs: /office-hours â†’ /autoplan â†’ saves plan file â†’ reports back
  Persist the plan link to memory/knowledge store.
  When the user is ready to implement, spawn a new FULL session pointing at the plan.

### Decision Heuristic

- Can it be done in <10 lines of code? â†’ **SIMPLE**
- Does it touch multiple files but the approach is obvious? â†’ **MEDIUM**
- Does the user name a specific skill (/cso, /review, /qa)? â†’ **HEAVY**
- "Upgrade gstack", "update gstack" â†’ **HEAVY** with `Run /gstack-upgrade`
- Is it a feature, project, or objective (not a task)? â†’ **FULL**
- Does the user want to PLAN something without implementing yet? â†’ **PLAN**
