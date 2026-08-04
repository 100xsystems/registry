---
slug: genai-14-gans
title: "Generative Adversarial Networks"
description: "The original generative deep learning architecture — two neural networks competing to create realistic content."
order: 14
tags:
  - generative-ai
  - gans
  - dcgan
  - stylegan
  - cyclegan
prerequisites:
  - genai-01-what-is-generative-ai
  - dl-12-convolutional-networks
  - dl-07-optimizers
references:
  - title: "Generative Adversarial Networks (Goodfellow et al., 2014)"
    url: "https://arxiv.org/abs/1406.2661"
    description: "The original GAN paper by Ian Goodfellow"
  - title: "Unsupervised Representation Learning with DCGAN"
    url: "https://arxiv.org/abs/1511.06434"
    description: "Radford et al.'s DCGAN paper establishing best practices for GAN architectures"
  - title: "A Style-Based Generator Architecture for GANs (StyleGAN)"
    url: "https://arxiv.org/abs/1812.04948"
    description: "NVIDIA's StyleGAN paper for high-quality face generation"
  - title: "Unpaired Image-to-Image Translation (CycleGAN)"
    url: "https://arxiv.org/abs/1703.10593"
    description: "Zhu et al.'s CycleGAN for unpaired image translation"
  - title: "Deep Convolutional GAN Tutorial (TensorFlow)"
    url: "https://www.tensorflow.org/tutorials/generative/dcgan"
    description: "Hands-on implementation of DCGAN on MNIST"
knowledge_refs:
  - dl-12-convolutional-networks
  - dl-06-loss-functions
  - genai-13-diffusion-models
---

# Generative Adversarial Networks

GANs (Goodfellow et al., 2014) revolutionized generative modeling by framing generation as a competition between two neural networks. Though largely superseded by diffusion models for images, GANs remain important for real-time generation and style transfer.

## The GAN Framework

Two networks compete in a zero-sum game:

**Generator ($G$)**: Creates fake images from random noise
**Discriminator ($D$)**: Distinguishes real from fake images

$$\min_G \max_D V(D, G) = \mathbb{E}_{x \sim p_{data}}[\log D(x)] + \mathbb{E}_{z \sim p_z}[\log(1 - D(G(z)))]$$

**Training process:**
1. Train $D$ to correctly classify real vs. fake
2. Train $G$ to fool $D$
3. Repeat until $D(x) = 0.5$ for all $x$ (equilibrium)

```python
import torch.nn as nn

class Generator(nn.Module):
    def __init__(self, latent_dim=100, img_shape=(1, 28, 28)):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(latent_dim, 128),
            nn.LeakyReLU(0.2),
            nn.Linear(128, 256),
            nn.BatchNorm1d(256),
            nn.LeakyReLU(0.2),
            nn.Linear(256, 512),
            nn.BatchNorm1d(512),
            nn.LeakyReLU(0.2),
            nn.Linear(512, int(torch.prod(torch.tensor(img_shape)))),
            nn.Tanh()
        )
    
    def forward(self, z):
        return self.model(z).view(-1, *img_shape)

class Discriminator(nn.Module):
    def __init__(self, img_shape=(1, 28, 28)):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(int(torch.prod(torch.tensor(img_shape))), 512),
            nn.LeakyReLU(0.2),
            nn.Linear(512, 256),
            nn.LeakyReLU(0.2),
            nn.Linear(256, 1),
            nn.Sigmoid()
        )
    
    def forward(self, img):
        return self.model(img.view(img.size(0), -1))
```

## Training Dynamics

