---
{
  "title": "Question Answering",
  "description": "Extractive and generative QA — from span prediction to retrieval-augmented answers.",
  "type": "lesson",
  "order": 18,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Distinguish extractive and generative QA",
    "Run a pretrained extractive QA model",
    "Pair QA with retrieval (open-domain)",
    "Evaluate with exact match and F1"
  ],
  "knowledge_refs": [
    "nlp/nlp-18-question-answering"
  ],
  "prerequisites": [
    "NLP-17: Fine-Tuning Transformers"
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

# NLP-18-QUESTION-ANSWERING: Question Answering

## Introduction

Extractive and generative QA — from span prediction to retrieval-augmented answers. By the end of this lesson you will be able to: Distinguish extractive and generative QA; Run a pretrained extractive QA model; Pair QA with retrieval (open-domain); Evaluate with exact match and F1.

## Key Concepts

### 1. Distinguish extractive and generative QA

Target: Distinguish extractive and generative QA. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from transformers import pipeline

qa = pipeline("question-answering")
ctx = "100xSystems is a developer education platform."
print(qa(question="What is 100xSystems?", context=ctx))
```
### 2. Run a pretrained extractive QA model

Target: Run a pretrained extractive QA model. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import torch

# Extractive: predict start and end span positions
start_logits = torch.randn(50)
end_logits = torch.randn(50)
print("span:", start_logits.argmax().item(), end_logits.argmax().item())
```
### 3. Pair QA with retrieval (open-domain)

Target: Pair QA with retrieval (open-domain). Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import numpy as np

def exact_match(pred, truth):
    return int(pred.strip().lower() == truth.strip().lower())

print("EM:", exact_match("Paris", " Paris "))
```
### 4. Evaluate with exact match and F1

Target: Evaluate with exact match and F1. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("open-domain QA = retriever + reader")
```

## Practice Questions

1. What is the key idea behind "Question Answering"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Question Answering with analogies and real-world examples"
1. "Show me common mistakes beginners make with Question Answering"
1. "Provide advanced patterns and performance considerations for Question Answering"

## Key Takeaways

- Master the core ideas of Question Answering through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
