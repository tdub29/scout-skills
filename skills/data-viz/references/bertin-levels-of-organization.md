# Bertin: Levels of Organization

## When to use

Trigger when the prior question is "what kind of data is this?" â€” the analytical step that comes BEFORE choosing a chart type or encoding. Concrete cues:

- The user is starting a new chart and is unsure how to treat a variable
- A column in a dataset could plausibly be categorical OR ordinal (Likert scales, satisfaction ratings, education levels)
- The user wants to take a mean / median / ratio and is unsure if the data type permits it
- A chart's reading "feels off" and the user suspects the data type is being misrepresented
- The user is reading about Stevens' measurement levels (nominal/ordinal/interval/ratio) and trying to map them to chart decisions
- "Can I sort this?" / "Can I average this?" / "Does subtraction make sense here?"
- The user wants to write a data dictionary or schema with the right type annotations
- A statistician or PM is pushing back on a chart with "those categories aren't ordered"

Don't trigger for: chart-type selection once the level is known (route to general data-viz), encoding within a level (route to `bertin-retinal-variables`), or pure stats questions ("which test should I use"). This skill is the data-type classification step, not the visualization step.

## The framework

### Core thesis

Every variable in a dataset operates at exactly one of three organizational levels. The level determines what mathematical operations make sense, what relationships are *real* in the data vs. invented by the encoding, and which visual variables can carry the data without lying. Bertin's levels predate Stevens' more famous nominal/ordinal/interval/ratio typology by ~20 years and collapse Stevens' four-level system into three by treating interval and ratio together (both are Qn).

### The three levels

**Q â€” QUALITATIVE (nominal).** Categories with no inherent order. Examples: blood type (A, B, AB, O); product line (SaaS, Marketplace, Consumer); country of origin; survey respondent ID. The only valid operations: equality and counting. No ordering, no arithmetic. "Country A *is* country A; country A is not country B." Comparing A > B is meaningless.

**O â€” ORDERED (ordinal).** Categories with a meaningful rank but no measurable distance between ranks. Examples: education level (high school < bachelor's < master's < PhD); Likert satisfaction (very dissatisfied < dissatisfied < neutral < satisfied < very satisfied); race finish position (1st, 2nd, 3rd). Valid operations: equality, counting, ordering. Not valid: arithmetic, ratios. "PhD comes after bachelor's, but PhD is not 'twice' bachelor's."

**Qn â€” QUANTITATIVE (interval or ratio).** Numerical with measurable distance and meaningful arithmetic. Examples: revenue in dollars; temperature in Celsius; age in years; count of website visits. Valid operations: equality, ordering, addition, subtraction, ratios (for ratio-level data â€” Celsius is interval not ratio because 0Â°C is arbitrary; Kelvin is ratio). "Customer A spent $100 more than customer B" is meaningful; "A spent twice as much as B" is meaningful (ratio scale).

### The hierarchy (Qn âŠƒ O âŠƒ Q)

Quantitative data is *also* ordered AND qualitative. You can always treat ratio data as ordered (e.g., rank customers by revenue) or as categorical (e.g., bucket revenue into bands). You CANNOT go up the hierarchy â€” you can't treat nominal data as ordinal (countries are not ranked) or ordinal as quantitative (3rd place is not "1.5Ã—" 2nd place).

This matters because **down-leveling is information-destroying but valid; up-leveling is information-inventing and false**.

### Why levels constrain encoding

Each visual variable supports a specific perceptual range (see `bertin-retinal-variables`):

- **Qn (quantitative) data** can only be encoded by position (x, y) or size â€” the two variables that support quantitative perception. Encoding ratio data as hue, shape, or even value is information loss.
- **O (ordered) data** can be encoded by position, size, value, or texture (all support ordered perception). Cannot be encoded by hue or shape â€” those don't support order.
- **Q (nominal) data** can be encoded by ANY selective variable â€” hue, shape, orientation, position. Choice is largely about cardinality and aesthetics.

Mismatched encoding â†’ silent communication failure. A bar chart of countries' GDP encoded by length is correct (Qn â†’ size). A pie chart of "favorite color" encoded by hue is correct (Q â†’ hue). A bar chart of education level (ordinal) plotted as length on a y-axis with equal spacing implies arithmetic distance that doesn't exist â€” sometimes acceptable, often misleading.

### The most common level confusions

- **Likert scales as quantitative.** "Strongly agree" through "strongly disagree" coded as 1â€“5, then averaged. This treats ordinal data as Qn â€” the "distances" between 1 and 2 vs. 4 and 5 aren't proven equal. Common, often defensible by convention (especially with 5â€“7 point scales and large samples), but the user should know they're making an upward leap.
- **Star ratings as quantitative.** "Average 4.2 stars" â€” same issue. Convention has made it acceptable, but technically star ratings are ordinal, not ratio.
- **IDs as quantitative.** Customer ID = 12345. The number looks numerical but is nominal â€” you can't average customer IDs. SQL/pandas will happily compute the mean and produce a garbage answer.
- **Year as ordinal vs. Qn.** A year (2020) is technically Qn (you can subtract years to get a duration), but when used as a category for grouping ("show 2020 vs 2021"), it's being used categorically. The "level" depends on the analytical use, not just the column type.
- **Rank data masquerading as quantitative.** Finish positions, leaderboard ranks. Position 1 to position 2 is one rank apart, but the *gap* in underlying performance may be enormous or tiny. Plotting ranks on a Qn axis implies equal gaps that don't exist.

### Length within a level

