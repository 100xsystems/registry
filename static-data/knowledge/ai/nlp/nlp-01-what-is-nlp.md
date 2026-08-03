---
{
  "title": "What Is NLP?",
  "description": "The field, the tasks, and the deep-learning revolution that reshaped how machines read language.",
  "type": "lesson",
  "order": 1,
  "duration": "40 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Define natural language processing and its scope",
    "List the core NLP tasks",
    "Contrast rule-based and learned approaches",
    "Identify modern production NLP use cases"
  ],
  "knowledge_refs": [
    "nlp/nlp-01-what-is-nlp"
  ],
  "prerequisites": [
    "DL-01: What Is Deep Learning?"
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

# NLP-01-WHAT-IS-NLP: What Is NLP?

## Introduction

The field, the tasks, and the deep-learning revolution that reshaped how machines read language. By the end of this lesson you will be able to: Define natural language processing and its scope; List the core NLP tasks; Contrast rule-based and learned approaches; Identify modern production NLP use cases.

## Key Concepts

### 1. Define natural language processing and its scope

Target: Define natural language processing and its scope. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
tasks = {
    "classification": "spam, sentiment, topic",
    "extraction": "entities, relations, keywords",
    "generation": "summaries, translations, dialogue",
}
for group, examples in tasks.items():
    print(f"{group:14} {examples}")
```
### 2. List the core NLP tasks

Target: List the core NLP tasks. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import spacy

nlp = spacy.load("en_core_web_sm")
print("spaCy pipeline:", nlp.pipe_names)
```
### 3. Contrast rule-based and learned approaches

Target: Contrast rule-based and learned approaches. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
apps = ["search", "chatbots", "translators", "voice assistants", "document search"]
for a in apps:
    print(f"- {a}")
```
### 4. Identify modern production NLP use cases

Target: Identify modern production NLP use cases. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("rule-based: brittle. learned: flexible.")
```

## Practice Questions

1. What is the key idea behind "What Is NLP?"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain What Is NLP? with analogies and real-world examples"
1. "Show me common mistakes beginners make with What Is NLP?"
1. "Provide advanced patterns and performance considerations for What Is NLP?"

## Key Takeaways

- Master the core ideas of What Is NLP? through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
