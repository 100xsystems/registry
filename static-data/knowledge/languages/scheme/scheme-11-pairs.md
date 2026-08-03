---
{
  "title": "Pairs and Association Lists",
  "description": "Key-value pairs.",
  "type": "lesson",
  "order": 11,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create pairs",
    "Use assoc",
    "Use assq",
    "Build association lists"
  ],
  "knowledge_refs": [
    "scheme/scheme-11-pairs"
  ],
  "prerequisites": [
    "Scheme-10: Vectors"
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

# SCHEME-11-PAIRS: Pairs and Association Lists

## Introduction

Key-value pairs. By the end of this lesson you will be able to: Create pairs; Use assoc; Use assq; Build association lists.

## Key Concepts

### 1. Create pairs

Target: Create pairs. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```scheme
(cons "key" 42)
```
### 2. Use assoc

Target: Use assoc. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```scheme
(assoc "key" (list (cons "key" 42)))
```
### 3. Use assq

Target: Use assq. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```scheme
(assq 'a '((a . 1) (b . 2)))
```
### 4. Build association lists

Target: Build association lists. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```scheme
(define al '((a . 1) (b . 2)))
(cdr (assq 'a al))
```

## Practice Questions

1. What is the key idea behind "Pairs and Association Lists"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Pairs and Association Lists with analogies and real-world examples"
1. "Show me common mistakes beginners make with Pairs and Association Lists"
1. "Provide advanced patterns and performance considerations for Pairs and Association Lists"

## Key Takeaways

- Master the core ideas of Pairs and Association Lists through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
