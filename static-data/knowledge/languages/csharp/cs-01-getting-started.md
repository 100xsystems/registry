---
{
  "title": "Getting Started with C# and the .NET CLI",
  "description": "Install the .NET SDK, understand dotnet CLI (new/build/run), project structure, and write Hello World.",
  "type": "lesson",
  "order": 1,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Install the .NET SDK and set up the toolchain",
    "Understand dotnet new / build / run lifecycle",
    "Understand project structure and namespaces",
    "Write and run your first C# program"
  ],
  "knowledge_refs": [
    "csharp/cs-01-getting-started"
  ],
  "prerequisites": [],
  "references": [
    {
      "title": "Tour of C# Overview",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/tour-of-csharp/overview"
    },
    {
      "title": "Get Started with C#",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/getting-started/"
    },
    {
      "title": "dotnet CLI Overview",
      "url": "https://learn.microsoft.com/en-us/dotnet/core/tools/"
    }
  ]
}
---

# CS-01-GETTING-STARTED: Getting Started with C# and the .NET CLI

## Introduction

Install the .NET SDK, understand dotnet CLI (new/build/run), project structure, and write Hello World. By the end of this lesson you will be able to: Install the .NET SDK and set up the toolchain; Understand dotnet new / build / run lifecycle; Understand project structure and namespaces; Write and run your first C# program.

## Key Concepts

### 1. Install the .NET SDK and set up the toolchain

Target: Install the .NET SDK and set up the toolchain. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```csharp
using System;

// .NET SDK toolchain: dotnet new console, dotnet build, dotnet run
Console.WriteLine("Hello, 100X Systems!");
Console.WriteLine($"Args: {args.Length}");
```
### 2. Understand dotnet new / build / run lifecycle

Target: Understand dotnet new / build / run lifecycle. Apply the idiomatic pattern — this is how production C# expresses this idea, so study the shape of the code.

```csharp
var sln = "app.sln";             // solution file groups projects
// dotnet new sln, dotnet sln add, dotnet build, dotnet run
Console.WriteLine(Path.GetFileName(sln));
```
### 3. Understand project structure and namespaces

Target: Understand project structure and namespaces. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```csharp
namespace HelloWorld;           // file-scoped namespace (C# 10+)

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Top-level statements avoid this boilerplate");
    }
}
```
### 4. Write and run your first C# program

Target: Write and run your first C# program. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```csharp
// Top-level statements: minimal entry point
Console.WriteLine("Hello from top-level statements!");
Console.WriteLine("dotnet run compiles + executes in one step");
```

## Practice Questions

1. What is the key idea behind "Getting Started with C# and the .NET CLI"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with C# and the .NET CLI with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with C# and the .NET CLI"
1. "Provide advanced patterns and performance considerations for Getting Started with C# and the .NET CLI"

## Key Takeaways

- Master the core ideas of Getting Started with C# and the .NET CLI through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked Microsoft Learn docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
