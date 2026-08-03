---
{
  "title": "Values and Types",
  "description": "let bindings, immutability, and types.",
  "type": "lesson",
  "order": 2,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Bind values with let",
    "Use built-in types",
    "Understand immutability",
    "Use type inference"
  ],
  "knowledge_refs": [
    "fsharp/fsharp-02-values"
  ],
  "prerequisites": [
    "FSharp-01: Getting Started with F#"
  ],
  "references": [
    {
      "title": "F# Documentation",
      "url": "https://learn.microsoft.com/en-us/dotnet/fsharp/",
      "description": "Official Microsoft docs"
    },
    {
      "title": "F# for Fun and Profit",
      "url": "https://fsharpforfunandprofit.com/",
      "description": "Excellent learning resource"
    },
    {
      "title": "FSharp.org",
      "url": "https://fsharp.org/",
      "description": "Community portal"
    }
  ]
}
---

# FSHARP-02-VALUES: Values and Types

## Introduction

let bindings, immutability, and types. By the end of this lesson you will be able to: Bind values with let; Use built-in types; Understand immutability; Use type inference.

## Key Concepts

### 1. Bind values with let

Target: Bind values with let. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```fsharp
let name = "Ada"
let age = 36
printfn "%s %d" name age
```
### 2. Use built-in types

Target: Use built-in types. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```fsharp
let pi = 3.14159
let active = true
```
### 3. Understand immutability

Target: Understand immutability. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```fsharp
let add a b = a + b   // inferred int -> int -> int
```
### 4. Use type inference

Target: Use type inference. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```fsharp
let mutable counter = 0
counter <- counter + 1
```

## Practice Questions

1. What is the key idea behind "Values and Types"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Values and Types with analogies and real-world examples"
1. "Show me common mistakes beginners make with Values and Types"
1. "Provide advanced patterns and performance considerations for Values and Types"

## Key Takeaways

- Master the core ideas of Values and Types through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
