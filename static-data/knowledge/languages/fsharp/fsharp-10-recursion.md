---
{
  "title": "Recursion",
  "description": "Recursive functions and tail calls.",
  "type": "lesson",
  "order": 10,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write recursive functions",
    "Use tail recursion",
    "Understand accumulator pattern",
    "Use List recursion"
  ],
  "knowledge_refs": [
    "fsharp/fsharp-10-recursion"
  ],
  "prerequisites": [
    "FSharp-09: Pattern Matching"
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

# FSHARP-10-RECURSION: Recursion

## Introduction

Recursive functions and tail calls. By the end of this lesson you will be able to: Write recursive functions; Use tail recursion; Understand accumulator pattern; Use List recursion.

## Key Concepts

### 1. Write recursive functions

Target: Write recursive functions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```fsharp
let rec fact n =
    if n <= 1 then 1 else n * fact (n - 1)
```
### 2. Use tail recursion

Target: Use tail recursion. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```fsharp
let rec sumList lst =
    match lst with
    | [] -> 0
    | x :: rest -> x + sumList rest
```
### 3. Understand accumulator pattern

Target: Understand accumulator pattern. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```fsharp
let rec loop acc n =
    if n <= 0 then acc else loop (acc + n) (n - 1)
```
### 4. Use List recursion

Target: Use List recursion. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```fsharp
let rec map f lst =
    match lst with
    | [] -> []
    | x :: rest -> f x :: map f rest
```

## Practice Questions

1. What is the key idea behind "Recursion"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Recursion with analogies and real-world examples"
1. "Show me common mistakes beginners make with Recursion"
1. "Provide advanced patterns and performance considerations for Recursion"

## Key Takeaways

- Master the core ideas of Recursion through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
