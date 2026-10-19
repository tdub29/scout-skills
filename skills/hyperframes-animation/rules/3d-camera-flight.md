---
name: 3d-camera-flight
description: Perspective camera FLIGHT through a 3D-laid-out world â€” one static perspective stage + preserve-3d world whose pose (translate3d + rotateX/rotateY) is tweened leg-by-leg from a single camera state object. Dive into an angled grid, tilt-to-flatten pull-back, continuous flight past standing cards, decelerate-into-focus. Hard power4.out landings, power2.inOut repositioning; DoF via depth-of-field-blur on non-focal planes.
metadata:
  tags: camera, 3d, flight, perspective, preserve-3d, rotateX, rotateY, translateZ, dive, tilt, world, cinematic
---

# 3D Camera Flight

Every other camera rule here is a **2D camera**: [viewport-change.md](viewport-change.md), [multi-phase-camera.md](multi-phase-camera.md), and [coordinate-target-zoom.md](coordinate-target-zoom.md) simulate the camera with `scale` + `translate` on a flat wrapper â€” the lens never tilts, and there is no depth axis to travel along. [3d-page-scroll.md](3d-page-scroll.md) is a **static tilt**: one angle held all scene while content scrolls inside. This rule is the missing camera that _flies_ â€” dives into an angled grid, pulls back while the world rotates flat, streaks past standing cards, decelerates out of a blur into focus: a **perspective camera traveling with `rotateX` / `rotateY` / `translateZ` through a 3D-laid-out world**, under the same single-camera discipline as `viewport-change`: **one perspective wrapper, one camera state object, one transform writer**, every leg a sequenced tween on that state.

## How It Works

Five layers, strictly separated:

