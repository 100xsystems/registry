---
{
  "title": "IO and FFI",
  "description": "Interact with the outside world.",
  "type": "lesson",
  "order": 13,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Print and read input",
    "Use external functions",
    "Call Erlang or JS",
    "Handle untrusted code"
  ],
  "knowledge_refs": [
    "gleam/gleam-13-io-ffi"
  ],
  "prerequisites": [
    "Gleam-12: Maps"
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

# GLEAM-13-IO-FFI: IO and FFI

## Introduction

Interact with the outside world. By the end of this lesson you will be able to: Print and read input; Use external functions; Call Erlang or JS; Handle untrusted code.

## Key Concepts

### 1. Print and read input

Target: Print and read input. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```gleam
import gleam/io

pub fn main() {
  io.println("hello")
}
```
### 2. Use external functions

Target: Use external functions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```gleam
pub external fn system_time() -> Int =
  "erlang" "system_time"

  "node" "Date.now"
```
### 3. Call Erlang or JS

Target: Call Erlang or JS. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```gleam
@external(javascript, "console", "log")
pub fn log(msg: String) -> Nil
```
### 4. Handle untrusted code

Target: Handle untrusted code. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```gleam
import gleam/dynamic

pub fn to_int(value: dynamic.Dynamic) -> Result(Int, String) {
  dynamic.int(value)
}
```

## Practice Questions

1. What is the key idea behind "IO and FFI"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain IO and FFI with analogies and real-world examples"
1. "Show me common mistakes beginners make with IO and FFI"
1. "Provide advanced patterns and performance considerations for IO and FFI"

## Key Takeaways

- Master the core ideas of IO and FFI through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
