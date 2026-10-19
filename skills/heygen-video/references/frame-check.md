# Frame Check â€” Aspect Ratio & Background Pre-Check

Runs automatically when `avatar_id` is set, before Generate. Appends correction notes to the Video Agent prompt. Does NOT generate images or create new looks.

## Step 1: Fetch the avatar look metadata

**MCP:** `get_avatar_look(look_id=<avatar_id>)`
**CLI:** `heygen avatar looks get --look-id <avatar_id>`

Extract:
- `avatar_type`: `"photo_avatar"` | `"studio_avatar"` | `"video_avatar"`
- `preview_image_url`: use to determine orientation
- `image_width` and `image_height`: use for orientation calculation

## Step 2: Determine avatar orientation

Use `image_width` and `image_height` from the API response (or fetch the preview image dimensions if those fields are missing).
- width > height â†’ landscape avatar
- height > width â†’ portrait avatar
- width == height â†’ **square avatar** (1:1) â†’ always needs framing correction
- Fetch fails or no preview â†’ assume portrait (safer default)

## Step 3: Determine if background exists

| `avatar_type` | Background? | Reason |
|---|---|---|
| `photo_avatar` | âœ… Handled by Video Agent | Video Agent generates avatar + environment together during video creation. No standalone bg correction needed. |
| `studio_avatar` | âš ï¸ Maybe | Check preview image â€” if transparent/solid/empty â†’ "No background" â†’ apply Correction C |
| `video_avatar` | âœ… Yes | Recorded in a real environment |

## Step 4: Append correction notes to prompt

Based on Steps 2-3, append zero or more correction notes **verbatim to the end of the Video Agent prompt text.** Do NOT ask the user. Do NOT generate images. Do NOT create new looks.

### A) Portrait avatar â†’ Landscape video (most common)

```
FRAMING NOTE: The selected avatar image is in portrait orientation but this video is landscape (16:9). Frame the presenter from the chest up, centered in the landscape canvas. Use AI Image tool to generative fill to extend the scene horizontally with a complementary background environment that matches the video's tone (studio, office, or contextually appropriate setting). Do NOT add black bars or pillarboxing. The avatar should feel natural in the 16:9 frame.
```

### B) Landscape avatar â†’ Portrait video

```
FRAMING NOTE: The selected avatar image is in landscape orientation but this video is portrait (9:16). Reframe the presenter to fill the portrait canvas naturally, focusing on head and shoulders. Use AI Image tool to generative fill to extend vertically if needed. Do NOT add letterboxing. The avatar should fill the portrait frame comfortably.
```

### D) Square avatar â†’ Landscape video

```
FRAMING NOTE: The selected avatar image is in square (1:1) orientation but this video is landscape (16:9). Frame the presenter from the chest up, centered in the landscape canvas. Use AI Image tool to generative fill to extend the scene horizontally with a complementary background environment that matches the video's tone (studio, office, or contextually appropriate setting). Do NOT add black bars or pillarboxing. The avatar should feel natural in the 16:9 frame.
```

### E) Square avatar â†’ Portrait video

```
FRAMING NOTE: The selected avatar image is in square (1:1) orientation but this video is portrait (9:16). Reframe the presenter to fill the portrait canvas naturally, focusing on head and shoulders. Use AI Image tool to generative fill to extend vertically if needed. Do NOT add letterboxing. The avatar should fill the portrait frame comfortably.
```

### C) Missing background â€” studio_avatar only

**Only for `studio_avatar` with transparent/solid/empty background. NOT for photo_avatar** (Video Agent handles photo_avatar environments during generation).

```
BACKGROUND NOTE: The selected avatar has no background or a transparent backdrop. Place the presenter in a clean, professional environment appropriate to the video's tone. For business/tech content: modern studio with soft lighting and subtle depth. For casual content: bright, minimal space with natural light. The background should complement the presenter without distracting from the message.
```

## Correction Stacking Matrix

Corrections can stack. Use the matrix to determine which notes to append.

| avatar_type | Orientation Match? | Has Background? | Corrections |
|---|---|---|---|
| `video_avatar` | âœ… matched | âœ… Yes | None |
| `video_avatar` | âŒ mismatched | âœ… Yes | Framing only (A or B) |
| `video_avatar` | â—» square | âœ… Yes | Framing only (D or E) |
| `studio_avatar` | âœ… matched | âœ… Yes (check preview) | None |
| `studio_avatar` | âœ… matched | âŒ No | Background (C) |
| `studio_avatar` | âŒ mismatched | âœ… Yes | Framing only (A or B) |
| `studio_avatar` | âŒ mismatched | âŒ No | Framing (A or B) + Background (C) |
| `studio_avatar` | â—» square | âœ… Yes | Framing only (D or E) |
| `studio_avatar` | â—» square | âŒ No | Framing (D or E) + Background (C) |
| `photo_avatar` | âœ… matched | (n/a) | **None** â€” Video Agent handles avatar + environment together |
| `photo_avatar` | âŒ mismatched | (n/a) | **Framing only (A or B)** |
| `photo_avatar` | â—» square | (n/a) | **Framing only (D or E)** |

**How to check if studio_avatar has a background:** Fetch `preview_image_url`. If transparent/checkered, solid color, or cutout â†’ "No background" â†’ append Correction C.

**photo_avatar rule:** Video Agent generates the avatar and its environment together during video creation. Do NOT append Correction C for photo_avatars. Only append framing corrections (A, B, D, or E) if there's an orientation mismatch.

## Step 5: Submit with original avatar_id

After appending correction notes to the prompt, submit the video request using the **original `avatar_id`** (unchanged). Video Agent handles framing and background internally based on the FRAMING NOTE and BACKGROUND NOTE directives in the prompt.

## Step 6: Log the correction

Add to learning log entry:
- `"aspect_correction"`: `"portrait_to_landscape"` | `"landscape_to_portrait"` | `"square_to_landscape"` | `"square_to_portrait"` | `"background_fill"` | `"both"` | `"none"`
- `"avatar_type"`: the raw value from the API
