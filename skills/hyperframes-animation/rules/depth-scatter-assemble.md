---
name: depth-scatter-assemble
description: N elements scatter into / reassemble from a rotating 3D depth-cloud, each starting at a deterministic index-derived 3D offset and settling to a clean flat layout.
metadata:
  tags: 3d, scatter, assemble, depth, cloud, tumble, kinetic, letter, fragment, logo, reassemble
---

# Depth Scatter â†” Assemble

N elements (glyphs, cards, logo fragments) fly in from a rotating 3D depth-cloud and lock into a flat layout â€” or the reverse. Each element has its OWN index-derived point in the cloud (translateZ depth + rotateX/Y tumble + x/y scatter). Distinct from `orbit-3d-entry` (flip-in then continuous orbit) and `center-outward-expansion` (flat burst from one shared center): here the resolve is a flat assembled layout.

## How It Works

Each element's flat target lives in `data-target-x/y`; its scattered state is pure trig on its index â€” golden-angle spread, stepped depth â€” so the cloud is byte-identical every render with no `Math.random`:

```js
const GOLDEN = Math.PI * (3 - Math.sqrt(5)); // ~2.39943 rad â€” even spread, no clumping
const a = i * GOLDEN;
const scatterX = Math.cos(a) * RADIUS;
const scatterY = Math.sin(a) * RADIUS;
const scatterZ = Z_NEAR - (i / (n - 1)) * (Z_NEAR - Z_FAR); // stepped depth
const rotX = Math.sin(a) * TUMBLE;
const rotY = Math.cos(a) * TUMBLE;
```

Elements are PARKED at their scatter points (`gsap.set`, opacity 0) before any tween, then each tweens to its flat target while the whole stage slowly rotates so the scatter has life before it locks. Requires `perspective` on the scene root and `preserve-3d` on the stage AND each element, or depth + tumble flatten to a 2D scale.

## Recipe

```html
<!-- inside a standard scene clip (hyperframes-core) -->
<div class="cloud-stage">
  <div class="frag" data-target-x="-260" data-target-y="0">{glyph1}</div>
  <div class="frag" data-target-x="-130" data-target-y="0">{glyph2}</div>
  <!-- â€¦ one .frag per glyph / fragment â€¦ -->
</div>
```

```css
.scene-root {
  display: grid;
  place-items: center;
  perspective: 1400px; /* REQUIRED */
}
.cloud-stage {
  position: relative;
  display: grid;
  place-items: center;
  transform-style: preserve-3d;
  will-change: transform;
}
.frag {
  position: absolute;
  top: 50%;
  left: 50%;
  transform-style: preserve-3d;
  backface-visibility: hidden; /* hides the mirrored face mid-tumble */
  will-change: transform, opacity;
}
```

```js
const frags = Array.from(document.querySelectorAll(".frag"));
const n = frags.length;
const GOLDEN = Math.PI * (3 - Math.sqrt(5));

// 1) Park every fragment in the cloud BEFORE any tween fires
const scatter = frags.map((el, i) => {
  const a = i * GOLDEN;
  const depthT = n > 1 ? i / (n - 1) : 0;
  return {
    x: Math.cos(a) * RADIUS,
    y: Math.sin(a) * RADIUS,
    z: Z_NEAR - depthT * (Z_NEAR - Z_FAR),
    rotationX: Math.sin(a) * TUMBLE,
    rotationY: Math.cos(a) * TUMBLE,
  };
});
frags.forEach((el, i) => gsap.set(el, { xPercent: -50, yPercent: -50, ...scatter[i], opacity: 0 }));

// 2) The cloud rotates so the scatter has life during assembly
tl.to(
  ".cloud-stage",
  { rotationY: CLOUD_SPIN_DEG, duration: CLOUD_SPIN_DUR, ease: "power1.out" },
  0,
);

// 3) ASSEMBLE â€” cloud point â†’ flat target, index stagger = cloud collapsing inward
frags.forEach((el, i) => {
  tl.to(
    el,
    {
      x: Number(el.dataset.targetX),
      y: Number(el.dataset.targetY),
      z: 0,
      rotationX: 0,
      rotationY: 0,
      opacity: 1,
      duration: ASSEMBLE_DUR,
      ease: ASSEMBLE_EASE,
    },
    i * STAGGER,
  );
});
```

