# Prompt Craft Reference

Production-quality prompt engineering for HeyGen Video Agent. Combines official HeyGen guidance with patterns validated across 80+ test videos.

Load this when the user wants cinematic/polished output, scene-by-scene control, or specific visual styles.

---

## Prompting Levels (from HeyGen Official Guide)

### Level 1: Basic
Just describe content. Video Agent fills in the rest.
```
"Introduce HeyGen to knowledge workers, talk about its Talking Avatar models"
```

### Level 2: Script-Driven (RECOMMENDED DEFAULT)
Paste a full video script. Agent follows scene-by-scene while improving flow, timing, and visuals.
This is "the single biggest upgrade most people miss." â€” HeyGen docs

### Level 3: Scene-by-Scene (Maximum Control)
```
Scene 1: [Scene Type]
  Visual: [Describe exact visual]
  VO/Script: "[What the avatar says]"
```

**Official recommendation:** Don't assign per-scene timestamps. Natural flow + tone description outperforms rigid scene structure.

---

## Prompt Anatomy (Production Quality)

```
FORMAT:    What kind of video, how long, what energy
TONE:      Emotional register, references
AVATAR:    "The selected presenter" (when avatar_id set) or delivery style
STYLE:     Colors, typography, motion rules, transitions (see Style Block)
CRITICAL ON-SCREEN TEXT:  Exact strings that must appear literally
SCENE-BY-SCENE:  (if >60s) Individual scene breakdowns with VO and visual type
MUSIC:     Genre, energy arc
```

**Rule: Content/script first, style block at the end.** Keeps creative intent clean and technical specs organized.

### Critical On-Screen Text

List every exact string. Without this, Video Agent rephrases, summarizes, or rounds numbers.

```
CRITICAL ON-SCREEN TEXT (display literally):
- "$141M ARR â€” All-Time High"
- "1.85M Signups â€” +28% MoM"
- Quote: "Use technology to serve the message." â€” Shalev Hani
```

---

## Style Block

Every prompt should end with a style block. Without one, visuals look inconsistent scene-to-scene.

### The HeyGen Catchall (official team recommendation)
```
Use minimal, clean styled visuals. Blue, black, and white as main colors.
Leverage motion graphics as B-rolls and A-roll overlays. Use AI videos when necessary.
When real-world footage is needed, use Stock Media.
Include an intro sequence, outro sequence, and chapter breaks using Motion Graphics.
```

### Style Presets (from HeyGen docs)

| Style | Best For | Prompt Language |
|-------|----------|-----------------|
| Minimalistic | Corporate, Tech, SaaS | "Use minimalistic, clean visuals with lots of white space" |
| Cartoon/Animated | Education, Kids | "Use cartoon-style illustrated visuals" |
| Bold & Vibrant | Marketing, Social | "Use bold, vibrant colors and dynamic visuals" |
| Cinematic | Brand films, High-end | "Use cinematic quality visuals with dramatic lighting" |
| Flat Design | Modern, App demos | "Use flat design style with geometric shapes" |
| Gradient Modern | Tech, Startup | "Use modern gradient backgrounds and sleek transitions" |
| Retro/Vintage | Nostalgia, Creative | "Use retro-inspired visuals with warm tones" |

### Brand Colors

Be explicit with hex codes and fonts:
```
Use #1E40AF as primary blue, #F8FAFC as background white, #0F172A for text.
Font: Inter family throughout.
```

Without defined colors, visuals look inconsistent scene-to-scene.

---

## Media Types & When to Use Each

Video Agent supports three media types. Guide it explicitly or it guesses (often wrong).

### Motion Graphics
Animated text, icons, charts, shapes, transitions.
- **A-roll overlays:** lower thirds, bullet points, animated callouts
- **B-roll scenes:** animated explanations, data viz, process flows
- **Chapter cards:** section breaks, intros, outros
- **Best for:** Data, statistics, brand elements, technical diagrams

