---
{
  "title": "Regular Expressions for Text",
  "description": "Pattern matching for extraction, validation and cleaning — the precision tool in every NLP workflow.",
  "type": "lesson",
  "order": 4,
  "duration": "50 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write regex patterns for common text shapes",
    "Extract emails, dates and numbers",
    "Use capture groups and lookarounds",
    "Clean text at scale with re.sub"
  ],
  "knowledge_refs": [
    "nlp/nlp-03-text-preprocessing",
    "generative-ai/genai-03-text-generation-basics"
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

# NLP-04-REGULAR-EXPRESSIONS: Regular Expressions for Text

## Introduction

Pattern matching for extraction, validation and cleaning — the precision tool in every NLP workflow. By the end of this lesson you will be able to: Write regex patterns for common text shapes; Extract emails, dates and numbers; Use capture groups and lookarounds; Clean text at scale with re.sub.

## Key Concepts

### 1. Write regex patterns for common text shapes

Target: Write regex patterns for common text shapes. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import re

text = "Contact support@example.com or sales@corp.io by 2024-12-31."
emails = re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", text)
print(emails)
```
### 2. Extract emails, dates and numbers

Target: Extract emails, dates and numbers. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import re

dates = re.findall(r"\d{4}-\d{2}-\d{2}", "Due 2024-12-31, reviewed 2025-01-05")
print(dates)
```
### 3. Use capture groups and lookarounds

Target: Use capture groups and lookarounds. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import re

text = "Order #12345 and #A-999"
ids = re.findall(r"#([A-Za-z0-9-]+)", text)
print(ids)
```
### 4. Clean text at scale with re.sub

Target: Clean text at scale with re.sub. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import re

messy = "call   me!! maybe??"
clean = re.sub(r"[!?]+", "", messy)
clean = re.sub(r"\s+", " ", clean).strip()
print(clean)
```

## Practice Questions

1. What is the key idea behind "Regular Expressions for Text"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Regular Expressions for Text with analogies and real-world examples"
1. "Show me common mistakes beginners make with Regular Expressions for Text"
1. "Provide advanced patterns and performance considerations for Regular Expressions for Text"

## Key Takeaways

- Master the core ideas of Regular Expressions for Text through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
