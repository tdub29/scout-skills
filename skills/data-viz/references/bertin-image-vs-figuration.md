# Bertin: Image vs. Figuration

## When to use

Trigger when the question is "how cognitively expensive is this chart to read?" â€” not "is it pretty," not "is it accurate," but how many distinct perceptual moments a reader needs to extract the chart's information. Concrete cues:

- The user has a chart with 4+ components or many cells and it "feels heavy" to read
- A dashboard with multiple coordinated panels and the user is debugging why it's overwhelming
- "This chart takes 30 seconds to interpret and I want it to take 1 second"
- The user is deciding between one big chart and a grid of small ones (route here for the cognitive-load tradeoff; then route to `tufte-small-multiples` for the design pattern)
- A heatmap or matrix layout that looks unified but the user notices readers scanning back and forth
- The user is reading Tufte's small-multiples chapter and wants Bertin's cognitive theory underneath
- A chart "looks fine" individually but in context (slide deck, dashboard) feels like work to parse
- "Why do readers seem to miss the main pattern here?"

Don't trigger for: chartjunk removal (`tufte-chartjunk`), data-ink optimization (`tufte-data-ink-ratio`), aesthetic polish, or chart-type selection. This skill operates at the perception/cognition layer â€” observation time per question â€” not at the design-grammar layer.

## The framework

### Core thesis

A chart's frame might look unified but the cognitive experience of reading it might not be. Bertin distinguishes:

- **IMAGE** â€” a graphic whose essential correspondences can be perceived in a *single instant of vision*. One glance, all relevant relationships extracted, no mental accumulation. The eye isolates the input, perceives the correspondences, outputs the answer â€” all simultaneously.

- **FIGURATION** â€” a graphic that occupies one visual frame but whose information requires *multiple successive perceptions* to extract. Each glance reveals a fraction; the brain has to stitch fragments together. The frame is one; the cognitive load is many.

The distinction matters because **efficiency** â€” Bertin's formal criterion for chart quality â€” is defined by observation time per question. An image answers fast. A figuration is slow regardless of how clean it looks. Bertin links this to Zipf's principle (cognitive economy): the right chart minimizes mental cost for the questions readers actually ask.

### The three reading levels

Every question a reader asks of a chart falls into one of three levels:

1. **ELEMENTARY** â€” single-value lookup. "What was revenue in March 2023?"
2. **INTERMEDIATE** â€” subgroup pattern. "How did Q1 2023 compare to Q1 2022?" "What's the trend in the western region?"
3. **OVERALL** â€” whole-data shape. "Is revenue growing, flat, or shrinking over the full period?" "Are most regions converging or diverging?"

An efficient image supports all three levels in single glances. A figuration typically supports only elementary reading (you can find individual cells) while intermediate and overall reading require sustained scanning, mental aggregation, or impossible holds on working memory.

This is why heatmaps with 100+ cells are figurations: you can find any single cell (elementary), but answering "which region cluster has the highest values" requires the reader to mentally aggregate dozens of cells. By the time they're done, they've forgotten the first few.

### Why 3 components is the soft ceiling

The plane carries 2 components (x, y). One retinal variable adds a third (color, size, etc.). With 3 components honestly encoded, a graphic can usually be an image â€” the reader perceives all the correspondences in one moment. Add a 4th component (a second retinal variable) and the reader starts juggling: "How does the size relate to the color across positions?" The chart often slips into figuration.

The 3-component ceiling is approximate, not strict. With careful design â€” strong primary encoding, weak secondary, and questions that don't require crossing all 4 dimensions â€” 4-component graphics can stay image-like. Beyond 4, figuration is almost guaranteed unless you split into multiple images.

### Efficiency: the formal criterion

Bertin proposes a comparison test rather than a beauty judgment: given two graphics encoding the same data, the more efficient one is the one that lets a reader answer a target question in less time. This is testable â€” A/B a chart and time the reader's correct answer. Aesthetics don't decide; the stopwatch does.

In practice you don't need to run a stopwatch test for every chart. The proxy: count the "images" (distinct perceptual moments) a reader must accumulate to answer the questions you care about.

- 1 image to answer the question â†’ efficient
- 2â€“5 images â†’ tolerable, but borderline figuration
- 5+ images â†’ figuration; the chart cannot honestly claim to be read in a glance

### How figurations sneak in

The trap is that figurations *look* unified. A heatmap is one rectangular grid; a multi-axis chart is one frame; a complex dashboard panel is one box. The visual frame says "I'm one thing." The cognitive reality says "I'm 50 things you have to compare."

Common figuration patterns:
- **Dense heatmaps** (>30 cells) â€” elementary lookup works; intermediate and overall reading require mental aggregation
- **Multi-series line charts with 5+ overlapping series** â€” each series is its own image; cross-comparing them is multi-image accumulation
- **Bubble charts where size + color + position all encode different variables** â€” 4-component, almost always figuration unless one channel dominates
- **Maps with multiple thematic layers** â€” geographic frame is unified; reading any specific layer requires isolating it from the others
- **Dashboards with many small charts coordinated only by topic** â€” each chart is its own image; cross-chart relationships are multi-image

### When figuration is OK

Not every chart needs to be an image. Some honest cases for figuration:

- **Lookup tables.** If the chart's purpose is "find a specific value," elementary reading is all that matters and figuration is fine.
- **Exploration tools.** Interactive charts where the reader can drill in: the user is *expected* to spend time, and the figuration becomes a navigable surface.
- **Reference posters / wall charts.** Designed for sustained study, not instant comprehension.

