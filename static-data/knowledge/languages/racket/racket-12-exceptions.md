---
{
  "title": "Exceptions",
  "description": "Raise and handle errors.",
  "type": "lesson",
  "order": 12,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Raise errors",
    "Handle with with-handlers",
    "Use error",
    "Create custom errors"
  ],
  "knowledge_refs": [
    "racket/racket-12-exceptions"
  ],
  "prerequisites": [
    "Racket-11: Hash Tables"
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

# RACKET-12-EXCEPTIONS: Exceptions

## Introduction

Raise and handle errors. By the end of this lesson you will be able to: Raise errors; Handle with with-handlers; Use error; Create custom errors.

## Key Concepts

### 1. Raise errors

Target: Raise errors. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```racket
#lang racket
(with-handlers ([exn:fail? (lambda (e) (displayln "caught"))])
  (error "boom"))
```
### 2. Handle with with-handlers

Target: Handle with with-handlers. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```racket
(raise "simple error")
```
### 3. Use error

Target: Use error. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```racket
(with-handlers ([exn:fail:contract? (lambda (e) "contract error")])
  (car 5))
```
### 4. Create custom errors

Target: Create custom errors. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```racket
(error "custom message")
```

## Practice Questions

1. What is the key idea behind "Exceptions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Exceptions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Exceptions"
1. "Provide advanced patterns and performance considerations for Exceptions"

## Key Takeaways

- Master the core ideas of Exceptions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
