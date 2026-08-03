---
{
  "title": "Async and Parallel",
  "description": "Asynchronous programming.",
  "type": "lesson",
  "order": 14,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Create async workflows",
    "Run in parallel",
    "Use Async.Parallel",
    "Cancel operations"
  ],
  "knowledge_refs": [
    "fsharp/fsharp-14-async"
  ],
  "prerequisites": [
    "FSharp-13: Computation Expressions"
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

# FSHARP-14-ASYNC: Async and Parallel

## Introduction

Asynchronous programming. By the end of this lesson you will be able to: Create async workflows; Run in parallel; Use Async.Parallel; Cancel operations.

## Key Concepts

### 1. Create async workflows

Target: Create async workflows. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```fsharp
let slow () = async { return 42 }
let result = slow () |> Async.RunSynchronously
```
### 2. Run in parallel

Target: Run in parallel. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```fsharp
let tasks = [1..10] |> List.map (fun i -> async { return i * i })
let all = tasks |> Async.Parallel |> Async.RunSynchronously
```
### 3. Use Async.Parallel

Target: Use Async.Parallel. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```fsharp
async {
    do! Async.Sleep 100
    return "done"
} |> Async.RunSynchronously
```
### 4. Cancel operations

Target: Cancel operations. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```fsharp
Async.StartAsTask (async { return 1 })
```

## Practice Questions

1. What is the key idea behind "Async and Parallel"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Async and Parallel with analogies and real-world examples"
1. "Show me common mistakes beginners make with Async and Parallel"
1. "Provide advanced patterns and performance considerations for Async and Parallel"

## Key Takeaways

- Master the core ideas of Async and Parallel through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
