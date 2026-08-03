---
{
  "title": "Text Representation: From Tokens to Vectors",
  "description": "Tokenization, bag-of-words and TF-IDF — how raw text becomes numbers a model can use.",
  "type": "lesson",
  "order": 2,
  "duration": "55 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Tokenize text into words and subwords",
    "Build a bag-of-words representation",
    "Weight terms with TF-IDF",
    "Explain sparsity and vocabulary growth"
  ],
  "knowledge_refs": [
    "nlp/nlp-01-what-is-nlp",
    "generative-ai/genai-07-tokenization",
    "llm-engineering/llm-05-tokenization-and-context"
  ],
  "prerequisites": [
    "NLP-01: What Is NLP?"
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

# NLP-02-TEXT-REPRESENTATION: Text Representation: From Tokens to Vectors

## Introduction

Tokenization, bag-of-words and TF-IDF — how raw text becomes numbers a model can use. By the end of this lesson you will be able to: Tokenize text into words and subwords; Build a bag-of-words representation; Weight terms with TF-IDF; Explain sparsity and vocabulary growth.

## Key Concepts

### 1. Tokenize text into words and subwords

Target: Tokenize text into words and subwords. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from sklearn.feature_extraction.text import CountVectorizer

corpus = ["the cat sat", "the dog ran", "cat and dog"]
vec = CountVectorizer()
X = vec.fit_transform(corpus)
print("vocab:", vec.get_feature_names_out())
print("matrix:", X.toarray())
```
### 2. Build a bag-of-words representation

Target: Build a bag-of-words representation. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from sklearn.feature_extraction.text import TfidfVectorizer

vec = TfidfVectorizer()
X = vec.fit_transform(corpus)
print("tfidf:", X.toarray().round(2))
```
### 3. Weight terms with TF-IDF

Target: Weight terms with TF-IDF. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import nltk
nltk.download("punkt", quiet=True)
from nltk.tokenize import word_tokenize

print(word_tokenize("Don't stop believing!"))
```
### 4. Explain sparsity and vocabulary growth

Target: Explain sparsity and vocabulary growth. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
from sklearn.feature_extraction.text import CountVectorizer

vec = CountVectorizer(ngram_range=(1, 2))
print("with bigrams:", vec.fit_transform(corpus).shape[1], "features")
```

## Practice Questions

1. What is the key idea behind "Text Representation: From Tokens to Vectors"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Text Representation: From Tokens to Vectors with analogies and real-world examples"
1. "Show me common mistakes beginners make with Text Representation: From Tokens to Vectors"
1. "Provide advanced patterns and performance considerations for Text Representation: From Tokens to Vectors"

## Key Takeaways

- Master the core ideas of Text Representation: From Tokens to Vectors through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
