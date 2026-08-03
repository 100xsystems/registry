---
{
  "title": "Higher-Order Functions",
  "description": "Abstract over functions.",
  "type": "lesson",
  "order": 8,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use map",
    "Use filter",
    "Use fold",
    "Compose functions"
  ],
  "knowledge_refs": [
    "scheme/scheme-08-higher-order"
  ],
  "prerequisites": [
    "Scheme-07: Recursion"
  ],
  "references": [
    {
      "title": "Scheme Reports",
      "url": "https://small.r7rs.org/",
      "description": "The R7RS specification"
    },
    {
      "title": "Structure and Interpretation of Computer Programs",
      "url": "https://mitp-press.mit.edu/sites/default/files/sicp/full-text/book/book.html",
      "description": "SICP — the classic book"
    },
    {
      "title": "The Scheme Programming Language",
      "url": "https://www.scheme.com/tspl4/",
      "description": "Dybvig's book"
    }
  ]
}
---

# SCHEME-08-HIGHER-ORDER: Higher-Order Functions

## Introduction

Abstract over functions. By the end of this lesson you will be able to: Use map; Use filter; Use fold; Compose functions.

## Key Concepts

### 1. Use map

Target: Use map. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```scheme
(map (lambda (x) (* x 2)) (list 1 2 3))
```
### 2. Use filter

Target: Use filter. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```scheme
(filter even? (list 1 2 3 4))
```
### 3. Use fold

Target: Use fold. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```scheme
(fold-left + 0 (list 1 2 3))
```
### 4. Compose functions

Target: Compose functions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```scheme
(define (compose f g) (lambda (x) (f (g x))))
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
