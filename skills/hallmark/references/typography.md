# Typography

Type carries the design. If the type is wrong, nothing else matters.

## Principles

- A page is a pairing, not a single font. Display face + body face, minimum. *Single-font pages are allowed only when the single font IS the design choice* â€” a true terminal aesthetic is monospace-everywhere on purpose; a Manifesto poster might be one display face on purpose. The default is a pairing.
- Commit to extremes. Weight 200 next to weight 800 reads as intentional. Weight 400 next to weight 600 reads as a default setting.
- Size steps should be ratios, not increments. Major third (1.25), perfect fourth (1.333), perfect fifth (1.5), or golden (1.618). Pick one and use it.
- Line-height changes with size. Tight for display (1.05â€“1.2), comfortable for body (1.5â€“1.65).
- Measure â€” line length â€” lives between 45 and 75 characters. Use `max-width: 65ch` as the default.

## The 2+1 rule â€” three faces is the ceiling

**A page may use at most three distinct font families.** One **display**, one **body**, and an optional **outlier** for a single typographic moment â€” wordmark, hero stat, pull quote, masthead â€” where the page wants exactly one note that doesn't sound like the rest. Four families is slop. Two is canonical. Three is the ceiling, used sparingly.

The pattern:

```css
:root {
  --font-display:  "Fraunces", ui-serif, Georgia, serif;       /* headings, hero */
  --font-body:     "Geist", ui-sans-serif, system-ui, sans;    /* prose, UI */
  --font-outlier:  "Geist Mono", ui-monospace, monospace;      /* wordmark + hero stat ONLY */
}
```

The outlier is a *register*, not a third surface. Rules:

- **Outlier appears in â‰¤ 2 places** on the whole page. Wordmark + hero stat. Or pull quote + masthead. Two slots, not five. If you find yourself reaching for it a third time, you don't have an outlier â€” you have a third body font, which is slop.
- **The outlier carries one role.** It tags a specific kind of content (the brand, the headline figure, the manifesto line). Once you know what it tags, every instance of that role uses it. Don't apply it to one button label and not another.
- **Mono counts as a face.** A page with Fraunces display, Geist body, and Geist Mono in code blocks is using three families. That's fine â€” code is the outlier role. Don't sneak in a fourth.
- **Same family at different weights is one family**, not two. Geist 400 + Geist 700 is one font; pairing it with Fraunces is two. Adding Geist Mono on top is three.

Two families is still the right answer for most pages. Three is for SaaS / brand-heavy / editorial-rich pages where the wordmark needs a different register than the body.

## Banned defaults

These fonts are on-distribution for every LLM. Do not reach for them without a deliberate reason:

- **Sans-serif:** Inter, Roboto, Open Sans, Lato, Poppins, Source Sans, Nunito, Montserrat, Raleway, Work Sans, DM Sans, system-ui, Arial, Helvetica.
- **Serif:** Merriweather, Playfair Display (as body â€” banned as overused body serif; ok as display in moderation), Lora, Source Serif, Georgia-as-default.
- **Mono:** Courier New, Consolas-as-default, system mono.

If the user insists on one, do it. Otherwise pick from the allowlist below.

## The font catalog

Three sources, in priority order:

- **Google Fonts** â€” free, served via CDN, works everywhere. The default source.
- **Fontshare** (Indian Type Foundry) â€” free for commercial use, foundry-grade. The "you didn't know these were free" tier. Drop-in via `<link href="https://api.fontshare.com/v2/css?f=...">`.
- **Foundry-licensed** â€” Klim, Pangram Pangram, Production Type, Lineto, Colophon. Only when the user has confirmed they're licensed.

### Free display faces

