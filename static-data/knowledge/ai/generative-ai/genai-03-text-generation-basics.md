---
{
  "title": "Text Generation Fundamentals",
  "description": "Generate text with pretrained models: sampling strategies, decoding, and the tokens that come out.",
  "type": "lesson",
  "order": 3,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Run a pretrained generation model",
    "Use greedy and sampling decoding",
    "Apply top-k and top-p (nucleus) sampling",
    "Set generation hyperparameters deliberately"
  ],
  "knowledge_refs": [
    "generative-ai/genai-02-probabilistic-generation",
    "nlp/nlp-03-text-preprocessing",
    "nlp/nlp-12-sequence-models"
  ],
  "prerequisites": [
    "GENAI-02: The Mathematics of Generation"
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

# GENAI-03-TEXT-GENERATION-BASICS: Text Generation Fundamentals

## Introduction

Generate text with pretrained models: sampling strategies, decoding, and the tokens that come out. By the end of this lesson you will be able to: Run a pretrained generation model; Use greedy and sampling decoding; Apply top-k and top-p (nucleus) sampling; Set generation hyperparameters deliberately.

## Key Concepts

### 1. Run a pretrained generation model

Target: Run a pretrained generation model. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from transformers import pipeline

pipe = pipeline("text-generation", model="gpt2")
print(pipe("Once upon a time,", max_new_tokens=20)[0]["generated_text"])
```
### 2. Use greedy and sampling decoding

Target: Use greedy and sampling decoding. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from transformers import pipeline

pipe = pipeline("text-generation", model="gpt2")
out = pipe("The future of AI is", max_new_tokens=15, do_sample=True, temperature=0.9)
print(out[0]["generated_text"])
```
### 3. Apply top-k and top-p (nucleus) sampling

Target: Apply top-k and top-p (nucleus) sampling. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import numpy as np

# Top-k: restrict sampling to the k most likely tokens
probs = np.array([0.5, 0.3, 0.15, 0.05])
k = 2
masked = np.where(np.argsort(probs)[::-1] < k, probs, 0)
print("top-k probs:", masked / masked.sum())
```
### 4. Set generation hyperparameters deliberately

Target: Set generation hyperparameters deliberately. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import numpy as np

# Top-p: keep the smallest set whose cumulative prob >= p
probs = np.array([0.5, 0.3, 0.15, 0.05])
order = np.argsort(probs)[::-1]
keep = np.cumsum(probs[order]) <= 0.8
print("nucleus keeps:", order[keep])
```

## Practice Questions

1. What is the key idea behind "Text Generation Fundamentals"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Text Generation Fundamentals with analogies and real-world examples"
1. "Show me common mistakes beginners make with Text Generation Fundamentals"
1. "Provide advanced patterns and performance considerations for Text Generation Fundamentals"

## Key Takeaways

- Master the core ideas of Text Generation Fundamentals through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
