# ðŸ§¬ Clone Site

**URL â†’ Pixel-Perfect Next.js Replica in Minutes**

Point this skill at any website URL and it reverse-engineers the entire thing â€” design tokens, assets, interactions, responsive behavior â€” then rebuilds it as a production-ready Next.js app using parallel builder agents.

This isn't "screenshot â†’ approximate HTML." This is computed-style extraction, section-by-section specification, and parallel construction with visual QA diffing against the original.

---

## What It Does

```
Input:  "Clone yourcompany.com"
Output: Pixel-perfect Next.js app with real assets, exact CSS, working interactions
```

### The Pipeline

1. **ðŸ” Reconnaissance** â€” Screenshots at desktop + mobile, extracts every design token (fonts, colors, spacing) via `getComputedStyle()`, downloads all assets (images, videos, SVGs, fonts), maps page topology

2. **ðŸ—ï¸ Foundation** â€” Sets up Next.js with the target's exact fonts, colors, and global styles. Configures Tailwind, shadcn/ui primitives, and any detected smooth scroll libraries (Lenis, Locomotive, etc.)

3. **ðŸ“‹ Component Specification** â€” Writes detailed spec files for each section with exact CSS values, interaction models (click-driven vs scroll-driven vs time-driven), multi-state behaviors, and responsive breakpoints

4. **âš¡ Parallel Build** â€” Dispatches builder agents in isolated git worktrees, one per section (complex sections get split into sub-component agents). Extraction continues while builders work.

5. **ðŸ”— Assembly & QA** â€” Merges all worktrees, wires up the page, runs visual diff comparison against the original at multiple viewports. Fixes discrepancies until pixel-perfect.

### What Makes This Different

- **Computed styles, not guesses.** Every CSS value comes from `getComputedStyle()` on the live site â€” not "it looks like `text-lg`"
- **Behavior extraction.** Captures scroll-triggered animations, hover states, tab switching, parallax, sticky headers â€” not just static layouts
- **Parallel construction.** Builder agents work simultaneously in git worktrees. A 10-section page doesn't take 10x as long.
- **Specification files as contracts.** Every component gets a detailed spec file before any builder touches it. Auditable, reproducible, debuggable.
- **Multi-state capture.** Clicks every tab, scrolls through every trigger point, hovers every interactive element. Extracts ALL states, not just the default.
- **Visual QA pass.** Side-by-side comparison at desktop and mobile after assembly. Not "done" until it matches.

---

## Requirements

- **Claude Code** with Chrome MCP enabled (`claude --chrome`)
- **Node.js 20+**
- A Next.js + Tailwind v4 + shadcn/ui scaffold (the skill expects this as the base project)

## Quick Start

### 1. Set up the project scaffold

```bash
npx create-next-app@latest my-clone --typescript --tailwind --app
cd my-clone
npx shadcn@latest init
npm install
```

### 2. Add the skill to Claude Code

Copy `SKILL.md` to your Claude Code agents or skills directory.

### 3. Clone a site

```
You: "Clone yourcompany.com"
```

Or create a `TARGET.md` with the URL and scope, then invoke the skill.

---

## How Parallel Building Works

The skill operates like a **construction foreman**:

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚   Recon &    â”‚  â† You (the foreman) inspect each section
â”‚  Extraction  â”‚
â””â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”˜
       â”‚
       â”œâ”€â”€ Section 1 spec written â†’ dispatch Builder Agent A (worktree)
       â”œâ”€â”€ Section 2 spec written â†’ dispatch Builder Agent B (worktree)
       â”œâ”€â”€ Section 3 spec written â†’ dispatch Builder Agent C (worktree)
       â”‚                            â†‘ all building in parallel
       â–¼
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚   Assembly   â”‚  â† Merge worktrees, wire up page, visual QA
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

Each builder receives:
- The full component spec (inline, not a file reference)
- Section screenshot
- Asset paths (`public/images/...`)
- Shared component imports (icons, utilities)
- TypeScript verification requirement (`npx tsc --noEmit`)

Builders never have to read external docs or guess values. Everything they need is in the prompt.

---

## Component Spec Format

Every section gets a specification file before any code is written:

