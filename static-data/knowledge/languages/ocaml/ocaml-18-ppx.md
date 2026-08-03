---
{
  "title": "PPX and Metaprogramming",
  "description": "Syntax extensions.",
  "type": "lesson",
  "order": 18,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Understand PPX",
    "Use ppx_deriving",
    "Write annotations",
    "Extend syntax"
  ],
  "knowledge_refs": [
    "ocaml/ocaml-18-ppx"
  ],
  "prerequisites": [
    "Ocaml-17: Concurrency with Lwt"
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

# OCAML-18-PPX: PPX and Metaprogramming

## Introduction

Syntax extensions. By the end of this lesson you will be able to: Understand PPX; Use ppx_deriving; Write annotations; Extend syntax.

## Key Concepts

### 1. Understand PPX

Target: Understand PPX. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ocaml
type point = { x : int; y : int } [@@deriving show]
```
### 2. Use ppx_deriving

Target: Use ppx_deriving. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ocaml
let () = print_endline (show_point { x = 1; y = 2 })
```
### 3. Write annotations

Target: Write annotations. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ocaml
type t = A | B [@@deriving sexp]
```
### 4. Extend syntax

Target: Extend syntax. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ocaml
[@@@warning "-27"]
```

## Practice Questions

1. What is the key idea behind "PPX and Metaprogramming"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain PPX and Metaprogramming with analogies and real-world examples"
1. "Show me common mistakes beginners make with PPX and Metaprogramming"
1. "Provide advanced patterns and performance considerations for PPX and Metaprogramming"

## Key Takeaways

- Master the core ideas of PPX and Metaprogramming through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
