---
name: tiktok-slides-style-guide
description: "Under Par brand style guide for TikTok 9:16 marketing slides. Use when creating, editing, or reviewing any TikTok slide component â€” hook slides, odds/table slides, promotional slides, or new slide types. Covers: canvas dimensions, color palette, typography (Edosz font), background treatment, safe zones, table layouts, export pipeline, viewer integration. Triggers: tiktok slide, tiktok style, new tiktok, slide design, hook slide, odds slide, tiktok marketing, slide export, tiktok component, create a slide, add a slide, tiktok branding, under par tiktok"
---

# Under Par TikTok Slides Style Guide

Reference for creating and maintaining TikTok 9:16 marketing slides for Under Par Fantasy Golf.

## Architecture Overview

All slides are **statically rendered React components** exported as 1080x1920 PNG images via Playwright. They live under `fantasy-golf/src/components/marketing/tiktok/` and are routed through Next.js pages at `/promo/tiktok/*`.

### File Map

| File | Purpose |
|------|---------|
| `tiktok-slide-shell.tsx` | Base canvas shell â€” backgrounds, overlays, color constants (`tt` object) |
| `TikTokHookSlides.tsx` | "Hook" slides â€” big headlines with Edosz font wordmark |
| `TikTokOddsSlides.tsx` | Odds/table slides â€” favorites, sleepers, full field |
| `tiktok-odds-data.ts` | Static data file (auto-generated from DB via `scripts/generate-tiktok-odds-data.ts`) |
| `scripts/export-tiktok-slides-core.ts` | Playwright export pipeline (shared by all decks) |
| `scripts/export-tiktok-hooks.ts` | Hook deck export entry point |
| `scripts/export-tiktok-odds.ts` | Odds deck export entry point |
| `tiktok-slideshow-viewer.html` | Local HTML viewer for all exported decks |

### Creating a New Slide Deck

1. Create component in `src/components/marketing/tiktok/`
2. Create route page at `src/app/promo/tiktok/{deck-name}/page.tsx` + `layout.tsx` (with `robots: { index: false }`)
3. Create export script in `scripts/export-tiktok-{deck-name}.ts`
4. Add npm script `"export:tiktok-{deck-name}"` using `start-server-and-test`
5. Add deck to `tiktok-slideshow-viewer.html`

---

## Canvas & Shell

**Dimensions:** 1080px wide x 1920px tall (9:16)

Every slide wraps its content in `<TikTokSlideShell>`:

```tsx
<TikTokSlideShell index={0} bgIndex={0} safeZone>
  {/* slide content */}
</TikTokSlideShell>
```

**Props:**
- `index` â€” Slide number (used for DOM id `slide-{index}`)
- `bgIndex` â€” Selects background image (0-2 cycle through 3 golf hole photographs)
- `safeZone` â€” Enables TikTok UI chrome padding (use for all content slides)

### Background Stack (bottom to top)

| Layer | Z | Description |
|-------|---|-------------|
| Golf hole photo | 0 | Oil-painting style course photography, rotates 3 images |
| Dark overlay | 1 | `bg-[#1a3328]/60` â€” 60% opacity deep forest green |
| Radial wash | 2 | Lime glow from top: `radial-gradient(ellipse 120% 85% at 50% -25%, rgba(164,217,68,0.12), transparent 52%)` |
| Linear gradient | 2 | Top-to-bottom vignette: `linear-gradient(180deg, rgba(15,31,24,0.2), rgba(15,31,24,0.88))` |
| Content | 10 | Actual slide content |

### Safe Zone Padding

TikTok's player UI crops content at the edges. When `safeZone={true}`:

```
Top:    160px  (notch + status bar + caption area)
Bottom: 280px  (playback controls + nav bar)
Left:    50px  (side UI elements)
Right:  110px  (like/comment/share buttons)
```

Default (non-safe-zone): `px-6 pb-10 pt-9`

**Rule:** Always use `safeZone` for slides with readable content (tables, text). Non-safe-zone is only for purely decorative or bleed-edge imagery.

---

## Color Palette

The `tt` constant in `tiktok-slide-shell.tsx` exports all brand colors:

```typescript
export const tt = {
  text:  "text-[#f5f2e8]",                // Primary foreground â€” warm off-white
  muted: "text-[#aabeb4]",                // Secondary â€” sage gray
  body:  "text-[#c7d8cf]",                // Body copy â€” light sage
  lime:  "text-[#a4d944]",                // Primary accent â€” lime green
  card:  "border-[#4d6b5c] bg-[#183026]", // Card container
};
```

| Token | Hex | Usage |
|-------|-----|-------|
| Lime (primary) | `#a4d944` | Headlines, callouts, odds values, section labels, URLs |
| Text (foreground) | `#f5f2e8` | Body text, player names, prices |
| Muted | `#aabeb4` | Column headers, OWGR values, rank numbers |
| Body | `#c7d8cf` | Subtitles, descriptions, parentheticals |
| Card BG | `#183026` | Table/card background |
| Card border | `#4d6b5c` | Borders, dividers (use `/50` for headers, `/30` for rows) |
| Dark green | `#1a3328` | Overlay base tint |
| Deep BG | `#0f1f18` | Viewer page background |

**Do not introduce new colors.** All new slides must use only these tokens.

---

## Checklist for New Slides

When creating any new TikTok slide, verify:

- [ ] Uses `<TikTokSlideShell>` with `safeZone` prop
- [ ] Only uses colors from the `tt` palette â€” no new colors
- [ ] Edosz font only for brand name and large display text, never body
- [ ] Drop shadows on all text over background images
- [ ] Tables use the card pattern: `rounded-[1.25rem] border-[3px] border-[#4d6b5c] bg-[#183026]`
- [ ] Text is legible at 1080x1920 (nothing below ~`2rem` for readable content)
- [ ] Safe zone padding keeps content away from TikTok UI chrome
- [ ] Export script created and added to `package.json`
- [ ] Deck added to `tiktok-slideshow-viewer.html`
- [ ] Footer includes `underparfantasy.com` in lime with drop shadow
- [ ] Tested export produces correct PNGs via Playwright

## References

- `references/typography.md`: load when choosing fonts, text sizes, text effects or wrapping
- `references/slide_types.md`: load when building hook slides or odds/table slides
- `references/export_pipeline.md`: load when exporting PNGs, writing an export script, naming files or generating static data
- `references/viewer_and_slidefill.md`: load when adding a deck to the viewer or using the SlideFill helper
- `references/common_patterns.md`: load when you need copy-paste JSX for section headers, table rows or the footer URL
