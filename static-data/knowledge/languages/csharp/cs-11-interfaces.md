---
{
  "title": "Interfaces and Abstract Classes",
  "description": "Interface contracts, abstract classes, multiple interface implementation.",
  "type": "lesson",
  "order": 11,
  "duration": "75 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define and implement interfaces",
    "Use interfaces as type abstractions",
    "Use abstract classes for shared implementation",
    "Implement multiple interfaces on one type"
  ],
  "knowledge_refs": [
    "csharp/cs-11-interfaces"
  ],
  "prerequisites": [
    "CS-10"
  ],
  "references": [
    {
      "title": "Interfaces Guide",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/types/interfaces"
    },
    {
      "title": "Abstract Classes",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/abstract"
    },
    {
      "title": "Default Interface Methods",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/tutorials/default-interface-methods-versions"
    }
  ]
}
---

# CS-11-INTERFACES: Interfaces and Abstract Classes

## Introduction

Interface contracts, abstract classes, multiple interface implementation. By the end of this lesson you will be able to: Define and implement interfaces; Use interfaces as type abstractions; Use abstract classes for shared implementation; Implement multiple interfaces on one type.

## Key Concepts

### 1. Define and implement interfaces

Target: Define and implement interfaces. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```csharp
interface IShape { double Area(); }
class Square : IShape
{
    public double Side { get; set; }
    public double Area() => Side * Side;
}
IShape s = new Square { Side = 4 };
Console.WriteLine(s.Area());  // 16 (interface reference)
```
### 2. Use interfaces as type abstractions

Target: Use interfaces as type abstractions. Apply the idiomatic pattern — this is how production C# expresses this idea, so study the shape of the code.

```csharp
interface ILogger { void Log(string msg); }
class ConsoleLogger : ILogger
{
    public void Log(string msg) => Console.WriteLine($"[LOG] {msg}");
}
new ConsoleLogger().Log("hello");
```
### 3. Use abstract classes for shared implementation

Target: Use abstract classes for shared implementation. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```csharp
abstract class Shape
{
    public abstract double Area();          // no body
    public string Describe() => "a shape";  // concrete
}
class Circle : Shape
{
    public double Radius { get; set; }
    public override double Area() => Math.PI * Radius * Radius;
}
Console.WriteLine(new Circle { Radius = 2 }.Area());
```
### 4. Implement multiple interfaces on one type

Target: Implement multiple interfaces on one type. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```csharp
interface IA { void A(); }
interface IB { void B(); }
class Both : IA, IB   // multiple interface implementation
{
    public void A() => Console.WriteLine("A");
    public void B() => Console.WriteLine("B");
}
Both b = new(); b.A(); b.B();
```

## Practice Questions

1. What is the key idea behind "Interfaces and Abstract Classes"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Interfaces and Abstract Classes with analogies and real-world examples"
1. "Show me common mistakes beginners make with Interfaces and Abstract Classes"
1. "Provide advanced patterns and performance considerations for Interfaces and Abstract Classes"

## Key Takeaways

- Master the core ideas of Interfaces and Abstract Classes through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked Microsoft Learn docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