1. **The lens** â€” `perspective: PERSPECTIVE_PX` on a static `.stage` wrapper. Set once, never tweened, never moved. Changing perspective mid-shot reads as the lens itself warping, not the camera moving.
2. **The world** â€” a `.world` div with `transform-style: preserve-3d`, laid out at final 1Ã— size: the ground surface (grid, form card, canvas) as flat DOM, optional **props** (a giant date number, a floating label) at static `translateZ(PROP_Z)` offsets so travel produces parallax, and **standing cards** counter-tilted to face the camera at their landing pose.
3. **The camera state** â€” a single object `cam = { x, y, z, rx, ry }` (the world's pose), written to `world.style.transform` by ONE function, `applyCamera()`, in a **fixed order**: `translate3d(x, y, z) rotateX(rx) rotateY(ry)`. With translate composed _outside_ the rotations, `x`/`y`/`z` always move the world along **screen axes** no matter how it is currently tilted â€” pan is always sideways, `z` is always toward/away from the lens. Put the rotations first and every leg's numbers change meaning as the tilt changes.
4. **The legs** â€” sequential tweens on `cam`, each one camera move: dive in (`power4.out` â€” violent arrival, sharp settle), tilt-to-flatten pull-back (`power2.inOut` â€” a repositioning, no slam), lateral flight, final dive. Camera intent inverts onto the world pose exactly as in `viewport-change`: camera flies **in** â†’ world `z` **increases** (comes toward the lens); camera pans **right** â†’ world `x` **negative**; camera tilts **down** over the surface â†’ world `rx` **positive** (far edge tips away).
5. **Depth cues** â€” DoF via [depth-of-field-blur.md](depth-of-field-blur.md) `--dof` tweens on the **non-focal planes** (cards, props â€” leaf elements, never the world itself), and velocity blur on travel legs via [motion-blur-streak.md](motion-blur-streak.md)'s Camera-Travel Carve-Out â€” applied to the **stage**, never the world (a `filter` on a `preserve-3d` element flattens it).

Landing poses are **authored, not derived**: set `cam` to candidate values at design time, call `applyCamera()`, screenshot, adjust, bake the numbers as constants. There is no counter-translate formula to get wrong in 3D â€” the pose IS the design decision. Never measure per-frame (`getBoundingClientRect` in `onUpdate` desyncs under parallel frame sampling), and don't hand-derive 3D projections â€” your eye at design time beats the math.

## Recipe

```html
<!-- The lens: static perspective, nothing else. -->
<div class="stage">
  <!-- The world: preserve-3d, laid out at final 1Ã— size; the camera flies by
       tweening THIS element's pose. Travel legs push content past the frame
       edges by design â€” hence data-layout-allow-overflow. -->
  <div class="world" id="world" data-layout-allow-overflow>
    <div class="surface">
      <div class="grid">{gridCells}</div>
      <div class="card layer" id="card-a" data-depth="0">{cardA}</div>
      <div class="card layer" id="card-b" data-depth="0">{cardB}</div>
    </div>
    <!-- Foreground props float at PROP_Z for parallax; they blur and fly past,
         never carry a read. -->
    <div class="prop layer" data-depth="2" style="--px: PROP_X; --py: PROP_Y">{propGlyph}</div>
  </div>
</div>
```

```css
.scene {
  overflow: hidden; /* travel legs push world content past the frame on purpose */
  background: {sceneBg}; /* the void the flight exposes at frame edges â€” must be a
     designed surface (deep brand color / soft gradient), never default white */
}
.stage {
  position: absolute;
  inset: 0;
  perspective: PERSPECTIVE_PX; /* THE LENS â€” static, never tweened */
  /* travel blur (motion-blur-streak carve-out) attaches HERE, never on .world */
}
.world {
  position: absolute;
  inset: 0;
  transform-style: preserve-3d;
  transform-origin: 50% 50%;
  will-change: transform;
  /* keep CLEAN: no filter, opacity < 1, overflow, clip-path, or mask â€” each
     flattens preserve-3d. Background on .scene, blur on .stage or leaf cards. */
}
.surface {
  position: absolute;
  inset: WORLD_INSET; /* world runs larger than the frame so travel has runway */
  transform-style: preserve-3d;
}
.prop {
  position: absolute;
  left: var(--px);
  top: var(--py);
  /* static world-space pose; counter-tilt faces the camera at the dive pose */
  transform: translateZ(PROP_Z) rotateX(PROP_COUNTER_TILT);
}
.layer {
  --dof: 0px; /* DoF channel per depth-of-field-blur â€” leaf elements only */
  filter: blur(var(--dof));
  will-change: filter;
}
```

```js
const world = document.getElementById("world");

// Camera state â€” the ONLY source of truth for the world's pose. Every leg
// tweens this object; nothing else touches world.style.transform.
const cam = { x: 0, y: 0, z: WIDE_Z, rx: 0, ry: 0 };

function applyCamera() {
  // Fixed order: translate OUTSIDE the rotations â†’ x/y/z stay screen-aligned
  // at any tilt. Changing this order changes what every baked pose means.
  world.style.transform = `translate3d(${cam.x}px, ${cam.y}px, ${cam.z}px) rotateX(${cam.rx}deg) rotateY(${cam.ry}deg)`;
}
applyCamera(); // seed frame 0 so a seek to t=0 renders the opening pose

// â”€â”€ LEG 1 â€” DIVE IN: wide establishing pose â†’ angled close-up on card A.
// fromTo states the opening pose explicitly; power4.out = violent arrival,
// razor-sharp settle. Travel blur: motion-blur-streak carve-out on .stage.
const DIVE_POSE = { x: DIVE_X, y: DIVE_Y, z: DIVE_Z, rx: DIVE_RX, ry: DIVE_RY };
tl.fromTo(
  cam,
  { x: 0, y: 0, z: WIDE_Z, rx: 0, ry: 0 },
  { ...DIVE_POSE, duration: DIVE_DUR, ease: "power4.out", onUpdate: applyCamera },
  DIVE_AT,
);
// Decelerate-INTO-FOCUS: non-focal planes' --dof ramps to BLUR_PER_DEPTH Ã— data-depth
// on the SAME window/ease (depth-of-field-blur focal pull); card A stays at --dof: 0.

// â”€â”€ LEG 2 â€” TILT-TO-FLATTEN PULL-BACK: every channel returns to neutral on ONE
// power2.inOut tween â€” a reposition, not a slam. DoF releases on the same window
// so the flat overview arrives fully crisp.
const FLAT_POSE = { x: 0, y: 0, z: 0, rx: 0, ry: 0 };
tl.to(
  cam,
  { ...FLAT_POSE, duration: FLATTEN_DUR, ease: "power2.inOut", onUpdate: applyCamera },
  FLATTEN_AT,
);
tl.to(".layer", { "--dof": "0px", duration: FLATTEN_DUR, ease: "power2.inOut" }, FLATTEN_AT);

// â”€â”€ LEG 3 â€” LATERAL FLIGHT: screen-aligned pan (translate is outside the
// rotations, so x is a pure sideways move even mid-tilt).
tl.to(cam, { x: PAN_X, duration: PAN_DUR, ease: "power2.inOut", onUpdate: applyCamera }, PAN_AT);

// â”€â”€ LEG 4 â€” FINAL DIVE onto card B: same grammar as leg 1; card A racks OUT of
// focus as card B racks in (depth-of-field-blur rack, shared window).
const LAND_POSE = { x: LAND_X, y: LAND_Y, z: LAND_Z, rx: LAND_RX, ry: LAND_RY };
tl.to(
  cam,
  { ...LAND_POSE, duration: LAND_DUR, ease: "power4.out", onUpdate: applyCamera },
  LAND_AT,
);
tl.to("#card-a", { "--dof": `${MAX_BLUR}px`, duration: LAND_DUR, ease: "power4.out" }, LAND_AT);
tl.to("#card-b", { "--dof": "0px", duration: LAND_DUR, ease: "power4.out" }, LAND_AT);
// Landing dwell: â‰¥1 s of stillness on card B â€” unless ending held mid-dive.
```

## Variations

- **Continuous flight past standing cards** â€” one long leg instead of dive-land-dive: sustained `z` + `x` travel (2â€“4 s, `power2.inOut` / `power1.inOut` near-constant cruise) through a corridor of cards and props at staggered `PROP_Z`. Parallax does the work â€” near props streak past while far ones crawl. Keep ONE plane sharp at a time via staggered `--dof` tweens. Props crossing the camera plane (`cam.z + PROP_Z` approaching `PERSPECTIVE_PX`) blow up to fill the frame and vanish â€” that IS the fly-past; never let a focal card cross it.
- **End held mid-dive** â€” give the final leg a window that overruns the composition (`LAND_AT + LAND_DUR > data-duration`); the last frame holds mid-tween â€” still traveling, blur not fully resolved. Seek-safe by construction (a seek to the last frame lands at a deterministic pose); don't fake it with a shorter leg plus a manual offset. Use when the brief wants momentum at the cut, not rest.
- **Whip sweep** â€” the heavily motion-blurred lateral whip that resolves into the next region: leg 3 driven by [nudge-curve.md](nudge-curve.md)'s three-phase chain (burst-dominant) on `cam.x`, with [motion-blur-streak.md](motion-blur-streak.md)'s Camera-Travel Carve-Out on the same window â€” blur ramps through the ramp-in, rides the burst at peak, resolves to 0 through the `power4.out` tail. Full recipe in that carve-out.
- **Hold drift (the hold never dies)** â€” between legs, fold `multi-phase-camera`-style micro-drift **through the same writer**: a driver tween writes tiny `dx`/`dy`/`drx` into a `drift` object and `applyCamera()` composes `cam.x + drift.dx`, `cam.rx + drift.drx`, etc. Never let drift write `world.style.transform` itself â€” two writers on one transform is the classic camera bug. Amplitudes per `multi-phase-camera` (2â€“8 px), rotation drift â‰¤ 0.5Â°.

## Values

| token                     | range                                                            | notes                                                                                                                                                                                     |
| ------------------------- | ---------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PERSPECTIVE_PX            | 700â€“1400 px (moving cam best 800â€“1200)                           | smaller = wilder foreshortening, more violent dives; larger = near-orthographic, the flight flattens                                                                                      |
| WORLD_INSET               | âˆ’50% to âˆ’150% per side                                           | world 2â€“4Ã— the frame so lateral legs have runway                                                                                                                                          |
| PROP_Z                    | 80â€“300 px                                                        | higher = stronger parallax, earlier fly-past                                                                                                                                              |
| PROP_COUNTER_TILT         | â‰ˆ `-LAND_RX` of the leg that reads it                            | author by eye and bake                                                                                                                                                                    |
| DIVE_RX / LAND_RX         | 30â€“55Â°                                                           | "angled grid" starts ~30Â°; \|rx\| â‰¤ ~65Â°, \|ry\| â‰¤ ~30Â° â€” beyond that flat planes go edge-on, text unreadable                                                                             |
| DIVE_Z / LAND_Z           | 300â€“700 px at PERSPECTIVE_PX â‰ˆ 1000                              | **Z budget**: `cam.z + PROP_Z â‰¤ ~0.6 Ã— PERSPECTIVE_PX` for readable content â€” near the perspective distance, scale blows toward infinity and elements invert/vanish past the camera plane |
| WIDE_Z                    | âˆ’100 to âˆ’400 px                                                  | negative z = world pushed away = camera wide                                                                                                                                              |
| DIVE_X/Y, LAND_X/Y        | read off a screenshot at the baked tilt                          | screen-aligned (translate outside rotations)                                                                                                                                              |
| DIVE_DUR / LAND_DUR       | 0.6â€“1.0 s                                                        | commitment, not a polite zoom; under 0.5 s reads as a cut                                                                                                                                 |
| FLATTEN_DUR               | 1.2â€“2.0 s                                                        | the repositioning is the breath between dives                                                                                                                                             |
| PAN_DUR                   | 0.8â€“1.5 s plain; 0.5â€“0.8 s whip                                  |                                                                                                                                                                                           |
| Ease law                  | `power4.out` dives/landings; `power2.inOut` repositioning/cruise | spring/back on a camera reads as the world wobbling on a string; four identical pushes read as a slideshow â€” vary the leg verbs                                                           |
| Holds                     | â‰¥ 0.8 s between legs; final dwell â‰¥ 1 s                          | unless ending held mid-dive                                                                                                                                                               |
| BLUR_PER_DEPTH / MAX_BLUR | per [depth-of-field-blur.md](depth-of-field-blur.md)             | 3â€“6 px per step, terminal 8â€“24 px, leaf elements only; travel-blur peak per [motion-blur-streak.md](motion-blur-streak.md) (~18â€“20 px full-frame, on `.stage`)                            |

## Critical Constraints

- **One lens, one state, one writer** â€” `perspective` on the static `.stage` only (never on `.world`, never tweened, never a second perspective wrapper inside); every leg tweens the single `cam` object; only `applyCamera()` writes the transform â€” drift folds into the same writer via additive state. Two writers (or a second transform sneaking in via CSS) is the classic broken-camera bug, five channels of it here.
- **Fixed transform order: translate outside the rotations** â€” `translate3d(x,y,z) rotateX() rotateY()`. Reorder it and every pose you authored silently means something else.
- **Keep the world CLEAN** â€” `filter`, `opacity < 1`, `overflow` other than `visible`, `clip-path`, or `mask` on `.world` (or any intermediate wrapper) forces used `transform-style: flat` and collapses every `translateZ` in the scene. Travel blur goes on `.stage`; DoF on leaf cards; fades on children; background on `.scene`. `transform-style: preserve-3d` on `.world` and every intermediate wrapper between it and 3D-positioned children.
- **Camera intent inverts onto the world** â€” fly in = world z up, pan right = world x negative, tilt down = world rx positive. Same sign law as `viewport-change`, two more axes to get right.
- **Poses authored and baked** â€” never measured per-frame, never hand-derived projections.
- **First leg is a `fromTo`** AND `applyCamera()` runs once at setup â€” a seek to t=0 must render the exact establishing pose.
- **Z budget** â€” only sacrificial props may cross the camera plane.
- **Reads happen at landings** â€” angled, blurred, flying text is texture; anything the viewer must read gets a near-flat pose or a sharp held close-up â‰¥ 1 s (the tilt-to-flatten leg exists to hand the surface over for reading).
- **`overflow: hidden` on `.scene` + `data-layout-allow-overflow` on `.world`** â€” travel legs deliberately push panels past the frame; without the pairing, `check` reports `container_overflow` for every region the flight leaves behind.

## See also

[viewport-change.md](viewport-change.md) (2D counterpart, same single-writer law â€” right when the shot never tilts) Â· [multi-phase-camera.md](multi-phase-camera.md) (leg-sequencing grammar + hold micro-drift) Â· [coordinate-target-zoom.md](coordinate-target-zoom.md) (aim math for a flat-hold zoom while `rx`/`ry` are 0) Â· [depth-of-field-blur.md](depth-of-field-blur.md) (non-focal defocus / racks) Â· [motion-blur-streak.md](motion-blur-streak.md) (travel blur on the stage) Â· [nudge-curve.md](nudge-curve.md) (whip-sweep burst tuning) Â· [3d-page-scroll.md](3d-page-scroll.md) (static-tilt cousin â€” camera should NOT travel) Â· [orbit-3d-entry.md](orbit-3d-entry.md) / [depth-scatter-assemble.md](depth-scatter-assemble.md) (elements moving under a still camera â€” the inverse; don't run both on one beat). Capability background: `../techniques.md` Â§ CSS 3D Transforms.
