---
{
  "title": "Optimizers: SGD, Momentum & Adam",
  "description": "From plain SGD to Adam — how optimizers navigate loss landscapes and converge faster.",
  "type": "lesson",
  "order": 7,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Implement an SGD update step",
    "Explain momentum",
    "Use Adam and understand its adaptive rates",
    "Tune learning rate and weight decay"
  ],
  "knowledge_refs": [
    "deep-learning/dl-07-optimizers"
  ],
  "prerequisites": [
    "DL-05: Backpropagation"
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

# DL-07-OPTIMIZERS: Optimizers: SGD, Momentum & Adam

## Introduction

From plain SGD to Adam — how optimizers navigate loss landscapes and converge faster. By the end of this lesson you will be able to: Implement an SGD update step; Explain momentum; Use Adam and understand its adaptive rates; Tune learning rate and weight decay.

## Key Concepts

### 1. Implement an SGD update step

Target: Implement an SGD update step. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import torch
import torch.nn as nn

param = nn.Parameter(torch.tensor([2.0]))
opt = torch.optim.SGD([param], lr=0.1)
loss = (param - 1.0) ** 2
loss.backward()
opt.step()
print("after step:", param.item())
```
### 2. Explain momentum

Target: Explain momentum. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import torch

param = nn.Parameter(torch.tensor([2.0]))
opt = torch.optim.SGD([param], lr=0.1, momentum=0.9)
for _ in range(5):
    opt.zero_grad()
    ((param - 1.0) ** 2).backward()
    opt.step()
print("with momentum:", round(param.item(), 3))
```
### 3. Use Adam and understand its adaptive rates

Target: Use Adam and understand its adaptive rates. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import torch

param = nn.Parameter(torch.tensor([2.0]))
opt = torch.optim.Adam([param], lr=0.05)
for _ in range(20):
    opt.zero_grad()
    ((param - 1.0) ** 2).backward()
    opt.step()
print("adam converged:", round(param.item(), 3))
```
### 4. Tune learning rate and weight decay

Target: Tune learning rate and weight decay. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import torch
import torch.nn as nn

model = nn.Linear(4, 2)
opt = torch.optim.AdamW(model.parameters(), lr=1e-3, weight_decay=0.01)
print("param groups:", len(opt.param_groups), "| lr:", opt.param_groups[0]["lr"])
```

## Practice Questions

1. What is the key idea behind "Optimizers: SGD, Momentum & Adam"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Optimizers: SGD, Momentum & Adam with analogies and real-world examples"
1. "Show me common mistakes beginners make with Optimizers: SGD, Momentum & Adam"
1. "Provide advanced patterns and performance considerations for Optimizers: SGD, Momentum & Adam"

## Key Takeaways

- Master the core ideas of Optimizers: SGD, Momentum & Adam through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
