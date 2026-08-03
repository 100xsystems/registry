---
{
  "title": "Advanced Types",
  "description": "GADTs and polymorphic variants.",
  "type": "lesson",
  "order": 14,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use polymorphic variants",
    "Understand GADTs",
    "Write type-safe DSLs",
    "Use first-class modules"
  ],
  "knowledge_refs": [
    "ocaml/ocaml-14-gadt"
  ],
  "prerequisites": [
    "Ocaml-13: Functors"
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

# OCAML-14-GADT: Advanced Types

## Introduction

GADTs and polymorphic variants. By the end of this lesson you will be able to: Use polymorphic variants; Understand GADTs; Write type-safe DSLs; Use first-class modules.

## Key Concepts

### 1. Use polymorphic variants

Target: Use polymorphic variants. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ocaml
let f = function `Int n -> n | `Str s -> String.length s
```
### 2. Understand GADTs

Target: Understand GADTs. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ocaml
type _ expr =
  | Int : int -> int expr
  | Bool : bool -> bool expr
  | Add : int expr * int expr -> int expr
```
### 3. Write type-safe DSLs

Target: Write type-safe DSLs. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ocaml
let rec eval : type a. a expr -> a = function
  | Int n -> n
  | Bool b -> b
  | Add (x, y) -> eval x + eval y
```
### 4. Use first-class modules

Target: Use first-class modules. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ocaml
module type S = sig val x : int end
module M = struct let x = 42 end
let v = (module M : S)
```

## Practice Questions

1. What is the key idea behind "Advanced Types"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Advanced Types with analogies and real-world examples"
1. "Show me common mistakes beginners make with Advanced Types"
1. "Provide advanced patterns and performance considerations for Advanced Types"

## Key Takeaways

- Master the core ideas of Advanced Types through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
