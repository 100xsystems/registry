---
{
  "title": "The Training Loop",
  "description": "Write the loop that every training run shares: batches, forward, loss, backward, step.",
  "type": "lesson",
  "order": 10,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write a complete training loop",
    "Create DataLoaders with shuffling and batching",
    "Track loss per epoch",
    "Evaluate on a validation set"
  ],
  "knowledge_refs": [
    "deep-learning/dl-10-the-training-loop"
  ],
  "prerequisites": [
    "DL-09: Building an MLP in PyTorch"
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

# DL-10-THE-TRAINING-LOOP: The Training Loop

## Introduction

Write the loop that every training run shares: batches, forward, loss, backward, step. By the end of this lesson you will be able to: Write a complete training loop; Create DataLoaders with shuffling and batching; Track loss per epoch; Evaluate on a validation set.

## Key Concepts

### 1. Write a complete training loop

Target: Write a complete training loop. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset

X = torch.randn(200, 4)
y = torch.randint(0, 2, (200,))
dl = DataLoader(TensorDataset(X, y), batch_size=32, shuffle=True)
print("batches:", len(dl))
```
### 2. Create DataLoaders with shuffling and batching

Target: Create DataLoaders with shuffling and batching. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import torch
import torch.nn as nn

model = nn.Sequential(nn.Linear(4, 8), nn.ReLU(), nn.Linear(8, 2))
opt = torch.optim.Adam(model.parameters(), lr=1e-3)
loss_fn = nn.CrossEntropyLoss()
for epoch in range(3):
    for xb, yb in dl:
        opt.zero_grad()
        loss = loss_fn(model(xb), yb)
        loss.backward()
        opt.step()
    print(f"epoch {epoch}: loss {loss.item():.3f}")
```
### 3. Track loss per epoch

Target: Track loss per epoch. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import torch

# Shuffling matters: keep order from leaking into the model
from torch.utils.data import DataLoader
print("shuffle=True -> unbiased batches")
```
### 4. Evaluate on a validation set

Target: Evaluate on a validation set. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import torch
import torch.nn as nn

# Validation: no_grad + eval mode
model = nn.Sequential(nn.Linear(4, 2))
model.eval()
with torch.no_grad():
    acc = (model(X[:16]).argmax(1) == y[:16]).float().mean()
print("val accuracy:", round(acc.item(), 3))
```

## Practice Questions

1. What is the key idea behind "The Training Loop"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain The Training Loop with analogies and real-world examples"
1. "Show me common mistakes beginners make with The Training Loop"
1. "Provide advanced patterns and performance considerations for The Training Loop"

## Key Takeaways

- Master the core ideas of The Training Loop through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
