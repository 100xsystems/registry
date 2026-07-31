---
{
  "title": "Operators and Expressions",
  "description": "Arithmetic, comparison, logical, bitwise operators; precedence and null-coalescing.",
  "type": "lesson",
  "order": 3,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use arithmetic, comparison, and logical operators",
    "Use the ternary and null-coalescing operators",
    "Use bitwise operators for flags and bit tricks",
    "Understand precedence and associativity"
  ],
  "knowledge_refs": [
    "csharp/cs-03-operators-expressions"
  ],
  "prerequisites": [
    "CS-02"
  ],
  "references": [
    {
      "title": "C# Operators Reference",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/"
    },
    {
      "title": "Operator Precedence",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/#operator-precedence"
    },
    {
      "title": "Numeric Conversions",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/numeric-conversions"
    }
  ]
}
---

# CS-03-OPERATORS-EXPRESSIONS: Operators and Expressions

## Introduction

Arithmetic, comparison, logical, bitwise operators; precedence and null-coalescing. By the end of this lesson you will be able to: Use arithmetic, comparison, and logical operators; Use the ternary and null-coalescing operators; Use bitwise operators for flags and bit tricks; Understand precedence and associativity.

## Key Concepts

### 1. Use arithmetic, comparison, and logical operators

Target: Use arithmetic, comparison, and logical operators. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```csharp
int a = 17, b = 5;
Console.WriteLine(a + b);       // 22
Console.WriteLine(a - b);       // 12
Console.WriteLine(a * b);       // 85
Console.WriteLine(a / b);       // 3 (integer division)
Console.WriteLine(a % b);       // 2 (remainder)
```
### 2. Use the ternary and null-coalescing operators

Target: Use the ternary and null-coalescing operators. Apply the idiomatic pattern — this is how production C# expresses this idea, so study the shape of the code.

```csharp
double x = 17.0, y = 5.0;
Console.WriteLine(x / y);       // 3.4
Console.WriteLine(x == y);      // false
Console.WriteLine(x > y);       // true
bool both = x > 0 && y > 0;     // logical AND
bool either = x > 100 || y > 0; // logical OR
```
### 3. Use bitwise operators for flags and bit tricks

Target: Use bitwise operators for flags and bit tricks. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```csharp
int? maybe = null;
int fallback = maybe ?? 42;     // null-coalescing
int cond = fallback > 40 ? 1 : 0; // ternary
Console.WriteLine($"{fallback} {cond}");
```
### 4. Understand precedence and associativity

Target: Understand precedence and associativity. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```csharp
int flags = 0b1100;            // 12
Console.WriteLine(flags & 0b1010); // 1000 = 8 (AND)
Console.WriteLine(flags | 0b0001); // 1101 = 13 (OR)
Console.WriteLine(flags << 1);     // 11000 = 24 (shift left)
```

## Practice Questions

1. What is the key idea behind "Operators and Expressions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Operators and Expressions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Operators and Expressions"
1. "Provide advanced patterns and performance considerations for Operators and Expressions"

## Key Takeaways

- Master the core ideas of Operators and Expressions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked Microsoft Learn docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
