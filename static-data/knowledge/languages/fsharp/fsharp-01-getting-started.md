---
{
  "title": "Getting Started with F#",
  "description": "Dotnet SDK, hello world, and F# Interactive.",
  "type": "lesson",
  "order": 1,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Install the .NET SDK",
    "Create an F# project",
    "Run F# Interactive",
    "Write hello world"
  ],
  "knowledge_refs": [
    "fsharp/fsharp-01-getting-started"
  ],
  "prerequisites": [
    "None — this is the entry point"
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

# FSHARP-01-GETTING-STARTED: Getting Started with F#

## Introduction

Dotnet SDK, hello world, and F# Interactive. By the end of this lesson you will be able to: Install the .NET SDK; Create an F# project; Run F# Interactive; Write hello world.

## Key Concepts

### 1. Install the .NET SDK

Target: Install the .NET SDK. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```fsharp
printfn "Hello, World!"
```
### 2. Create an F# project

Target: Create an F# project. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```fsharp
dotnet new console -lang F# -o hello
cd hello && dotnet run
```
### 3. Run F# Interactive

Target: Run F# Interactive. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```fsharp
printfn "Hello, %s!" "Ada"
```
### 4. Write hello world

Target: Write hello world. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```fsharp
let square x = x * x
printfn "%d" (square 21)
```

## Practice Questions

1. What is the key idea behind "Getting Started with F#"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with F# with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with F#"
1. "Provide advanced patterns and performance considerations for Getting Started with F#"

## Key Takeaways

- Master the core ideas of Getting Started with F# through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
