---
{
  "title": "Modules",
  "description": "Organize code with modules.",
  "type": "lesson",
  "order": 10,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create modules",
    "Import modules",
    "Control exports",
    "Use aliases"
  ],
  "knowledge_refs": [
    "gleam/gleam-10-modules"
  ],
  "prerequisites": [
    "Gleam-09: Records"
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

# GLEAM-10-MODULES: Modules

## Introduction

Organize code with modules. By the end of this lesson you will be able to: Create modules; Import modules; Control exports; Use aliases.

## Key Concepts

### 1. Create modules

Target: Create modules. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```gleam
// src/math.gleam
pub fn square(x: Int) -> Int {
  x * x
}
```
### 2. Import modules

Target: Import modules. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```gleam
import math

pub fn main() {
  io.debug(math.square(5))
}
```
### 3. Control exports

Target: Control exports. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```gleam
import gleam/string as str

pub fn main() {
  io.println(str.uppercase("hi"))
}
```
### 4. Use aliases

Target: Use aliases. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```gleam
pub fn public_fn() { "visible" }
fn private_fn() { "hidden" }
```

## Practice Questions

1. What is the key idea behind "Modules"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Modules with analogies and real-world examples"
1. "Show me common mistakes beginners make with Modules"
1. "Provide advanced patterns and performance considerations for Modules"

## Key Takeaways

- Master the core ideas of Modules through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