The error is calling these figurations "images" when claiming efficiency, or designing for a single-glance use case but shipping a figuration.

## How to apply (step-by-step)

1. **List the questions the chart should answer.** What are readers actually doing with this graphic? Lookup ("what was X")? Pattern-finding ("what's the trend")? Comparison ("which is highest")? Be specific and explicit.

2. **Classify each question by reading level.** Elementary, intermediate, or overall.

3. **For each question, count how many distinct images (perceptual moments) it requires.**
   - Can the reader answer it in one glance, without scanning back and forth? â†’ 1 image (efficient)
   - Does the reader need to isolate one region, then another, and compare? â†’ 2+ images (multi-image figuration)
   - Does the reader need to hold many cells in working memory before aggregating? â†’ many images (figuration)

4. **Check coverage across reading levels.** An efficient design supports all three levels in single glances when needed. If elementary works but intermediate / overall require multi-image work, that's the failure mode â€” and it's the diagnosis for the redesign.

5. **If the chart is a figuration, choose the remedy.**
   - **Reduce components.** Cut the data scope to 3 components or fewer. (Often the most powerful move.)
   - **Re-encode for hierarchy.** Make one encoding clearly primary, others secondary. Reduces juggling.
   - **Switch to small multiples.** Convert a 4-component grid into a set of 3-component panels â€” each panel is its own image (route to `tufte-small-multiples`).
   - **Replace with a different chart type.** Sometimes the same data fits an image when re-shaped (e.g., a busy parallel-coordinates plot â†’ a parallel-set diagram).
   - **Accept the figuration but disclose.** If the use case genuinely needs all the data and the chart is for exploration, label it as such â€” don't claim instant-readability.

6. **Re-test by predicting glances per question.** After the redesign, walk through the questions again. How many images does each one need now? If the count is meaningfully lower (and not at the cost of dropping a question that mattered), the redesign works.

7. **If you can A/B test, time it.** Show the original and the redesign to fresh readers; ask them the questions; time correct answers. The stopwatch is Bertin's actual test.

## Common failure modes

- **Mistaking the visual frame for an image.** A heatmap has one rectangular boundary, therefore "it's one chart" â€” but as Bertin shows, the cognitive count of distinct images required to read it can be in the dozens. The frame is the figuration; the image is what the eye can actually grasp in one moment.

- **Designing for elementary reading only.** A chart where readers can look up any value but can't see overall pattern. Common in financial reports â€” every cell is correct, the chart's overall shape is invisible. Bertin's test exposes this: ask "what's the dominant pattern across all data?" If the reader can't answer in one glance, intermediate/overall reading is broken.

- **Designing for overall reading only.** The opposite failure: a chart shows a smooth trend or shape, but readers can't extract specific values. Editorial infographics often have this problem.

- **Assuming "clean = efficient."** A clean, minimal chart with 5 overlapping line series is still a figuration. Removing chartjunk doesn't fix multi-image accumulation. The remedy is structural (reduce components, split into multiples), not cosmetic.

- **Adding a fourth encoding when readers can't perceive it.** "I'll add color to the bubble chart for the new variable." Now the chart has x-position, y-position, size, AND color. Readers perceive maybe two cleanly. The fourth encoding is invisible most of the time.

- **Pretending a dashboard is one image.** Multiple coordinated charts can each be their own efficient image, but the dashboard *as a whole* is a figuration. Each cross-chart relationship requires multi-image accumulation. Acknowledge this; design for the use cases that are dashboard-local vs. those that require cross-chart synthesis.

- **Skipping the question enumeration.** "Make it efficient" without naming the questions. Without specific questions, efficiency is undefined â€” there's no clock to start. Always list questions first.

- **Confusing image vs. figuration with chartjunk or data-ink.** Chartjunk is decorative noise; data-ink is structural ink usage; image/figuration is cognitive load. A chart can be perfectly clean (no chartjunk, high data-ink ratio) and still be a figuration. They operate at different layers. Run all three audits when integrity / efficiency matter.

## References

- Jacques Bertin, *Semiology of Graphics* (1967; English 1983; Esri 2011 ed.):
  - Chapter I.A â€” "The Invariant and the Components," book pages 28â€“30. Where image, figuration, and the three reading levels are first introduced.
  - Chapter III.B â€” "Image Theory: Efficiency," book pages 139â€“170. The full theoretical exposition: stages of reading (p. 140), definition of an image (p. 142), construction (p. 148), limits (p. 154), and the three functions of graphic representation (p. 160).

- Sibling Bertin skills:
  - `bertin-retinal-variables` â€” what gets encoded at each layer affects how many distinct images are possible
  - `bertin-levels-of-organization` â€” data type affects which encodings preserve image-quality
  - `bertin-reorderable-matrix` â€” a specific technique for converting a figuration into a sequence of images via permutation
  - `bertin-legibility-rules` â€” quantitative thresholds for when an image stops being legible at all

- Related Tufte skills:
  - `tufte-small-multiples` â€” the design pattern that Bertin's framework theoretically justifies. Tufte teaches *how* to use small multiples; Bertin teaches *why* they work (each panel is its own image)
  - `tufte-data-density` â€” closely related but distinct: density is about ink-per-area; image/figuration is about glances-per-question
