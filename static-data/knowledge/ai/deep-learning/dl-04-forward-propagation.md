---
{
  "title": "Forward Propagation",
  "description": "Push data through the network layer by layer and understand the shapes at every step.",
  "type": "lesson",
  "order": 4,
  "duration": "50 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Trace activations through a small network",
    "Write a NumPy forward pass for a 2-layer net",
    "Verify tensor shapes with matrix multiplication rules",
    "Explain the role of the final layer per task"
  ],
  "knowledge_refs": [
    "deep-learning/dl-04-forward-propagation"
  ],
  "prerequisites": [
    "DL-03: Activation Functions"
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

# DL-04-FORWARD-PROPAGATION: Forward Propagation

## Introduction

Push data through the network layer by layer and understand the shapes at every step. By the end of this lesson you will be able to: Trace activations through a small network; Write a NumPy forward pass for a 2-layer net; Verify tensor shapes with matrix multiplication rules; Explain the role of the final layer per task.

## Key Concepts

### 1. Trace activations through a small network

Target: Trace activations through a small network. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import numpy as np

def relu(x):
    return np.maximum(0, x)

X = np.array([[0.5, 0.2]])          # (1, 2)
W1 = np.array([[0.4, -0.2, 0.1], [0.3, 0.1, -0.5]])
b1 = np.array([0.0, 0.0, 0.0])
h = relu(X @ W1 + b1)              # (1, 3)
print("hidden:", h)
```
### 2. Write a NumPy forward pass for a 2-layer net

Target: Write a NumPy forward pass for a 2-layer net. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import numpy as np

W2 = np.array([[0.6], [-0.4], [0.2]])
b2 = np.array([0.0])
out = h @ W2 + b2                  # (1, 1)
print("output:", out)
```
### 3. Verify tensor shapes with matrix multiplication rules

Target: Verify tensor shapes with matrix multiplication rules. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import numpy as np

# Shape checklist
print("X:", X.shape, "W1:", W1.shape, "-> h:", h.shape)
print("W2:", W2.shape, "-> out:", out.shape)
```
### 4. Explain the role of the final layer per task

Target: Explain the role of the final layer per task. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import numpy as np

# Batched forward pass: many examples at once
Xb = np.random.default_rng(0).normal(size=(32, 2))
hb = relu(Xb @ W1 + b1)
print("batched hidden:", hb.shape)
```

## Practice Questions

1. What is the key idea behind "Forward Propagation"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Forward Propagation with analogies and real-world examples"
1. "Show me common mistakes beginners make with Forward Propagation"
1. "Provide advanced patterns and performance considerations for Forward Propagation"

## Key Takeaways

- Master the core ideas of Forward Propagation through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
