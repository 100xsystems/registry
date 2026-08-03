---
{
  "title": "File I/O",
  "description": "Read and write files.",
  "type": "lesson",
  "order": 12,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Open files",
    "Read file content",
    "Write to files",
    "Close streams"
  ],
  "knowledge_refs": [
    "prolog/prolog-12-file-io"
  ],
  "prerequisites": [
    "Prolog-11: Input/Output"
  ],
  "references": [
    {
      "title": "SWI-Prolog Documentation",
      "url": "https://www.swi-prolog.org/pldoc/",
      "description": "Official SWI-Prolog docs"
    },
    {
      "title": "Learn Prolog Now!",
      "url": "https://www.learnprolognow.org/",
      "description": "The classic free textbook"
    },
    {
      "title": "Prolog Wiki",
      "url": "https://en.wikipedia.org/wiki/Prolog",
      "description": "Overview article"
    }
  ]
}
---

# PROLOG-12-FILE-IO: File I/O

## Introduction

Read and write files. By the end of this lesson you will be able to: Open files; Read file content; Write to files; Close streams.

## Key Concepts

### 1. Open files

Target: Open files. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```prolog
open("data.txt", read, Stream),
read_string(Stream, _, Content),
close(Stream).
```
### 2. Read file content

Target: Read file content. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```prolog
open("out.txt", write, Stream),
write(Stream, "hello"),
nl(Stream),
close(Stream).
```
### 3. Write to files

Target: Write to files. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```prolog
setup_call_cleanup(open("f", read, S), read_line(S, L), close(S)).
```
### 4. Close streams

Target: Close streams. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```prolog
forall(
    member(X, [1, 2, 3]),
    (write(X), nl)).
```

## Practice Questions

1. What is the key idea behind "File I/O"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain File I/O with analogies and real-world examples"
1. "Show me common mistakes beginners make with File I/O"
1. "Provide advanced patterns and performance considerations for File I/O"

## Key Takeaways

- Master the core ideas of File I/O through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
