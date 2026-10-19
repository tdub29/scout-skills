---
name: animation-systems
description: Use when designing or implementing product-grade web motion like Stripe, Linear, Apple, and Vercel. Covers motion principles, easing/duration defaults, choreography patterns, scroll/hover interactions, performance, accessibility (reduced motion), and implementation guidance.
---

# Animation Systems (Stripe Ã— Linear Ã— Apple Ã— Vercel)

This skill helps you ship **tasteful, product-grade motion**.
Not â€œmore animation.â€
**Better animation**: clarity, hierarchy, feedback, and delightâ€”without jank.

---

## The goals (why motion exists)
Use animation to:
1) **Explain hierarchy** (what matters)
2) **Confirm action** (feedback)
3) **Guide attention** (where to look next)
4) **Maintain continuity** (spatial relationships)
5) **Add polish** (craft signals)

If an animation doesnâ€™t serve one of these, delete it.

---

## The Stripe/Linear/Apple/Vercel style (shared traits)

### 1) Restraint
- Fewer animations, better chosen.
- One strong hero moment; the rest is supporting motion.

### 2) Clear choreography
- Primary element moves first.
- Secondary elements follow with small stagger.
- Motion establishes a â€œreading order.â€

### 3) Physical but not cartoony
- Use easing that feels **human** (soft acceleration + gentle settle).
- Avoid bouncy defaults for serious product UI.

### 4) Texture + depth (subtle)
- Small parallax, soft shadows, blur fades, light beams.
- Avoid heavy 3D unless itâ€™s the hero.

---

## Motion primitives (build these first)
Think in primitives you can reuse everywhere.

### A) Fade + rise (default entrance)
Use for: text blocks, cards, modals.
- Opacity: 0 â†’ 1
- Y: 12â€“24px â†’ 0
- Duration: 300â€“700ms depending on size

### B) Scale + fade (micro emphasis)
Use for: popovers, toasts, selected states.
- Scale: 0.98 â†’ 1
- Opacity: 0 â†’ 1

### C) Slide (navigation)
Use for: drawers, step transitions.
- Use transform translate; avoid animating layout.

### D) Morph / shared element (high craft)
Use for: tab indicators, expanding cards.
- Requires consistent geometry + measured layout.

---

## Defaults (practical numbers)
Use these as a starting system.

### Durations (rule of thumb)
- Micro (hover/press): **120â€“200ms**
- UI state change (toggle, select): **180â€“260ms**
- Small transitions (popover, toast): **220â€“320ms**
- Page section entrance: **400â€“800ms**
- Hero sequences: **800â€“1600ms** (with internal beats)

### Easing (safe set)
Pick a small set and reuse.
- UI: **ease-out** with gentle settle
- Emphasis: slightly stronger ease
- Entering: ease-out
- Exiting: ease-in (faster)

If implementing:
- Use your animation libraryâ€™s â€œpower2.out / expo.outâ€ equivalents.
- Avoid elastic/bounce unless brand is playful.

### Stagger
- 40â€“90ms per element (text lines/cards)
- Use smaller stagger on mobile

---

## Choreography patterns

### 1) â€œHero â†’ supporting elementsâ€
- Hero visual animates in first.
- Headline appears next.
- CTA appears last.

### 2) â€œSection reveal on scrollâ€
- Trigger when section is ~20â€“30% visible.
- Animate once (donâ€™t replay on tiny scroll).

### 3) â€œHover: lift + glowâ€
- Y: -2 to -6px
- Shadow: subtle increase
- Optional: border/gradient glow

### 4) â€œFocus ring + micro shiftâ€
- For form fields: focus ring + tiny scale/translate for responsiveness.

---

## Performance rules (nonâ€‘negotiable)

### Animate the right properties
Prefer:
- `transform` (translate/scale/rotate)
- `opacity`

Avoid (unless necessary):
- width/height/top/left
- expensive filters on large areas

### Respect the GPU
- Clamp device pixel ratio in heavy canvases (1â€“2)
- Keep blur subtle and small
- Avoid many simultaneous animated shadows

### Reduce reflows
- Donâ€™t measure layout every frame.
- For scroll effects, use a library that batches reads/writes.

---

## Accessibility: Reduced Motion
Always support `prefers-reduced-motion`.

Policy:
- Keep content visible.
- Replace motion with **instant state** + subtle opacity.
- Disable scroll-scrub/pin.

Ask the user:
- â€œDo you want a reduced-motion mode that disables all non-essential motion?â€

---

## Implementation guidance (library-agnostic)

### For simple sites
- CSS transitions for small hovers/toggles.
- Use a single motion library (GSAP or Framer Motion) for complex sequences.

### For product sites
- Create a motion token set:
  - durations
  - easing curves
  - standard offsets (8/16/24px)
  - stagger defaults

### For hero moments
- Use timelines (or keyframes) with labeled beats.
- Lock camera/scene movement first, then layer text.

---

## What to ask the user
- Whatâ€™s the brand lane: Stripe (polished), Linear (minimal), Apple (cinematic), Vercel (developer/product)?
- What are the key moments? (hero, scroll story, hover cards, nav transitions)
- Any performance constraints? (mobile, low-end devices)
- Reduced motion requirements?

---

## Output format (when asked to â€œadd Stripe/Linear-style animationâ€)
Return:
1) Motion goals (what weâ€™re trying to communicate)
2) Motion tokens (durations + easing + offsets)
3) A choreography plan (timeline beats)
4) Implementation notes (perf + reduced motion)
5) A small code recipe (CSS or GSAP/Framer depending on stack)
