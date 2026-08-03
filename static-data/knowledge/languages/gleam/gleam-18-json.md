---
{
  "title": "JSON",
  "description": "Encode and decode JSON.",
  "type": "lesson",
  "order": 18,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Build JSON values",
    "Encode to string",
    "Decode with dynamic",
    "Validate shapes"
  ],
  "knowledge_refs": [
    "gleam/gleam-18-json"
  ],
  "prerequisites": [
    "Gleam-17: HTTP Servers"
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

# GLEAM-18-JSON: JSON

## Introduction

Encode and decode JSON. By the end of this lesson you will be able to: Build JSON values; Encode to string; Decode with dynamic; Validate shapes.

## Key Concepts

### 1. Build JSON values

Target: Build JSON values. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```gleam
import gleam/json

let value = json.object([
  #("name", json.string("Ada")),
  #("age", json.int(36)),
])

let text = json.to_string(value)
```
### 2. Encode to string

Target: Encode to string. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```gleam
let decoded = json.decode(text)
```
### 3. Decode with dynamic

Target: Decode with dynamic. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```gleam
import gleam/dynamic

dynamic.field(decoded, "name") |> dynamic.string
```
### 4. Validate shapes

Target: Validate shapes. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```gleam
json.string("hello") |> json.to_string
```

## Practice Questions

1. What is the key idea behind "JSON"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain JSON with analogies and real-world examples"
1. "Show me common mistakes beginners make with JSON"
1. "Provide advanced patterns and performance considerations for JSON"

## Key Takeaways

- Master the core ideas of JSON through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
