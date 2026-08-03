---
{
  "title": "Named Entity Recognition",
  "description": "Find people, places, organizations and dates — the extraction workhorse of document AI.",
  "type": "lesson",
  "order": 9,
  "duration": "50 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define NER and common entity types",
    "Extract entities with spaCy",
    "Explain BIO tagging",
    "Fine-tune or use pretrained NER"
  ],
  "knowledge_refs": [
    "nlp/nlp-09-named-entity-recognition"
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

# NLP-09-NAMED-ENTITY-RECOGNITION: Named Entity Recognition

## Introduction

Find people, places, organizations and dates — the extraction workhorse of document AI. By the end of this lesson you will be able to: Define NER and common entity types; Extract entities with spaCy; Explain BIO tagging; Fine-tune or use pretrained NER.

## Key Concepts

### 1. Define NER and common entity types

Target: Define NER and common entity types. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Elon Musk founded SpaceX in Hawthorne, California.")
for ent in doc.ents:
    print(ent.text, "->", ent.label_)
```
### 2. Extract entities with spaCy

Target: Extract entities with spaCy. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import spacy

# NER as token classification (BIO scheme)
print("B-PER I-PER O O B-ORG ...")
```
### 3. Explain BIO tagging

Target: Explain BIO tagging. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
from transformers import pipeline

ner = pipeline("ner", aggregation_strategy="simple")
print(ner("Apple is looking to buy a startup in London"))
```
### 4. Fine-tune or use pretrained NER

Target: Fine-tune or use pretrained NER. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import spacy

# Custom entities: train with a few hundred labeled examples
print("spaCy supports training custom entity types")
```

## Practice Questions

1. What is the key idea behind "Named Entity Recognition"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Named Entity Recognition with analogies and real-world examples"
1. "Show me common mistakes beginners make with Named Entity Recognition"
1. "Provide advanced patterns and performance considerations for Named Entity Recognition"

## Key Takeaways

- Master the core ideas of Named Entity Recognition through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
