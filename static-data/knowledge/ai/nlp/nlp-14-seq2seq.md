---
{
  "title": "Seq2Seq Models & Machine Translation",
  "description": "Encoder-decoder architectures that map one sequence to another — the basis of translation.",
  "type": "lesson",
  "order": 14,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Explain the encoder-decoder split",
    "Decode with greedy and beam search",
    "Use teacher forcing in training",
    "Describe how attention improved seq2seq"
  ],
  "knowledge_refs": [
    "nlp/nlp-13-lstm-for-text"
  ],
  "prerequisites": [
    "NLP-13: LSTMs for Text"
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

# NLP-14-SEQ2SEQ: Seq2Seq Models & Machine Translation

## Introduction

Encoder-decoder architectures that map one sequence to another — the basis of translation. By the end of this lesson you will be able to: Explain the encoder-decoder split; Decode with greedy and beam search; Use teacher forcing in training; Describe how attention improved seq2seq.

## Key Concepts

### 1. Explain the encoder-decoder split

Target: Explain the encoder-decoder split. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import torch.nn as nn

class Encoder(nn.Module):
    def __init__(self):
        super().__init__()
        self.emb = nn.Embedding(1000, 64)
        self.rnn = nn.GRU(64, 128, batch_first=True)
    def forward(self, ids):
        _, h = self.rnn(self.emb(ids))
        return h

print(Encoder())
```
### 2. Decode with greedy and beam search

Target: Decode with greedy and beam search. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import torch.nn as nn

class Decoder(nn.Module):
    def __init__(self):
        super().__init__()
        self.emb = nn.Embedding(1000, 64)
        self.rnn = nn.GRU(64, 128, batch_first=True)
        self.head = nn.Linear(128, 1000)
    def forward(self, ids, hidden):
        out, h = self.rnn(self.emb(ids), hidden)
        return self.head(out), h

print(Decoder())
```
### 3. Use teacher forcing in training

Target: Use teacher forcing in training. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import torch

# Greedy decoding: pick the argmax token at each step
logits = torch.randn(1, 5, 1000)
tok = logits[:, -1].argmax(-1)
print("next token id:", tok.item())
```
### 4. Describe how attention improved seq2seq

Target: Describe how attention improved seq2seq. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import torch

# Teacher forcing: feed the true token during training
print("train with ground truth; decode with own predictions")
```

## Practice Questions

1. What is the key idea behind "Seq2Seq Models & Machine Translation"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Seq2Seq Models & Machine Translation with analogies and real-world examples"
1. "Show me common mistakes beginners make with Seq2Seq Models & Machine Translation"
1. "Provide advanced patterns and performance considerations for Seq2Seq Models & Machine Translation"

## Key Takeaways

- Master the core ideas of Seq2Seq Models & Machine Translation through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
