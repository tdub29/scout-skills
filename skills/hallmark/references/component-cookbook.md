# Component cookbook

Fifty component archetypes you can compose into any macrostructure. Every entry: a *shape*, a one-line "use when", a one-line "don't confuse with", and a short structural sketch (DOM + minimal CSS). Pick from this file when you're building a section and don't know which shape to reach for.

The same macrostructure (e.g., Bento Grid) can be built from many different combinations of these archetypes. The macrostructure picks the *page shape*; this file picks the *components inside it*.

**Diversification rule:** within a single page, no two sections should use the same archetype. A Bento Grid might pair *Bento feature block* with *Inline form CTA* with *Logo wall (hairline)*. The next page Hallmark builds should pick different archetypes from the same categories.

---


---

## Archetype index â€” load ONLY the picks you need

**Pick your archetype names here, then read ONLY those individual files** from `references/components/`. Do not load the whole cookbook. A typical build needs 5â€“7 files: 1 hero + 1 section head + 1â€“2 features + 1 CTA + 1 footer + 1 nav.

### Heroes

- **H1 Â· Marquee** â€” A single statement fills the fold. No subhead, no CTA in view. [`components/h1-marquee.md`](components/h1-marquee.md)
- **H2 Â· Split diptych** â€” Headline + lede on one side, image or product capture on the other. 6/6 or 7/5 columns. [`components/h2-split-diptych.md`](components/h2-split-diptych.md)
- **H3 Â· Quote led** â€” A pull-quote with attribution is the hero. Your headline is borrowed credibility. [`components/h3-quote-led.md`](components/h3-quote-led.md)
- **H4 Â· Stat led** â€” A giant number or metric is the hero. A small qualifier line below. [`components/h4-stat-led.md`](components/h4-stat-led.md)
- **H5 Â· Letter hero** â€” First-person opening â€” "Dear reader,". No buttons in fold. Reads as personal correspondence. [`components/h5-letter-hero.md`](components/h5-letter-hero.md)
- **H6 Â· Photographic fold** â€” Single full-bleed image fills the viewport. Caption sits in a corner. [`components/h6-photographic-fold.md`](components/h6-photographic-fold.md)
- **H7 Â· Demo video clipped by viewport edge** â€” Display headline left, demo video right, the rightmost ~10â€“20 % extending past the viewport so it's intentionally cut off. The clip *is* the design â€” implies "there's more product  [`components/h7-demo-video-clipped-by-viewport-edge.md`](components/h7-demo-video-clipped-by-viewport-edge.md)
- **H8 Â· Mockup split browser framed** â€” Headline left, browser-frame mockup right, the mockup tilted 1â€“3Â° for life. Frame can be browser chrome, macOS toolbar, minimal hairline, or floating no-frame. [`components/h8-mockup-split-browser-framed.md`](components/h8-mockup-split-browser-framed.md)
- **H9 Â· Custom illustration centerpiece** â€” A single hand-built SVG (Tier B in the enrichment hierarchy â€” or pure CSS at Tier A for simpler shapes) sitting on the hero as one illustrative element. The bakery loaf, the studio [`components/h9-custom-illustration-centerpiece.md`](components/h9-custom-illustration-centerpiece.md)

### Section heads

- **S1 Â· Left margin numbered** â€” A narrow left column holds `01 â€” LABEL.`; the wide right column holds the heading and content. [`components/s1-left-margin-numbered.md`](components/s1-left-margin-numbered.md)
- **S2 Â· Hanging** â€” Heading floats above the section in negative space; no border, no rule. [`components/s2-hanging.md`](components/s2-hanging.md)
- **S3 Â· Sticky pinned** â€” Heading remains in viewport while content scrolls beneath. Orientation aid. [`components/s3-sticky-pinned.md`](components/s3-sticky-pinned.md)
- **S4 Â· Inline no break** â€” The heading is a small caps phrase that emerges *inside* the body flow; no spatial break. [`components/s4-inline-no-break.md`](components/s4-inline-no-break.md)
- **S5 Â· Bottom anchored** â€” The label or heading sits *below* the section's content. Inverts hierarchy. [`components/s5-bottom-anchored.md`](components/s5-bottom-anchored.md)

### Feature blocks

