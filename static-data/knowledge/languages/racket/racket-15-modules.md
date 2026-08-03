---
{
  "title": "Modules",
  "description": "Organize Racket code.",
  "type": "lesson",
  "order": 15,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Create modules",
    "Require modules",
    "Provide bindings",
    "Use contracts"
  ],
  "knowledge_refs": [
    "racket/racket-15-modules"
  ],
  "prerequisites": [
    "Racket-14: Macros"
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

# RACKET-15-MODULES: Modules

## Introduction

Organize Racket code. By the end of this lesson you will be able to: Create modules; Require modules; Provide bindings; Use contracts.

## Key Concepts

### 1. Create modules

Target: Create modules. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```racket
#lang racket
(provide square)
(define (square x) (* x x))
```
### 2. Require modules

Target: Require modules. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```racket
(require "math.rkt")
(square 5)
```
### 3. Provide bindings

Target: Provide bindings. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```racket
(provide (all-defined-out))
```
### 4. Use contracts

Target: Use contracts. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```racket
(provide (contract-out
           [square (-> number? number?)]))
```

## Practice Questions

1. What is the key idea behind "Modules"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Modules with analogies and real-world examples"
1. "Show me common mistakes beginners make with Modules"
1. "Provide advanced patterns and performance considerations for Modules"

## Key Takeaways

- Master the core ideas of Modules through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
