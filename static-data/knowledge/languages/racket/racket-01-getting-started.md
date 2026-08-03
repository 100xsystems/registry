---
{
  "title": "Getting Started with Racket",
  "description": "Install, DrRacket, hello world.",
  "type": "lesson",
  "order": 1,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Install Racket",
    "Use DrRacket IDE",
    "Write hello world",
    "Run scripts"
  ],
  "knowledge_refs": [
    "racket/racket-01-getting-started"
  ],
  "prerequisites": [
    "None — this is the entry point"
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

# RACKET-01-GETTING-STARTED: Getting Started with Racket

## Introduction

Install, DrRacket, hello world. By the end of this lesson you will be able to: Install Racket; Use DrRacket IDE; Write hello world; Run scripts.

## Key Concepts

### 1. Install Racket

Target: Install Racket. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```racket
#lang racket

(displayln "Hello, World!")
```
### 2. Use DrRacket IDE

Target: Use DrRacket IDE. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```racket
#lang racket
(displayln "Hello, ")
(displayln "Racket!")
```
### 3. Write hello world

Target: Write hello world. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```racket
#lang racket
(displayln (+ 1 2))
```
### 4. Run scripts

Target: Run scripts. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```racket
#lang racket
(displayln "Racket is a language for making languages")
```

## Practice Questions

1. What is the key idea behind "Getting Started with Racket"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with Racket with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with Racket"
1. "Provide advanced patterns and performance considerations for Getting Started with Racket"

## Key Takeaways

- Master the core ideas of Getting Started with Racket through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
