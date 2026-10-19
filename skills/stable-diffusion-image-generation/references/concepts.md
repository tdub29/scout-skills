# Architecture and Core Concepts

## Architecture overview

### Three-pillar design

Diffusers is built around three core components:

```
Pipeline (orchestration)
â”œâ”€â”€ Model (neural networks)
â”‚   â”œâ”€â”€ UNet / Transformer (noise prediction)
â”‚   â”œâ”€â”€ VAE (latent encoding/decoding)
â”‚   â””â”€â”€ Text Encoder (CLIP/T5)
â””â”€â”€ Scheduler (denoising algorithm)
```

### Pipeline inference flow

```
Text Prompt â†’ Text Encoder â†’ Text Embeddings
                                    â†“
Random Noise â†’ [Denoising Loop] â† Scheduler
                      â†“
               Predicted Noise
                      â†“
              VAE Decoder â†’ Final Image
```

## Core concepts

### Pipelines

Pipelines orchestrate complete workflows:

| Pipeline | Purpose |
|----------|---------|
| `StableDiffusionPipeline` | Text-to-image (SD 1.x/2.x) |
| `StableDiffusionXLPipeline` | Text-to-image (SDXL) |
| `StableDiffusion3Pipeline` | Text-to-image (SD 3.0) |
| `FluxPipeline` | Text-to-image (Flux models) |
| `StableDiffusionImg2ImgPipeline` | Image-to-image |
| `StableDiffusionInpaintPipeline` | Inpainting |

### Schedulers

Schedulers control the denoising process:

| Scheduler | Steps | Quality | Use Case |
|-----------|-------|---------|----------|
| `EulerDiscreteScheduler` | 20-50 | Good | Default choice |
| `EulerAncestralDiscreteScheduler` | 20-50 | Good | More variation |
| `DPMSolverMultistepScheduler` | 15-25 | Excellent | Fast, high quality |
| `DDIMScheduler` | 50-100 | Good | Deterministic |
| `LCMScheduler` | 4-8 | Good | Very fast |
| `UniPCMultistepScheduler` | 15-25 | Excellent | Fast convergence |

### Swapping schedulers

```python
from diffusers import DPMSolverMultistepScheduler

# Swap for faster generation
pipe.scheduler = DPMSolverMultistepScheduler.from_config(
    pipe.scheduler.config
)

# Now generate with fewer steps
image = pipe(prompt, num_inference_steps=20).images[0]
```
