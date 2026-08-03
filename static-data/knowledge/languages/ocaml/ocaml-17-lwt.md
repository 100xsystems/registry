---
{
  "title": "Concurrency with Lwt",
  "description": "Cooperative threads for IO.",
  "type": "lesson",
  "order": 17,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Create Lwt promises",
    "Bind with >>=",
    "Use Lwt_main.run",
    "Handle async errors"
  ],
  "knowledge_refs": [
    "ocaml/ocaml-17-lwt"
  ],
  "prerequisites": [
    "Ocaml-16: Objects and Classes"
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

# OCAML-17-LWT: Concurrency with Lwt

## Introduction

Cooperative threads for IO. By the end of this lesson you will be able to: Create Lwt promises; Bind with >>=; Use Lwt_main.run; Handle async errors.

## Key Concepts

### 1. Create Lwt promises

Target: Create Lwt promises. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ocaml
let () =
  Lwt_main.run (Lwt_io.printl "hello")
```
### 2. Bind with >>=

Target: Bind with >>=. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ocaml
let () =
  Lwt_main.run (Lwt.return 42 >>= fun n -> Lwt_io.printlf "%d" n)
```
### 3. Use Lwt_main.run

Target: Use Lwt_main.run. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ocaml
let fetch url =
  Cohttp_lwt_unix.Client.get (Uri.of_string url)
```
### 4. Handle async errors

Target: Handle async errors. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ocaml
let both = Lwt.both p1 p2
```

## Practice Questions

1. What is the key idea behind "Concurrency with Lwt"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Concurrency with Lwt with analogies and real-world examples"
1. "Show me common mistakes beginners make with Concurrency with Lwt"
1. "Provide advanced patterns and performance considerations for Concurrency with Lwt"

## Key Takeaways

- Master the core ideas of Concurrency with Lwt through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
