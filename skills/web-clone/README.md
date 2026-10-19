# ðŸªž Web Clone Â· ç½‘ç«™å¤åˆ»æ–¹æ³•è®º

> Reproduce any website â€” from a single-file static page to a WebGL-heavy interactive demo â€” without faking it from AI hallucinations.
> æŠŠä»»ä½•ä¸€ä¸ªç½‘ç«™(ä»Žå•æ–‡ä»¶é™æ€é¡µåˆ° WebGL é‡å‰ç«¯ demo)å¿ å®žå¤åˆ»å‡ºæ¥ â€”â€” ä¸é  AI è‡†æµ‹ä»£ç ç¡¬æŠ„ã€‚

**English** Â· [ä¸­æ–‡](#ä¸­æ–‡)

---

## What this skill does

You see a website you love. You want to clone it â€” to learn how it works, to remix it into your own thing, or to run it offline. AI tools love to produce *plausible-looking* "clone analysis" documents full of code blocks that are entirely fabricated and break the moment you run them.

This skill is a **methodology plus executable probes that put real source first**, with a 6-step decision tree covering:

- Static HTML/CSS sites â†’ `wget --mirror`
- React / Vue / Next content sites â†’ rebuild on a template
- Multi-page sites â†’ crawl internal routes before designing templates
- Interactive sites â†’ record hover / click / scroll / canvas-drag states before cloning
- **WebGL / Canvas / Three.js heavy frontends** â†’ reverse-engineer real source, line by line; when there's no findable source, runtime frame-capture + a **baseline-first replay gate** with `SOURCE / PARTIAL / GUESS` evidence grading
- **Static-built sites (Astro / Vite SSG / Hugo), even WebGL-heavy** â†’ `mirror-site.mjs` full-scroll-captures and mirrors every deployed asset (incl. runtime-fetched `.sog/.buf/.wasm`) for a true 1:1 clone â€” for a static site, "get the real source" = "mirror the whole deployed bundle"
- Verify in a real browser, document the truth, replace content with yours
- **Visual / rebrand modes** â†’ distill a versionable `design-dna.json` (design tokens + style + effects), then "keep the DNA, swap the content"

## Iron rule: real source first, never copy AI-guessed code

> Any AI-written "clone analysis" â€” treat the conceptual skeleton as a hint, but **assume every executable code block is hallucinated** until you've verified it against real source code line by line.

**Case in point** (see `references/marbles-case.md`): A real WebGL marbles demo uses **analytic ray-sphere intersection** + an SVG `feDisplacementMap` to refract the live DOM. An AI analysis confidently described it as **ray-marching + SDF + sampling the DOM as a texture** â€” two entirely different implementations. Copying the AI version produces nothing like the original and runs many times slower.

So **step 1 is always: get the real source**.

## What's in here

```
claude-skill-web-clone/
â”œâ”€â”€ SKILL.md                       â† The methodology (loaded by Claude Code / Codex / Cursor)
â”œâ”€â”€ README.md
â”œâ”€â”€ LICENSE                         â† MIT
â”œâ”€â”€ follow-wechat-qrcode.jpg
â””â”€â”€ references/
    â”œâ”€â”€ reverse-engineering.md     â† How to dissect a WebGL/Canvas frontend, line by line
    â”œâ”€â”€ effect-extraction.md       â† Evidence grading + baseline-first gate for extracting effects
    â”œâ”€â”€ static-mirror.md           â† 1:1 clone of static-built sites (Astro/Vite SSG/Hugo) via full asset mirror
    â”œâ”€â”€ design-dna.md              â† Structured design-identity layer (visual / rebrand modes)
    â”œâ”€â”€ marbles-case.md            â† Flagship case: real architecture vs AI hallucination
    â””â”€â”€ deliverables.md            â† NOTES.md / TEARDOWN.md / RECON/ templates
â””â”€â”€ scripts/
    â”œâ”€â”€ recon-site.mjs             â† Browser screenshots + DOM/framework/resource signals
    â”œâ”€â”€ mirror-site.mjs            â† Full-scroll capture + mirror every same-origin asset (static-site 1:1 clone)
    â”œâ”€â”€ route-crawl.mjs            â† Same-site route map + screenshot per route
    â”œâ”€â”€ interaction-probe.mjs      â† Scroll/hover/click/canvas-drag state evidence
    â”œâ”€â”€ network-capture.mjs        â† XHR/fetch capture for SPA fixtures
    â”œâ”€â”€ asset-harvest.mjs          â† Download discovered source assets
    â”œâ”€â”€ dna-scaffold.mjs           â† Build a design-dna.json skeleton, prefilled from recon
    â””â”€â”€ visual-diff.mjs            â† Pixel comparison for original vs clone screenshots
```

## Install

This is a [Claude Code skill](https://docs.claude.com/en/docs/agents-and-tools/skills). Drop it into your skills directory:

```bash
git clone https://github.com/Jane-xiaoer/claude-skill-web-clone.git ~/.claude/skills/web-clone
```

Then use it by saying things like:
- "å¤åˆ»è¿™ä¸ªç½‘ç«™: https://..."
- "Clone this site for me"
- "Reverse-engineer this WebGL demo"
- "æŠŠè¿™ä¸ªç«™æŠ„ä¸‹æ¥æ”¹æˆæˆ‘çš„"

Claude / Codex will load `SKILL.md` and walk the decision tree.

## The decision tree (one-screen summary)

| Step | What to do |
|---|---|
| **1** | `gh api search/repositories?q=<name>` â€” find the real source on GitHub FIRST |
| **2** | If no source: browser-probe the site, crawl routes, capture network, and probe interactions |
| **3** | Pick the path: `wget` mirror / template rebuild / **WebGL reverse-engineering** / theme market |
| **4** | Set up `~/projects/website-clones/<name>-clone/` (or your equivalent), keep `index-original.html` read-only |
| **5** | Strip tracking, write `NOTES.md` + `TEARDOWN.md`, verify in a real browser with screenshots |
| **6** | Replace text / media / brand colors with yours |

## License & attribution discipline

Before deploying anything publicly, **check the source repo's license**:

| License | What you can do |
|---|---|
| MIT / Apache / BSD / Unlicense | Modify, redeploy, just keep credits |
| **NONE / unstated** | Default = **All Rights Reserved**. Local learning only, must credit, **do not redeploy publicly without permission** |
| Proprietary / explicitly forbidden | Read-only learning, no copying, no deployment |

âš ï¸ "Code is on GitHub" â‰  "code is MIT". Many viral demos have no LICENSE file and default to All Rights Reserved.

## Flagship case

`marbles-case.md` documents the full reverse-engineering of [chiuhans111/marbles](https://github.com/chiuhans111/marbles) â€” a 1067-line single-file WebGL + SVG-filter glass marbles interactive demo â€” and contrasts the real architecture with an AI-generated clone analysis that got the core mechanism completely backwards. This is the canonical example of why you must verify against real source.

---

## ä¸­æ–‡

### è¿™ä¸ª skill æ˜¯å¹²ä»€ä¹ˆçš„

ä½ çœ‹åˆ°ä¸€ä¸ªå–œæ¬¢çš„ç½‘ç«™,æƒ³å¤åˆ» â€”â€” å­¦å®ƒæ€Žä¹ˆåšã€æ”¹æˆä½ è‡ªå·±çš„ç‰ˆæœ¬ã€æˆ–è€…ç¦»çº¿è·‘èµ·æ¥ã€‚AI å·¥å…·æœ€çˆ±äº§å‡º**çœ‹èµ·æ¥ç…žæœ‰å…¶äº‹**çš„"å¤åˆ»åˆ†æžæ–‡æ¡£",é‡Œé¢çš„ä»£ç å—å‡ ä¹Žå…¨æ˜¯è‡†é€ çš„,ç…§æŠ„å¿…å´©ã€‚

è¿™ä¸ª skill æŠŠ"çœŸæºç è‡³ä¸Š"åšæˆå¯é‡å¤çš„æµç¨‹,**6 æ­¥å†³ç­–æ ‘**è¦†ç›–ä¸‰å¤§åˆ†æ”¯:
- é™æ€ HTML/CSS ç«™ â†’ `wget --mirror`
- React / Vue / Next å†…å®¹ç«™ â†’ é‡å»ºæ¨¡æ¿çŒå†…å®¹
- **WebGL / Canvas / Three.js é‡å‰ç«¯** â†’ é€†å‘çœŸæºç ,é€è¡Œæ ¸å¯¹;æ‰¾ä¸åˆ°æºç æ—¶ç”¨è¿è¡Œæ—¶å¸§æ•èŽ· + **baseline-first å¤çŽ°é—¸é—¨** + `SOURCE/PARTIAL/GUESS` è¯æ®åˆ†çº§
- **é™æ€æž„å»ºç«™(Astro/Vite SSG/Hugo),å“ªæ€•é‡ WebGL** â†’ `mirror-site.mjs` å…¨ç¨‹æ»šåŠ¨æ•èŽ· + é•œåƒæ¯ä¸€ä¸ªéƒ¨ç½²èµ„äº§(å«è¿è¡Œæ—¶ fetch çš„ `.sog/.buf/.wasm`),åšçœŸ 1:1 å¿ å®žå¤åˆ»â€”â€”å¯¹é™æ€ç«™,"æ‹¿åˆ°çœŸæºç "="é•œåƒéƒ¨ç½²èµ„äº§æ•´å¥—"(èŒƒä¾‹:Lusion oryzo.ai,é«˜æ–¯æ³¼æº…,hero åƒç´  diff 5/5)
- **è§†è§‰å¤åˆ» / å†…å®¹çˆ†æ”¹æ¨¡å¼** â†’ æŠŠ"é‚£ä¸ªç«™çš„æ„Ÿè§‰"è’¸é¦æˆå¯ç‰ˆæœ¬åŒ–çš„ `design-dna.json`(è®¾è®¡ token + é£Žæ ¼ + ç‰¹æ•ˆ),ç„¶åŽ"DNA ç•™ç€ã€å†…å®¹æ¢æŽ‰"
- æµè§ˆå™¨çœŸéªŒè¯,å¦‚å®žè®°å½•,æœ€åŽæ›¿æ¢æˆä½ è‡ªå·±çš„å†…å®¹

### å¤´å·é“å¾‹:çœŸæºç è‡³ä¸Š,ç»ä¸æŠ„ AI è‡†é€ ä»£ç 

> ä»»ä½• AI å†™çš„"å¤åˆ»åˆ†æž",**æ¦‚å¿µéª¨æž¶å¯ä»¥å‚è€ƒ,ä½†é‡Œé¢çš„å¯æ‰§è¡Œä»£ç å—é»˜è®¤å…¨æ˜¯è‡†é€ çš„**,å¿…é¡»ç”¨çœŸæºç æ ¸å¯¹,å¦åˆ™ç…§æŠ„å¿…å´©ã€‚

**å®žè¯æ¡ˆä¾‹**:ä¸€ä»½ AI åˆ†æžæ–‡æ¡£æŠŠåŽŸç«™"è§£æžæ³•æ±‚å…‰çº¿-çƒä½“äº¤ç‚¹ + æŠŠå…‰å­¦ç»“æžœç¼–ç æˆä½ç§»å›¾ + äº¤ç»™ SVG `feDisplacementMap` æ‰­æ›²çœŸå®ž DOM"çš„çœŸæž¶æž„,è‡†é€ æˆäº†"ray-marching + SDF + æŠŠ DOM å½“çº¹ç†é‡‡æ ·"â€”â€” ä¸¤å¥—å®Œå…¨ä¸åŒçš„å®žçŽ°,ç…§æŠ„åšä¸å‡ºåŽŸæ•ˆæžœä¸”æ…¢ N å€ã€‚è¯¦è§ `references/marbles-case.md`ã€‚

### å®‰è£…

è¿™æ˜¯ä¸€ä¸ª [Claude Code skill](https://docs.claude.com/en/docs/agents-and-tools/skills)ã€‚clone åˆ°ä½ çš„ skills ç›®å½•:

```bash
git clone https://github.com/Jane-xiaoer/claude-skill-web-clone.git ~/.claude/skills/web-clone
```

ç„¶åŽè·Ÿ Claude / Codex / Cursor è¯´:
- ã€Œå¤åˆ»è¿™ä¸ªç½‘ç«™: https://...ã€
- ã€ŒæŠŠè¿™ä¸ªç«™æŠ„ä¸‹æ¥æ”¹æˆæˆ‘çš„ã€
- ã€Œé€†å‘æ‹†è§£è¿™ä¸ª WebGL demoã€

AI ä¼šè‡ªåŠ¨åŠ è½½ `SKILL.md` èµ°å†³ç­–æ ‘ã€‚

### æ——èˆ°èŒƒä¾‹

`references/marbles-case.md` æ‹†è§£äº† [chiuhans111/marbles](https://github.com/chiuhans111/marbles) â€”â€” 1067 è¡Œå•æ–‡ä»¶ WebGL + SVG filter çŽ»ç’ƒå¼¹ç ç«™,çœŸæž¶æž„å¯¹æ¯” AI åˆ†æžæ–‡æ¡£çš„é”™è¯¯,æ˜¯"ä¸ºä»€ä¹ˆå¿…é¡»çœŸæºç æ ¸å¯¹"çš„æ ‡å‡†æ•™æã€‚

---

## è‡´è°¢ / Credits

- **æ–¹æ³•è®ºæ²‰æ·€æ¥æº / Origin**:Jane çš„å…‹éš†ä¸­æž¢ `~/projects/website-clones/` å·¥ä½œæµ(2026-05-27 marbles æ¡ˆä¾‹è·‘é€šåŽæŠ½å‡º skill)
- **æ——èˆ°èŒƒä¾‹åŽŸä½œ / Flagship case author**:[chiuhans111/marbles](https://github.com/chiuhans111/marbles) by Hans Chiu â€” æ²¡æœ‰è¿™ä»½å•æ–‡ä»¶ 1067 è¡Œçš„çŽ»ç’ƒå¼¹ç æºç å°±æ²¡æœ‰è¿™ä¸ª skill çš„"çœŸæºç è‡³ä¸Š"é“å¾‹
- **è®¾è®¡èº«ä»½å±‚ schema / Design-DNA schema**:`references/design-dna.md` çš„ä¸‰ç»´ DNA JSON æ”¹ç¼–è‡ª [zanwei/design-dna](https://github.com/zanwei/design-dna)ï¼ˆMITï¼‰ï¼Œç”¨äºŽ"è§†è§‰å¤åˆ» / å†…å®¹çˆ†æ”¹"æ¨¡å¼
- **ç‰¹æ•ˆæå–çºªå¾‹ / Effect-extraction discipline**:`references/effect-extraction.md` çš„è¯æ®åˆ†çº§ + baseline-first é—¸é—¨å— [lixiaolin94/skills Â· web-shader-extractor](https://github.com/lixiaolin94/skills) å¯å‘ï¼ˆè¯¥ä»“åº“æ—  LICENSEï¼Œæœ¬ skill åªå€Ÿæ–¹æ³•æ¦‚å¿µã€ç”¨è‡ªå·±çš„è¯é‡å†™ï¼Œæœªå¤åˆ¶å…¶ä»£ç æˆ–åŽŸæ–‡ï¼‰
- **è¿­ä»£æ‰“ç£¨ / Iteration**:Jane(`@xiaoerzhan`) + Claude Code(å¤šè½® reverse-engineering)

---

## License

MIT. Use it freely, remix it, ship it. Attribution welcome but not required.

å¦‚æžœè¿™ä¸ª skill è®©ä½ å…äºŽåœ¨ AI è‡†é€ ä»£ç ä¸Šæµªè´¹ä¸€ä¸ªä¸‹åˆ,æ¬¢è¿Ž â­ è¿™ä¸ªä»“åº“ã€‚
If this skill saves you a frustrating afternoon of debugging fake AI code, â­ the repo.

---

## ðŸ“± å…³æ³¨ä½œè€… / Follow Me

å¦‚æžœè¿™ä¸ªä»“åº“å¯¹ä½ æœ‰å¸®åŠ©,æ¬¢è¿Žå…³æ³¨æˆ‘ã€‚åŽé¢æˆ‘ä¼šæŒç»­æ›´æ–°æ›´å¤š AI Skillã€è®¾è®¡æ–¹æ³•ã€ç½‘ç«™ç¾Žå­¦å’Œåˆ›æ„å·¥ä½œæµã€‚

If this repo helped you, follow me for more AI skills, design systems, web aesthetics, and creative workflows.

- X (Twitter): [@xiaoerzhan](https://x.com/xiaoerzhan)
- å¾®ä¿¡å…¬ä¼—å· / WeChat Official Account: æ‰«ç å…³æ³¨ / Scan to follow

<p align="center">
  <img src="./follow-wechat-qrcode.jpg" alt="Jane WeChat Official Account QR code" width="300" />
</p>

<p align="center"><strong>ä¸­æ–‡:</strong>æ¬¢è¿Žå…³æ³¨æˆ‘çš„å…¬ä¼—å·,ä¸€èµ·ç ”ç©¶ AI Skillã€è®¾è®¡åŽŸåˆ™ã€ç½‘ç«™è¡¨è¾¾å’Œåˆ›æ„å·¥ä½œæµã€‚</p>

<p align="center"><strong>English:</strong> Follow my WeChat Official Account for more AI skills, design principles, web aesthetics, and creative workflows.</p>
