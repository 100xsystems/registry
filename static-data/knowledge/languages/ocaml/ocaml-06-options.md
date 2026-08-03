---
{
  "title": "Option Types",
  "description": "Represent optional values.",
  "type": "lesson",
  "order": 6,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use option type",
    "Pattern match Some/None",
    "Use Option module",
    "Avoid null patterns"
  ],
  "knowledge_refs": [
    "ocaml/ocaml-06-options"
  ],
  "prerequisites": [
    "Ocaml-05: Pattern Matching"
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

# OCAML-06-OPTIONS: Option Types

## Introduction

Represent optional values. By the end of this lesson you will be able to: Use option type; Pattern match Some/None; Use Option module; Avoid null patterns.

## Key Concepts

### 1. Use option type

Target: Use option type. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ocaml
let safe_div a b =
  if b = 0 then None else Some (a / b)
```
### 2. Pattern match Some/None

Target: Pattern match Some/None. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ocaml
match safe_div 10 2 with
| Some n -> Printf.printf "%d
" n
| None -> print_endline "div by zero"
```
### 3. Use Option module

Target: Use Option module. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ocaml
Option.map (fun n -> n * 2) (Some 21)
```
### 4. Avoid null patterns

Target: Avoid null patterns. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ocaml
let lookup key tbl = Hashtbl.find_opt tbl key
```

## Practice Questions

1. What is the key idea behind "Option Types"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Option Types with analogies and real-world examples"
1. "Show me common mistakes beginners make with Option Types"
1. "Provide advanced patterns and performance considerations for Option Types"

## Key Takeaways

- Master the core ideas of Option Types through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
