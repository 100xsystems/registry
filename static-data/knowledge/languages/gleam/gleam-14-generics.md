---
{
  "title": "Generics",
  "description": "Type-parameterized code.",
  "type": "lesson",
  "order": 14,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Write generic types",
    "Write generic functions",
    "Use type variables",
    "Build containers"
  ],
  "knowledge_refs": [
    "gleam/gleam-14-generics"
  ],
  "prerequisites": [
    "Gleam-13: IO and FFI"
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

# GLEAM-14-GENERICS: Generics

## Introduction

Type-parameterized code. By the end of this lesson you will be able to: Write generic types; Write generic functions; Use type variables; Build containers.

## Key Concepts

### 1. Write generic types

Target: Write generic types. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```gleam
pub type Box(a) {
  Box(value: a)
}
```
### 2. Write generic functions

Target: Write generic functions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```gleam
pub fn identity(value: a) -> a {
  value
}
```
### 3. Use type variables

Target: Use type variables. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```gleam
pub fn first(list: List(a)) -> Option(a) {
  case list {
    [x, ..] -> Some(x)
    [] -> None
  }
}
```
### 4. Build containers

Target: Build containers. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```gleam
pub type Result(a, e) {
  Ok(a)
  Error(e)
}
```

## Practice Questions

1. What is the key idea behind "Generics"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Generics with analogies and real-world examples"
1. "Show me common mistakes beginners make with Generics"
1. "Provide advanced patterns and performance considerations for Generics"

## Key Takeaways

- Master the core ideas of Generics through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
