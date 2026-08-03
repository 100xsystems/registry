---
{
  "title": "Project Structure",
  "description": "Organize a real project.",
  "type": "lesson",
  "order": 20,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Structure modules sensibly",
    "Manage dependencies",
    "Use gleam.toml",
    "Document code"
  ],
  "knowledge_refs": [
    "gleam/gleam-20-project-structure"
  ],
  "prerequisites": [
    "Gleam-19: Testing"
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

# GLEAM-20-PROJECT-STRUCTURE: Project Structure

## Introduction

Organize a real project. By the end of this lesson you will be able to: Structure modules sensibly; Manage dependencies; Use gleam.toml; Document code.

## Key Concepts

### 1. Structure modules sensibly

Target: Structure modules sensibly. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```gleam
name = "hello"
version = "1.0.0"

[dependencies]
gleam_stdlib = "~> 0.34"

```
### 2. Manage dependencies

Target: Manage dependencies. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```gleam
gleam add mist
# or: gleam add gleam/http
```
### 3. Use gleam.toml

Target: Use gleam.toml. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```gleam
gleam run
# dev workflow
```
### 4. Document code

Target: Document code. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```gleam
pub fn documented_fn() { /* doc comments above */ }
```

## Practice Questions

1. What is the key idea behind "Project Structure"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Project Structure with analogies and real-world examples"
1. "Show me common mistakes beginners make with Project Structure"
1. "Provide advanced patterns and performance considerations for Project Structure"

## Key Takeaways

- Master the core ideas of Project Structure through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
