---
{
  "title": "Variants",
  "description": "Sum types for data modeling.",
  "type": "lesson",
  "order": 8,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define variant types",
    "Carry data in variants",
    "Match variants",
    "Model states"
  ],
  "knowledge_refs": [
    "ocaml/ocaml-08-variants"
  ],
  "prerequisites": [
    "Ocaml-07: Records"
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

# OCAML-08-VARIANTS: Variants

## Introduction

Sum types for data modeling. By the end of this lesson you will be able to: Define variant types; Carry data in variants; Match variants; Model states.

## Key Concepts

### 1. Define variant types

Target: Define variant types. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ocaml
type color = Red | Green | Blue
```
### 2. Carry data in variants

Target: Carry data in variants. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ocaml
type shape =
  | Circle of float
  | Square of float

let area s =
  match s with
  | Circle r -> 3.14159 *. r *. r
  | Square side -> side *. side
```
### 3. Match variants

Target: Match variants. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ocaml
type state =
  | Loading
  | Loaded of string list
  | Failed of string
```
### 4. Model states

Target: Model states. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ocaml
let name c =
  match c with
  | Red -> "red" | Green -> "green" | Blue -> "blue"
```

## Practice Questions

1. What is the key idea behind "Variants"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Variants with analogies and real-world examples"
1. "Show me common mistakes beginners make with Variants"
1. "Provide advanced patterns and performance considerations for Variants"

## Key Takeaways

- Master the core ideas of Variants through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
