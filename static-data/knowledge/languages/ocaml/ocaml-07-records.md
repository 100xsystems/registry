---
{
  "title": "Records",
  "description": "Named field structures.",
  "type": "lesson",
  "order": 7,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define record types",
    "Create and access records",
    "Copy records",
    "Use record patterns"
  ],
  "knowledge_refs": [
    "ocaml/ocaml-07-records"
  ],
  "prerequisites": [
    "Ocaml-06: Option Types"
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

# OCAML-07-RECORDS: Records

## Introduction

Named field structures. By the end of this lesson you will be able to: Define record types; Create and access records; Copy records; Use record patterns.

## Key Concepts

### 1. Define record types

Target: Define record types. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ocaml
type person = { name : string; age : int }

let ada = { name = "Ada"; age = 36 }
```
### 2. Create and access records

Target: Create and access records. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ocaml
let name = ada.name
```
### 3. Copy records

Target: Copy records. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ocaml
let older = { ada with age = 37 }
```
### 4. Use record patterns

Target: Use record patterns. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ocaml
let describe { name; age } = Printf.sprintf "%s %d" name age
```

## Practice Questions

1. What is the key idea behind "Records"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Records with analogies and real-world examples"
1. "Show me common mistakes beginners make with Records"
1. "Provide advanced patterns and performance considerations for Records"

## Key Takeaways

- Master the core ideas of Records through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
