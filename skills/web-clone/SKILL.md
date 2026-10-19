---
name: web-clone
description: >
  ç½‘ç«™å¤åˆ» / å…‹éš†æ–¹æ³•è®ºã€‚USE WHEN ç”¨æˆ·è¯´ å¤åˆ»ç½‘ç«™ã€å…‹éš†ç½‘ç«™ã€clone websiteã€æŠ„ä¸ªç«™ã€ä»¿ç«™ã€
  ç…§ç€è¿™ä¸ªç«™åšä¸€ä¸ªã€reproduce siteã€è¿˜åŽŸæŸä¸ªç½‘é¡µæ•ˆæžœã€æŠŠè¿™ä¸ªç«™æ¬ä¸‹æ¥æ”¹æˆæˆ‘çš„ã€
  å¤åˆ»æŸä¸ªäº¤äº’/WebGL/Canvas/Three.js æ•ˆæžœã€‚æä¾›ã€Œå…ˆæ‹¿çœŸæºç  â†’ åˆ¤è·¯å¾„ â†’ é€†å‘æ‹†è§£ â†’
  æ­å·¥ç¨‹ â†’ æ›¿æ¢å†…å®¹ã€çš„å¯ç§»æ¤å†³ç­–æ ‘ï¼Œè¦†ç›–é™æ€ç«™ / React-Vue-Next å†…å®¹ç«™ /
  WebGL-Canvas é‡å‰ç«¯ç«™ä¸‰å¤§åˆ†æ”¯ï¼Œå¹¶å¼ºåˆ¶æ ¸å¯¹ä»»ä½• AI äºŒæ‰‹åˆ†æžé‡Œçš„å¯æ‰§è¡Œä»£ç ã€‚
metadata:
  author: jane (xiaoer)
  version: "1.6.0"
  use_case: ä¸ªäººæœ¬åœ°å¤åˆ»/å­¦ä¹ ç½‘ç«™ï¼Œæ²‰æ·€è‡ª website-clones å…‹éš†ä¸­æž¢
---

# Web Clone Â· ç½‘ç«™å¤åˆ»æ–¹æ³•è®º

æŠŠ"å¤åˆ»ä¸€ä¸ªç½‘ç«™"åšæˆå¯é‡å¤çš„æµç¨‹ã€‚é…å¥—å·¥ç¨‹åŒºï¼š`~/projects/website-clones/`ï¼ˆæ¯ä¸ªå¤åˆ»æ˜¯ä¸€ä¸ªå­ç›®å½•ï¼‰ã€‚

## å¤´å·é“å¾‹ï¼šçœŸæºç è‡³ä¸Šï¼Œç»ä¸ä¿¡ AI æŽ¨æµ‹çš„ä»£ç 

> ä»»ä½• AI ç”Ÿæˆçš„"å¤åˆ»åˆ†æž/æ–½å·¥å›¾"ï¼Œ**æ­£æ–‡çš„æ¦‚å¿µéª¨æž¶å¯ä»¥å‚è€ƒï¼Œä½†é‡Œé¢çš„å¯æ‰§è¡Œä»£ç å—é»˜è®¤å…¨æ˜¯è‡†é€ çš„**ï¼Œå¿…é¡»é€è¡Œç”¨çœŸæºç æ ¸å¯¹ï¼Œå¦åˆ™ç…§æŠ„å¿…å´©ã€‚

**å®žè¯ï¼ˆmarbles æ¡ˆä¾‹ï¼‰**ï¼šä¸€ä»½ AI åˆ†æžæ–‡æ¡£æŠŠåŽŸç«™"è§£æžæ³•æ±‚å…‰çº¿-çƒä½“äº¤ç‚¹ + æŠŠå…‰å­¦ç»“æžœç¼–ç æˆä½ç§»å›¾ã€äº¤ç»™ SVG `feDisplacementMap` åŽ»æ‰­æ›²çœŸå®ž DOM"çš„çœŸæž¶æž„ï¼Œè‡†é€ æˆäº†"ray-marching + SDF + æŠŠ DOM å½“çº¹ç†é‡‡æ ·"â€”â€”ä¸¤å¥—å®Œå…¨ä¸åŒçš„å®žçŽ°ï¼Œç…§æŠ„åšä¸å‡ºåŽŸæ•ˆæžœä¸”æ…¢ N å€ã€‚è¯¦è§ `references/marbles-case.md`ã€‚

æ‰€ä»¥ç¬¬ä¸€åŠ¨ä½œæ°¸è¿œæ˜¯ï¼š**æ‹¿åˆ°çœŸæºç **ã€‚

## å†³ç­–æ ‘ï¼ˆæŒ‰é¡ºåºèµ°ï¼Œä¸è®¸è·³ï¼‰

### Step 0 Â· å…ˆå»ºæ ‡å‡†å·¥ç¨‹éª¨æž¶

```bash
node /Users/jane/.shared-skills/web-clone/scripts/init-clone.mjs <ç«™å> --url <åŽŸç«™URL>
```

