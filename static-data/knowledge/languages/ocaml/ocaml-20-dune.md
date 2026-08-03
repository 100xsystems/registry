---
{
  "title": "Dune Build System",
  "description": "Build and manage OCaml projects.",
  "type": "lesson",
  "order": 20,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Create a dune project",
    "Define libraries",
    "Run executables",
    "Use dune test"
  ],
  "knowledge_refs": [
    "ocaml/ocaml-20-dune"
  ],
  "prerequisites": [
    "Ocaml-19: Testing with Alcotest"
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

# OCAML-20-DUNE: Dune Build System

## Introduction

Build and manage OCaml projects. By the end of this lesson you will be able to: Create a dune project; Define libraries; Run executables; Use dune test.

## Key Concepts

### 1. Create a dune project

Target: Create a dune project. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ocaml
dune init project hello
cd hello && dune build
```
### 2. Define libraries

Target: Define libraries. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ocaml
(executable
 (name main)
 (libraries unix))
```
### 3. Run executables

Target: Run executables. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ocaml
(library
 (name mylib)
 (modules mylib))
```
### 4. Use dune test

Target: Use dune test. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ocaml
dune test
 dune utop src
```

## Practice Questions

1. What is the key idea behind "Dune Build System"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Dune Build System with analogies and real-world examples"
1. "Show me common mistakes beginners make with Dune Build System"
1. "Provide advanced patterns and performance considerations for Dune Build System"

## Key Takeaways

- Master the core ideas of Dune Build System through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
