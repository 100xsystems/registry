---
{
  "title": "Functions",
  "description": "define and lambda.",
  "type": "lesson",
  "order": 4,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Define functions",
    "Use lambda",
    "Apply functions",
    "Compose functions"
  ],
  "knowledge_refs": [
    "racket/racket-04-functions"
  ],
  "prerequisites": [
    "Racket-03: Definitions"
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

# RACKET-04-FUNCTIONS: Functions

## Introduction

define and lambda. By the end of this lesson you will be able to: Define functions; Use lambda; Apply functions; Compose functions.

## Key Concepts

### 1. Define functions

Target: Define functions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```racket
#lang racket
(define (square x) (* x x))
(displayln (square 5))
```
### 2. Use lambda

Target: Use lambda. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```racket
(define double (lambda (x) (* x 2)))
(displayln (double 21))
```
### 3. Apply functions

Target: Apply functions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```racket
(map (lambda (x) (* x 2)) (list 1 2 3))
```
### 4. Compose functions

Target: Compose functions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```racket
(define (add a b) (+ a b))
(displayln (add 2 3))
```

## Practice Questions

1. What is the key idea behind "Functions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Functions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Functions"
1. "Provide advanced patterns and performance considerations for Functions"

## Key Takeaways

- Master the core ideas of Functions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
