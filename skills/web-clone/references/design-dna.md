# Design DNA Â· ç»“æž„åŒ–è®¾è®¡èº«ä»½å±‚ï¼ˆè§†è§‰å¤åˆ» / å†…å®¹çˆ†æ”¹ä¸“ç”¨ï¼‰

æŠŠ"åšæˆé‚£ä¸ªç«™çš„æ„Ÿè§‰"ä»Žæ¨¡ç³Šæ„Ÿè§‰å˜æˆ**å¯ç‰ˆæœ¬åŒ–ã€å¯å¤ç”¨ã€å¯å¯¹ç…§çš„ JSON è§„èŒƒ**ã€‚
ç”¨åœ¨ã€Œè§†è§‰å¤åˆ»ã€å’Œã€Œå†…å®¹çˆ†æ”¹ã€ä¸¤ä¸ªæ¨¡å¼â€”â€”ä¾¦å¯Ÿä¹‹åŽã€æ­å·¥ç¨‹ä¹‹å‰ï¼Œå¤šäº§å‡ºä¸€ä¸ª `design-dna.json`ï¼Œ
è®© Step 6ã€Œæ›¿æ¢æˆ Jane è‡ªå·±çš„ä¸œè¥¿ã€æœ‰æ®å¯ä¾ï¼š**DNA ç•™ç€ã€å†…å®¹æ¢æŽ‰**ã€‚

