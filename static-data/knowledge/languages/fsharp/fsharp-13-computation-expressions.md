---
{
  "title": "Computation Expressions",
  "description": "Workflows like option and async.",
  "type": "lesson",
  "order": 13,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use option workflows",
    "Use async workflows",
    "Write let! and return",
    "Build custom expressions"
  ],
  "knowledge_refs": [
    "fsharp/fsharp-13-computation-expressions"
  ],
  "prerequisites": [
    "FSharp-12: Classes and OOP"
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

# FSHARP-13-COMPUTATION-EXPRESSIONS: Computation Expressions

## Introduction

Workflows like option and async. By the end of this lesson you will be able to: Use option workflows; Use async workflows; Write let! and return; Build custom expressions.

## Key Concepts

### 1. Use option workflows

Target: Use option workflows. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```fsharp
let tryDiv a b =
    option {
        if b = 0 then return! None
        else return a / b
    }
```
### 2. Use async workflows

Target: Use async workflows. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```fsharp
let fetch url =
    async {
        let! html = System.Net.Http.HttpClient().GetStringAsync(url) |> Async.AwaitTask
        return html.Length
    }
```
### 3. Write let! and return

Target: Write let! and return. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```fsharp
let compute =
    async {
        let! a = task1
        let! b = task2
        return a + b
    }
```
### 4. Build custom expressions

Target: Build custom expressions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```fsharp
let result = option { let! x = parse "42"; return x * 2 }
```

## Practice Questions

1. What is the key idea behind "Computation Expressions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Computation Expressions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Computation Expressions"
1. "Provide advanced patterns and performance considerations for Computation Expressions"

## Key Takeaways

- Master the core ideas of Computation Expressions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
