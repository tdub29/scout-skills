---
name: loopify
description: "Schedule recurring Claude Code work. Cron or wake-ups."
metadata:
  version: 0.1.0
---

# /loopify â€” Set up an agent loop

Wizard for going from *"this task should run periodically"* to a working loop with the right pacing, idempotency, and bail-out. Reference: `ScheduleWakeup` (dynamic pacing), `CronCreate` (fixed schedule), and the built-in `/loop` (dynamic self-paced re-entry).

## Step 0 â€” Confirm what you're looping

Ask if not obvious from context: *"What task should this loop do each iteration?"*

Then get the essentials:

| Question | Why it matters |
|---|---|
| **How often?** | Determines cron vs dynamic vs one-shot |
| **When to stop?** | Bail-out condition â€” loops must have one |
| **What's the loop body doing?** | Determines idempotency requirements |
| **Where does output go?** | File / notification / commit / nothing |
| **What's the failure mode if it runs twice?** | Idempotency validation |

## Step 1 â€” Pick the pattern

Three primary patterns. Route by the answer to "how often":

### Pattern A â€” Cron (fixed schedule)

**Use when**: task runs at predictable intervals â€” daily at 8am, weekly on Fridays, hourly on the hour.

Tool: `CronCreate` â€” schedules a recurring task with a cron expression.

```
CronCreate({
  schedule: "0 8 * * *",           // daily at 8am local
  prompt: "<loop body prompt>",
  timezone: "America/Los_Angeles"
})
```

Common cron patterns:
- `0 8 * * *` â€” daily at 8am
- `0 9 * * 1` â€” Mondays at 9am
- `0 9 * * 5` â€” Fridays at 9am
- `0 */2 * * *` â€” every 2 hours
- `*/15 * * * *` â€” every 15 minutes

**Trade-offs:**
- âœ… Predictable, human-readable, easy to reason about
- âœ… Best for time-of-day-dependent tasks (morning brief, EOD summary)
- âŒ Runs at the scheduled time even if the last run isn't done â€” need idempotent body
- âŒ No self-pacing â€” over-schedules if the task duration varies wildly

### Pattern B â€” Dynamic pacing (self-scheduled)

**Use when**: task should react to state, not the clock. Monitor-until-condition-met patterns. Waiting on an external event.

Tool: `ScheduleWakeup` â€” the current run schedules its own next wake-up.

```
ScheduleWakeup({
  delaySeconds: 270,               // stay in cache window (< 5min)
  reason: "checking build status; sleeping under 5min to stay cache-warm",
  prompt: "<same task, re-entered>"
})
```

**Critical delay rules** (from `ScheduleWakeup` docs â€” internalized in the wizard):

| Delay range | Use for | Cache impact |
|---|---|---|
| **60sâ€“270s** | Active work â€” polling build, waiting for state that's about to change | Stays in 5-min prompt cache â€” fast + cheap |
| **300s** âŒ | **DON'T USE THIS** | Worst of both worlds â€” pay cache miss without amortizing |
| **300sâ€“3600s** | Waiting on something that takes minutes to change | Pay cache miss but justified |
| **1200sâ€“1800s** (20â€“30 min) | Idle ticks with no specific signal | Default for autonomous loops |

Never pick 300s literally â€” either drop to 270 (cache stays warm) or commit to 1200+ (cache miss buys longer wait).

**Trade-offs:**
- âœ… Adaptive â€” sleeps longer when idle, shorter when active
- âœ… Cache-optimal when tuned right
- âŒ Requires the loop body to know when to schedule next (extra logic)
- âŒ Harder to reason about when it'll run

### Pattern C â€” One-shot loop (until-condition)

**Use when**: task runs until a condition is met, then stops. No recurrence after that.

Tool: `/loop` (built-in) with an exit condition in the prompt itself.

```
/loop
Check if the deploy is healthy. If yes â†’ stop. If no â†’ wait 5 min and check again.
Max 10 iterations. If still failing after 10, alert and stop.
```

**Trade-offs:**
- âœ… Simplest for check-until-condition
- âœ… Bounded â€” always eventually terminates
- âŒ Not for indefinite recurrence â€” that's Pattern A or B

## Step 2 â€” Design the loop body for idempotency

Idempotent = running the loop twice produces the same result as running it once. **Non-negotiable for cron and dynamic patterns** because they'll fire while the previous iteration is still running or partially complete.

Idempotency patterns:

