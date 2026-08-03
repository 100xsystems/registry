---
{
  "title": "Interfacing with C",
  "description": "Call C from Scheme.",
  "type": "lesson",
  "order": 19,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use FFI libraries",
    "Call C functions",
    "Pass numbers",
    "Handle strings"
  ],
  "knowledge_refs": [
    "scheme/scheme-19-ffi"
  ],
  "prerequisites": [
    "Scheme-18: Metacircular Evaluators"
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

# SCHEME-19-FFI: Interfacing with C

## Introduction

Call C from Scheme. By the end of this lesson you will be able to: Use FFI libraries; Call C functions; Pass numbers; Handle strings.

## Key Concepts

### 1. Use FFI libraries

Target: Use FFI libraries. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```scheme
;; Guile:
(use-modules (system foreign))
```
### 2. Call C functions

Target: Call C functions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```scheme
(define libc (dynamic-link "libc"))
(define strlen (pointer->procedure size_t (dynamic-func "strlen" libc) (list '*)))(strlen (string->pointer "hello"))
```
### 3. Pass numbers

Target: Pass numbers. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```scheme
;; Racket: (require ffi/unsafe)
```
### 4. Handle strings

Target: Handle strings. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```scheme
;; Guile:
(use-modules (system foreign))
```

## Practice Questions

1. What is the key idea behind "Interfacing with C"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Interfacing with C with analogies and real-world examples"
1. "Show me common mistakes beginners make with Interfacing with C"
1. "Provide advanced patterns and performance considerations for Interfacing with C"

## Key Takeaways

- Master the core ideas of Interfacing with C through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