è¯¥è„šæœ¬ä¼šåˆ›å»º `~/projects/website-clones/<ç«™å>-clone/`ã€`NOTES.md`ã€`RECON/screenshots/`ï¼Œé¿å…æ¯æ¬¡æ‰‹å·¥æ¼æŽ‰äº§ç‰©ã€‚

### Step 1 Â· å…ˆåŽ» GitHub æœæºç ï¼Œåˆ«æ€¥ç€æŠ“ç«™

```bash
unset SSL_CERT_FILE   # macOS æ€ªç™–ï¼Œbash å‰å…ˆè§£
# æŒ‰ç«™å/äº§å“åæœ
SSL_CERT_FILE=/etc/ssl/cert.pem gh api "search/repositories?q=<å…³é”®è¯>" \
  | jq -r '.items[] | "\(.full_name) â­\(.stargazers_count) \(.description)"' | head -10
# vercel.app/netlify.app/github.io çš„ URL slug å¸¸å¸¸å°±æ˜¯ ä»“åº“å / éƒ¨ç½²è€…ç”¨æˆ·å
```
- å•æ–‡ä»¶ç«™ï¼ˆgithub.io / çº¯ HTMLï¼‰â†’ ç›´æŽ¥æŠ“ rawï¼š`curl -sL https://raw.githubusercontent.com/<user>/<repo>/main/index.html`
- **æ‰¾åˆ°æºç ä¸”è®¸å¯å…è®¸ â†’ è·³ Step 4 ç›´æŽ¥ cloneã€‚** æ•™è®­ï¼šå…ˆæœ GitHub èƒ½çœ 30 åˆ†é’Ÿå¼¯è·¯ã€‚

### Step 2 Â· æ²¡æ‰¾åˆ°æºç  â†’ æµè§ˆå™¨ä¾¦å¯Ÿï¼ˆæŽ¢é’ˆï¼‰

åŠ è½½ `Browser` skill æˆ– playwright MCPï¼Œè·‘æŽ¢é’ˆæŠ½ä¿¡å·ï¼ˆæ¡†æž¶ / `window.THREE` / canvas æ•° / å¹³æ»‘æ»šåŠ¨åº“ / å­—ä½“ / scrollHeightï¼‰ã€‚æˆªå›¾ 1440/768/390 ä¸‰æ¡£ + ä¾¦å¯Ÿ JSON å­˜ `<ç«™>/RECON/`ã€‚

ä¼˜å…ˆç”¨å†…ç½®è„šæœ¬è·‘æ ‡å‡†ä¾¦å¯Ÿï¼š

```bash
node /Users/jane/.shared-skills/web-clone/scripts/recon-site.mjs \
  --url <åŽŸç«™URL> \
  --out ~/projects/website-clones/<ç«™å>-clone/RECON \
  --label original

node /Users/jane/.shared-skills/web-clone/scripts/asset-harvest.mjs \
  --recon ~/projects/website-clones/<ç«™å>-clone/RECON/original-recon.json \
  --out ~/projects/website-clones/<ç«™å>-clone/assets/original \
  --manifest ~/projects/website-clones/<ç«™å>-clone/RECON/asset-manifest.json

node /Users/jane/.shared-skills/web-clone/scripts/network-capture.mjs \
  --url <åŽŸç«™URL> \
  --out ~/projects/website-clones/<ç«™å>-clone/RECON/network \
  --label original

node /Users/jane/.shared-skills/web-clone/scripts/route-crawl.mjs \
  --url <åŽŸç«™URL> \
  --out ~/projects/website-clones/<ç«™å>-clone/RECON/routes \
  --label original \
  --max-pages 25 \
  --max-depth 2

node /Users/jane/.shared-skills/web-clone/scripts/interaction-probe.mjs \
  --url <åŽŸç«™URL> \
  --out ~/projects/website-clones/<ç«™å>-clone/RECON/interactions \
  --label original

node /Users/jane/.shared-skills/web-clone/scripts/sourcemap-hunt.mjs \
  --recon ~/projects/website-clones/<ç«™å>-clone/RECON/original-recon.json \
  --out ~/projects/website-clones/<ç«™å>-clone/RECON/sourcemaps
```

> ç™»å½•æ€ç§åŸŸç«™æ‰ç”¨ `bb-browser`ï¼›localhost / æ— ç™»å½•å…¬å¼€ç«™ç”¨ `Browser` skill æˆ– playwrightï¼ˆåˆ«åŠ¨ bb-browserï¼Œä¼šæŠ¢ Braveï¼‰ã€‚

### Step 2.5 Â· å…ˆç»™å¤æ‚åº¦å®šçº§ï¼Œåˆ«ç›²ç›®æ‰¿è¯º

æ ¹æ®ä¾¦å¯Ÿç»“æžœå…ˆå†™ä¸€ç‰ˆ"å¤åˆ»å‰é¢„åˆ¤"ï¼šå¤æ‚åº¦ L1-L6ã€æŽ¨èæ¨¡å¼ï¼ˆå¿ å®žå¤åˆ» / è§†è§‰å¤åˆ» / å†…å®¹çˆ†æ”¹ï¼‰ã€é¢„è®¡å¯è¿˜åŽŸèŒƒå›´ã€æ˜Žç¡®ä¸å…‹éš†çš„éƒ¨åˆ†ã€‚åˆ†çº§å’Œè¯„åˆ†è§„åˆ™è§ `references/assessment.md`ã€‚