```markdown
# HeroSection Specification

## Overview
- Target file: src/components/HeroSection.tsx
- Interaction model: scroll-driven

## Computed Styles (from getComputedStyle)
### Container
- display: flex
- padding: 80px 64px
- maxWidth: 1440px
- background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 100%)

## States & Behaviors
### Scroll-triggered parallax
- Trigger: scroll position > 0
- Background layer: translateY at 0.3x scroll rate
- Foreground: translateY at 0.6x scroll rate
- Transition: none (frame-synced via requestAnimationFrame)

## Assets
- Hero image: public/images/hero-dashboard.webp
- Background pattern: public/images/hero-bg-pattern.svg

## Responsive
- Desktop (1440px): 2-column, image right
- Mobile (390px): stack, image below text, full-width
```

---

## The Extraction Arsenal

The skill includes battle-tested JavaScript extraction scripts that run via Chrome MCP:

- **Asset discovery** â€” Enumerates all `<img>`, `<video>`, background-images, inline SVGs, and fonts on the page. Detects layered compositions (multiple images stacked in one container).
- **CSS extraction** â€” Deep `getComputedStyle()` capture for 50+ properties per element, walking up to 4 levels of DOM depth.
- **Behavior detection** â€” Scroll sweep, click sweep, hover sweep, responsive sweep at 3 viewport widths.

---

## What It Catches That You'd Miss

| Pattern | What happens if missed |
|---------|----------------------|
| Scroll-driven tabs vs click-driven tabs | Complete rewrite (hours wasted) |
| Layered images (background + overlay) | Section looks empty/broken |
| Smooth scroll library (Lenis) | Page "feels wrong" even if it looks right |
| Multi-state content (tabs with different cards) | Only default tab's content appears |
| Header scroll transition | Nav looks static and cheap |
| CSS `animation-timeline` | Scroll animations don't work |
| Video/Lottie elements | Built as static HTML mockups |

---

## Output

```
my-clone/
â”œâ”€â”€ public/
â”‚   â”œâ”€â”€ images/          # All downloaded assets
â”‚   â”œâ”€â”€ videos/          # Video assets
â”‚   â””â”€â”€ seo/             # Favicons, OG images
â”œâ”€â”€ src/
â”‚   â”œâ”€â”€ app/
â”‚   â”‚   â”œâ”€â”€ layout.tsx   # Configured with target's fonts, metadata
â”‚   â”‚   â”œâ”€â”€ globals.css  # Target's exact color tokens, animations
â”‚   â”‚   â””â”€â”€ page.tsx     # All sections assembled
â”‚   â”œâ”€â”€ components/      # One component per section
â”‚   â””â”€â”€ types/           # TypeScript interfaces
â”œâ”€â”€ docs/
â”‚   â”œâ”€â”€ design-references/  # Screenshots at multiple viewports
â”‚   â””â”€â”€ research/
â”‚       â”œâ”€â”€ PAGE_TOPOLOGY.md
â”‚       â”œâ”€â”€ BEHAVIORS.md
â”‚       â””â”€â”€ components/     # Spec file per component
â””â”€â”€ TARGET.md
```

Run `npm run dev` and you have a working clone.

---

## Limitations & Honest Caveats

- **Server-rendered dynamic content** (personalized feeds, auth-gated pages) won't be captured â€” this clones what's publicly visible
- **Complex JS applications** (SPAs with client-side routing, real-time data) are better suited to different approaches â€” this excels at marketing sites, landing pages, and content-heavy pages
- **Third-party widgets** (Intercom chat, embedded forms) are identified but not replicated
- **Exact font rendering** may vary slightly across OS/browser combinations

---

## File Structure

```
clone-site/
â”œâ”€â”€ README.md              # This file
â”œâ”€â”€ SKILL.md               # Claude Code skill instructions
â””â”€â”€ references/
    â””â”€â”€ FULL_METHODOLOGY.md  # Complete technical methodology (~500 lines)
```

---

## License

MIT â€” See [LICENSE](../LICENSE) in the repository root.


---

<div align="center">

**ðŸ§  [Want these built and managed for you? â†’](https://singlebrain.com/?utm_source=github&utm_medium=skill_repo&utm_campaign=ai_marketing_skills)**

*This is how we build agents at [Single Brain](https://singlebrain.com/?utm_source=github&utm_medium=skill_repo&utm_campaign=ai_marketing_skills) for our clients.*

[Single Grain](https://www.singlegrain.com/?utm_source=github&utm_medium=skill_repo&utm_campaign=ai_marketing_skills) Â· our marketing agency

ðŸ“¬ **[Level up your marketing with 14,000+ marketers and founders â†’](https://levelingup.beehiiv.com/subscribe)** *(free)*

</div>
