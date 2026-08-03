---
{
  "title": "Strings",
  "description": "String functions.",
  "type": "lesson",
  "order": 9,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Concatenate strings",
    "Get length",
    "Convert cases",
    "Format output"
  ],
  "knowledge_refs": [
    "racket/racket-09-strings"
  ],
  "prerequisites": [
    "Racket-08: Structs"
  ],
  "references": [
    {
      "title": "Racket Documentation",
      "url": "https://docs.racket-lang.org/",
      "description": "Official docs"
    },
    {
      "title": "How to Design Programs",
      "url": "https://htdp.org/",
      "description": "The classic textbook"
    },
    {
      "title": "Racket Guide",
      "url": "https://docs.racket-lang.org/guide/",
      "description": "Official language guide"
    }
  ]
}
---

# RACKET-09-STRINGS: Strings

## Introduction

String functions. By the end of this lesson you will be able to: Concatenate strings; Get length; Convert cases; Format output.

## Key Concepts

### 1. Concatenate strings

Target: Concatenate strings. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```racket
#lang racket
(string-append "Hello" " " "World")
```
### 2. Get length

Target: Get length. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```racket
(string-length "hello")
```
### 3. Convert cases

Target: Convert cases. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```racket
(string-upcase "hi")
(string-downcase "HI")
```
### 4. Format output

Target: Format output. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```racket
(format "value: ~a" 42)
```

## Practice Questions

1. What is the key idea behind "Strings"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Strings with analogies and real-world examples"
1. "Show me common mistakes beginners make with Strings"
1. "Provide advanced patterns and performance considerations for Strings"

## Key Takeaways

- Master the core ideas of Strings through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
