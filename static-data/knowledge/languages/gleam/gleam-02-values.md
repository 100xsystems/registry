---
{
  "title": "Values and Types",
  "description": "Integers, floats, strings, bools.",
  "type": "lesson",
  "order": 2,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use integer and float types",
    "Work with strings",
    "Use booleans",
    "Use type annotations"
  ],
  "knowledge_refs": [
    "gleam/gleam-02-values"
  ],
  "prerequisites": [
    "Gleam-01: Getting Started with Gleam"
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

# GLEAM-02-VALUES: Values and Types

## Introduction

Integers, floats, strings, bools. By the end of this lesson you will be able to: Use integer and float types; Work with strings; Use booleans; Use type annotations.

## Key Concepts

### 1. Use integer and float types

Target: Use integer and float types. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```gleam
pub fn main() {
  let x = 42
  let pi = 3.14
  io.debug(x)
  io.debug(pi)
}
```
### 2. Work with strings

Target: Work with strings. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```gleam
let name: String = "Ada"
let age: Int = 36
```
### 3. Use booleans

Target: Use booleans. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```gleam
let ok = True
let not_ok = False
```
### 4. Use type annotations

Target: Use type annotations. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```gleam
io.debug(1 + 2)
io.debug(1.5 + 2.5)
```

## Practice Questions

1. What is the key idea behind "Values and Types"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Values and Types with analogies and real-world examples"
1. "Show me common mistakes beginners make with Values and Types"
1. "Provide advanced patterns and performance considerations for Values and Types"

## Key Takeaways

- Master the core ideas of Values and Types through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
