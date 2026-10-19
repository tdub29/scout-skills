# Advanced Techniques

Load for character consistency, conversational editing, weights, negative prompts and style mixing.

## Advanced Techniques

### ðŸŒŸ Gemini (Nano Banana) Techniques - PRIMARY

#### Character Consistency
```
First prompt: "Generate a character: [detailed description]"
Follow-up: "Show the same character [in new scenario/pose/style]"
# Gemini will maintain character likeness across images
```

#### Conversational Editing
```
Initial: "Create [image description]"
Edits:
- "Make the background darker"
- "Add [element] to the scene"
- "Change [attribute] to [new value]"
# Each edit builds on the previous image
```

#### Photographic Control
```
Use technical terms:
- "85mm portrait lens at f/1.8" (lens + aperture)
- "wide-angle shot from low angle" (lens + perspective)
- "shallow depth of field with bokeh" (focus effect)
- "golden hour lighting from left" (lighting direction)
```

#### Semantic Positive Descriptions
```
Instead of: "no cars, no people"
Use: "an empty, peaceful street with no signs of activity"

Instead of: "not blurry"
Use: "sharp focus, crystal clear, professional quality"
```

---

### Other Platform Techniques (Secondary)

#### Weight Control (Midjourney)
```
(red flower)::2 (blue flower)::1
# Red flower weighted 2x more than blue
```

#### Negative Prompts (Stable Diffusion)
```
Negative prompt: ugly, blurry, low quality, distorted,
bad anatomy, watermark, text
```

#### Style Mixing (Multiple Platforms)
```
in the style of [Artist A] combined with [Artist B]
```

#### Multi-Concept Fusion (Multiple Platforms)
```
a fusion of [concept 1] and [concept 2]
```
