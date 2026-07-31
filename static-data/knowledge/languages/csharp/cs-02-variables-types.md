---
{
  "title": "Variables and Built-in Types",
  "description": "Value vs reference types, var inference, built-in numeric types, and default values.",
  "type": "lesson",
  "order": 2,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Understand value vs reference type semantics",
    "Use built-in numeric, bool, char, and string types",
    "Use var type inference correctly",
    "Understand default values and literals"
  ],
  "knowledge_refs": [
    "csharp/cs-02-variables-types"
  ],
  "prerequisites": [
    "CS-01"
  ],
  "references": [
    {
      "title": "C# Types System",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/types/"
    },
    {
      "title": "Built-in Types",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types"
    },
    {
      "title": "Value Types Reference",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/value-types"
    }
  ]
}
---

# CS-02-VARIABLES-TYPES: Variables and Built-in Types

## Introduction

Value vs reference types, var inference, built-in numeric types, and default values. By the end of this lesson you will be able to: Understand value vs reference type semantics; Use built-in numeric, bool, char, and string types; Use var type inference correctly; Understand default values and literals.

## Key Concepts

### 1. Understand value vs reference type semantics

Target: Understand value vs reference type semantics. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```csharp
int age = 30;                  // value type: stack-allocated
bool isActive = true;
char grade = 'A';
decimal price = 19.99m;         // exact decimal arithmetic
Console.WriteLine($"{age} {isActive} {grade} {price}");
```
### 2. Use built-in numeric, bool, char, and string types

Target: Use built-in numeric, bool, char, and string types. Apply the idiomatic pattern — this is how production C# expresses this idea, so study the shape of the code.

```csharp
string name = "Alice";         // reference type: heap + GC
int[] nums = { 1, 2, 3 };       // reference type (array)
Console.WriteLine($"name: {name}, nums: {nums.Length}");
```
### 3. Use var type inference correctly

Target: Use var type inference correctly. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```csharp
var x = 42;                    // var infers int
var y = "hello";                // var infers string
dynamic d = "anything";         // dynamic resolves at runtime
Console.WriteLine($"{x.GetType()} {y.GetType()} {d}");
```
### 4. Understand default values and literals

Target: Understand default values and literals. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```csharp
int i = default;               // 0
bool b = default;               // false
string? s = default;            // null
Console.WriteLine($"{i} {b} {s is null}");
```

## Practice Questions

1. What is the key idea behind "Variables and Built-in Types"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Variables and Built-in Types with analogies and real-world examples"
1. "Show me common mistakes beginners make with Variables and Built-in Types"
1. "Provide advanced patterns and performance considerations for Variables and Built-in Types"

## Key Takeaways

- Master the core ideas of Variables and Built-in Types through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked Microsoft Learn docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
