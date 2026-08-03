---
{
  "title": "Part-of-Speech Tagging",
  "description": "Tag every token with its grammatical role — the classic sequence-labeling task.",
  "type": "lesson",
  "order": 10,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Explain POS tags and why they matter",
    "Tag text with NLTK and spaCy",
    "Use POS tags as features",
    "Describe sequence labeling formally"
  ],
  "knowledge_refs": [
    "nlp/nlp-10-pos-tagging"
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

# NLP-10-POS-TAGGING: Part-of-Speech Tagging

## Introduction

Tag every token with its grammatical role — the classic sequence-labeling task. By the end of this lesson you will be able to: Explain POS tags and why they matter; Tag text with NLTK and spaCy; Use POS tags as features; Describe sequence labeling formally.

## Key Concepts

### 1. Explain POS tags and why they matter

Target: Explain POS tags and why they matter. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import nltk
nltk.download("averaged_perceptron_tagger_eng", quiet=True)
from nltk import pos_tag, word_tokenize

print(pos_tag(word_tokenize("The quick brown fox jumps")))
```
### 2. Tag text with NLTK and spaCy

Target: Tag text with NLTK and spaCy. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("They are running late")
print([(t.text, t.pos_) for t in doc])
```
### 3. Use POS tags as features

Target: Use POS tags as features. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import spacy

# POS features feed higher-level parsers
print("tags: NOUN, VERB, ADJ, ADP, DET ...")
```
### 4. Describe sequence labeling formally

Target: Describe sequence labeling formally. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import spacy

# Disambiguation: "book" as noun vs verb
for d in [nlp("read the book"), nlp("book a flight")]:
    print([(t.text, t.pos_) for t in d])
```

## Practice Questions

1. What is the key idea behind "Part-of-Speech Tagging"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Part-of-Speech Tagging with analogies and real-world examples"
1. "Show me common mistakes beginners make with Part-of-Speech Tagging"
1. "Provide advanced patterns and performance considerations for Part-of-Speech Tagging"

## Key Takeaways

- Master the core ideas of Part-of-Speech Tagging through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
