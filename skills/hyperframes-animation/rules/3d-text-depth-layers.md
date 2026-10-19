---
name: 3d-text-depth-layers
description: Multiple offset text layers create a stacked 3D shadow / extrusion effect on large typography â€” more impactful than CSS text-shadow because each layer is a full DOM element.
metadata:
  tags: text, 3d, depth, layers, shadow, typography, stacked, extrusion
---

# 3D Text Depth Layers

The same text rendered N times at increasing offsets â€” back layers translucent, front layer full opacity and brand color â€” creates a physical "stacked extrusion" depth illusion on large typography. Distinct from `text-shadow` (which can't have per-layer hue / opacity / animation): each layer is a real DOM element.

## How It Works

A build script appends `LAYER_COUNT` copies back-to-front; each back layer sits at `translate(i Ã— OFFSET_X, i Ã— OFFSET_Y)` with alpha stepping down per layer, while the front copy (`i = 0`) is `position: relative` so it defines the container size (back layers stack absolutely behind it). The default entrance cascades the layers' fades back-to-front while a proxy tween grows the offsets from 0 â†’ full, so the depth "builds forward" and lands as the last layer fades in.

## Recipe

```html
<!-- inside a standard scene clip (hyperframes-core) -->
<div class="depth-stack">
  <!-- layers injected by script â€” LAYER_COUNT copies of {label} -->
</div>
```

```css
.depth-stack {
  position: relative; /* front layer defines size; back layers stack behind */
}
.depth-text {
  font-weight: 900; /* black weight â€” thin text loses the illusion */
  font-size: HERO_FONT_SIZE;
  letter-spacing: HERO_LETTER_SPACING;
  line-height: 1;
  color: {frontColor};
}
.depth-text.is-back {
  position: absolute;
  top: 0;
  left: 0;
  pointer-events: none; /* decorative */
}
.depth-text.is-front {
  position: relative;
  z-index: 10;
}
```

```js
const stack = document.querySelector(".depth-stack");

// Build back-to-front so the FRONT (i=0) is appended LAST
for (let i = LAYER_COUNT - 1; i >= 0; i--) {
  const el = document.createElement("div");
  el.className = "depth-text " + (i === 0 ? "is-front" : "is-back");
  el.textContent = "{label}";
  if (i > 0) {
    const alpha = Math.max(BACK_ALPHA_MAX - i * BACK_ALPHA_STEP, BACK_ALPHA_MIN);
    el.style.color = `rgba({backHueRGB}, ${alpha})`; // rgba in color, NOT element opacity
    el.style.transform = `translate(${i * OFFSET_X}px, ${i * OFFSET_Y}px)`;
  }
  el.dataset.layer = String(i);
  stack.appendChild(el);
}

// Cascade entry â€” back layers fade in first, building forward
stack.querySelectorAll(".depth-text").forEach((el) => {
  const i = Number(el.dataset.layer);
  const finalAlpha = i === 0 ? 1 : Math.max(BACK_ALPHA_MAX - i * BACK_ALPHA_STEP, BACK_ALPHA_MIN);
  tl.fromTo(
    el,
    { opacity: 0 },
    { opacity: finalAlpha, duration: LAYER_FADE_DUR, ease: "power2.out" },
    LAYER_CASCADE_START + (LAYER_COUNT - 1 - i) * LAYER_CASCADE_STEP,
  );
});

// Depth grows on entry â€” offsets interpolate 0 â†’ full
const depthState = { p: 0 };
tl.to(
  depthState,
  {
    p: 1,
    duration: DEPTH_GROW_DUR,
    ease: "power2.out",
    onUpdate: () => {
      stack.querySelectorAll(".depth-text.is-back").forEach((el) => {
        const i = Number(el.dataset.layer);
        el.style.transform = `translate(${i * OFFSET_X * depthState.p}px, ${i * OFFSET_Y * depthState.p}px)`;
      });
    },
  },
  LAYER_CASCADE_START, // align with the cascade so depth lands as the last layer fades in
);
```

## Variations

- **Static depth** (single hero shot) â€” render all layers at final positions from t=0; optionally fade the whole stack in with a subtle scale (0.94â€“0.98 â†’ 1, 0.5â€“0.8s).
- **Dynamic depth pulse** â€” after the grow completes, modulate the offsets with a sine multiplier `1 + sin(p) Ã— BEAT_AMP` (BEAT_AMP 0.2â€“0.6; one beat per 0.7â€“1.5s reads as a heartbeat).
- **Color-shift back layers** â€” instead of fading to translucent, step hue/lightness per layer: `hsla(HUE_BASE âˆ’ i Ã— HUE_STEP, SAT_PCT%, LIGHT_BASE âˆ’ i Ã— LIGHT_STEP%, 1)` (HUE_STEP 4â€“12Â°; larger reads as glitch). Depth reads as a colored cast shadow.

## Values

| token               | range                    | notes                                                                  |
| ------------------- | ------------------------ | ---------------------------------------------------------------------- |
| LAYER_COUNT         | 4â€“6                      | <4 doesn't read as 3D; >6 clutters on tight kerning                    |
| OFFSET_X / OFFSET_Y | 1â€“3px each               | >4px reads as glitch / chromatic aberration, not depth                 |
| BACK_ALPHA_MAX      | 0.6â€“0.85                 | nearest back layer; >0.9 fights the front for dominance                |
| BACK_ALPHA_STEP     | 0.08â€“0.15                | small = soft gradient; large = discrete plates                         |
| BACK_ALPHA_MIN      | 0.1â€“0.2                  | floor â€” below 0.1 the deepest layer vanishes on dark backgrounds       |
| HERO_FONT_SIZE      | 60px min; 200â€“340px hero | thin/small text loses the layered illusion                             |
| HERO_LETTER_SPACING | âˆ’0.03emâ€“0                | tighter makes offsets read as depth, not repetition                    |
| LAYER_CASCADE_STEP  | 0.04â€“0.10s               | smaller â‰ˆ simultaneous; larger feels stepped                           |
| LAYER_FADE_DUR      | 0.3â€“0.6s                 | per-layer fade                                                         |
| DEPTH_GROW_DUR      | 0.4â€“0.8s                 | â‰ˆ `LAYER_FADE_DUR Ã— LAYER_COUNT / 2` so depth lands with the last fade |

## Critical Constraints

- **Offset direction implies light direction** â€” `(+x, +y)` = light upper-left, `(-x, +y)` = upper-right; one sign convention for the whole composition.
- **Back layers translucent OR darker â€” never more saturated than the front** (reads as a halo, not depth).
- **Set back-layer color via `rgba()` in `color`, not element `opacity`** â€” opacity fades the whole rendered glyph including any shadow.
- **Front layer `position: relative` defines container size**; back layers absolute with `pointer-events: none`; offsets via `transform: translate()`, never `top`/`left`.
- **No CSS `text-shadow` alongside layered depth** â€” they compound and over-extrude.
- **No per-letter animation on top of the stack** â€” hacker-flip / typewriter over 6-layer depth is chaos; drop to 2â€“3 layers or apply depth only to the static post-reveal state.

## See also

`counting-dynamic-scale` (counter rendered with depth layers) Â· `sine-wave-loop` (idle breathing on the front layer post-reveal) Â· `center-outward-expansion` (depth-stacked wordmark after the burst lands).
