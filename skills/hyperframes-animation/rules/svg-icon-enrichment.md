---
name: svg-icon-enrichment
description: Animate internal SVG elements (rotating hands, opening blades, pulsing dots, dash flows) to make icons feel alive without replacing them.
metadata:
  tags: svg, icon, animation, internal, micro-animation, pulse, rotation
---

# SVG Icon Enrichment

Treats an SVG icon as a composition of animated PARTS, not an opaque image. Each meaningful internal element (a clock hand, scissor blade, recording dot, data line) gets its own micro-animation, targeted by id. Distinct from [svg-path-draw](svg-path-draw.md) (which animates the OUTLINE drawing) â€” enrichment animates INTERNAL PARTS, ideally after the outline has drawn.

Four signature patterns:

| Pattern     | Use For                            | Math                                  | Tip                                |
| ----------- | ---------------------------------- | ------------------------------------- | ---------------------------------- |
| Rotation    | Clock, gear, loader, dial          | `rotate(deg cx cy)` attribute, linear | see the transform-center gotcha    |
| Oscillation | Scissors, wings, toggle            | `rotate(Â±sinÂ·amp)` on opposing groups | opposite signs on the two parts    |
| Pulse       | Recording dot, heart, notification | `scale(1 + sinÂ·amp)` + opacity        | ring lags dot by Ï€/2 for ripple    |
| Dash flow   | Cutting line, data stream          | `strokeDashoffset` linear via time    | negative for Lâ†’R, positive for Râ†’L |

## â— The transform-center gotcha

**For rotation around an explicit point inside an SVG, use the SVG `transform` ATTRIBUTE, not CSS transform**: `el.setAttribute("transform", `rotate(${deg} ${cx} ${cy})`)`. The CSS combination `transform: rotate(...)` + `transform-origin: 60px 60px` + `transform-box: fill-box` interprets the origin in the element's OWN **bbox-local** coordinates, NOT viewBox coordinates. For a thin `<line>` (whose bbox is the line's narrow envelope), `60 60` bbox-local is a point OUTSIDE the line â€” the hand flies along an off-center arc instead of rotating in place. Same trap for small inner shapes (a dot circle whose bbox is the small circle, not the full viewBox).

**Scaling around a center point**: same attribute route â€” `el.setAttribute("transform", `translate(${cx} ${cy}) scale(${s}) translate(-${cx} -${cy})`)`.

## Recipe

```html
<!-- inside a standard scene clip â€” named children are the animation targets -->
<svg class="icon-svg" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
  <circle cx="60" cy="60" r="50" fill="none" stroke="{accentColor}" stroke-width="6" />
  <line
    id="hand-min"
    x1="60"
    y1="60"
    x2="60"
    y2="22"
    stroke="{textColor}"
    stroke-width="6"
    stroke-linecap="round"
  />
  <line
    id="hand-sec"
    x1="60"
    y1="60"
    x2="60"
    y2="30"
    stroke="{recordColor}"
    stroke-width="3"
    stroke-linecap="round"
  />
  <circle cx="60" cy="60" r="6" fill="{textColor}" />
</svg>
<!-- pulse icon: #rec-ring + #rec-dot circles; dash-flow: a <line> with stroke-dasharray="14 12" -->
```

