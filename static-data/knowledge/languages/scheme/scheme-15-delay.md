---
{
  "title": "Lazy Evaluation",
  "description": "delay and force.",
  "type": "lesson",
  "order": 15,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use delay",
    "Use force",
    "Build lazy streams",
    "Memoize values"
  ],
  "knowledge_refs": [
    "scheme/scheme-15-delay"
  ],
  "prerequisites": [
    "Scheme-14: Tail Calls and CPS"
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

# SCHEME-15-DELAY: Lazy Evaluation

## Introduction

delay and force. By the end of this lesson you will be able to: Use delay; Use force; Build lazy streams; Memoize values.

## Key Concepts

### 1. Use delay

Target: Use delay. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```scheme
(define x (delay (* 3 4)))
(force x)
```
### 2. Use force

Target: Use force. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```scheme
(define (stream-cons a b) (cons a (delay b)))
```
### 3. Build lazy streams

Target: Build lazy streams. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```scheme
(define (stream-car s) (car s))
(define (stream-cdr s) (force (cdr s)))
```
### 4. Memoize values

Target: Memoize values. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```scheme
(define ones (cons 1 (delay ones)))
```

## Practice Questions

1. What is the key idea behind "Lazy Evaluation"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Lazy Evaluation with analogies and real-world examples"
1. "Show me common mistakes beginners make with Lazy Evaluation"
1. "Provide advanced patterns and performance considerations for Lazy Evaluation"

## Key Takeaways

- Master the core ideas of Lazy Evaluation through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
