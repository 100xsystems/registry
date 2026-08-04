---
slug: genai-13-diffusion-models
title: "Diffusion Models for Images"
description: "The architecture behind Stable Diffusion, DALL-E, and Midjourney — learning to generate images by reversing noise."
order: 13
tags:
  - generative-ai
  - diffusion
  - stable-diffusion
  - ddpm
  - image-generation
prerequisites:
  - genai-01-what-is-generative-ai
  - dl-12-convolutional-networks
references:
  - title: "Denoising Diffusion Probabilistic Models (Ho et al.)"
    url: "https://arxiv.org/abs/2006.11239"
    description: "The foundational DDPM paper from NeurIPS 2020"
  - title: "High-Resolution Image Synthesis with Latent Diffusion Models"
    url: "https://arxiv.org/abs/2112.10752"
    description: "Rombach et al.'s Latent Diffusion paper — the architecture behind Stable Diffusion"
  - title: "Classifier-Free Diffusion Guidance (Ho & Salimans)"
    url: "https://arxiv.org/abs/2207.12598"
    description: "The classifier-free guidance paper enabling text-conditioned generation"
  - title: "The Annotated Diffusion Model (Hugging Face)"
    url: "https://huggingface.co/blog/annotated-diffusion"
    description: "Step-by-step PyTorch implementation of DDPM"
  - title: "Guidance: A Cheat Code for Diffusion Models (Sander Dieleman)"
    url: "https://sander.ai/2022/05/26/guidance.html"
    description: "Deep dive into classifier guidance and classifier-free guidance"
knowledge_refs:
  - dl-12-convolutional-networks
  - dl-06-loss-functions
  - genai-14-gans
---

# Diffusion Models for Images

Diffusion models are the current state-of-the-art for image generation, powering Stable Diffusion, DALL-E 3, and Midjourney. They generate images by learning to reverse a gradual noising process.

## The Core Idea

**Forward process**: Gradually add noise to an image until it becomes pure noise:
$$\mathbf{x}_0 \to \mathbf{x}_1 \to \mathbf{x}_2 \to \ldots \to \mathbf{x}_T \approx \mathcal{N}(0, I)$$

**Reverse process**: Learn to gradually remove noise:
$$\mathbf{x}_T \to \mathbf{x}_{T-1} \to \ldots \to \mathbf{x}_1 \to \mathbf{x}_0$$

The key insight: if you can learn to denoise one step, you can chain denoising steps to generate images from pure noise.

## Denoising Diffusion Probabilistic Models (DDPM)

### Forward Process
Each step adds a small amount of Gaussian noise:
$$q(\mathbf{x}_t | \mathbf{x}_{t-1}) = \mathcal{N}(\mathbf{x}_t; \sqrt{1-\beta_t}\mathbf{x}_{t-1}, \beta_t \mathbf{I})$$

where $\beta_t$ is the noise schedule (typically linear from $10^{-4}$ to $0.02$).

**Nice property**: We can jump directly to any timestep:
$$q(\mathbf{x}_t | \mathbf{x}_0) = \mathcal{N}(\mathbf{x}_t; \sqrt{\bar{\alpha}_t}\mathbf{x}_0, (1-\bar{\alpha}_t)\mathbf{I})$$

### Reverse Process
A neural network (typically a U-Net) predicts the noise at each step:
$$p_\theta(\mathbf{x}_{t-1} | \mathbf{x}_t) = \mathcal{N}(\mathbf{x}_{t-1}; \mu_\theta(\mathbf{x}_t, t), \sigma_t^2 \mathbf{I})$$

### Training Loss
Simplified to predicting the noise:
$$\mathcal{L} = \mathbb{E}_{t, \mathbf{x}_0, \epsilon}\left[\|\epsilon - \epsilon_\theta(\mathbf{x}_t, t)\|^2\right]$$

```python
# Simplified DDPM training loop
for x_batch in dataloader:
    t = torch.randint(0, T, (batch_size,))
    noise = torch.randn_like(x_batch)
    
    # Forward: add noise
    x_t = add_noise(x_batch, noise, t)
    
    # Predict noise
    predicted_noise = model(x_t, t)
    
    # Loss: MSE between actual and predicted noise
    loss = F.mse_loss(predicted_noise, noise)
    loss.backward()
    optimizer.step()
```

## Latent Diffusion Models (Stable Diffusion)

Pixel-space diffusion is computationally expensive. Latent Diffusion Models (LDMs) solve this:

