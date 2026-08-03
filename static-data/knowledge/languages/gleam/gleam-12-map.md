---
{
  "title": "Maps",
  "description": "Key-value storage.",
  "type": "lesson",
  "order": 12,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create maps",
    "Insert and get",
    "Iterate entries",
    "Update values"
  ],
  "knowledge_refs": [
    "gleam/gleam-12-map"
  ],
  "prerequisites": [
    "Gleam-11: String Functions"
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

# GLEAM-12-MAP: Maps

## Introduction

Key-value storage. By the end of this lesson you will be able to: Create maps; Insert and get; Iterate entries; Update values.

## Key Concepts

### 1. Create maps

Target: Create maps. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```gleam
import gleam/map

pub fn main() {
  let ages = map.new()
  let ages = map.insert(ages, "Ada", 36)
  io.debug(ages)
}
```
### 2. Insert and get

Target: Insert and get. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```gleam
map.get(ages, "Ada")
```
### 3. Iterate entries

Target: Iterate entries. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```gleam
let ages = map.insert(ages, "Grace", 85)
map.keys(ages)
```
### 4. Update values

Target: Update values. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```gleam
map.values(ages)
```

## Practice Questions

1. What is the key idea behind "Maps"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Maps with analogies and real-world examples"
1. "Show me common mistakes beginners make with Maps"
1. "Provide advanced patterns and performance considerations for Maps"

## Key Takeaways

- Master the core ideas of Maps through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
