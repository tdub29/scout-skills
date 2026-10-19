# Knaflic Declutter

## When to Use

Use this skill when an explanatory visual needs a practical cleanup pass before attention and narrative are added.

Trigger when:
- A chart or slide feels busy, exhausting, or harder than necessary.
- Default chart borders, gridlines, legends, markers, trailing zeros, or rotated labels are competing with the data.
- A table or graph makes the audience go back and forth to decode it.
- Visual order, alignment, white space, or contrast is weak.
- The user asks how to reduce cognitive load in a business visual.

Do not use this as a Tufte data-ink-ratio or chartjunk audit; route explicit Tufte questions to `tufte-data-ink-ratio`, `tufte-chartjunk`, or related `tufte-*` skills. Do not use for generic chart picking; use `data-visualization`. Do not use for dashboards; use `build-dashboard` or `kpi-dashboard-design`. Do not use for Bertin retinal variables or encoding theory; use `bertin-*`.

## Framework

Knaflic's decluttering pass reduces extraneous cognitive load: anything that consumes mental effort without increasing understanding should be removed, muted, or redesigned.

1. Identify clutter.
   Clutter is any visual element that takes up space but does not increase understanding enough to justify its presence.

2. Use Gestalt principles.
   Proximity, similarity, enclosure, closure, continuity, and connection help determine which elements are needed and which can be removed.

3. Create visual order.
   Align elements, avoid unnecessary diagonals, preserve margins, and use white space as a pause.

4. Use contrast strategically.
   If many things differ, nothing stands out. Make only the important thing meaningfully different.

5. Remove defaults on purpose.
   Chart borders, heavy gridlines, markers, legends, axis clutter, and redundant formatting are suspect until proven useful.

## How to Apply

1. Name the message the visual should support.
2. Inventory every visible element:
   - border,
   - gridlines,
   - axes and tick marks,
   - labels,
   - legend,
   - data markers,
   - colors,
   - annotations,
   - background,
   - title and supporting text.
3. For each element, ask: does this increase understanding for this audience and message?
4. Remove, lighten, or reposition low-value elements.
5. Prefer direct labeling over legends when it reduces lookup work.
6. Clean numerical labels: remove trailing zeros, preserve meaningful units, percent signs, dollar signs, and commas.
7. Align titles, labels, visuals, and annotations into clean vertical and horizontal lines.
8. Preserve white space and resist adding data just because space exists.

## Output Format

Return:
- **Message:** the point the cleaned visual should support.
- **Clutter inventory:** keep, mute, remove, or redesign for each element.
- **Gestalt fixes:** proximity, similarity, enclosure, closure, continuity, or connection changes.
- **Ordering fixes:** alignment, white space, label orientation, and layout changes.
- **Contrast plan:** what should stand out and what should recede.
- **Rebuild instructions:** concrete edits in order.
- **Residual risks:** information that may need to remain despite looking redundant.

## Common Failure Modes

- Removing labels or units that reduce cognitive load by making numbers self-explanatory.
- Treating all redundant detail as clutter; dollar signs, percent signs, and commas often help.
- Leaving a legend when direct labels would save effort.
- Rotating text or adding diagonals because the default chart did so.
- Filling white space with more data.
- Confusing practical decluttering with Tufte's formal data-ink theory; route formal Tufte work to `tufte-*`.
- Cleaning a chart before knowing the explanatory message.

## References

- Cole Nussbaumer Knaflic, *Storytelling with Data: A Data Visualization Guide for Business Professionals* (Wiley, 2015), Chapter 3, "clutter is your enemy!"
- Sibling skills: `knaflic-explanatory-context`, `knaflic-preattentive-hierarchy`, `knaflic-before-after-critique`.