```
Image (512×512×3) 
    ↓ VAE Encoder
Latent (64×64×4) 
    ↓ Diffusion in Latent Space
    ↓ U-Net + Cross-Attention
Latent (64×64×4)
    ↓ VAE Decoder
Image (512×512×3)
```

**Key components:**
1. **VAE Encoder**: Compresses image to latent space (8x smaller)
2. **U-Net**: Denoises in latent space with text conditioning
3. **Text Encoder**: CLIP or T5 encodes text prompts
4. **VAE Decoder**: Reconstructs image from denoised latent

```python
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
image = pipe("A cat playing piano, oil painting").images[0]
```

## Classifier-Free Guidance (CFG)

Controls how closely the image follows the text prompt:
$$\hat{\epsilon}_\theta(\mathbf{x}_t, y) = \epsilon_\theta(\mathbf{x}_t, \emptyset) + w \cdot (\epsilon_\theta(\mathbf{x}_t, y) - \epsilon_\theta(\mathbf{x}_t, \emptyset))$$

where $w$ is the guidance scale:
- $w = 1$: No guidance (unconditional generation)
- $w = 7.5$: Standard (good prompt adherence)
- $w = 15$: Very strong (high fidelity, less diversity)

```python
# Higher guidance = more faithful to prompt
image = pipe("A sunset over mountains", guidance_scale=7.5).images[0]
```

## Sampling Strategies

| Method | Speed | Quality | Steps |
|---|---|---|---|
| DDPM | Slow | High | 1000 |
| DDIM | Medium | High | 50-100 |
| DPM-Solver | Fast | High | 20-30 |
| Euler | Fast | Good | 20-50 |
| LCM | Very fast | Good | 4-8 |

**LCM (Latent Consistency Models)**: Distilled models that generate in 4-8 steps.

## The Stable Diffusion Pipeline

```python
from diffusers import StableDiffusionXLPipeline
import torch

# Load model
pipe = StableDiffusionXLPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    torch_dtype=torch.float16
).to("cuda")

# Generate
image = pipe(
    prompt="A photorealistic cat wearing sunglasses, studio lighting",
    negative_prompt="blurry, low quality, distorted",
    num_inference_steps=30,
    guidance_scale=7.5,
    width=1024,
    height=1024,
).images[0]
```

## Text-to-Image Models

| Model | Architecture | Key Feature |
|---|---|---|
| Stable Diffusion 1.5 | Latent Diffusion | Open source, community |
| Stable Diffusion XL | Latent Diffusion | Higher quality, 1024px |
| DALL-E 3 | Diffusion + CLIP | Best prompt following |
| Midjourney | Diffusion (proprietary) | Best aesthetics |
| Flux | Flow matching | New architecture, fast |

## Image Editing with Diffusion

**Inpainting**: Replace specific regions of an image
**img2img**: Transform an image while keeping structure
**ControlNet**: Guide generation with edge maps, depth maps, poses

```python
from diffusers import StableDiffusionInpaintPipeline

inpaint = StableDiffusionInpaintPipeline.from_pretrained("runwayml/stable-diffusion-inpainting")
result = inpaint(
    prompt="A red sports car",
    image=original_image,
    mask_image=mask  # white = area to replace
).images[0]
```

## Training Your Own Diffusion Model

```python
from diffusers import DDPMPipeline, DDPMScheduler, UNet2DModel

# Define model
model = UNet2DModel(
    sample_size=64,
    in_channels=3,
    out_channels=3,
    layers_per_block=2,
    block_out_channels=(64, 128, 256, 512),
    down_block_types=("DownBlock2D",) * 4,
    up_block_types=("UpBlock2D",) * 4,
)

# Training
noise_scheduler = DDPMScheduler(num_train_timesteps=1000)

for epoch in range(num_epochs):
    for batch in dataloader:
        noise = torch.randn_like(batch)
        timesteps = torch.randint(0, 1000, (batch.shape[0],))
        
        noisy = noise_scheduler.add_noise(batch, noise, timesteps)
        noise_pred = model(noisy, timesteps).sample
        
        loss = F.mse_loss(noise_pred, noise)
        loss.backward()
```

## Further Reading

- Ho et al.'s DDPM paper is the foundational reference
- Rombach et al.'s Latent Diffusion paper explains the Stable Diffusion architecture
- Hugging Face's annotated diffusion model is excellent for implementation
- Sander Dieleman's guidance article is the best explanation of CFG
