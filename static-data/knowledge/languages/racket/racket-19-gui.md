---
{
  "title": "GUI Programming",
  "description": "Build interfaces with racket/gui.",
  "type": "lesson",
  "order": 19,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Create a frame",
    "Add widgets",
    "Handle events",
    "Run the event loop"
  ],
  "knowledge_refs": [
    "racket/racket-19-gui"
  ],
  "prerequisites": [
    "Racket-18: Threads and Concurrency"
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

# RACKET-19-GUI: GUI Programming

## Introduction

Build interfaces with racket/gui. By the end of this lesson you will be able to: Create a frame; Add widgets; Handle events; Run the event loop.

## Key Concepts

### 1. Create a frame

Target: Create a frame. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```racket
#lang racket
(require racket/gui/base)

(define frame (new frame% [label "Hello"] [width 300] [height 200]))
(send frame show #t)
```
### 2. Add widgets

Target: Add widgets. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```racket
(define msg (new message% [parent frame] [label "Hello, World!"]))
```
### 3. Handle events

Target: Handle events. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```racket
(define btn (new button% [parent frame] [label "Click"]
                          [callback (lambda (b e) (displayln "clicked"))]))
```
### 4. Run the event loop

Target: Run the event loop. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```racket
(require racket/gui/base)
```

## Practice Questions

1. What is the key idea behind "GUI Programming"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain GUI Programming with analogies and real-world examples"
1. "Show me common mistakes beginners make with GUI Programming"
1. "Provide advanced patterns and performance considerations for GUI Programming"

## Key Takeaways

- Master the core ideas of GUI Programming through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
