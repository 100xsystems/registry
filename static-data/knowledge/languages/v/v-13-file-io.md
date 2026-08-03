---
{
  "title": "File I/O",
  "description": "Read and write files.",
  "type": "lesson",
  "order": 13,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Read files",
    "Write files",
    "Read lines",
    "Handle paths"
  ],
  "knowledge_refs": [
    "v/v-13-file-io"
  ],
  "prerequisites": [
    "V-12: Generics"
  ],
  "references": [
    {
      "title": "V Documentation",
      "url": "https://docs.vlang.io/",
      "description": "Official docs"
    },
    {
      "title": "V Manual",
      "url": "https://docs.vlang.io/introduction.html",
      "description": "Language manual"
    },
    {
      "title": "V Language GitHub",
      "url": "https://github.com/vlang/v",
      "description": "Source code"
    }
  ]
}
---

# V-13-FILE-IO: File I/O

## Introduction

Read and write files. By the end of this lesson you will be able to: Read files; Write files; Read lines; Handle paths.

## Key Concepts

### 1. Read files

Target: Read files. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```v
import os

content := os.read_file("data.txt") or { panic(err) }
println(content)
```
### 2. Write files

Target: Write files. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```v
os.write_file("out.txt", "hello") or { panic(err) }
```
### 3. Read lines

Target: Read lines. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```v
for line in os.read_lines("data.txt") or { [] } {
	println(line)
}
```
### 4. Handle paths

Target: Handle paths. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```v
println(os.exists("data.txt"))
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
