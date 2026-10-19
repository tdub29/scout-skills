# TikTok Slide Typography

## Typography

### Fonts

1. **Edosz** â€” Custom brush script. Brand wordmark only.
   - File: `/public/fonts/edosz.ttf`
   - Apply via: `style={{ fontFamily: '"Edosz", sans-serif' }}`
   - Used for: "Under Par" brand name, tournament titles, main hook headlines
   - Never use for body text, table content, or small labels

2. **System stack** â€” `system-ui, -apple-system, Segoe UI, Roboto, sans-serif`
   - Used for: Everything else (tables, descriptions, footer)

### Text Size Scale

| Element | Size | Leading | Weight | Extra |
|---------|------|---------|--------|-------|
| Hook headline (large) | `10.5â€“10.75rem` | `1.02` | Bold | `tracking-tight text-balance` |
| Hook headline (medium) | `7.85â€“8.4rem` | `1.05â€“1.06` | Bold | `tracking-tight text-balance` |
| Hook headline (small/two-part) | `6.65â€“6.95rem` | `1.08â€“1.1` | Bold | `tracking-tight text-balance` |
| Edosz brand name | `5.95rem` | `0.86` | Bold | `tracking-[-0.02em]` |
| Parenthetical quip | `4.15rem` | tight | Medium | `tracking-tight text-balance` |
| Footer URL | `3.5rem` | tight | Semibold | `tracking-tight` |
| Table header label | `2rem` (default) / `1.8rem` (dense) | â€” | Black | `uppercase tracking-[0.14em]` |
| Section label | `3rem` | â€” | Black | `uppercase tracking-[0.2em]` |
| Tournament title (Edosz) | `6.5rem` | `1.02` | Bold | `tracking-tight` |
| Subtitle | `3rem` | â€” | Medium | `tracking-tight` |
| Table row (default) | `3.2rem` | `1.15` | varies by cell | â€” |
| Table row (dense) | `2.65rem` | `1.15` | varies by cell | â€” |
| Pagination label | `2.4rem` | â€” | Medium | `tracking-tight` |

### Text Effects

```
Headlines:      drop-shadow-[0_10px_36px_rgba(0,0,0,0.55)]
Brand name:     drop-shadow-[0_8px_28px_rgba(0,0,0,0.45)]
Footer URL:     drop-shadow-[0_4px_20px_rgba(0,0,0,0.45)]
```

Always add drop shadows to text over the background image for legibility.

### Wrapping

- `text-balance` on multi-line headlines (prevents orphans)
- `text-pretty` for body text
- Max widths: headlines `max-w-[56rem]`, descriptions `max-w-[52ch]`, quips `max-w-[40ch]`
