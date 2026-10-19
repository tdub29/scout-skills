---
name: document-processing
description: Use when working with "PDF", "Excel", "Word", "PowerPoint", "XLSX", "DOCX", "PPTX", "spreadsheets", "presentations", "extract text", "merge documents", "convert documents", or asking about "office document manipulation"
version: 1.0.0
---

# Document Processing Guide

Work with office documents: PDF, Excel, Word, and PowerPoint.

---

## Format Overview

| Format | Extension | Structure | Best For |
|--------|-----------|-----------|----------|
| **PDF** | .pdf | Binary/text | Reports, forms, archives |
| **Excel** | .xlsx | XML in ZIP | Data, calculations, models |
| **Word** | .docx | XML in ZIP | Text documents, contracts |
| **PowerPoint** | .pptx | XML in ZIP | Presentations, slides |

**Key concept**: XLSX, DOCX, and PPTX are all ZIP archives containing XML files. You can unzip them to access raw content.

---

## PDF Processing

### PDF Tools

| Task | Best Tool |
|------|-----------|
| Basic read/write | pypdf |
| Text extraction | pdfplumber |
| Table extraction | pdfplumber |
| Create PDFs | reportlab |
| Text layer to Markdown | anydoc (`anydoc.to_markdown(path)`), keeps headings |
| OCR scanned PDFs | `.agents/scripts/pdf-ocr.py` renders pages, `.agents/scripts/ocr-pages.ps1` reads them |

On this machine `pdftotext`, `pdftoppm`, `qpdf` and `tesseract` are not installed. Pick the path by
chars per page from PyMuPDF (`fitz`): roughly 1,500 to 3,000 means a text layer (anydoc or
pdfplumber); a few hundred for the whole file means scanned (pdf-ocr.py, then ocr-pages.ps1, both
key-free). Detail: `skills/book-to-skill/references/pdf-text-extraction.md`.

### Common Operations

| Operation | Approach |
|-----------|----------|
| **Merge** | Loop through files, add pages to writer |
| **Split** | Create new writer per page |
| **Extract tables** | Use pdfplumber, convert to DataFrame |
| **Rotate** | Call `.rotate(degrees)` on page |
| **Encrypt** | Use writer's `.encrypt()` method |
| **OCR** | Render with pdf-ocr.py, then OCR with ocr-pages.ps1 |

---

## Excel Processing

### Excel Tools

| Task | Best Tool |
|------|-----------|
| Data analysis | pandas |
| Formulas & formatting | openpyxl |
| Simple CSV | pandas |
| Financial models | openpyxl |

### Critical Rule: Use Formulas

| Approach | Result |
|----------|--------|
| **Wrong**: Calculate in Python, write value | Static number, breaks when data changes |
| **Right**: Write Excel formula | Dynamic, recalculates automatically |

### Financial Model Standards

| Convention | Meaning |
|------------|---------|
| Blue text | Hardcoded inputs |
| Black text | Formulas |
| Green text | Links to other sheets |
| Yellow fill | Needs attention |

### Common Formula Errors

| Error | Cause |
|-------|-------|
| #REF! | Invalid cell reference |
| #DIV/0! | Division by zero |
| #VALUE! | Wrong data type |
| #NAME? | Unknown function name |

---

## Word Processing

### Word Tools

| Task | Best Tool |
|------|-----------|
| Text extraction | pandoc |
| Create new | python-docx or docx-js |
| Simple edits | python-docx |
| Tracked changes | Direct XML editing |

### Document Structure

| File | Contains |
|------|----------|
| `word/document.xml` | Main content |
| `word/comments.xml` | Comments |
| `word/media/` | Images |

### Tracked Changes (Redlining)

| Element | XML Tag |
|---------|---------|
| Deletion | `<w:del><w:delText>...</w:delText></w:del>` |
| Insertion | `<w:ins><w:t>...</w:t></w:ins>` |

**Key concept**: For professional/legal documents, use tracked changes XML rather than replacing text directly.

---

## PowerPoint Processing

### PowerPoint Tools

| Task | Best Tool |
|------|-----------|
| Text extraction | markitdown |
| Create new | pptxgenjs (JS) or python-pptx |
| Edit existing | Direct XML or python-pptx |

### Slide Structure

| Path | Contains |
|------|----------|
| `ppt/slides/slide{N}.xml` | Slide content |
| `ppt/notesSlides/` | Speaker notes |
| `ppt/slideMasters/` | Master templates |
| `ppt/media/` | Images |

### Design Principles

| Principle | Guideline |
|-----------|-----------|
| Fonts | Use web-safe: Arial, Helvetica, Georgia |
| Layout | Two-column preferred, avoid vertical stacking |
| Hierarchy | Size, weight, color for emphasis |
| Consistency | Repeat patterns across slides |

---

## Converting Between Formats

| Conversion | Tool |
|------------|------|
| Any â†’ PDF | LibreOffice headless (not installed on this machine) |
| PDF â†’ Images | PyMuPDF `page.get_pixmap()`, or pdf-ocr.py |
| DOCX â†’ Markdown | pandoc |
| Any â†’ Text | Appropriate extractor |

---

## Best Practices

| Practice | Why |
|----------|-----|
| Use formulas in Excel | Dynamic calculations |
| Preserve formatting on edit | Don't lose styles |
| Test output opens correctly | Catch corruption early |
| Use tracked changes for contracts | Audit trail |
| Extract to markdown for analysis | Easier to process |

## Common Packages

| Language | Packages |
|----------|----------|
| **Python** | pypdf, pdfplumber, openpyxl, python-docx, python-pptx |
| **JavaScript** | docx, pptxgenjs |
| **CLI** | pandoc, `npx @firecrawl/anydoc` |
