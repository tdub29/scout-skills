# Bertin: The Reorderable Matrix

## When to use

Trigger when the user has a multivariate table and the question is "what's in here?" â€” not "how do I display this?" Concrete cues:

- The user has a data table with many rows and several columns and is trying to find structure
- "I have 50 customers across 8 metrics and I can't see what's interesting"
- The user wants to cluster but hasn't decided on a statistical method
- An existing heatmap looks like noise; the user suspects there's pattern hidden by row/column order
- The user is reading about hierarchical clustering, seriation, or dendrogram-ordered visualization
- "Should I reorder this table?" / "Is there a natural grouping in this data?"
- The user wants to compare two rankings (e.g., two leaderboards) and quantify the difference
- A scatterplot matrix looks busy and the user suspects ordering would help
- The user is doing exploratory data analysis and unsure where to start
- Modern context: the user is building a clustered heatmap (seaborn `clustermap`, R `pheatmap`) and wants to ground the technique in theory

Don't trigger for: finished communication graphics (route to general data-viz / Tufte); pure stats / hypothesis testing; single- or two-variable problems where permutation isn't possible; large-N machine learning workflows where the methodology won't scale. This skill is exploratory and human-scale (10sâ€“1000s of rows; up to ~50 columns).

## The framework

### Core thesis: graphics as instruments of processing

Bertin's revolutionary claim, often missed in modern data-viz pedagogy: a graphic is not just a display medium â€” it can be a *processing tool*. By reordering rows and columns of a table and visually encoding the values, you turn the act of viewing into the act of analyzing. Pattern, cluster, and anomaly emerge through visual rearrangement rather than through prior statistical modeling.

