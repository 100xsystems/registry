---
{
  "title": "Property Testing with FsCheck",
  "description": "Automated property-based testing.",
  "type": "lesson",
  "order": 17,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Define properties",
    "Run FsCheck",
    "Use generators",
    "Test with FsCheck.Xunit"
  ],
  "knowledge_refs": [
    "fsharp/fsharp-17-fscheck"
  ],
  "prerequisites": [
    "FSharp-16: Testing with xUnit"
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

# FSHARP-17-FSCHECK: Property Testing with FsCheck

## Introduction

Automated property-based testing. By the end of this lesson you will be able to: Define properties; Run FsCheck; Use generators; Test with FsCheck.Xunit.

## Key Concepts

### 1. Define properties

Target: Define properties. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```fsharp
open FsCheck
open FsCheck.Xunit

[<Property>]
let ``double is even`` (n: int) =
    (n * 2) % 2 = 0
```
### 2. Run FsCheck

Target: Run FsCheck. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```fsharp
Check.Quick (fun n -> n + 0 = n)
```
### 3. Use generators

Target: Use generators. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```fsharp
Gen.choose (0, 100)
|> Gen.sample 0 5
|> printfn "%A"
```
### 4. Test with FsCheck.Xunit

Target: Test with FsCheck.Xunit. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```fsharp
[<Property>]
let ``reverse reverse`` (s: string) =
    s |> Seq.rev |> Seq.rev |> Seq.toArray |> System.String = s
```

## Practice Questions

1. What is the key idea behind "Property Testing with FsCheck"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Property Testing with FsCheck with analogies and real-world examples"
1. "Show me common mistakes beginners make with Property Testing with FsCheck"
1. "Provide advanced patterns and performance considerations for Property Testing with FsCheck"

## Key Takeaways

- Master the core ideas of Property Testing with FsCheck through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
