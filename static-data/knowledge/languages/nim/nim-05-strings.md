---
{
  "title": "Strings",
  "description": "String operations and formatting.",
  "type": "lesson",
  "order": 5,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Concatenate strings",
    "Format with & and fmt",
    "Split and join",
    "Convert between types"
  ],
  "knowledge_refs": [
    "nim/nim-05-strings"
  ],
  "prerequisites": [
    "Nim-04: Sequences and Arrays"
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

# NIM-05-STRINGS: Strings

## Introduction

String operations and formatting. By the end of this lesson you will be able to: Concatenate strings; Format with & and fmt; Split and join; Convert between types.

## Key Concepts

### 1. Concatenate strings

Target: Concatenate strings. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```nim
import std/strutils

let a = "Hello"
let b = a & " " & "World"
echo b
```
### 2. Format with & and fmt

Target: Format with & and fmt. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```nim
let name = "Ada"
echo "Hi, ", name, "!"
```
### 3. Split and join

Target: Split and join. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```nim
import std/strformat
let x = 42
echo fmt"value = {x}"
```
### 4. Convert between types

Target: Convert between types. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```nim
let parts = "a,b,c".split(",")
echo parts.join(" | ")
```

## Practice Questions

1. What is the key idea behind "Strings"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Strings with analogies and real-world examples"
1. "Show me common mistakes beginners make with Strings"
1. "Provide advanced patterns and performance considerations for Strings"

## Key Takeaways

- Master the core ideas of Strings through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
