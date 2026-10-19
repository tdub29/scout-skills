# Knaflic Preattentive Hierarchy

## When to Use

Use this skill when an explanatory visual needs attention control.

Trigger when:
- The viewer's eye is drawn to the wrong part of a chart or slide.
- Too many colors, marks, labels, or sizes compete.
- A chart needs a clear "look here" signal.
- A slide needs a first-read, second-read, and background layer.
- The user wants to highlight a specific point in a graph or table.

Do not use this for Bertin's formal retinal-variable theory; use `bertin-retinal-variables` or related `bertin-*` skills. Do not use for generic chart choice; use `data-visualization`. Do not use for dashboards; use `build-dashboard` or `kpi-dashboard-design`. Do not use for Tufte data-ink, chartjunk, lie-factor, or integrity issues; use `tufte-*`.

## Framework

Knaflic's attention framework uses preattentive attributes strategically and sparingly.

1. Iconic memory spots differences before conscious processing.
   Size, color, intensity, position, orientation, added marks, and similar attributes can make something pop.

2. Preattentive attributes do two jobs.
   They draw attention quickly and create visual hierarchy.

3. Highlighting one thing makes other things harder to see.
   This is useful in explanatory communication but risky in exploratory analysis.

4. Push everything back before bringing anything forward.
   Muting all elements forces an explicit decision about what deserves emphasis.

5. Test the hierarchy.
   Close your eyes, look back, and notice where your eye lands first. Better: ask someone else to narrate their eye path.

## How to Apply

1. Identify the exact point the audience should see first.
2. Push non-message elements to the background with grey, lighter weight, smaller size, or less saturation.
3. Choose one or two preattentive cues for the primary message:
   - color,
   - size,
   - boldness,
   - position,
   - marks,
   - enclosure,
   - line weight.
4. Use consistent color semantics across the communication.
5. Avoid rainbow palettes unless category differentiation is truly the primary job.
6. Design for colorblindness: avoid red/green dependence and add non-color cues.
7. Place important words or visuals where the audience naturally starts, often the upper left in left-to-right reading contexts.
8. Run the "where are your eyes drawn?" test and adjust.

## Output Format

Return:
- **Intended first read:** where the audience should look first.
- **Intended sequence:** first, second, third, and background layers.
- **Current eye path:** what likely attracts attention now.
- **Hierarchy edits:** mute, emphasize, reposition, relabel, or remove.
- **Color plan:** sparing, consistent, accessible use of color.
- **Test plan:** how to validate the eye path with a viewer.
- **Caveats:** what becomes less visible because of the highlight.

## Common Failure Modes

- Using color for decoration instead of meaning.
- Making everything different, so nothing stands out.
- Encoding quantitative order with arbitrary categorical colors.
- Highlighting in exploratory analysis before knowing the story.
- Changing color meanings across slides for novelty.
- Depending only on red/green contrast.
- Letting brand colors override sufficient contrast.
- Treating this as Bertin theory; this skill is Knaflic's business-communication attention pass.

## References

- Cole Nussbaumer Knaflic, *Storytelling with Data: A Data Visualization Guide for Business Professionals* (Wiley, 2015), Chapter 4, "focus your audience's attention."
- Stephen Few, *Show Me the Numbers* (2004), preattentive attributes as cited by Knaflic.
- Sibling skills: `knaflic-declutter`, `knaflic-deck-logic`, `knaflic-before-after-critique`.
