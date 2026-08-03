---
{
  "title": "Expressions and Values",
  "description": "S-expressions and evaluation.",
  "type": "lesson",
  "order": 2,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Understand S-expressions",
    "Evaluate expressions",
    "Use literals",
    "Quote data"
  ],
  "knowledge_refs": [
    "racket/racket-02-forms"
  ],
  "prerequisites": [
    "Racket-01: Getting Started with Racket"
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

# RACKET-02-FORMS: Expressions and Values

## Introduction

S-expressions and evaluation. By the end of this lesson you will be able to: Understand S-expressions; Evaluate expressions; Use literals; Quote data.

## Key Concepts

### 1. Understand S-expressions

Target: Understand S-expressions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```racket
#lang racket
(+ 1 2)
(- 10 4)
(* 3 4)
(/ 10 2)
```
### 2. Evaluate expressions

Target: Evaluate expressions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```racket
(displayln "hi")
(displayln 42)
```
### 3. Use literals

Target: Use literals. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```racket
'(1 2 3)
```
### 4. Quote data

Target: Quote data. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```racket
(quote hello)
```

## Practice Questions

1. What is the key idea behind "Expressions and Values"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Expressions and Values with analogies and real-world examples"
1. "Show me common mistakes beginners make with Expressions and Values"
1. "Provide advanced patterns and performance considerations for Expressions and Values"

## Key Takeaways

- Master the core ideas of Expressions and Values through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
