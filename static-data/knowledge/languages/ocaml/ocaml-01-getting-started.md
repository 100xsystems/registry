---
{
  "title": "Getting Started with OCaml",
  "description": "OPAM, utop, and hello world.",
  "type": "lesson",
  "order": 1,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Install OCaml with OPAM",
    "Use utop REPL",
    "Compile with ocamlopt",
    "Write hello world"
  ],
  "knowledge_refs": [
    "ocaml/ocaml-01-getting-started"
  ],
  "prerequisites": [
    "None — this is the entry point"
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

# OCAML-01-GETTING-STARTED: Getting Started with OCaml

## Introduction

OPAM, utop, and hello world. By the end of this lesson you will be able to: Install OCaml with OPAM; Use utop REPL; Compile with ocamlopt; Write hello world.

## Key Concepts

### 1. Install OCaml with OPAM

Target: Install OCaml with OPAM. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ocaml
print_endline "Hello, World!"
```
### 2. Use utop REPL

Target: Use utop REPL. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ocaml
ocaml
# print_endline "hello";;
```
### 3. Compile with ocamlopt

Target: Compile with ocamlopt. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ocaml
ocamlopt -o hello hello.ml
./hello
```
### 4. Write hello world

Target: Write hello world. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ocaml
let () = print_endline "Hello, " ^ "OCaml!"
```

## Practice Questions

1. What is the key idea behind "Getting Started with OCaml"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with OCaml with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with OCaml"
1. "Provide advanced patterns and performance considerations for Getting Started with OCaml"

## Key Takeaways

- Master the core ideas of Getting Started with OCaml through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
