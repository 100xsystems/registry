---
{
  "title": "The Perceptron & Linear Units",
  "description": "Start with the neuron: linear combination, threshold, and the step up to learnable weights.",
  "type": "lesson",
  "order": 2,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Describe a perceptron as a weighted sum plus threshold",
    "Implement a perceptron in NumPy",
    "Explain the XOR limitation of a single layer",
    "Motivate multiple layers"
  ],
  "knowledge_refs": [
    "deep-learning/dl-02-perceptron-and-linear-units"
  ],
  "prerequisites": [
    "DL-01: What Is Deep Learning?"
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

# DL-02-PERCEPTRON-AND-LINEAR-UNITS: The Perceptron & Linear Units

## Introduction

Start with the neuron: linear combination, threshold, and the step up to learnable weights. By the end of this lesson you will be able to: Describe a perceptron as a weighted sum plus threshold; Implement a perceptron in NumPy; Explain the XOR limitation of a single layer; Motivate multiple layers.

## Key Concepts

### 1. Describe a perceptron as a weighted sum plus threshold

Target: Describe a perceptron as a weighted sum plus threshold. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import numpy as np

def perceptron(x, w, b):
    return 1 if np.dot(x, w) + b > 0 else 0

w = np.array([1.0, 1.0])
print("AND(1,1):", perceptron([1, 1], w, -1.5))
print("AND(1,0):", perceptron([1, 0], w, -1.5))
```
### 2. Implement a perceptron in NumPy

Target: Implement a perceptron in NumPy. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import numpy as np

# Learning rule for a single neuron
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 0, 0, 1])   # AND
w = np.zeros(2)
b = 0.0
for _ in range(10):
    for xi, yi in zip(X, y):
        pred = 1 if np.dot(xi, w) + b > 0 else 0
        w += (yi - pred) * xi
        b += (yi - pred)
print("learned weights:", w, "bias:", b)
```
### 3. Explain the XOR limitation of a single layer

Target: Explain the XOR limitation of a single layer. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import numpy as np

# XOR is not linearly separable — no single line works
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])
print("XOR needs hidden layers (nonlinearity)")
```
### 4. Motivate multiple layers

Target: Motivate multiple layers. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import numpy as np

# Two-layer XOR solution
w_hidden = np.array([[1.0, 1.0], [1.0, 1.0]])
b_hidden = np.array([-0.5, -1.5])
w_out = np.array([1.0, -2.0])
b_out = 0.0
h = np.maximum(0, X @ w_hidden.T + b_hidden)
out = (h @ w_out + b_out > 0).astype(int)
print("XOR solved:", out)
```

## Practice Questions

1. What is the key idea behind "The Perceptron & Linear Units"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain The Perceptron & Linear Units with analogies and real-world examples"
1. "Show me common mistakes beginners make with The Perceptron & Linear Units"
1. "Provide advanced patterns and performance considerations for The Perceptron & Linear Units"

## Key Takeaways

- Master the core ideas of The Perceptron & Linear Units through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