- **Use "already done" markers**: e.g., commit a state file `<vault>/.loopify/<name>-last-run.txt` with the timestamp of last successful run. Loop body checks the timestamp before doing work.
- **Use dedupe keys**: if the loop writes to a DB or file, key by content-hash or timestamp so re-runs are no-ops.
- **Use transactions**: DB writes in the loop body should be atomic â€” either all commit or all roll back.
- **Query before mutate**: check current state before applying the change. If already applied, skip.

Show the user the loop body draft, highlighting the idempotency check. If none exists, add one.

## Step 3 â€” Bail-out condition

Every loop needs one. Options:

| Bail-out | When to use |
|---|---|
| **Max iterations** (e.g., stop after 100 runs) | Cron loops â€” prevents runaway |
| **State-based** (e.g., stop when metric X drops below Y) | Monitoring loops |
| **Time-based** (e.g., stop after 24 hours) | Bounded monitoring |
| **Error-based** (e.g., stop on 3 consecutive failures) | All loops â€” catches degradation |

If the loop is truly indefinite (e.g., a weekly cron with no end), still add a manual bail-out via `CronDelete`. Document it in the SKILL/loop notes so the user knows how to stop it.

## Step 4 â€” Set the schedule

Based on the pattern from Step 1:

**Cron (Pattern A):**
```
CronCreate({
  schedule: "<expression>",
  timezone: "<tz>",
  prompt: "<loop body>",
})
```
Report the `cron_id` returned so the user can `CronDelete` later.

**Dynamic (Pattern B):**
Wrap the loop body prompt so it ends with a `ScheduleWakeup` call:
```
<do the work>
Then: ScheduleWakeup({delaySeconds: <tuned per Step 1>, prompt: "<same body>", reason: "<why this cadence>"})
```

**One-shot (Pattern C):**
Just run `/loop <prompt with exit condition>`.

## Step 5 â€” Verify the first run

Wait for the first iteration (or trigger it manually via `/loop` with the same prompt for a dry-run). Confirm:

- Output landed where expected
- Idempotency check works (run twice â€” second should be a no-op)
- Bail-out condition would fire correctly if triggered
- Log/notification appears if configured

## Step 6 â€” Report + follow-ups

Report:
- Pattern picked (A/B/C) + why
- Cron ID or wakeup pattern registered
- Bail-out condition set
- Idempotency mechanism in place
- How to stop the loop (`CronDelete <cron_id>` or "just don't call the wakeup" for dynamic)

Offer:
- *"Save this loop configuration as a skill via `skillify from-chat`?"*
- *"Want to also register a `weekly-review` or `daily-startup` loop while we're here?"*
- *"Should the loop write to `second-brain` outputs when it runs?"*

## Common loop recipes

Templates for frequent loop types (fill in as they're used):

- `references/daily-brief.md` â€” morning routine loop (calendar + priorities + overnight)
- `references/weekly-review.md` â€” Friday portfolio pulse
- `references/upstream-check.md` â€” periodic check for changes to an adapted skill's upstream
- `references/vault-compile.md` â€” periodic raw/ â†’ wiki/ compilation
- `references/metric-monitor.md` â€” poll a metric until it crosses a threshold, then alert

## Composes with

- **`skillify`** â€” sibling in `-ify` trifecta. Use `skillify` to author a new SKILL.md â€” use `loopify` when the goal is a scheduled task, not a skill.
- **`toolify`** â€” sibling. Use `toolify` for adding an integration â€” use `loopify` when the goal is running something on top of an already-integrated tool on a schedule.
- **`second-brain`** â€” many loops write to the vault (raw/ or outputs/). The vault auto-commit pattern applies.
- **`pm`** â€” daily-brief and weekly-review loops often read from pm before generating output.

## Notes on quality

- **Never pick 300s for `delaySeconds`.** Worst of both worlds. Drop to 270 or commit to 1200+.
- **Every loop needs a bail-out.** Even indefinite ones need a documented manual stop.
- **Idempotency is non-negotiable for cron + dynamic.** Assume the loop will fire twice while a previous iteration is running.
- **Prefer dynamic pacing over over-frequent cron.** Cron every 15 min wastes tokens if the work isn't ready; dynamic pacing scales down when idle.
- **Document the cron_id.** Otherwise the loop is orphaned and hard to stop.
- **Log every iteration briefly** â€” even a single line ("2026-06-30 08:00 daily-brief: ran, 3 items") makes debugging drift trivial.
- **Loops that touch external APIs need rate-limit respect.** If the vendor has a 100/day limit, don't schedule 500/day.
- **Bounded > unbounded when uncertain.** If unsure whether to run for a week or a month, start with a week â€” extend after seeing it work.