```js
// Pattern 1 â€” Rotation. Proxy tween â†’ SVG transform attribute (explicit center, see gotcha).
const hand = document.getElementById("hand-min");
const minState = { deg: 0 };
tl.to(
  minState,
  {
    deg: 360 * MIN_REVOLUTIONS,
    duration: TOTAL_DURATION,
    ease: "none", // linear motion is the point
    onUpdate: () => hand.setAttribute("transform", `rotate(${minState.deg} 60 60)`),
  },
  0,
);
// second hand: same shape with SEC_REVOLUTIONS (visibly faster).

// Pattern 3 â€” Pulse. One phase proxy drives dot + ring, ring offset by Ï€/2.
const dot = document.getElementById("rec-dot");
const ring = document.getElementById("rec-ring");
const pulse = { p: 0 };
tl.to(
  pulse,
  {
    p: Math.PI * 2 * PULSE_CYCLES,
    duration: TOTAL_DURATION,
    ease: "none", // sine handles the curve
    onUpdate: () => {
      const sD = 1 + Math.sin(pulse.p) * PULSE_DOT_AMP;
      const sR = 1 + Math.sin(pulse.p + Math.PI / 2) * PULSE_RING_AMP;
      dot.setAttribute("transform", `translate(60 60) scale(${sD}) translate(-60 -60)`);
      ring.setAttribute("transform", `translate(60 60) scale(${sR}) translate(-60 -60)`);
      ring.style.opacity = String(
        PULSE_RING_OPACITY_BASE + Math.sin(pulse.p) * PULSE_RING_OPACITY_AMP,
      );
    },
  },
  0,
);

// Pattern 4 â€” Dash flow. Linear offset tween on a dashed stroke.
const flowState = { offset: 0 };
tl.to(
  flowState,
  {
    offset: DASH_FLOW_TOTAL_OFFSET, // negative = Lâ†’R
    duration: TOTAL_DURATION,
    ease: "none",
    onUpdate: () => {
      document.getElementById("data-flow").style.strokeDashoffset = String(flowState.offset);
    },
  },
  0,
);
```

## Variations

- **Stroke draw â†’ enrichment chain** â€” draw the outline first via [svg-path-draw](svg-path-draw.md) (phase 1, `0 â†’ OUTLINE_DUR`), then start enrichment at `OUTLINE_DUR`: the icon "wakes up" after assembly.
- **Per-icon entry stagger** â€” for a row of icons, each icon's enrichment starts as it fades in, not synchronized.

## Values

| token                           | range                | notes                                                                                           |
| ------------------------------- | -------------------- | ----------------------------------------------------------------------------------------------- |
| MIN_REVOLUTIONS                 | 0.5â€“2.0              | avoid integer revolutions if the end frame is visible (lands back at start)                     |
| SEC_REVOLUTIONS                 | 4â€“10                 | > MIN Ã— 3 or the speed difference doesn't read                                                  |
| PULSE_CYCLES                    | 2â€“4 over a 3â€“5s comp | â‰¥5 reads as anxious flicker; â‰¤1 reads as forgotten                                              |
| PULSE_DOT_AMP                   | 0.05â€“0.20            | 0.05 = breathing; 0.20 = throbbing                                                              |
| PULSE_RING_AMP                  | 0.04â€“0.12            | must be < PULSE_DOT_AMP or the ring overshadows the dot                                         |
| PULSE_RING_OPACITY_BASE / \_AMP | 0.4â€“0.6 / 0.3â€“0.5    | BASE âˆ’ AMP â‰¥ 0 and BASE + AMP â‰¤ 1                                                               |
| DASH_FLOW_TOTAL_OFFSET          | Â±100â€“400             | must be an integer multiple of the dash period (dash + gap) or the end frame shows a phase jump |

## Critical Constraints

- **The transform-center gotcha above** â€” SVG `transform` attribute for any rotation/scale around an explicit interior point; never CSS `transform-origin` + `transform-box: fill-box` on thin lines or small inner shapes.
- **No `requestAnimationFrame`** â€” like CSS animation, it desyncs from HF's frame-by-frame seek; continuous motion lives inside the timeline as linear proxy tweens.
- **Amplitudes subtle** â€” icons are decorative, not headlines; calibrate rotation speed against composition length, not absolute time.
- **Phase-offset the parts** â€” minute vs second hand at different speeds, ring lagging dot by Ï€/2. Pure sync looks mechanical.
- **`stroke-linecap: round`** on flowing/dashed lines for clean dash edges.
- **Climax dwell â‰¥1s** â€” if the enrichment is the headline beat, the composition continues â‰¥1s after the most dramatic moment.

## See also

`svg-path-draw` (outline draws first, enrichment second) Â· `orbit-3d-entry` (orbiting items are enriched icons) Â· `sine-wave-loop` (the whole icon floats while internal parts animate).
