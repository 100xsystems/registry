---
{
  "title": "OOP in Scheme",
  "description": "Object patterns.",
  "type": "lesson",
  "order": 16,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Build objects with closures",
    "Encapsulate state",
    "Create messages",
    "Use dispatch"
  ],
  "knowledge_refs": [
    "scheme/scheme-16-oop"
  ],
  "prerequisites": [
    "Scheme-15: Lazy Evaluation"
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

# SCHEME-16-OOP: OOP in Scheme

## Introduction

Object patterns. By the end of this lesson you will be able to: Build objects with closures; Encapsulate state; Create messages; Use dispatch.

## Key Concepts

### 1. Build objects with closures

Target: Build objects with closures. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```scheme
(define (make-counter)
  (let ((count 0))
    (lambda (msg)
      (case msg
        ((inc) (set! count (+ count 1)))
        ((get) count)))))
```
### 2. Encapsulate state

Target: Encapsulate state. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```scheme
(define c (make-counter))
(c 'inc)
(c 'get)
```
### 3. Create messages

Target: Create messages. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```scheme
(define (make-point x y)
  (lambda (op)
    (cond ((eq? op 'x) x)
          ((eq? op 'y) y))))
```
### 4. Use dispatch

Target: Use dispatch. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```scheme
(define (make-account balance)
  (lambda (amount)
    (set! balance (+ balance amount))
    balance))
```

## Practice Questions

1. What is the key idea behind "OOP in Scheme"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain OOP in Scheme with analogies and real-world examples"
1. "Show me common mistakes beginners make with OOP in Scheme"
1. "Provide advanced patterns and performance considerations for OOP in Scheme"

## Key Takeaways

- Master the core ideas of OOP in Scheme through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
