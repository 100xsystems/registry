---
{
  "title": "Objects and Classes",
  "description": "Racket OOP.",
  "type": "lesson",
  "order": 17,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Define classes",
    "Create instances",
    "Use methods",
    "Use inheritance"
  ],
  "knowledge_refs": [
    "racket/racket-17-oop"
  ],
  "prerequisites": [
    "Racket-16: Pattern Matching"
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

# RACKET-17-OOP: Objects and Classes

## Introduction

Racket OOP. By the end of this lesson you will be able to: Define classes; Create instances; Use methods; Use inheritance.

## Key Concepts

### 1. Define classes

Target: Define classes. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```racket
#lang racket
(define animal%
  (class object%
    (super-new)
    (define/public (speak) "...")))
```
### 2. Create instances

Target: Create instances. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```racket
(define dog%
  (class animal%
    (super-new)
    (define/override (speak) "Woof")))
```
### 3. Use methods

Target: Use methods. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```racket
(define d (new dog%))
(send d speak)
```
### 4. Use inheritance

Target: Use inheritance. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```racket
(define counter%
  (class object%
    (super-new)
    (define count 0)
    (define/public (increment!) (set! count (add1 count)))
    (define/public (get-count) count)))
```

## Practice Questions

1. What is the key idea behind "Objects and Classes"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Objects and Classes with analogies and real-world examples"
1. "Show me common mistakes beginners make with Objects and Classes"
1. "Provide advanced patterns and performance considerations for Objects and Classes"

## Key Takeaways

- Master the core ideas of Objects and Classes through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
