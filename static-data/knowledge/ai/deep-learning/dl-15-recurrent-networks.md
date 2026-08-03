---
{
  "title": "Recurrent Neural Networks",
  "description": "Process sequences with a hidden state that carries context through time.",
  "type": "lesson",
  "order": 15,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Explain the recurrent hidden state",
    "Build an RNN cell in PyTorch",
    "Describe backpropagation through time",
    "Know why plain RNNs struggle with long sequences"
  ],
  "knowledge_refs": [
    "deep-learning/dl-14-transfer-learning",
    "reinforcement-learning/rl-09-deep-q-networks",
    "generative-ai/genai-14-gans"
  ],
  "prerequisites": [
    "DL-10: The Training Loop"
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

# DL-15-RECURRENT-NETWORKS: Recurrent Neural Networks

## Introduction

Process sequences with a hidden state that carries context through time. By the end of this lesson you will be able to: Explain the recurrent hidden state; Build an RNN cell in PyTorch; Describe backpropagation through time; Know why plain RNNs struggle with long sequences.

## Key Concepts

### 1. Explain the recurrent hidden state

Target: Explain the recurrent hidden state. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import torch.nn as nn

rnn = nn.RNN(input_size=8, hidden_size=16, batch_first=True)
x = torch.randn(4, 10, 8)   # batch=4, seq=10, feat=8
out, h = rnn(x)
print("outputs:", out.shape, "final hidden:", h.shape)
```
### 2. Build an RNN cell in PyTorch

Target: Build an RNN cell in PyTorch. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import torch

# Hidden state is passed step by step — a rolling memory
h = torch.zeros(1, 4, 16)
for t in range(10):
    _, h = rnn(x[:, t:t+1], h)
print("final hidden after 10 steps:", h.shape)
```
### 3. Describe backpropagation through time

Target: Describe backpropagation through time. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import torch.nn as nn

class SimpleRNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.rnn = nn.RNN(8, 16, batch_first=True)
        self.head = nn.Linear(16, 1)
    def forward(self, x):
        out, _ = self.rnn(x)
        return self.head(out[:, -1])   # use last step
```
### 4. Know why plain RNNs struggle with long sequences

Target: Know why plain RNNs struggle with long sequences. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import torch

# Vanishing gradients: repeated tanh shrinks signal
import math
h = 1.0
for _ in range(20):
    h = math.tanh(h)
print("after 20 steps:", h)
```

## Practice Questions

1. What is the key idea behind "Recurrent Neural Networks"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Recurrent Neural Networks with analogies and real-world examples"
1. "Show me common mistakes beginners make with Recurrent Neural Networks"
1. "Provide advanced patterns and performance considerations for Recurrent Neural Networks"

## Key Takeaways

- Master the core ideas of Recurrent Neural Networks through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
