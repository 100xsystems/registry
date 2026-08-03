---
{
  "title": "Threads and Concurrency",
  "description": "Parallel execution.",
  "type": "lesson",
  "order": 18,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Spawn threads",
    "Use semaphores",
    "Synchronize access",
    "Use channels"
  ],
  "knowledge_refs": [
    "racket/racket-18-threads"
  ],
  "prerequisites": [
    "Racket-17: Objects and Classes"
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

# RACKET-18-THREADS: Threads and Concurrency

## Introduction

Parallel execution. By the end of this lesson you will be able to: Spawn threads; Use semaphores; Synchronize access; Use channels.

## Key Concepts

### 1. Spawn threads

Target: Spawn threads. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```racket
#lang racket
(thread (lambda () (displayln "in thread")))
```
### 2. Use semaphores

Target: Use semaphores. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```racket
(define s (make-semaphore 1))
(semaphore-wait s)
; critical section
(semaphore-post s)
```
### 3. Synchronize access

Target: Synchronize access. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```racket
(define ch (make-channel))
(thread (lambda () (channel-put ch 42)))
(displayln (channel-get ch))
```
### 4. Use channels

Target: Use channels. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```racket
(make-thread-pool 4)
```

## Practice Questions

1. What is the key idea behind "Threads and Concurrency"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Threads and Concurrency with analogies and real-world examples"
1. "Show me common mistakes beginners make with Threads and Concurrency"
1. "Provide advanced patterns and performance considerations for Threads and Concurrency"

## Key Takeaways

- Master the core ideas of Threads and Concurrency through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