## Variations

- **Tumble-swap** (the beat-change hand-off): two glyph sets share the cloud; ONE shared 0â†’1 progress tween drives both in its `onUpdate` â€” outgoing lerps layoutâ†’cloud with `opacity: 1âˆ’p`, incoming lerps cloudâ†’layout with `opacity: p`. Two separate tweens drift out of phase under seek and the cross stops reading as one hand-off. Inject per-glyph spans per phrase at setup (measure advance widths after `document.fonts.ready` â€” single-scene only).
- **Radial letter-explode â†’ resolve**: flat-plane special case â€” `Z_NEAR = Z_FAR = 0`, small `TUMBLE`; reverse the assemble for the explode. Pure in-plane.
- **Scatter-OUT**: reverse assemble (layout â†’ cloud, opacity 1â†’0) ONLY as the composition's final beat â€” mid-shot it reads as the shot ending.
- **Parallax lockup**: back layers get deeper `|Z_FAR|` + longer `ASSEMBLE_DUR`, foreground shallower/shorter â€” depth-speeded slide-in that locks into the logo.

## Values

| token                  | range                 | notes                                                                         |
| ---------------------- | --------------------- | ----------------------------------------------------------------------------- |
| n                      | 4â€“14 (fragments 4â€“9)  | above ~14 individual paths stop reading                                       |
| RADIUS                 | 250â€“700px             | keep the farthest scatter in frame or fragments pop in with no travel         |
| Z_NEAR / Z_FAR         | +150â€¦+450 / âˆ’150â€¦âˆ’500 | large `\|z\|` needs a wider `perspective` or fragments smear                  |
| TUMBLE                 | 40â€“110Â°               | past 90Â° glyphs show blank mid-tween (intended); cap ~80Â° for one-faced cards |
| ASSEMBLE_DUR           | 0.7â€“1.4s              |                                                                               |
| ASSEMBLE_EASE          | `power3.out` default  | `expo.out` snaps, `back.out(1.4)` seats with overshoot; never `in`            |
| STAGGER                | 0.03â€“0.09s            | `n Ã— STAGGER < ASSEMBLE_DUR` â€” one collapsing motion, not a queue             |
| CLOUD_SPIN_DEG / \_DUR | 15â€“60Â° over â‰¥ dur     | gentle life; too fast competes with the assembly                              |
| SWAP_DUR               | 0.5â€“1.0s              | on the beat boundary; shorter = hard cross                                    |

## Critical Constraints

- **Every scattered value is index-derived** â€” `cos/sin(i Ã— GOLDEN)` + stepped `z`. The golden angle spreads points evenly with no clumps and no `Math.random`.
- **`gsap.set` the cloud BEFORE adding tweens** â€” skipping it leaves frame 0 showing the assembled layout, then a teleport when the first tween starts.
- **`perspective` + `preserve-3d` on stage AND each fragment** â€” missing any one flattens the depth.
- **Resolve flat** â€” settled state is `z: 0`, rotations 0; a still-tilted resolve reads unfinished.
- **Tumble-swap: one shared progress for both glyph sets.**
- **Depth ordering is automatic** inside `preserve-3d` (paint order follows actual Z) â€” no manual z-index, unlike the orbit case's capped band.

## See also

`orbit-3d-entry` (settles into a continuous orbit instead) Â· `hacker-flip-3d` (glyphs decode on arrival) Â· `3d-text-depth-layers` (extrude the locked wordmark) Â· `center-outward-expansion` (flat 2D cousin) Â· `sine-wave-loop` (idle breathe on the resolved layout).
