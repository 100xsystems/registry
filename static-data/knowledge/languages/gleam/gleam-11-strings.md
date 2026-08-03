---
{
  "title": "String Functions",
  "description": "Manipulate text.",
  "type": "lesson",
  "order": 11,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Concatenate strings",
    "Split and join",
    "Get length",
    "Convert cases"
  ],
  "knowledge_refs": [
    "gleam/gleam-11-strings"
  ],
  "prerequisites": [
    "Gleam-10: Modules"
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

# GLEAM-11-STRINGS: String Functions

## Introduction

Manipulate text. By the end of this lesson you will be able to: Concatenate strings; Split and join; Get length; Convert cases.

## Key Concepts

### 1. Concatenate strings

Target: Concatenate strings. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```gleam
import gleam/string

pub fn main() {
  io.println(string.concat(["a", "b", "c"]))
}
```
### 2. Split and join

Target: Split and join. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```gleam
let parts = string.split("a,b,c", ",")
```
### 3. Get length

Target: Get length. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```gleam
io.debug(string.length("hello"))
```
### 4. Convert cases

Target: Convert cases. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```gleam
io.println(string.uppercase("hello"))
```

## Practice Questions

1. What is the key idea behind "String Functions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain String Functions with analogies and real-world examples"
1. "Show me common mistakes beginners make with String Functions"
1. "Provide advanced patterns and performance considerations for String Functions"

## Key Takeaways

- Master the core ideas of String Functions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
