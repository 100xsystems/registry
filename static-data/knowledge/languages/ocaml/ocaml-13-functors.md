---
{
  "title": "Functors",
  "description": "Modules parameterized by modules.",
  "type": "lesson",
  "order": 13,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Define functors",
    "Apply functors",
    "Use Set.Make",
    "Use Map.Make"
  ],
  "knowledge_refs": [
    "ocaml/ocaml-13-functors"
  ],
  "prerequisites": [
    "Ocaml-12: Exceptions"
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

# OCAML-13-FUNCTORS: Functors

## Introduction

Modules parameterized by modules. By the end of this lesson you will be able to: Define functors; Apply functors; Use Set.Make; Use Map.Make.

## Key Concepts

### 1. Define functors

Target: Define functors. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ocaml
module type ORDERED = sig
  type t
  val compare : t -> t -> int
end
```
### 2. Apply functors

Target: Apply functors. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ocaml
module MakeSet (X : ORDERED) = struct
  type t = X.t list
  let empty = []
  let mem x s = List.exists (fun y -> X.compare x y = 0) s
end
```
### 3. Use Set.Make

Target: Use Set.Make. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ocaml
module IntSet = MakeSet(struct type t = int let compare = compare end)
```
### 4. Use Map.Make

Target: Use Map.Make. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ocaml
module S = Set.Make(Int)
```

## Practice Questions

1. What is the key idea behind "Functors"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Functors with analogies and real-world examples"
1. "Show me common mistakes beginners make with Functors"
1. "Provide advanced patterns and performance considerations for Functors"

## Key Takeaways

- Master the core ideas of Functors through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
