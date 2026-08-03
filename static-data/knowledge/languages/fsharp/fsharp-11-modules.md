---
{
  "title": "Modules and Namespaces",
  "description": "Organize code with modules.",
  "type": "lesson",
  "order": 11,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create modules",
    "Use module functions",
    "Nest modules",
    "Control visibility"
  ],
  "knowledge_refs": [
    "fsharp/fsharp-11-modules"
  ],
  "prerequisites": [
    "FSharp-10: Recursion"
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

# FSHARP-11-MODULES: Modules and Namespaces

## Introduction

Organize code with modules. By the end of this lesson you will be able to: Create modules; Use module functions; Nest modules; Control visibility.

## Key Concepts

### 1. Create modules

Target: Create modules. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```fsharp
module Math =
    let square x = x * x

Math.square 5
```
### 2. Use module functions

Target: Use module functions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```fsharp
module Geometry =
    module Circle =
        let area r = 3.14159 * r * r
```
### 3. Nest modules

Target: Nest modules. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```fsharp
module private Helpers =
    let secret () = 42
```
### 4. Control visibility

Target: Control visibility. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```fsharp
module StringUtils =
    let reverse (s: string) =
        s |> Seq.rev |> System.String.Concat
```

## Practice Questions

1. What is the key idea behind "Modules and Namespaces"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Modules and Namespaces with analogies and real-world examples"
1. "Show me common mistakes beginners make with Modules and Namespaces"
1. "Provide advanced patterns and performance considerations for Modules and Namespaces"

## Key Takeaways

- Master the core ideas of Modules and Namespaces through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