- **F1 Â· Bento grid** â€” Asymmetric grid of 8â€“15 tiles in mixed spans (1Ã—1, 2Ã—1, 1Ã—2, 2Ã—2). Visual rhythm via size. [`components/f1-bento-grid.md`](components/f1-bento-grid.md)
- **F2 Â· Sticky scroll stack** â€” Sticky left pane, scrolling right pane that cycles through related screenshots. [`components/f2-sticky-scroll-stack.md`](components/f2-sticky-scroll-stack.md)
- **F3 Â· Tabular spec sheet** â€” Each row is a feature; columns hold name, value, footnote. Hairline rules between rows. Tabular numerics. [`components/f3-tabular-spec-sheet.md`](components/f3-tabular-spec-sheet.md)
- **F4 Â· Step sequence** â€” Numbered stages (`1.0 â†’ 2.0 â†’ 3.0`) flow vertically. Each stage has a heading, a paragraph, sometimes a small visual. [`components/f4-step-sequence.md`](components/f4-step-sequence.md)
- **F5 Â· Annotated screenshot** â€” A product capture sits centre-stage with arrows or short labels pointing to UI details. [`components/f5-annotated-screenshot.md`](components/f5-annotated-screenshot.md)
- **F6 Â· Product card grid** â€” Each card is a product, not a feature. Image Â· name Â· price Â· one micro-action. Reads like a shop floor, not a marketing site. [`components/f6-product-card-grid.md`](components/f6-product-card-grid.md)

### CTAs / signups

- **C1 Â· Outlined chip** â€” A bordered, transparent button with a typographic verb ("Save changes"). [`components/c1-outlined-chip.md`](components/c1-outlined-chip.md)
- **C2 Â· Inline form as cta** â€” The CTA *is* the form â€” a single email input with a "Submit â†’" beside it. No separate landing for sign-up. [`components/c2-inline-form-as-cta.md`](components/c2-inline-form-as-cta.md)
- **C3 Â· Typographic link** â€” Just a word, an arrow, and a 1-px underline. No box, no fill. [`components/c3-typographic-link.md`](components/c3-typographic-link.md)
- **C4 Â· Sticky bottom bar** â€” A horizontal bar pinned to the viewport bottom, holding a CTA + a brief reassurance line. [`components/c4-sticky-bottom-bar.md`](components/c4-sticky-bottom-bar.md)

### Testimonials / proof

- **T1 Â· Pull quote with marginalia** â€” A quote sits in the wide column; the attribution and source link float in the narrow margin column. [`components/t1-pull-quote-with-marginalia.md`](components/t1-pull-quote-with-marginalia.md)
- **T2 Â· Logo wall hairline** â€” A row of customer logos, monochromatic, separated by hairline rules. No card boxes, no shadows. [`components/t2-logo-wall-hairline.md`](components/t2-logo-wall-hairline.md)
- **T3 Â· Single huge quote** â€” One quote, set big, centered, taking a whole section. No supporting text, no attribution boxes â€” attribution is a small caps line beneath. [`components/t3-single-huge-quote.md`](components/t3-single-huge-quote.md)
- **T4 Â· Numbered stat strip** â€” A horizontal strip of 3â€“5 stats (count + qualifier) running across one row. Tabular nums. [`components/t4-numbered-stat-strip.md`](components/t4-numbered-stat-strip.md)

### Footers