**è‹¥æ¨¡å¼æ˜¯ã€Œè§†è§‰å¤åˆ»ã€æˆ–ã€Œå†…å®¹çˆ†æ”¹ã€** â†’ é¡ºæ‰‹äº§å‡ºç»“æž„åŒ–è®¾è®¡èº«ä»½ `design-dna.json`ï¼ŒæŠŠ"é‚£ä¸ªç«™çš„æ„Ÿè§‰"å˜æˆå¯ç‰ˆæœ¬åŒ–ã€å¯å¯¹ç…§çš„ token è§„èŒƒï¼Œè®© Step 6 æ›¿æ¢æ—¶"DNA ç•™ç€ã€å†…å®¹æ¢æŽ‰"æœ‰æ®å¯ä¾ï¼š

```bash
node /Users/jane/.shared-skills/web-clone/scripts/dna-scaffold.mjs \
  --recon ~/projects/website-clones/<ç«™å>-clone/RECON/original-recon.json \
  --out   ~/projects/website-clones/<ç«™å>-clone/RECON/design-dna.json \
  --name  "<ç«™å>"
```

è„šæœ¬ä¼šæŠŠä¾¦å¯Ÿåˆ°çš„å­—ä½“/è‰²å€™é€‰/æ¡†æž¶ç‰¹æ•ˆä¿¡å· best-effort é¢„å¡«ï¼Œå…¶ä½™å­—æ®µäººå·¥ Analyze è¡¥å…¨ã€‚ä¸‰ç»´ç»“æž„ï¼ˆdesign_system / design_style / visual_effectsï¼‰ã€å®Œæ•´ schemaã€é€‚ç”¨è¾¹ç•Œè§ `references/design-dna.md`ã€‚
> âš ï¸ **ã€Œå¿ å®žå¤åˆ»ã€åˆ†æ”¯ä¸è¦ç”¨ DNA**ï¼šçœŸæºç å°±æ˜¯çœŸç›¸ï¼Œåˆ«è®©"è¿‘ä¼¼é£Žæ ¼"çš„ DNA ç¨€é‡Šé€å­—èŠ‚é“å¾‹ã€‚

### Step 3 Â· æŒ‰ä¾¦å¯Ÿç»“æžœé€‰è·¯å¾„

| ä¾¦å¯Ÿç»“æžœ | èµ°å“ªæ¡è·¯ |
|---|---|
| é™æ€ HTML/CSSï¼Œæ— æ¡†æž¶ | `wget --mirror` æŠ“é•œåƒ â†’ åˆ è¿½è¸ªè„šæœ¬ â†’ æ”¹æ–‡æ¡ˆ |
| React / Vue / Nextï¼ˆå†…å®¹ä¸ºä¸»ï¼‰ | é‡å»ºæ¨¡æ¿ï¼ˆå¦‚ `ai-website-cloner-template`ï¼ŒNode 24+ï¼‰ï¼ŒçŒå†…å®¹ |
| SPA / SaaS / æ•°æ®é©±åŠ¨é¡µé¢ | å…ˆè·‘ `network-capture.mjs` ä¿å­˜ API fixtures â†’ æœ¬åœ° JSON/mock server æ›¿èº« |
| å¤šé¡µé¢å®˜ç½‘ / äº§å“ç«™ | å…ˆè·‘ `route-crawl.mjs` åšè·¯ç”±åœ°å›¾ â†’ æ¯ç±»é¡µé¢æŠ½æ¨¡æ¿ â†’ ç»Ÿä¸€æ›¿æ¢å†…å®¹ |
| å¤æ‚äº¤äº’ç«™ | å…ˆè·‘ `interaction-probe.mjs` è®°å½• hover/click/scroll/canvas drag çŠ¶æ€ â†’ æŒ‰çŠ¶æ€è¡¥äº¤äº’ï¼Œä¸è®¸åªæˆªé¦–å± |
| **WebGL / Canvas / Three.js é‡å‰ç«¯** | **æ·±åº¦é€†å‘çœŸæºç ï¼ˆè§ä¸‹ï¼‰â†’ å¿ å®žå¤åˆ» æˆ– æ‰¾åŒç±»å¼€æº 3D æ¨¡æ¿æ¢å†…å®¹**ã€‚å•æ–‡ä»¶åŽŸç”Ÿç«™å¸¸å¸¸é€å­—èŠ‚ä¿ç•™=æœ€å¿ å®žå¤åˆ»ã€‚**æ‰¾ä¸åˆ°çœŸæºç æ—¶èµ°è¿è¡Œæ—¶å¸§æ•èŽ· + baseline é—¸é—¨**ï¼Œçºªå¾‹è§ `references/effect-extraction.md`ï¼ˆå¯å§”æ‰˜ web-shader-extractorï¼‰ |
| **é™æ€æž„å»ºç«™ï¼ˆAstro/Vite SSG/Hugoï¼‰ï¼Œå«é‡ WebGL** | **`mirror-site.mjs` å…¨é‡é•œåƒéƒ¨ç½²èµ„äº§ â†’ è‡ªæ‰˜ç®¡å­—ä½“ + åˆ è¿½è¸ª â†’ æœ¬åœ° web æ ¹æœåŠ¡ = çœŸæºç  1:1 å¿ å®žå¤åˆ»**ã€‚å¯¹é™æ€ç«™ï¼Œ"æ‹¿åˆ°çœŸæºç "="é•œåƒéƒ¨ç½²èµ„äº§æ•´å¥—"ã€‚é…æ–¹è§ `references/static-mirror.md`ã€‚èŒƒä¾‹ï¼šoryzo.aiï¼ˆLusionï¼ŒL6ï¼Œé«˜æ–¯æ³¼æº…ï¼Œhero åƒç´  diff 5/5ï¼‰ |
| ç”¨çŽ°æˆå¼€æºä¸»é¢˜çš„ç«™ï¼ˆAstro/Hugo ä¸»é¢˜ï¼‰ | åŽ»å¯¹åº”ä¸»é¢˜å¸‚åœºæ‰¾æºä¸»é¢˜ï¼ˆ**ä»…é™å¥—ç”¨çŽ°æˆä¸»é¢˜çš„ç«™**ï¼›å®šåˆ¶ç«™èµ°ä¸Šä¸€è¡Œçš„å…¨é‡é•œåƒï¼Œåˆ«æ¥è¿™è¡Œï¼‰ |

