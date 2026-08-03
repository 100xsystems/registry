---
{
  "title": "Build a CLI Tool",
  "description": "Parse args and build tools.",
  "type": "lesson",
  "order": 16,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Parse command-line args",
    "Structure a CLI",
    "Handle options",
    "Exit with codes"
  ],
  "knowledge_refs": [
    "gleam/gleam-16-todo-app"
  ],
  "prerequisites": [
    "Gleam-15: The Erlang Runtime"
  ],
  "references": [
    {
      "title": "Gleam Documentation",
      "url": "https://gleam.run/documentation/",
      "description": "Official docs"
    },
    {
      "title": "Gleam Language Tour",
      "url": "https://tour.gleam.run/",
      "description": "Interactive tour"
    },
    {
      "title": "Gleam Book",
      "url": "https://gleam.run/book/",
      "description": "The official book"
    }
  ]
}
---

# GLEAM-16-TODO-APP: Build a CLI Tool

## Introduction

Parse args and build tools. By the end of this lesson you will be able to: Parse command-line args; Structure a CLI; Handle options; Exit with codes.

## Key Concepts

### 1. Parse command-line args

Target: Parse command-line args. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```gleam
import gleam/argv

pub fn main() {
  let args = argv.load()
  io.debug(args)
}
```
### 2. Structure a CLI

Target: Structure a CLI. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```gleam
pub fn main() {
  case argv.load() {
    [] -> io.println("usage: app NAME")
    [name] -> io.println("Hello, " <> name)
    _ -> io.println("too many args")
  }
}
```
### 3. Handle options

Target: Handle options. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```gleam
import gleam/erlang/process

process.exit(0)
```
### 4. Exit with codes

Target: Exit with codes. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```gleam
io.println("done")
```

## Practice Questions

1. What is the key idea behind "Build a CLI Tool"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Build a CLI Tool with analogies and real-world examples"
1. "Show me common mistakes beginners make with Build a CLI Tool"
1. "Provide advanced patterns and performance considerations for Build a CLI Tool"

## Key Takeaways

- Master the core ideas of Build a CLI Tool through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
