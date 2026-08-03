---
{
  "title": "Sequence Models for Text",
  "description": "Process text as a sequence with RNNs — the pre-transformer era of deep NLP.",
  "type": "lesson",
  "order": 12,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Represent text as sequences of token ids",
    "Build an RNN text classifier",
    "Understand hidden states as context",
    "Know why attention replaced recurrence"
  ],
  "knowledge_refs": [
    "nlp/nlp-12-sequence-models"
  ],
  "prerequisites": [
    "DL-16: LSTM & GRU"
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

# NLP-12-SEQUENCE-MODELS: Sequence Models for Text

## Introduction

Process text as a sequence with RNNs — the pre-transformer era of deep NLP. By the end of this lesson you will be able to: Represent text as sequences of token ids; Build an RNN text classifier; Understand hidden states as context; Know why attention replaced recurrence.

## Key Concepts

### 1. Represent text as sequences of token ids

Target: Represent text as sequences of token ids. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import torch
import torch.nn as nn

class RNNTextClassifier(nn.Module):
    def __init__(self, vocab, emb_dim, hid, n_cls):
        super().__init__()
        self.emb = nn.Embedding(vocab, emb_dim)
        self.rnn = nn.LSTM(emb_dim, hid, batch_first=True)
        self.head = nn.Linear(hid, n_cls)
    def forward(self, ids):
        out, _ = self.rnn(self.emb(ids))
        return self.head(out[:, -1])

print(RNNTextClassifier(1000, 64, 128, 2))
```
### 2. Build an RNN text classifier

Target: Build an RNN text classifier. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import torch

ids = torch.randint(0, 1000, (4, 20))
print("token ids:", ids.shape)
```
### 3. Understand hidden states as context

Target: Understand hidden states as context. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import torch.nn as nn

# Padding makes batches rectangular
pad = nn.utils.rnn.pad_sequence([torch.tensor([1, 2]), torch.tensor([3, 4, 5])], batch_first=True)
print("padded:", pad)
```
### 4. Know why attention replaced recurrence

Target: Know why attention replaced recurrence. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("context carried left-to-right; long-range info fades")
```

## Practice Questions

1. What is the key idea behind "Sequence Models for Text"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Sequence Models for Text with analogies and real-world examples"
1. "Show me common mistakes beginners make with Sequence Models for Text"
1. "Provide advanced patterns and performance considerations for Sequence Models for Text"

## Key Takeaways

- Master the core ideas of Sequence Models for Text through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
