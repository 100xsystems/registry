---
{
  "title": "Tail Calls and CPS",
  "description": "Efficient recursion.",
  "type": "lesson",
  "order": 14,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Understand tail calls",
    "Write accumulator style",
    "Use call/cc",
    "Understand continuations"
  ],
  "knowledge_refs": [
    "scheme/scheme-14-tail-calls"
  ],
  "prerequisites": [
    "Scheme-13: Macros"
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

# SCHEME-14-TAIL-CALLS: Tail Calls and CPS

## Introduction

Efficient recursion. By the end of this lesson you will be able to: Understand tail calls; Write accumulator style; Use call/cc; Understand continuations.

## Key Concepts

### 1. Understand tail calls

Target: Understand tail calls. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```scheme
(define (loop acc n)
  (if (= n 0) acc (loop (+ acc n) (- n 1))))
(loop 0 1000000)
```
### 2. Write accumulator style

Target: Write accumulator style. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```scheme
(define (fact n) (fact-iter n 1))
(define (fact-iter n acc)
  (if (= n 0) acc (fact-iter (- n 1) (* n acc))))
```
### 3. Use call/cc

Target: Use call/cc. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```scheme
(call/cc (lambda (k) (k 42)))
```
### 4. Understand continuations

Target: Understand continuations. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```scheme
(define (double k) (k 42))
```

## Practice Questions

1. What is the key idea behind "Tail Calls and CPS"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Tail Calls and CPS with analogies and real-world examples"
1. "Show me common mistakes beginners make with Tail Calls and CPS"
1. "Provide advanced patterns and performance considerations for Tail Calls and CPS"

## Key Takeaways

- Master the core ideas of Tail Calls and CPS through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