In Bertin's framing:
- **Recording** â€” graphics as exact preservation (tables, archives)
- **Communicating** â€” graphics as fast transfer to a viewer (the world Tufte focuses on)
- **Processing** â€” graphics as discovery instruments (this skill's territory)

The reorderable matrix is the canonical processing tool. It predates modern algorithmic clustering by decades and remains a useful first-pass analysis even when sophisticated methods are available â€” partly because the human eye is excellent at spotting patterns that don't conform to any statistical model.

### The basic technique

You have a table: N rows (cases â€” customers, villages, products, time points), M columns (variables â€” metrics, dimensions). Each cell holds a value.

1. **Visualize each cell as a magnitude.** Encode the value as the *darkness* of the cell â€” black for high, white for low (or vice versa), with grays in between. (Bertin's preferred encoding because value is ordered AND because the eye groups dark cells automatically.)

2. **Reorder the rows.** Pick an ordering criterion (e.g., the total of all values per row, the value of a specific column, an external attribute like age or region). Re-sort the rows by that criterion.

3. **Reorder the columns.** Same logic: by total per column, by similarity to another column, by external attribute.

4. **Look at the resulting image.** Does the table show:
   - **Bands of dark and light** (gradient pattern â†’ ordered structure)?
   - **Blocks of dark surrounded by light** (clusters)?
   - **Single dark cells in light regions** (anomalies / outliers)?
   - **Diagonal pattern** (correlated ordering between row and column criteria)?
   - **No pattern** (data is genuinely random OR the reorder criterion is wrong)?

5. **Try different orderings.** The first ordering rarely reveals everything. Cycle through several â€” by row total, by specific column, by external attribute. The technique's power comes from comparing what each ordering surfaces.

6. **Record findings as you go.** Each useful ordering is its own "image" of the data. You may want to save 2â€“4 distinct orderings as the final analytical artifact.

### Image-file: the physical version

Bertin's original method used physical cards. Each row of the data became a card, with cells along the card encoded as varying-darkness shading. The cards stacked vertically; you could pick up the stack and physically rearrange it â€” sort by one column, then by another, then by total â€” and watch the visual pattern shift.

Modern equivalent: a clustered heatmap in your tool of choice (Seaborn, R `pheatmap`, Excel conditional formatting, an interactive matrix-permutation tool). The cards are gone but the methodology is identical.

### Sub-techniques

Bertin's chapter unifies several variations under one framework:

- **Image-file** â€” the physical card method described above. Best for small-N (â‰¤100 rows), exploratory work.
- **Matrix-file** â€” extension to two-dimensional rearrangement; both rows AND columns permute.
- **Ordered table** â€” a snapshot of one specific ordering, frozen as an analytical artifact.
- **Collection of ordered tables** â€” multiple snapshots, presented together to compare structures.
- **Array of curves** â€” when columns are time-series, each row's curve becomes the visual signature; reorder the curves to find similar shapes.
- **Comparison of orders (inversion counting)** â€” given two rankings of the same N items, count the number of pair-inversions to quantify how different the rankings are.

All share one principle: *the order is not given â€” the analyst chooses it, and the chosen order reveals (or hides) the pattern.*

### When the methodology shines vs. fails

**Shines when:**
- Moderate N (10â€“500 rows) and moderate M (3â€“30 columns)
- Data values vary widely enough to encode as visible saturation differences
- The user is open to multiple hypotheses about what structure exists
- No prior commitment to a clustering algorithm or model
- Anomaly hunting (single-cell outliers stand out instantly)

**Fails when:**
- N is huge (>>1000 rows) â€” visualization breaks down; the matrix becomes texture
- All values are clustered tightly (no saturation contrast to encode)
- The "right" pattern requires specific statistical modeling that simple ordering can't capture
- The user wants confirmatory analysis (this is exploratory)
- M >> 50 (too many columns to perceive in one image)

### Modern descendants

The reorderable matrix lives on, often without attribution:

- **Clustered heatmaps** (Seaborn `clustermap`, R `pheatmap`, Plotly heatmap with reordering) â€” directly implement Bertin's methodology with automated reordering via hierarchical clustering
- **Dendrogram-ordered matrices** in genomics and bioinformatics
- **Seriation algorithms** in archaeology and operations research
- **Sankey diagrams** with reorderable axes
- **Interactive matrix-permutation tools** like Bertin.js, Bertifier

If the user is using any of these, they're using Bertin's methodology â€” knowing the underlying framework makes them more deliberate about ordering choices.

## How to apply (step-by-step)

1. **Confirm the data shape.** Rows Ã— columns, with each cell a meaningful magnitude. If the data isn't already in this shape, reshape it (pivot, melt, etc.). Aim for N â‰¤ ~500 rows, M â‰¤ ~30 columns for human-scale work.

2. **Establish the visual encoding.** Value (lightness/darkness) is Bertin's preferred encoding because it's ordered and instinctively forms visual groups. Black = high, white = low (or domain-appropriate inversion). If using a tool, a sequential color map with strong saturation contrast (viridis, magma, single-hue ramp).

3. **Decide on candidate orderings.** Brainstorm 3â€“6 orderings worth trying:
   - By row total (or column total)
   - By the values of one specific row / column
   - By an external attribute not in the matrix (date, region, customer tenure)
   - By a derived attribute (PCA first component; hierarchical clustering distance)
   - By similarity to a reference row / column

4. **Apply each ordering, observe, document.** For each ordering, reorder the matrix (rows alone, columns alone, or both) and look. Note what's visible:
   - Banding / gradient â†’ ordered structure aligned with the criterion
   - Blocks â†’ cluster
   - Outlier cells â†’ anomaly
   - Diagonal â†’ correlation between the row and column criteria
   - Noise â†’ no structure under this criterion, try another

5. **Iterate.** Combine orderings. Try row-by-criterion-A and column-by-criterion-B. See if the picture clarifies.

6. **Identify the "best" orderings.** Usually 1â€“3 orderings are revealing; the others are not. The revealing orderings ARE your analytical findings.

7. **Produce the findings document.** For each revealing ordering:
   - State the ordering criterion in one sentence
   - Identify the pattern visible (clusters? gradient? outliers?)
   - Name the clusters / anomalies in domain terms
   - Suggest follow-up analysis (statistical test? deeper dive? action?)

8. **Sanity-check.** Show the matrix to someone unfamiliar with the data. Can they describe the pattern from the visual alone? If yes, the methodology worked; if no, either the pattern isn't really there or the encoding needs adjustment.

## Common failure modes

- **Encoding values as hue instead of value.** Color (hue) is not ordered â€” readers can't tell that "red" is higher than "blue" without a legend. Saturation/value gradients work without legends; hue requires the eye to consult the legend each time. Use a single-hue sequential ramp, not a rainbow.

- **Sticking with the first ordering.** The whole point of the reorderable matrix is that ordering is not given. If you apply one ordering and call it done, you've used a heatmap, not a reorderable matrix. The methodology lives in the *comparison* of orderings.

- **Too many rows for the eye.** Above ~500 rows, the matrix becomes texture rather than a perceivable grid. Either aggregate, sample, or switch to statistical clustering with the matrix as a confirmation step rather than the primary analysis.

- **Too few values of contrast.** If all cells are similar magnitude (say, all between 4.0 and 4.2 on a 0â€“5 scale), the saturation differences will be invisible. Either rescale (subtract the mean, divide by std â€” display z-scores) or accept that the matrix has no useful structure to reveal.

- **Confusing reordering with statistical clustering.** They overlap but aren't identical. Statistical clustering imposes a specific distance metric and algorithm (k-means, hierarchical, DBSCAN); Bertin's reorderable matrix lets you try arbitrary orderings, including ones a clustering algorithm wouldn't suggest. Use them together: clustering for first-pass automation, Bertin permutations for "what does this *look* like."

- **Treating the matrix as a finished communication artifact.** This is an exploratory tool. Don't ship the working matrix unchanged to a stakeholder presentation â€” that's mistaking processing for communicating. If a finding from the matrix matters, redraw a *communication* graphic that highlights just that finding.

- **Ignoring anomalies.** The eye picks out individual dark cells in light regions instantly. Don't lose that information just because it doesn't fit a cluster. Sometimes the anomaly IS the finding â€” a single customer who behaves nothing like the rest, a village that breaks the regional pattern.

- **Skipping the external-attribute reordering.** Reordering by row total or column total is mechanical and often boring. The interesting orderings are by attributes *not encoded in the matrix* â€” region, customer tenure, time of acquisition. Those reveal whether the matrix patterns align with structures the data doesn't explicitly contain.

- **Not iterating across both row AND column orderings.** Often, the pattern emerges only when both are reordered simultaneously. Trying only row reorderings (or only column reorderings) misses the cluster blocks that require both.

## References

- Jacques Bertin, *Semiology of Graphics* (1967; English 1983; Esri 2011 ed.), Part Two, Chapter I.C â€” "Problems Involving More Than Three Components," book pages 254â€“268. Includes:
  - "Graphic information-processing" (p. 254)
  - "The reorderable matrix" (p. 256) â€” the canonical exposition
  - "The image-file" (p. 258)
  - "The matrix-file" (p. 263)
  - "An array of curves" (p. 263)
  - "An ordered table" / "A collection of ordered tables" (p. 265)
  - "A collection of maps or a matrix permutation?" (p. 268)

- Bertin's later book *La graphique et le traitement graphique de l'information* (1977) extends the matrix methodology with more case studies.

- Sibling Bertin skills:
  - `bertin-retinal-variables` â€” why value/saturation is the right encoding for matrix cells (it's the only ordered, dissociative-when-needed channel that works at small implantation)
  - `bertin-image-vs-figuration` â€” the reorderable matrix is the canonical example of using permutation to convert a figuration (the unordered grid) into an image (the ordered grid)
  - `bertin-levels-of-organization` â€” Bertin emphasizes that ordering only makes sense for O or Qn data; if your columns are Q (nominal), permutation logic differs

- Modern descendants:
  - Hahsler et al. *seriation* R package (and the underlying seriation literature) â€” algorithmic reorderable matrices
  - Bertin.js, Bertifier â€” interactive matrix-permutation web tools
  - Seaborn `clustermap`, R `pheatmap` â€” clustered heatmap implementations that automate the ordering step
