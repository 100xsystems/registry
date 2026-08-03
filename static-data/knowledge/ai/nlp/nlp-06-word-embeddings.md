---
{
  "title": "Word Embeddings",
  "description": "Dense vectors that capture meaning: word2vec, GloVe, and using embeddings in models.",
  "type": "lesson",
  "order": 6,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Explain why dense embeddings beat one-hot vectors",
    "Describe the word2vec objective",
    "Load pretrained embeddings",
    "Use embedding similarity for search and features"
  ],
  "knowledge_refs": [
    "nlp/nlp-06-word-embeddings"
  ],
  "prerequisites": [
    "NLP-02: Text Representation: From Tokens to Vectors"
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

# NLP-06-WORD-EMBEDDINGS: Word Embeddings

## Introduction

Dense vectors that capture meaning: word2vec, GloVe, and using embeddings in models. By the end of this lesson you will be able to: Explain why dense embeddings beat one-hot vectors; Describe the word2vec objective; Load pretrained embeddings; Use embedding similarity for search and features.

## Key Concepts

### 1. Explain why dense embeddings beat one-hot vectors

Target: Explain why dense embeddings beat one-hot vectors. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import torch
import torch.nn as nn

emb = nn.Embedding(1000, 128)
ids = torch.tensor([5, 42, 7])
print("embedding shape:", emb(ids).shape)
```
### 2. Describe the word2vec objective

Target: Describe the word2vec objective. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import numpy as np

# Semantic arithmetic: king - man + woman ≈ queen
king = np.array([1.0, 0.9])
man = np.array([1.0, 0.1])
woman = np.array([0.1, 0.9])
queen = king - man + woman
print("target vector:", queen)
```
### 3. Load pretrained embeddings

Target: Load pretrained embeddings. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import gensim.downloader as api

# Pretrained GloVe vectors
wv = api.load("glove-twitter-25")
print("similar:", wv.most_similar("computer")[:3])
```
### 4. Use embedding similarity for search and features

Target: Use embedding similarity for search and features. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import torch.nn as nn

# Embedding + average pooling as a text feature
emb = nn.Embedding(100, 64)
tokens = torch.randint(0, 100, (8, 12))
feat = emb(tokens).mean(dim=1)
print("doc vector:", feat.shape)
```

## Practice Questions

1. What is the key idea behind "Word Embeddings"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Word Embeddings with analogies and real-world examples"
1. "Show me common mistakes beginners make with Word Embeddings"
1. "Provide advanced patterns and performance considerations for Word Embeddings"

## Key Takeaways

- Master the core ideas of Word Embeddings through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
