---
{
  "title": "Macros",
  "description": "Code generation.",
  "type": "lesson",
  "order": 14,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Write define-syntax-rule",
    "Use syntax-parse",
    "Generate code",
    "Build DSLs"
  ],
  "knowledge_refs": [
    "racket/racket-14-macros"
  ],
  "prerequisites": [
    "Racket-13: Input/Output"
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

# RACKET-14-MACROS: Macros

## Introduction

Code generation. By the end of this lesson you will be able to: Write define-syntax-rule; Use syntax-parse; Generate code; Build DSLs.

## Key Concepts

### 1. Write define-syntax-rule

Target: Write define-syntax-rule. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```racket
#lang racket
(define-syntax-rule (twice expr)
  (begin expr expr))

(twice (displayln "hi"))
```
### 2. Use syntax-parse

Target: Use syntax-parse. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```racket
(define-syntax-rule (unless test body ...)
  (when (not test) body ...))
```
### 3. Generate code

Target: Generate code. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```racket
(require syntax/parse)
(define-syntax (my-let stx)
  (syntax-parse stx
    [(_ (x val) body ...)
     #'(let ([x val]) body ...)]))
```
### 4. Build DSLs

Target: Build DSLs. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```racket
(define-syntax-rule (defn name args body ...)
  (define (name args) body ...))
```

## Practice Questions

1. What is the key idea behind "Macros"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Macros with analogies and real-world examples"
1. "Show me common mistakes beginners make with Macros"
1. "Provide advanced patterns and performance considerations for Macros"

## Key Takeaways

- Master the core ideas of Macros through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
