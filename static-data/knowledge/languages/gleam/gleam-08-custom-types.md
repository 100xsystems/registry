---
{
  "title": "Custom Types",
  "description": "Model data with tagged unions.",
  "type": "lesson",
  "order": 8,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define custom types",
    "Create values",
    "Pattern match variants",
    "Carry data in variants"
  ],
  "knowledge_refs": [
    "gleam/gleam-08-custom-types"
  ],
  "prerequisites": [
    "Gleam-07: Option Types"
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

# GLEAM-08-CUSTOM-TYPES: Custom Types

## Introduction

Model data with tagged unions. By the end of this lesson you will be able to: Define custom types; Create values; Pattern match variants; Carry data in variants.

## Key Concepts

### 1. Define custom types

Target: Define custom types. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```gleam
pub type Colour {
  Red
  Green
  Blue
}
```
### 2. Create values

Target: Create values. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```gleam
pub type Shape {
  Circle(Float)
  Square(Float)
}

pub fn area(s: Shape) -> Float {
  case s {
    Circle(r) -> 3.14159 *. r *. r
    Square(side) -> side *. side
  }
}
```
### 3. Pattern match variants

Target: Pattern match variants. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```gleam
pub type State {
  Loading
  Loaded(List(String))
  Failed(String)
}
```
### 4. Carry data in variants

Target: Carry data in variants. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```gleam
let color = Red
let shape = Circle(2.0)
```

## Practice Questions

1. What is the key idea behind "Custom Types"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Custom Types with analogies and real-world examples"
1. "Show me common mistakes beginners make with Custom Types"
1. "Provide advanced patterns and performance considerations for Custom Types"

## Key Takeaways

- Master the core ideas of Custom Types through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