- **Ft1 Â· Mast headed** â€” A wordmark and tagline anchor a single horizontal band. Two or three small links beside, address or licence below. [`components/ft1-mast-headed.md`](components/ft1-mast-headed.md)
- **Ft2 Â· Inline rule single line** â€” A single horizontal line of credits, address, copyright. Hairline rule above. No columns. [`components/ft2-inline-rule-single-line.md`](components/ft2-inline-rule-single-line.md)
- **Ft3 Â· Index style category list** â€” Three or four short columns, each headed by a category in small caps, holding 4â€“6 links each. [`components/ft3-index-style-category-list.md`](components/ft3-index-style-category-list.md)
- **Ft4 Â· Dense typographic** â€” One large block of text â€” credits, references, licence, address â€” in a small monospace font, fully justified or ragged-right. Editorial colophon energy. [`components/ft4-dense-typographic.md`](components/ft4-dense-typographic.md)
- **Ft5 Â· Statement** â€” One large display sentence dominates the footer â€” a closing line, not a sitemap. Wordmark, minimal links, copyright sit beneath in muted small type. Stripe (older), Mailchimp pre-r [`components/ft5-statement.md`](components/ft5-statement.md)
- **Ft6 Â· Letter close** â€” Closes the page like a letter â€” `Yours, the team. 2026.` Optional postscript line beneath. Sets the page as a piece of writing rather than a product. [`components/ft6-letter-close.md`](components/ft6-letter-close.md)
- **Ft7 Â· Newsletter first** â€” The form (label + input + submit) is the *primary* element of the footer; everything else (wordmark, links, copyright) is set in 12 px muted type beneath. Stratechery, Substack-sha [`components/ft7-newsletter-first.md`](components/ft7-newsletter-first.md)
- **Ft8 Â· Marquee scroll** â€” A horizontal infinite-scroll line of repeating tagline + dot separator: `STUDIO Â· 2026 Â· STUDIO Â· 2026 Â· STUDIO Â· 2026 Â·`. Sport-genre sites, fashion lookbooks, brand-forward agenc [`components/ft8-marquee-scroll.md`](components/ft8-marquee-scroll.md)

### Navigation