A component at a level still has a "length" â€” the number of distinct values. A nominal variable with 3 categories vs. 50 categories has the same *level* but very different visualization implications. The length determines:

- Which retinal variables can carry the data (hue maxes out around 7â€“10 distinct categories; shape around 5)
- Whether the chart should encode the variable directly or aggregate it (50 categories rarely all belong on one chart)
- Whether to use position (suitable up to a few hundred for points) or color (saturates quickly)

## How to apply (step-by-step)

1. **List the components you intend to display.** For each one, isolate it: forget the chart you're imagining and ask, "what kind of measurement is this column, by itself?"

2. **Apply the three-question test to each component:**
   - Can you meaningfully say A < B? If no, it's Q (nominal).
   - Can you meaningfully say A is "twice" B? If no, but ordering works, it's O (ordinal).
   - Can you meaningfully add or subtract values and the result has interpretation? If yes, it's Qn (quantitative).

3. **Flag borderline cases.** Likert scales, star ratings, NPS scores, year-as-grouping â€” these often get treated as Qn by convention but are technically O. Decide explicitly: are you using convention or rigor? Either is fine; just don't slip without noticing.

4. **List the encoding constraints per component.**
   - Qn â†’ position or size only
   - O â†’ position, size, value, or texture
   - Q â†’ any selective variable (hue, shape, orientation, position)

5. **Check the chart you have in mind against the encoding constraints.** Is the variable's level matched to the variable's encoding? If not, either re-encode or down-level the data (acceptable) â€” never up-level (false).

6. **Note the lengths.** For each component, count distinct values. Check that the chosen encoding has enough length to carry it (e.g., hue saturates around 7â€“10 categories â€” don't try to encode 30 product lines by hue).

7. **Produce the classification artifact.** A table per component:

   | Component | Level | Length | Valid encodings |
   |---|---|---|---|
   | Revenue | Qn | continuous | position, size |
   | Region | Q | 5 | hue, shape, position |
   | Satisfaction (Likert 1â€“5) | O (or Qn by convention) | 5 | position, size, value |

8. **Sanity-check the chart.** Read the implied claims aloud. "This bar chart's length implies that 'PhD' is 4Ã— 'high school' in the data" â€” if the data doesn't support that arithmetic, fix the encoding (e.g., dot plot at categorical positions, or use value gradation).

## Common failure modes

- **Up-leveling.** Treating nominal as ordinal, or ordinal as quantitative, to enable an analysis the data doesn't support. The classic: averaging Likert responses. Sometimes acceptable, sometimes not â€” the rule is to *know you're doing it*, not to pretend the level is higher than it is.

- **Down-leveling without knowing.** Plotting numerical revenue as buckets ("High / Medium / Low") on a categorical axis throws away information. Fine if the user wants categorical insight; bad if they wanted to see distribution.

- **Mistaking columns for levels.** A column type (`int`, `varchar`, `decimal`) does not determine the level. Customer ID is an `int` but nominal. Year is `int` but used variably. Level is about *meaning*, not storage type.

- **Confusing length with level.** A nominal variable can have 2 or 200 values; level is unchanged. A quantitative variable can be discrete (count of visits) or continuous (revenue); level is unchanged. Length and level are independent dimensions.

- **Treating ranks as quantitative.** Finish positions, leaderboard ranks, even percentiles â€” all ordinal at best. Subtracting "rank 5 minus rank 2 = 3 rank-units" is technically valid as an ordinal operation but ratio claims ("rank 5 is 2.5Ã— rank 2") are false. Don't plot ranks on a Qn y-axis if magnitude implications matter.

- **Ignoring the hierarchy.** Refusing to use a Q-level encoding for Qn data when it would simplify the chart (e.g., "Customer A is in the high-revenue bucket") is over-rigor. Down-leveling is legitimate. Up-leveling is the only sin.

- **Treating Bertin and Stevens as identical.** Stevens splits Qn into interval (Celsius â€” no true zero) and ratio (Kelvin â€” true zero). Bertin lumps them. For most practical viz work, Bertin's three-level system suffices; if your analysis depends on true-zero behavior (ratios meaningful), use Stevens to disambiguate within Qn.

- **Skipping the classification step entirely.** Jumping straight to "what chart should I use?" without classifying the components. This is the single most common cause of charts that "look right but feel wrong." The level decision is the foundation; everything downstream depends on it.

## References

- Jacques Bertin, *Semiology of Graphics* (1967; English 1983; Esri 2011 ed.), chapter I.D â€” "The Level of Organization of the Components," book pages 34â€“38. The hierarchy (Q âŠ‚ O âŠ‚ Qn) appears explicitly with examples on pages 36â€“38.

- Stevens, S. S. (1946). "On the theory of scales of measurement." *Science.* The more famous 4-level system (nominal/ordinal/interval/ratio); Bertin's 3-level system can be mapped onto it (Q â‰ˆ nominal; O â‰ˆ ordinal; Qn â‰ˆ interval + ratio).

- Sibling skills:
  - `bertin-retinal-variables` â€” the encoding choice that this skill's level classification feeds into. Run them together: classify the level here, then route to retinal-variables to pick the channel.
  - `bertin-invariant-components` â€” the prior analysis step (what *are* the components in the first place?)
  - `bertin-image-vs-figuration` â€” the cognitive layer that uses the encoded chart

- Related Tufte skills: `tufte-graphical-integrity-principles` (Principle 5 â€” information-carrying dimensions â‰¤ data dimensions â€” is Bertin's level-matching restated as integrity).
