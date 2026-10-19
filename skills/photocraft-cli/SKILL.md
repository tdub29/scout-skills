---
name: photocraft-cli
description: Layer-aware PSD/PSB editing from the terminal or MCP with PhotoCraft's headless CLI (open-source Rust Photoshop clone). Use when an image task needs real layers, masks, adjustment layers (curves, levels, vibrance), type layers, layer styles, or must read or write a layered PSD, inspect a PSD's layer tree as JSON, batch-apply an action list to a folder, export adjustment layers as a .cube LUT, or let an agent drive a Photoshop-like editor over MCP. Not for plain resize/convert/thumbnail jobs (image-manipulation-image-magick) or AI image generation.
---

# PhotoCraft CLI

PhotoCraft (github.com/storytold/photocraft, MIT OR Apache-2.0, early alpha) is a clean-room,
pure-Rust reimplementation of Photoshop. Every menu item, tool and dialog is a command in one
registry of 500+ commands, and the CLI, JSON-lines server and MCP server all call that registry.

Reach for it over ImageMagick when the layers matter: ImageMagick flattens a PSD, PhotoCraft
keeps layers, masks, adjustment and type layers and writes them back to PSD.

## 1. Get the binary (never build or run from an untrusted clone)

The CLI ships inside the release packages, so no Rust build is needed.

| Platform | Where `photocraft-cli` lands |
|---|---|
| Windows MSI | `C:\Program Files\PhotoCraft\photocraft-cli.exe` (not on PATH) |
| Windows portable | `photocraft-<ver>-windows-x64-portable.zip` from GitHub Releases |
| Linux deb/rpm | `/usr/bin/photocraft-cli` |
| macOS | separate `photocraft-cli-<ver>-macos-universal.zip` release asset |

Check `SHA256SUMS.txt` on the release before running anything downloaded. Installing is a
system change: ask before doing it. Confirm with `photocraft-cli --help`.

## 2. Discover commands before guessing ids

```sh
photocraft-cli commands --filter curves          # human list
photocraft-cli commands --json --filter sharpen  # ids + parameter docs
photocraft-cli info input.psd --compact          # layer tree, size, mode, depth as JSON
```

Command ids look like `filter.sharpen.smartSharpen`, `layer.newAdjustmentLayer.curves`,
`image.adjustments.invert`. Never invent an id or a param name: read it from `commands --json`.

## 3. One-shot edit

```sh
photocraft-cli run wave.psd \
  --cmd filter.sharpen.smartSharpen     --params '{"amount":80}' \
  --cmd layer.newAdjustmentLayer.curves --params '{"points":[[0,0],[64,48],[192,212],[255,255]]}' \
  --out wave-final.png
```

- Each `--params` applies to the preceding `--cmd`. Each command prints its JSON result.
- `--new <json>` instead of a file creates a blank document.
- `--out x.psd` keeps layers; `.tif` is flat unless `--tiff-layers`; `--quality` for JPEG/WebP
  (WebP with a quality is lossy, without one lossless).
- Missing fonts warn on stderr (and in `warnings` JSON); fix with `type.resolveMissingFonts`.

Convert only: `photocraft-cli convert in.psd out.png`.

## 4. Batch a folder

```sh
photocraft-cli batch --actions grade.json --in ./raw --out ./graded
```

`grade.json` is a list of steps: `[id, params]` pairs, `{"command": id, "params": {...}}` objects,
or bare ids, optionally wrapped in `{"actions": ...}` or `{"steps": ...}`. An Actions-panel set
(`{"actions": [{"name", "steps"}...]}`) needs `--action <name>` when it holds more than one.
`--out` equal to `--in` is refused unless `--in-place`. Max 256 steps per headless/MCP batch.
Droplets: `photocraft-cli droplet file.pcdroplet <files-or-dirs> --out <dir>`.

## 5. Agent-driven: MCP

```sh
# Claude Code, Windows default install; scope roots to the working folder only
claude mcp add photocraft -- "C:\Program Files\PhotoCraft\photocraft-cli.exe" mcp --automation-read-root <dir> --automation-write-root <dir>
```

Core tools: `command_list`, `command_run`, `command_batch`, `doc_inspect`, `render_preview`
(also `doc_render_preview`); resources `photocraft://document`, `photocraft://commands`.
Omitting a root removes that authority; paths are relative to the roots. Registering an MCP
server changes Claude config: ask first. Bridge mode to the running desktop app
(`photocraft --control <port>` plus `--bridge 127.0.0.1:<port> --control-token-file <path>`)
adds UI inspection, pointer input and screenshots. See `references/automation/mcp.md`.

## 6. Safety rules

- PSD/PSB/.pcraft, LUTs, profiles and action files are untrusted input. Run unknown ones in a
  scratch folder, never with `--in-place` on originals.
- The plain CLI does NOT confine paths to a root; only `mcp`/`serve` roots do.
- Never expose the control port or `serve --port` beyond loopback; the token grants the whole
  control surface. Do not leave `--control` enabled.
- Early alpha: verify output by rendering or `info` before reporting success.

## References

| File | Read when |
|---|---|
| `references/cli-usage.txt` | Exact `--help` text for every subcommand (upstream commit 3d6050b) |
| `references/automation/cli.md` | Subcommands, LUT export (`file.export.colorLookupTables`), path rules |
| `references/automation/mcp.md` | MCP headless vs bridge, tools, install from a release |
| `references/automation/overview.md` | Choosing CLI vs `serve` vs MCP |
| `references/automation/control-protocol.md` | Desktop JSON control channel |
| `references/automation/security-model.md`, `references/security/*.md` | Limits and trust boundaries |
| `references/architecture/command-engine.md`, `references/architecture/automation.md` | How the command registry works |
| `references/formats/*.md` | PSD/PSB, raster, `.pcraft` fidelity notes |
| `references/getting-started/installation.md`, `building.md` | Install and source build |

Links in the upstream pages to `docs/*.md` (for example `docs/mcp.md`, `docs/control-protocol.md`)
point at files not published in the public repo; use `commands --json` and `--help` instead.
