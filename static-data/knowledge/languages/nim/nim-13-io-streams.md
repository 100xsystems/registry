---
{
  "title": "Streams and stdin/stdout",
  "description": "Stream processing and user input.",
  "type": "lesson",
  "order": 13,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Read from stdin",
    "Write to stdout",
    "Use streams",
    "Format output"
  ],
  "knowledge_refs": [
    "nim/nim-13-io-streams"
  ],
  "prerequisites": [
    "Nim-12: File Input/Output"
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

# NIM-13-IO-STREAMS: Streams and stdin/stdout

## Introduction

Stream processing and user input. By the end of this lesson you will be able to: Read from stdin; Write to stdout; Use streams; Format output.

## Key Concepts

### 1. Read from stdin

Target: Read from stdin. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```nim
import std/strutils

let input = readLine(stdin)
echo "You said: ", input
```
### 2. Write to stdout

Target: Write to stdout. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```nim
stdout.write("no newline")
stdout.flushFile()
```
### 3. Use streams

Target: Use streams. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```nim
import std/streams
let s = newStringStream("hello")
echo s.readAll()
```
### 4. Format output

Target: Format output. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```nim
echo "done"  # writes to stdout with newline
```

## Practice Questions

1. What is the key idea behind "Streams and stdin/stdout"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Streams and stdin/stdout with analogies and real-world examples"
1. "Show me common mistakes beginners make with Streams and stdin/stdout"
1. "Provide advanced patterns and performance considerations for Streams and stdin/stdout"

## Key Takeaways

- Master the core ideas of Streams and stdin/stdout through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
