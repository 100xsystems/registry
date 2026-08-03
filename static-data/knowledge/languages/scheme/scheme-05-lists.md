---
{
  "title": "Lists",
  "description": "The fundamental data structure.",
  "type": "lesson",
  "order": 5,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create lists",
    "Use car and cdr",
    "Use cons",
    "Process lists"
  ],
  "knowledge_refs": [
    "scheme/scheme-05-lists"
  ],
  "prerequisites": [
    "Scheme-04: Functions"
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

# SCHEME-05-LISTS: Lists

## Introduction

The fundamental data structure. By the end of this lesson you will be able to: Create lists; Use car and cdr; Use cons; Process lists.

## Key Concepts

### 1. Create lists

Target: Create lists. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```scheme
(list 1 2 3)
```
### 2. Use car and cdr

Target: Use car and cdr. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```scheme
(cons 0 (list 1 2))
```
### 3. Use cons

Target: Use cons. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```scheme
(car (list 1 2 3))
(cdr (list 1 2 3))
```
### 4. Process lists

Target: Process lists. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```scheme
(map (lambda (x) (* x 2)) (list 1 2 3))
```

## Practice Questions

1. What is the key idea behind "Lists"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Lists with analogies and real-world examples"
1. "Show me common mistakes beginners make with Lists"
1. "Provide advanced patterns and performance considerations for Lists"

## Key Takeaways

- Master the core ideas of Lists through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
