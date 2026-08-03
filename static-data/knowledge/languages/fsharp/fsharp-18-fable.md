---
{
  "title": "Fable: F# in the Browser",
  "description": "Compile F# to JavaScript.",
  "type": "lesson",
  "order": 18,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Set up Fable",
    "Build a web app",
    "Interop with JS",
    "Use Elmish"
  ],
  "knowledge_refs": [
    "fsharp/fsharp-18-fable"
  ],
  "prerequisites": [
    "FSharp-17: Property Testing with FsCheck"
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

# FSHARP-18-FABLE: Fable: F# in the Browser

## Introduction

Compile F# to JavaScript. By the end of this lesson you will be able to: Set up Fable; Build a web app; Interop with JS; Use Elmish.

## Key Concepts

### 1. Set up Fable

Target: Set up Fable. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```fsharp
dotnet new fable -lang F#
```
### 2. Build a web app

Target: Build a web app. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```fsharp
module App

open Fable.Core.JsInterop

let main () =
    emitJsStatement () "document.body.textContent = 'Hello from F#';"
```
### 3. Interop with JS

Target: Interop with JS. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```fsharp
importAll "bootstrap/dist/css/bootstrap.min.css"
```
### 4. Use Elmish

Target: Use Elmish. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```fsharp
open Elmish
open Elmish.React
```

## Practice Questions

1. What is the key idea behind "Fable: F# in the Browser"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Fable: F# in the Browser with analogies and real-world examples"
1. "Show me common mistakes beginners make with Fable: F# in the Browser"
1. "Provide advanced patterns and performance considerations for Fable: F# in the Browser"

## Key Takeaways

- Master the core ideas of Fable: F# in the Browser through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
