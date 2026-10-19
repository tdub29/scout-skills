---
name: duhigg-smarter-faster-better
description: Router hub for Charles Duhigg's *Smarter Faster Better: The Secrets of Productivity in Life and Business* (Random House, 2016), organized as the book's eight productivity concepts â€” one reference each. Triggers: (1) self-motivation, "I can't get started," procrastination, autonomy, internal vs. external locus of control, connecting a chore to a bigger "why" â†’ `duhigg-motivation-locus-of-control`; (2) team effectiveness, "who should be on the team," team norms, Google's Project Aristotle, psychological safety, equal turn-taking, social sensitivity â†’ `duhigg-teams-psychological-safety`; (3) staying focused, cognitive tunneling, reactive thinking, automation complacency, building mental models by narrating what you expect â†’ `duhigg-focus-mental-models`; (4) goal setting, SMART goals, stretch goals, near-term vs. audacious, to-do lists, timidity vs. overwhelm â†’ `duhigg-goals-smart-and-stretch`; (5) managing people, commitment vs. lean/agile cultures, pushing decisions to people closest to the problem, trust and ownership â†’ `duhigg-managing-others-commitment-agile`; (6) making decisions under uncertainty, probabilistic/Bayesian thinking, envisioning multiple contradictory futures and assigning odds, calibration, learning from failures â†’ `duhigg-decision-probabilistic-futures`; (7) innovation, creativity, idea/innovation brokers, combining old ideas in new ways, creative desperation, killing your darlings / not clinging to the first idea â†’ `duhigg-innovation-brokerage`; (8) absorbing data, learning from information, information blindness/overload, disfluency, making data harder by manipulating/writing/testing it â†’ `duhigg-absorbing-data-disfluency`. GUARDRAILS: this is the named *Smarter Faster Better* productivity router (NOT *The Power of Habit*); it covers motivation, teams, focus, goals, management, decisions, innovation, and learning from data. For systematic cognitive/decision biases (anchoring, loss aversion, framing, nudges) use the `behavioral-economics` hub; for designing and analyzing controlled experiments use `kohavi-controlled-experiments` or `ab-testing` â€” do not duplicate those here. Load the matching references/<name>.md file when a specific concept is needed.
---

# duhigg-smarter-faster-better

This hub collapses Duhigg's eight productivity concepts into one router plus references. Route by user cue, read the referenced file in full, and apply that concept's framework â€” including its how-to-apply steps and failure modes.

Book provenance: **Charles Duhigg, *Smarter Faster Better: The Secrets of Productivity in Life and Business* (Random House, 2016)**. Load the matching `references/*.md` file when a specific concept is needed.

## When to use

Use this hub when the user wants to be **more productive** in the sense Duhigg means it â€” getting started and staying motivated, building teams that actually perform, holding focus in automated or noisy environments, setting goals that are both concrete and ambitious, managing people so the right decisions get made fast, deciding well under uncertainty, generating genuinely new ideas, or actually learning from the data in front of them. Match the request to **one** concept, read that reference fully, then execute its process and output.

Do not improvise a hybrid of multiple concepts unless the user explicitly asks for a combined pass (e.g., goals + focus for a planning ritual).

## Guardrails

- **This is *Smarter Faster Better*, not *The Power of Habit*.** Duhigg's earlier book covers cue-routine-reward habit loops and keystone habits; this hub does not. If the user wants habit-formation mechanics specifically, say so rather than forcing it through one of these eight concepts.
- **Sibling hubs (not part of this book; do not modify or duplicate):** for cognitive and decision biases â€” anchoring, loss aversion, framing, nudges, choice architecture as a manipulation taxonomy â€” use `behavioral-economics`. For designing, running, and reading controlled experiments and A/B tests use `kohavi-controlled-experiments` or `ab-testing`. Duhigg's decision chapter teaches *probabilistic forecasting and calibration*, which complements but does not replace those. Where a user's question is really about debiasing decisions in a group, `noise-decision-hygiene` is a useful cross-reference; cross-reference it, don't copy it.
- **Do not answer from router memory alone.** Load the selected reference file first and follow its process and failure modes.

