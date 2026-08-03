---
{
  "title": "Recursion and Tail Calls",
  "description": "Recursive definitions.",
  "type": "lesson",
  "order": 10,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write recursive functions",
    "Ensure tail recursion",
    "Use accumulator patterns",
    "Define recursive types"
  ],
  "knowledge_refs": [
    "ocaml/ocaml-10-recursion"
  ],
  "prerequisites": [
    "Ocaml-09: Modules and Signatures"
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

# OCAML-10-RECURSION: Recursion and Tail Calls

## Introduction

Recursive definitions. By the end of this lesson you will be able to: Write recursive functions; Ensure tail recursion; Use accumulator patterns; Define recursive types.

## Key Concepts

### 1. Write recursive functions

Target: Write recursive functions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ocaml
let rec fact n =
  if n <= 1 then 1 else n * fact (n - 1)
```
### 2. Ensure tail recursion

Target: Ensure tail recursion. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ocaml
let rec loop acc n =
  if n <= 0 then acc else loop (acc + n) (n - 1)
```
### 3. Use accumulator patterns

Target: Use accumulator patterns. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ocaml
type intlist = Nil | Cons of int * intlist
```
### 4. Define recursive types

Target: Define recursive types. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ocaml
let rec map f = function
  | [] -> []
  | x :: rest -> f x :: map f rest
```

## Practice Questions

1. What is the key idea behind "Recursion and Tail Calls"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Recursion and Tail Calls with analogies and real-world examples"
1. "Show me common mistakes beginners make with Recursion and Tail Calls"
1. "Provide advanced patterns and performance considerations for Recursion and Tail Calls"

## Key Takeaways

- Master the core ideas of Recursion and Tail Calls through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
