---
{
  "title": "File Input/Output",
  "description": "Read and write files.",
  "type": "lesson",
  "order": 12,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Read whole files",
    "Write files",
    "Read line by line",
    "Handle file errors"
  ],
  "knowledge_refs": [
    "nim/nim-12-file-io"
  ],
  "prerequisites": [
    "Nim-11: Tables and Sets"
  ],
  "references": [
    {
      "title": "Nim Manual",
      "url": "https://nim-lang.org/docs/manual.html",
      "description": "Official language manual"
    },
    {
      "title": "Nim by Example",
      "url": "https://nim-by-example.github.io/",
      "description": "Practical Nim examples"
    },
    {
      "title": "Nim Tutorial",
      "url": "https://nim-lang.org/docs/tut1.html",
      "description": "Official tutorial"
    },
    {
      "title": "Nim Forum",
      "url": "https://forum.nim-lang.org/",
      "description": "Community discussions"
    }
  ]
}
---

# NIM-12-FILE-IO: File Input/Output

## Introduction

Read and write files. By the end of this lesson you will be able to: Read whole files; Write files; Read line by line; Handle file errors.

## Key Concepts

### 1. Read whole files

Target: Read whole files. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```nim
let content = readFile("data.txt")
echo content
```
### 2. Write files

Target: Write files. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```nim
writeFile("out.txt", "hello")
```
### 3. Read line by line

Target: Read line by line. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```nim
for line in lines("data.txt"):
  echo line
```
### 4. Handle file errors

Target: Handle file errors. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```nim
import std/os
if fileExists("data.txt"):
  echo "exists"
```

## Practice Questions

1. What is the key idea behind "File Input/Output"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain File Input/Output with analogies and real-world examples"
1. "Show me common mistakes beginners make with File Input/Output"
1. "Provide advanced patterns and performance considerations for File Input/Output"

## Key Takeaways

- Master the core ideas of File Input/Output through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
