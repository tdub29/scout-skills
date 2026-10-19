---
name: book-to-skill
description: Turn a book (or a structured body of long-form thinking â€” a methodology paper, a course, a vault of notes on one thinker) into a family of reusable agent skills modeled on the schwartz-* exemplar. Use whenever the user has a book they want to "absorb into the agent," wants to make a thinker's frameworks available to Claude on demand, says things like "turn this into a skill," "I want Claude to know X," "extract the playbook from this book," "make this reusable," "carve this into skills," or hands over a PDF, EPUB, chapter notes, vault folder, or course outline and asks what to do with it. Also trigger when the user already has notes on a methodology (Cialdini, Schwartz, Halbert, Kahneman, Christensen, Munger, Hopkins, Ogilvy, Heath, Godin, Tufte, etc.) and wonders if it could become a skill, or when they ask which book they should turn into a skill next. Output is a carved family of SKILL.md bundles â€” one atomic framework per skill, schwartz-style â€” placed in the correct skill trees with the lockfile updated, plus an optional `<author>-voice` skill if the book is voice-defining. The skill orchestrates existing tools (`brainstorming`, `voice-analysis`, `skill-creator`, `llm-council`) and spawns subagents in parallel for chapter extraction, dedupe synthesis, and per-skill drafting â€” book carves are not a place for serial work.
---

# Book â†’ Skill

## Why this skill exists

