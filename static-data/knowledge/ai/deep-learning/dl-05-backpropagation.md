---
{
  "title": "Backpropagation",
  "description": "The chain rule in action: propagate errors backward to compute gradients for every weight.",
  "type": "lesson",
  "order": 5,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Explain the chain rule as gradient routing",
    "Derive the local gradients for common layers",
    "Implement backprop for a 2-layer net",
    "Use autograd instead of hand-written derivatives"
  ],
  "knowledge_refs": [
    "deep-learning/dl-04-forward-propagation"
  ],
  "prerequisites": [
    "DL-04: Forward Propagation"
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

# DL-05-BACKPROPAGATION: Backpropagation

## Introduction

The chain rule in action: propagate errors backward to compute gradients for every weight. By the end of this lesson you will be able to: Explain the chain rule as gradient routing; Derive the local gradients for common layers; Implement backprop for a 2-layer net; Use autograd instead of hand-written derivatives.

## Key Concepts

### 1. Explain the chain rule as gradient routing

Target: Explain the chain rule as gradient routing. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import numpy as np

# Chain rule: dL/dw = dL/dy * dy/dh * dh/dw
x = np.array([1.0])
y_true = np.array([0.0])
w = np.array([0.5])
y_pred = w * x
loss = 0.5 * (y_pred - y_true) ** 2
dL_dy = y_pred - y_true
dL_dw = dL_dy * x
print("gradient:", dL_dw)
```
### 2. Derive the local gradients for common layers

Target: Derive the local gradients for common layers. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import numpy as np

# Full 2-layer backprop (regression)
X = np.array([[0.2, 0.5]])
y = np.array([[0.8]])
W1 = np.random.default_rng(0).normal(size=(2, 3)) * 0.5
W2 = np.random.default_rng(1).normal(size=(3, 1)) * 0.5
h = np.maximum(0, X @ W1)
out = h @ W2
dL_dout = out - y
dL_dW2 = h.T @ dL_dout
dL_dh = dL_dout @ W2.T
dL_dW1 = X.T @ (dL_dh * (h > 0))
print("dW2:", dL_dW2.ravel().round(3))
print("dW1:", dL_dW1.round(3))
```
### 3. Implement backprop for a 2-layer net

Target: Implement backprop for a 2-layer net. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import torch

# Autograd does the chain rule for you
w = torch.tensor([0.5], requires_grad=True)
x = torch.tensor([1.0])
y = torch.tensor([0.0])
loss = 0.5 * (w * x - y) ** 2
loss.backward()
print("autograd dL/dw:", w.grad)
```
### 4. Use autograd instead of hand-written derivatives

Target: Use autograd instead of hand-written derivatives. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import torch

x = torch.randn(4, 2, requires_grad=True)
y = (x ** 2).sum()
y.backward()
print("grad shape:", x.grad.shape)
```

## Practice Questions

1. What is the key idea behind "Backpropagation"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Backpropagation with analogies and real-world examples"
1. "Show me common mistakes beginners make with Backpropagation"
1. "Provide advanced patterns and performance considerations for Backpropagation"

## Key Takeaways

- Master the core ideas of Backpropagation through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
