---
{
  "title": "Higher-Order Functions",
  "description": "Functions as values.",
  "type": "lesson",
  "order": 10,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Pass functions",
    "Return functions",
    "Use curry",
    "Use compose"
  ],
  "knowledge_refs": [
    "racket/racket-10-higher-order"
  ],
  "prerequisites": [
    "Racket-09: Strings"
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

# RACKET-10-HIGHER-ORDER: Higher-Order Functions

## Introduction

Functions as values. By the end of this lesson you will be able to: Pass functions; Return functions; Use curry; Use compose.

## Key Concepts

### 1. Pass functions

Target: Pass functions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```racket
#lang racket
(define (apply-twice f x) (f (f x)))
(displayln (apply-twice add1 5))
```
### 2. Return functions

Target: Return functions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```racket
(define (adder n) (lambda (x) (+ x n)))
(define add5 (adder 5))
(displayln (add5 10))
```
### 3. Use curry

Target: Use curry. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```racket
((compose add1 add1) 5)
```
### 4. Use compose

Target: Use compose. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```racket
(curry + 5)
```

## Practice Questions

1. What is the key idea behind "Higher-Order Functions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Higher-Order Functions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Higher-Order Functions"
1. "Provide advanced patterns and performance considerations for Higher-Order Functions"

## Key Takeaways

- Master the core ideas of Higher-Order Functions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
