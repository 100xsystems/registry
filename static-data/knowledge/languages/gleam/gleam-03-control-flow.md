---
{
  "title": "Control Flow",
  "description": "case expressions and pattern matching.",
  "type": "lesson",
  "order": 3,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use case expressions",
    "Pattern match values",
    "Use guards",
    "Handle multiple patterns"
  ],
  "knowledge_refs": [
    "gleam/gleam-03-control-flow"
  ],
  "prerequisites": [
    "Gleam-02: Values and Types"
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

# GLEAM-03-CONTROL-FLOW: Control Flow

## Introduction

case expressions and pattern matching. By the end of this lesson you will be able to: Use case expressions; Pattern match values; Use guards; Handle multiple patterns.

## Key Concepts

### 1. Use case expressions

Target: Use case expressions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```gleam
import gleam/io

pub fn describe(n: Int) -> String {
  case n {
    0 -> "zero"
    1 -> "one"
    _ -> "many"
  }
}

pub fn main() {
  io.println(describe(2))
}
```
### 2. Pattern match values

Target: Pattern match values. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```gleam
pub fn grade(score: Int) -> String {
  case score {
    s if s >= 90 -> "A"
    s if s >= 80 -> "B"
    _ -> "C"
  }
}
```
### 3. Use guards

Target: Use guards. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```gleam
case pair {
  (0, 0) -> "origin"
  _ -> "elsewhere"
}
```
### 4. Handle multiple patterns

Target: Handle multiple patterns. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```gleam
case list {
  [] -> "empty"
  [first, ..rest] -> "has items"
}
```

## Practice Questions

1. What is the key idea behind "Control Flow"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Control Flow with analogies and real-world examples"
1. "Show me common mistakes beginners make with Control Flow"
1. "Provide advanced patterns and performance considerations for Control Flow"

## Key Takeaways

- Master the core ideas of Control Flow through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
