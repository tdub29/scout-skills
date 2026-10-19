# Minto â€” Problem Definition and Structuring the Analysis

## The framework

> "The secret to writing consulting reports efficiently is to make sure you (a) define the problem and (b) structure the gathering and analysis of your data so as to facilitate their translation into pyramid form." (Intro to Part Three)

For longer, problem-oriented documents (reports, proposals, recommendation decks), the pyramid is *pre-built* by the problem-solving itself. The ideal is a sequential pipeline:

> Define the problem â†’ Structure the analysis â†’ Conduct analysis / find the solution â†’ Form the pyramid to communicate

Done well, the first two stages "pre-structure your pyramid" â€” the problem definition becomes the introduction, and the analysis structure becomes the body.

### Defining the problem: the R1 â†’ R2 gap

A problem is "a gap between the results you get now and the results you would rather have had" (Ch 8). Lay out four elements (Ch 8, Lay Out the Problem):

- **Starting Point / Opening Scene** â€” the existing structure or process, sketched simply (imagine the curtain rising on a stage; or "tell a friend the story" â€” what must they *see* to understand it?). Assume the general knowledge of a *Fortune*/*Business Week* reader.
- **Disturbing Event** â€” what happened (or could/will happen) to threaten the stable Opening Scene. Three kinds: **external** (new competitor, new technology, policy shift), **internal** (added a process, new system, new market), **recently recognized** (lagging performance, sub-par results, research hinting at a shift). If you can't pin one down, skip it and go straight to R1.
- **R1 (Undesired Result)** â€” the problem the reader is trying to solve (the typical trigger for a consulting engagement). State briefly.
- **R2 (Desired Result)** â€” what he wants instead, stated "as specifically and quantifiably as you can" in end-product terms ("Reduce time to market by 1/3"; "Have sufficient capacity to cope with projected demand"), so you can tell when you've achieved it and choose between candidate solutions. If you can't state R2 yet, that becomes the first analysis step.

### Sequential analysis

Defining the gap begins **Sequential Analysis** â€” five questions in order (Ch 8, citing B. Robert Holland):

1. Is there / is there likely to be a problem (or opportunity)?
2. Where does it lie?
3. Why does it exist?
4. What could we do about it?
5. What should we do about it?

Questions 1â€“2 **define the problem** (â†’ the introduction); question 3 **finds the causes** (â†’ diagnostic frameworks); questions 4â€“5 **find the solution** (â†’ logic trees, â†’ the pyramid's points).

### Converting the problem definition into the introduction

> "Once you are ready to put the solution in writing, you can easily convert the problem definition to an introduction. You simply read from left to right and down, with the last thing known by the reader always serving as the Complication." (Ch 8, Converting to an Introduction)

So Situation = Opening Scene (+ Disturbing Event); the last-known element becomes the Complication; the gap raises the Question. The reader sits in one of **seven situations** depending on how far they've progressed toward a solution (Ch 8, Exhibit 34) â€” e.g., don't know how to get R1â†’R2 (Q: *What should we do?*); have a suggested solution (Q: *Is it the right one?* / *How do we implement?*); tried a solution that failed (Q: *What should we do?*); have several alternatives (Q: *Which is best?*); know R1 but not R2 (Q: *What should our objectives be?*); know R2, unsure if at R1 (benchmarking â€” Q: *Do we have a problem?*). Each maps cleanly onto an S-C-Q introduction (see `minto-scqa-introduction.md`).

### Structuring the analysis â€” don't start with the data

The old habit of gathering all available data first wastes effort â€” "a major consulting firm once estimated that fully 60% of its fact-finding and analysis effort was wasted" (Ch 9, Starting with the Data). Better is to **structure the analysis before gathering**, replicating the scientific method: generate hypotheses about *why the problem exists*, then gather data to prove each right or wrong. The hypotheses come from "looking critically at the structure of the area within which the problem occurred" â€” the Opening Scene â€” using a **diagnostic framework**.

### Diagnostic frameworks (find the causes â€” question 3)

A diagnostic framework helps you "visualize what's going on in the area within which the problem occurred," revealing where to look (Ch 9, Devising Diagnostic Frameworks). Built with the same three analytical activities as any structure (`minto-mece-grouping.md`): **divide** (show physical/industry structure), **trace cause and effect** (financial structure, task structure, activity structure â€” the headache that's physical-or-mental, then external-or-internal), or **classify** (group likely culprits; the choice/bifurcation tree). The output is always a set of **yes/no questions** â€” the "crucial experiments" that "unambiguously identify or exclude the contributing causes" and tell you in advance when research is done. (This is why diagnostic frameworks are *not* decision trees or PERT diagrams, which reveal the need for action rather than generate questions.)

### Logic trees (find/validate solutions â€” questions 4â€“5)

Where diagnostic frameworks model *what exists* (steps 2â€“3), **logic trees** "spell out logically possible actions that could be taken to solve a problem" (Ch 9, Developing Logic Trees), broken down MECE (the cigarette-cost tree: reduce cost-per-hour vs. hours-per-million, each split further). You then estimate the benefit and risk of each branch to arrive at the recommended set. Logic trees also **reveal flaws in grouped ideas** after writing â€” mapping a list of "key issues" onto the tree exposes which items don't belong (the energy-cost list where issues 7, 8, 9 "simply don't relate to the subject").

### Issues are yes/no questions, not topics

> "Strictly speaking, an issue is a question so phrased as to demand a yes-or-no answer." (Ch 9, Performing an Issue Analysis)

"How should we reorganize?" is not an issue; "Should we reorganize functionally?" is. Use **"concerns"** for the topics that worry the client, and reserve **"issues"** for genuine yes/no questions. Minto's strong view: there is almost never a need for an "Issues" section â€” "the issues, if any, will always derive from the analytical process to be used to solve the problem. So the issues, the process, and the end products of the study all turn out to be the same thing."

### The structure mirrors the problem-solving, then the document mirrors the structure

Because the introduction comes from the problem definition and the body's points come from the diagnostic/logic-tree analysis, the finished pyramid *is* the visible shape of the problem-solving. The real-life warehouse example runs the whole pipeline: problem definition (3 centers, can serve 438 not 490, growth + 198 new stores â†’ run out of capacity) â†’ alternatives â†’ introduction (S-C-Q, situation #5 "which alternative?") â†’ pyramid ("Add capacity incrementallyâ€¦ modify Worcester and Evansville / implement fast-cycle handling / continue selective third-party relationships").

## How to apply

1. **Lay out the four elements first:** Opening Scene, Disturbing Event, R1, R2 â€” R2 quantified as an end product.
2. **Locate the reader among the seven situations** to pick the correct Question, then read the elements left-to-right-and-down into an S-C-Q introduction.
3. **Structure the analysis before gathering data.** From the Opening Scene, build a diagnostic framework (divide / cause-effect / classify) whose branches are **yes/no questions**.
4. **Use logic trees for solutions.** Lay out MECE possible actions (questions 4â€“5); estimate benefit and risk per branch; pick the recommended set.
5. **Validate groupings against the trees.** After drafting, map your points onto the framework â€” anything off-tree doesn't belong.
6. **Rename "issues" as "concerns"** unless they're true yes/no questions; delete the "Issues" section and let the analysis supply them.
7. **Let the pyramid fall out of the structure** â€” recommendations on the key line, supporting findings beneath, per `minto-deductive-vs-inductive.md`.

## Common failure modes

- **Data-first analysis.** Gathering everything before thinking; ~60% wasted effort and "interesting" facts only marginally tied to the real problem.
- **Vague R2.** No quantified desired result, so you can't judge when the problem is solved or choose among solutions.
- **Topics labeled "issues."** Lists of concerns dressed as issues, with no yes/no end product to direct the analysis.
- **Non-MECE trees.** Diagnostic or logic-tree branches that overlap or omit causes â€” you'll miss the real driver or chase phantom ones.
- **Confusing diagnostic frameworks with decision trees/PERT.** The former generate questions; the latter reveal actions â€” using the wrong one for cause-finding.
- **An "Issues" section in a proposal.** Almost always redundant; issues = the analytical process = the study's end products.

## References

- Barbara Minto, *The Minto Pyramid Principle* (Minto International, 2010), Intro to Part Three; Ch 8 (Defining the Problem â€” Problem-Definition Framework; Lay Out the Problem; the seven situations / Exhibit 34; Converting to an Introduction; Real-Life Example); Ch 9 (Structuring the Analysis â€” Starting with the Data; Devising Diagnostic Frameworks; Developing Logic Trees; Revealing Flaws in Grouped Ideas; Performing an Issue Analysis). Sequential Analysis: B. Robert Holland, McKinsey & Company, 1972.
- Related: [minto-scqa-introduction.md](minto-scqa-introduction.md) (the problem definition generates S-C-Q), [minto-mece-grouping.md](minto-mece-grouping.md) (diagnostic frameworks and issue trees are MECE structures), [minto-pyramid-structure.md](minto-pyramid-structure.md) (the analysis pre-builds the pyramid), [minto-deductive-vs-inductive.md](minto-deductive-vs-inductive.md) (recommendations-first key line). For slide rendering of trees/decks hand off to `data-viz` / `knaflic`.