L4-L6 å¤æ‚ç«™æŒ‰ `references/complex-playbooks.md` èµ°ï¼Œä¸è¦åªç”¨æ™®é€šå®˜ç½‘æµç¨‹ã€‚

### Step 4 Â· åœ¨å…‹éš†ä¸­æž¢é‡Œæ­å·¥ç¨‹

```bash
mkdir ~/projects/website-clones/<ç«™å>-clone && cd $_
# git æºç ï¼šclone è¿›æ¥ï¼›å•æ–‡ä»¶ï¼šæ”¾è¿›æ¥ã€‚åŽŸå§‹æºç ç•™ä¸€ä»½åªè¯»åŸºå‡† index-original.html
# æ£€æŸ¥ Node ç‰ˆæœ¬ï¼ˆpackage.json enginesï¼‰ï¼Œnvm use å¯¹åº”ç‰ˆæœ¬ï¼Œé’‰ .nvmrc
```

### Step 5 Â· åˆ è¿½è¸ª + å†™å…ƒä¿¡æ¯ + éªŒè¯

- **åˆ è¿½è¸ª**ï¼šGoogle Analyticsï¼ˆ`gtag` / `googletagmanager`ï¼‰ã€åƒç´ ã€çƒ­å›¾â€”â€”é€è¡Œç²¾ç¡®åˆ‡é™¤ï¼ˆGA å—å¸¸åœ¨ `<head>` é¡¶éƒ¨ï¼‰ã€‚
- **å†™ NOTES.md**ï¼ˆå¿…é¡»ï¼‰ï¼šåŒ…å«å¤æ‚åº¦ã€å¤åˆ»æ¨¡å¼ã€åŽŸç«™ vs å…‹éš†ç«™å¯¹æ¯”ã€ä¿çœŸåº¦è¯„åˆ†ã€å·²çŸ¥ç¼ºå£ã€‚æ¨¡æ¿è§ `references/deliverables.md`ã€‚
- **å¤æ‚ç«™å†™ TEARDOWN.md**ï¼ˆæŠ€æœ¯æ‹†è§£ï¼‰ã€‚æ‰€æœ‰ç»“è®ºæ ‡çœŸæºç è¡Œå·ã€‚
- **å¤åˆ»åŽè¯„åˆ†**ï¼šæŒ‰ `references/assessment.md` ç»™ç»“æž„ / è§†è§‰ / äº¤äº’ / å“åº”å¼ / å†…å®¹æ›¿æ¢ / åŠŸèƒ½å®Œæ•´åº¦æ‰“åˆ†ã€‚åˆ†æ•°è¦èƒ½è¢«æˆªå›¾ã€æºç ã€è¿è¡Œç»“æžœæ”¯æ’‘ã€‚
- **æµè§ˆå™¨çœŸéªŒè¯**ï¼ˆç¡¬è¦æ±‚ï¼Œä¸è®¸åªçœ‹ä»£ç å°±è¯´"åº”è¯¥èƒ½è·‘"ï¼‰ï¼šèµ·æœ¬åœ°æœåŠ¡å™¨ â†’ æµè§ˆå™¨æ‰“å¼€ â†’ æŠ“ consoleï¼ˆä¸èƒ½æœ‰ JS/WebGL ç¼–è¯‘é”™è¯¯ï¼‰â†’ æˆªå›¾å¯¹ç…§åŽŸç«™ã€‚è¯šå®žè®°å½•éªŒè¯ä¸äº†çš„éƒ¨åˆ†ï¼ˆå¦‚åˆæˆ PointerEvent `isTrusted=false` è§¦å‘ä¸äº†æ‹–æ‹½ï¼Œè¦å¦‚å®žå†™ï¼Œåˆ«ä¼ªé€ "æ‹–åŠ¨æˆåŠŸ"ï¼‰ã€‚

