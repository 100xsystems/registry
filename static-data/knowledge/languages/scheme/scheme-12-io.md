---
{
  "title": "Input/Output",
  "description": "Read and write.",
  "type": "lesson",
  "order": 12,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Display output",
    "Read input",
    "Read files",
    "Write files"
  ],
  "knowledge_refs": [
    "scheme/scheme-12-io"
  ],
  "prerequisites": [
    "Scheme-11: Pairs and Association Lists"
  ],
  "references": [
    {
      "title": "Scheme Reports",
      "url": "https://small.r7rs.org/",
      "description": "The R7RS specification"
    },
    {
      "title": "Structure and Interpretation of Computer Programs",
      "url": "https://mitp-press.mit.edu/sites/default/files/sicp/full-text/book/book.html",
      "description": "SICP — the classic book"
    },
    {
      "title": "The Scheme Programming Language",
      "url": "https://www.scheme.com/tspl4/",
      "description": "Dybvig's book"
    }
  ]
}
---

# SCHEME-12-IO: Input/Output

## Introduction

Read and write. By the end of this lesson you will be able to: Display output; Read input; Read files; Write files.

## Key Concepts

### 1. Display output

Target: Display output. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```scheme
(display "hello")
(newline)
```
### 2. Read input

Target: Read input. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```scheme
(define line (read-line))
(display line)
```
### 3. Read files

Target: Read files. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```scheme
(call-with-input-file "data.txt" (lambda (in) (read-line in)))
```
### 4. Write files

Target: Write files. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```scheme
(call-with-output-file "out.txt" (lambda (out) (display "hello" out)))
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
