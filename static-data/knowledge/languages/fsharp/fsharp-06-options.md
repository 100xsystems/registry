---
{
  "title": "Option and Result",
  "description": "Handle absence and errors safely.",
  "type": "lesson",
  "order": 6,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use Option type",
    "Pattern match options",
    "Use Result type",
    "Chain computations"
  ],
  "knowledge_refs": [
    "fsharp/fsharp-06-options"
  ],
  "prerequisites": [
    "FSharp-05: Strings"
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

# FSHARP-06-OPTIONS: Option and Result

## Introduction

Handle absence and errors safely. By the end of this lesson you will be able to: Use Option type; Pattern match options; Use Result type; Chain computations.

## Key Concepts

### 1. Use Option type

Target: Use Option type. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```fsharp
let parse (s: string) : int option =
    match System.Int32.TryParse s with
    | true, n -> Some n
    | false, _ -> None
```
### 2. Pattern match options

Target: Pattern match options. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```fsharp
let div a b =
    if b = 0 then None else Some (a / b)
```
### 3. Use Result type

Target: Use Result type. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```fsharp
type Result<'T, 'E> = Ok of 'T | Error of 'E
```
### 4. Chain computations

Target: Chain computations. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```fsharp
Option.map (fun n -> n * 2) (parse "42")
```

## Practice Questions

1. What is the key idea behind "Option and Result"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Option and Result with analogies and real-world examples"
1. "Show me common mistakes beginners make with Option and Result"
1. "Provide advanced patterns and performance considerations for Option and Result"

## Key Takeaways

- Master the core ideas of Option and Result through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
