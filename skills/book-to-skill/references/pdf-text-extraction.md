# Getting text out of a book PDF

Two paths. Pick by whether the PDF has a text layer. Both are local and key-free.

## 1. Detect which path you need

```powershell
# char count from the text layer, against page count
python -c "import fitz; d=fitz.open(r'source.pdf'); print('pages', d.page_count, 'chars', sum(len(p.get_text()) for p in d))"
```

Rule of thumb: a real text layer yields **roughly 1,500 to 3,000 chars per page**.
A few hundred bytes for a 400-page book means the PDF is **scanned images** and
`pdftotext`-style extraction will silently return almost nothing. (Natenberg's
*Option Volatility and Pricing* was exactly this: 475 pages, 0.5 KB of text.)

## 2. Text-layer PDFs: `anydoc`

[`firecrawl/anydoc`](https://github.com/firecrawl/anydoc) (MIT, Rust with Python
and Node bindings). Installed on the plain `python` on PATH (the user install; never a project venv):

```powershell
python -m pip install firecrawl-anydoc
```

```python
import anydoc
md = anydoc.to_markdown("source.pdf")     # also docx, pptx, xlsx, odf, rtf, epub, csv
```

Why prefer it over flat text extraction: it emits **GitHub-flavored Markdown with
heading structure preserved**, which is what makes chapter splitting reliable
instead of guess-the-offset. Fast: a 5.8 MB, 250-page PDF converted in ~1.1 s to
465 K chars.

CLI form: `npx @firecrawl/anydoc report.docx -o report.md`.

**Limitation, and it is the important one: anydoc handles text-based PDFs only.**
The open-source library has no OCR. (The hosted Firecrawl Parse API does, but
that needs a key, so it is out of scope here.) For a scanned PDF it produces
nothing useful, which is path 2.

## 3. Scanned PDFs: render, then Windows OCR

No tesseract install, no API key, no account. Two workspace scripts:

```powershell
# 1. rasterize (PyMuPDF). 200 dpi is enough for body text; grayscale.
python .\.agents\scripts\pdf-ocr.py source.pdf .\pages --dpi 200

# 2. OCR every page into one .txt with page markers (Windows.Media.Ocr).
#    Resumable: re-running skips pages already written.
& .\.agents\scripts\ocr-pages.ps1 -PagesDir .\pages -OutFile .\raw\source.txt
```

Output carries a `=== PAGE n ===` marker before each page, which the chunker can
use as a split anchor.

Cost and quality, measured on Natenberg (475 pages at 200 dpi): render ~2 min,
OCR ~15 min, 989 KB of text, 474 pages recognized. Quality is good enough to
carve from; expect scattered artifacts in ligatures and small caps
(`VolaÃƒÂ¼lity`, `OpÃƒÂ¼ons`), so **quote sparingly from OCR text and never
transcribe a formula from it without checking the rendered page image.**

## 4. Splitting into chunks

Verify the split **anchor**, not just proportional sizes. Past failures:

- Covel: header-vote offset was 30 pages off because it matched a running header.
- Fitschen: the offset was not even constant.

When the header vote is unstable, fall back to **equal contiguous text chunks**
(6 or 7 of them) and let the synthesis pass dedupe across the seams. Chapter
precision is not required for carving; coverage is.

Always open the first, middle, and last chunk and confirm the content matches
what you think that chapter is.
