# Knaflic Deck Logic

## When to Use

Use this skill when a deck, report, or analytical presentation needs story structure and slide-to-slide logic.

Trigger when:
- Slide titles do not tell a story when read in order.
- A deck has facts and charts but no narrative path.
- An executive summary needs to map to the body.
- A slide has content that does not reinforce its title.
- The user wants to reverse-storyboard an existing deck.
- A live presentation and leave-behind need different narrative handling.

Do not use this for chart-type selection; use `data-visualization`. Do not use for dashboards; use `build-dashboard` or `kpi-dashboard-design`. Do not use for Tufte integrity, data-ink, chartjunk, or lie-factor checks; use `tufte-*`. Do not use for Bertin encoding theory; use `bertin-*`.

## Framework

Knaflic's deck logic is a set of narrative checks:

1. Story has beginning, middle, and end.
   Beginning sets context and tension. Middle develops evidence and options. End gives a clear call to action.

2. Choose narrative order deliberately.
   Use chronological order when the audience needs process or credibility. Lead with the ending when trust exists and the audience wants the so-what first.

3. Bing, Bang, Bongo.
   Tell the audience what you will tell them, tell them, then summarize what you told them. Use repetition to make the message stick.

4. Horizontal logic.
   Read only the slide titles. Together, they should tell the overarching story in order. Titles should be action titles, not topic labels.

5. Vertical logic.
   On each slide, every element should reinforce the title and the title should explain the visual or evidence.

6. Reverse storyboarding.
   For an existing deck, write down the main point of each slide. The resulting list should match the intended story outline.

## How to Apply

1. Capture the Big Idea and audience action.
2. Decide the narrative flow: chronological, lead-with-ending, problem-solution, or executive-summary-first.
3. Draft an executive summary whose bullets map one-to-one to the body sections or slide titles.
4. Check horizontal logic:
   - Extract all slide titles.
   - Read them without the slides.
   - Rewrite topic labels as action titles.
5. Check vertical logic:
   - For each slide, ask whether the visual, annotations, text, and title reinforce one point.
   - Remove or appendix content that does not support the title.
6. Reverse-storyboard the deck and compare the extracted story to the intended story.
7. Identify where spoken narrative is required for live delivery and where written narrative is required for a leave-behind.

## Output Format

Return:
- **Narrative choice:** chronological, lead-with-ending, or other, with rationale.
- **Bing:** executive summary or opening setup.
- **Bang:** body sequence with action titles.
- **Bongo:** closing summary and call to action.
- **Horizontal logic audit:** title-by-title story check.
- **Vertical logic audit:** slide-level keep/cut/fix list.
- **Reverse storyboard:** extracted current story and revised story.
- **Presentation vs leave-behind notes:** what must be spoken versus written.

## Common Failure Modes

- Using descriptive titles like "Revenue by Region" instead of action titles.
- Letting the analytical process dictate order when the audience needs the answer first.
- Making the audience infer the call to action.
- Putting unrelated evidence on a slide because it is interesting.
- Creating a slideument without deciding what is spoken and what must stand alone.
- Rearranging charts for novelty instead of preserving audience comprehension.
- Treating a dashboard as a deck; dashboards are monitoring systems, not linear stories.

## References

- Cole Nussbaumer Knaflic, *Storytelling with Data: A Data Visualization Guide for Business Professionals* (Wiley, 2015), Chapter 7, "lessons in storytelling."
- Sibling skills: `knaflic-big-idea`, `knaflic-storyboard`, `knaflic-before-after-critique`, `knaflic-preattentive-hierarchy`.
