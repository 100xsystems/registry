---
{
  "title": "Pattern Matching",
  "description": "match expressions.",
  "type": "lesson",
  "order": 16,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use match",
    "Match structures",
    "Use match-let",
    "Bind with patterns"
  ],
  "knowledge_refs": [
    "racket/racket-16-matching"
  ],
  "prerequisites": [
    "Racket-15: Modules"
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

# RACKET-16-MATCHING: Pattern Matching

## Introduction

match expressions. By the end of this lesson you will be able to: Use match; Match structures; Use match-let; Bind with patterns.

## Key Concepts

### 1. Use match

Target: Use match. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```racket
#lang racket
(match 5
  [0 "zero"]
  [n (format "number ~a" n)])
```
### 2. Match structures

Target: Match structures. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```racket
(match (list 1 2 3)
  [(list a b c) (+ a b c)])
```
### 3. Use match-let

Target: Use match-let. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```racket
(match (struct point (1 2))
  [(point x y) (+ x y)])
```
### 4. Bind with patterns

Target: Bind with patterns. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```racket
(match-define (list a b) (list 1 2))
a
```

## Practice Questions

1. What is the key idea behind "Pattern Matching"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Pattern Matching with analogies and real-world examples"
1. "Show me common mistakes beginners make with Pattern Matching"
1. "Provide advanced patterns and performance considerations for Pattern Matching"

## Key Takeaways

- Master the core ideas of Pattern Matching through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
