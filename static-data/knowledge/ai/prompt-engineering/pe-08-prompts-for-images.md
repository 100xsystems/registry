---
{
  "title": "Prompting for Images",
  "description": "Text-to-image prompting: composition, style, lighting and negative prompts.",
  "type": "lesson",
  "order": 8,
  "duration": "50 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Describe subjects and composition clearly",
    "Control style, lighting and mood",
    "Use negative prompts",
    "Iterate with seeds and variations"
  ],
  "knowledge_refs": [
    "prompt-engineering/pe-08-prompts-for-images"
  ],
  "prerequisites": [
    "GENAI-13: Diffusion Models for Images"
  ],
  "references": [
    {
      "title": "OpenAI Prompt Engineering Guide",
      "url": "https://platform.openai.com/docs/guides/prompt-engineering",
      "description": "Six strategies for reliable prompting from OpenAI."
    },
    {
      "title": "Anthropic Prompt Engineering Docs",
      "url": "https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering",
      "description": "Claude's practical prompt engineering guide."
    },
    {
      "title": "Prompt Engineering Guide (DAIR.AI)",
      "url": "https://www.promptingguide.ai/",
      "description": "A broad open-source guide to prompt techniques."
    },
    {
      "title": "CoT: Chain-of-Thought Prompting",
      "url": "https://arxiv.org/abs/2201.11903",
      "description": "The paper on reasoning via chain-of-thought prompts."
    },
    {
      "title": "ReAct: Reasoning + Acting",
      "url": "https://arxiv.org/abs/2210.03629",
      "description": "Combining reasoning traces with tool actions."
    }
  ]
}
---

# PE-08-PROMPTS-FOR-IMAGES: Prompting for Images

## Introduction

Text-to-image prompting: composition, style, lighting and negative prompts. By the end of this lesson you will be able to: Describe subjects and composition clearly; Control style, lighting and mood; Use negative prompts; Iterate with seeds and variations.

## Key Concepts

### 1. Describe subjects and composition clearly

Target: Describe subjects and composition clearly. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
prompt = "a cozy mountain cabin at dusk, warm window light, photorealistic, wide shot"
print(prompt)
```
### 2. Control style, lighting and mood

Target: Control style, lighting and mood. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
negative = "blurry, low quality, extra limbs, watermark"
print("negative prompt:", negative)
```
### 3. Use negative prompts

Target: Use negative prompts. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("order matters: subject -> setting -> style -> quality")
```
### 4. Iterate with seeds and variations

Target: Iterate with seeds and variations. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
print("pipeline ready")
```

## Practice Questions

1. What is the key idea behind "Prompting for Images"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Prompting for Images with analogies and real-world examples"
1. "Show me common mistakes beginners make with Prompting for Images"
1. "Provide advanced patterns and performance considerations for Prompting for Images"

## Key Takeaways

- Master the core ideas of Prompting for Images through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
