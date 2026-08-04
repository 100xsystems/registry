---
slug: genai-15-vision-language-models
title: "Vision-Language Models"
description: "Multimodal AI that understands both images and text — from CLIP to GPT-4V to LLaVA."
order: 15
tags:
  - generative-ai
  - vision-language
  - clip
  - multimodal
  - llava
  - gpt-4v
prerequisites:
  - genai-13-diffusion-models
  - genai-06-llm-architecture
  - dl-13-cnn-architectures
references:
  - title: "Learning Transferable Visual Models From Natural Language Supervision (CLIP)"
    url: "https://arxiv.org/abs/2103.00020"
    description: "Radford et al.'s CLIP paper — contrastive learning for vision-language"
  - title: "BLIP-2: Bootstrapping Language-Image Pre-training"
    url: "https://arxiv.org/abs/2301.12597"
    description: "Li et al.'s BLIP-2 with Q-Former bridge architecture"
  - title: "Visual Instruction Tuning (LLaVA)"
    url: "https://arxiv.org/abs/2304.08485"
    description: "Liu et al.'s LLaVA paper — visual instruction tuning"
  - title: "Hugging Face BLIP-2 Documentation"
    url: "https://huggingface.co/docs/transformers/en/model_doc/blip-2"
    description: "Practical guide to using BLIP-2 for image understanding"
  - title: "GPT-4V Technical Report (OpenAI)"
    url: "https://arxiv.org/abs/2303.08774"
    description: "OpenAI's GPT-4 technical report covering vision capabilities"
knowledge_refs:
  - genai-06-llm-architecture
  - dl-13-cnn-architectures
  - genai-13-diffusion-models
---

# Vision-Language Models

Vision-Language Models (VLMs) understand both images and text, enabling tasks like image captioning, visual question answering, and multimodal reasoning. They represent the convergence of computer vision and language modeling.

## The Three Architectural Patterns

### 1. Dual Encoders (CLIP)
Separate vision and text encoders trained with contrastive learning:
```
Image → Vision Encoder → Image Embedding ─┐
                                            ├→ Contrastive Loss
Text → Text Encoder → Text Embedding ──────┘
```

**CLIP** (Contrastive Language-Image Pretraining):
- Trained on 400M image-text pairs
- Maps images and text to shared 512-dim embedding space
- Zero-shot classification: match image embeddings to text embeddings

```python
import clip
import torch
from PIL import Image

model, preprocess = clip.load("ViT-B/32")
image = preprocess(Image.open("cat.jpg")).unsqueeze(0)
text = clip.tokenize(["a photo of a cat", "a photo of a dog"])

with torch.no_grad():
    image_features = model.encode_image(image)
    text_features = model.encode_text(text)
    
    similarity = (image_features @ text_features.T).softmax(dim=-1)
    print(similarity)  # ["a photo of a cat": 0.98, "a photo of a dog": 0.02]
```

### 2. Cross-Attention Bridge (BLIP-2, Flamingo)
Frozen vision encoder + frozen LLM, connected by a lightweight bridge:

```
Image → [Frozen Vision Encoder] → Visual Features
                                        ↓
                                [Q-Former / Perceiver]
                                        ↓
Text → [Frozen LLM] ← Cross-Attention ← Visual Tokens
```

**BLIP-2** uses a **Q-Former** (Querying Transformer):
- 12-layer transformer with learnable query tokens
- Extracts visual features from frozen vision encoder
- Aligns visual features to LLM input space
- Only 188M trainable parameters (vs. 7B+ for full model)

### 3. Direct Projection (LLaVA)
Simple linear projection connecting vision and language:

```
Image → [CLIP Vision Encoder] → Visual Tokens
                                      ↓
                               [Linear Projector / MLP]
                                      ↓
Text → [LLM] ← Visual Tokens appended to text tokens
```

