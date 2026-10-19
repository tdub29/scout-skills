# Visual format library (naming, classifying, building)

`meta-creative-formats.md` answers **which format to make next** (tiered by funnel role). This file
answers the two questions that come after: **what format is this ad** (classify) and **how do I
build one correctly** (execute). It indexes an external, practitioner-maintained library rather than
copying it.

Source: [alyshadotmd/visual-formats](https://github.com/alyshadotmd/visual-formats) (75 documented
formats, ~490 tagged in-market example ads, rechecked at upstream commit `ce9991a`, 2026-10-10). **No license is published**, so
treat it as read-only reference: link to it, study it, never copy its SOP text or example media into
a deliverable or this repo.

## How to use it

- **Classifying or naming an existing ad:** open `formats/<token>/classify.md`. Each one states the
  identifying property and the near-miss formats it is not.
- **Ideating, scripting or briefing a new ad:** open `formats/<token>/execute.md`. Each one gives
  anatomy, build rules in priority order, and the one property to protect.
- **Calibrating:** find real examples by filename token, e.g. every file containing `vf=greenscreen`
  in the single `files/` folder (evergreen and BFCM were merged on 2026-10-09; the season is now the
  `s=` token, not a subfolder). `files/_index.md` holds the naming rules and per-ad tag notes. Study,
  do not copy.
- **Start from the best examples:** files tagged `_tag=favorite` (6 at last check) carry a same-name
  `.md` beside them with source, transcript and a creative breakdown. Read those first.

URL pattern: `https://github.com/alyshadotmd/visual-formats/tree/main/formats/<token>`

## Naming convention worth adopting

Their example files carry a machine-readable creative name. Use the same shape when naming ads in a
batch (it makes performance roll-ups by format trivial):

```
[b=<brand>][_c=<creator>]_s=<evergreen|bfcm>_vf=<anchor-format>[_vf=<secondary>]_ot=<offer-type>[_ot=<offer-2>][_tag=favorite][_n=<k>]
```

- At least one of `b=` or `c=`: brand ad = `b=` only; brand x creator partnership = both, brand
  first; organic creator post with no brand = `c=` only.
- `_n=2`, `_n=3` only on a true name collision, in the order added. Dedupe by md5 first: an exact
  byte match is a duplicate, not a collision.

- `vf=` is the format token from the index below. Up to two, **anchor first** (the format that
  carries the ad), secondary second (a device layered inside it).
- `ot=` offer type: `amount-off`, `free-gift`, `bundle`, `tiered`, `buy-x-get-y`, `other`, `none`.
- `_` separates fields, `-` joins words inside a value, `=` (not `:`) so names are legal filenames.

## Anchor vs. secondary, device vs. structure

The library's most reusable idea: a format is either a **structure** (how the content is organized),
a **device** (the visual wrapper it wears) or an **anchor** (the video spine everything else rides).
They stack. Examples:

- `listicle` is a structure; `notes-app` is a device. A list of tips in Apple Notes is `vf=notes-app_vf=listicle`.
- `greenscreen`, `graphic-anchor`, `high-production-edit` are anchors; `unboxing` or `listicle` ride on them.
- `product-animation` is motion with no layout of its own; it pairs with `offer-banner` or `product-grid`.
- `found-footage` (doorbell, dashcam) is a frame; another format plays inside it.

## Boundaries that trip people up

| Looks like | Is actually | Deciding property |
|---|---|---|
| product-grid / bento-grid / collage | depends on tiles | Only flat product shots = product-grid. Aligned tiles with at least one lifestyle/in-use/macro tile = bento-grid. Loose cut-outs with no boxes = collage |
| review / testimonial | depends on arc | One pulled quote or star cards = review. One person narrating struggle, turn, result = testimonial |
| before-and-after / transformation | depends on match | Same subject, matched before and after frames = before-and-after. A problem-to-result sequence without a matched pair = transformation |
| feature-benefit-callout / -pointout | arrows | Features listed beside the product = callout. Lines pointing at specific parts = pointout |
| flatlay / shelfie | angle | Overhead arrangement = flatlay. Front-on styled shelf = shelfie |
| ad-in-the-wild / flyer | scale | Paid out-of-home surface composited into a scene = ad-in-the-wild. A taped-up printed sheet = flyer |
| matching-chart / flowchart / listicle | logic | Self-select lookup table = matching-chart. Branching yes/no = flowchart. Ordered items = listicle |
| statistic / line-chart / text-echo | hero | One big proof number = statistic. A plotted trend = line-chart. A repeated phrase in huge type = text-echo |
| ugc / yapper / testimonial / egc / founder | who and how | Founder tells origin story = founder. Employee speaks for brand = egc. Fast monologue, no evidence = yapper. Journey story = testimonial. Anything else creator-style = ugc |
| comment-response / comment-screenshot | medium | Question sticker answered on camera or as overlay = comment-response. A screenshotted comment as the static hero = comment-screenshot |

## Format index

