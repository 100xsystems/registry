---
{
  "title": "Option Types",
  "description": "Handle missing values.",
  "type": "lesson",
  "order": 7,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use Option type",
    "Pattern match Some/None",
    "Use option.unwrap",
    "Chain options"
  ],
  "knowledge_refs": [
    "gleam/gleam-07-option"
  ],
  "prerequisites": [
    "Gleam-06: Result and Error Handling"
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

# GLEAM-07-OPTION: Option Types

## Introduction

Handle missing values. By the end of this lesson you will be able to: Use Option type; Pattern match Some/None; Use option.unwrap; Chain options.

## Key Concepts

### 1. Use Option type

Target: Use Option type. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```gleam
import gleam/option

pub fn find(list: List(Int), target: Int) -> Option(Int) {
  case list {
    [] -> None
    [x, ..rest] -> case x == target {
      True -> Some(x)
      False -> find(rest, target)
    }
  }
}
```
### 2. Pattern match Some/None

Target: Pattern match Some/None. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```gleam
case find([1, 2, 3], 2) {
  Some(v) -> io.debug(v)
  None -> io.println("not found")
}
```
### 3. Use option.unwrap

Target: Use option.unwrap. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```gleam
import gleam/option

let value = option.unwrap(find([1], 1), 0)
```
### 4. Chain options

Target: Chain options. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```gleam
option.map(Some(4), fn(n) { n * 2 })
```

## Practice Questions

1. What is the key idea behind "Option Types"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Option Types with analogies and real-world examples"
1. "Show me common mistakes beginners make with Option Types"
1. "Provide advanced patterns and performance considerations for Option Types"

## Key Takeaways

- Master the core ideas of Option Types through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