**LLaVA** (Large Language and Vision Assistant):
- Connects frozen CLIP-ViT to frozen Vicuna/LLaMA
- Two-stage training: feature alignment → visual instruction tuning
- Simple but effective — showed projection works surprisingly well

## VLM Comparison

| Model | Architecture | Parameters | Key Feature |
|---|---|---|---|
| CLIP | Dual encoder | 400M | Zero-shot classification |
| BLIP-2 | Q-Former bridge | 188M (bridge) | Efficient multimodal |
| LLaVA | Linear projection | ~7B | Visual instruction following |
| GPT-4V | Proprietary | ~1.8T | Best multimodal reasoning |
| Gemini | Native multimodal | ~1.5T | Native multi-modal training |
| Claude 3 | Proprietary | Unknown | Strong image understanding |

## Using Vision-Language Models

### BLIP-2 for Image Captioning
```python
from transformers import Blip2Processor, Blip2ForConditionalGeneration
import torch
from PIL import Image

processor = Blip2Processor.from_pretrained("Salesforce/blip2-opt-2.7b")
model = Blip2ForConditionalGeneration.from_pretrained(
    "Salesforce/blip2-opt-2.7b", torch_dtype=torch.float16
).to("cuda")

image = Image.open("cat.jpg")
inputs = processor(images=image, return_tensors="pt").to("cuda", torch.float16)

generated = model.generate(**inputs, max_new_tokens=50)
print(processor.decode(generated[0], skip_special_tokens=True))
```

### BLIP-2 for Visual Question Answering
```python
prompt = "Question: What color is the cat? Answer:"
inputs = processor(images=image, text=prompt, return_tensors="pt").to("cuda", torch.float16)

generated = model.generate(**inputs, max_new_tokens=10)
print(processor.decode(generated[0], skip_special_tokens=True))
```

### LLaVA for Visual Instruction Following
```python
from llava.model.builder import load_pretrained_model

model, tokenizer = load_pretrained_model("llava-v1.5-7b")
# Process image + instruction together
response = model.generate(image, "Describe this image in detail.")
```

## VLM Capabilities

| Capability | Example |
|---|---|
| **Image captioning** | "A dog playing fetch in a park" |
| **Visual QA** | "What is the man holding?" → "A tennis racket" |
| **OCR** | Read text from images and documents |
| **Chart understanding** | Analyze graphs and data visualizations |
| **Spatial reasoning** | "What is to the left of the red car?" |
| **Document analysis** | Understand layouts, tables, forms |
| **Math from images** | Solve equations shown in photos |

## Training Vision-Language Models

### Stage 1: Feature Alignment
Train the projector/bridge to align visual and language representations:
```python
# Freeze vision encoder and LLM, train only projector
for param in vision_encoder.parameters():
    param.requires_grad = False
for param in llm.parameters():
    param.requires_grad = False

# Train projector on image-caption pairs
for image, caption in alignment_dataset:
    visual_tokens = vision_encoder(image)
    projected = projector(visual_tokens)
    loss = llm(projected, caption)
    loss.backward()
```

### Stage 2: Visual Instruction Tuning
Fine-tune on visual instruction data:
```python
# Unfreeze LLM, keep vision encoder frozen
for param in llm.parameters():
    param.requires_grad = True

# Train on visual QA, captioning, reasoning data
for image, instruction, response in instruction_dataset:
    visual_tokens = projector(vision_encoder(image))
    loss = llm(visual_tokens, instruction, response)
    loss.backward()
```

## Practical Tips

1. **Start with BLIP-2** for quick image understanding tasks
2. **Use LLaVA** for open-source visual instruction following
3. **GPT-4V** for complex visual reasoning (but expensive)
4. **Always resize images** to model's expected resolution
5. **Use system prompts** to control output format

## Further Reading

- CLIP paper established contrastive vision-language learning
- BLIP-2 showed frozen models + lightweight bridges work well
- LLaVA demonstrated visual instruction tuning at scale
- GPT-4V shows the frontier of multimodal capabilities
