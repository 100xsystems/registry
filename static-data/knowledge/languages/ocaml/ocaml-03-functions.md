---
{
  "title": "Functions",
  "description": "Higher-order functions and currying.",
  "type": "lesson",
  "order": 3,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Write functions",
    "Understand currying",
    "Use lambda functions",
    "Compose functions"
  ],
  "knowledge_refs": [
    "ocaml/ocaml-03-functions"
  ],
  "prerequisites": [
    "Ocaml-02: Values and Types"
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

# OCAML-03-FUNCTIONS: Functions

## Introduction

Higher-order functions and currying. By the end of this lesson you will be able to: Write functions; Understand currying; Use lambda functions; Compose functions.

## Key Concepts

### 1. Write functions

Target: Write functions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ocaml
let square x = x * x
```
### 2. Understand currying

Target: Understand currying. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ocaml
let add a b = a + b
let addFive = add 5
```
### 3. Use lambda functions

Target: Use lambda functions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ocaml
let doubled = List.map (fun x -> x * 2) [1; 2; 3]
```
### 4. Compose functions

Target: Compose functions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ocaml
let compose f g x = f (g x)
```

## Practice Questions

1. What is the key idea behind "Functions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Functions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Functions"
1. "Provide advanced patterns and performance considerations for Functions"

## Key Takeaways

- Master the core ideas of Functions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
