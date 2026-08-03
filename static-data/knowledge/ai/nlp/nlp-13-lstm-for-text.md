---
{
  "title": "LSTMs for Text",
  "description": "Gated memory for language: LSTMs and GRUs that actually hold context over long sequences.",
  "type": "lesson",
  "order": 13,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use LSTM cells for text modeling",
    "Bidirectional context",
    "Train an LSTM classifier",
    "Understand the limits that transformers fixed"
  ],
  "knowledge_refs": [
    "nlp/nlp-12-sequence-models",
    "deep-learning/dl-16-lstm-and-gru",
    "deep-learning/dl-15-recurrent-networks"
  ],
  "prerequisites": [
    "NLP-12: Sequence Models for Text"
  ],
  "references": [
    {
      "title": "Hugging Face NLP Course",
      "url": "https://huggingface.co/learn/nlp-course",
      "description": "The hands-on course for transformers and modern NLP."
    },
    {
      "title": "Speech and Language Processing — Jurafsky & Martin",
      "url": "https://web.stanford.edu/~jurafsky/slp3/",
      "description": "The standard textbook for NLP (free draft)."
    },
    {
      "title": "Stanford CS224n",
      "url": "https://web.stanford.edu/class/cs224n/",
      "description": "Natural Language Processing with Deep Learning."
    },
    {
      "title": "NLTK Book",
      "url": "https://www.nltk.org/book/",
      "description": "Natural Language Processing with Python — classic fundamentals."
    },
    {
      "title": "spaCy Documentation",
      "url": "https://spacy.io/usage",
      "description": "Industrial-strength NLP library docs."
    }
  ]
}
---

# NLP-13-LSTM-FOR-TEXT: LSTMs for Text

## Introduction

Gated memory for language: LSTMs and GRUs that actually hold context over long sequences. By the end of this lesson you will be able to: Use LSTM cells for text modeling; Bidirectional context; Train an LSTM classifier; Understand the limits that transformers fixed.

## Key Concepts

### 1. Use LSTM cells for text modeling

Target: Use LSTM cells for text modeling. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import torch.nn as nn

lstm = nn.LSTM(64, 128, num_layers=2, batch_first=True)
print("2-layer LSTM")
```
### 2. Bidirectional context

Target: Bidirectional context. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import torch.nn as nn

bi = nn.LSTM(64, 128, bidirectional=True, batch_first=True)
out, _ = bi(torch.randn(4, 20, 64))
print("bidirectional out:", out.shape)
```
### 3. Train an LSTM classifier

Target: Train an LSTM classifier. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import torch

# Packing sequences skips padding for speed/correctness
print("pack_padded_sequence handles variable lengths")
```
### 4. Understand the limits that transformers fixed

Target: Understand the limits that transformers fixed. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import torch.nn as nn

class LSTMAgent(nn.Module):
    def __init__(self):
        super().__init__()
        self.emb = nn.Embedding(500, 64)
        self.lstm = nn.LSTM(64, 128, batch_first=True)
        self.head = nn.Linear(128, 500)
    def forward(self, ids):
        out, _ = self.lstm(self.emb(ids))
        return self.head(out)

print("next-token LSTM ready")
```

## Practice Questions

1. What is the key idea behind "LSTMs for Text"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain LSTMs for Text with analogies and real-world examples"
1. "Show me common mistakes beginners make with LSTMs for Text"
1. "Provide advanced patterns and performance considerations for LSTMs for Text"

## Key Takeaways

- Master the core ideas of LSTMs for Text through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
