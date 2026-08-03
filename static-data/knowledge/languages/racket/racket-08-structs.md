---
{
  "title": "Structs",
  "description": "Custom data types.",
  "type": "lesson",
  "order": 8,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define structs",
    "Create instances",
    "Access fields",
    "Use struct predicates"
  ],
  "knowledge_refs": [
    "racket/racket-08-structs"
  ],
  "prerequisites": [
    "Racket-07: Iteration"
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

# RACKET-08-STRUCTS: Structs

## Introduction

Custom data types. By the end of this lesson you will be able to: Define structs; Create instances; Access fields; Use struct predicates.

## Key Concepts

### 1. Define structs

Target: Define structs. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```racket
#lang racket
(struct person (name age))
(define ada (person "Ada" 36))
(displayln (person-name ada))
```
### 2. Create instances

Target: Create instances. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```racket
(struct point (x y))
(define p (point 1 2))
```
### 3. Access fields

Target: Access fields. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```racket
(point? p)
(person? p)
```
### 4. Use struct predicates

Target: Use struct predicates. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```racket
(struct circle (radius) #:transparent)
```

## Practice Questions

1. What is the key idea behind "Structs"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Structs with analogies and real-world examples"
1. "Show me common mistakes beginners make with Structs"
1. "Provide advanced patterns and performance considerations for Structs"

## Key Takeaways

- Master the core ideas of Structs through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
