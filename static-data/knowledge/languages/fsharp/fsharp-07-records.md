---
{
  "title": "Records and Tuples",
  "description": "Structured data types.",
  "type": "lesson",
  "order": 7,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define records",
    "Create and update records",
    "Use tuples",
    "Pattern match records"
  ],
  "knowledge_refs": [
    "fsharp/fsharp-07-records"
  ],
  "prerequisites": [
    "FSharp-06: Option and Result"
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

# FSHARP-07-RECORDS: Records and Tuples

## Introduction

Structured data types. By the end of this lesson you will be able to: Define records; Create and update records; Use tuples; Pattern match records.

## Key Concepts

### 1. Define records

Target: Define records. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```fsharp
type Person = { Name: string; Age: int }

let ada = { Name = "Ada"; Age = 36 }
```
### 2. Create and update records

Target: Create and update records. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```fsharp
let older = { ada with Age = 37 }
```
### 3. Use tuples

Target: Use tuples. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```fsharp
let pair = (1, "one")
fst pair
```
### 4. Pattern match records

Target: Pattern match records. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```fsharp
let describe p =
    match p with
    | { Name = n; Age = a } -> sprintf "%s is %d" n a
```

## Practice Questions

1. What is the key idea behind "Records and Tuples"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Records and Tuples with analogies and real-world examples"
1. "Show me common mistakes beginners make with Records and Tuples"
1. "Provide advanced patterns and performance considerations for Records and Tuples"

## Key Takeaways

- Master the core ideas of Records and Tuples through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
