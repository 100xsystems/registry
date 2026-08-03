---
{
  "title": "What Is Generative AI?",
  "description": "The field that creates text, images, audio and code — and the system stack behind it.",
  "type": "lesson",
  "order": 1,
  "duration": "40 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Define generative AI and contrast it with discriminative models",
    "List the modalities generative models create",
    "Describe the modern GenAI stack",
    "Identify risks and opportunities in production"
  ],
  "knowledge_refs": [
    "generative-ai/genai-02-probabilistic-generation"
  ],
  "prerequisites": [
    "DL-17: Transformers"
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

# GENAI-01-WHAT-IS-GENERATIVE-AI: What Is Generative AI?

## Introduction

The field that creates text, images, audio and code — and the system stack behind it. By the end of this lesson you will be able to: Define generative AI and contrast it with discriminative models; List the modalities generative models create; Describe the modern GenAI stack; Identify risks and opportunities in production.

## Key Concepts

### 1. Define generative AI and contrast it with discriminative models

Target: Define generative AI and contrast it with discriminative models. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
modalities = {
    "text": "LLMs",
    "image": "diffusion, GANs",
    "audio": "TTS, music",
    "code": "code models",
    "video": "diffusion",
}
for m, tech in modalities.items():
    print(f"{m:8} -> {tech}")
```
### 2. List the modalities generative models create

Target: List the modalities generative models create. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
stack = ["models", "prompt layer", "retrieval", "guardrails", "apps"]
for layer in stack:
    print(f"- {layer}")
```
### 3. Describe the modern GenAI stack

Target: Describe the modern GenAI stack. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("discriminative: P(label | x). generative: P(x)")
```
### 4. Identify risks and opportunities in production

Target: Identify risks and opportunities in production. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
risks = ["hallucination", "bias", "prompt injection", "misuse"]
for r in risks:
    print(f"- {r}")
```

## Practice Questions

1. What is the key idea behind "What Is Generative AI?"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain What Is Generative AI? with analogies and real-world examples"
1. "Show me common mistakes beginners make with What Is Generative AI?"
1. "Provide advanced patterns and performance considerations for What Is Generative AI?"

## Key Takeaways

- Master the core ideas of What Is Generative AI? through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
