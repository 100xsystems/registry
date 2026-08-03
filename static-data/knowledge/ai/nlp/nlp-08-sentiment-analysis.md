---
{
  "title": "Sentiment Analysis",
  "description": "Detect opinion and emotion in text — from lexicon scores to fine-tuned transformers.",
  "type": "lesson",
  "order": 8,
  "duration": "50 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Score sentiment with lexicons",
    "Train a classifier on labeled reviews",
    "Use a pretrained sentiment model",
    "Handle negation and domain shift"
  ],
  "knowledge_refs": [
    "nlp/nlp-07-text-classification",
    "computer-vision/cv-15-video-analysis"
  ],
  "prerequisites": [
    "NLP-07: Text Classification"
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

# NLP-08-SENTIMENT-ANALYSIS: Sentiment Analysis

## Introduction

Detect opinion and emotion in text — from lexicon scores to fine-tuned transformers. By the end of this lesson you will be able to: Score sentiment with lexicons; Train a classifier on labeled reviews; Use a pretrained sentiment model; Handle negation and domain shift.

## Key Concepts

### 1. Score sentiment with lexicons

Target: Score sentiment with lexicons. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from textblob import TextBlob

print(TextBlob("This movie was amazing!").sentiment)
print(TextBlob("Waste of time.").sentiment)
```
### 2. Train a classifier on labeled reviews

Target: Train a classifier on labeled reviews. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
print(analyzer.polarity_scores("Not bad at all, actually good!"))
```
### 3. Use a pretrained sentiment model

Target: Use a pretrained sentiment model. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis")
print(classifier("I absolutely loved this film"))
```
### 4. Handle negation and domain shift

Target: Handle negation and domain shift. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import re

# Negation flips meaning: "not good" != "good"
text = "the food was not good"
print("flipped" if "not" in text.split() else "same")
```

## Practice Questions

1. What is the key idea behind "Sentiment Analysis"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Sentiment Analysis with analogies and real-world examples"
1. "Show me common mistakes beginners make with Sentiment Analysis"
1. "Provide advanced patterns and performance considerations for Sentiment Analysis"

## Key Takeaways

- Master the core ideas of Sentiment Analysis through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
