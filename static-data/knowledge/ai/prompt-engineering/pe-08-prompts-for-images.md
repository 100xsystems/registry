---
slug: pe-08-prompts-for-images
title: "Prompting for Images"
description: "Crafting effective prompts for DALL-E, Stable Diffusion, and Midjourney — from basic composition to advanced style control."
order: 8
tags:
  - prompt-engineering
  - image-generation
  - dall-e
  - stable-diffusion
  - midjourney
prerequisites:
  - pe-02-prompt-structure
knowledge_refs:
  - pe-02-prompt-structure
    title: "Prompt Structure"
  - pe-17-domain-specific-prompts
    title: "Domain-Specific Prompting"
  - genai-13-diffusion-models
    title: "Diffusion Models"
references:
  - title: "Civitai — Prompt Crafting Guide: Part 1 — Basics"
    url: "https://education.civitai.com/civitais-prompt-crafting-guide-part-1-basics/"
  - title: "Portkey — Prompt Engineering for Stable Diffusion"
    url: "https://portkey.ai/blog/prompt-engineering-for-stable-diffusion/"
  - title: "Learn Prompting — DALL-E 3"
    url: "https://learnprompting.org/docs/models/dalle_3"
  - title: "Midjourney — Prompt Basics"
    url: "https://docs.midjourney.com/hc/en-us/articles/32023408776205-Prompt-Basics"
  - title: "Midjourney — Image Prompts"
    url: "https://docs.midjourney.com/hc/en-us/articles/32040250122381-Image-Prompts"
---

## Prompting for Images

Image generation models (DALL-E, Stable Diffusion, Midjourney) each have different prompt styles, but share core principles: specificity, structure, and control over composition, style, and lighting.

### DALL-E: Natural Language Prompts

DALL-E 3 uses an integrated LLM to preprocess your prompt. It automatically expands brief inputs into detailed synthetic captions. This means you should write in **natural language sentences**, not keyword lists.

**Good:** "A fluffy orange cat sits on a rainy windowsill, illuminated by neon pink storefront signs reflecting off puddles outside"

**Bad:** "cat, neon, 8k, cyberpunk, photorealistic"

DALL-E handles complex scene descriptions, spatial relationships, and text rendering. It's the most "conversational" of the image models.

### Stable Diffusion: Token-Based Prompting

Stable Diffusion parses text through CLIP tokenizers. This creates specific requirements:

**Structure your prompt in blocks:**
```
[Subject & Appearance] + [Medium & Style] + [Color & Lighting] + [Composition & Atmosphere]
```

Example: `a cyberpunk samurai standing in neon-lit rain, concept art, dramatic rim lighting, cinematic wide-angle shot`

**Weighting syntax:** Use parentheses to control emphasis:
- `(keyword:1.3)` — increase attention by 30%
- `[keyword]` — decrease emphasis
- `((keyword))` — double emphasis

**Negative prompts** are essential in Stable Diffusion to avoid common artifacts:
```
Negative: lowres, bad anatomy, bad hands, text, error, 
missing fingers, extra digits, worst quality, low quality, 
jpeg artifacts, signature, watermark, blurry
```

### Midjourney: Parameter-Driven

Midjourney uses text prompts with modular parameter suffixes:
- `--ar 16:9` — aspect ratio
- `--v 6.0` — model version
- `--stylize 750` — artistic interpretation (0–1000)
- `--chaos 30` — variation between results

Midjourney is more artistically interpretive than DALL-E or Stable Diffusion. It excels at atmospheric, stylized imagery.

### Universal Principles

Regardless of the model:

1. **Lead with the subject.** Start with what you want to see, not adjectives.
2. **Be specific about style.** "Concept art" vs. "watercolor" vs. "photograph" dramatically changes output.
3. **Control composition.** "Close-up portrait" vs. "wide landscape" vs. "bird's-eye view" directs the camera.
4. **Use reference images** when available. Image-to-image guidance is more reliable than text alone for exact matches.
5. **Iterate quickly.** Generate 4 variations, pick the best, refine the prompt, repeat.

---

*Continue to learn about prompting for RAG systems — grounding LLM responses in retrieved context.*
