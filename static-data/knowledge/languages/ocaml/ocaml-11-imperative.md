---
{
  "title": "Imperative Features",
  "description": "Refs, arrays, and mutable state.",
  "type": "lesson",
  "order": 11,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use ref cells",
    "Use arrays",
    "Understand aliasing",
    "Use while loops"
  ],
  "knowledge_refs": [
    "ocaml/ocaml-11-imperative"
  ],
  "prerequisites": [
    "Ocaml-10: Recursion and Tail Calls"
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

# OCAML-11-IMPERATIVE: Imperative Features

## Introduction

Refs, arrays, and mutable state. By the end of this lesson you will be able to: Use ref cells; Use arrays; Understand aliasing; Use while loops.

## Key Concepts

### 1. Use ref cells

Target: Use ref cells. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ocaml
let counter = ref 0
counter := !counter + 1
```
### 2. Use arrays

Target: Use arrays. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ocaml
let arr = [|1; 2; 3|]
arr.(0) <- 10
```
### 3. Understand aliasing

Target: Understand aliasing. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ocaml
let total = ref 0
let () =
  for i = 1 to 10 do
    total := !total + i
  done
```
### 4. Use while loops

Target: Use while loops. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ocaml
while !counter < 3 do incr counter done
```

## Practice Questions

1. What is the key idea behind "Imperative Features"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Imperative Features with analogies and real-world examples"
1. "Show me common mistakes beginners make with Imperative Features"
1. "Provide advanced patterns and performance considerations for Imperative Features"

## Key Takeaways

- Master the core ideas of Imperative Features through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
