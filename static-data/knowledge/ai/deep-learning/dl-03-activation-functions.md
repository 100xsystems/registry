---
{
  "title": "Activation Functions",
  "description": "Nonlinearity is what makes deep networks expressive — sigmoid, tanh, ReLU and friends.",
  "type": "lesson",
  "order": 3,
  "duration": "50 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Explain why activation functions must be nonlinear",
    "Compare sigmoid, tanh and ReLU",
    "Understand the dying-ReLU problem",
    "Pick activations for hidden versus output layers"
  ],
  "knowledge_refs": [
    "deep-learning/dl-02-perceptron-and-linear-units"
  ],
  "prerequisites": [
    "DL-02: The Perceptron & Linear Units"
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

# DL-03-ACTIVATION-FUNCTIONS: Activation Functions

## Introduction

Nonlinearity is what makes deep networks expressive — sigmoid, tanh, ReLU and friends. By the end of this lesson you will be able to: Explain why activation functions must be nonlinear; Compare sigmoid, tanh and ReLU; Understand the dying-ReLU problem; Pick activations for hidden versus output layers.

## Key Concepts

### 1. Explain why activation functions must be nonlinear

Target: Explain why activation functions must be nonlinear. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import numpy as np

z = np.linspace(-5, 5, 5)
print("sigmoid:", np.round(1 / (1 + np.exp(-z)), 3))
print("tanh:", np.round(np.tanh(z), 3))
print("relu:", np.round(np.maximum(0, z), 3))
```
### 2. Compare sigmoid, tanh and ReLU

Target: Compare sigmoid, tanh and ReLU. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import numpy as np

# ReLU sparsity: negative inputs become exactly zero
z = np.array([-2.0, -0.5, 0.0, 1.0, 3.0])
print(np.maximum(0, z))
```
### 3. Understand the dying-ReLU problem

Target: Understand the dying-ReLU problem. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import numpy as np

# Dying ReLU: a large negative bias can kill a unit forever
z = np.array([-100.0, -99.0])
print("outputs:", np.maximum(0, z))  # gradient will be 0 too
```
### 4. Pick activations for hidden versus output layers

Target: Pick activations for hidden versus output layers. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import numpy as np

# Output activations: softmax for classification
logits = np.array([2.0, 1.0, 0.1])
exp = np.exp(logits - logits.max())
probs = exp / exp.sum()
print("softmax:", probs.round(3))
```

## Practice Questions

1. What is the key idea behind "Activation Functions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Activation Functions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Activation Functions"
1. "Provide advanced patterns and performance considerations for Activation Functions"

## Key Takeaways

- Master the core ideas of Activation Functions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
