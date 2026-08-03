---
{
  "title": "Pattern Matching",
  "description": "Powerful destructuring.",
  "type": "lesson",
  "order": 9,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Match constants",
    "Match with guards",
    "Destructure tuples and lists",
    "Use wildcards"
  ],
  "knowledge_refs": [
    "fsharp/fsharp-09-pattern-matching"
  ],
  "prerequisites": [
    "FSharp-08: Discriminated Unions"
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

# FSHARP-09-PATTERN-MATCHING: Pattern Matching

## Introduction

Powerful destructuring. By the end of this lesson you will be able to: Match constants; Match with guards; Destructure tuples and lists; Use wildcards.

## Key Concepts

### 1. Match constants

Target: Match constants. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```fsharp
let describe n =
    match n with
    | 0 -> "zero"
    | 1 -> "one"
    | _ -> "many"
```
### 2. Match with guards

Target: Match with guards. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```fsharp
let classify n =
    match n with
    | n when n < 0 -> "negative"
    | 0 -> "zero"
    | _ -> "positive"
```
### 3. Destructure tuples and lists

Target: Destructure tuples and lists. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```fsharp
let sum (a, b) = a + b
```
### 4. Use wildcards

Target: Use wildcards. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```fsharp
let rec length lst =
    match lst with
    | [] -> 0
    | _ :: rest -> 1 + length rest
```

## Practice Questions

1. What is the key idea behind "Pattern Matching"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Pattern Matching with analogies and real-world examples"
1. "Show me common mistakes beginners make with Pattern Matching"
1. "Provide advanced patterns and performance considerations for Pattern Matching"

## Key Takeaways

- Master the core ideas of Pattern Matching through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
