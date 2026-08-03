---
{
  "title": "Input/Output",
  "description": "Read and write streams.",
  "type": "lesson",
  "order": 13,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write to stdout",
    "Read from stdin",
    "Open files",
    "Format streams"
  ],
  "knowledge_refs": [
    "common-lisp/common-lisp-13-io"
  ],
  "prerequisites": [
    "Common Lisp-12: Conditions and Restarts"
  ],
  "references": [
    {
      "title": "Practical Common Lisp",
      "url": "https://gigamonkeys.com/book/",
      "description": "The classic online book"
    },
    {
      "title": "Common Lisp HyperSpec",
      "url": "http://www.lispworks.com/documentation/HyperSpec/Front/Contents.htm",
      "description": "Official standard reference"
    },
    {
      "title": "Common Lisp Cookbook",
      "url": "https://lispcookbook.github.io/cl-cookbook/",
      "description": "Community cookbook"
    }
  ]
}
---

# COMMON-LISP-13-IO: Input/Output

## Introduction

Read and write streams. By the end of this lesson you will be able to: Write to stdout; Read from stdin; Open files; Format streams.

## Key Concepts

### 1. Write to stdout

Target: Write to stdout. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```lisp
(format t "hello~%")
```
### 2. Read from stdin

Target: Read from stdin. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```lisp
(read-line)
```
### 3. Open files

Target: Open files. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```lisp
(with-open-file (s "data.txt" :direction :output)
  (format s "hello~%"))
```
### 4. Format streams

Target: Format streams. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```lisp
(with-open-file (s "data.txt" :direction :input)
  (read-line s))
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
