---
{
  "title": "Lists",
  "description": "Immutable lists and List functions.",
  "type": "lesson",
  "order": 5,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Build lists",
    "Use list.append",
    "Map and filter",
    "Fold lists"
  ],
  "knowledge_refs": [
    "gleam/gleam-05-lists"
  ],
  "prerequisites": [
    "Gleam-04: Functions"
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

# GLEAM-05-LISTS: Lists

## Introduction

Immutable lists and List functions. By the end of this lesson you will be able to: Build lists; Use list.append; Map and filter; Fold lists.

## Key Concepts

### 1. Build lists

Target: Build lists. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```gleam
import gleam/list

pub fn main() {
  let nums = [1, 2, 3]
  io.debug(nums)
}
```
### 2. Use list.append

Target: Use list.append. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```gleam
import gleam/list

let doubled = list.map([1, 2, 3], fn(n) { n * 2 })
```
### 3. Map and filter

Target: Map and filter. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```gleam
let evens = list.filter([1, 2, 3, 4], fn(n) { n % 2 == 0 })
```
### 4. Fold lists

Target: Fold lists. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```gleam
let sum = list.fold([1, 2, 3], 0, fn(acc, n) { acc + n })
```

## Practice Questions

1. What is the key idea behind "Lists"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Lists with analogies and real-world examples"
1. "Show me common mistakes beginners make with Lists"
1. "Provide advanced patterns and performance considerations for Lists"

## Key Takeaways

- Master the core ideas of Lists through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