å¤åˆ»å®ŒæˆåŽå†è·‘ä¸€æ¬¡å…‹éš†ç«™ä¾¦å¯Ÿï¼Œå¹¶ç”Ÿæˆè‡ªåŠ¨å¯¹æ¯”æŠ¥å‘Šï¼š

```bash
node /Users/jane/.shared-skills/web-clone/scripts/recon-site.mjs \
  --url http://127.0.0.1:<ç«¯å£>/ \
  --out ~/projects/website-clones/<ç«™å>-clone/RECON \
  --label clone

node /Users/jane/.shared-skills/web-clone/scripts/route-crawl.mjs \
  --url http://127.0.0.1:<ç«¯å£>/ \
  --out ~/projects/website-clones/<ç«™å>-clone/RECON/routes-clone \
  --label clone \
  --max-pages 25 \
  --max-depth 2

node /Users/jane/.shared-skills/web-clone/scripts/interaction-probe.mjs \
  --url http://127.0.0.1:<ç«¯å£>/ \
  --out ~/projects/website-clones/<ç«™å>-clone/RECON/interactions-clone \
  --label clone

node /Users/jane/.shared-skills/web-clone/scripts/compare-recon.mjs \
  --original ~/projects/website-clones/<ç«™å>-clone/RECON/original-recon.json \
  --clone ~/projects/website-clones/<ç«™å>-clone/RECON/clone-recon.json \
  --visual-diff ~/projects/website-clones/<ç«™å>-clone/RECON/visual-diff-1440.json \
  --original-routes ~/projects/website-clones/<ç«™å>-clone/RECON/routes/original-route-map.json \
  --clone-routes ~/projects/website-clones/<ç«™å>-clone/RECON/routes-clone/clone-route-map.json \
  --original-interactions ~/projects/website-clones/<ç«™å>-clone/RECON/interactions/original-interactions.json \
  --clone-interactions ~/projects/website-clones/<ç«™å>-clone/RECON/interactions-clone/clone-interactions.json \
  --out ~/projects/website-clones/<ç«™å>-clone/CLONE_REPORT.md

node /Users/jane/.shared-skills/web-clone/scripts/visual-diff.mjs \
  --original ~/projects/website-clones/<ç«™å>-clone/RECON/screenshots/original-1440.png \
  --clone ~/projects/website-clones/<ç«™å>-clone/RECON/screenshots/clone-1440.png \
  --out ~/projects/website-clones/<ç«™å>-clone/RECON/visual-diff-1440.json \
  --diff ~/projects/website-clones/<ç«™å>-clone/RECON/screenshots/visual-diff-1440.png

node /Users/jane/.shared-skills/web-clone/scripts/audit-clone.mjs \
  --project ~/projects/website-clones/<ç«™å>-clone \
  --brand "<åŽŸç«™å“ç‰Œå>" \
  --out ~/projects/website-clones/<ç«™å>-clone/CLONE_AUDIT.md
```

### Step 6 Â· æ›¿æ¢æˆ Jane è‡ªå·±çš„ä¸œè¥¿

ç›®æ ‡æ°¸è¿œæ˜¯"åšå¥¹è‡ªå·±çš„ç«™"ï¼Œä¸æ˜¯æ¬ä¸€ä¸ªä¸€æ¨¡ä¸€æ ·çš„ã€‚æ›¿æ¢ä¸‰ä»¶å¥—ï¼šæ–‡å­—ï¼ˆ`index.html`/`data/*.json`/`content/*.md`ï¼‰ã€åª’ä½“ï¼ˆ`public`/`assets`ï¼‰ã€å“ç‰Œè‰²ï¼ˆCSS å˜é‡ / Tailwind themeï¼‰ã€‚ç»“æž„éžå¹³å‡¡å°±å†™ REPLACE_GUIDE.mdã€‚

**åšè¿‡ `design-dna.json`ï¼ˆè§†è§‰/çˆ†æ”¹æ¨¡å¼ï¼‰çš„**ï¼šè¿™ä¸€æ­¥å°±æ˜¯å®ƒçš„å…‘çŽ°â€”â€”**DNA ç•™ç€ã€å†…å®¹æ¢æŽ‰**ã€‚æŠŠ `design_system` è½æˆ CSS è‡ªå®šä¹‰å±žæ€§ã€æŒ‰ `design_style` åšä¸»è§‚å–èˆã€æŒ‰ `visual_effects.effect_intensity` é€‰å®žçŽ°å±‚çº§ï¼ˆlightweight CSS / medium Canvas+GSAP / heavy Three.jsï¼‰ï¼›ç´ æä¼˜å…ˆç”¨ `asset-harvest.mjs` å–åŽŸç«™çœŸå›¾ï¼Œåˆ« AI é‡ç»˜è¿‘ä¼¼ã€‚ç”Ÿæˆæµç¨‹è§ `references/design-dna.md`ã€‚

