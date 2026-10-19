---
name: vectorcraft-mcp
description: Drive the VectorCraft vector editor (open-source Rust Illustrator clone) through its MCP server or headless CLI to build editable vector art - posters, icon sets, Pathfinder, live effects and blends, Image Trace, recolor, graphs - then screenshot and export SVG, PDF, PNG, EPS, DXF or PSD. Use when a real vector editor beats hand-written SVG, or to batch-convert vector files.
---

# VectorCraft MCP

VectorCraft (github.com/storytold/vectorcraft, MIT or Apache-2.0) is a clean-room Adobe Illustrator
reimplementation. Its `vectorcraft-cli mcp` server lets an agent draw, inspect, screenshot and export
real documents with live shapes, live effects and live type. Pick this over `svg-logo-designer` or
hand-written SVG when the art needs Pathfinder, blends, gradient mesh, envelope distort, Image Trace,
multi-artboard PDF or print-ready export.

## 0. Is it installed?

Nothing here works until the binary exists. Check, in order:

1. `claude mcp list` shows a `vectorcraft` server, or
2. Windows MSI default: `C:\Program Files\VectorCraft\vectorcraft-cli.exe` (not on PATH), or
3. `vectorcraft-cli` on PATH (Linux packages, unzipped macOS asset).

If none exist, stop and tell the user. Installing it (release MSI from
`github.com/storytold/vectorcraft/releases`, or `cargo build --release -p vectorcraft-cli`) is their
call; do not run an installer unasked. Register once it is there:

```sh
claude mcp add vectorcraft -- "C:\Program Files\VectorCraft\vectorcraft-cli.exe" mcp --headless \
  --automation-read-root <in-dir> --automation-write-root <out-dir>
```

The two root flags confine every file read and write; prefer them. `--connect 127.0.0.1:7979` drives
a running app (`vectorcraft --control 7979`) so the user watches live; no flag tries that, then falls
back to headless.

## 1. The working loop

1. `inspect_document {depth: 0}` first. Coordinates are points, y points down, origin is the first
   artboard's top-left; a new document is 612 x 792.
2. Build with the dedicated tools: `draw_shape`, `draw_path` (points or SVG `d`), `set_paint`,
   `add_text`, `apply_effect` (call with no `effect` to get the catalogue), `pathfinder`, `transform`,
   `create_graph`. Everything else is `run_command {command, params}`; find ids with
   `list_commands {filter}`.
3. Batch dependent steps with `command_batch` (`atomic: true` for one undo step); `"$N.path"` /
   `"$last.ids.0"` pull values from earlier step results.
4. `screenshot` (or `render_preview`) to look, fix, then `export {path, format, options}`.
5. Keep it editable: live shapes, effects and type. No flatten or rasterize unless asked.

Errors come back as `isError: true` with a readable message; read it and retry rather than abandon.

## 2. Ready-made workflows

`prompts/get` serves five templated workflows: `poster`, `icon-set`, `recolor`, `trace-and-style`,
`export-set`. Their full text is in `references/prompts.rs` (the `text:` field of each `PromptDef`).
Follow the matching one when the task fits.

## 3. Headless batch CLI (no MCP client needed)

```sh
vectorcraft-cli run --in in.svg --cmd select.all --cmd paint.setFill --params '{"color":"#ff0000"}' \
  --export out.svg --export out.png --scale 2
```

One JSON line per step, non-zero exit on the first failure. Good for format conversion.

## References

- `references/mcp.md` - the full server manual: every tool, resource template, prompt, export option,
  and the per-feature sections (masks, symbols, swatches, appearance stacks, Live Corners, Recolor,
  flattener, PDF/X options). Grep its `##` headings rather than reading 3,000 lines.
- `references/control-protocol.md` - the app's TCP control protocol behind `--connect`.
- `references/plugins.md` - plug-in model (its `../crates/plugins/example` link points at upstream
  source, not shipped here).
- `references/revolve.md` - the Revolve 3D effect.
- `references/prompts.rs` - the five workflow prompts verbatim.
- `LICENSE-MIT`, `LICENSE-APACHE`, `NOTICE` - upstream licenses.

Provenance: upstream commit 04bc43c802170b446efb5451734651d820b56dcf (release v0.9.0 era,
2026-10-12). Upstream ships no SKILL.md; this one was written for the harness from its docs.
