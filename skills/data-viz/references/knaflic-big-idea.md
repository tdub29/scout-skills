# Knaflic Big Idea

## When to Use

Use this skill when the user needs the core message of a data story, slide, report, or presentation.

Trigger when:
- The user says the data is interesting but cannot state the point.
- A deck has findings but no recommendation.
- A chart title is descriptive rather than action-oriented.
- A stakeholder asks, "What is the takeaway?"
- A communication needs to survive a shortened meeting or executive skim.

Do not use this to choose chart types; use `data-visualization`. Do not use it to design a monitoring dashboard; use `build-dashboard` or `kpi-dashboard-design`. Do not use it for graphical honesty or data-ink diagnosis; use `tufte-*`. Do not use it for visual variable theory; use `bertin-*`.

## Framework

Knaflic uses two compression tests before content creation:

1. The 3-minute story.
   If you had only three minutes to explain what the audience needs to know, what would you say? This strips away process details and reveals the essential story.

2. The Big Idea.
   The Big Idea compresses the so-what to one complete sentence. Borrowing Nancy Duarte's criteria, it must:
   - Articulate a unique point of view.
   - Convey what is at stake.
   - Be a complete sentence.

3. The action link.
   A Big Idea is not just a summary. It should imply or state what the audience should do next.

## How to Apply

1. Start from context: audience, desired action, data evidence, and communication mechanism.
2. Draft a 3-minute story in plain language:
   - situation,
   - tension or question,
   - key evidence,
   - implication,
   - recommendation or action.
3. Cut the 3-minute story down to a single complete sentence.
4. Test the sentence:
   - Does it have a point of view?
   - Does it make the stakes visible?
   - Would the audience know why this matters?
   - Could it become a slide title, executive summary bullet, or opening statement?
5. Use the Big Idea to decide what belongs in the communication and what should move to an appendix.

## Output Format

Return:
- **3-minute story:** one concise paragraph.
- **Big Idea:** one complete sentence.
- **Stakes:** what changes if the audience acts or does not act.
- **Audience action:** the requested decision or behavior.
- **Keep:** content that supports the Big Idea.
- **Cut or appendix:** content that does not support the Big Idea.
- **Action-title candidates:** 3-5 slide/report titles derived from the Big Idea.

## Common Failure Modes

- Writing a topic label instead of a complete sentence.
- Summarizing the data without a point of view.
- Hiding the recommendation until the audience has already disengaged.
- Including every analytical detail because it took work to produce.
- Confusing the Big Idea with a dashboard KPI; dashboards monitor, while this skill argues a point.
- Using a clever headline that does not tell the audience what to know or do.

## References

- Cole Nussbaumer Knaflic, *Storytelling with Data: A Data Visualization Guide for Business Professionals* (Wiley, 2015), Chapter 1, "The 3-minute story & Big Idea."
- Nancy Duarte, *Resonate* (2010), Big Idea criteria as cited by Knaflic.
- Sibling skills: `knaflic-explanatory-context`, `knaflic-storyboard`, `knaflic-deck-logic`, `knaflic-before-after-critique`.
