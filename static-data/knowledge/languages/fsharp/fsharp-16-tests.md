---
{
  "title": "Testing with xUnit",
  "description": "Unit testing in F#.",
  "type": "lesson",
  "order": 16,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Create a test project",
    "Write xUnit tests",
    "Use assertions",
    "Run dotnet test"
  ],
  "knowledge_refs": [
    "fsharp/fsharp-16-tests"
  ],
  "prerequisites": [
    "FSharp-15: File I/O"
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

# FSHARP-16-TESTS: Testing with xUnit

## Introduction

Unit testing in F#. By the end of this lesson you will be able to: Create a test project; Write xUnit tests; Use assertions; Run dotnet test.

## Key Concepts

### 1. Create a test project

Target: Create a test project. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```fsharp
dotnet new xunit -lang F# -o tests
```
### 2. Write xUnit tests

Target: Write xUnit tests. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```fsharp
module Tests

open Xunit

[<Fact>]
let ``addition works`` () =
    Assert.Equal(4, 2 + 2)
```
### 3. Use assertions

Target: Use assertions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```fsharp
[<Theory>]
[<InlineData(1, 1, 2)>]
[<InlineData(2, 3, 5)>]
let ``add works`` (a, b, expected) =
    Assert.Equal(expected, a + b)
```
### 4. Run dotnet test

Target: Run dotnet test. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```fsharp
Assert.True(5 > 3)
```

## Practice Questions

1. What is the key idea behind "Testing with xUnit"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Testing with xUnit with analogies and real-world examples"
1. "Show me common mistakes beginners make with Testing with xUnit"
1. "Provide advanced patterns and performance considerations for Testing with xUnit"

## Key Takeaways

- Master the core ideas of Testing with xUnit through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
