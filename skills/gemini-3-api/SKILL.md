---
name: gemini-3-api
description: Implements or integrates with the Gemini 3 API â€” model selection, thinking level, thought signatures, media resolution, and agentic workflows. Use when implementing Gemini 3 API calls, function calling, agent operations, image generation, migrating from Gemini 2.5, or when the user mentions "Gemini 3," "thought signatures," "thinking level," or "gemini-3-pro."
---

# Gemini 3 API

Quick reference for implementing Gemini 3 in this codebase. For full API details and code samples, see [references/gemini-3-guide.md](references/gemini-3-guide.md).

## Models

| Model ID | Context (In / Out) | Use case |
|----------|--------------------|----------|
| **gemini-3-pro-preview** | 1M / 64k | Complex reasoning, agentic workflows, broad knowledge |
| **gemini-3-pro-image-preview** | 65k / 32k | Image generation and conversational editing |

Pricing: input/output per 1M tokens; image pricing varies. See [references/gemini-3-guide.md](references/gemini-3-guide.md) for exact rates.

## Critical settings

### Thinking level

- **Parameter:** `thinking_level` (not `thinking_budget`; do not use both).
- **Default:** `high`. Use for complex reasoning, agents, multi-step tasks.
- **`low`:** Use for simple instruction-following, chat, or high throughput. Reduces latency and cost.
- Do not set `thinking_level` and legacy `thinking_budget` in the same request (400 error).

### Temperature

- **Keep at 1.0.** Gemini 3 is tuned for this. Lower values can cause looping or worse performance on reasoning tasks.

### Thought signatures

- Encrypted representations of the modelâ€™s reasoning; **must be returned exactly as received** in the next request when applicable.
- **Function calling (strict):** Missing signatures â†’ 400. "Current turn" = all Model (`functionCall`) and User (`functionResponse`) steps since the last User `text`.
  - Single call: signature on the `functionCall` part.
  - Parallel calls: only the **first** `functionCall` has a signature; preserve part order.
  - Multi-step (sequential): **each** function call has a signature; return **all** in history.
- **Text/chat:** Not strictly enforced, but omitting signatures hurts reasoning and quality. In streaming, signatures can appear in a final chunk with empty text â€” parse for them.
- **Image generation/editing (strict):** Signatures on first part (text or image) and every subsequent image part; all required for editing context.
- **Migration / custom traces:** When conversation or function call did not come from Gemini 3, use dummy: `"thoughtSignature": "context_engineering_is_the_way_to_go"`.

Official SDKs (Python, Node, Java) handle thought signatures for standard chat; manual handling needed for custom history or REST.

## Media resolution

Controls max tokens per image/video frame. Set per media part or globally (except `ultra_high` global).

| Media | Recommended | Notes |
|-------|--------------|--------|
| Images | `media_resolution_high` | Best quality for most image tasks |
| PDFs | `media_resolution_medium` | Document understanding; high rarely helps OCR |
| Video (general) | `media_resolution_low` or `medium` | 70 tokens/frame; enough for action/description |
| Video (text-heavy) | `media_resolution_high` | 280 tokens/frame for dense text/OCR |

`media_resolution` is in the v1alpha API; use `api_version: "v1alpha"` (or equivalent) where required.

## Prompting

- **Be concise.** Gemini 3 prefers direct instructions; long or over-engineered prompts can be over-analyzed.
- **Verbosity:** Default is less verbose. To get a more conversational tone, say so in the prompt (e.g. "Explain as a friendly, talkative assistant").
- **Large context:** Put the main instruction or question **after** the data (e.g. at end of prompt). Start the question with "Based on the information above..." to anchor reasoning.

## Migration from Gemini 2.5

- Replace complex chain-of-thought hacks with `thinking_level: "high"` and simpler prompts.
- Remove or stop overriding temperature; use default 1.0.
- PDFs: if you relied on specific OCR behavior, try `media_resolution_high` and verify.
- Token use may increase for PDFs and decrease for video with new defaults; reduce media resolution if you hit context limits.
- Image segmentation (pixel masks) is not in Gemini 3 Pro; use Gemini 2.5 Flash or Gemini Robotics-ER 1.5 if needed.

## Tools and capabilities

- **Supported:** Google Search, File Search, Code Execution, URL Context, custom function calling, structured outputs with tools.
- **Not supported:** Grounding with Google Maps, Computer Use.

## Project alignment

- Backend agent operations and conversation storage: see `AGENTS.md` (request/response schema, conversation state, error handling).
- Source of truth for Gemini 3 API details and code samples: `_/docs/gemini-3.md.txt` and [references/gemini-3-guide.md](references/gemini-3-guide.md).
