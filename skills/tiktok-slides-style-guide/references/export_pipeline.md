# TikTok Slide Export Pipeline

## Export Pipeline

Slides are exported via Playwright (Chromium) as PNGs.

### Key Pipeline Details

- **Server:** Dev server on port 3010 via `start-server-and-test`
- **Browser context:** `bypassCSP: true` (required for font injection)
- **Font injection:** Edosz loaded as base64 data URI via `page.addStyleTag()`
- **Wait strategy:** `document.fonts.ready` + 500ms delay per slide
- **DOM cleanup:** Removes Next.js portals, toast notifications, dev overlays before screenshot
- **Lock file:** Always `rm -f .next/dev/lock` before starting dev server

### Creating a New Export Script

Minimal export script (`scripts/export-tiktok-{name}.ts`):

```typescript
process.env.TIKTOK_SLIDES_PATH = "/promo/tiktok/{name}";
process.env.TIKTOK_SLIDES_OUT = "tiktok/{name}";
import("./export-tiktok-slides-core");
```

Add to `package.json`:
```json
"export:tiktok-{name}": "npx start-server-and-test dev:tiktok-export http://127.0.0.1:3010/promo/tiktok/{name} \"npx tsx scripts/export-tiktok-{name}.ts\""
```

### Image File Naming Convention

All exported slide PNGs use the `n_` prefix pattern:

```
n_{NN}_{descriptive-slug}.png
```

- `n_` â€” fixed prefix (stands for "numbered")
- `{NN}` â€” zero-padded slide index (`01`, `02`, etc.)
- `{descriptive-slug}` â€” kebab-case description of slide content

**Examples:**
```
n_01_masters-odds-favorites.png
n_02_masters-odds-sleepers.png
n_03_masters-odds-full-field-p01-of-05.png
n_01_porkiest-bmi-28-plus.png
n_06_porkiest-bmi-under-23.png
```

Never use generic `slide-01.png` names for final exports. After the initial Playwright export (which produces `slide-XX.png` by default), rename files to the `n_` convention and update the viewer's `files` array accordingly.

### Static Data Generation

For data-driven slides, use the pattern from odds slides:
1. Create a `generate-tiktok-{name}-data.ts` script that queries the DB
2. Output a static `.ts` file that the component imports
3. Run the generator before exporting: `npm run generate:tiktok-{name}-data && npm run export:tiktok-{name}`

This keeps slides static (no DB dependency at render time) while allowing easy data refresh.
