---
{
  "title": "Ethical AI & Safety",
  "description": "Bias, privacy, transparency and misuse — the responsibilities that come with generative models.",
  "type": "lesson",
  "order": 19,
  "duration": "50 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Identify bias sources in training data",
    "Explain privacy risks (PII, memorization)",
    "Design for transparency and auditability",
    "Build safeguards against misuse"
  ],
  "knowledge_refs": [
    "generative-ai/genai-19-ethical-ai-and-safety"
  ],
  "prerequisites": [
    "GENAI-01: What Is Generative AI?"
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

# GENAI-19-ETHICAL-AI-AND-SAFETY: Ethical AI & Safety

## Introduction

Bias, privacy, transparency and misuse — the responsibilities that come with generative models. By the end of this lesson you will be able to: Identify bias sources in training data; Explain privacy risks (PII, memorization); Design for transparency and auditability; Build safeguards against misuse.

## Key Concepts

### 1. Identify bias sources in training data

Target: Identify bias sources in training data. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
concerns = {
    "bias": "skewed training data -> skewed outputs",
    "privacy": "models can memorize training data",
    "misuse": "fraud, disinformation, impersonation",
}
print(concerns)
```
### 2. Explain privacy risks (PII, memorization)

Target: Explain privacy risks (PII, memorization). Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import re

# Never log raw PII from prompts
prompt = "my email is john@example.com"
sanitized = re.sub(r"[\w.+-]+@[\w-]+\.[\w.]+", "[EMAIL]", prompt)
print(sanitized)
```
### 3. Design for transparency and auditability

Target: Design for transparency and auditability. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("disclose: tell users when content is AI-generated")
```
### 4. Build safeguards against misuse

Target: Build safeguards against misuse. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
guardrails = ["input filtering", "output moderation", "rate limits", "human review"]
print(guardrails)
```

## Practice Questions

1. What is the key idea behind "Ethical AI & Safety"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Ethical AI & Safety with analogies and real-world examples"
1. "Show me common mistakes beginners make with Ethical AI & Safety"
1. "Provide advanced patterns and performance considerations for Ethical AI & Safety"

## Key Takeaways

- Master the core ideas of Ethical AI & Safety through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
