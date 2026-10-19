---
name: stable-diffusion-image-generation
description: "Local Stable Diffusion via HuggingFace Diffusers"
version: 1.0.0
author: Orchestra Research
license: MIT
tags: [Image Generation, Stable Diffusion, Diffusers, Text-to-Image, Multimodal, Computer Vision]
dependencies: [diffusers>=0.30.0, transformers>=4.41.0, accelerate>=0.31.0, torch>=2.0.0]
---

# Stable Diffusion Image Generation

Comprehensive guide to generating images with Stable Diffusion using the HuggingFace Diffusers library.

## When to use Stable Diffusion

**Use Stable Diffusion when:**
- Generating images from text descriptions
- Performing image-to-image translation (style transfer, enhancement)
- Inpainting (filling in masked regions)
- Outpainting (extending images beyond boundaries)
- Creating variations of existing images
- Building custom image generation workflows

**Key features:**
- **Text-to-Image**: Generate images from natural language prompts
- **Image-to-Image**: Transform existing images with text guidance
- **Inpainting**: Fill masked regions with context-aware content
- **ControlNet**: Add spatial conditioning (edges, poses, depth)
- **LoRA Support**: Efficient fine-tuning and style adaptation
- **Multiple Models**: SD 1.5, SDXL, SD 3.0, Flux support

**Use alternatives instead:**
- **DALL-E 3**: For API-based generation without GPU
- **Midjourney**: For artistic, stylized outputs
- **Imagen**: For Google Cloud integration
- **Leonardo.ai**: For web-based creative workflows

## Quick start

### Installation

```bash
pip install diffusers transformers accelerate torch
pip install xformers  # Optional: memory-efficient attention
```

### Basic text-to-image

```python
from diffusers import DiffusionPipeline
import torch

# Load pipeline (auto-detects model type)
pipe = DiffusionPipeline.from_pretrained(
    "stable-diffusion-v1-5/stable-diffusion-v1-5",
    torch_dtype=torch.float16
)
pipe.to("cuda")

# Generate image
image = pipe(
    "A serene mountain landscape at sunset, highly detailed",
    num_inference_steps=50,
    guidance_scale=7.5
).images[0]

image.save("output.png")
```

### Using SDXL (higher quality)

```python
from diffusers import AutoPipelineForText2Image
import torch

pipe = AutoPipelineForText2Image.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    torch_dtype=torch.float16,
    variant="fp16"
)
pipe.to("cuda")

# Enable memory optimization
pipe.enable_model_cpu_offload()

image = pipe(
    prompt="A futuristic city with flying cars, cinematic lighting",
    height=1024,
    width=1024,
    num_inference_steps=30
).images[0]
```

Moved to `references/concepts.md`: architecture, pipelines and schedulers; load when choosing or swapping a pipeline or scheduler.

## Generation parameters

### Key parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `prompt` | Required | Text description of desired image |
| `negative_prompt` | None | What to avoid in the image |
| `num_inference_steps` | 50 | Denoising steps (more = better quality) |
| `guidance_scale` | 7.5 | Prompt adherence (7-12 typical) |
| `height`, `width` | 512/1024 | Output dimensions (multiples of 8) |
| `generator` | None | Torch generator for reproducibility |
| `num_images_per_prompt` | 1 | Batch size |

### Reproducible generation

```python
import torch

generator = torch.Generator(device="cuda").manual_seed(42)

image = pipe(
    prompt="A cat wearing a top hat",
    generator=generator,
    num_inference_steps=50
).images[0]
```

### Negative prompts

```python
image = pipe(
    prompt="Professional photo of a dog in a garden",
    negative_prompt="blurry, low quality, distorted, ugly, bad anatomy",
    guidance_scale=7.5
).images[0]
```

Moved to `references/image-to-image-controlnet-lora.md`: image-to-image, inpainting, ControlNet and LoRA recipes.

Moved to `references/memory-and-precision.md`: memory optimization, precision variants, custom components, batching.

Moved to `references/workflows-and-issues.md`: end-to-end workflows and common issues.

## References

- **[Advanced Usage](references/advanced-usage.md)** - Custom pipelines, fine-tuning, deployment
- `references/concepts.md`: load when choosing or swapping a pipeline or scheduler
- `references/image-to-image-controlnet-lora.md`: load for img2img, inpainting, ControlNet or LoRA
- `references/memory-and-precision.md`: load for out-of-memory errors, precision choice or batching
- `references/workflows-and-issues.md`: load for end-to-end recipes or quick fixes to common errors
- **[Troubleshooting](references/troubleshooting.md)** - Common issues and solutions

## Resources

- **Documentation**: https://huggingface.co/docs/diffusers
- **Repository**: https://github.com/huggingface/diffusers
- **Model Hub**: https://huggingface.co/models?library=diffusers
- **Discord**: https://discord.gg/diffusers