### AI-Generated Images & Videos
- Conceptual illustrations, abstract concepts
- Custom scenarios stock can't cover
- Stylized visuals in particular artistic style
- **Best for:** Abstract concepts, custom scenarios, product mockups

### Stock Media
Real-world footage from stock libraries.
- Authentic scenes (offices, cities, people)
- Industry-specific (medical, manufacturing, retail)
- **Best for:** Real environments, human emotions, establishing shots

### Decision Matrix

| Content Type | Motion Graphics | AI Generated | Stock Media |
|---|---|---|---|
| Data/Statistics | âœ… Best | âŒ | âŒ |
| Abstract Concepts | âœ… Good | âœ… Best | âŒ |
| Real Environments | âŒ | âš ï¸ Can work | âœ… Best |
| Brand Elements | âœ… Best | âŒ | âŒ |
| Human Emotions | âŒ | âš ï¸ Uncanny | âœ… Best |
| Custom Scenarios | âš ï¸ Limited | âœ… Best | âš ï¸ May not exist |
| Technical Diagrams | âœ… Best | âŒ | âŒ |

---

## Scene Types

| Type | Format | When |
|------|--------|------|
| **A-ROLL** | Avatar speaking to camera | Intros, key insights, CTAs, emotional beats |
| **FULL SCREEN B-ROLL** | No avatar, motion graphics only | Data visualization, info-dense content |
| **A-ROLL + OVERLAY** | Split frame: avatar + content | Presenting data while maintaining human connection |

**Rotation is mandatory.** Never 3+ of the same type in a row.

**Voiceover on EVERY scene.** Silent B-roll = broken video.

### Scene-by-Scene Template (HeyGen Official Format)

```
Scene 1: [Scene Type]
  Visual: [Describe exact visual â€” include media type]
  VO/Script: "[What the avatar says]"
```

### Detailed Scene Templates (validated in testing)

**A-ROLL:**
```
SCENE 1 â€” A-ROLL
[Avatar center-frame, excited, hands gesturing]
VOICEOVER: "The exact script for this scene."
Lower-third: "TITLE TEXT" white on blue bar.
```

**B-ROLL with layered motion:**
```
SCENE 2 â€” FULL SCREEN B-ROLL
[NO AVATAR â€” motion graphic only]
VOICEOVER: "The exact script for this scene."
Dark background with subtle grid. "HEADLINE" SLAMS in from left.
Three data cards CASCADE from right, staggered. Bottom ticker SLIDES in.
```

**A-ROLL + OVERLAY:**
```
SCENE 3 â€” A-ROLL + OVERLAY
[Avatar LEFT 35%. Content RIGHT 65%.]
VOICEOVER: "The exact script for this scene."
RIGHT SIDE: Stats COUNT UP below headline.
```

---

### Non-English Videos

The same prompt structure applies regardless of language:
1. **Script/narration:** In the video language
2. **Style block:** Always English (Video Agent directive)
3. **Motion verbs:** Always English (SLAMS, CASCADE, etc.)
4. **Critical on-screen text:** In whatever language should appear on screen
5. **Scene labels:** English (Scene 1, Scene 2) â€” structural, not rendered

---

## Example Prompts (from HeyGen Official Guide)

### Compliance Training
```
Use a professional female avatar. Make a compliance training video explaining phishing
in detail. Use examples and list top watch-outs. Leverage motion graphics as A-roll
overlay and B-roll to help explain core concepts.
```

### Educational Explainer (Voice-Over Only)
```
Create a 1-minute video about camera aperture. Use minimal science diagrams and
visualizations. No avatar needed, only voice-over. Cool neutrals (navy, cyan),
thin-line diagrams, and slow elegant motion. B-roll is abstract scientific
illustrations. Sequencing: definition â†’ diagram expansion â†’ conceptual layering.
```

