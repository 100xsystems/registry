---
{
  "title": "Nullable Types and Pattern Matching",
  "description": "Nullable value types, nullable reference types, is patterns, switch patterns.",
  "type": "lesson",
  "order": 19,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use Nullable<T> and nullable reference types",
    "Use null-conditional operators",
    "Write is expressions with type patterns",
    "Use switch expressions with patterns"
  ],
  "knowledge_refs": [
    "csharp/cs-19-patterns-nullable"
  ],
  "prerequisites": [
    "CS-18"
  ],
  "references": [
    {
      "title": "Pattern Matching",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/patterns"
    },
    {
      "title": "Nullable Value Types",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/nullable-value-types"
    },
    {
      "title": "Nullable Reference Types",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/nullable-references"
    }
  ]
}
---

# CS-19-PATTERNS-NULLABLE: Nullable Types and Pattern Matching

## Introduction

Nullable value types, nullable reference types, is patterns, switch patterns. By the end of this lesson you will be able to: Use Nullable<T> and nullable reference types; Use null-conditional operators; Write is expressions with type patterns; Use switch expressions with patterns.

## Key Concepts

### 1. Use Nullable<T> and nullable reference types

Target: Use Nullable<T> and nullable reference types. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```csharp
int? count = null;               // Nullable<int>
Console.WriteLine(count.HasValue);       // False
Console.WriteLine(count ?? 5);           // 5
count = 3;
Console.WriteLine(count.Value);          // 3
```
### 2. Use null-conditional operators

Target: Use null-conditional operators. Apply the idiomatic pattern — this is how production C# expresses this idea, so study the shape of the code.

```csharp
string? name = null;             // nullable reference type
Console.WriteLine(name?.Length ?? 0);   // 0 (safe navigation)
```
### 3. Write is expressions with type patterns

Target: Write is expressions with type patterns. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```csharp
object value = 42;
if (value is int i) Console.WriteLine($"int: {i}");      // type pattern
if (value is not string) Console.WriteLine("not a string");
if (value is int n && n > 0) Console.WriteLine("positive");
```
### 4. Use switch expressions with patterns

Target: Use switch expressions with patterns. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```csharp
string shape = "circle";
string describe = shape switch
{
    "circle" => "round",
    "square" => "four sides",
    _ => "unknown"
};
Console.WriteLine(describe);  // round

object? maybe = null;
var result = maybe switch
{
    null => "null",
    int x when x > 100 => "big",
    _ => "other"
};
```

## Practice Questions

1. What is the key idea behind "Nullable Types and Pattern Matching"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Nullable Types and Pattern Matching with analogies and real-world examples"
1. "Show me common mistakes beginners make with Nullable Types and Pattern Matching"
1. "Provide advanced patterns and performance considerations for Nullable Types and Pattern Matching"

## Key Takeaways

- Master the core ideas of Nullable Types and Pattern Matching through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked Microsoft Learn docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