## é€†å‘æ‹†è§£ WebGL/Canvas é‡å‰ç«¯ï¼ˆæ ¸å¿ƒæ‰‹è‰ºï¼‰

æŠŠäº¤äº’ç«™æ‹†æˆ**æŠ€æœ¯æ”¯æŸ±**ï¼Œé€æŸ±å®šä½çœŸå®žå®žçŽ° + æ ‡è¡Œå·ï¼šæ¸²æŸ“ï¼ˆWebGL/ç€è‰²å™¨ç®—æ³•ï¼‰ã€åˆæˆï¼ˆSVG filter / å¤š canvas / åŽæœŸï¼‰ã€ç‰©ç†ã€äº¤äº’ã€éŸ³é¢‘ã€‚ç„¶åŽæ‰åŽ»æ ¸å¯¹ä»»ä½•äºŒæ‰‹åˆ†æžã€‚

**é€†å‘ç‰¹æ•ˆæ—¶ä¸‰ä»¶å¥—çºªå¾‹**ï¼ˆæ²»"è¾¹æŠ è¾¹ç¾ŽåŒ–ã€æœ€åŽæ—¢ä¸åƒä¹Ÿè¯´ä¸æ¸…"ï¼‰ï¼š
1. **è¯æ®åˆ†çº§**ï¼šæ¯æ¡ç»“è®ºæ ‡ `SOURCE`ï¼ˆçœŸæºç /source-map/è¿è¡Œæ—¶ dump/å¸§æ•èŽ·ï¼‰ã€`PARTIAL`ï¼ˆåå­—/åˆ‡ç‰‡ï¼Œå¾…è¯ï¼‰ã€`GUESS`ï¼ˆè§†è§‰æ‹Ÿåˆ/é­”æ•°ï¼‰ã€‚**æœªæ ‡=GUESSï¼Œç…§æŠ„å‰å¿…é¡»å‡çº§åˆ° SOURCEã€‚**
2. **no-compensation**ï¼šä¸¥ç¦é è°ƒäº®åº¦/é€Ÿåº¦/ä½ç½®/å™ªå£°åŽ»æŽ©ç›–æ—¶åº/åæ ‡/çŠ¶æ€é”™è¯¯ï¼›æ‹Ÿåˆå€¼ä»æ ‡ GUESSï¼Œå†™æ˜Žè¦æ‹¿åˆ°ä»€ä¹ˆè¯æ®æ‰èƒ½å‡çº§ã€‚
3. **baseline-first é—¸é—¨**ï¼šå…ˆç”¨çœŸå®ž draw call/shader/uniform åš"æœ€å°åŽŸæ ·å¯å¤çŽ° RAW REPLAY"â†’ é€å¸§æ¯”å¯¹é€šè¿‡ â†’ **æ‰å…è®¸**é‡æž„å·¥ç¨‹åŒ–ã€‚
è¯¦è§ `references/effect-extraction.md`ï¼ˆå«è¿è¡Œæ—¶æ•èŽ·å…œåº• + ä½•æ—¶å§”æ‰˜ web-shader-extractorï¼‰ã€‚

**å¯è¿ç§»çš„é«˜çº§èŒƒå¼**ï¼ˆå€¼å¾—æ”’ç€ï¼‰ï¼š
- **ä½ç§»å›¾æŠ˜å°„ DOM**ï¼šç¦»å± WebGL ç®—å‡º RG=ä½ç§»/B=è²æ¶…å°”çš„"ä½ç§»å›¾"ï¼Œå†ç”¨ SVG `<filter><feDisplacementMap scale=N>` æ‹¿å®ƒåŽ»æ‰­æ›²çœŸå®žçš„ã€æ´»çš„ã€å¯äº¤äº’çš„ HTMLâ€”â€”æŠ˜å°„çš„æ˜¯çœŸ DOMï¼ŒWebGL å…¨ç¨‹ä¸ç¢° DOM åƒç´ ã€‚è¿™æ˜¯ marbles çš„çµé­‚ï¼Œä¹Ÿæ˜¯ Three.js `MeshPhysicalMaterial(transmission)` åšä¸åˆ°çš„äº‹ï¼ˆå®ƒåªèƒ½åš"çŽ»ç’ƒçƒå¤–è§‚"ï¼Œåšä¸å‡º"æŠ˜å°„æ•´ä¸ªç½‘é¡µ"ï¼‰ã€‚

è¯¦ç»†æ–¹æ³• + marbles çœŸæž¶æž„é€é¡¹æ‹†è§£ â†’ `references/reverse-engineering.md`ã€`references/marbles-case.md`ã€‚

## è®¸å¯ä¸Žç½²åï¼ˆclone å‰å¿…æŸ¥ï¼‰

```bash
SSL_CERT_FILE=/etc/ssl/cert.pem gh api repos/<u>/<r> | jq '.license'  # + æ‰¾ LICENSE æ–‡ä»¶ + çœ‹ README
```

