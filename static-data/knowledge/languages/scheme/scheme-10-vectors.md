---
{
  "title": "Vectors",
  "description": "Random-access arrays.",
  "type": "lesson",
  "order": 10,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create vectors",
    "Access elements",
    "Update elements",
    "Convert to lists"
  ],
  "knowledge_refs": [
    "scheme/scheme-10-vectors"
  ],
  "prerequisites": [
    "Scheme-09: Strings"
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

# SCHEME-10-VECTORS: Vectors

## Introduction

Random-access arrays. By the end of this lesson you will be able to: Create vectors; Access elements; Update elements; Convert to lists.

## Key Concepts

### 1. Create vectors

Target: Create vectors. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```scheme
(vector 1 2 3)
```
### 2. Access elements

Target: Access elements. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```scheme
(vector-ref (vector 1 2 3) 1)
```
### 3. Update elements

Target: Update elements. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```scheme
(define v (make-vector 3 0))
(vector-set! v 0 42)
```
### 4. Convert to lists

Target: Convert to lists. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```scheme
(vector->list (vector 1 2))
```

## Practice Questions

1. What is the key idea behind "Vectors"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Vectors with analogies and real-world examples"
1. "Show me common mistakes beginners make with Vectors"
1. "Provide advanced patterns and performance considerations for Vectors"

## Key Takeaways

- Master the core ideas of Vectors through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
