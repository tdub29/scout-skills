# Review Mode & the Evidence Loop

Two systems share one data source (quiz results) but have different jobs:
**retention** (spaced-repetition review of cards) and **adaptation** (evidence-
gated updates to LEARNER.md). Keep them distinct.

## Data files (in `~/.explain-this/memory/`)

**cards.jsonl** â€” one self-contained card per line:

```json
{"id": "card_aiayn_03",
 "artifact": {"title": "Attention Is All You Need", "source": "https://arxiv.org/abs/1706.03762", "explained": "2026-07-15"},
 "question": "Why does multi-head attention use multiple smaller heads instead of one full-width head?",
 "answer": "Each head learns a different relationship type in a different subspace; one full-width head would average them into mush.",
 "type": "transfer",
 "tags": ["mechanism"],
 "state": {"interval_days": 4, "ease": 2.5, "due": "2026-07-19", "reps": 2, "lapses": 0},
 "history": [{"ts": "2026-07-15T09:12:00Z", "result": "hit", "mode": "inline"}],
 "status": "active"}
```

**signals.jsonl** â€” one append-only line per quiz attempt:

```json
{"ts": "2026-07-15T09:12:00Z", "artifact": "attention-is-all-you-need", "card": "card_aiayn_03", "tags": ["mechanism"], "result": "hit", "mode": "inline", "excluded": false}
```

Signals are dumb at write time â€” no interpretation. Scheduling is straight
SM-2 (see `scripts/sm2.ts`): hit (q=5) â†’ interval Ã— ease; partial (q=3) â†’
advances but drops ease; miss (q=2) â†’ interval resets, ease drops, lapse
recorded. Cards retire when the interval exceeds ~120 days (known â€” stop
asking); `suspended` when the user says "don't quiz me on this." Cap ~5 cards
per artifact so the deck grows linearly with reading.

## Review session flow

```
explain-this review
  â†’ scripts/sm2.ts due            (due cards, most overdue first, cap 8)
  â†’ per card:
      ask the question â†’ user answers in FREE TEXT
      â†’ grade it yourself: hit / partial / miss, one line of feedback
      â†’ on miss: RE-EXPLAIN DIFFERENTLY â€” a new route in, shaped by
        LEARNER.md, never the same words again
      â†’ scripts/sm2.ts grade <id> <result>   (updates SM-2 + logs the signal)
  â†’ session close: score summary ("6/8 â€” two derivation misses")
  â†’ run the threshold scan (below); if a pattern crossed, show the drafted
    profile entry WITH its evidence and add it to LEARNER.md
```

Grading is always agent-side against the stored answer/rubric. Never
self-graded â€” self-grading is generous and corrupts the evidence.

## The evidence loop (adaptation)

The path from "missed a question" to "the profile says something about you"
must pass through accumulated evidence:

1. **Threshold scan** after each session: `scripts/scan-signals.ts scan`
   (defaults: â‰¥4 misses on the same tag, across â‰¥2 distinct artifacts, within
   a 60-day window). The cross-artifact requirement separates "struggles with
   derivations" (profile-worthy) from "that one paper was brutal" (not).
2. **Evidence cited inline.** Every Known Weak Patterns entry written to
   LEARNER.md carries its proof: `[evidence: 5 misses / 3 artifacts, Julâ€“Sep]`.
   Auditable against signals.jsonl; the user may delete any entry they
   disagree with. The profile never claims what it can't prove.
3. **Patterns heal.** `scripts/scan-signals.ts heal` (defaults: hit-rate â‰¥80%
   over the last 6 graded signals on a tag) lists entries eligible for
   retirement. Weak patterns are supposed to shrink under treatment â€” a
   deficit-only profile becomes a self-fulfilling ceiling.
4. **Bad-question escape hatch.** If the user says a question was bad, mark
   that signal `"excluded": true` â€” generation failures never become facts
   about the learner. Skips are logged as signals too.

All thresholds are tunable constants in the scripts' flags; the defaults are
starting guesses.

## Surfacing

Portable core is on-demand plus a non-blocking nudge: when the skill is
invoked for a new explanation and cards are due, mention it once ("6 due â€”
review first, or after?"). Never block, never nag. Host-specific layers
(daily digests, notes-app exports) are optional additions, never requirements.
