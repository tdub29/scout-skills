# book-to-skill pipeline critique â€” Tufte test run

Test input: *The Visual Display of Quantitative Information* (Tufte, 2001, 2nd ed.), 191 pages, **scanned-image-only PDF**.

Pipeline output: 7 carve-worthy frameworks identified (master inventory below); 2 written as proof-of-pipeline (`tufte-lie-factor`, `tufte-small-multiples`).

## What worked

- **Workspace layout was sensible.** `book-to-skill-workspace/<book-slug>/raw/pages/p*.png` is a clean place for the rendered source.
- **Chapter subagents in parallel.** 9 subagents ran simultaneously, total wall time â‰ˆ 60s vs. ~10 minutes serial. Output quality on the strong chapters (Ch 2, 4, 5, 8, 9) was production-quality.
- **The 4-test rubric did its job when subagents respected it.** The Ch 6 subagent correctly *failed* "Erase Non-Data Ink" on the `distinct_triggers` test and folded it into `tufte-data-ink-ratio`. Exactly the dedupe behavior the rubric is designed to force.
- **The schwartz-* anatomy holds up.** The two written skills follow the same shape and read as standalone, triggerable, decision-producing skills. The template generalizes.

## What broke â€” 15 findings

### Critical (pipeline doesn't work without fixing these)

**F1. Scanned-PDF fallback was wrong.** SKILL.md said "OCR offline." Reality: the best path is `PyMuPDF render â†’ PNG â†’ multimodal Read`. Tesseract loses layout; Claude's native multimodal read preserves it. The skill needs an explicit scanned-book path with the render script bundled.

**F2. No page-offset mapping step.** I had to manually probe PDF pages 10/25/50/67 to find that `book_page = pdf_page + 3`. Every Tufte run would repeat this. The skill needs a TOC-mapping pass that produces `chapter_map.json` *before* chapter subagents are dispatched.

**F3. No cross-chapter dedupe / synthesis step.** Chapter subagents identified the Lie Factor 3Ã— (Ch 1, 2, 3) and Data-Ink Ratio 4Ã— (Ch 1, 4, 5, 6). Each subagent worked blind. The skill specified Step 4 (scoring) and Step 5 (decide shape) but no step that *consolidates* across chapters. Without it the carving list has duplicates.

**F4. Rubric enforcement is not enforced.** Ch 7 subagent marked "Coordinate-Elimination" as CARVE despite failing `stable_across_contexts`. The skill said the four tests are required but didn't make this binding. Need explicit: "ALL four tests must PASS. Any FAIL â†’ fold or reference. No judgment override."

**F5. No subagent usage in the skill.** User flagged this directly â€” the skill is currently described as sequential. It needs to specify subagent parallelization at three points: (a) chapter outline extraction, (b) synthesis/dedupe, (c) per-skill drafting.

### Important (degrades output quality)

**F6. No anti-filler guard.** Ch 7 subagent invented framework names like "Coordinate-Elimination Through Strategic Label Placement" and "Grid Relocation for Information Density" that read like LLM filler rather than Tufte's own terms. The skill needs a red-flag list and a requirement that framework names appear in or near-verbatim from the book.

**F7. Each subagent reached outside its chapter.** Ch 1 extracted Lie Factor (defined in Ch 2) and Data-Ink Ratio (defined in Ch 4). Forgivable because Tufte foreshadows these, but it caused duplicates. Subagent prompts need a stricter bound: "you may *reference* concepts defined elsewhere but you may NOT extract them as your chapter's frameworks."

**F8. Permission to return zero frameworks wasn't explicit.** Ch 7 strained to produce three frameworks where probably only zero or one belonged. The skill needs "zero-framework return is a valid result" as a first-class verdict in the subagent template.

**F9. Umbrella-chapter handling is missing.** Ch 7 ("Multifunctioning Graphical Elements") is the *unifying principle* for what Chs 4â€“6 individually cover. Umbrella chapters always overlap with their member chapters and always fail the distinct-trigger test. The skill should detect umbrella chapters and route them to a parent reference doc, not to a peer skill.

**F10. Borderline carves drift toward over-carving.** Ch 6 subagent flagged Range-Frame Design and Dot-Dash Plot as borderline/CARVE. Both are probably better folded into `tufte-data-ink-ratio` as referenced techniques. The synthesis step needs an explicit "ruthlessly fold borderlines" rule.

### Polish (nice-to-have)

**F11. Subagent prompt template wasn't bundled.** I wrote 9 chapter prompts by hand. Should live in `assets/chapter-subagent-prompt.md` as a template with `{chapter_number}`, `{chapter_title}`, `{page_range}`, `{existing_skills_to_avoid}` placeholders.

