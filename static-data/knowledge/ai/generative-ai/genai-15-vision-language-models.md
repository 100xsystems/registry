---
{
  "title": "Vision-Language Models",
  "description": "Bridge images and text: CLIP, captioning, and multimodal chat (LLaVA, GPT-4V).",
  "type": "lesson",
  "order": 15,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Explain contrastive image-text learning (CLIP)",
    "Generate captions with a pretrained VLM",
    "Do zero-shot classification with CLIP",
    "Use multimodal chat models"
  ],
  "knowledge_refs": [
    "generative-ai/genai-15-vision-language-models"
  ],
  "prerequisites": [
    "GENAI-13: Diffusion Models for Images"
  ],
  "references": [
    {
      "title": "Hugging Face NLP Course",
      "url": "https://huggingface.co/learn/nlp-course",
      "description": "Transformers, fine-tuning and LLM fundamentals with hands-on code."
    },
    {
      "title": "OpenAI Documentation",
      "url": "https://platform.openai.com/docs",
      "description": "API reference for GPT models, embeddings and function calling."
    },
    {
      "title": "Attention Is All You Need",
      "url": "https://arxiv.org/abs/1706.03762",
      "description": "The Transformer paper that made generative AI possible."
    },
    {
      "title": "LangChain Documentation",
      "url": "https://python.langchain.com/docs",
      "description": "Frameworks for RAG, agents and LLM applications."
    },
    {
      "title": "DeepLearning.AI Short Courses",
      "url": "https://www.deeplearning.ai/short-courses/",
      "description": "Practical AI courses from industry experts."
    }
  ]
}
---

# GENAI-15-VISION-LANGUAGE-MODELS: Vision-Language Models

## Introduction

Bridge images and text: CLIP, captioning, and multimodal chat (LLaVA, GPT-4V). By the end of this lesson you will be able to: Explain contrastive image-text learning (CLIP); Generate captions with a pretrained VLM; Do zero-shot classification with CLIP; Use multimodal chat models.

## Key Concepts

### 1. Explain contrastive image-text learning (CLIP)

Target: Explain contrastive image-text learning (CLIP). Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import torch

# CLIP aligns image and text embeddings in one space
image_emb = torch.randn(512)
text_emb = torch.randn(512)
sim = torch.nn.functional.cosine_similarity(image_emb, text_emb, dim=0)
print("similarity:", round(sim.item(), 3))
```
### 2. Generate captions with a pretrained VLM

Target: Generate captions with a pretrained VLM. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from transformers import pipeline

captioner = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
print(captioner("photo.png"))
```
### 3. Do zero-shot classification with CLIP

Target: Do zero-shot classification with CLIP. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import torch

# Zero-shot classification: pick the label text with highest similarity
labels = ["a dog", "a cat", "a car"]
scores = torch.rand(3)
print("predicted:", labels[scores.argmax()])
```
### 4. Use multimodal chat models

Target: Use multimodal chat models. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("multimodal chat: images + text in, text out")
```

## Practice Questions

1. What is the key idea behind "Vision-Language Models"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Vision-Language Models with analogies and real-world examples"
1. "Show me common mistakes beginners make with Vision-Language Models"
1. "Provide advanced patterns and performance considerations for Vision-Language Models"

## Key Takeaways

- Master the core ideas of Vision-Language Models through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
