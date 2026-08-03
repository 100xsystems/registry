---
{
  "title": "Functions",
  "description": "Typed functions and pipelines.",
  "type": "lesson",
  "order": 4,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Write typed functions",
    "Use pipelines with |>",
    "Use anonymous functions",
    "Compose functions"
  ],
  "knowledge_refs": [
    "gleam/gleam-04-functions"
  ],
  "prerequisites": [
    "Gleam-03: Control Flow"
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

# GLEAM-04-FUNCTIONS: Functions

## Introduction

Typed functions and pipelines. By the end of this lesson you will be able to: Write typed functions; Use pipelines with |>; Use anonymous functions; Compose functions.

## Key Concepts

### 1. Write typed functions

Target: Write typed functions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```gleam
pub fn add(a: Int, b: Int) -> Int {
  a + b
}
```
### 2. Use pipelines with |>

Target: Use pipelines with |>. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```gleam
pub fn double(x: Int) -> Int {
  x * 2
}

pub fn main() {
  21 |> double |> io.debug
}
```
### 3. Use anonymous functions

Target: Use anonymous functions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```gleam
let square = fn(x) { x * x }
io.debug(square(5))
```
### 4. Compose functions

Target: Compose functions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```gleam
pub fn apply(f: fn(Int) -> Int, x: Int) -> Int {
  f(x)
}
```

## Practice Questions

1. What is the key idea behind "Functions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Functions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Functions"
1. "Provide advanced patterns and performance considerations for Functions"

## Key Takeaways

- Master the core ideas of Functions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