The proven shape for turning a book into agent capability is **not** one giant "summary of Book X" skill. It is **a family of atomic skills, one per framework**, modeled on the `schwartz-*` set (14 skills carved from Schwartz's *Breakthrough Advertising*). That carving is the hard part â€” pick the wrong atomization and you either get one mega-skill nobody triggers correctly, or fifty trivia-skills that step on each other and on existing skills like `copywriting` and `data-visualization`. This skill codifies the carving methodology, runs the heavy stages (chapter extraction, dedupe, drafting) in parallel via subagents, and orchestrates the existing tools so the workflow is robust, not improvised every time.

A worked example exists in [`references/example-tufte-carving.md`](references/example-tufte-carving.md) â€” the full run that produced `tufte-lie-factor` and `tufte-small-multiples` and shaped the failure modes called out below.

Getting usable text out of the source PDF is its own step and has two paths (text-layer vs scanned): [`references/pdf-text-extraction.md`](references/pdf-text-extraction.md). Check which one you need BEFORE chunking; a scanned PDF silently yields near-zero text.

## When to use

Trigger when the user wants to convert structured long-form thinking into reusable agent skills. Concrete cues:

- Hands over a PDF, EPUB, chapter notes, Obsidian vault folder, or course outline
- Says "turn this into a skill," "carve this up," "I want Claude to know X," "absorb this book," "extract the playbook"
- Names a thinker/methodology and asks if it could be a skill (Cialdini, Schwartz, Halbert, Kahneman, Christensen, Munger, Hopkins, Ogilvy, Heath, Godin, Tufte, Drucker, Sutherland, Sinek, etc.)
- Has a `llm-knowledge-base/raw/<book>/` folder and wants to know what comes next
- Already produced a one-shot "book summary" skill and is unhappy that Claude never triggers it

Do **not** trigger for: turning a single blog post into a skill (too thin), turning a codebase into a skill (use the codebase's own conventions), or turning a workflow the user just demonstrated into a skill (that's `skill-creator`'s home turf â€” invoke `skill-creator` directly).

## The carving methodology

### Core thesis

A book contains 1â€“N reusable frameworks. The job is to identify each one, score it for skill-worthiness, then carve. The schwartz-* family is the canonical output: every skill stands on its own, has its own trigger contexts, produces a concrete decision or artifact, and references no other skill to function. **Atomicity beats comprehensiveness.** A skill the agent triggers correctly 80% of the time on a narrow surface beats a skill that covers the whole book but never gets invoked.

### The four-test rubric (BINDING)

A passage earns its own skill only if it passes ALL FOUR tests. Any FAIL means fold or reference. There is no "carve anyway" override â€” if you find yourself wanting one, the framework should be a `references/` doc inside a parent skill, not a peer skill of its own.

1. **Decision or artifact, not description.** The framework produces a specific output: a diagnosis, a score, a rewrite, a ranked list, a go/no-go. "Mass Desire" produces a diagnosis + headline-ready claim. "Lie Factor" produces a numerical score + a corrected redraw spec. A passage that only *explains* something (e.g., "how the brain forms habits") without telling the agent what to *do* with it is reference material, not a skill.

2. **Distinct trigger surface.** Write 5 hypothetical user prompts. Would each of them *want* to route here, or to an existing skill (`copywriting`, `frontend-design`, `data-visualization`, etc.)? If 3+ of the 5 would route to an existing skill, the candidate fails this test. Steal-from-existing is worse than fold-into-existing.

3. **Three or more sub-rules / failure modes.** A framework needs internal structure worth codifying. If the whole thing is "use scarcity in your subject lines" â€” that's a tip, not a skill. Schwartz's Mass Desire passes because it has 3 dimensions Ã— scoring + 6 failure modes + step-by-step.

4. **Stable across contexts.** The framework applies to a wide-enough surface that the agent will hit it repeatedly. "How Tufte redrew the 1976 OPEC chart" is too narrow. "Lie Factor" is broad enough to apply to any quantitative graphic in any era.

### The shape decision (family vs. one-skill vs. don't-carve)

Count CARVE verdicts after the synthesis/dedupe step:

- **â‰¥ 5 carves and they're independently triggerable** â†’ **family** of atomic skills with `<prefix>-<framework>` names (`schwartz-`, `tufte-`, `cialdini-`). Each skill stands alone.
- **2â€“4 carves, OR carves are co-dependent** â†’ **one skill with `references/` chapters.** SKILL.md holds the orchestration; each framework is a markdown file in `references/` the SKILL.md reads on demand.
- **0â€“1 carves** â†’ **don't carve.** Write a single SKILL.md plus a `references/` of book notes, OR (more honest) recommend the user keep the book content as a knowledge-base doc and skip the skill conversion entirely.

When in doubt, prefer the family shape â€” atomic skills trigger more reliably and don't blow context loading reference files the user didn't need.

### Umbrella chapters (a special case)

Some chapters present the *unifying principle* for what other chapters individually cover (Tufte's Ch 7 "Multifunctioning Graphical Elements" is the unifying principle behind Chs 4â€“6). Umbrella chapters always overlap with their member chapters and always fail the distinct-trigger test. **Route umbrella chapters to a parent reference doc**, not to a peer skill. The synthesis step is responsible for spotting these.

## Workspace layout (required)

Every run produces this structure. Future re-runs depend on it:

```
book-to-skill-workspace/<book-slug>/
â”œâ”€â”€ raw/
â”‚   â”œâ”€â”€ source.pdf           # or source.epub, source.md
â”‚   â”œâ”€â”€ pages/p001.png ...   # rendered if scanned PDF (one per page)
â”‚   â””â”€â”€ text/c01.md ...      # extracted markdown if native PDF/EPUB
â”œâ”€â”€ chapter_map.json         # {"1": {"title": "...", "pdf_pages": [10, 49], "book_pages": [13, 52]}, ...}
â”œâ”€â”€ outline/
â”‚   â”œâ”€â”€ chapter_01.md ...    # one subagent report per chapter
â”‚   â””â”€â”€ synthesis.md         # dedupe + carving plan after synthesis subagent runs
â””â”€â”€ drafts/<skill-name>/     # carved SKILL.md drafts (move to skills/ when complete)
```

## How to apply (step-by-step)

### Step 1 â€” Brainstorm intent

Invoke `brainstorming` to clarify:

- What book and what edition? (Editions matter â€” chapter numbering shifts.)
- Source format: native PDF / scanned PDF / EPUB / markdown notes / Obsidian vault / course outline
- What's the agent supposed to *do* with the book? Output type decides which passages pass the 4-test rubric.
- Existing skills that might overlap (run the user's `skills/` directory through grep for adjacent domains)
- Where do the skills live? Default per workspace `CLAUDE.md`: canonical in `skills/`, mirror to `.agents/skills/` and `.claude/skills/`, update `skills-lock.json`.

### Step 2 â€” Ingest the source

Produce per-chapter readable content. **Strategy depends on the source â€” pick the right path:**

- **Native PDF with selectable text:**
  - Try `pdftotext -layout source.pdf source.txt` first; verify non-zero output.
  - If non-empty: split into per-chapter markdown using the TOC.
  - If empty: the PDF is scanned-image-only â€” go to the scanned-PDF path.
  - Alternative: `tanis90/pdf-converter-mineru@pdf-converter` (registry skill â€” install via `npx skills add tanis90/pdf-converter-mineru@pdf-converter -g -y`) for layout-aware extraction of multi-column / table-heavy books.

- **Scanned-image PDF (no extractable text):** This is the case for many OceanofPDF and older-edition PDFs. The correct path:
  ```python
  import fitz
  doc = fitz.open("source.pdf")
  for i in range(doc.page_count):
      doc[i].get_pixmap(dpi=140).save(f"raw/pages/p{i+1:03d}.png")
  ```
  Then chapter subagents read PNGs directly via the multimodal Read tool. **Do not OCR with tesseract first** â€” Claude's multimodal read preserves visual layout (figure captions, marginalia, multi-column flow) better than OCR + plain text. Install PyMuPDF if needed: `pip install pymupdf`.

- **EPUB:** `pandoc source.epub -o source.md --wrap=none`, then split by H1/H2.

- **Obsidian / markdown notes:** read the folder; merge by chapter. Watch for cross-links â€” they tell you which concepts the user already groups together.

- **The user's own summary:** treat as authoritative for what they care about. Their summary is already a filter; carve from it rather than re-reading the whole book.

### Step 3 â€” Map chapters to source pages

Produce `chapter_map.json`. For native sources this comes from the TOC parser. For scanned PDFs, spawn ONE small subagent that:

1. Reads the TOC page (typically PDF pages 3â€“8) to find the chapter list with book-page numbers.
2. Spot-checks PDF pages around the predicted offset (book page + ~12 to +14 is typical for trade-paperback PDFs).
3. Returns `chapter_map.json` with PDF-page bounds per chapter.

This eliminates manual probing on every run.

### Step 4 â€” Chapter subagents in parallel (subagent step #1)

Spawn N chapter subagents in parallel (N = number of chapters). Each gets:

- Path to its assigned PNG / markdown range
- The four-test rubric (binding â€” see above)
- The anti-filler guard (see below)
- The "existing skills to avoid stealing triggers from" list
- The output format (one markdown report per chapter into `outline/chapter_NN.md`)

Use the bundled prompt template at [`assets/chapter-subagent-prompt.md`](assets/chapter-subagent-prompt.md). Substitute `{chapter_number}`, `{chapter_title}`, `{page_range}`, `{existing_skills_to_avoid}`.

**Critical constraints in the subagent prompt:**

- **"You may extract ONLY frameworks defined in your assigned chapter."** No reaching into later chapters even if the book foreshadows them. Cross-references to other chapters are noted in a separate "cross-reference" section but never claimed as your chapter's framework.
- **"Returning zero frameworks for this chapter is a valid result."** Some chapters are definitional, exemplary, or umbrella; they don't yield carve-worthy frameworks. Don't manufacture frameworks to pad the output.
- **"ALL FOUR tests must PASS for a CARVE verdict. Any FAIL means fold or reference, no exceptions."** The rubric is binding.

**Anti-filler guard (in the subagent prompt):** Framework names like "X-Driven Y Optimization," "Strategic Z-ing of W," "Z Relocation for Y," or "Multi-functional A Through B" are LLM filler. The framework's name must appear verbatim or near-verbatim in the book's chapter heads, section heads, or key phrases. If you can't quote the book's own term for it, the framework probably isn't a distinct framework â€” fold or reference.

### Step 5 â€” Synthesis subagent: dedupe and decide shape (subagent step #2)

Spawn ONE synthesis subagent that reads ALL of `outline/*.md` and produces `outline/synthesis.md` containing:

1. **Master inventory table** â€” one row per unique framework with:
   - Framework name
   - Canonical chapter (where it's *defined*, not where it's first mentioned)
   - All chapters that cited it
   - Verdict (CARVE / fold / reference)

2. **Deduplication notes** â€” for each duplicate, name the chapter the framework belongs to canonically. Example: "Lie Factor â€” extracted by Ch 1, 2, 3 subagents. Canonical: Ch 2 (where the formula appears on page 57). Ch 1 reference is foreshadowing; Ch 3 reference is application."

3. **Ruthless borderline-folding** â€” for every CARVE marked "borderline," the synthesis subagent must explicitly defend why it shouldn't fold. Default is to fold.

4. **Umbrella-chapter detection** â€” chapters that overlap heavily with multiple member chapters get routed to a parent reference doc, not a peer skill.

5. **Shape decision** â€” apply the â‰¥5/2â€“4/0â€“1 thresholds.

6. **`llm-council` pressure-test** â€” recommended (optional) call for the synthesis subagent to invoke `llm-council` on the borderline carves, with the prompt: "is this really a reusable skill, or is it a paraphrased chapter?" If 2+ councilors flag it as a paraphrase, fold.

The synthesis subagent gets the bundled prompt at [`assets/synthesis-subagent-prompt.md`](assets/synthesis-subagent-prompt.md).

### Step 6 â€” Per-skill drafting in parallel (subagent step #3)

Once `synthesis.md` lists the final carved frameworks, spawn ONE drafting subagent per carved skill (in parallel). Each gets:

- Framework name + canonical chapter + page range
- Path to the source markdown / PNGs for the chapter
- The bundled skill template at [`assets/skill-template.md`](assets/skill-template.md) (mirrors schwartz-* anatomy)
- The list of sibling carved skills, so the References section can link to them
- An instruction to write the draft to `drafts/<skill-name>/SKILL.md`

**Subagent type matters.** Use `subagent_type: general-purpose` (or `claude`) for drafting subagents â€” they need Write access to produce the SKILL.md file. **Do NOT use `Explore`** â€” that subagent type is read-only and will return the SKILL.md as text in the tool result instead of writing it, which defeats the parallelism. (The Step 4 chapter-extraction subagents can stay on `Explore` because they only produce markdown reports as their return text, not files on disk.)

**Batching for token economy.** For books that yield >5 carved skills, consider batching drafts 2â€“3 at a time rather than firing all in parallel. Anthropic session token limits and parallel-subagent token economics can make a fully-parallel fan-out expensive â€” and for some users, a serial orchestrator-driven draft is actually cheaper. Judge by skill count and the user's stated budget.

The drafting subagents do NOT run skill-creator's full eval loop â€” that's heavy and shouldn't fire many times in parallel. If the user wants per-skill eval iteration after the draft lands, they can invoke `skill-creator` on the specific skill later.

### Step 7 â€” Optional voice capture

If the book *is* the voice (Schwartz, Halbert, Hopkins, Ogilvy, Sutherland â€” i.e., the author's style is part of why the user loves the book), invoke `voice-analysis` separately with 5â€“10 peak-voice excerpts. Output is a separate `<author>-voice` skill the user invokes when drafting in that author's style. This is independent of the framework carves.

### Step 8 â€” Place, mirror, and lock

For each carved SKILL.md:

1. Move from `drafts/<skill-name>/` to `skills/<skill-name>/` (canonical).
2. Mirror byte-identical to `.agents/skills/<skill-name>/` and `.claude/skills/<skill-name>/`.
3. Compute SHA-256 of the canonical bundle. Add a lockfile entry alphabetically:
   ```json
   "<skill-name>": {
     "source": "local/book-to-skill",
     "sourceType": "local",
     "book": "<Author> â€” <Title> (<year>, <edition>), <chapter ref>",
     "computedHash": "<sha256>"
   }
   ```
   The `"book":` field is required for book-derived skills â€” it's the provenance that makes the carve traceable back to source.

4. **Companion linkage check.** Each carved SKILL.md's References section must link to:
   - The source book (full citation)
   - Sibling carved skills in the same family (`tufte-data-ink-ratio` references `tufte-chartjunk` and `tufte-small-multiples`, etc.)
   - The parent reference doc if one exists (`tufte-graphical-excellence-reference.md`)

   The drafting subagent template handles this; verify before placing.

## Common failure modes

- **One mega-skill per book.** The instinct is "the book is one thing, the skill should be one thing." This produces a skill with a 600-word description that triggers on everything and decides nothing. Carve. The schwartz-* family is 14 skills for a reason â€” each one fires on a specific user moment.

- **Triggering overlap with existing skills.** New `<author>-headlines` skill that competes with the user's existing `copywriting`. Now `copywriting` triggers less and `<author>-headlines` triggers in the wrong contexts. Resolution: the 4-test rubric's `distinct_triggers` test catches this â€” write 5 hypothetical prompts and check. If 3+ would route to an existing skill, fold the content into that skill as a `references/<author>.md` file instead.

- **Skills that explain instead of decide.** A skill that reads like a chapter summary. Triggers correctly, then outputs a wall of text. Users skip it next time. Every skill must end with the agent producing a *thing*: a score, a ranked list, a rewrite, a go/no-go, a diagnosis, a checklist filled out. If you can't name the artifact in one sentence, the framework didn't pass test #1.

- **Carving along chapter boundaries instead of framework boundaries.** Books are organized for narrative; skills are organized for triggering. A single chapter often contains two frameworks (one early, one late) and a single framework often spans three chapters. Synthesis is where chapter-blind output gets reconciled.

- **Cross-chapter duplicate extraction.** Multiple chapter subagents identify the same framework because Tufte/Schwartz/etc. foreshadow concepts across chapters. The synthesis subagent's job is to dedupe and assign each framework to its canonical chapter. Without that step, the carving list double- or triple-counts.

- **Subagents overriding the rubric.** Subagents will sometimes mark a framework CARVE despite failing one of the four tests. Treat this as a bug, not a judgment call. The rubric is binding. If the synthesis subagent sees an "override CARVE," it must downgrade to fold or reference.

- **LLM filler framework names.** "Coordinate-Elimination Through Strategic Label Placement" is not a Tufte framework â€” it's a model paraphrase. Real frameworks have names the book uses verbatim (Lie Factor, Chartjunk, Small Multiples, Data-Ink Ratio). The anti-filler guard in the subagent prompt catches most of these; the synthesis step catches the rest.

- **Manufacturing frameworks to fill an umbrella chapter.** Chapter 7 of Tufte ("Multifunctioning Graphical Elements") is a unifying principle for chapters 4â€“6, not a source of standalone frameworks. The Tufte test produced one weak forced-carve and one ambiguous CARVE from this chapter, both of which the synthesis step should have downgraded to a parent reference doc. Subagents working blind don't recognize umbrella chapters; synthesis does.

- **Forcing voice into every framework skill.** Voice belongs in its own `<author>-voice` skill. Framework skills should be agent-readable instructions, not impersonations. If the SKILL.md is full of "as Tufte would sayâ€¦" â€” strip it. Voice and method are different tools.

- **Skipping the synthesis/dedupe step.** The biggest single failure mode if subagents are used. Each chapter subagent works blind; without synthesis the carving list has 30% duplicates. Synthesis is not optional.

- **Mirror drift.** Edit the canonical `skills/<name>/SKILL.md`, forget to mirror to `.agents/skills/` and `.claude/skills/`, lockfile hash gets stale. Future runs see different content depending on which tool loaded the skill. After every edit, mirror and recompute the hash in the same turn â€” don't defer.

- **Burning through subagents on a short book.** A 12-chapter book gets 12+ chapter subagents + 1 synthesis + N drafting subagents. That's 20+ subagents per run. For books under ~80 pages with 3â€“5 chapters, consider serial single-pass extraction by the parent agent â€” the parallelism overhead exceeds the time savings.

- **Skipping the worked example.** [`references/example-tufte-carving.md`](references/example-tufte-carving.md) records the exact failures this skill was rewritten to fix. Re-read it before a new book carve â€” it will save the same failures from happening again.

## References

- [`references/example-tufte-carving.md`](references/example-tufte-carving.md) â€” the Tufte test run that shaped this skill (workspace, subagent outputs, synthesis, and the 15 critique findings).
- [`assets/chapter-subagent-prompt.md`](assets/chapter-subagent-prompt.md) â€” template for chapter extraction subagents.
- [`assets/synthesis-subagent-prompt.md`](assets/synthesis-subagent-prompt.md) â€” template for the dedupe / shape-decision synthesis subagent.
- [`assets/skill-template.md`](assets/skill-template.md) â€” schwartz-style SKILL.md template for each carved skill.
- `~/.claude/skills/schwartz-mass-desire/SKILL.md` â€” exemplar carved skill (audit/diagnosis flavor).
- `~/.claude/skills/tufte-lie-factor/SKILL.md` â€” exemplar carved skill (quantitative-metric flavor).
- `~/.claude/skills/tufte-small-multiples/SKILL.md` â€” exemplar carved skill (design-pattern flavor).
- `~/.claude/skills/voice-analysis/SKILL.md` â€” used in Step 7 for voice-defining authors.
- `~/.claude/skills/brainstorming/SKILL.md` â€” required preamble in Step 1.
- `~/.claude/skills/llm-council/SKILL.md` â€” optional borderline-carve pressure-test in Step 5.
