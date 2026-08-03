---
{
  "title": "PyTorch Tensors & Autograd",
  "description": "The PyTorch fundamentals: tensors, dtypes, devices, and the autograd graph.",
  "type": "lesson",
  "order": 8,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create and manipulate tensors",
    "Move tensors between CPU and GPU",
    "Explain the autograd computation graph",
    "Control gradient tracking with no_grad"
  ],
  "knowledge_refs": [
    "deep-learning/dl-08-pytorch-tensors-and-autograd"
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

# DL-08-PYTORCH-TENSORS-AND-AUTOGRAD: PyTorch Tensors & Autograd

## Introduction

The PyTorch fundamentals: tensors, dtypes, devices, and the autograd graph. By the end of this lesson you will be able to: Create and manipulate tensors; Move tensors between CPU and GPU; Explain the autograd computation graph; Control gradient tracking with no_grad.

## Key Concepts

### 1. Create and manipulate tensors

Target: Create and manipulate tensors. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import torch

x = torch.arange(12).reshape(3, 4)
print(x)
print("dtype:", x.dtype, "device:", x.device)
```
### 2. Move tensors between CPU and GPU

Target: Move tensors between CPU and GPU. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import torch

if torch.cuda.is_available():
    x = torch.ones(3).cuda()
    print("on GPU:", x.device)
else:
    print("CUDA unavailable — CPU only")
```
### 3. Explain the autograd computation graph

Target: Explain the autograd computation graph. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import torch

x = torch.tensor([1.0, 2.0], requires_grad=True)
y = (x ** 2).sum()
y.backward()
print("grads:", x.grad)  # 2 * x
```
### 4. Control gradient tracking with no_grad

Target: Control gradient tracking with no_grad. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import torch

x = torch.randn(1000, 1000, requires_grad=True)
with torch.no_grad():
    y = x * 2   # no graph, fast, no memory
print("requires_grad:", y.requires_grad)
```

## Practice Questions

1. What is the key idea behind "PyTorch Tensors & Autograd"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain PyTorch Tensors & Autograd with analogies and real-world examples"
1. "Show me common mistakes beginners make with PyTorch Tensors & Autograd"
1. "Provide advanced patterns and performance considerations for PyTorch Tensors & Autograd"

## Key Takeaways

- Master the core ideas of PyTorch Tensors & Autograd through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
