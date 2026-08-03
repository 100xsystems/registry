---
{
  "title": "Discriminated Unions",
  "description": "Model complex states with types.",
  "type": "lesson",
  "order": 8,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define DUs",
    "Pattern match variants",
    "Carry data in cases",
    "Model states safely"
  ],
  "knowledge_refs": [
    "fsharp/fsharp-08-discriminated-unions"
  ],
  "prerequisites": [
    "FSharp-07: Records and Tuples"
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

# FSHARP-08-DISCRIMINATED-UNIONS: Discriminated Unions

## Introduction

Model complex states with types. By the end of this lesson you will be able to: Define DUs; Pattern match variants; Carry data in cases; Model states safely.

## Key Concepts

### 1. Define DUs

Target: Define DUs. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```fsharp
type Shape =
    | Circle of float
    | Square of float

let area s =
    match s with
    | Circle r -> 3.14159 * r * r
    | Square side -> side * side
```
### 2. Pattern match variants

Target: Pattern match variants. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```fsharp
type Option<'T> = Some of 'T | None
```
### 3. Carry data in cases

Target: Carry data in cases. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```fsharp
type Color = Red | Green | Blue

let name c =
    match c with
    | Red -> "red"
    | Green -> "green"
    | Blue -> "blue"
```
### 4. Model states safely

Target: Model states safely. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```fsharp
type State =
    | Loading
    | Loaded of string list
    | Failed of string
```

## Practice Questions

1. What is the key idea behind "Discriminated Unions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Discriminated Unions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Discriminated Unions"
1. "Provide advanced patterns and performance considerations for Discriminated Unions"

## Key Takeaways

- Master the core ideas of Discriminated Unions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