| Family | Source | Voice | Best for |
| --- | --- | --- | --- |
| **Fraunces** | Google | Variable serif, deeply expressive italic, optical-size axis | Editorial, Atelier, brand-heavy |
| **Newsreader** | Google | Roman serif with optical-size + italic | Editorial, magazine, long-form |
| **Instrument Serif** | Google | Tight contrast, italic available, smart for short heads | Brand, atelier, intimate editorial |
| **Cormorant Garamond** | Google | Classical, high contrast, luxury register | Luxury, fashion, fine arts |
| **EB Garamond** | Google | Honest classical Garamond, body-grade | Editorial body, longform reading |
| **Cardo** | Google | Scholarly serif, generous x-height | Reference, academic, slow reading |
| **Source Serif 4** | Google | Modern transitional, big OT family | SaaS marketing with serif tone |
| **DM Serif Display** | Google | Bracketed serif, high-contrast display | Headlines that need to feel printed |
| **Bodoni Moda** | Google | Modern Bodoni revival, dramatic | Fashion, editorial, luxury display |
| **Playfair Display** | Google | Use only as display; banned as body | Marketing display moments â€” sparingly |
| **Geist** | Google | Modern grotesque, geometric, 7 weights | Modern minimal, SaaS, dev tools |
| **Inter Tight** | Google | Tighter Inter â€” allowed *only* as a body fallback in technical themes; never as display | UI body in restrained themes |
| **Bricolage Grotesque** | Google | Variable display sans, bold weights, condensable | Brutal, playful, riso-bold |
| **Space Grotesk** | Google | Geometric grotesque, slightly quirky | Brutalist, technical |
| **Anton** | Google | Heavy condensed grotesque | Posters, manifestos |
| **Big Shoulders Display** | Google | Industrial condensed | Sports, manifestos, declarative |
| **Tomorrow** | Google | Variable optical condensed | Tech, atmospheric, near-future |
| **Outfit** | Google | Modern geometric (banned as default; use only when *picked* deliberately) | Restrained tech â€” sparingly |
| **General Sans** | Fontshare | Modern grotesque, Geist-adjacent | Modern minimal alternative to Geist |
| **Switzer** | Fontshare | Neutral sans, broad weight range | SaaS body, restrained |
| **Cabinet Grotesk** | Fontshare | Display grotesque, 9 weights | Editorial display, magazine |
| **Clash Display** | Fontshare | Ultra-condensed display | Posters, brand moments |
| **Satoshi** | Fontshare | Playful geometric sans | Playful, consumer |
| **Sentient** | Fontshare | Variable serif, soft contrast | Soft editorial, atmospheric |
| **Erode** | Fontshare | Distressed serif, hand-set feel | Riso, tactile-rebellion, brand-y |
| **Tanker** | Fontshare | Heavy condensed grotesque, pure display | One-word posters, mastheads |

### Free body faces

| Family | Source | Voice | Best for |
| --- | --- | --- | --- |
| **Geist** | Google | The default modern body sans | Modern minimal, SaaS, atmospheric |
| **The Future** | (in repo) | Hallmark's own body workhorse | Default Hallmark tone |
| **Newsreader** | Google | Reading serif, optical-size aware | Editorial body, longform |
| **Source Serif 4** | Google | Body-grade serif | Editorial mid-weight |
| **EB Garamond** | Google | Classical body | Editorial slow reading |
| **Spectral** | Google | Slab-ish serif, screen-tuned | Long-form on screen |
| **Lora** | Google | Calligraphic serif, body-grade | Body â€” sparingly (over-used) |
| **Crimson Pro** | Google | Old-style body, generous | Editorial slow body |
| **IBM Plex Sans** | Google | Engineering sans, broad family | Technical body |
| **Switzer** | Fontshare | Neutral sans body | SaaS body, restrained |
| **General Sans** | Fontshare | Geist-adjacent body | Modern minimal body |

### Free mono / outlier faces

| Family | Source | Voice | Best for |
| --- | --- | --- | --- |
| **Geist Mono** | Google | Geist's mono companion | Default Hallmark mono, code, captions |
| **JetBrains Mono** | Google | Engineering mono, ligatures | Code, terminal, technical |
| **IBM Plex Mono** | Google | Engineering mono, broad family | Technical body-grade |
| **Commit Mono** | Google | Tighter mono, modern | Code, modern terminal |
| **Space Mono** | Google | Quirky, slightly retro | Playful tech, riso |

