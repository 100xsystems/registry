---
{
  "title": "Performance",
  "description": "Structs, arrays, and optimization.",
  "type": "lesson",
  "order": 20,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use struct records",
    "Avoid allocations",
    "Use arrays for hot paths",
    "Profile with dotnet"
  ],
  "knowledge_refs": [
    "fsharp/fsharp-20-performance"
  ],
  "prerequisites": [
    "FSharp-19: DSLs and Type Providers"
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

# FSHARP-20-PERFORMANCE: Performance

## Introduction

Structs, arrays, and optimization. By the end of this lesson you will be able to: Use struct records; Avoid allocations; Use arrays for hot paths; Profile with dotnet.

## Key Concepts

### 1. Use struct records

Target: Use struct records. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```fsharp
[<Struct>]
type Point = { X: float; Y: float }
```
### 2. Avoid allocations

Target: Avoid allocations. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```fsharp
let arr = Array.zeroCreate<int> 1000000
```
### 3. Use arrays for hot paths

Target: Use arrays for hot paths. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```fsharp
// use Arrays over Lists in hot loops
```
### 4. Profile with dotnet

Target: Profile with dotnet. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```fsharp
dotnet trace collect -- dotnet run
```

## Practice Questions

1. What is the key idea behind "Performance"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Performance with analogies and real-world examples"
1. "Show me common mistakes beginners make with Performance"
1. "Provide advanced patterns and performance considerations for Performance"

## Key Takeaways

- Master the core ideas of Performance through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
