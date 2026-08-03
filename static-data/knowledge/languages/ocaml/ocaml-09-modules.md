---
{
  "title": "Modules and Signatures",
  "description": "Encapsulate code with modules.",
  "type": "lesson",
  "order": 9,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create modules",
    "Define signatures",
    "Hide implementations",
    "Use module functors"
  ],
  "knowledge_refs": [
    "ocaml/ocaml-09-modules"
  ],
  "prerequisites": [
    "Ocaml-08: Variants"
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

# OCAML-09-MODULES: Modules and Signatures

## Introduction

Encapsulate code with modules. By the end of this lesson you will be able to: Create modules; Define signatures; Hide implementations; Use module functors.

## Key Concepts

### 1. Create modules

Target: Create modules. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ocaml
module Math = struct
  let square x = x * x
end

let () = print_int (Math.square 5)
```
### 2. Define signatures

Target: Define signatures. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ocaml
module type COUNTER = sig
  val inc : unit -> unit
  val get : unit -> int
end
```
### 3. Hide implementations

Target: Hide implementations. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ocaml
module Counter : COUNTER = struct
  let count = ref 0
  let inc () = incr count
  let get () = !count
end
```
### 4. Use module functors

Target: Use module functors. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ocaml
module StringMap = Map.Make(String)
```

## Practice Questions

1. What is the key idea behind "Modules and Signatures"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Modules and Signatures with analogies and real-world examples"
1. "Show me common mistakes beginners make with Modules and Signatures"
1. "Provide advanced patterns and performance considerations for Modules and Signatures"

## Key Takeaways

- Master the core ideas of Modules and Signatures through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
