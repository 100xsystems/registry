---
{
  "title": "Text Summarization",
  "description": "Extractive and abstractive summaries with pretrained sequence-to-sequence models.",
  "type": "lesson",
  "order": 19,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Compare extractive and abstractive summarization",
    "Summarize with a pretrained BART/T5 model",
    "Control summary length",
    "Evaluate with ROUGE"
  ],
  "knowledge_refs": [
    "nlp/nlp-19-summarization"
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

# NLP-19-SUMMARIZATION: Text Summarization

## Introduction

Extractive and abstractive summaries with pretrained sequence-to-sequence models. By the end of this lesson you will be able to: Compare extractive and abstractive summarization; Summarize with a pretrained BART/T5 model; Control summary length; Evaluate with ROUGE.

## Key Concepts

### 1. Compare extractive and abstractive summarization

Target: Compare extractive and abstractive summarization. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
print(summarizer("Long article text here...", max_length=50, min_length=10)[0]["summary_text"])
```
### 2. Summarize with a pretrained BART/T5 model

Target: Summarize with a pretrained BART/T5 model. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from transformers import pipeline

# T5 style: task prefix controls behavior
print("summarize: <text>")
```
### 3. Control summary length

Target: Control summary length. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
from transformers import pipeline

summarizer = pipeline("summarization")
out = summarizer("text", max_length=30, min_length=5, do_sample=False)
print(out[0]["summary_text"])
```
### 4. Evaluate with ROUGE

Target: Evaluate with ROUGE. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import numpy as np

# ROUGE-N: n-gram overlap between summary and reference
ref = "the cat sat on the mat"
pred = "the cat sat"
print("ROUGE-1 precision:", len(set(pred.split()) & set(ref.split())) / len(pred.split()))
```

## Practice Questions

1. What is the key idea behind "Text Summarization"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Text Summarization with analogies and real-world examples"
1. "Show me common mistakes beginners make with Text Summarization"
1. "Provide advanced patterns and performance considerations for Text Summarization"

## Key Takeaways

- Master the core ideas of Text Summarization through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
