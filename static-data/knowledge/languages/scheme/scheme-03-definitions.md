---
{
  "title": "Definitions and Binding",
  "description": "define and let.",
  "type": "lesson",
  "order": 3,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Define variables",
    "Use let",
    "Define functions",
    "Nest bindings"
  ],
  "knowledge_refs": [
    "scheme/scheme-03-definitions"
  ],
  "prerequisites": [
    "Scheme-02: Expressions and Values"
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

# SCHEME-03-DEFINITIONS: Definitions and Binding

## Introduction

define and let. By the end of this lesson you will be able to: Define variables; Use let; Define functions; Nest bindings.

## Key Concepts

### 1. Define variables

Target: Define variables. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```scheme
(define name "Ada")
(display name)
```
### 2. Use let

Target: Use let. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```scheme
(let ((x 10) (y 20)) (+ x y))
```
### 3. Define functions

Target: Define functions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```scheme
(define (square x) (* x x))
```
### 4. Nest bindings

Target: Nest bindings. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```scheme
(define pi 3.14159)
```

## Practice Questions

1. What is the key idea behind "Definitions and Binding"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Definitions and Binding with analogies and real-world examples"
1. "Show me common mistakes beginners make with Definitions and Binding"
1. "Provide advanced patterns and performance considerations for Definitions and Binding"

## Key Takeaways

- Master the core ideas of Definitions and Binding through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
