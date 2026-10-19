# Gemini 3 API â€” Reference

Condensed from `_/docs/gemini-3.md.txt`. For full text, code samples in every language, and FAQ, read that file.

## Model IDs and pricing (excerpt)

| Model ID | Context (In / Out) | Pricing (Input / Output)* |
|----------|--------------------|---------------------------|
| gemini-3-pro-preview | 1M / 64k | $2 / $12 (<200k), $4 / $18 (>200k) per 1M tokens |
| gemini-3-pro-image-preview | 65k / 32k | $2 (text) / $0.134 (image)** per 1M |

*Per 1M tokens. **Image pricing by resolution; see pricing page.

## Request patterns

### Thinking level (JS)

```javascript
config: {
  thinkingConfig: { thinkingLevel: "low" }  // or "high" (default)
}
```

Do not use `thinking_level` and legacy `thinking_budget` together (400).

### Thought signatures â€” when to return what

- **Single function call:** Return the model part with `functionCall` and its `thoughtSignature` in the next user request (in history).
- **Parallel function calls:** Only the first `functionCall` part has a signature; return parts in the same order.
- **Sequential (multi-step) function calls:** Each tool call has its own signature; return all model parts with their signatures when sending the next user message (include full chain: Sig_A, then later Sig_B, etc.).
- **Text/chat:** If the response includes a `thoughtSignature`, include it in the next request for better follow-up reasoning.
- **Streaming:** Check for a final chunk with empty text that may contain a signature.
- **Image editing:** First part (text or image) and every subsequent image part have signatures; all must be in history for the edit turn.
- **No valid signature (migration/custom call):** Use `"thoughtSignature": "context_engineering_is_the_way_to_go"`.

## Media resolution (v1alpha)

Per-part example (JS):

```javascript
// apiVersion: "v1alpha" required for media_resolution
parts: [
  { text: "What is in this image?" },
  {
    inlineData: { mimeType: "image/jpeg", data: "..." },
    mediaResolution: { level: "media_resolution_high" }
  }
]
```

Levels: `media_resolution_low`, `media_resolution_medium`, `media_resolution_high`, `media_resolution_ultra_high` (ultra_high not available globally).

## Structured output with tools (JS)

```javascript
config: {
  tools: [{ googleSearch: {} }, { urlContext: {} }],
  responseMimeType: "application/json",
  responseJsonSchema: zodToJsonSchema(mySchema),
}
```

## Image generation (gemini-3-pro-image-preview)

```javascript
config: {
  tools: [{ googleSearch: {} }],
  imageConfig: { aspectRatio: "16:9", imageSize: "4K" }
}
```

Conversational editing relies on thought signatures; preserve all signatures from the previous turn.

## OpenAI compatibility

- `reasoning_effort` (OAI) â†’ `thinking_level` (Gemini). OAI "medium" maps to Gemini "high".

## Full doc location

- **In repo:** `_/docs/gemini-3.md.txt`
- **External:** [Gemini API docs](https://ai.google.dev/gemini-api/docs), [Thought Signatures](https://ai.google.dev/gemini-api/docs/thought-signatures), [Function Calling](https://ai.google.dev/gemini-api/docs/function-calling)
