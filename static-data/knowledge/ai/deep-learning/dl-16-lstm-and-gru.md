---
{
  "title": "LSTM & GRU",
  "description": "Gated memory cells that actually remember — the fixes that made sequence modeling practical.",
  "type": "lesson",
  "order": 16,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Explain the LSTM cell (forget, input, output gates)",
    "Use nn.LSTM and nn.GRU",
    "Bidirectional processing",
    "Choose RNN variants by task"
  ],
  "knowledge_refs": [
    "deep-learning/dl-15-recurrent-networks",
    "nlp/nlp-13-lstm-for-text",
    "nlp/nlp-12-sequence-models"
  ],
  "prerequisites": [
    "DL-15: Recurrent Neural Networks"
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

# DL-16-LSTM-AND-GRU: LSTM & GRU

## Introduction

Gated memory cells that actually remember — the fixes that made sequence modeling practical. By the end of this lesson you will be able to: Explain the LSTM cell (forget, input, output gates); Use nn.LSTM and nn.GRU; Bidirectional processing; Choose RNN variants by task.

## Key Concepts

### 1. Explain the LSTM cell (forget, input, output gates)

Target: Explain the LSTM cell (forget, input, output gates). Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import torch.nn as nn

lstm = nn.LSTM(input_size=8, hidden_size=32, batch_first=True)
x = torch.randn(4, 12, 8)
out, (h, c) = lstm(x)
print("out:", out.shape, "hidden:", h.shape, "cell:", c.shape)
```
### 2. Use nn.LSTM and nn.GRU

Target: Use nn.LSTM and nn.GRU. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import torch.nn as nn

gru = nn.GRU(input_size=8, hidden_size=32, batch_first=True)
out, h = gru(torch.randn(4, 12, 8))
print("gru out:", out.shape)
```
### 3. Bidirectional processing

Target: Bidirectional processing. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import torch.nn as nn

bi = nn.LSTM(8, 16, bidirectional=True, batch_first=True)
out, _ = bi(torch.randn(4, 12, 8))
print("bidirectional out:", out.shape)  # 2 * hidden
```
### 4. Choose RNN variants by task

Target: Choose RNN variants by task. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import torch.nn as nn

class LSTMClassifier(nn.Module):
    def __init__(self):
        super().__init__()
        self.lstm = nn.LSTM(16, 32, batch_first=True)
        self.head = nn.Linear(32, 2)
    def forward(self, x):
        out, _ = self.lstm(x)
        return self.head(out[:, -1])

print("LSTM classifier ready")
```

## Practice Questions

1. What is the key idea behind "LSTM & GRU"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain LSTM & GRU with analogies and real-world examples"
1. "Show me common mistakes beginners make with LSTM & GRU"
1. "Provide advanced patterns and performance considerations for LSTM & GRU"

## Key Takeaways

- Master the core ideas of LSTM & GRU through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
