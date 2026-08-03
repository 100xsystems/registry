---
{
  "title": "Strings",
  "description": "String operations and interpolation.",
  "type": "lesson",
  "order": 5,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Interpolate strings",
    "Split and join",
    "Use StringBuilder",
    "Work with characters"
  ],
  "knowledge_refs": [
    "fsharp/fsharp-05-strings"
  ],
  "prerequisites": [
    "FSharp-04: Collections"
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

# FSHARP-05-STRINGS: Strings

## Introduction

String operations and interpolation. By the end of this lesson you will be able to: Interpolate strings; Split and join; Use StringBuilder; Work with characters.

## Key Concepts

### 1. Interpolate strings

Target: Interpolate strings. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```fsharp
let name = "Ada"
let msg = $"Hello, {name}!"
```
### 2. Split and join

Target: Split and join. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```fsharp
let parts = "a,b,c".Split(
```
### 3. Use StringBuilder

Target: Use StringBuilder. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```fsharp
)
let joined = String.concat " | " parts
```
### 4. Work with characters

Target: Work with characters. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```fsharp
let upper = "hello".ToUpper()
```

## Practice Questions

1. What is the key idea behind "Strings"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Strings with analogies and real-world examples"
1. "Show me common mistakes beginners make with Strings"
1. "Provide advanced patterns and performance considerations for Strings"

## Key Takeaways

- Master the core ideas of Strings through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
