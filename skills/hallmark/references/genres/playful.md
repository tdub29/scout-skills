# Genre â€” playful

For the consumer / friendly / onboarding-led page. Soft surfaces, mild colour, motion that responds to hover, friendlier voice. Closer to Notion's marketing or Figma's onboarding than to Stripe's API docs.

## When to pick it

Brief mentions any of: *fun, consumer, casual, family, kids, friendly, approachable, onboarding-heavy, community, social, tactile-but-soft, post-Linear-soft*. Pick playful sparingly â€” most consumer briefs still belong to editorial (warm-paper, hand-set) unless the user explicitly asks for *softer* and *friendlier*.

## Themes that belong

`Hum` (vibrant, alive) is the genre's canonical theme â€” the post-Brilliant-alive register: multi-accent cream + pear + cyan + coral, mandatory motion, a single character moment. Pick it when the brief wants "feels alive in the room with you." For the quieter, more restrained end of friendly â€” "friendly but soft" rather than "alive" â€” reach instead for modern-minimal (Coral): a single low-chroma accent on warm paper, smooth easings, motion optional.

`Hum` is the catalog's only **rounded-sans-multi-accent** theme â€” it relaxes several playful defaults: bouncy spring easings are allowed (and canonical) on its primary CTA, accent chroma goes higher than 0.16, and motion is mandatory not optional. It answers a specific brief: a learning platform for curious adults, a daily-curiosity app, a habit tracker with character â€” products that should feel warm and alive, not merely tidy.

## Voice

- **Display** â€” Geist Sans 600 with tighter tracking (`-0.025em`), or a bricolage-style display weighted at 700. Friendly, not childish.
- **Body** â€” Geist Sans 400 in a slightly muted ink (not pure black).
- **Accent** â€” soft indigo, warm coral, or muted rose at low chroma. Always low â€” never the saturated consumer-app pop.
- **Layout** â€” slightly rounded surfaces, soft drop shadows, friendlier card edges (12 px radius is the upper bound).
- **Motion** â€” responsive on hover (cards lift slightly). One small bounce-free reveal per section. No spring physics on UI state.
- **Copy tone** â€” warm, direct, specific. Avoid quirk for quirk's sake. *"Made for teams who write together."* over *"For the squad âœ¨"*.

## What this genre allows

- **Soft drop shadows** on cards (`0 8px 24px -10px <accent at low chroma>`). Restrained.
- **12 px radius** on cards, 8 px on inputs, 999 px on pills.
- **Hover-lift animations** on cards (`translateY(-2px)` + shadow expansion).
- **Mild tinted backgrounds** on alternating sections (paper-2 vs paper, with a tinted band).
- **Soft accent colours** â€” `oklch(50% 0.13 282)` (indigo) and similar, never above 0.16 chroma.

## What this genre disallows

- **Saturated consumer-app pinks / purples** â€” playful keeps chroma low by default. **Hum is the documented exception** â€” pear-yellow at chroma 0.18, sky-cyan at 0.18, coral at 0.24 are allowed and canonical for Hum builds only.
- **Emoji-as-decoration** â€” emoji can appear in copy ("we built X ðŸŒ±") but never as visual ornament replacing iconography.
- **Comic Sans, Comic Neue, anything that signals "we're zany"** â€” playful stays sophisticated, even at full vibrancy.
- **Bouncy / overshoot easings** â€” playful uses smooth easings by default. **Hum is the documented exception** â€” spring overshoot (`cubic-bezier(0.34, 1.56, 0.64, 1)`) is canonical on the primary CTA and character moment (one each per page).
- **Glassmorphism** â€” banned across all genres.
- **Gradient text** â€” gate 2 universal. Stays banned.

## Voice fixtures

- *"Made for teams who write together."* â€” Hum voice
- *"Soft, but exact."* â€” Hum voice
- *"Software can be soft and exact at once. That's the trick."* â€” Hum voice
- *"A small tool, gently opinionated."* â€” Hum voice
- *"Your daily 30-second curio."* â€” Hum voice
- *"Get really good at one thing this quarter."* â€” Hum voice
- *"Notice yourself, in 30 seconds."* â€” Hum voice
- *"Learn something genuinely new today."* â€” Hum voice

## Nav and footer voice

- **Default nav:** N7 Brutal slab â€” heavy uppercase wordmark + tracked uppercase links + 2 px border-bottom. The voice is loud but composed.
- **Acceptable also:** N1 Wordmark + 2 links (when destinations are minimal); N3 Side-rail (when the page is long-scroll and section-numbered, e.g. Studio).
- **Default footer:** Ft8 Marquee scroll â€” horizontal repeating tagline + dot separator. Honours `prefers-reduced-motion: reduce`.
- **Acceptable also:** Ft5 Statement; Ft3 Index columns (only when the page is a hub).
- **Banned for playful:** N5 Floating pill (modern-minimal vocabulary, fights the loud register); N6 Newspaper masthead (editorial); Ft6 Letter close (warm-quiet voice; wrong genre).

See [`component-cookbook.md`](../component-cookbook.md) Â§ Navigation and Â§ Footers for the full archetypes + code.

## Stamp signature

```css
/* Hallmark Â· genre: playful Â· macrostructure: <name> Â· theme: <name> Â· enrichment: <tier> Â· nav: <N#> Â· footer: <Ft#> */
```

## Reference register

The aesthetic to match: soft surfaces, low-chroma colour, friendly-but-restrained type, hover-responsive motion. The post-Linear soft school. Never childish, never quirk-for-quirk.
