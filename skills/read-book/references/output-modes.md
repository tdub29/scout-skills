# Output mode templates

Per-mode templates for the final aggregated `notes.md`. Each chapter chunk produces a partial in the same shape, then the aggregator combines them.

---

## notes (default)

Best for: reading nonfiction you want to refer back to.

### Per-chunk template

```markdown
### Chapter <N>: <Chapter Title>

**TL;DR**: <2â€“3 sentence summary>

**Key concepts**:
- **<concept>** â€” <1-line explanation>
- **<concept>** â€” <1-line explanation>
- (3â€“7 per chapter, no more)

**Quotes worth keeping**:
> "<verbatim quote>" (p. X)
> "<verbatim quote>" (p. Y)

**Action items / Implications**:
- <if I believed this chapter, what would I do differently?>
- <thing to try / experiment to run>

**Frameworks introduced**:
- **<Framework name>**: <1-sentence summary of the structure>

**Open questions / disagreements**:
- <where I push back or want more evidence>
```

### Full-book aggregation

```markdown
# <Book Title> by <Author>

## TL;DR
<2â€“3 sentences synthesizing the whole book>

## Key takeaways
1. <takeaway>
2. <takeaway>
3. <takeaway>
(3â€“7 total â€” the things that survive forgetting)

## Who this is for
<1 sentence>

## Verdict
<recommend? skip? read in this order with other books?>

## Chapter notes
<all per-chunk outputs concatenated>

## Cross-references (suggested for wiki)
- Could connect to [[<existing wiki page>]] (per <chapter ref>)
- Could connect to [[<existing wiki page>]] (per <chapter ref>)

## Source
- File: <path>
- Author: <author>
- Pages: <count>
- Read on: <date>
- Mode: notes
```

---

## summary

Best for: short attention, "did I miss anything important," catching up before a meeting.

### Single-pass template (no per-chunk aggregation)

```markdown
# <Book Title> by <Author> â€” Summary

**TL;DR (1 paragraph)**: <4â€“6 sentences>

**Key takeaways**:
1. <takeaway>
2. <takeaway>
3. <takeaway>
(3â€“5 total, not more)

**Who this is for**: <1 sentence>

**Should you read the whole thing?** <yes / no / just chapters X and Y>

**Source**: <path>, <author>, <pages> pages, read on <date>
```

For books over 100 pages, sample chapters (read intro + 2â€“3 random middle chapters + conclusion) rather than full chunking â€” summary doesn't justify full processing.

---

## quotes

Best for: pull-quote mining for talks, social, content drafting.

### Per-chunk template

```markdown
### Chapter <N>: <Chapter Title>

> "<verbatim quote>" â€” <attribution if not the author> (p. X)
> "<verbatim quote>" â€” (p. Y)
> "<verbatim quote>" â€” (p. Z)

(5â€“15 per chapter for quote-heavy books; 0â€“3 for sparse chapters â€” only the keepers)
```

### Full-book aggregation

```markdown
# <Book Title> by <Author> â€” Quotes

<all quotes from all chunks, grouped by chapter, with page refs>

## Source
- File: <path>
- Read on: <date>
```

No analysis, no commentary â€” pure verbatim quotes. If you want analysis, use `notes` mode.

---

## study

Best for: deep learning, books you want to retain long-term, prep for talks/teaching.

### Per-chunk template

Notes-mode output + add:

```markdown
**Spaced-repetition Q&A**:
1. **Q**: <question that tests recall of a key concept>
   **A**: <1â€“2 sentence answer>
2. **Q**: <question>
   **A**: <answer>
(2â€“4 Q&A pairs per chapter)
```

### Full-book aggregation

Notes-mode aggregation + add at the end:

```markdown
## Spaced-repetition deck (full)

<all Q&A pairs from all chapters, in order, ready to import to Anki/Mochi/RemNote>

## Suggested review cadence
- Week 1: review all Q&A daily
- Week 2-4: every other day
- After that: standard SRS schedule
```

The Q&A format makes the output directly importable to spaced-repetition apps. If the user wants Anki-importable TSV, add a `--anki` flag (one Q-tab-A per line).

---

## Notes shared across modes

- **Quote attribution**: when the author quotes someone else, the attribution goes after the quote (`â€” Andy Wilkinson`). When it's the author themselves, no attribution needed.
- **Page numbers**: always include if available. For EPUB-converted books without stable page numbers, use chapter + paragraph approximation (`Ch 3, Â¶12`).
- **Frameworks** in the `notes` mode get their own bullet because they're the most reusable â€” a framework you remember outperforms 10 ideas you forget.
- **Disagreements / pushback** in `notes` mode is mandatory if you have any. Reading critically beats reading reverently â€” surface the friction.

---

## Render to PDF / HTML (pandoc)

Triggered by `--render pdf` or `--render html` flag on the invocation. Post-processes the final `notes.md` (or `summary.md` / `quotes.md` / `study.md`) into a shareable, styled document.

### Prerequisites

```bash
# One-time
brew install pandoc                                    # required
brew install --cask basictex                           # required for PDF (smaller than full mactex)
# After basictex install, run once:
sudo tlmgr update --self && sudo tlmgr install collection-fontsrecommended
```

### Commands

```bash
# PDF
pandoc "<workdir>/notes.md" \
  --css ~/.local/share/makerskills/render.css \
  --metadata title="<book title>" \
  --pdf-engine=xelatex \
  -o "<workdir>/notes.pdf"

# HTML (standalone â€” CSS inlined into the file)
pandoc "<workdir>/notes.md" \
  --standalone \
  --embed-resources \
  --css ~/.local/share/makerskills/render.css \
  --metadata title="<book title>" \
  -o "<workdir>/notes.html"
```

The shared stylesheet at `~/.local/share/makerskills/render.css` is system-font + max-width 720px + print-optimized. Edit it freely â€” it's your file, used by `read-book` and `second-brain`.

After rendering, open:

```bash
open "<workdir>/notes.pdf"   # or notes.html
```

### When to render

- **PDF** for archive / email / print â€” looks the same on any device, no JS
- **HTML** for sharing via link (drop into a static-hosted folder) or browser viewing â€” preserves CSS, can be edited live
- Don't auto-render unless `--render` is specified â€” most book notes stay as markdown for Obsidian / second-brain capture

---

## Alternative: Quarto (`.qmd`) for richer publishing

If you ever want **executable code blocks** (Python/R/Julia analysis inline), **native citations + bibliography** (BibTeX/CSL), **multi-format publishing** (slides, websites, books â€” not just PDF/HTML), or to **turn your reading corpus into a published handbook/site**, consider [Quarto](https://quarto.org) instead of pandoc.

Tradeoff: gains rich publishing features; costs an extra tool, breaks Obsidian native rendering (wikilinks especially), adds frontmatter complexity. Skipped by default â€” see `second-brain/references/schema.md` for the full pros/cons.

For most book notes (one-off summaries, shared briefs, personal archive), **pandoc + the shared CSS above is plenty.**
