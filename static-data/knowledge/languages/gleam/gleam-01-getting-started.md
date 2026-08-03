---
{
  "title": "Getting Started with Gleam",
  "description": "Install, project setup, hello world.",
  "type": "lesson",
  "order": 1,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Install Gleam",
    "Create a project",
    "Write hello world",
    "Run with gleam run"
  ],
  "knowledge_refs": [
    "gleam/gleam-01-getting-started"
  ],
  "prerequisites": [
    "None — this is the entry point"
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

# GLEAM-01-GETTING-STARTED: Getting Started with Gleam

## Introduction

Install, project setup, hello world. By the end of this lesson you will be able to: Install Gleam; Create a project; Write hello world; Run with gleam run.

## Key Concepts

### 1. Install Gleam

Target: Install Gleam. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```gleam
import gleam/io

pub fn main() {
  io.println("Hello, World!")
}
```
### 2. Create a project

Target: Create a project. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```gleam
gleam new hello
cd hello && gleam run
```
### 3. Write hello world

Target: Write hello world. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```gleam
import gleam/io

pub fn main() {
  io.println("Hello, " <> "Gleam!")
}
```
### 4. Run with gleam run

Target: Run with gleam run. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```gleam
import gleam/io

pub fn main() {
  let name = "Ada"
  io.println("Hello, " <> name)
}
```

## Practice Questions

1. What is the key idea behind "Getting Started with Gleam"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with Gleam with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with Gleam"
1. "Provide advanced patterns and performance considerations for Getting Started with Gleam"

## Key Takeaways

- Master the core ideas of Getting Started with Gleam through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
