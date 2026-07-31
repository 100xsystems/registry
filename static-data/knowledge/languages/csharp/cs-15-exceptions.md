---
{
  "title": "Exceptions and Error Handling",
  "description": "try/catch/finally, exception filters, custom exceptions, throw expressions.",
  "type": "lesson",
  "order": 15,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write try/catch/finally blocks",
    "Use exception filters with when",
    "Create custom exception types",
    "Use throw expressions and defensive coding"
  ],
  "knowledge_refs": [
    "csharp/cs-15-exceptions"
  ],
  "prerequisites": [
    "CS-14"
  ],
  "references": [
    {
      "title": "Exception Handling Statements",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/exception-handling-statements"
    },
    {
      "title": "Exceptions and Errors",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/exceptions/"
    },
    {
      "title": "Best Practices",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/exceptions/best-practices-for-exceptions"
    }
  ]
}
---

# CS-15-EXCEPTIONS: Exceptions and Error Handling

## Introduction

try/catch/finally, exception filters, custom exceptions, throw expressions. By the end of this lesson you will be able to: Write try/catch/finally blocks; Use exception filters with when; Create custom exception types; Use throw expressions and defensive coding.

## Key Concepts

### 1. Write try/catch/finally blocks

Target: Write try/catch/finally blocks. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```csharp
try
{
    int.Parse("not-a-number");
}
catch (FormatException ex)
{
    Console.WriteLine($"Format: {ex.Message}");
}
finally
{
    Console.WriteLine("Cleanup always runs");
}
```
### 2. Use exception filters with when

Target: Use exception filters with when. Apply the idiomatic pattern — this is how production C# expresses this idea, so study the shape of the code.

```csharp
try
{
    throw new InvalidOperationException("custom failure");
}
catch (InvalidOperationException) when (DateTime.Now.Day > 0)  // filter
{
    Console.WriteLine("Filtered catch");
}
```
### 3. Create custom exception types

Target: Create custom exception types. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```csharp
class ValidationException : Exception
{
    public ValidationException(string field) : base($"Invalid: {field}") { }
}
try { throw new ValidationException("email"); }
catch (ValidationException ex) { Console.WriteLine(ex.Message); }
```
### 4. Use throw expressions and defensive coding

Target: Use throw expressions and defensive coding. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```csharp
static int SafeDivide(int a, int b) =>
    b == 0 ? throw new DivideByZeroException() : a / b;
try { Console.WriteLine(SafeDivide(4, 0)); }
catch (DivideByZeroException) { Console.WriteLine("Cannot divide by zero"); }
```

## Practice Questions

1. What is the key idea behind "Exceptions and Error Handling"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Exceptions and Error Handling with analogies and real-world examples"
1. "Show me common mistakes beginners make with Exceptions and Error Handling"
1. "Provide advanced patterns and performance considerations for Exceptions and Error Handling"

## Key Takeaways

- Master the core ideas of Exceptions and Error Handling through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked Microsoft Learn docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