Token, then a short gloss in our words. Tier hints point at `meta-creative-formats.md` where that
taxonomy ranks the same idea; no hint means it is not ranked there yet.

**Statics: layout and proof**
- `bento-grid`: aligned tile mix with at least one non-product tile (see Grid-style statics, A-tier)
- `product-grid`: product-only lineup (Grid-style statics, A-tier)
- `collage`: loose cut-outs, moodboard feel
- `flatlay`: overhead styled arrangement
- `shelfie`: products on a styled shelf, front-on
- `offer-banner`: the offer is the hero; default BFCM static
- `statistic`: one or a few huge proof numbers
- `line-chart`: plotted trend as proof of mechanism or result
- `case-study`: clinical-proof framing with multiple result stats and a method footnote
- `before-and-after`: matched pair of the same subject
- `us-vs-them`: two-column brand vs. old way, 4 to 7 rows
- `feature-benefit-callout`: features listed beside the product
- `feature-benefit-pointout`: lines pointing at product parts, each turned into a benefit
- `matching-chart`: self-select row to recommended variant
- `flowchart`: yes/no decision tree ending in a product
- `venn-diagram`: product sits in the overlap
- `listicle`: 2+ discrete items, one frame or carousel
- `review`: quote or star cards, skimmable
- `press`: pull-quote, logos or awards (F-tier as press ads; never credit a real outlet falsely)
- `letter`: chunky text block under one hook headline, often founder-signed (founder content, S-tier)
- `faq`: customer question as headline, short answer beside product
- `text-echo`: one phrase repeated in stacked type

**Statics: native-UI and found-object devices**
- `notes-app`: Apple Notes card (F-tier as fake-native)
- `text-message`: iMessage thread carrying the pitch
- `comment-screenshot`: a real-looking social comment as hero
- `web-search`: search bar sets up the product as the answer
- `toggle`: iOS switch, brand option on
- `cart-screenshot`: checkout page with the discount showing
- `receipt`: receipt, ticket or coupon carrying the deal
- `post-it`: one handwritten sticky thought over an image
- `handwritten`: whole layout drawn by hand around a product photo
- `sign`: person holding a handmade sign in a real scene
- `whiteboard`: marker argument on a real whiteboard
- `annotation`: printed copy being highlighted as it is read
- `fortune-cookie`: message on a fortune slip
- `unexpected-text-placement`: words on a surprising surface (skin, sidewalk, cake)
- `flyer`: printed sheet taped up in an everyday space
- `ad-in-the-wild`: creative composited onto a billboard or transit placement
- `meme`: known meme template or meme style
- `news`: breaking-news banner styling
- `doodle`: original line-drawn character or scene

**Video: people on camera**
- `founder`: origin and problem story only the founder can tell (S-tier)
- `egc`: an employee speaking for the brand
- `yapper`: fast talking-head monologue (Yapper ads, A-tier)
- `testimonial`: one person's full journey
- `explainer`: confident expert or everyday person teaching something
- `interview`: interviewer asks, people answer
- `street-interview`: strangers stopped in public
- `podcast`: podcast-set styling (F-tier unless a known show)
- `comment-response`: answering a question sticker on camera
- `skit`: scripted multi-character scene, often wrong-self vs. right-self split
- `challenge`: live contest or stunt with a rule; payoff is often the discount
- `taste-test`: consumption plus immediate reaction
- `live-demo`: cause the problem on camera, product visibly fixes it
- `live-selling`: mimics a live-shopping stream with comment bubbles
- `point-to-screen`: phone films a screen while a hand points through it
- `ugc`: fallback for creator-style clips that match nothing more specific
- `ugc-mashup`: several creators stitched together
- `signature-series`: a creator's own recurring bit, one more episode, product written in (emerging)

**Video: edit-led and anchors**
- `greenscreen`: creator over a relevant full-frame background; hook opens on it (Green-screen commentary, A-tier)
- `graphic-anchor`: creator holds the frame while graphics pop in beat by beat
- `high-production-edit`: fast VO-driven edit where every beat gets its own visual payoff
- `b-roll-overlay`: b-roll plus text, no VO, no talking head
- `instagram-text-overlay`: native IG story text over a selfie or POV shot
- `split-screen`: fixed offer or product panel beside live footage
- `transformation`: problem, product, result in sequence
- `behind-the-scenes`: how it is made, with founder or chemist VO
- `unboxing`: packaging reveal, usually talked through; pairs as a secondary
- `asmr`: sound-led tactile product audio
- `text-alert`: notification drops into a moment, tap cuts to product
- `found-footage`: seen through a doorbell, dashcam or monitor frame
- `product-animation`: motion graphics only, no live action
- `stop-motion`: frame-by-frame objects
- `ai-animation`: fully generated animated narrative, often a mascot
- `swatch-picker`: cursor clicks swatches, product photo swaps color

Upstream also lists stub folders without docs yet (ai-chat, demo, how-to, nostalgia, reaction,
stitch, time-lapse, trend, vsl). VSL is already covered here as S-tier in `meta-creative-formats.md`.