> æ–¹æ³•ä¸Ž schema æ”¹ç¼–è‡ª [zanwei/design-dna](https://github.com/zanwei/design-dna)ï¼ˆMITï¼‰ï¼ŒæŒ‰ web-clone çš„å£å¾„è£å‰ªã€‚

## âš ï¸ é€‚ç”¨è¾¹ç•Œï¼ˆå¿…é¡»å…ˆè¯»ï¼‰

Design DNA çš„ç”Ÿæˆå“²å­¦æ˜¯**"è¿‘ä¼¼é£Žæ ¼"**â€”â€”å®ƒäº§å‡ºçš„æ˜¯"é£Žæ ¼ä¸€è‡´çš„æ–°ç«™"ï¼Œä¸æ˜¯é€å­—èŠ‚å¤åˆ¶ã€‚
è¿™å’Œ web-clone çš„å¤´å·é“å¾‹ã€ŒçœŸæºç è‡³ä¸Š / é€å­—èŠ‚å¿ å®žã€æ˜¯**ç›¸åæ–¹å‘**ã€‚æ‰€ä»¥ï¼š

| æ¨¡å¼ | ç”¨ä¸ç”¨ DNA |
|---|---|
| å¿ å®žå¤åˆ»ï¼ˆæ‹¿åˆ°çœŸæºç  / å•æ–‡ä»¶åŽŸç”Ÿç«™ / WebGL é€å­—èŠ‚è¿˜åŽŸï¼‰ | **ä¸ç”¨**ã€‚çœŸæºç å°±æ˜¯çœŸç›¸ï¼Œåˆ«è®© DNA æŠŠå®ƒç¨€é‡Šæˆ"è¿‘ä¼¼" |
| è§†è§‰å¤åˆ»ï¼ˆè¿˜åŽŸè§‚æ„Ÿä½†ç®€åŒ–å®žçŽ°ï¼‰ | **ç”¨**ã€‚DNA æ˜¯è¿™æ¡è·¯çš„ä¸»äº§ç‰© |
| å†…å®¹çˆ†æ”¹ï¼ˆä¿ç•™ä¿¡æ¯æž¶æž„+èŠ‚å¥+è§†è§‰è¯­æ³•ï¼Œæ¢æˆ Jane çš„å†…å®¹ï¼‰ | **ç”¨**ã€‚DNA å®šä¹‰"è¦ä¿ç•™ä»€ä¹ˆ"ï¼Œå†…å®¹éšä¾¿æ¢ |

ä¸€å¥è¯ï¼š**DNA æ˜¯ç»™"åšæˆ‘è‡ªå·±çš„ç«™"ç”¨çš„ï¼Œä¸æ˜¯ç»™"æ¬ä¸€æ¨¡ä¸€æ ·"ç”¨çš„ã€‚**

## ä¸‰ç»´ç»“æž„

DNA JSON åˆ†ä¸‰å±‚ï¼Œå¯¹åº”"å¯é‡åŒ– / å¯æ„ŸçŸ¥ / ç‰¹æ®Šæ¸²æŸ“"ï¼š

1. **`design_system`** â€” å¯æµ‹é‡çš„ tokenï¼šcolor / typography / spacing / layout / shape / elevation / iconography / motion / components
2. **`design_style`** â€” ä¸»è§‚æ„ŸçŸ¥ï¼šaestheticï¼ˆmood/genre/eraï¼‰/ visual_language / composition / imagery / interaction_feel / brand_voice_in_ui
3. **`visual_effects`** â€” è¶…å‡ºæ™®é€š CSS çš„æ¸²æŸ“ï¼šbackground / particles / 3d / shader / scroll / text / cursor / image / glass-neu / canvas / svg

`design_system` ç›´æŽ¥è½æˆ CSS å˜é‡ï¼›`design_style` æŒ‡å¯¼ä¸»è§‚å–èˆï¼›`visual_effects` å†³å®šè¦ä¸è¦ä¸Š Canvas/WebGL/GSAPï¼Œå¹¶å’Œæœ¬ skill çš„ã€ŒWebGL é€†å‘åˆ†æ”¯ã€å¯¹æŽ¥ã€‚

## ä¸‰æ­¥å·¥ä½œæµ

1. **Structure** â€” å…ˆçœ‹ schemaï¼ˆä¸‹æ–¹ + `dna-scaffold.mjs` ç”Ÿæˆçš„éª¨æž¶ï¼‰ï¼Œç¡®è®¤è¦å¡«å“ªäº›ç»´åº¦ï¼Œå¯è£æŽ‰ä¸ç›¸å…³çš„ã€‚
2. **Analyze** â€” ä»Žä¾¦å¯Ÿäº§ç‰©é‡ŒæŠ½ï¼š
   - é¢œè‰²ï¼š`<label>-recon.json` çš„ `cssVariables`ï¼ˆ`--` å¼€å¤´çš„è‰²å€¼ï¼‰+ `sections[].style` çš„ `backgroundColor` / `color`ï¼ŒæŒ‰é¢ç§¯å®š primaryã€æŒ‰ CTA å®š accentã€‚
   - å­—ä½“ï¼š`fonts` æ•°ç»„ + `sections[].style.fontFamily`ï¼Œåˆ† heading / body / monoã€‚
   - é—´è·/å¸ƒå±€ï¼šæˆªå›¾ + `sections[].rect` é‡èŠ‚å¥ä¸Žæœ€å¤§å®½åº¦ã€‚
   - ç‰¹æ•ˆï¼š`frameworks.three/gsap/lenis` + `canvases` + `counts.canvas` â†’ å¡« `visual_effects.overview.primary_technology` å’Œå„ enabled æ ‡å¿—ã€‚
   - é£Žæ ¼/æ„ŸçŸ¥ï¼šçœ‹ä¸‰æ¡£æˆªå›¾ï¼ˆ1440/768/390ï¼‰äººå·¥åˆ¤ moodã€genreã€compositionã€whitespaceã€‚
   - **æ¯ä¸ªå­—æ®µéƒ½è¦å¡«å®žï¼Œä¸è¦ç•™ç©ºå­—ç¬¦ä¸²**ï¼›å¡«ä¸å‡ºçš„æ ‡ `TODO` å¹¶è¯´æ˜Žç¼ºä»€ä¹ˆè¯æ®ã€‚
3. **Generate** â€” è§£æž DNA â†’ ç”Ÿæˆ CSS è‡ªå®šä¹‰å±žæ€§ â†’ æŒ‰ `design_style` åšä¸»è§‚å†³ç­– â†’ æŒ‰ `effect_intensity` é€‰å®žçŽ°å±‚çº§ï¼ˆlightweight=CSS/SVG/vanillaï¼›medium=Canvas2D/GSAP/Lottieï¼›heavy=Three.js/GLSL/Pixiï¼‰â†’ è¾“å‡ºé¡µé¢ â†’ çŒ Jane è‡ªå·±çš„å†…å®¹ã€‚**ç´ æä¼˜å…ˆä»ŽåŽŸç«™å–çœŸå›¾ï¼ˆç”¨ `asset-harvest.mjs`ï¼‰ï¼Œä¸è¦ AI é‡ç»˜è¿‘ä¼¼ã€‚**

## è„šæ‰‹æž¶

```bash
node /Users/jane/.shared-skills/web-clone/scripts/dna-scaffold.mjs \
  --recon ~/projects/website-clones/<ç«™å>-clone/RECON/original-recon.json \
  --out   ~/projects/website-clones/<ç«™å>-clone/RECON/design-dna.json
```

è„šæœ¬ä¼šè¾“å‡ºå®Œæ•´ DNA éª¨æž¶ï¼Œå¹¶æŠŠä¾¦å¯Ÿåˆ°çš„å­—ä½“ã€CSS è‰²å˜é‡ã€æ¡†æž¶/ç‰¹æ•ˆä¿¡å·**best-effort é¢„å¡«**ï¼Œ
å…¶ä½™å­—æ®µç•™ `""`ï¼ˆå¾…äººå·¥ Analyze è¡¥å…¨ï¼‰ã€‚æ²¡æœ‰ `--recon` ä¹Ÿèƒ½è·‘ï¼Œçº¯å‡ºç©ºéª¨æž¶ã€‚

## DNA JSON å®Œæ•´å­—æ®µï¼ˆæ”¹ç¼–è‡ª design-dnaï¼ŒMITï¼‰

```json
{
  "meta": { "name": "", "description": "", "source_references": "", "created_at": "" },

  "design_system": {
    "color": {
      "palette_type": "monochromatic | complementary | analogous | triadic | split-complementary",
      "primary":   { "hex": "", "role": "" },
      "secondary": { "hex": "", "role": "" },
      "accent":    { "hex": "", "role": "" },
      "neutral":   { "scale": "", "usage": "" },
      "semantic":  { "success": "", "warning": "", "error": "", "info": "" },
      "surface":   { "background": "", "card": "", "elevated": "" },
      "contrast_strategy": "high contrast | subtle layers | dark-on-light dominant"
    },
    "typography": {
      "type_scale": {
        "display":    { "size": "", "weight": "", "line_height": "", "tracking": "" },
        "heading_1":  { "size": "", "weight": "", "line_height": "", "tracking": "" },
        "heading_2":  { "size": "", "weight": "", "line_height": "", "tracking": "" },
        "heading_3":  { "size": "", "weight": "", "line_height": "", "tracking": "" },
        "body":       { "size": "", "weight": "", "line_height": "", "tracking": "" },
        "body_small": { "size": "", "weight": "", "line_height": "", "tracking": "" },
        "caption":    { "size": "", "weight": "", "line_height": "", "tracking": "" },
        "overline":   { "size": "", "weight": "", "line_height": "", "tracking": "" }
      },
      "font_families": { "heading": "", "body": "", "mono": "" },
      "font_style_notes": ""
    },
    "spacing": { "base_unit": "", "scale": "", "content_density": "compact | comfortable | spacious", "section_rhythm": "" },
    "layout":  { "grid_system": "", "max_content_width": "", "columns": "", "gutter": "", "breakpoints": "", "alignment_tendency": "strict grid | centered | asymmetric | mixed" },
    "shape":   { "border_radius": { "small": "", "medium": "", "large": "", "pill": "" }, "border_usage": "none | subtle 1px | bold borders | only on inputs", "divider_style": "" },
    "elevation": { "shadow_style": "none | soft diffused | hard drop | layered", "levels": { "low": "", "medium": "", "high": "" }, "depth_cues": "shadows | overlapping layers | blur/glass | color intensity" },
    "iconography": { "style": "", "stroke_weight": "", "size_scale": "", "preferred_set": "" },
    "motion": { "easing": "", "duration_scale": { "micro": "", "normal": "", "macro": "" }, "entrance_pattern": "", "exit_pattern": "", "philosophy": "minimal functional | playful bouncy | cinematic | none" },
    "components": { "button_style": "", "input_style": "", "card_style": "", "navigation_pattern": "", "modal_style": "", "list_style": "", "component_notes": "" }
  },

  "design_style": {
    "aesthetic": { "mood": [], "visual_metaphor": "", "era_influence": "", "genre": "", "personality_traits": [], "adjectives": [] },
    "visual_language": { "complexity": "minimal | moderate | rich | maximal", "ornamentation": "none | subtle accents | decorative | heavily ornamented", "whitespace_usage": "", "visual_weight_distribution": "", "focal_strategy": "single hero element | distributed interest | progressive reveal", "contrast_level": "", "texture_usage": "" },
    "composition": { "hierarchy_method": "scale contrast | color weight | spatial isolation | typographic hierarchy", "balance_type": "symmetric | asymmetric | radial | mosaic", "flow_direction": "", "grouping_strategy": "", "negative_space_role": "" },
    "imagery": { "photo_treatment": "", "illustration_style": "", "graphic_elements": "", "pattern_usage": "", "image_shape": "" },
    "interaction_feel": { "feedback_style": "", "hover_behavior": "", "transition_personality": "snappy | smooth glide | bouncy elastic | fade-subtle", "loading_style": "", "microinteraction_density": "" },
    "brand_voice_in_ui": { "tone": "", "formality": "", "cta_style": "direct imperative | friendly invitation | urgent scarcity | subtle suggestion", "empty_state_approach": "", "error_tone": "" }
  },

  "visual_effects": {
    "overview": { "effect_intensity": "none | subtle-accent | moderate | heavy-immersive", "performance_tier": "lightweight | medium | heavy", "fallback_strategy": "", "primary_technology": "CSS only | Canvas 2D | WebGL/Three.js | GSAP | Lottie | SVG SMIL | Pixi.js" },
    "background_effects": { "type": "gradient-animation | noise-field | mesh-gradient | video-bg | generative-art | none", "description": "", "technology": "", "params": { "color_palette": "", "speed": "", "density": "", "opacity": "", "blend_mode": "" } },
    "particle_systems": { "enabled": false, "type": "floating-dots | confetti | snow | fireflies | connected-nodes | custom", "description": "", "technology": "", "params": { "count": "", "shape": "", "size_range": "", "movement_pattern": "", "color_behavior": "", "interaction": "mouse-repel | mouse-attract | click-burst | none", "spawn_area": "" } },
    "3d_elements": { "enabled": false, "type": "hero-model | product-viewer | scene-bg | text-extrusion | abstract-geometry", "description": "", "technology": "", "params": { "renderer": "", "lighting": "", "camera": "", "materials": "", "geometry": "", "post_processing": [], "interaction_model": "" } },
    "shader_effects": { "enabled": false, "type": "noise-distortion | wave | morph | color-shift | custom-GLSL", "description": "", "technology": "", "params": { "uniforms": "", "vertex_manipulation": "", "fragment_output": "", "noise_type": "perlin | simplex | worley | fbm", "distortion": "" } },
    "scroll_effects": { "parallax": { "enabled": false, "layers": "", "depth_range": "", "speed_curve": "" }, "scroll_triggered_animations": { "enabled": false, "trigger_points": "", "animation_type": "fade-up | scale-in | clip-reveal | counter | draw-SVG", "scrub_behavior": "" }, "scroll_morphing": { "enabled": false, "description": "" } },
    "text_effects": { "type": "split-letter-animate | typewriter | glitch | gradient-fill | 3d-extrude | none", "description": "", "technology": "", "params": { "split_strategy": "by-char | by-word | by-line", "animation_per_unit": "", "stagger": "", "effect_style": "" } },
    "cursor_effects": { "enabled": false, "type": "custom-cursor | magnetic-buttons | spotlight | trail | none", "description": "", "params": { "shape": "", "size": "", "blend_mode": "", "trail": "", "interaction_zone": "" } },
    "image_effects": { "type": "hover-distortion | reveal-clip | parallax-tilt | rgb-shift | none", "description": "", "technology": "", "params": { "filter_pipeline": "", "hover_transform": "", "reveal_animation": "", "distortion_type": "barrel | wave | liquid | glitch" } },
    "glassmorphism_neumorphism": { "enabled": false, "style": "glass | neumorphic-light | neumorphic-dark | frosted-layers | none", "params": { "blur_radius": "", "transparency": "", "border_treatment": "", "shadow_type": "", "light_source_angle": "" } },
    "canvas_drawings": { "enabled": false, "type": "generative-lines | interactive-blobs | data-visualization | pattern-fill | none", "description": "", "technology": "", "params": { "draw_method": "", "animation_loop": "", "color_scheme": "", "responsiveness": "", "interaction": "" } },
    "svg_animations": { "enabled": false, "type": "path-draw | morph-shapes | logo-reveal | decorative-loop | none", "description": "", "params": { "animation_method": "", "path_morphing": "", "stroke_animation": "", "filter_effects": "" } },
    "composite_notes": ""
  }
}
```

## å’Œ WebGL é€†å‘åˆ†æ”¯çš„åˆ†å·¥

- `visual_effects` é‡Œæ ‡äº† `heavy-immersive` / `WebGL/Three.js` / `shader_effects.enabled=true` çš„ç«™ï¼Œ**åˆ«ç”¨ DNA åŽ»"è¿‘ä¼¼"é‚£ä¸ªç‰¹æ•ˆ**â€”â€”é‚£æ˜¯ `effect-extraction.md` + `reverse-engineering.md` çš„æ´»ï¼Œè¦é€†å‘çœŸå®žçŽ°ã€‚
- DNA åœ¨è¿™ç§ç«™é‡Œåªè´Ÿè´£"ç‰¹æ•ˆ**ä¹‹å¤–**"çš„è®¾è®¡å±‚ï¼ˆé…è‰²/æŽ’ç‰ˆ/å¸ƒå±€/æ™®é€šåŠ¨æ•ˆï¼‰ï¼Œç‰¹æ•ˆæœ¬èº«èµ°é€†å‘æˆ–å§”æ‰˜ web-shader-extractorã€‚
