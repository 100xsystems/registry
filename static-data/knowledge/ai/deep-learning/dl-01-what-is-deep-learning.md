---
{
  "title": "What Is Deep Learning?",
  "description": "Why deep learning took over AI: representation learning, scale, and the hardware that made it possible.",
  "type": "lesson",
  "order": 1,
  "duration": "40 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Define deep learning and representation learning",
    "Explain why depth helps learn complex functions",
    "Trace the hardware and data drivers of the deep learning boom",
    "Identify tasks where deep learning excels"
  ],
  "knowledge_refs": [
    "deep-learning/dl-02-perceptron-and-linear-units"
  ],
  "prerequisites": [
    "ML-01: What Is Machine Learning?"
  ],
  "references": [
    {
      "title": "PyTorch Documentation",
      "url": "https://pytorch.org/docs/stable/index.html",
      "description": "The official reference for the deep-learning framework used across this course."
    },
    {
      "title": "Deep Learning — Goodfellow, Bengio & Courville",
      "url": "https://www.deeplearningbook.org/",
      "description": "The canonical textbook on deep learning (free HTML)."
    },
    {
      "title": "Dive into Deep Learning (d2l.ai)",
      "url": "https://d2l.ai/",
      "description": "Interactive deep-learning textbook with code in PyTorch."
    },
    {
      "title": "Practical Deep Learning — fast.ai",
      "url": "https://course.fast.ai/",
      "description": "A top-down course that gets you training models quickly."
    },
    {
      "title": "Attention Is All You Need",
      "url": "https://arxiv.org/abs/1706.03762",
      "description": "The paper that introduced the Transformer architecture."
    }
  ]
}
---

# DL-01-WHAT-IS-DEEP-LEARNING: What Is Deep Learning?

## Introduction

Why deep learning took over AI: representation learning, scale, and the hardware that made it possible. By the end of this lesson you will be able to: Define deep learning and representation learning; Explain why depth helps learn complex functions; Trace the hardware and data drivers of the deep learning boom; Identify tasks where deep learning excels.

## Key Concepts

### 1. Define deep learning and representation learning

Target: Define deep learning and representation learning. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import numpy as np

# A deep net = many simple layers composed
x = np.array([2.0])
w1, b1 = 1.5, 0.1
w2, b2 = 0.8, -0.2
h = np.maximum(0, w1 * x + b1)   # hidden layer + ReLU
out = w2 * h + b2                # output layer
print("output:", out)
```
### 2. Explain why depth helps learn complex functions

Target: Explain why depth helps learn complex functions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
tasks = ["image classification", "speech recognition", "language modeling", "game playing"]
for t in tasks:
    print(f"- deep learning dominates: {t}")
```
### 3. Trace the hardware and data drivers of the deep learning boom

Target: Trace the hardware and data drivers of the deep learning boom. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import numpy as np

# GPUs: thousands of cores, one instruction many data (SIMD)
X = np.random.default_rng(0).normal(size=(1024, 1024))
Y = X @ X.T   # matrix multiply — the heart of neural nets
print("matmul shape:", Y.shape)
```
### 4. Identify tasks where deep learning excels

Target: Identify tasks where deep learning excels. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
def why_deep():
    return {"representation_learning": True, "scale": True, "compute": True}

print(why_deep())
```

## Practice Questions

1. What is the key idea behind "What Is Deep Learning?"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain What Is Deep Learning? with analogies and real-world examples"
1. "Show me common mistakes beginners make with What Is Deep Learning?"
1. "Provide advanced patterns and performance considerations for What Is Deep Learning?"

## Key Takeaways

- Master the core ideas of What Is Deep Learning? through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
