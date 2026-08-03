---
{
  "title": "Classes and OOP",
  "description": "Interop with the .NET object model.",
  "type": "lesson",
  "order": 12,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define classes",
    "Use properties and methods",
    "Use inheritance",
    "Implement interfaces"
  ],
  "knowledge_refs": [
    "fsharp/fsharp-12-classes"
  ],
  "prerequisites": [
    "FSharp-11: Modules and Namespaces"
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

# FSHARP-12-CLASSES: Classes and OOP

## Introduction

Interop with the .NET object model. By the end of this lesson you will be able to: Define classes; Use properties and methods; Use inheritance; Implement interfaces.

## Key Concepts

### 1. Define classes

Target: Define classes. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```fsharp
type Person(name: string, age: int) =
    member _.Name = name
    member _.Age = age

let ada = Person("Ada", 36)
```
### 2. Use properties and methods

Target: Use properties and methods. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```fsharp
type Counter() =
    let mutable count = 0
    member _.Increment() = count <- count + 1
    member _.Count = count
```
### 3. Use inheritance

Target: Use inheritance. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```fsharp
type Animal() =
    abstract member Speak : unit -> string
    default _.Speak() = "..."

type Dog() =
    inherit Animal()
    override _.Speak() = "Woof"
```
### 4. Implement interfaces

Target: Implement interfaces. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```fsharp
type ILogger =
    abstract member Log : string -> unit
```

## Practice Questions

1. What is the key idea behind "Classes and OOP"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Classes and OOP with analogies and real-world examples"
1. "Show me common mistakes beginners make with Classes and OOP"
1. "Provide advanced patterns and performance considerations for Classes and OOP"

## Key Takeaways

- Master the core ideas of Classes and OOP through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
