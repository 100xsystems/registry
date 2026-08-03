---
{
  "title": "Getting Started with Scheme",
  "description": "Install a Scheme, hello world.",
  "type": "lesson",
  "order": 1,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Install a Scheme implementation",
    "Write hello world",
    "Evaluate expressions",
    "Run scripts"
  ],
  "knowledge_refs": [
    "scheme/scheme-01-getting-started"
  ],
  "prerequisites": [
    "None — this is the entry point"
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

# SCHEME-01-GETTING-STARTED: Getting Started with Scheme

## Introduction

Install a Scheme, hello world. By the end of this lesson you will be able to: Install a Scheme implementation; Write hello world; Evaluate expressions; Run scripts.

## Key Concepts

### 1. Install a Scheme implementation

Target: Install a Scheme implementation. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```scheme
(display "Hello, World!")
(newline)
```
### 2. Write hello world

Target: Write hello world. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```scheme
(displayln "Hello, World!")   ; some implementations
```
### 3. Evaluate expressions

Target: Evaluate expressions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```scheme
guile -s hello.scm
```
### 4. Run scripts

Target: Run scripts. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```scheme
(display (+ 1 2))
(newline)
```

## Practice Questions

1. What is the key idea behind "Getting Started with Scheme"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with Scheme with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with Scheme"
1. "Provide advanced patterns and performance considerations for Getting Started with Scheme"

## Key Takeaways

- Master the core ideas of Getting Started with Scheme through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
