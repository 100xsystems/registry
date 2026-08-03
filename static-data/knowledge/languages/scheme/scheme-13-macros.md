---
{
  "title": "Macros",
  "description": "define-syntax and hygiene.",
  "type": "lesson",
  "order": 13,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Write define-syntax-rule",
    "Use syntax-rules",
    "Generate code",
    "Understand hygiene"
  ],
  "knowledge_refs": [
    "scheme/scheme-13-macros"
  ],
  "prerequisites": [
    "Scheme-12: Input/Output"
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

# SCHEME-13-MACROS: Macros

## Introduction

define-syntax and hygiene. By the end of this lesson you will be able to: Write define-syntax-rule; Use syntax-rules; Generate code; Understand hygiene.

## Key Concepts

### 1. Write define-syntax-rule

Target: Write define-syntax-rule. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```scheme
(define-syntax-rule (twice expr)
  (begin expr expr))

(twice (display "hi"))
```
### 2. Use syntax-rules

Target: Use syntax-rules. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```scheme
(define-syntax my-when
  (syntax-rules ()
    [(_ test body ...)
     (if test (begin body ...))]))
```
### 3. Generate code

Target: Generate code. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```scheme
(my-when (> 3 2) (display "yes"))
```
### 4. Understand hygiene

Target: Understand hygiene. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```scheme
(define-syntax-rule (unless test body ...)
  (when (not test) body ...))
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
