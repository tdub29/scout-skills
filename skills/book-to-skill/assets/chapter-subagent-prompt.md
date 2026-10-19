# Chapter extraction subagent prompt (template)

Use this when spawning a chapter subagent in Step 4 of `book-to-skill`. Substitute the placeholders. The constraints below are not negotiable â€” they exist because each was a failure mode in past runs.

---

You are extracting reusable agent-skill frameworks from one chapter of {book_title} ({book_year}, {book_edition}).

**Your chapter:** Chapter {chapter_number} â€” {chapter_title} (book pages {book_page_start}â€“{book_page_end}, PDF pages {pdf_page_start}â€“{pdf_page_end})

**Source:** {source_path}
- For scanned PDFs: PNG files at `raw/pages/p{pdf_page_start:03d}.png` through `p{pdf_page_end:03d}.png`. Use the Read tool on each PNG path â€” this is a multimodal read, no OCR step.
- For native PDFs / EPUBs: markdown at `raw/text/c{chapter_number:02d}.md`.

**Existing skills the user already has â€” you must NOT step on these triggers:** {existing_skills_to_avoid}

## Binding constraints

These constraints are binding. Violating them invalidates your output.

1. **You may extract ONLY frameworks defined in your assigned chapter.** No reaching into later chapters even if your chapter foreshadows them. Cross-references to other chapters go in a separate "cross-references" section but are NEVER claimed as your chapter's framework.

2. **Returning zero frameworks is a valid result.** Some chapters are definitional, exemplary, or umbrella (the unifying principle for chapters you cover separately). If your chapter doesn't yield a carve-worthy framework, say so clearly and stop. Do not manufacture frameworks to pad the output.

3. **The four-test rubric is binding.** ALL FOUR tests must PASS for a CARVE verdict. Any FAIL means fold or reference, no exceptions. You may not mark a framework CARVE if any test FAILs.

4. **Anti-filler guard.** Framework names like "X-Driven Y Optimization," "Strategic Z-ing of W," "Coordinate-Elimination Through Strategic Label Placement," "Grid Relocation for Information Density," "Numerical Multifunctioning" are LLM filler. The framework's name must appear verbatim or near-verbatim in the book's chapter heads, section heads, or canonical passages. If you can't quote the book's own term for it, it's almost certainly not a distinct framework â€” fold or reference, do not carve.

## Output format

Per candidate framework:

```
FRAMEWORK: <short name â€” must appear in the book>
BOOK_QUOTE: <quote the passage where the book names this framework, with page number>
SOURCE: book pages Xâ€“Y (PDF pages Aâ€“B)
ONE_LINE: <single sentence â€” what the framework IS>
CORE_THESIS: <2â€“3 sentences in plain English, NOT in the author's prose style>
SUB_CONCEPTS: <numbered list of the framework's internal structure>
ACTIONABLE_OUTPUT: <concrete output a skill using this framework would produce. If you can't name a concrete output, this fails test #1>
FAILURE_MODES: <3â€“6 things the book warns against>

TESTS:
  decision_or_artifact: PASS/FAIL with one-line reason
  distinct_triggers: PASS/FAIL â€” write 3 example user prompts. For each, predict whether it would route HERE or to an existing skill from the "skills to avoid" list. If 2+ would route to an existing skill, this test FAILS.
  three_plus_subrules: PASS/FAIL with count
  stable_across_contexts: PASS/FAIL with one-line reason

VERDICT: carve / fold-into-<other-skill> / reference-only
REASONING: <one sentence>
```

If your chapter yields zero frameworks, return:

```
NO FRAMEWORKS CARVED FROM THIS CHAPTER.

REASON: <why â€” e.g., "this chapter is definitional/exemplary/umbrella; its content belongs as a reference doc to the parent skill family">

CROSS-REFERENCES: <list concepts this chapter discusses that are defined in other chapters; the framework belongs there, not here>

REFERENCE MATERIAL TO PRESERVE: <case studies, historical examples, quotations worth keeping>
```

## Other expectations

- Read selectively, not exhaustively. Sample the chapter intro, section heads, and key framework-definition passages. Skim historical examples / figures unless they're part of a framework's definition.
- Write the report to `outline/chapter_{chapter_number:02d}.md`.
- Length: 400â€“1200 words. Don't pad.
- Plain markdown, no JSON wrapping.