## Quick routing table

| User cue (examples) | Route to reference |
|---|---|
| can't get going, procrastinating, low drive, want autonomy, blaming luck vs. effort, "why should I even do this," connecting a task to a larger purpose | `references/duhigg-motivation-locus-of-control.md` |
| building or fixing a team, "who's on the team vs. how they work," meeting dynamics, Project Aristotle, psychological safety, equal airtime, reading the room | `references/duhigg-teams-psychological-safety.md` |
| losing focus, tunnel vision in a crisis, over-trusting automation, missing the signal in the noise, narrating/forecasting what you expect to see | `references/duhigg-focus-mental-models.md` |
| setting goals, SMART vs. stretch, to-do lists that become busywork, goals too timid or too overwhelming, pairing ambition with a concrete first step | `references/duhigg-goals-smart-and-stretch.md` |
| managing or leading people, command-and-control vs. agile, pushing decisions down to the front line, building trust and ownership, stand-ups | `references/duhigg-managing-others-commitment-agile.md` |
| deciding under uncertainty, forecasting, "what are the odds," holding multiple contradictory futures, Bayesian updating, calibrating from wins and losses | `references/duhigg-decision-probabilistic-futures.md` |
| need a new idea, feeling stuck/derivative, combining ideas across domains, creative brokers, deadline pressure as fuel, clinging to the first solution | `references/duhigg-innovation-brokerage.md` |
| drowning in dashboards/reports, data isn't changing behavior, information overload, making data stick by writing/manipulating/testing it | `references/duhigg-absorbing-data-disfluency.md` |

## Workflow

1. Identify which of the eight concepts the user's situation maps to.
2. Run the guardrail check: is this actually a *Smarter Faster Better* concept, or is it habits (*The Power of Habit*), a cognitive bias (`behavioral-economics`), or an experiment-design question (`kohavi-controlled-experiments` / `ab-testing`)? Route out if so.
3. Pick the closest row in the routing table.
4. Read that `references/*.md` file completely.
5. Apply the concept's framework, how-to-apply steps, and failure modes, grounded in the book's evidence (cite the chapter).
6. Combine concepts only when the user explicitly asks for a multi-lens pass.

## Common failure modes (hub-level)

- **Wrong book** â€” answering with habit-loop mechanics from *The Power of Habit* instead of one of these eight productivity concepts.
- **Wrong sibling hub** â€” handling a pure cognitive bias or an A/B-test design question here instead of routing to `behavioral-economics` / `kohavi-controlled-experiments` / `ab-testing`.
- **Router-only answer** â€” summarizing the concept without loading the reference's full framework.
- **Concept blur** â€” collapsing all eight into "just try harder"; each concept has a specific, distinct mechanism and the value is in keeping them separate.

## References

- [references/duhigg-motivation-locus-of-control.md](references/duhigg-motivation-locus-of-control.md)
- [references/duhigg-teams-psychological-safety.md](references/duhigg-teams-psychological-safety.md)
- [references/duhigg-focus-mental-models.md](references/duhigg-focus-mental-models.md)
- [references/duhigg-goals-smart-and-stretch.md](references/duhigg-goals-smart-and-stretch.md)
- [references/duhigg-managing-others-commitment-agile.md](references/duhigg-managing-others-commitment-agile.md)
- [references/duhigg-decision-probabilistic-futures.md](references/duhigg-decision-probabilistic-futures.md)
- [references/duhigg-innovation-brokerage.md](references/duhigg-innovation-brokerage.md)
- [references/duhigg-absorbing-data-disfluency.md](references/duhigg-absorbing-data-disfluency.md)

- **Book:** Charles Duhigg, *Smarter Faster Better: The Secrets of Productivity in Life and Business* (Random House, 2016)
