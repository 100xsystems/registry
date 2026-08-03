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
    "Pass functions",
    "Use variadic functions"
  ],
  "knowledge_refs": [
    "scheme/scheme-04-functions"
  ],
  "prerequisites": [
    "Scheme-03: Definitions and Binding"
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

# SCHEME-04-FUNCTIONS: Functions

## Introduction

define and lambda. By the end of this lesson you will be able to: Define functions; Use lambda; Pass functions; Use variadic functions.

## Key Concepts

### 1. Define functions

Target: Define functions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```scheme
(define (add a b) (+ a b))
(add 2 3)
```
### 2. Use lambda

Target: Use lambda. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```scheme
(define double (lambda (x) (* x 2)))
(double 21)
```
### 3. Pass functions

Target: Pass functions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```scheme
(map (lambda (x) (* x x)) (list 1 2 3))
```
### 4. Use variadic functions

Target: Use variadic functions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```scheme
(define (sum . nums) (apply + nums))
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
