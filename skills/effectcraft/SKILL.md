---
name: effectcraft
description: Drive EffectCraft, the open-source After Effects clone, headless over MCP, CLI or scripts. Comps, keyframes, effects, renders, Lottie.
---

# EffectCraft

EffectCraft (storytold/effectcraft, MIT OR Apache-2.0) is a pure-Rust, clean-room reimplementation of
Adobe After Effects: compositions, layers, keyframes, 306 effects, expressions, 3D cameras and lights,
motion tracking, Essential Graphics templates, a render queue, and built-in Lottie import/export.
Projects are versioned JSON (`.ecproj`). Every menu item is an engine command with a stable id and
JSON params, so an agent can do anything a user can.

Use it when the job is a motion graphic, title card, lower third, keyed/composited shot or Lottie
file built the After Effects way (layers on a timeline), rendered headless. It differs from the code-first
video skills here: `remotion-best-practices` (React components) and `hyperframes-*` (HTML/GSAP scenes)
author video as code; EffectCraft authors a layer/keyframe project and renders it. For hand-written
Lottie JSON see `text-to-lottie` / `lottie-integration`.

## Get the binary (nothing here installs it)

The skill ships docs only. Trevor installs the app; never run an installer unasked.

- Windows: `effectcraft-<ver>-windows-x64.msi` or `-windows-x64-portable.zip` from
  https://github.com/storytold/effectcraft/releases. The MSI puts the CLI at
  `C:\Program Files\EffectCraft\effectcraft-cli.exe` (not on PATH).
- macOS: separate `effectcraft-cli-<ver>-macos-universal.zip` asset. Linux: deb/rpm put it at `/usr/bin/effectcraft-cli`.
- From source: Rust 1.95+, `cargo build --release -p effectcraft-cli`.

Check it exists before planning around it: `effectcraft-cli info --demo --json`.

## Three ways in

| Interface | Use for | Window |
|---|---|---|
| MCP `effectcraft-cli mcp` | an agent session: inspect, edit, render frames to look at | no (headless) or `--bridge 9877` to the live app |
| CLI `effectcraft-cli exec/run/get/set/render` | one-shot edits and renders, CI, `--json` output | no |
| Control channel `effectcraft --control 9877` | driving and screenshotting the live UI | yes |

Register MCP for Claude Code (Windows MSI path):

```sh
claude mcp add effectcraft -- "C:\Program Files\EffectCraft\effectcraft-cli.exe" mcp --autosave \
  --automation-read-root "<project dir>" --automation-write-root "<output dir>"
```

The read/write roots confine file access and refuse scripts and UI driving while set. Drop them only
when `run_script` is needed. `--autosave` checkpoints headless work; without it, unsaved work dies with
the server, so `save_project` after each milestone.

## Working loop

1. Orient: `get_state` then `get_project` then `get_comp {}`.
2. Find the command: `list_commands {"filter":"mask"}` then `describe_command {"command":"mask.new"}` (params + JSON Schema). Unknown param keys are rejected with the accepted list, never ignored.
3. Edit: `execute_command`, `set_property`, `add_keyframe`, `add_effect`, or `batch` (one undo step, `"$1.layer"` references earlier step results, rolls back on failure).
4. Look: `render_frame {"time":1.0,"max_side":640}` returns a PNG. Check every visual change this way; do not assume.
5. Save, then render: `renderQueue.add {comp, format, output}` then `renderQueue.render {"wait":true}`, or CLI `effectcraft-cli render --comp Main --out main.mp4 --project main.ecproj`.

Lottie out: `effectcraft-cli exec file.exportLottie '{"comp":"Main","path":"main.json"}' main.ecproj`.
Template render: `effectcraft-cli render --template lt.ectemplate --values values.json --out 'title_[#####].png'`.

## Pitfalls that cost real sessions

- **Layer time vs comp time.** `add_keyframe` / `set_property` with `time` take layer time; `get_property` and `render_frame` take comp time. Pass `timeBase: "comp"` on offset or stretched layers.
- **Name layers at creation** (`layer.newText {"name":"Title",...}`) so later calls say `"layer":"Title"`. A reference that matches nothing errors.
- **Use the paths replies return** (`effect.apply` gives `effects/#2`; `@uid` works as a path).
- **Scripts that throw keep partial edits.** Wrap `run_script` loops in `app.beginUndoGroup()` / `app.endUndoGroup()`.
- **Effect points are in effect space** (layer pixels from the effect bounds' top-left), not comp space.
- **Long jobs** (`track.analyze`, `warp.analyze`, `track.mask`, renders) run in the background in the app; pass `"wait": true` headless.
- It is young (v0.8.0, Oct 2026). Check `docs/gaps.md` before promising parity with an After Effects feature.

## References (load the one the task needs)

- `docs/agents.md`: full MCP tool catalog, typical session, cookbook, tracking, Warp Stabilizer, Roto Brush. Start here.
- `docs/mcp.md`: MCP conventions, file-access confinement, render progress and cancellation.
- `docs/control-protocol.md`: the live-app JSON-lines control channel.
- `docs/scripting-parity.md`: the After Effects-style JavaScript object model for `run_script` / `script`.
- `docs/effects.md` (generated catalog of every effect and param), `docs/effects-parity.md`.
- `docs/footage.md`: import, image sequences, Interpret Footage.
- `docs/plugins.md` with `examples/plugins/posterize-bands/`: writing an effect plug-in.
- `docs/preferences.md`, `docs/web.md` (browser build), `docs/file-format-parity.md`, `docs/gaps.md`, `docs/target-app-parity.md`, `docs/ui-parity.md`, `docs/hardware-parity.md`, `docs/localization-parity.md`, `docs/fidelity/`.
- Maintainer docs kept for link integrity: `docs/architecture.md`, `docs/testing.md`, `docs/releasing.md`, `docs/roadmap.md`, `ROADMAP.md`, `docs/contributors.md`.

Links in the docs to `../AGENTS.md`, `../.mcp.json`, `../.github/`, `../packaging/` point at the upstream
repo and were left out on purpose (contributor rules, a cargo-run MCP config, CI files). The `.mcp.json`
content is the `claude mcp add` line above.

Upstream: https://github.com/storytold/effectcraft @ 9efe75330c090748df1818348942d4abc30c9b1f (2026-10-12).
License: MIT OR Apache-2.0 (`LICENSE-MIT`, `LICENSE-APACHE`, `NOTICE`).
