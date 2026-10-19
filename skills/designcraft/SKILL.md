---
name: designcraft
description: Drive DesignCraft, the open-source InDesign-style page layout app, from an agent over its CLI, MCP server or JSON control channel. Use when laying out print pages, magazines, flyers, brochures or books with frames, threaded text, paragraph styles, swatches and data merge, or converting IDML, DOCX or CSV into PDF/X-4, PDF/A, PNG or EPUB output.
---

# DesignCraft

DesignCraft (github.com/storytold/designcraft, MIT OR Apache-2.0) is a clean-room Rust reimplementation
of the Adobe InDesign workflow. Every menu item, tool and dialog is a command, so an agent can lay out a
document and look at the rendered page. Upstream ships no skill; this one routes its agent docs.

## When to reach for it

- Print-grade layout: real text in PDF with subset fonts, PDF/X-4, PDF/A-2b, CMYK and spot colors, bleed.
- Typography HTML and Typst do not do well: Knuth-Plass paragraph composition, hyphenation, baseline grid.
- Data merge from CSV/TSV/xlsx into a template, producing a new merged document.
- IDML in or out (the only route back to InDesign). `.indd` cannot be opened yet: ask for IDML.

Not for web UI, slides or charts. For a quick PDF from markdown, Typst or Pandoc on PATH is cheaper.

## Get the binary first (it is not installed here)

Use a release, never a source build of an untrusted checkout: `gh release list -R storytold/designcraft`.
The Windows MSI installs `C:\Program Files\DesignCraft\designcraft-cli.exe`, not on PATH. Installing an MSI
is a machine change: confirm with Trevor before running it.

## Pick a surface

| Surface | Use for | Command |
|---|---|---|
| CLI | one-shot builds, pipelines, export | `designcraft-cli run`, `script`, `commands`, `describe` |
| MCP | Claude sees rendered pages as images | `claude mcp add designcraft -- "<path>\designcraft-cli.exe" mcp` |
| Control channel | drive the running app live | `designcraft --control 7979`, then `designcraft-cli app ...` or `mcp --connect 7979` |

## Working loop

1. Discover: `designcraft-cli commands <word>` then `describe <command.id>` for its params.
2. Build with a script (`command.id {json}` per line); `"$N.path"` reuses step N's result (ids, stories).
3. Look: `render_page` (MCP) or `run ... --export page.png`, and check `inspect_document` for overset text.
4. Export: `--save x.designcraft --export x.pdf`.

## Traps

- Coordinates are points, y down, in spread space; a facing spread's right page starts at x = page width.
- Text offsets are UTF-8 byte offsets, not characters (an em dash is 3 bytes).
- Manual threading between drawn frames is missing (no `frame.thread` command): flow long text with autoflow.
- A failed connected-mode request is not resent; inspect the document before retrying.
- The control port has no auth and listens on loopback only; enable it only while in use.
- Installed or font-manager fonts are not always found; text falls back to Source Sans 3.

## References

- `references/agents.md` - CLI, scripts with result references, data merge, driving the running app.
- `references/mcp.md` - MCP registration, headless vs connected modes, every tool, example session.
- `references/control-protocol.md` - JSON-lines methods for the running app, panel docking.
- `references/file-format-parity.md` - what opens, places and exports, with fidelity notes.
- `references/gaps.md` - known shortfalls ranked; check before promising a feature.
- Other `references/*.md` and `ROADMAP.md` are upstream parity and planning docs, kept so links resolve.

Upstream snapshot: commit ebd1d78 (2026-10-12), release v0.6.0. `NOTICE` covers third-party material.
