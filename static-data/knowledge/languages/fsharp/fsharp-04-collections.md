---
{
  "title": "Collections",
  "description": "Lists, arrays, and sequences.",
  "type": "lesson",
  "order": 4,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Create lists",
    "Map and filter",
    "Fold collections",
    "Use arrays and seq"
  ],
  "knowledge_refs": [
    "fsharp/fsharp-04-collections"
  ],
  "prerequisites": [
    "FSharp-03: Functions"
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

# FSHARP-04-COLLECTIONS: Collections

## Introduction

Lists, arrays, and sequences. By the end of this lesson you will be able to: Create lists; Map and filter; Fold collections; Use arrays and seq.

## Key Concepts

### 1. Create lists

Target: Create lists. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```fsharp
let nums = [1; 2; 3]
let doubled = List.map (fun n -> n * 2) nums
```
### 2. Map and filter

Target: Map and filter. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```fsharp
List.filter (fun n -> n > 2) [1; 2; 3; 4]
```
### 3. Fold collections

Target: Fold collections. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```fsharp
List.fold (+) 0 [1; 2; 3]
```
### 4. Use arrays and seq

Target: Use arrays and seq. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```fsharp
let arr = [|1; 2; 3|]
let s = seq { 1..10 }
```

## Practice Questions

1. What is the key idea behind "Collections"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Collections with analogies and real-world examples"
1. "Show me common mistakes beginners make with Collections"
1. "Provide advanced patterns and performance considerations for Collections"

## Key Takeaways

- Master the core ideas of Collections through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
