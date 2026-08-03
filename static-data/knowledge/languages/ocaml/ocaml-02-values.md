---
{
  "title": "Values and Types",
  "description": "let bindings and basic types.",
  "type": "lesson",
  "order": 2,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Bind values with let",
    "Use int, float, and string",
    "Use bool and char",
    "Understand type inference"
  ],
  "knowledge_refs": [
    "ocaml/ocaml-02-values"
  ],
  "prerequisites": [
    "Ocaml-01: Getting Started with OCaml"
  ],
  "references": [
    {
      "title": "OCaml Manual",
      "url": "https://ocaml.org/manual/",
      "description": "Official language manual"
    },
    {
      "title": "OCaml Tutorials",
      "url": "https://ocaml.org/docs",
      "description": "Official documentation"
    },
    {
      "title": "Real World OCaml",
      "url": "https://dev.realworldocaml.org/",
      "description": "Comprehensive book"
    }
  ]
}
---

# OCAML-02-VALUES: Values and Types

## Introduction

let bindings and basic types. By the end of this lesson you will be able to: Bind values with let; Use int, float, and string; Use bool and char; Understand type inference.

## Key Concepts

### 1. Bind values with let

Target: Bind values with let. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ocaml
let name = "Ada"
let age = 36
```
### 2. Use int, float, and string

Target: Use int, float, and string. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ocaml
let pi = 3.14159
let active = true
```
### 3. Use bool and char

Target: Use bool and char. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ocaml
let add a b = a + b
```
### 4. Understand type inference

Target: Understand type inference. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ocaml
let greet name = "Hello, " ^ name ^ "!"
```

## Practice Questions

1. What is the key idea behind "Values and Types"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Values and Types with analogies and real-world examples"
1. "Show me common mistakes beginners make with Values and Types"
1. "Provide advanced patterns and performance considerations for Values and Types"

## Key Takeaways

- Master the core ideas of Values and Types through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
