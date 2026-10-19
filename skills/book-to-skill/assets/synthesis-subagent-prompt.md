# Synthesis subagent prompt (template)

Use this when spawning the synthesis subagent in Step 5 of `book-to-skill`. The synthesis subagent runs AFTER all chapter subagents complete and BEFORE per-skill drafting begins. It's the most important step in the pipeline.

---

You are the synthesis step in a bookâ†’skill carving pipeline. Chapter extraction subagents have run in parallel and produced one report each. Your job is to dedupe across chapters, decide the family shape, and produce the final carving plan.

**Inputs:**
- Chapter reports: `outline/chapter_01.md` through `outline/chapter_NN.md`
- Source book: {book_title} ({book_year}, {book_edition})
- Existing skills the carved family must not step on: {existing_skills_to_avoid}

**Output:** Write `outline/synthesis.md` with the structure below.

## Required output sections

### 1. Master framework inventory

A table with one row per UNIQUE framework (deduplicated across chapters):

| Framework | Canonical Chapter | Cited by Chapters | Verdict | Sibling links |
|---|---|---|---|---|

- **Canonical chapter** = the chapter where the framework is *defined* with a formula, taxonomy, or step-by-step. Not where it's first mentioned, foreshadowed, or applied.
- **Cited by chapters** = all chapters whose subagent extracted (or referenced) this framework.
- **Verdict** = CARVE / FOLD-INTO-<other> / REFERENCE-ONLY / UMBRELLA-PARENT-REF.

### 2. Deduplication notes

For every framework that appeared in multiple chapter reports, explain the dedupe:

> **Lie Factor** â€” extracted by Ch 1, Ch 2, Ch 3 subagents.
> - Canonical: Ch 2 (formula appears on book page 57).
> - Ch 1 mention: foreshadowing; downgrade to cross-reference.
> - Ch 3 mention: application/integration with the 6 principles; do not re-extract as a separate framework.

### 3. Umbrella-chapter detection

Chapters that overlap heavily with their member chapters get routed to a parent reference doc, not to a peer skill. Symptoms of an umbrella chapter:

- Its frameworks fail the `distinct_triggers` test against multiple sibling carves
- Its prose explicitly unifies concepts you've already extracted as separate frameworks
- Its content reads like "what we've been doing all along"

For each umbrella chapter you detect, write the parent-ref-doc target (e.g., `tufte-graphical-excellence-reference.md`) and the section structure that doc should contain.

### 4. Borderline-folding pass

For every candidate marked "borderline CARVE" in a chapter report, default to FOLD. Reverse to CARVE only if you can defend in one sentence why folding would lose something. Examples of legitimate carve-over-fold:

- The borderline framework has a distinct output type (e.g., a layout vs. an audit)
- The borderline framework triggers on a different user moment than the parent
- The parent skill is already at the SKILL.md size ceiling (>500 lines) and can't absorb more

Otherwise, fold it. Over-carving is more expensive than under-carving â€” it pollutes the trigger surface.

### 5. Shape decision

Count final CARVE verdicts after dedupe + folding:

- **â‰¥ 5 carves, independently triggerable** â†’ family of atomic skills with `{prefix}-` naming. State the prefix (usually author surname or book's defining word).
- **2â€“4 carves, OR carves are co-dependent** â†’ one skill with `references/<framework>.md` chapters. Name the parent skill.
- **0â€“1 carves** â†’ don't carve. Recommend the user keep the content as a knowledge-base doc instead.

### 6. (Optional but recommended) llm-council pressure-test

For carves you're least confident about, invoke `llm-council` with the prompt:

> "Is `{candidate-skill-name}` really a reusable agent skill, or is it a paraphrased chapter of {book_title}? An agent skill must produce a concrete output (decision, score, rewrite, plan). A paraphrased chapter just summarizes. Verdict: skill or summary?"

If 2+ councilors flag the candidate as a summary, downgrade it to a reference doc.

### 7. Carving plan

For each final CARVE, write:

```
SKILL: {prefix}-{framework-slug}
CANONICAL CHAPTER: <book pages Xâ€“Y>
FRAMEWORK NAME (verbatim from book): <quoted>
OUTPUT TYPE: <audit-metric / design-pattern / decision-rubric / checklist / process>
SIBLING LINKS: <other carved skills in this family that this one should reference>
PARENT REFERENCE DOC (if any): <path>
```

Per-skill drafting subagents will consume this plan in Step 6.

## Style notes

- Be ruthless. The biggest failure mode of this pipeline is over-carving â€” producing 12 skills when 5 would have been enough.
- The four-test rubric is binding. Reject CARVE verdicts from chapter reports that violated the rubric (e.g., marked CARVE despite a FAIL on one of the four tests).
- Length: 600â€“1500 words. The synthesis is dense by design.
