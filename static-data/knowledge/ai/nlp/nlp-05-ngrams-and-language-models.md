---
{
  "title": "N-grams & Language Models",
  "description": "Model word sequences with Markov assumptions, estimate probabilities, and generate text the old way.",
  "type": "lesson",
  "order": 5,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Explain n-gram counts and conditional probability",
    "Build a bigram model",
    "Smooth probabilities to avoid zeros",
    "Generate text by sampling from the model"
  ],
  "knowledge_refs": [
    "nlp/nlp-05-ngrams-and-language-models"
  ],
  "prerequisites": [
    "NLP-03: Text Preprocessing"
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

# NLP-05-NGRAMS-AND-LANGUAGE-MODELS: N-grams & Language Models

## Introduction

Model word sequences with Markov assumptions, estimate probabilities, and generate text the old way. By the end of this lesson you will be able to: Explain n-gram counts and conditional probability; Build a bigram model; Smooth probabilities to avoid zeros; Generate text by sampling from the model.

## Key Concepts

### 1. Explain n-gram counts and conditional probability

Target: Explain n-gram counts and conditional probability. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from collections import Counter
from nltk import bigrams

tokens = ["i", "love", "nlp", "i", "love", "coffee"]
counts = Counter(bigrams(tokens))
print(counts)
```
### 2. Build a bigram model

Target: Build a bigram model. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import numpy as np

# P(w2 | w1) = count(w1 w2) / count(w1)
count_w1 = 2   # "i" appears twice
count_w1w2 = 2  # "i love" appears twice
print("P(love | i) =", count_w1w2 / count_w1)
```
### 3. Smooth probabilities to avoid zeros

Target: Smooth probabilities to avoid zeros. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import numpy as np

# Add-one (Laplace) smoothing: no zero probabilities
V = 1000
smooth = (count_w1w2 + 1) / (count_w1 + V)
print("smoothed:", round(smooth, 6))
```
### 4. Generate text by sampling from the model

Target: Generate text by sampling from the model. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import random

bigram = {("i", "love"): ["nlp", "coffee"], ("love", "nlp"): ["a", "and"]}
start = "i"
for _ in range(5):
    nxt = random.choice(bigram.get((start, None), ["nlp"]))
    print(start, end=" ")
    start = nxt
print()
```

## Practice Questions

1. What is the key idea behind "N-grams & Language Models"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain N-grams & Language Models with analogies and real-world examples"
1. "Show me common mistakes beginners make with N-grams & Language Models"
1. "Provide advanced patterns and performance considerations for N-grams & Language Models"

## Key Takeaways

- Master the core ideas of N-grams & Language Models through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
