---
{
  "title": "Functions",
  "description": "First-class functions and composition.",
  "type": "lesson",
  "order": 3,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Write functions",
    "Use pipe operator |>",
    "Compose with >>",
    "Use lambda expressions"
  ],
  "knowledge_refs": [
    "fsharp/fsharp-03-functions"
  ],
  "prerequisites": [
    "FSharp-02: Values and Types"
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

# FSHARP-03-FUNCTIONS: Functions

## Introduction

First-class functions and composition. By the end of this lesson you will be able to: Write functions; Use pipe operator |>; Compose with >>; Use lambda expressions.

## Key Concepts

### 1. Write functions

Target: Write functions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```fsharp
let double x = x * 2
let result = double 21
```
### 2. Use pipe operator |>

Target: Use pipe operator |>. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```fsharp
5 |> double |> string |> printfn "%s"
```
### 3. Compose with >>

Target: Compose with >>. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```fsharp
let addThenDouble = double << (fun x -> x + 1)
```
### 4. Use lambda expressions

Target: Use lambda expressions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```fsharp
let apply f x = f x
apply (fun n -> n + 1) 41
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
