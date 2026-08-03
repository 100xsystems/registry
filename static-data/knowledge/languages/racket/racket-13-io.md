---
{
  "title": "Input/Output",
  "description": "Read and write.",
  "type": "lesson",
  "order": 13,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write to stdout",
    "Read from stdin",
    "Read files",
    "Write files"
  ],
  "knowledge_refs": [
    "racket/racket-13-io"
  ],
  "prerequisites": [
    "Racket-12: Exceptions"
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

# RACKET-13-IO: Input/Output

## Introduction

Read and write. By the end of this lesson you will be able to: Write to stdout; Read from stdin; Read files; Write files.

## Key Concepts

### 1. Write to stdout

Target: Write to stdout. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```racket
#lang racket
(displayln "hello")
(display "no newline")
```
### 2. Read from stdin

Target: Read from stdin. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```racket
(define line (read-line))
(displayln line)
```
### 3. Read files

Target: Read files. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```racket
(define text (file->string "data.txt"))
```
### 4. Write files

Target: Write files. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```racket
(call-with-output-file "out.txt"
  (lambda (out) (displayln "hello" out)))
```

## Practice Questions

1. What is the key idea behind "Input/Output"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Input/Output with analogies and real-world examples"
1. "Show me common mistakes beginners make with Input/Output"
1. "Provide advanced patterns and performance considerations for Input/Output"

## Key Takeaways

- Master the core ideas of Input/Output through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
