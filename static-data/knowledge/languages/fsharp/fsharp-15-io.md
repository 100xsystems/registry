---
{
  "title": "File I/O",
  "description": "Read and write files.",
  "type": "lesson",
  "order": 15,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Read files",
    "Write files",
    "Read lines",
    "Use paths"
  ],
  "knowledge_refs": [
    "fsharp/fsharp-15-io"
  ],
  "prerequisites": [
    "FSharp-14: Async and Parallel"
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

# FSHARP-15-IO: File I/O

## Introduction

Read and write files. By the end of this lesson you will be able to: Read files; Write files; Read lines; Use paths.

## Key Concepts

### 1. Read files

Target: Read files. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```fsharp
let content = System.IO.File.ReadAllText("data.txt")
```
### 2. Write files

Target: Write files. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```fsharp
System.IO.File.WriteAllText("out.txt", "hello")
```
### 3. Read lines

Target: Read lines. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```fsharp
System.IO.File.ReadLines("data.txt") |> Seq.iter (printfn "%s")
```
### 4. Use paths

Target: Use paths. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```fsharp
System.IO.Directory.GetFiles(".")
```

## Practice Questions

1. What is the key idea behind "File I/O"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain File I/O with analogies and real-world examples"
1. "Show me common mistakes beginners make with File I/O"
1. "Provide advanced patterns and performance considerations for File I/O"

## Key Takeaways

- Master the core ideas of File I/O through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