### Brand Story (Animated)
```
Make a video telling the story of how Twitch got started. Use cartoon-style
animations and overlays. I want Twitch's iconic colors and fonts. Use motion
graphics overlays and AI-generated B-roll.
```

### Product Introduction (Japanese â€” non-English example)
```
æ—¥æœ¬ã®ãƒŠãƒ¬ãƒƒã‚¸ãƒ¯ãƒ¼ã‚«ãƒ¼å‘ã‘ã«HeyGenã‚’ç´¹ä»‹ã™ã‚‹1åˆ†é–“ã®ãƒ“ãƒ‡ã‚ªã‚’ä½œæˆã—ã¦ãã ã•ã„ã€‚
ãƒˆãƒ¼ã‚­ãƒ³ã‚°ã‚¢ãƒã‚¿ãƒ¼ãƒ¢ãƒ‡ãƒ«ã®ç‰¹å¾´ã‚’èª¬æ˜Žã—ã€å…·ä½“çš„ãªæ´»ç”¨ä¾‹ã‚’3ã¤å«ã‚ã¦ãã ã•ã„ã€‚
ãƒŠãƒ¬ãƒ¼ã‚¿ãƒ¼ã¯é¸æŠžã•ã‚ŒãŸãƒ—ãƒ¬ã‚¼ãƒ³ã‚¿ãƒ¼ãŒèª¬æ˜Žã—ã¾ã™ã€‚

CRITICAL ON-SCREEN TEXT (display literally):
- "HeyGen ã‚¢ãƒã‚¿ãƒ¼ V"
- "3åˆ†ã§å‹•ç”»ä½œæˆ"
- "APIé€£æºå¯¾å¿œ"

STYLE â€” SWISS PULSE (MÃ¼ller-Brockmann): Black/white + electric blue #0066FF.
Grid-locked. Helvetica Bold. Animated counters. Diagonal accents.
Grid wipe transitions.
```

Note: Script content is in Japanese but STYLE block and scene labels remain in English â€” these are Video Agent directives, not viewer-facing content.

---

## Motion Vocabulary

Every visual element should have a motion verb. Static frames look dead.

### High Energy
- **SLAMS** â€” `"$95M" SLAMS in from left at -5 degrees`
- **CRASHES** â€” `Title CRASHES in from right, screen-shake on impact`
- **PUNCHES** â€” `Quote card PUNCHES up from bottom`

### Medium Energy
- **CASCADE** â€” `Three cards CASCADE from top, staggered 0.3s`
- **SLIDES** â€” `Ticker SLIDES in from right, continuous scroll`
- **FILLS** â€” `Progress bar FILLS 0 to 90% in orange`
- **DRAWS** â€” `Chart line DRAWS itself left to right`

### Low Energy
- **types on** â€” `Quote types on word by word in italic white`
- **fades in** â€” `Logo fades in at center, held 3 seconds`
- **COUNTS UP** â€” `"1.85M" COUNTS UP from 0 in amber`

---

## Pro Tips (from HeyGen community)

1. **Save your catchall as a template.** Find a style combo that works, reuse it. Consistency builds brand.
2. **Iterate in conversation.** Video Agent remembers context within a session. "Make the intro shorter" or "swap B-roll in scene 3 for stock footage" without re-prompting everything.
3. **Stack style at the end.** Content first, style directives last.
4. **Describe B-roll as motion verbs** ("slams in," "counts up"), NOT layout coordinates ("upper-left, 48pt").

---

## What Doesn't Work

- **Layout coordinates** â€” "upper-left: headline in 48pt" â†’ blank frames. Use motion verbs.
- **Named artists without specs** â€” "Ikko Tanaka style" means nothing. Translate to colors + shapes + motion.
- **B-roll under 5 seconds** â€” Causes black/empty frames. 10s+ minimum.
- **Static elements** â€” Every element needs a motion verb.
- **Per-scene timestamps** â€” Makes delivery robotic (per HeyGen's own research). Use overall duration only.
