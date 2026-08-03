---
{
  "title": "Evaluating Deep Learning Models",
  "description": "Accuracy is not enough: confusion matrices, calibration, and failure-case analysis for neural nets.",
  "type": "lesson",
  "order": 20,
  "duration": "50 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Evaluate classifiers with precision/recall per class",
    "Inspect failure cases systematically",
    "Check calibration of probabilities",
    "Track experiments with metrics logging"
  ],
  "knowledge_refs": [
    "deep-learning/dl-20-evaluating-deep-models"
  ],
  "prerequisites": [
    "DL-14: Transfer Learning"
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

# DL-20-EVALUATING-DEEP-MODELS: Evaluating Deep Learning Models

## Introduction

Accuracy is not enough: confusion matrices, calibration, and failure-case analysis for neural nets. By the end of this lesson you will be able to: Evaluate classifiers with precision/recall per class; Inspect failure cases systematically; Check calibration of probabilities; Track experiments with metrics logging.

## Key Concepts

### 1. Evaluate classifiers with precision/recall per class

Target: Evaluate classifiers with precision/recall per class. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from sklearn.metrics import classification_report

import torch
preds = torch.randint(0, 3, (100,))
true = torch.randint(0, 3, (100,))
print(classification_report(true.numpy(), preds.numpy(), target_names=["a", "b", "c"]))
```
### 2. Inspect failure cases systematically

Target: Inspect failure cases systematically. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import torch

# Find the worst failures for human review
probs, idx = torch.topk(torch.rand(50, 10), k=2, dim=-1)
print("top-2 per sample (for error analysis)")
```
### 3. Check calibration of probabilities

Target: Check calibration of probabilities. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
from sklearn.calibration import calibration_curve

print("calibration: bins of predicted prob vs observed freq")
```
### 4. Track experiments with metrics logging

Target: Track experiments with metrics logging. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import torch

# Log everything: each run becomes comparable
run = {"model": "resnet18", "acc": 0.93, "val_loss": 0.31}
print(run)
```

## Practice Questions

1. What is the key idea behind "Evaluating Deep Learning Models"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Evaluating Deep Learning Models with analogies and real-world examples"
1. "Show me common mistakes beginners make with Evaluating Deep Learning Models"
1. "Provide advanced patterns and performance considerations for Evaluating Deep Learning Models"

## Key Takeaways

- Master the core ideas of Evaluating Deep Learning Models through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
