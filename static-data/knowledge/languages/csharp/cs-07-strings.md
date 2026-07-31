---
{
  "title": "Strings and String Interpolation",
  "description": "String immutability, interpolation, StringBuilder, and common string methods.",
  "type": "lesson",
  "order": 7,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Understand string immutability",
    "Use string interpolation and formatting",
    "Use StringBuilder for efficient concatenation",
    "Master common string methods and slicing"
  ],
  "knowledge_refs": [
    "csharp/cs-07-strings"
  ],
  "prerequisites": [
    "CS-06"
  ],
  "references": [
    {
      "title": "String Concatenation",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/strings/common-tasks/concatenate"
    },
    {
      "title": "String Interpolation",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/tokens/interpolated"
    },
    {
      "title": "StringBuilder Class",
      "url": "https://learn.microsoft.com/en-us/dotnet/api/system.text.stringbuilder"
    }
  ]
}
---

# CS-07-STRINGS: Strings and String Interpolation

## Introduction

String immutability, interpolation, StringBuilder, and common string methods. By the end of this lesson you will be able to: Understand string immutability; Use string interpolation and formatting; Use StringBuilder for efficient concatenation; Master common string methods and slicing.

## Key Concepts

### 1. Understand string immutability

Target: Understand string immutability. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```csharp
string greeting = "Hello";
string who = "World";
string msg = greeting + ", " + who + "!";  // concatenation
Console.WriteLine(msg);
```
### 2. Use string interpolation and formatting

Target: Use string interpolation and formatting. Apply the idiomatic pattern — this is how production C# expresses this idea, so study the shape of the code.

```csharp
string name = "World";
string msg = $"Hello, {name}!";
Console.WriteLine(msg);
Console.WriteLine($"Pi is {Math.PI:F2}");   // formatted
```
### 3. Use StringBuilder for efficient concatenation

Target: Use StringBuilder for efficient concatenation. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```csharp
var sb = new System.Text.StringBuilder();
for (int i = 0; i < 3; i++) sb.Append(i).Append("-");
Console.WriteLine(sb.ToString().TrimEnd('-')); // 0-1-2
```
### 4. Master common string methods and slicing

Target: Master common string methods and slicing. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```csharp
string text = "Hello World";
Console.WriteLine(text.ToUpper());         // HELLO WORLD
Console.WriteLine(text.Contains("World")); // True
Console.WriteLine(text[0..5]);             // Hello (range)
Console.WriteLine(text.Split(' ').Length); // 2
```

## Practice Questions

1. What is the key idea behind "Strings and String Interpolation"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Strings and String Interpolation with analogies and real-world examples"
1. "Show me common mistakes beginners make with Strings and String Interpolation"
1. "Provide advanced patterns and performance considerations for Strings and String Interpolation"

## Key Takeaways

- Master the core ideas of Strings and String Interpolation through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked Microsoft Learn docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
