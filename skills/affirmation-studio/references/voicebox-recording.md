# Recording affirmations in your own voice with voicebox

[jamiepine/voicebox](https://github.com/jamiepine/voicebox) â€” local-first AI voice studio. **Clone** a voice from your own samples, **dictate** anywhere via a global hotkey, **create** speech on a multi-voice timeline. MIT license. Everything (models, voice data, captures) stays on your machine â€” nothing is uploaded. macOS / Windows / Linux / Docker, with GPU acceleration (Metal / CUDA / ROCm / Intel Arc) or CPU fallback.

For affirmations the loop is: **clone your voice once â†’ paste a script â†’ generate â†’ save the audio â†’ play it on a loop.**

## One-time install

Prereqs: **Bun**, **Rust**, **Python 3.11+**, Tauri platform prerequisites (on macOS also Xcode CLT). Then from the cloned repo:

```bash
git clone https://github.com/jamiepine/voicebox
cd voicebox
just setup   # creates the Python venv + installs dependencies
just dev     # starts the FastAPI backend + the desktop app
```

(Check the repo README for the current `just` recipes and any model-download step â€” the TTS engines such as Qwen3-TTS / Chatterbox / Kokoro and Whisper for STT download on first use.)

> Heads-up: voicebox is a full desktop build (Tauri + Rust + Python). Budget time for the first setup and model downloads. You don't need it installed to *write* scripts with `affirmation-studio` â€” only to record them.

## Clone your voice (once)

1. In voicebox, create a new **voice profile** â†’ record or upload a sample.
2. Sample quality is everything:
   - **Quiet room**, no fan/AC/echo. A cheap USB mic or even AirPods beats a noisy room.
   - **30â€“90 seconds** of natural speech â€” read something neutral at your normal pace and warmth (not performed).
   - Speak the way you want the affirmations to *sound* â€” calm and steady reads back calm and steady.
3. Save the profile (e.g. "Trevor â€” calm"). Reuse it for every track.

## Generate a track

1. Open a new generation / timeline, select your cloned voice.
2. Paste the **spoken text** from the affirmation script â€” exactly the lines, no markdown, no stage directions (voicebox reads what's there).
3. For pacing, put each affirmation on its own line and add blank lines / ellipses where you want a breath; tune rate so it doesn't rush.
4. Generate, listen, regenerate any line that lands flat.
5. Optional post-processing in voicebox (light reverb / compression) for a warmer, more "spoken to you" feel â€” keep it subtle.
6. **Export** the audio.

## Save & loop

- Save exports to `self/affirmations/audio/<area>.<date>.wav` (or mp3).
- Build the habit: morning loop, on a walk, or before the specific situation the area is about (before a call, before a confrontation).
- Re-record when a line stops feeling true in either direction â€” it became obvious (ladder up) or it never landed (ladder down). The script in `self/affirmations/scripts/` is the source of truth; regenerate audio from it.

## Two voices, optionally

Default is **your own clone, first person** ("I amâ€¦") â€” strongest for self-recorded affirmation work. If you also want a **guided/second-person** track ("You areâ€¦", "Notice your breathâ€¦"), use one of voicebox's 50+ **preset** voices (pick a calm one) for that version. Keep first-person = your voice, second-person = preset.

## Agent voice (bonus)

voicebox exposes an **MCP** integration so an assistant can speak in a chosen voice. Out of scope for the affirmations practice, but it means a future agent in this workspace could read a freshly generated track aloud in your cloned voice without you opening the app.
