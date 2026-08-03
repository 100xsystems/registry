---
{
  "title": "Hash Tables",
  "description": "Key-value storage.",
  "type": "lesson",
  "order": 11,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create hash tables",
    "Set and get",
    "Iterate entries",
    "Remove keys"
  ],
  "knowledge_refs": [
    "racket/racket-11-hash-tables"
  ],
  "prerequisites": [
    "Racket-10: Higher-Order Functions"
  ],
  "references": [
    {
      "title": "Racket Documentation",
      "url": "https://docs.racket-lang.org/",
      "description": "Official docs"
    },
    {
      "title": "How to Design Programs",
      "url": "https://htdp.org/",
      "description": "The classic textbook"
    },
    {
      "title": "Racket Guide",
      "url": "https://docs.racket-lang.org/guide/",
      "description": "Official language guide"
    }
  ]
}
---

# RACKET-11-HASH-TABLES: Hash Tables

## Introduction

Key-value storage. By the end of this lesson you will be able to: Create hash tables; Set and get; Iterate entries; Remove keys.

## Key Concepts

### 1. Create hash tables

Target: Create hash tables. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```racket
#lang racket
(define ht (make-hash))
(hash-set! ht "key" 42)
(displayln (hash-ref ht "key"))
```
### 2. Set and get

Target: Set and get. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```racket
(hash-ref ht "missing" 0)
```
### 3. Iterate entries

Target: Iterate entries. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```racket
(hash-keys ht)
```
### 4. Remove keys

Target: Remove keys. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```racket
(hash-remove! ht "key")
```

## Practice Questions

1. What is the key idea behind "Hash Tables"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Hash Tables with analogies and real-world examples"
1. "Show me common mistakes beginners make with Hash Tables"
1. "Provide advanced patterns and performance considerations for Hash Tables"

## Key Takeaways

- Master the core ideas of Hash Tables through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