- **N1 (N1a) Â· Wordmark 2 links** â€” Top-of-page bar: wordmark on the left, two text links on the right ("Pricing" / "Sign in"). No logo image, no menu icon. The *minimal* variant â€” for the dense canonical SaaS bar use **N1b**. [`components/n1-wordmark-2-links.md`](components/n1-wordmark-2-links.md)
- **N2 Â· Floating chip** â€” A small fixed chip in a corner â€” wordmark + a single action ("Try it"). Doesn't sit in document flow. [`components/n2-floating-chip.md`](components/n2-floating-chip.md)
- **N3 Â· Side rail** â€” A thin vertical strip on the left edge â€” wordmark rotated, plus 2â€“3 dot-indicators for sections. Editorial / portfolio energy. [`components/n3-side-rail.md`](components/n3-side-rail.md)
- **N4 Â· Hidden behind k** â€” No visible nav. The user opens a command palette via `âŒ˜K` to get anywhere. Designed for keyboard-first audiences. [`components/n4-hidden-behind-k.md`](components/n4-hidden-behind-k.md)
- **N5 Â· Floating pill** â€” A rounded full-pill nav, *visibly detached* from the page edges, sitting ~`var(--space-md)` from the top, soft blur backdrop, soft shadow. Reads as contemporary modern-minimal â€” Ve [`components/n5-floating-pill.md`](components/n5-floating-pill.md)
- **N6 Â· Newspaper masthead** â€” Full-width header, large centred wordmark on the top row, thin issue/date line above or below in serif small caps, optional inline link row beneath, double-rule below the whole thi [`components/n6-newspaper-masthead.md`](components/n6-newspaper-masthead.md)
- **N7 Â· Brutal slab** â€” A heavy, full-width nav with a 2 px solid border-bottom, all-caps wordmark and tracked uppercase link row, dense rhythm, no shadow, no rounded corners. Reads as Pentagram project p [`components/n7-brutal-slab.md`](components/n7-brutal-slab.md)
- **N8 Â· Terminal command** â€” A nav formatted as a CLI prompt: `> studio --catalog --voice --getâ–®`. The "links" are command flags. The blinking cursor (`â–®`) is allowed *only here* (it has purpose â€” signals "you [`components/n8-terminal-command.md`](components/n8-terminal-command.md)
- **N9 Â· Edge aligned minimal** â€” Wordmark hard-left, single CTA hard-right, vast empty space between, no link row at all. The *absence* is the design â€” Apple product pages, Carl Hauser, luxury sites. [`components/n9-edge-aligned-minimal.md`](components/n9-edge-aligned-minimal.md)
- **N10 Â· Floating on scroll morph** â€” A sticky bar at the top that **morphs into a floating pill** as the user scrolls past a threshold. Two visual modes share one DOM â€” `.nav` (outer) owns the bar look, `.nav__inner`  [`components/n10-floating-on-scroll-morph.md`](components/n10-floating-on-scroll-morph.md)
- **N1b Â· Canonical SaaS three-section** â€” Wordmark-left Â· centred 4â€“6-link cluster (some with hover dropdowns) Â· sign-in + filled CTA right. The dominant modern marketing nav; frosts on scroll. N1/N1a is the *minimal* two-link variant; this is the dense, balanced one. [`components/n1b-saas-three-section.md`](components/n1b-saas-three-section.md)
- **N11 Â· Mega-menu panel** â€” Top bar whose triggers open a full-width multi-column panel (icon Â· title Â· description per item, grouped, + a feature card); page dims behind a scrim. For platforms/hubs with many grouped destinations. [`components/n11-mega-menu.md`](components/n11-mega-menu.md)
- **N12 Â· Announcement banner + retracting nav** â€” A coloured promo banner stacked above one real nav; banner retracts on scroll-down, returns on scroll-up, dismisses via Ã—. Banner â‰  second nav (colour contrast keeps them distinct). [`components/n12-banner-retract.md`](components/n12-banner-retract.md)
- **N13 Â· Inline âŒ˜K search pill** â€” A visible search pill in the bar (placeholder + `âŒ˜K` hint) opening a spotlight modal with grouped, keyboard-navigable results. The *visible* opposite of N4. For search/docs-heavy products. [`components/n13-inline-cmdk-pill.md`](components/n13-inline-cmdk-pill.md)

---

## Within-archetype variation knobs

Picking an archetype is the first axis of variety. The second is *how you build it*. Two pages built with the same archetype should not be identical â€” each archetype below has 2â€“3 *variation knobs*. Pick one value per knob per output. This prevents "every Bento I build looks like the same Bento."

When you pick an archetype, **state the knob values you chose** in the macrostructure stamp comment, e.g.:

```css
/* Hallmark Â· macrostructure: Bento Grid Â· F1 Bento knobs: tiles=6, spans=irregular, accent=corner-only Â· ... */
```

| Archetype | Knob A | Knob B | Knob C |
| --- | --- | --- | --- |
| **H1 Marquee** | Display size: `xxl` (clamp 4â€“12rem) Â· `xl` (clamp 3â€“8rem) | Alignment: left-bias Â· centred Â· right-bias | Underlay: none Â· single rule above Â· single rule below |
| **H2 Split Diptych** | Ratio: 7/5 Â· 6/6 Â· 5/7 | Right side: photo Â· proof column Â· pull-quote | Divider: hairline Â· negative space Â· vertical rule |
| **H3 Quote-Led** | Quote weight: italic display Â· roman display Â· roman body large | Attribution position: under quote Â· margin-aligned Â· right-flush | Length: â‰¤80 chars Â· 80â€“160 chars |
| **H4 Stat-Led** | Number style: tabular display Â· italic display Â· monospace | Qualifier position: below Â· inline-right Â· stacked-above | Secondary stats: none Â· two below Â· row of four |
| **H5 Letter** | Salutation: greeting Â· "Dear X," Â· time-stamp | Body length: 1 paragraph Â· 2 paragraphs Â· 3 paragraphs | Signoff: typed name Â· drawn signature SVG Â· initials |
| **H6 Photographic** | Image area: full-bleed Â· 16/7 Â· 4/3 Â· 1/1 square | Caption position: lower-left Â· upper-right Â· margin | Text below or overlaid |
| **H7 Demo Video Clipped-Edge** | Clip side: right Â· left Â· both | Aspect ratio: 16/10 Â· 16/9 Â· 4/3 | Frame: hairline Â· browser chrome Â· none |
| **H8 Mockup Split** | Frame style: browser chrome Â· macOS toolbar Â· minimal hairline Â· floating no-frame | Tilt: 0Â° Â· 1.5Â° Â· 3Â° | Screenshot count: 1 Â· stack-of-3 Â· orbit-of-3 |
| **H9 Custom Illustration** | Build method: Tier-A pure-CSS Â· Tier-B hand-SVG Â· Tier-C generated Â· Tier-D library | Animation: none Â· loop Â· scroll-linked | Scale: small accent Â· dominant |
| **F1 Bento (feature)** | Tiles: 4 Â· 6 Â· 7 Â· 9 | Spans: regular Â· irregular Â· mosaic | Border: hairline all Â· accent corners Â· none |
| **F2 Sticky-scroll stack** | Pinned side: left Â· right | Right pane content: code Â· screenshot Â· diagram | Pin steps: 3 Â· 4 Â· 5 |
| **F3 Tabular spec sheet** | Columns: 2 (key/val) Â· 3 (key/val/unit) Â· 4 (with footnote) | Rule density: every row Â· groups of 3 Â· headers only | Numbers: tabular Â· proportional |
| **F4 Step sequence** | Numbering: I/II/III Â· 01/02/03 Â· 1.0/2.0/3.0 | Layout: vertical stack Â· horizontal flow Â· diagonal | Connector: line Â· arrow Â· none |
| **F5 Annotated screenshot** | Callouts: numbered pins Â· margin labels Â· inline arrows | Frame: device Â· plain Â· floating | Anchor: image-led or text-led |
| **F6 Product card grid** | Card ratio: 3/4 portrait Â· 1/1 square Â· 4/3 landscape | Density: 3-up Â· 4-up Â· 5-up | Micro-action: Add Â· Save Â· View â†’ Â· none |
| **C1 Outlined chip** | Shape: rectangular Â· pill (only allowed for tactile/playful tones) Â· slab | Density: spacious Â· compact | Adornment: arrow Â· plus Â· none |
| **C2 Inline form-as-CTA** | Field count: 1 Â· 2 Â· 3 | Submit position: end-of-row Â· separate line Â· embedded button | Helper: above Â· below Â· none |
| **C3 Typographic link CTA** | Underline: solid Â· dashed Â· double Â· none | Hover behaviour: thicken Â· slide Â· colour shift | Arrow: â†’ Â· â†— Â· none |
| **C4 Sticky bottom bar** | Reveal: always Â· scroll-up Â· after fold | Anchored: viewport bottom Â· viewport top Â· inline at bottom | Shadow: hairline Â· none Â· subtle |
| **T1 Pull quote w/ marginalia** | Quote treatment: italic display Â· roman large Â· serif italic | Attribution: signed Â· stamped Â· timestamped | Marginalia: none Â· timeline Â· 1 footnote |
| **T2 Logo wall (hairline)** | Layout: single row Â· 2 rows Â· grid 3Ã—N | Logo treatment: monochrome ink Â· brand colour Â· ghosted | Divider: hairline cells Â· none |
| **T3 Single huge quote** | Quote face: serif italic Â· roman display Â· italic mono | Width: full-bleed Â· 60ch Â· 40ch | Attribution position: same line Â· separate band |
| **T4 Numbered stat strip** | Layout: 3-up Â· 4-up Â· 5-up Â· 6-up | Number weight: display Â· body large | Qualifier position: under Â· inline Â· above |
| **Ft1 Mast-headed** | Wordmark size: display 3xl Â· display 2xl Â· xl | Tagline: italic serif Â· roman body Â· none | Links row: inline Â· 2-line stack |
| **Ft2 Inline single line** | Order: wordmark/links/credit Â· credit/wordmark/links | Separator: middot Â· pipe Â· em-dash Â· vertical rule | Density: dense Â· spaced |
| **Ft3 Index columns** | Columns: 3 Â· 4 Â· 5 | Heading style: small caps Â· italic Â· monospace | Bullet: hairline Â· none |
| **Ft4 Dense colophon** | Family: monospace Â· serif Â· sans | Layout: single block Â· paragraphs Â· log-style | Includes: build hash Â· date Â· attribution |
| **N1 Wordmark + 2 links** | Position: left/right split Â· centred Â· right-flush | Links: text Â· text+icon Â· pill | Sticky: yes Â· no |
| **N2 Floating chip** | Anchor: top Â· bottom Â· top-right Â· bottom-left | Content: theme picker Â· search Â· navigation | Backdrop: blur Â· solid Â· none |
| **N3 Side-rail** | Side: left Â· right | Width: 12ch Â· 16ch Â· 20ch | Indicator: filled bar Â· text-only Â· numbered |
| **N4 Hidden behind âŒ˜K** | Trigger: button Â· keyboard only Â· both | Surface: modal Â· sheet Â· spotlight | Recents: shown Â· hidden |
| **N5 Floating pill** | Width: content-sized Â· max ~720 px Â· max ~560 px | Backdrop: blur+saturate Â· solid Â· subtle gradient | Anchor: top-centred Â· top-right Â· top-left |
| **N6 Newspaper masthead** | Issue line: above wordmark Â· below wordmark Â· none | Wordmark size: 3xl Â· 2xl Â· xl | Rule: double Â· single Â· none |
| **N7 Brutal slab** | Border weight: 2 px Â· 3 px Â· 4 px | Letter-spacing: tracked uppercase Â· normal | CTA: filled slab Â· outline block Â· text-only |
| **N8 Terminal command** | Prompt: `>` Â· `$` Â· `~/$` | Cursor: in-line at end Â· after final flag Â· none | Width: full bleed Â· content Â· ~80 ch |
| **N9 Edge-aligned minimal** | CTA shape: outlined Â· filled pill Â· text+arrow | Wordmark: serif italic Â· sans Â· monospace | Padding-block: tight Â· default Â· spacious |
| **N1b SaaS three-section** | Centre links: 3 Â· 4 Â· 5â€“6 | Dropdowns: none Â· 1 Â· 2 | Scroll: frost-on-scroll Â· always-solid Â· transparent-fixed |
| **N11 Mega-menu** | Columns: 2 Â· 3 Â· 4 | Feature cell: none Â· promo card Â· code sample | Scrim: dim+blur Â· dim only Â· none |
| **N12 Banner + retract** | Banner fill: solid Â· gradient Â· tint+ink | Dismiss: yes Â· none | Bar scroll: sticky Â· also-frosts |
| **N13 Inline âŒ˜K-pill** | Pill placement: centred Â· right-of-brand | Result groups: flat Â· grouped | Footer hints: shown Â· hidden |
| **Ft5 Statement** | Sentence width: 28 ch Â· 38 ch Â· 50 ch | Wordmark position: under sentence Â· top-right Â· none | Rule above meta: hairline Â· double Â· none |
| **Ft6 Letter close** | Signoff: italic Â· roman Â· monogram | Postscript: yes Â· no | Width: 40 ch Â· 60 ch Â· 80 ch |
| **Ft7 Newsletter-first** | Layout: stacked Â· inline Â· split (form left Â· meta right) | Submit style: filled Â· outline Â· arrow link | Privacy line: yes Â· no |
| **Ft8 Marquee scroll** | Speed: 24 s Â· 32 s Â· 48 s | Direction: left Â· right Â· alternate (rare) | Glyph: middot Â· em-dash Â· slash |

**Anti-pattern:** picking the same knob values across two different outputs is the same kind of templating as picking the same archetype. If your last Bento was `tiles=6, spans=irregular, accent=corner-only`, the next one must change at least one knob.

---


## Routing â€” which footer fits which genre

| Genre | Default | Also OK |
| --- | --- | --- |
| editorial | **Ft1 Mast-headed** | Ft2, Ft4, Ft6, Ft7 |
| modern-minimal | **Ft2 Inline single line** | Ft1, Ft5 |
| atmospheric | **Ft5 Statement** | Ft1, Ft2 |
| playful | **Ft8 Marquee scroll** | Ft5, Ft3 |
| terminal | **Ft4 Dense colophon** | Ft2 |
| docs / reference | **Ft3 Index columns** | Ft1 |

**Diversification.** Same rule as nav â€” across consecutive Hallmark runs in the same session, no two outputs should share the same footer archetype.

**Default away from Ft3.** The 4-column index footer is the AI fingerprint when used reflexively (Product Â· Company Â· Resources Â· Legal + social row + tiny copyright). Reach for Ft3 only when the page is a hub or docs-root with a genuine sitemap; default to Ft1, Ft2, Ft4, Ft5, Ft6, Ft7, or Ft8 otherwise.

---


## Routing â€” which nav fits which genre / theme

| Genre / cluster | Default nav | Acceptable also |
| --- | --- | --- |
| editorial (Newsprint Â· Garden Â· Atelier Â· Carnival Â· â€¦) | **N6 Masthead** | N1a, N9, N12 |
| modern-minimal (Coral Â· Cobalt) | **N1b SaaS three-section** | N5, N11, N13, N9 |
| atmospheric (Bloom Â· Aurora Â· Midnight Â· Lumen) | **N5 Floating pill** (blur backdrop sells the mood) | N9, N4, N13, N1b |
| playful (Hum) | **N1b SaaS three-section** | N5, N11, N12, N13, N7 (rounded) |
| terminal / CLI (Terminal) | **N8 Terminal command** | N4 âŒ˜K-only, N13 |
| docs / reference (Almanac) | **N3 Side-rail** | N13, N1a, N4 |
| commerce / product launch | **N12 Banner + retract** | N1b, N11, N9 |

**Diversification â€” state it out loud, every build.** Across consecutive Hallmark runs in the same project session (and across multiple test builds of the *same theme*), no two outputs may share the same nav archetype. Before writing nav markup, write one line: *"Previous nav: <X>. This build: <Y>, because <reason>."* This is the same accountability step as the macrostructure rotation. **A theme with 4 test builds should show 4 different navs** â€” e.g. Hum across Curio/Sprout/Tally/Mixtape uses N5 â†’ N1b â†’ N12 â†’ N13. Reaching for the genre *default* on every build is exactly the failure this rule exists to prevent; rotate through the "Acceptable also" column deliberately.

**Default away from N1a.** The most-recognised AI fingerprint is N1a (wordmark + inline link row + button-right) used reflexively. For a real product nav reach for **N1b** (the dense, balanced canonical bar) or N5/N11/N13 first; reach for N1a only when the page genuinely has 2 destinations.

---


## Picking from this file

When building a section:

1. Identify the section's role (hero / section-head / feature / CTA / testimonial / footer / navigation).
2. Glance at the archetypes in that category.
3. Pick the one whose "Use when" fits the brief.
4. Make sure no two sections in the same page use the same archetype.
5. If the macrostructure suggests a default (e.g., Bento Grid â†’ F1 Bento), use it; if it doesn't suggest, vary deliberately.

The goal is composed variety â€” within a page, sections feel different from each other; across pages Hallmark builds, sections feel different from the last.

---


## Mobile collapse â€” per archetype

Every archetype has a defined collapse behaviour at narrow viewports. The two breakpoints to know:

- **60 rem (~960 px)** â€” the *layout* breakpoint. Multi-column grids collapse to single column. Tilts and clip effects drop. Sticky panes unstick.
- **40 rem (~640 px)** â€” the *typography* breakpoint. Display sizes shrink one step. Side-margin labels move inline. Annotations consolidate.

Below 60 rem the archetype must still feel like itself â€” same hierarchy, same tone, same rhythm â€” but in a stacked single-column form. Below 40 rem the page is a phone; treat space like a luxury.

| Archetype | Below 60 rem | Below 40 rem |
| --- | --- | --- |
| **H1 Marquee** | unchanged (typography-only; centres / left-biases naturally) | display size step down (`xl` â†’ `lg`); reduce side padding |
| **H2 Split Diptych** | grid `1fr` (text top, proof column below); divider becomes hairline-rule between | proof column collapses to a 2-column compact grid for items |
| **H3 Quote-Led** | quote stays full width; attribution wraps to its own line | quote size step down; attribution font-size step down |
| **H4 Stat-Led** | number stays full width, text stacks below; secondary stats become 2-up grid | number size step down (`clamp` floor lifts); qualifier text wraps |
| **H5 Letter** | unchanged single column; aside (if present) moves below body, divider becomes top border | salutation size step down; signoff tightens |
| **H6 Photographic** | image stays full-bleed; caption moves from absolute corner to inline below image | caption font-size step down; corner caption never overlaps text on phones |
| **H7 Demo Video Clipped-Edge** | **drops the clip**; goes `1fr` stacked, full-width media; tilt removed (clipping at 375 px reads as broken) | media reduces to 16/9; poster image used (auto-playing on cellular is hostile) |
| **H8 Mockup Split** | drops the tilt; grid `1fr`; mockup goes full-width below text | annotation pins consolidate; numbered legend moves below mockup |
| **H9 Custom Illustration** | grid `1fr`; illustration moves below text (or above â€” pick by tone) | illustration scales to â‰¤ 40 % viewport width; never dominates |
| **F1 Bento** | grid drops from 6/4-col to 2-col; large tiles span 2; small tiles span 1 | drops to 1-col; tile order respects information priority |
| **F2 Sticky-scroll stack** | sticky pane unsticks; content becomes linear sequence of paired text+visual blocks | the visuals shrink to 16/9 inline; no sticky behaviour at all |
| **F3 Tabular spec sheet** | columns reduce: 4-col â†’ 2 (key + value), drop unit + footnote | spec list goes vertical; each row is `dt` above `dd` |
| **F4 Step sequence** | numbering moves from left margin to inline-with-step | step containers tighten; connector lines drop |
| **F5 Annotated screenshot** | screenshot full-width; annotations restack as a numbered list below | screenshot 16/9; annotations consolidate into a legend |
| **F6 Product card grid** | grid 3-up â†’ 2-up | grid 2-up â†’ 1-up; card height becomes flexible |
| **C1 Outlined chip** | unchanged (chips wrap onto multiple lines if needed) | full-width single chip ; min-height 44 px hit target |
| **C2 Inline form-as-CTA** | input + button stack vertically; full-width | label moves above input; button is full-width below |
| **C3 Typographic link** | unchanged (links wrap naturally) | unchanged |
| **C4 Sticky bottom bar** | unchanged (already designed for narrow); ensure 44 px min-height | label truncates if needed; CTA stays right-aligned |
| **T1 Pull quote w/ marginalia** | marginalia move below quote; divider becomes hairline | marginalia consolidate into a single line |
| **T2 Logo wall** | grid 6-up â†’ 3-up | grid 3-up â†’ 2-up; logo height step down (32 px â†’ 24 px) |
| **T3 Single huge quote** | quote remains full width; attribution wraps below | quote size step down by 1.4Ã— |
| **T4 Numbered stat strip** | strip 4-up â†’ 2-up | strip becomes vertical; 1 stat per row |
| **Ft1 Mast-headed** | links wrap to two lines; tagline below wordmark | wordmark size step down; tagline italicises in if not already |
| **Ft2 Inline single line** | links wrap to multiple lines; separator becomes a soft return | becomes a vertical list |
| **Ft3 Index columns** | grid 4-col â†’ 2-col | grid 2-col â†’ 1-col; column heads remain |
| **Ft4 Dense colophon** | unchanged (mono/wraps naturally); reduce padding | font-size step down |
| **Ft5 Statement** | sentence stays full width; meta row stacks | sentence size step down (clamp floor lifts); meta wraps |
| **Ft6 Letter close** | unchanged single column; postscript wraps | signoff size step down; postscript italicises if not already |
| **Ft7 Newsletter-first** | input + button stack vertically; full-width | label moves above input; button is full-width below |
| **Ft8 Marquee scroll** | unchanged (already designed for narrow); slow speed by ~25 % | speed slows further; track height step down |
| **N1 Wordmark + 2 links** | unchanged | links wrap to second line if long; wordmark stays |
| **N2 Floating chip** | chip remains floating; reduce padding | chip widens to support 44 px hit target; never below 280 px |
| **N3 Side-rail** | rail unsticks and becomes a hamburger trigger above | hamburger becomes the only nav |
| **N4 âŒ˜K-only** | hamburger appears for users who don't know âŒ˜K | unchanged (âŒ˜K equivalent is on-screen tap) |
| **N5 Floating pill** | pill drops link list, keeps wordmark + CTA; stays detached | becomes a top-anchored corner chip â€” wordmark left, hamburger right |
| **N6 Newspaper masthead** | issue line stacks above wordmark; nav links wrap to a second row | wordmark size step down; nav row collapses behind a "menu" disclosure |
| **N7 Brutal slab** | links wrap to second line; CTA stays right-aligned | links collapse to hamburger; wordmark + hamburger only |
| **N8 Terminal command** | flags wrap to a second `>` line if needed; cursor stays at the end | becomes a single hamburger labelled `> menu`; cursor visible at line end |
| **N9 Edge-aligned minimal** | unchanged (already designed for breathing room) | wordmark + CTA stay edge-aligned; CTA pads to 44 px hit target |

**Cross-cutting rules:**

- All hit targets â‰¥ 44 Ã— 44 px below 40 rem (WCAG AA). Never below.
- Padding-inline â‰¥ `clamp(1rem, 4vw, 1.5rem)` on the page container so content doesn't kiss the screen edge.
- Disable any scroll-linked animation below 40 rem (mobile scroll has its own physics; layered animations fight it).
- Image `loading="lazy"` always below the fold; **never on the LCP element regardless of viewport.**
- Auto-play video respects `data-saver` (`navigator.connection.saveData`) â€” replaces with poster when set.