**F12. Workspace layout wasn't specified.** Created ad hoc. Should be:
```
book-to-skill-workspace/<book-slug>/
â”œâ”€â”€ raw/
â”‚   â”œâ”€â”€ source.pdf           # or source.epub, source.md
â”‚   â”œâ”€â”€ pages/p001.png ...   # rendered if scanned
â”‚   â””â”€â”€ text/c01.md ...      # extracted if native
â”œâ”€â”€ chapter_map.json         # chapter â†’ PDF/page mapping
â”œâ”€â”€ outline/
â”‚   â”œâ”€â”€ chapter_01.md        # subagent reports
â”‚   â””â”€â”€ synthesis.md         # dedupe + carving plan
â””â”€â”€ skills/<skill-name>/     # carved drafts before they move to skills/
```

**F13. Lockfile convention for book-derived skills wasn't defined.** Each entry should include a `"book":` field with author, title, edition, chapter. I added this manually for the two Tufte skills.

**F14. Companion-skill linkage wasn't required.** A family of skills should cross-reference. I added References sections to both Tufte skills by hand; the skill template should require it.

**F15. The family-vs-one-skill threshold was fuzzy.** "5 or more survivors" was a heuristic. Should formalize: â‰¥5 carves â†’ family; 2â€“4 â†’ one-skill-with-references; 0â€“1 â†’ don't carve, write a single SKILL.md plus a `references/` of book notes.

## Master framework inventory (after dedupe)

| Framework | Canonical Ch. | Verdict | Carved? |
|---|---|---|---|
| Lie Factor | Ch 2 | **CARVE** | âœ“ written |
| Six Principles of Graphical Integrity | Ch 2 | **CARVE** | pending |
| Data-Ink Ratio (incl. Ch 6 erasure techniques) | Ch 4+6 | **CARVE** | pending |
| Chartjunk (vibrations, grids, ducks) | Ch 5 | **CARVE** | pending |
| Small Multiples | Ch 8 | **CARVE** | âœ“ written |
| Data Density | Ch 8 | **CARVE** | pending |
| Aspect Ratio / Proportion | Ch 9 | **CARVE** | pending |
| Line-Weight Hierarchy | Ch 9 | borderline | likely fold into aspect ratio |
| Range-Frame Design | Ch 6 | borderline | fold into data-ink ratio |
| Multifunctioning Elements | Ch 7 | **REFERENCE** | umbrella â†’ parent ref doc |
| Graphical Excellence Principles | Ch 1 | **REFERENCE** | definitional â†’ parent ref doc |

## What this means for the skill

The book-to-skill SKILL.md gets rewritten with the 15 findings baked in. The two big structural additions are (a) explicit subagent parallelization at three checkpoints, and (b) a synthesis/dedupe step between chapter extraction and carving. Plus bundled assets so future runs aren't ad hoc.

---

## Second-pass test (drafting the remaining 5 skills) â€” finding #16 added

After the SKILL.md rewrite, the pipeline was re-tested on the remaining 5 Tufte carves by spawning 5 drafting subagents in parallel (one per skill). Outcome: **3 hit the Anthropic session token limit and returned no output; 2 completed but their SKILL.md content came back as text in the tool result rather than written to disk.**

**F16. Explore subagents cannot write files.** The `Explore` subagent type is documented as read-only (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit). Step 6 of the pipeline (per-skill drafting) requires Write access. Using `Explore` for drafting forced the subagent to embed the SKILL.md content in its return text â€” which then needs the orchestrator to extract and write, defeating the parallelism benefit. **Fix:** drafting subagents must use `subagent_type: general-purpose` (or `claude`), not `Explore`. The chapter extraction subagents in Step 4 can stay on `Explore` because they only need Read access â€” they produce reports as text, not files.

This is now reflected in the SKILL.md Step 6 instructions.

**F17 (context, not a skill change).** Long-running parallel drafting subagents can hit Anthropic session token limits when drafting many SKILL.md files at once. For books that yield >5 carved skills, batch drafts (2â€“3 at a time) rather than firing all in parallel â€” or have the orchestrator draft serially. Token economics may favor the orchestrator over fan-out for some user budgets.

## Final Tufte family inventory (after both passes)

7 skills carved, all written and mirrored:

1. **tufte-lie-factor** (Ch 2) â€” quantitative metric for proportionality
2. **tufte-graphical-integrity-principles** (Ch 2) â€” six-principle audit checklist
3. **tufte-data-ink-ratio** (Ch 4 + 6) â€” structural-ink optimization
4. **tufte-chartjunk** (Ch 5) â€” decorative-noise elimination
5. **tufte-data-density** (Ch 8) â€” efficiency principle
6. **tufte-small-multiples** (Ch 8) â€” design pattern for cross-category comparison
7. **tufte-aspect-ratio** (Ch 9) â€” proportion + line-weight hierarchy

Folded as sub-rules: range-frame design (into data-ink-ratio), dot-dash plot (into data-ink-ratio), line-weight hierarchy (into aspect-ratio), causal-axis emphasis (into aspect-ratio).

Reference-only (not yet drafted as parent doc): graphical excellence principles (Ch 1), multifunctioning elements (Ch 7). Future work if needed.
