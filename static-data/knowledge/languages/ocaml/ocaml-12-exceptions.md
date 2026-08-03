---
{
  "title": "Exceptions",
  "description": "Raise and handle errors.",
  "type": "lesson",
  "order": 12,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Raise exceptions",
    "Catch with try/with",
    "Define custom exceptions",
    "Clean up with finally"
  ],
  "knowledge_refs": [
    "ocaml/ocaml-12-exceptions"
  ],
  "prerequisites": [
    "Ocaml-11: Imperative Features"
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

# OCAML-12-EXCEPTIONS: Exceptions

## Introduction

Raise and handle errors. By the end of this lesson you will be able to: Raise exceptions; Catch with try/with; Define custom exceptions; Clean up with finally.

## Key Concepts

### 1. Raise exceptions

Target: Raise exceptions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ocaml
let () =
  try
    failwith "boom"
  with
  | Failure msg -> print_endline msg
```
### 2. Catch with try/with

Target: Catch with try/with. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ocaml
exception Empty_list
```
### 3. Define custom exceptions

Target: Define custom exceptions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ocaml
let safe_head = function
  | [] -> raise Empty_list
  | x :: _ -> x
```
### 4. Clean up with finally

Target: Clean up with finally. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ocaml
let read () =
  try
    Some (input_line stdin)
  with End_of_file -> None
```

## Practice Questions

1. What is the key idea behind "Exceptions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Exceptions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Exceptions"
1. "Provide advanced patterns and performance considerations for Exceptions"

## Key Takeaways

- Master the core ideas of Exceptions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
