---
{
  "title": "Getting Started with Nim",
  "description": "Install, compile, and run your first program.",
  "type": "lesson",
  "order": 1,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Install Nim via choosenim",
    "Compile with nim c",
    "Write hello world",
    "Understand nimble packages"
  ],
  "knowledge_refs": [
    "nim/nim-01-getting-started"
  ],
  "prerequisites": [
    "None — this is the entry point"
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

# NIM-01-GETTING-STARTED: Getting Started with Nim

## Introduction

Install, compile, and run your first program. By the end of this lesson you will be able to: Install Nim via choosenim; Compile with nim c; Write hello world; Understand nimble packages.

## Key Concepts

### 1. Install Nim via choosenim

Target: Install Nim via choosenim. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```nim
echo "Hello, World!"
```
### 2. Compile with nim c

Target: Compile with nim c. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```nim
nim c -r hello.nim
```
### 3. Write hello world

Target: Write hello world. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```nim
import std/strutils

echo "Hello, " & "Nim!"
```
### 4. Understand nimble packages

Target: Understand nimble packages. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```nim
const version = "1.0.0"
echo "Nim version: ", NimVersion
```

## Practice Questions

1. What is the key idea behind "Getting Started with Nim"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with Nim with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with Nim"
1. "Provide advanced patterns and performance considerations for Getting Started with Nim"

## Key Takeaways

- Master the core ideas of Getting Started with Nim through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
