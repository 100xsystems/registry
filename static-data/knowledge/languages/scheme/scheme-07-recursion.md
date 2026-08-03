---
{
  "title": "Recursion",
  "description": "Recursive definitions.",
  "type": "lesson",
  "order": 7,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write recursive functions",
    "Use tail recursion",
    "Use named let",
    "Process trees"
  ],
  "knowledge_refs": [
    "scheme/scheme-07-recursion"
  ],
  "prerequisites": [
    "Scheme-06: Conditionals"
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

# SCHEME-07-RECURSION: Recursion

## Introduction

Recursive definitions. By the end of this lesson you will be able to: Write recursive functions; Use tail recursion; Use named let; Process trees.

## Key Concepts

### 1. Write recursive functions

Target: Write recursive functions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```scheme
(define (fact n)
  (if (<= n 1)
      1
      (* n (fact (- n 1)))))
```
### 2. Use tail recursion

Target: Use tail recursion. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```scheme
(define (loop acc n)
  (if (= n 0)
      acc
      (loop (+ acc n) (- n 1))))
```
### 3. Use named let

Target: Use named let. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```scheme
(define (length lst)
  (if (null? lst)
      0
      (+ 1 (length (cdr lst)))))
```
### 4. Process trees

Target: Process trees. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```scheme
(define (even-count lst)
  (let loop ((l lst) (acc 0))
    (cond ((null? l) acc)
          ((even? (car l)) (loop (cdr l) (+ acc 1)))
          (else (loop (cdr l) acc)))))
```

## Practice Questions

1. What is the key idea behind "Recursion"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Recursion with analogies and real-world examples"
1. "Show me common mistakes beginners make with Recursion"
1. "Provide advanced patterns and performance considerations for Recursion"

## Key Takeaways

- Master the core ideas of Recursion through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
