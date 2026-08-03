---
{
  "title": "Result and Error Handling",
  "description": "Typed errors with Result.",
  "type": "lesson",
  "order": 6,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use Result type",
    "Pattern match Ok/Error",
    "Use result.try",
    "Map results"
  ],
  "knowledge_refs": [
    "gleam/gleam-06-result"
  ],
  "prerequisites": [
    "Gleam-05: Lists"
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

# GLEAM-06-RESULT: Result and Error Handling

## Introduction

Typed errors with Result. By the end of this lesson you will be able to: Use Result type; Pattern match Ok/Error; Use result.try; Map results.

## Key Concepts

### 1. Use Result type

Target: Use Result type. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```gleam
import gleam/result

pub fn divide(a: Int, b: Int) -> Result(Int, String) {
  case b {
    0 -> Error("division by zero")
    _ -> Ok(a / b)
  }
}
```
### 2. Pattern match Ok/Error

Target: Pattern match Ok/Error. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```gleam
case divide(10, 2) {
  Ok(n) -> io.debug(n)
  Error(e) -> io.println(e)
}
```
### 3. Use result.try

Target: Use result.try. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```gleam
import gleam/result

pub fn compute() -> Result(Int, String) {
  use a <- result.try(divide(10, 2))
  use b <- result.try(divide(a, 2))
  Ok(b)
}
```
### 4. Map results

Target: Map results. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```gleam
result.map(Ok(4), fn(n) { n * 2 })
```

## Practice Questions

1. What is the key idea behind "Result and Error Handling"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Result and Error Handling with analogies and real-world examples"
1. "Show me common mistakes beginners make with Result and Error Handling"
1. "Provide advanced patterns and performance considerations for Result and Error Handling"

## Key Takeaways

- Master the core ideas of Result and Error Handling through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
