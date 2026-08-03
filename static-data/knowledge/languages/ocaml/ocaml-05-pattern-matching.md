---
{
  "title": "Pattern Matching",
  "description": "Destructure data safely.",
  "type": "lesson",
  "order": 5,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Match on values",
    "Match lists",
    "Use wildcards",
    "Match tuples"
  ],
  "knowledge_refs": [
    "ocaml/ocaml-05-pattern-matching"
  ],
  "prerequisites": [
    "Ocaml-04: Lists"
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

# OCAML-05-PATTERN-MATCHING: Pattern Matching

## Introduction

Destructure data safely. By the end of this lesson you will be able to: Match on values; Match lists; Use wildcards; Match tuples.

## Key Concepts

### 1. Match on values

Target: Match on values. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ocaml
let describe n =
  match n with
  | 0 -> "zero"
  | 1 -> "one"
  | _ -> "many"
```
### 2. Match lists

Target: Match lists. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ocaml
let rec length lst =
  match lst with
  | [] -> 0
  | _ :: rest -> 1 + length rest
```
### 3. Use wildcards

Target: Use wildcards. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ocaml
let classify n =
  match n with
  | n when n < 0 -> "neg"
  | 0 -> "zero"
  | _ -> "pos"
```
### 4. Match tuples

Target: Match tuples. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ocaml
let sum (a, b) = a + b
```

## Practice Questions

1. What is the key idea behind "Pattern Matching"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Pattern Matching with analogies and real-world examples"
1. "Show me common mistakes beginners make with Pattern Matching"
1. "Provide advanced patterns and performance considerations for Pattern Matching"

## Key Takeaways

- Master the core ideas of Pattern Matching through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
