---
slug: cv-19-vision-transformers
title: "Vision Transformers (ViT)"
description: "Transformers in computer vision — from ViT to DeiT to Swin, challenging CNN dominance."
order: 19
tags:
  - computer-vision
  - vision-transformers
  - vit
  - swin
  - deit
prerequisites:
  - dl-17-transformers
  - cv-06-cnns-for-vision
  - cv-05-image-classification
references:
  - title: "An Image is Worth 16x16 Words (ViT)"
    url: "https://arxiv.org/abs/2010.11929"
    description: "Dosovitskiy et al.'s Vision Transformer paper"
  - title: "Training data-efficient image transformers (DeiT)"
    url: "https://arxiv.org/abs/2012.12877"
    description: "Touvron et al.'s DeiT — training ViT without large datasets"
  - title: "Swin Transformer: Hierarchical Vision Transformer"
    url: "https://arxiv.org/abs/2103.14030"
    description: "Liu et al.'s Swin Transformer with shifted windows"
  - title: "PyTorch ViT Implementation"
    url: "https://pytorch.org/vision/main/models/vision_transformer.html"
    description: "Official PyTorch ViT models"
  - title: "Hugging Face ViT Documentation"
    url: "https://huggingface.co/docs/transformers/model_doc/vit"
    description: "Hugging Face's ViT model documentation"
knowledge_refs:
  - dl-17-transformers
  - cv-06-cnns-for-vision
  - dl-18-attention-mechanisms
---

# Vision Transformers (ViT)

Vision Transformers apply the transformer architecture to images, treating image patches as tokens. They've matched or exceeded CNN performance on many vision tasks.

## How ViT Works

1. **Split image into patches**: 224×224 image → 16×16 = 196 patches of 16×16
2. **Linearly embed patches**: Each patch → d-dimensional vector
3. **Add positional embeddings**: Inject spatial information
4. **Process through transformer layers**: Self-attention + FFN
5. **Classify using [CLS] token**: Aggregate information

```python
import torch
from torchvision import models

# Load pretrained ViT
model = models.vit_b_16(weights=models.ViT_B_16_Weights.IMAGENET1K_V1)

# Input: (B, 3, 224, 224)
output = model(torch.randn(1, 3, 224, 224))
# Output: (B, 1000) — class logits
```

## Patch Embedding

```python
class PatchEmbedding(nn.Module):
    def __init__(self, img_size=224, patch_size=16, in_channels=3, embed_dim=768):
        super().__init__()
        self.num_patches = (img_size // patch_size) ** 2
        self.proj = nn.Conv2d(in_channels, embed_dim, 
                              kernel_size=patch_size, stride=patch_size)
    
    def forward(self, x):
        x = self.proj(x)  # (B, E, H/P, W/P)
        x = x.flatten(2).transpose(1, 2)  # (B, num_patches, E)
        return x
```

## ViT Variants

| Model | Patches | Layers | Dims | Params | Top-1 |
|---|---|---|---|---|---|
| ViT-S/16 | 16×16 | 12 | 384 | 22M | 81% |
| ViT-B/16 | 16×16 | 12 | 768 | 86M | 84% |
| ViT-L/16 | 16×16 | 24 | 1024 | 307M | 85% |
| ViT-H/14 | 14×14 | 32 | 1280 | 632M | 88% |

## DeiT (Data-efficient Image Transformers)

Training ViT without massive datasets:
- Knowledge distillation from CNN teacher
- Strong data augmentation
- Regularization strategies

```python
# DeiT adds a distillation token
# During training: learn from both ground truth and teacher
# During inference: use distillation token for prediction
```

## Swin Transformer

Hierarchical transformer with shifted windows:
- **Window attention**: Local attention within windows (efficient)
- **Shifted windows**: Cross-window connections
- **Multi-scale**: Like FPN — detect objects at different scales

```
Stage 1: 56×56 patches → 96-dim → local attention
Stage 2: 28×28 patches → 192-dim → shifted window attention
Stage 3: 14×14 patches → 384-dim → shifted window attention
Stage 4: 7×7 patches → 768-dim → shifted window attention
```

## CNN vs. ViT

| Aspect | CNN | ViT |
|---|---|---|
|归纳偏置 | 局部性、平移不变性 | 无（需要更多数据） |
| 大数据 | 表现好 | 表现更好 |
| 小数据 | 表现好 | 表现差（需要预训练） |
| 计算 | O(N×K²) | O(N²) — 注意力 |
| 可解释性 | 特征图 | 注意力图 |

## Hybrid Approaches

Combine CNN feature extraction with transformer processing:
```
Image → CNN backbone → Feature maps → Transformer layers → Classification
```

## Practical Tips

1. **Start with ViT-B/16** for most tasks
2. **Use pretrained weights** — ViT needs lots of data
3. **Swin Transformer** for detection/segmentation (multi-scale)
4. **Data augmentation** is critical for ViT training
5. **Learning rate warmup** helps ViT training stability

## Further Reading

- ViT paper proved transformers work for vision
- DeiT showed ViT can be trained without massive data
- Swin Transformer made transformers practical for dense prediction
- For video: ViViT extends ViT to temporal dimension