### The Minimax Game
- $G$ improves at generating fakes → $D$ gets harder task
- $D$ improves at detection → $G$ must generate better fakes
- **Equilibrium**: $D(x) = 0.5$ for all $x$ (can't distinguish)

### Common Failure Modes

**Mode Collapse**: Generator produces only a few types of outputs:
```
Expected: diverse images of cats, dogs, birds
Actual:   only identical-looking cats
```

**Vanishing Gradients**: If $D$ is too strong, $G$ receives no useful gradient:
- $\log(1 - D(G(z)))$ saturates near 0
- $G$ can't improve

**Training Instability**: $G$ and $D$ oscillate instead of converging

### Solutions
- **Wasserstein GAN (WGAN)**: Uses Earth Mover's distance instead of JS divergence
- **Spectral Normalization**: Stabilizes discriminator training
- **Progressive Growing**: Start with low-resolution, gradually increase
- **Two Time-Scale Update Rule**: Different learning rates for $G$ and $D$

## DCGAN (Deep Convolutional GAN)

The first stable convolutional GAN architecture:
- Replace pooling with strided convolutions (discriminator) and transposed convolutions (generator)
- Use batch normalization in both networks
- Use ReLU (generator) and LeakyReLU (discriminator)
- Remove fully connected layers

```python
class DCGANGenerator(nn.Module):
    def __init__(self, latent_dim=100, channels=3):
        super().__init__()
        self.main = nn.Sequential(
            nn.ConvTranspose2d(latent_dim, 512, 4, 1, 0, bias=False),
            nn.BatchNorm2d(512), nn.ReLU(True),
            nn.ConvTranspose2d(512, 256, 4, 2, 1, bias=False),
            nn.BatchNorm2d(256), nn.ReLU(True),
            nn.ConvTranspose2d(256, 128, 4, 2, 1, bias=False),
            nn.BatchNorm2d(128), nn.ReLU(True),
            nn.ConvTranspose2d(128, channels, 4, 2, 1, bias=False),
            nn.Tanh()
        )
    
    def forward(self, z):
        return self.main(z.view(-1, 100, 1, 1))
```

## StyleGAN (NVIDIA)

StyleGAN generates photorealistic faces by controlling style at multiple scales:

```
Latent z → Mapping Network (8 FC layers) → W (style vector)
    ↓
Synthesis Network:
  4×4: W controls coarse style (pose, face shape)
  8×8: W controls medium style (facial features)
  ...
  1024×1024: W controls fine style (skin texture, hair)
```

**Key innovations:**
- **Mapping Network**: Disentangles latent space
- **AdaIN**: Injects style at each layer
- **Stochastic noise**: Adds randomness per-pixel

**Results**: Indistinguishable from real faces. Generated celebrity faces that don't exist.

## CycleGAN (Unpaired Translation)

Translates between domains without paired examples:
```
Horse → Zebra → Horse (cycle consistency)
Summer → Winter → Summer (cycle consistency)
```

**Two losses:**
1. **Adversarial loss**: $G_{h2z}$ should fool $D_{zebra}$
2. **Cycle consistency loss**: $G_{z2h}(G_{h2z}(x)) \approx x$

```python
# Cycle consistency loss
loss_cycle = F.l1_loss(G_z2h(G_h2z(real_horse)), real_horse)
```

**Applications**: Photo → painting, day → night, horse ↔ zebra, apple ↔ orange

## GAN Variants

| Variant | Innovation | Use Case |
|---|---|---|
| DCGAN | Convolutional architecture | Stable training |
| WGAN | Wasserstein distance | Better convergence |
| StyleGAN | Style-based generator | Photorealistic faces |
| CycleGAN | Cycle consistency | Unpaired translation |
| Pix2Pix | Paired translation | Image-to-image |
| ProGAN | Progressive growing | High-resolution |
| BigGAN | Large-scale training | Class-conditional generation |
| SPADE | Spatially-adaptive denormalization | Semantic image synthesis |

## GANs vs. Diffusion Models

| Aspect | GANs | Diffusion |
|---|---|---|
| Speed | Fast (1 forward pass) | Slow (20-1000 steps) |
| Quality | Very high (StyleGAN) | State-of-the-art |
| Diversity | Prone to mode collapse | High diversity |
| Training | Difficult, unstable | Stable, predictable |
| Control | Limited conditioning | Excellent (CFG) |
| Real-time | ✅ Yes | ❌ Too slow |

**When to use GANs**: Real-time applications, video generation, style transfer where speed matters.

## Practical Tips

1. **Start with WGAN-GP** — more stable than vanilla GAN
2. **Use spectral normalization** on discriminator
3. **Monitor both G and D losses** — they should balance
4. **Evaluate with FID** (Fréchet Inception Distance) — lower is better
5. **Save G regularly** — training can collapse suddenly

## Further Reading

- Goodfellow et al.'s original GAN paper is a must-read
- DCGAN established practical best practices
- StyleGAN showed GANs can generate photorealistic faces
- CycleGAN enabled unpaired image translation
- For modern GAN training: StyleGAN2 and StyleGAN3 improved stability