| è®¸å¯ | èƒ½åšä»€ä¹ˆ |
|---|---|
| MIT / Apache / BSD / Unlicense | å¯æ”¹ã€å¯ä¸Šçº¿ï¼Œä¿ç•™è‡´è°¢å³å¯ |
| **NONEï¼ˆæ—  LICENSE æ–‡ä»¶ / æœªå£°æ˜Žï¼‰** | **é»˜è®¤ä¿ç•™æ‰€æœ‰æƒåˆ©**ã€‚ä»…æœ¬åœ°å­¦ä¹ /å¤åˆ»ï¼Œé¡»ç½²ååŽŸä½œè€…ï¼Œ**æœªç»è®¸å¯ä¸å¾—å…¬å¼€é‡æ–°éƒ¨ç½²**ã€‚åˆ«å› ä¸ºä»£ç å…¬å¼€å°±å½“æˆå¯è‡ªç”±ç”¨ |
| ä¸“æœ‰ / æ˜Žç¡®ç¦æ­¢ | åªè¯»å­¦ä¹ ï¼Œä¸å¤åˆ¶ä¸éƒ¨ç½² |

âš ï¸ åˆ«æŠŠ"GitHub ä¸Šæ˜¯å…¬å¼€çš„"æˆ–"gh api ä¸€æ—¶æŸ¥ä¸åˆ°"ç­‰åŒäºŽ MITâ€”â€”æ ¸å®žåˆ°åº•ã€‚

## äº§ç‰©è§„èŒƒ
- æ¯ä¸ªå­é¡¹ç›®æ ¹ç›®å½•ï¼š`NOTES.md`ï¼ˆæºä¿¡æ¯/æŠ€æœ¯æ ˆ/license/æ›¿æ¢åœ°å›¾/è·‘èµ·æ¥å‘½ä»¤ï¼‰
- å¤æ‚äº¤äº’ç«™è¿½åŠ ï¼š`TEARDOWN.md`ï¼ˆæŠ€æœ¯æ‹†è§£ï¼Œæ ‡è¡Œå·ï¼‰
- éœ€è¦å¯¹å¤–æ±‡æŠ¥æˆ–è¯„ä¼° skill æ•ˆæžœæ—¶è¿½åŠ ï¼š`CLONE_REPORT.md`ï¼ˆåŽŸç«™ vs å…‹éš†ç«™å®Œæ•´å¯¹æ¯”ï¼‰
- ä¸Šçº¿å‰è¿½åŠ ï¼š`CLONE_AUDIT.md`ï¼ˆè¿½è¸ªè„šæœ¬ã€åŽŸç«™å“ç‰Œ/è¯­è¨€æ®‹ç•™ã€TODOã€å¤–é“¾é£Žé™©ï¼‰
- `RECON/screenshots/`ï¼šåŽŸç«™ vs å…‹éš†å¯¹ç…§å›¾
- å¤åˆ»å®Œæ›´æ–°ä¸­æž¢ `README.md` ç´¢å¼•è¡Œ

