---
name: nudge-curve
description: Slow-fast-slow three-phase group slide â€” reposition a composed group (word rows, card stacks, lists) to reveal content or make room. No single built-in ease produces it; chain power3.in ramp â†’ linear burst â†’ power4.out tail (10/65/25 distance, tail â‰¥3Ã— ramp-in in time).
metadata:
  tags: slide, reposition, group-motion, easing, nudge, slow-fast-slow, reveal, layout
---

# Nudge Curve

Slow-fast-slow repositioning of a composed group (word rows, card stacks, lists) to
reveal content or make room. **In-scene group slide â€” not a seam.** No single built-in
ease produces it â€” `power4.inOut` smacks to a stop. Chain three tweens on one property:

| Phase     | Ease            | Distance | Time | Feel                                     |
| --------- | --------------- | -------- | ---- | ---------------------------------------- |
| 1 ramp-in | `power3.in`     | ~10%     | ~20% | barely moves â€” motion registers, no jolt |
| 2 burst   | `none` (linear) | ~65%     | ~18% | ~2Ã— average px/frame â€” purposeful        |
| 3 tail    | `power4.out`    | ~25%     | ~62% | decaying creep to rest â€” kills the smack |

## Rules

- The tail is â‰¥3Ã— the ramp-in in TIME. If it still smacks: extend the tail's time (not
  distance) or use `power5.out`.
- Phase 2 stays linear â€” easing it loses the burst contrast.
- Reveal new content DURING phase 2 â€” the burst masks its appearance.
- Same ratios vertical; scale distances proportionally, keep the time ratios.
- A cascade arrival usually precedes this slide â€” see [waterfall-entry.md](waterfall-entry.md).

## JS

Reference values for a 270px leftward slide (0.57s total). Scale distances
proportionally for other travels; preserve the TIME ratios; tail â‰¥3Ã— ramp-in.

```js
var t = /* start after content settles */;
tl.to(".text-row", { x: -30,  duration: 0.12, ease: "power3.in"  }, t);          // ramp-in: 11% dist / 21% time
tl.to(".text-row", { x: -210, duration: 0.10, ease: "none"       }, t + 0.12);   // burst:   67% dist / 18% time
tl.to(".text-row", { x: -270, duration: 0.35, ease: "power4.out" }, t + 0.22);   // tail:    22% dist / 61% time
// vertical: same ratios on y. 150px variant: -15 / -115 / -150 at the same times.
```

## Anti-patterns

| Don't                                                    | Instead                                  |
| -------------------------------------------------------- | ---------------------------------------- |
| Single ease for a group slide (`power4.inOut`, `slow()`) | The three-phase chain above              |
| Nudge tail shorter than 3Ã— the ramp-in                   | Extend the tail's TIME, not its distance |
