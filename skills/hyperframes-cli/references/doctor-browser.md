# doctor, browser

Environment diagnosis and bundled-Chrome management. Run these first when a render or preview fails.

## doctor

```bash
npx hyperframes doctor
npx hyperframes doctor --json     # CI / agent output (always exit 0; gate on payload `ok`)
```

Runs independent checks and reports each as ok/warn/fail:

- **Version** â€” installed CLI vs latest on npm (hints upgrade when stale)
- **Node.js** â€” â‰¥ 22 required
- **CPU**, **Memory**, **Disk** â€” host resources
- **Environment** â€” env vars that affect the renderer
- **FFmpeg** / **FFprobe** â€” found, version, codecs
- **Chrome** â€” bundled or system, version, path
- **Docker** / **Docker running** â€” required only for `render --docker`
- **/dev/shm** â€” inside containers only

Run `doctor` first when:

- `render` fails with a Chrome or FFmpeg error.
- `preview` opens but the composition fails to load.
- A fresh machine has never run HyperFrames.

Common issues:

- **Missing FFmpeg** â€” install via `brew install ffmpeg` (macOS) or your package manager.
- **Missing bundled Chrome** â€” run `npx hyperframes browser ensure`.
- **Low memory** â€” close other Chromes, reduce `--workers`, or use `--quality draft`.
- **Chrome exits instantly inside an agent sandbox (macOS)** â€” seatbelt-style sandboxes
  (e.g. codex `workspace-write`) block Chromium's Mach port bootstrap
  (`MachPortRendezvous`; openai/codex#21292), so every Chrome â€” bundled, system, or
  headless shell â€” dies at startup. This is a host-level block, not a HyperFrames or
  Chrome install problem: compile checks and audio still pass, only rendering is
  unavailable. State the blocker and deliver the checked composition; render outside the
  sandbox or via `render --docker` / cloud rendering where available. **Do not build a
  substitute rasterizer** (magick/PIL/SVG frame pipelines) â€” on a blocked-browser host
  the deliverable IS the checked composition plus this blocker note, and rendering is
  handed to `--docker`, cloud, or the user. Write your final summary the moment the
  blocker is identified, BEFORE any optional fallback work: a later session failure must
  not erase the report of work already done.

## browser

```bash
npx hyperframes browser ensure    # find or download the pinned Chrome
npx hyperframes browser path      # print the browser executable path (for scripting)
npx hyperframes browser clear     # remove the cached Chrome download
```

Manage the Chrome build HyperFrames uses for rendering. The pinned version exists because pixel output drifts across Chrome versions â€” using the bundled build keeps rendered output reproducible across machines.

Use `path` to embed the binary in scripts: `$(npx hyperframes browser path)`.
