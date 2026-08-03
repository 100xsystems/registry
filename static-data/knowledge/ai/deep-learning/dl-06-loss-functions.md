---
{
  "title": "Loss Functions",
  "description": "Pick the right objective: MSE for regression, cross-entropy for classification, and why it matters.",
  "type": "lesson",
  "order": 6,
  "duration": "50 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Compute MSE and MAE for regression",
    "Explain cross-entropy for classification",
    "Understand why cross-entropy pairs with softmax",
    "Handle class imbalance in the loss"
  ],
  "knowledge_refs": [
    "deep-learning/dl-05-backpropagation"
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

# DL-06-LOSS-FUNCTIONS: Loss Functions

## Introduction

Pick the right objective: MSE for regression, cross-entropy for classification, and why it matters. By the end of this lesson you will be able to: Compute MSE and MAE for regression; Explain cross-entropy for classification; Understand why cross-entropy pairs with softmax; Handle class imbalance in the loss.

## Key Concepts

### 1. Compute MSE and MAE for regression

Target: Compute MSE and MAE for regression. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import torch
import torch.nn.functional as F

pred = torch.tensor([2.5, 0.0, 2.0])
target = torch.tensor([2.0, 0.0, 2.0])
print("MSE:", F.mse_loss(pred, target))
```
### 2. Explain cross-entropy for classification

Target: Explain cross-entropy for classification. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import torch
import torch.nn.functional as F

logits = torch.tensor([[2.0, 1.0, 0.1]])
target = torch.tensor([0])
print("CE:", F.cross_entropy(logits, target))
```
### 3. Understand why cross-entropy pairs with softmax

Target: Understand why cross-entropy pairs with softmax. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import torch
import torch.nn.functional as F

# Why cross-entropy: log softmax is numerically stable
logits = torch.tensor([[1000.0, 0.0]])
print("stable probs:", torch.softmax(logits, dim=-1))
```
### 4. Handle class imbalance in the loss

Target: Handle class imbalance in the loss. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import torch
import torch.nn.functional as F

# Class weights push the model to care about rare classes
logits = torch.tensor([[1.0, -1.0]])
target = torch.tensor([1])
print("weighted CE:", F.cross_entropy(logits, target, weight=torch.tensor([1.0, 5.0])))
```

## Practice Questions

1. What is the key idea behind "Loss Functions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Loss Functions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Loss Functions"
1. "Provide advanced patterns and performance considerations for Loss Functions"

## Key Takeaways

- Master the core ideas of Loss Functions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
