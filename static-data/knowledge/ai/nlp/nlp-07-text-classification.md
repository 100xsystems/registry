---
{
  "title": "Text Classification",
  "description": "Spam, topics, intent: logistic regression and linear models on TF-IDF — fast and often enough.",
  "type": "lesson",
  "order": 7,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Frame text classification as a supervised task",
    "Build a TF-IDF + logistic regression pipeline",
    "Evaluate with precision/recall per class",
    "Explain when linear models beat deep ones"
  ],
  "knowledge_refs": [
    "nlp/nlp-07-text-classification"
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

# NLP-07-TEXT-CLASSIFICATION: Text Classification

## Introduction

Spam, topics, intent: logistic regression and linear models on TF-IDF — fast and often enough. By the end of this lesson you will be able to: Frame text classification as a supervised task; Build a TF-IDF + logistic regression pipeline; Evaluate with precision/recall per class; Explain when linear models beat deep ones.

## Key Concepts

### 1. Frame text classification as a supervised task

Target: Frame text classification as a supervised task. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

texts = ["cheap pills now", "free money", "meeting at noon", "lunch tomorrow"]
y = [1, 1, 0, 0]
pipe = make_pipeline(TfidfVectorizer(), LogisticRegression())
pipe.fit(texts, y)
print("pred:", pipe.predict(["win a free ipad"])[0])
```
### 2. Build a TF-IDF + logistic regression pipeline

Target: Build a TF-IDF + logistic regression pipeline. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(pipe, texts, y, cv=2)
print("cv accuracy:", scores.mean().round(2))
```
### 3. Evaluate with precision/recall per class

Target: Evaluate with precision/recall per class. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
from sklearn.metrics import classification_report

print(classification_report(y, pipe.predict(texts), target_names=["ham", "spam"]))
```
### 4. Explain when linear models beat deep ones

Target: Explain when linear models beat deep ones. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import numpy as np

# Imbalanced data: stratify or weight classes
from sklearn.utils.class_weight import compute_class_weight
print("class weights:", compute_class_weight("balanced", classes=np.array([0, 1]), y=np.array(y)))
```

## Practice Questions

1. What is the key idea behind "Text Classification"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Text Classification with analogies and real-world examples"
1. "Show me common mistakes beginners make with Text Classification"
1. "Provide advanced patterns and performance considerations for Text Classification"

## Key Takeaways

- Master the core ideas of Text Classification through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