### Tone-based pairing patterns

Each tone gets two rows: a **free baseline** (Google Fonts / Fontshare; works out of the box) and a **paid upgrade** (foundry licences required; only when the user has confirmed the budget and the licence). The free row is the default. **Never name a paid font in code without confirming the user is licensed** â€” the demo will fall back to system-default and look broken to the user.

| Tone | Tier | Display | Body | Outlier |
| --- | --- | --- | --- | --- |
| **Editorial** | Free | Fraunces Â· Newsreader Â· EB Garamond Â· Instrument Serif Â· Cabinet Grotesk | IBM Plex Sans Â· Switzer Â· Source Serif 4 | JetBrains Mono Â· Geist Mono Â· Erode (display moment) |
| | *Paid* | *Tiempos Headline Â· SÃ¶hne Breit Â· Reckless Display Â· Migra Â· Tobias* | *SÃ¶hne Â· Haffer Â· Untitled Sans* | *SÃ¶hne Mono Â· GT America Mono* |
| **Technical** | Free | JetBrains Mono Â· Geist Mono Â· Geist (700) Â· Commit Mono | Geist Â· IBM Plex Sans Â· Switzer | Tomorrow Â· Cabinet Grotesk (wordmark) |
| | *Paid* | *Berkeley Mono Â· SÃ¶hne Mono Â· GT Pressura Â· ABC Diatype Mono* | *SÃ¶hne Â· Untitled Sans Â· ABC Diatype* | *Berkeley Mono Â· GT Pressura Mono* |
| **Brutalist** | Free | Bricolage Grotesque (800) Â· Anton Â· Tanker Â· Big Shoulders Display | Geist Â· Switzer | Space Grotesk (numerals) Â· Geist Mono |
| | *Paid* | *Druk Â· Monument Extended Â· NaN Jaune Â· Migra Â· ABC Pressura* | *SÃ¶hne Breit Â· GT America* | *GT America Mono* |
| **Soft** | Free | Geist Â· Bricolage Grotesque (500) Â· Sentient Â· Newsreader | Geist Â· Crimson Pro Â· Switzer | Geist Mono Â· Satoshi (label) |
| | *Paid* | *SÃ¶hne Â· GT Pressura Â· Pangaia Â· Tobias* | *SÃ¶hne Â· Halyard Text Â· Satoshi* | *SÃ¶hne Mono Â· GT Maru Mono* |
| **Luxury** | Free | Cormorant Garamond Â· Fraunces Â· Cardo Â· DM Serif Display Â· Bodoni Moda | EB Garamond Â· Crimson Pro Â· Source Serif 4 | (rare; small caps from display family) |
| | *Paid* | *Canela Â· Tiempos Headline Â· GT Super Â· Domaine Display Â· Migra* | *Tiempos Text Â· Suisse Int'l Â· Domaine Text* | *(rarely used at this tier)* |
| **Playful** | Free | Bricolage Grotesque Â· Fraunces (italic) Â· Satoshi Â· Newsreader (italic) Â· Sentient | Geist Â· Newsreader Â· Satoshi | Geist Mono Â· Space Mono |
| | *Paid* | *Clash Display Â· Cabinet Grotesk Â· Migra Â· Tobias Â· Pangaia* | *Satoshi Â· Plus Jakarta Sans Â· GT Maru* | *Space Mono Â· GT Maru Mono* |
| **Austere** | Free | system-ui Â· Inter Tight (regular) Â· Geist (400) Â· Switzer (regular) | system-ui Â· Geist Â· Switzer | system-ui mono Â· Geist Mono |
| | *Paid* | *ABC Diatype Â· ABC Monument Grotesk Â· SÃ¶hne (regular) Â· ABC Pressura* | *ABC Diatype Â· SÃ¶hne* | *ABC Diatype Mono Â· SÃ¶hne Mono* |
| **Atmospheric** | Free | Geist (600) Â· Sentient Â· Tomorrow Â· Bricolage Grotesque | Geist (400) Â· Switzer | Geist Mono Â· JetBrains Mono |
| | *Paid* | *SÃ¶hne Â· GT Pressura Â· ABC Diatype* | *SÃ¶hne Â· ABC Diatype* | *Berkeley Mono Â· SÃ¶hne Mono* |
| **Workshop** *(Hallmark's own theme)* | Free | The Future Â· Geist Â· Cabinet Grotesk | The Future Â· Switzer | The Future Mono Â· Geist Mono |
| | *Paid* | *Avenir Next Â· GT Walsheim* | *SÃ¶hne Â· GT Walsheim* | *Berkeley Mono* |

**The discipline.** Default to the free pairings. They're not consolation prizes; Fraunces, Geist, Bricolage Grotesque, Cabinet Grotesk, Sentient, and JetBrains Mono are first-rate faces in 2026. The paid upgrades exist for two cases: (a) the user has explicitly confirmed they're licensed, or (b) the user is asking for a specific named foundry voice (e.g., "make it look like Klim", "I want SÃ¶hne"). Reach for Tier 2 only then; otherwise the free row is the right answer. Treat the free row as canon, the paid row as a *cited* alternative.

## Wordmark / logo typography

The wordmark in the navbar and footer **may use a different display face than the body**. On tone-rich themes (Editorial, Atelier, Specimen) it **should** â€” collapsing the wordmark into the body family flattens the visual hierarchy and the page reads as un-branded.

```css
:root {
  --display:       "Geist", system-ui, sans-serif;     /* body + display */
  --font-wordmark: "Fraunces", Georgia, serif;         /* logo only */
}
.wordmark {
  font-family: var(--font-wordmark);
  font-weight: 600;
  letter-spacing: -0.015em;
}
```

Recommended pairings (free baseline first):

- **Geist body â†’ Fraunces wordmark, IBM Plex Mono wordmark, or Bricolage Grotesque (heavy) wordmark**
- **Fraunces body â†’ Geist Mono wordmark, Inter Tight wordmark**
- **System-ui body â†’ JetBrains Mono wordmark, Newsreader wordmark**
- **Inter Tight body â†’ Fraunces wordmark, EB Garamond wordmark**

When to use the same family for both:

- **Editorial Â· Letter Â· Manifesto Â· Long Document** can collapse to a single family because the body voice carries the brand. The wordmark in these contexts is small, grounded, and earns its weight by being typeset rather than decorated.

When to use a contrasting family:

- **Bento Grid Â· Stat-Led Â· Workbench Â· Marquee Hero** â€” these archetypes lean visually generic (geometric grids, big numbers, browser-frame mockups) and need the wordmark to do the typographic differentiation work the body can't.

**Avoid the same-family collapse on a SaaS page.** A Geist-only page where the wordmark is also Geist 600 reads as un-designed; the wordmark in Fraunces SemiBold over a Geist body costs nothing and adds the one typographic register that says *this is a brand*.

## Scale

Pick a ratio. The default for Hallmark work is **1.25** (major third). Build the scale from a 16px body, then clamp display sizes for responsive.

```css
:root {
  --text-xs:   0.64rem;   /* 10.24px */
  --text-sm:   0.8rem;    /* 12.8px  */
  --text-base: 1rem;      /* 16px    */
  --text-md:   1.25rem;   /* 20px    */
  --text-lg:   1.5625rem; /* 25px    */
  --text-xl:   1.9531rem; /* 31.25px */
  --text-2xl:  2.4414rem;
  --text-3xl:  3.0518rem;
  --text-4xl:  3.8147rem;
  --text-display: clamp(2.75rem, 5vw + 1rem, 5.25rem);
}
```

**Display max â€” keep it â‰¤ 5.5rem (88 px).** Above that, hero headlines crowd themselves on 1280â€“1440 px viewports and require multi-line wrapping that almost always reads as drama, not gravity. Even on Manifesto / Brutal display-heavy themes, cap at 6rem (96 px). The exception is a single-line, single-word display (e.g. a stat) that occupies â‰¤ 12 ch â€” it can grow to 7rem. **Default emit format is `clamp(2.75rem, 5vw + 1rem, 5.25rem)`.**

### Hero headline sizing â€” match size to copy length

Count characters in the rendered hero `h1`. Pick the cap by bucket â€” the rule applies on top of any per-theme `--text-display` clamp:

| Headline length | Size cap | Notes |
| --- | --- | --- |
| **â‰¤ 20 chars** (e.g. *"Limitless"*, *"Made not generated"*) | full `--text-display`; single-word can grow to 7rem | Display-heavy themes only |
| **21â€“50 chars** (the default sweet spot) | `--text-display` | If it wraps past 2 lines at 414 px, step down to `--text-display-s` |
| **51â€“90 chars** | cap at `--text-display-s` | Strongly consider splitting into eyebrow + headline |
| **> 90 chars** | rewrite shorter, or cap at `--text-4xl` with tighter leading | A 100-char headline at display size is the single most reliable AI tell |

**Aggressive-display themes step down one rung when headline > 50 chars.** Brutal, Riso, and Manifesto clamp `--text-display` at 6.5â€“9rem â€” that ceiling is for â‰¤ 50-char statements only. Past 50 chars, route them to `--text-display-s` automatically. **When you write the headline yourself (no user-supplied copy), aim for â‰¤ 7 words and â‰¤ 50 chars from the start** â€” imperative or nominal phrase, never a gerund opener.

Use no more than five sizes on a single page. If you need more hierarchy, use weight and colour, not another size.

## Weights

- Body: one weight (typically 400 or 350). Bold for emphasis only.
- Headings: a weight that contrasts the body by at least 300 units. If body is 400, headings are 700 or 200 â€” not 500 or 600.
- Never synthesise. Load the weight you need; don't rely on `font-weight: bold` against a single-weight file.

## Required features

- `font-display: swap` on every web font.
- Match fallback metrics with `size-adjust`, `ascent-override`, `descent-override`, `line-gap-override` to prevent CLS.
- Tabular numbers on any data display: `font-variant-numeric: tabular-nums;`.
- Oldstyle figures for body copy where the face supports them: `font-variant-numeric: oldstyle-nums;`.
- Proper typographic punctuation: `" " â€” â€¦ â€˜ â€™`. Never straight quotes, never `--` or `...`.

## Body text rules

- Minimum 16px. Below 14px is accessibility-hostile.
- Line-height 1.5â€“1.65 on body copy, tighter (1.1â€“1.3) on display. **Floor for all-caps display heads (`text-transform: uppercase` on `.hero__display` / `.section__title` / `h1` / `h2`) is `1.0` â€” recommended `1.02â€“1.08`.** Below 1.0 the cap-tops of line N+1 collide with the baseline of line N (no descenders to cushion the gap); the comma + cap-D on a wrapped "PROMPT, / DIFFERENT" fuse into a single glyph blob. Condensed display faces (Anton, Inter Tight 900, Bebas Neue) make this worse. Gate 55 auto-fails the pattern.
- Measure 45â€“75 characters (`max-width: 65ch`).
- Never all-caps body copy. Never justified text without hyphenation. Never letter-spacing above 0.05em on body.

## Headings rules

- Tight tracking on display sizes (`letter-spacing: -0.02em` to `-0.04em` depending on the face).
- Loose tracking on small caps / labels (`letter-spacing: 0.08em` to `0.14em`, `text-transform: uppercase`, use small caps if the face has them: `font-variant-caps: all-small-caps;`).
- Skip no levels. `h1` â†’ `h2` â†’ `h3`. Style them visually how you like, but keep semantic order.

## Bans

- No Inter, no Roboto, no Open Sans. No system stack as the *only* stack.
- No gradient text on headings (`background-clip: text` with a gradient fill).
- No single-font pages.
- No all-caps paragraphs.
- No font-size below 14px for body copy, below 10px anywhere.
- No hard-synthesised bold or italic.
- **No more than three font families on a single page.** Display + body + one outlier is the ceiling. Four families = slop. Audit gate.
- No outlier face used in more than two slots. Wordmark + hero stat is the canonical pair; if you reach for a third slot, drop it back to the body face.
