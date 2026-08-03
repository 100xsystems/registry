---
{
  "title": "Lists",
  "description": "Build and process lists.",
  "type": "lesson",
  "order": 5,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create lists",
    "Use cons/car/cdr",
    "Map and filter",
    "Fold lists"
  ],
  "knowledge_refs": [
    "racket/racket-05-lists"
  ],
  "prerequisites": [
    "Racket-04: Functions"
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

# RACKET-05-LISTS: Lists

## Introduction

Build and process lists. By the end of this lesson you will be able to: Create lists; Use cons/car/cdr; Map and filter; Fold lists.

## Key Concepts

### 1. Create lists

Target: Create lists. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```racket
#lang racket
(define nums (list 1 2 3))
(displayln nums)
```
### 2. Use cons/car/cdr

Target: Use cons/car/cdr. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```racket
(cons 0 (list 1 2))
```
### 3. Map and filter

Target: Map and filter. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```racket
(car (list 1 2 3))
(cdr (list 1 2 3))
```
### 4. Fold lists

Target: Fold lists. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```racket
(map (lambda (n) (* n 2)) (list 1 2 3))
(filter odd? (list 1 2 3 4))
```

## Practice Questions

1. What is the key idea behind "Lists"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Lists with analogies and real-world examples"
1. "Show me common mistakes beginners make with Lists"
1. "Provide advanced patterns and performance considerations for Lists"

## Key Takeaways

- Master the core ideas of Lists through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
