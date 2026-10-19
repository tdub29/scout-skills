# PdfCraft CLI and MCP server (optional engine)

Source: https://github.com/storytold/pdfcraft (repo was renamed from `storytold/printcraft`),
commit `07df4de63d88f0a7d97001f2b6fb0d4cfdf19f3b`, release v0.6.0. MIT OR Apache-2.0
(see `pdfcraft-license/`). Pure-Rust PDF engine with one JSON-Schema tool table exposed three ways:
`pdfcraft-cli run`, an opt-in stdio MCP server, and a Rust API.

## When to reach for it instead of pymupdf

Plain `python` already has `pymupdf` (render, text, merge, split, rotate, basic annotations, widgets).
Stay there by default. PdfCraft earns a call only for:

- Editing **existing** text in place with font matching (`text_edit`, `text_edit_layout`, `text_font_import`).
- Edits that must keep **signed PDFs valid**: `doc_save` to the same path appends an incremental update and writes atomically.
- Form **authoring** with batch, atomic, undoable property edits (`form_set_props` with `fields: [...]`), field detection, data exchange.
- Accessibility review before/after (`accessibility_review_record`), calibrated measurements with CSV export, redaction and sanitizing, OCR.
- Handing a PDF workbench to an agent as MCP tools with undo/redo and path confinement (`--root`).

## Install (not installed on this machine)

Key-free, no account. Windows release assets ship `pdfcraft-cli.exe` beside the app:

- Portable: `pdfcraft-<ver>-windows-x64-portable.zip` from https://github.com/storytold/pdfcraft/releases/latest (verify against `SHA256SUMS.txt`). Settings stay in `PdfCraftData` next to the exe.
- MSI: installs to `C:\Program Files\PdfCraft\pdfcraft-cli.exe`, NOT on PATH, needs admin.

Check: `pdfcraft-cli --version`. If absent, use pymupdf and say so; do not build from source (Rust 1.95+, OCR models via `cargo xtask models`).

## CLI

```sh
pdfcraft-cli info  form.pdf                                   # structure as JSON
pdfcraft-cli text  paper.pdf --page 3                         # reading-order text
pdfcraft-cli edit  in.pdf --rotate 1,2:90 --delete 5 --title "Q3" --out out.pdf
pdfcraft-cli combine report.pdf appendix.pdf --out combined.pdf
pdfcraft-cli extract report.pdf --pages 1,3,5 --out highlights.pdf
pdfcraft-cli split   report.pdf --every 10 --out-dir parts/
pdfcraft-cli tools                                            # every tool + JSON Schema (source of truth)
pdfcraft-cli run text_find doc=1 query=invoice                # key=value; values parse as JSON
pdfcraft-cli run --script steps.json --root ./work            # several steps in one session
```

A script step like `comment_add {"type": "highlight", "find": "total due"}` highlights by search text.

## MCP server

Opt-in, stdio only, no port, stops on EOF. Always pass `--root`; use `--compact` to keep `tools/list`
to about ten core tools plus `tool_search` / `tool_call` (every tool still callable).

```sh
claude mcp add pdfcraft -- "C:\path\to\pdfcraft-cli.exe" mcp --root <dir> --compact
```

Common tools: `command_list {doc?, filter?}`, `command_run {id, params?}`,
`command_batch {steps, stop_on_error?}`, `doc_inspect {doc?}`, `render_preview {doc?, page?, max_side?}`.
Resources: `pdfcraft://document`, `pdfcraft://commands`, `pdfcraft://doc/{doc}/page/{page}/image{?dpi}`.

## Conventions that bite

- Tool names are `snake_case`; pages are **1-based**; rectangles are PDF points with a **top-left** origin (pymupdf also uses top-left; raw PDF space is bottom-left).
- Unknown top-level argument keys are refused (`-32602`), so typos fail loudly.
- Edits live in memory, undoable, until `doc_save`. `doc_close` refuses unsaved changes unless `discard_changes: true`.
- With `--root`, any path outside it gets one identical refusal; UNC and device paths are refused without contact.
- `command_batch` stops at the first error by default and keeps earlier edits.
- The desktop-app control channel (`pdfcraft --control <file>` + `pdfcraft-cli ui ...`) drives the GUI over loopback with a token file. Do not use it for headless work; the tool table covers every engine feature.