## å†…ç½®è„šæœ¬
- `scripts/init-clone.mjs`ï¼šåˆå§‹åŒ–å…‹éš†é¡¹ç›®éª¨æž¶å’Œ `NOTES.md`ã€‚
- `scripts/recon-site.mjs`ï¼šç”¨ Playwright æ‰“å¼€é¡µé¢ï¼Œé‡‡é›†æ¡†æž¶/èµ„æº/DOM ç»“æž„/console é”™è¯¯ï¼Œå¹¶ä¿å­˜ä¸‰æ¡£æˆªå›¾ã€‚
- `scripts/asset-harvest.mjs`ï¼šä»Žä¾¦å¯Ÿ JSON ä¸‹è½½åŽŸç«™å›¾ç‰‡ã€è„šæœ¬ã€æ ·å¼å¹¶ç”Ÿæˆç´ ææ¸…å•ã€‚
- `scripts/network-capture.mjs`ï¼šæ•èŽ· XHR/fetch è¯·æ±‚å¹¶ä¿å­˜ JSON/text å“åº”ï¼Œç»™ SPA/SaaS åšæœ¬åœ° fixturesã€‚
- `scripts/mirror-site.mjs`ï¼šçœŸæµè§ˆå™¨å…¨ç¨‹æ»šåŠ¨æ•èŽ·æ¯ä¸€ä¸ªçœŸå®žè¯·æ±‚ â†’ æŒ‰è·¯å¾„é•œåƒåŒæºèµ„äº§ï¼ˆå« JS è¿è¡Œæ—¶ fetch çš„ `.sog/.buf/.wasm/.riv`/å­—ä½“ï¼‰ï¼Œç»™é™æ€æž„å»ºç«™ï¼ˆAstro/Vite SSG/Hugoï¼‰åš 1:1 å¿ å®žå¤åˆ»ã€‚è¯¦è§ `references/static-mirror.md`ã€‚
- `scripts/route-crawl.mjs`ï¼šçˆ¬åŒç«™å†…éƒ¨é“¾æŽ¥ï¼ŒæŒ‰è·¯ç”±ä¿å­˜æˆªå›¾ã€æ ‡é¢˜ã€H1ã€ç»“æž„ä¿¡å·ï¼Œè§£å†³å¤šé¡µé¢ç«™åªå¤åˆ»é¦–é¡µçš„é—®é¢˜ã€‚
- `scripts/interaction-probe.mjs`ï¼šè‡ªåŠ¨æ‰§è¡Œ scrollã€hoverã€å®‰å…¨ clickã€canvas dragï¼Œä¿å­˜äº¤äº’å‰åŽçŠ¶æ€ã€æˆªå›¾ã€ç½‘ç»œå’Œ console è¯æ®ã€‚
- `scripts/sourcemap-hunt.mjs`ï¼šä»Ž JS chunk é‡Œæ‰¾ source mapï¼Œèƒ½æ‹¿åˆ°å°±ä¿å­˜æºç æ˜ å°„ã€‚
- `scripts/compare-recon.mjs`ï¼šè¯»å–åŽŸç«™ä¸Žå…‹éš†ç«™çš„ä¾¦å¯Ÿ JSONã€è·¯ç”±å›¾ã€äº¤äº’è¯æ®ï¼Œç”Ÿæˆ `CLONE_REPORT.md`ã€‚
- `scripts/visual-diff.mjs`ï¼šç”¨æµè§ˆå™¨ canvas åšæˆªå›¾åƒç´ å·®å¼‚ï¼Œè¾“å‡º visual score å’Œå·®å¼‚å›¾ã€‚
- `scripts/audit-clone.mjs`ï¼šæ‰«æè¿½è¸ªè„šæœ¬ã€åŽŸç«™å“ç‰Œæ®‹ç•™ã€æ—¥æ–‡æ®‹ç•™ã€TODOã€å¤–éƒ¨ URL é£Žé™©ã€‚
- `scripts/dna-scaffold.mjs`ï¼šä»Žä¾¦å¯Ÿ JSON ç”Ÿæˆ `design-dna.json` è®¾è®¡èº«ä»½éª¨æž¶ï¼ˆå­—ä½“/è‰²å€™é€‰/æ¡†æž¶ç‰¹æ•ˆä¿¡å· best-effort é¢„å¡«ï¼‰ï¼Œç»™ã€Œè§†è§‰å¤åˆ» / å†…å®¹çˆ†æ”¹ã€æ¨¡å¼ç”¨ã€‚è¯¦è§ `references/design-dna.md`ã€‚

## èƒ½åŠ›è¾¹ç•Œï¼ˆé»˜è®¤å£å¾„ï¼‰
- **èƒ½é«˜ä¿çœŸåš**ï¼šé™æ€è¥é”€é¡µã€ä¼ä¸šå®˜ç½‘ã€å†…å®¹åž‹ React/Vue/Next å‰ç«¯ã€å¯ç›´æŽ¥æ‹¿åˆ°æºç çš„åŠ¨ç”»ç«™ã€‚
- **èƒ½è§†è§‰è¿˜åŽŸä½†ä¼šç®€åŒ–**ï¼šCMS åŽå°æ•°æ®ã€å¤æ‚æ»šåŠ¨å™äº‹ã€å¤šç«¯æ–­ç‚¹ã€WebGL/Canvas ç‰¹æ•ˆã€ç¬¬ä¸‰æ–¹åµŒå…¥ã€‚
- **é»˜è®¤ä¸æ‰¿è¯ºå®Œæ•´å…‹éš†**ï¼šç™»å½•ã€æ”¯ä»˜ã€ä¸‹å•ã€æœç´¢æŽ¨èã€æƒé™ç³»ç»Ÿã€æœåŠ¡ç«¯ä¸šåŠ¡é€»è¾‘ã€ä¸“æœ‰ APIã€å—ç‰ˆæƒé™åˆ¶çš„ç´ æã€‚éœ€è¦æ—¶åªåšå¯æ¼”ç¤ºå‰ç«¯æ›¿èº«ã€‚
- **å†…å®¹çˆ†æ”¹æ—¶**ï¼šä¼˜å…ˆä¿ç•™åŽŸç«™çš„ä¿¡æ¯æž¶æž„ã€èŠ‚å¥ã€åŠ¨æ•ˆå’Œè§†è§‰è¯­æ³•ï¼ŒæŠŠæ–‡æ¡ˆã€å›¾ç‰‡ã€å“ç‰Œè‰²ã€ä¸šåŠ¡ä¸»å¼ æ¢æˆ Jane è‡ªå·±çš„å†…å®¹ã€‚

## æ——èˆ°æ¡ˆä¾‹
`~/projects/website-clones/marbles-clone/` â€” åŽŸç”Ÿ WebGL + SVG Filter + è‡ªç ”ç‰©ç†çš„çŽ»ç’ƒå¼¹ç ç«™ï¼Œé€å­—èŠ‚å¿ å®žå¤åˆ» + å®Œæ•´ TEARDOWNï¼Œæ˜¯"WebGL é‡å‰ç«¯åˆ†æ”¯"çš„èŒƒä¾‹ã€‚
