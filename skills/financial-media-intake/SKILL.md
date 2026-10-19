---
name: financial-media-intake
description: Use when the user provides videos, audio, screenshots, or image files for personal-finance, tax, portfolio, mortgage, or financial-advisor context. Extract source context, verify actionable claims, and persist a dated artifact under .agents/artifacts/.
---

# Financial Media Intake

Use this for local MP4/MOV/audio files, screenshots, social clips, advisor prep
material, podcasts, and similar sources when the user's goal is finance context
or "apply this in the repo."

## Non-Negotiable Context Rule

The user's latest request defines the target. Open IDE tabs, visible browser
tabs, and recently touched files are only context unless the user explicitly
names them. Do not modify a visible HTML/UI file during media intake unless the
user asks for that exact file to change.

Start by stating the inferred target in one sentence, for example:

`The target is: extract these media files into durable finance/advisor context in .agents/artifacts/.`

## Workflow

1. Read `docs/llm-guides/agent-harness.md`.
2. Read `.agents/memory/00-INDEX.md`, then the memory files it requires.
3. Scan `.agents/artifacts/financial-insight-loop/BACKLOG.md` for related open
   finance items.
4. Inspect each media file with metadata tools (`ffprobe`, file properties, OCR,
   or image inspection as appropriate).
5. Transcribe audio when present. Prefer
   `.agents/artifacts/research-notes/_tools/transcribe.py` for local audio/video.
6. Extract representative frames/contact sheets for video, or crop/OCR important
   regions for screenshots.
7. Summarize what the source actually says, separating:
   - extracted claims,
   - visual context,
   - verified facts,
   - advisor/CPA questions,
   - current-plan impact.
8. Verify actionable/current claims against primary sources. For tax claims,
   prefer IRS, SEC, prospectus, plan documents, or provider disclosures over
   social-media framing.
9. Save a dated note under `.agents/artifacts/research-notes/` unless the output
   is clearly a ticker-specific review, in which case use `stock-reviews/`.
10. Put bulky/generated transcripts, frames, screenshots, and raw OCR in a
    matching `_cache/` directory. `_cache/` is gitignored; the durable `.md`
    artifact should link or name the cache paths.

## Artifact Shape

Use a concise structure:

- Date captured
- Source inventory
- Method used
- What the media actually adds
- Verification / source checks
- Advisor or action agenda
- Position / plan impact
- Open questions

## Gotchas

- Do not treat social clips as advice. Convert them into advisor questions or
  verified planning implications.
- Do not infer that an open IDE file is the destination. If no destination is
  named, the destination is the finance artifact system.
- Do not quote market prices, rates, or tax thresholds from memory. Fetch and
  cite current primary or high-quality sources before using them in advice.
- Do not update `finances.html` unless the media contains actual account data or
  the user explicitly asks to update the dashboard.
- Do not leave a useful transcript only in chat. Persist it or a summary in
  `.agents/artifacts/`.
