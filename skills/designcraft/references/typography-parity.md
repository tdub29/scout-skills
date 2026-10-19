# Typography and composition parity

> **Last reviewed:** 2026-10-10 Â· **Last updated:** 2026-10-10 Â· **Change:** major (first version, from the full re-measure) Â· **Target:** Adobe InDesign 2026 (21.6)

Typesetting is what InDesign is bought for. A feature can exist and still set text differently
from InDesign: different line breaks, different page count, overset where InDesign fits. This
document tracks both: does the attribute exist, and does it compose like InDesign? Script-specific
detail lives in [cjk-typography.md](cjk-typography.md), [cjk.md](cjk.md) and
[arabic-typography.md](arabic-typography.md). Overall numbers: [target-app-parity.md](target-app-parity.md).

**Dimension score: ~45% ready (estimated), 120â€“200 h to parity.** Presence is high (76% scored below, nothing absent); fidelity
against InDesign is **unmeasured**, which is the main gap.

## Fidelity: how we'd know

There is no oracle yet. What exists: unit tests of break points and invariants in
`crates/compose/src/tests.rs` (165 tests in the crate), IDML files built by DesignCraft and opened
in InDesign 2026 by hand, and user reports comparing the two (#179, #180, #181, #282â€“#295).

**Needed (gap 4 in [gaps.md](gaps.md)):** a set of synthetic stories (our own text and fonts:
Source Serif 4, Inter, Shippori Mincho from craft-fonts) covering each row below, set in InDesign
2026 by observation on the owner's Mac (results under `plan/`, never committed), exported as IDML;
DesignCraft opens the IDML and a test compares per paragraph: line count, break positions (by
character offset), last-line width, overset and frame fit. Report the share of paragraphs whose
breaks match exactly. Target for beta: â‰¥ 90% of Latin body paragraphs identical, 100% fit in the
same frames.

## Checklist

Status: **âœ“** present and believed close Â· **~** present, known differences or partial Â· **âœ—** missing.
Fidelity: **unmeasured** unless stated.

| Area | InDesign 2026 | DesignCraft | Status | Notes / evidence |
|---|---|---|---|---|
| Paragraph Composer | Adobe's multi-line composer | Knuthâ€“Plass total fit, fitness classes, hyphen penalties | ~ | same family of algorithm, Adobe's weights unknown; breaks will differ on some paragraphs |
| Single-line Composer | greedy | greedy with the same ranges | âœ“ | |
| World-Ready composers | Paragraph / Single-line World-Ready | RTL, Arabic and bidi in the main composer | ~ | Indic scripts (Devanagari etc.) shape through harfrust but are untested |
| Justification | word/letter spacing, glyph scaling min/desired/max, single-word, last line | all of these | âœ“ | a justified line with a tab now justifies after the tab (#284) |
| Hyphenation | per-language dictionaries (~40), zone, limits, capitalized, last word, across columns | Liang patterns: English (trained from the public-domain Moby list) and Spanish (Bezos); zone, limits, exceptions in the user dictionary | ~ | other languages don't hyphenate (#87 reported "doesn't work") |
| Spelling | per-language dictionaries | English (Moby) + document/user dictionary | ~ | |
| Kerning | Metrics, Optical, manual, none | Metrics, manual, none | ~ | **Optical treated as Metrics** (#181): imported display text sets wider and can overset |
| Tracking, scale, skew, baseline shift | âœ“ | âœ“ | âœ“ | |
| OpenType features | ligatures, discretionary, swash, fractions, ordinals, figures, small caps, stylistic sets, positional forms | through harfrust | âœ“ | |
| Variable fonts | axes in Character panel | named instances and free axis values; PDF embeds the instance | âœ“ | |
| Leading | auto (120%), absolute, leading model | âœ“ | âœ“ | CJK leading models in cjk-typography.md |
| First baseline | ascent, cap height, x-height, leading, fixed, min | âœ“ | âœ“ | |
| Frame fit / overset | baseline of the last line must fit | descenders must fit | ~ | **differs** (#180): frames go overset where InDesign fits |
| Baseline grid | document and frame grids | âœ“ | âœ“ | |
| Vertical justification | top, centre, bottom, justify, paragraph spacing limit | âœ“ | âœ“ | |
| Columns, span / split columns | âœ“ | âœ“ | âœ“ | split columns within a column (#295); text after a span flows below it (#276) |
| Column rules | âœ“ | âœ“ (screen, PDF, IDML) | ~ | no stroke types or overprint (#274) |
| Keep options and breaks | keep with next, lines together, start in next column/frame/page/odd/even | âœ“ | âœ“ | break characters end paragraphs (#285); the line before a break is a last line (#283) |
| Drop caps, nested, line and GREP styles | âœ“ | âœ“ | âœ“ | |
| Bullets and numbering | lists, levels, formats, restart, across stories | âœ“ | ~ | numbering expressions from IDML (#298); Convert Bullets/Numbering to Text missing |
| Tabs | left/center/right/decimal/align-on, leaders, right-indent tab | âœ“ | ~ | **Tabs panel missing** (#326); wrapping of lines with tabs fixed (#282) |
| Paragraph rules, borders, shading | âœ“ | âœ“ | âœ“ | |
| Balance ragged lines | âœ“ | âœ“ | âœ“ | |
| Optical margin alignment | âœ“ | âœ“ (hang table of our own) | ~ | hang amounts are ours, InDesign's unknown |
| Text wrap | bounding box, shape, jump object/column, contour options | âœ“ | âœ“ | |
| Anchored objects | inline, above line, custom | âœ“ | ~ | anchored objects in table cells not drawn (#163) |
| Footnotes, endnotes | âœ“ | âœ“ | ~ | footnotes don't split across columns yet |
| Type on a path | âœ“ | âœ“ | âœ“ | |
| Vertical text (CJK) | âœ“ | âœ“ | ~ | see cjk.md |
| CJK composition | mojikumi, kinsoku, aki, tsume, ruby, kenten, warichu, frame grid | most; mojikumi tables kept but not applied; ruby group-only; no frame grid | ~ | cjk.md, cjk-typography.md |
| Arabic / Hebrew | kashida, digits, diacritic positioning, RTL stories and tables | âœ“ | ~ | vendor justification presets unsupported; list bullets and multi-column RTL (#100) |
| Missing glyphs and fonts | pink highlight, substitution | âœ“ | âœ“ | |
| Installed fonts | every activated font | system font folders; user folders, font managers and Adobe Fonts not always found | ~ | #161, #110, #107, #327, #261 |
| Composition highlights | H&J, keeps, custom tracking/kerning, substituted fonts | âœ“ | âœ“ | |

Measured from the table above (2026-10-10): 34 rows, 18 âœ“, 16 ~, 0 âœ—, scoring âœ“ = 1 and ~ = 0.5:
**76%**. Every row exists in some form; the ~ rows are where InDesign users will see a difference.

## Remaining effort

| Work | Opus 5.5 h |
|---|---|
| Oracle harness (synthetic stories, IDML exchange, comparison metric) | 20â€“30 |
| Optical kerning approximation (outline-based side-bearing model) + preflight warning | 15â€“25 |
| Overset rule (baseline fits) and frame-fit parity | 5â€“10 |
| Fixing composer differences the harness finds (weights, penalties, glyph-scaling order) | 40â€“70 |
| Hyphenation patterns for the top 15 InDesign languages (permissive sources) | 20â€“35 |
| Spelling dictionaries beyond English (licence review per language) | 10â€“20 (+ owner review) |
| Tabs panel, list conversion commands | 8â€“15 |
| **Total** | **120â€“200** |

## Revision history

| Date | Change | Summary |
|---|---|---|
| 2026-10-10 | major | Created: typography checklist (34 rows), fidelity gap and oracle plan |
