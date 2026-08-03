---
{
  "title": "Text Preprocessing",
  "description": "Lowercasing, stop words, stemming and lemmatization — clean text without destroying meaning.",
  "type": "lesson",
  "order": 3,
  "duration": "50 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Normalize case and punctuation",
    "Remove stop words judiciously",
    "Stem and lemmatize words",
    "Know when preprocessing hurts modern models"
  ],
  "knowledge_refs": [
    "nlp/nlp-03-text-preprocessing"
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

# NLP-03-TEXT-PREPROCESSING: Text Preprocessing

## Introduction

Lowercasing, stop words, stemming and lemmatization — clean text without destroying meaning. By the end of this lesson you will be able to: Normalize case and punctuation; Remove stop words judiciously; Stem and lemmatize words; Know when preprocessing hurts modern models.

## Key Concepts

### 1. Normalize case and punctuation

Target: Normalize case and punctuation. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("stopwords", quiet=True)
words = [w.lower() for w in word_tokenize("The quick brown fox jumps over the lazy dog")]
clean = [w for w in words if w not in stopwords.words("english")]
print(clean)
```
### 2. Remove stop words judiciously

Target: Remove stop words judiciously. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
print([stemmer.stem(w) for w in ["running", "runner", "runs"]])
```
### 3. Stem and lemmatize words

Target: Stem and lemmatize words. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import nltk
from nltk.stem import WordNetLemmatizer
nltk.download("wordnet", quiet=True)

lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("running", pos="v"))
```
### 4. Know when preprocessing hurts modern models

Target: Know when preprocessing hurts modern models. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import re

raw = "  Hello,   WORLD!!  "
cleaned = re.sub(r"[^a-zA-Z0-9\s]", "", raw).lower().split()
print(cleaned)
```

## Practice Questions

1. What is the key idea behind "Text Preprocessing"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Text Preprocessing with analogies and real-world examples"
1. "Show me common mistakes beginners make with Text Preprocessing"
1. "Provide advanced patterns and performance considerations for Text Preprocessing"

## Key Takeaways

- Master the core ideas of Text Preprocessing through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
