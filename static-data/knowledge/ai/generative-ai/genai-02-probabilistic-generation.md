---
{
  "title": "The Mathematics of Generation",
  "description": "Generation is sampling from a probability distribution over tokens — conditioned on context.",
  "type": "lesson",
  "order": 2,
  "duration": "50 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Model text generation as next-token sampling",
    "Explain conditional probability chains",
    "Sample from a categorical distribution",
    "Control randomness with temperature"
  ],
  "knowledge_refs": [
    "generative-ai/genai-02-probabilistic-generation"
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

# GENAI-02-PROBABILISTIC-GENERATION: The Mathematics of Generation

## Introduction

Generation is sampling from a probability distribution over tokens — conditioned on context. By the end of this lesson you will be able to: Model text generation as next-token sampling; Explain conditional probability chains; Sample from a categorical distribution; Control randomness with temperature.

## Key Concepts

### 1. Model text generation as next-token sampling

Target: Model text generation as next-token sampling. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import numpy as np

# Next-token distribution
logits = np.array([2.0, 1.0, 0.1])
probs = np.exp(logits - logits.max())
probs = probs / probs.sum()
print("probs:", probs.round(3))
```
### 2. Explain conditional probability chains

Target: Explain conditional probability chains. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import numpy as np

rng = np.random.default_rng(0)
probs = np.array([0.7, 0.2, 0.1])
token = rng.choice(3, p=probs)
print("sampled token:", token)
```
### 3. Sample from a categorical distribution

Target: Sample from a categorical distribution. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import numpy as np

# P("cat sat") = P("cat") * P("sat" | "cat")
p_cat = 0.2
p_sat_given_cat = 0.5
print("P(cat sat):", p_cat * p_sat_given_cat)
```
### 4. Control randomness with temperature

Target: Control randomness with temperature. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import numpy as np

# Temperature sharpens or flattens the distribution
logits = np.array([2.0, 1.0, 0.1])
for t in [0.2, 1.0, 2.0]:
    p = np.exp(logits / t - (logits / t).max())
    print(f"T={t}: {np.round(p / p.sum(), 3)}")
```

## Practice Questions

1. What is the key idea behind "The Mathematics of Generation"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain The Mathematics of Generation with analogies and real-world examples"
1. "Show me common mistakes beginners make with The Mathematics of Generation"
1. "Provide advanced patterns and performance considerations for The Mathematics of Generation"

## Key Takeaways

- Master the core ideas of The Mathematics of Generation through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
