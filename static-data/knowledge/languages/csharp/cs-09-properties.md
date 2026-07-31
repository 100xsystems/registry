---
{
  "title": "Properties, Indexers, and Fields",
  "description": "Auto-properties, get/set accessors, computed properties, and indexers.",
  "type": "lesson",
  "order": 9,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Implement auto-implemented properties",
    "Write custom get/set accessors with validation logic",
    "Implement indexers for indexed access",
    "Use init-only and expression-bodied members"
  ],
  "knowledge_refs": [
    "csharp/cs-09-properties"
  ],
  "prerequisites": [
    "CS-08"
  ],
  "references": [
    {
      "title": "C# Properties",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/properties"
    },
    {
      "title": "Indexers",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/indexers/"
    },
    {
      "title": "Auto-Implemented Properties",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/auto-implemented-properties"
    }
  ]
}
---

# CS-09-PROPERTIES: Properties, Indexers, and Fields

## Introduction

Auto-properties, get/set accessors, computed properties, and indexers. By the end of this lesson you will be able to: Implement auto-implemented properties; Write custom get/set accessors with validation logic; Implement indexers for indexed access; Use init-only and expression-bodied members.

## Key Concepts

### 1. Implement auto-implemented properties

Target: Implement auto-implemented properties. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```csharp
class Temperature
{
    public double Celsius { get; set; }
    public double Fahrenheit => Celsius * 9 / 5 + 32;
}
var t = new Temperature { Celsius = 25 };
Console.WriteLine($"{t.Fahrenheit:F1}°F");  // 77.0°F
```
### 2. Write custom get/set accessors with validation logic

Target: Write custom get/set accessors with validation logic. Apply the idiomatic pattern — this is how production C# expresses this idea, so study the shape of the code.

```csharp
class Person
{
    private string _name = "";
    public string Name
    {
        get => _name;
        set => _name = string.IsNullOrWhiteSpace(value) ? "unknown" : value;
    }
}
var p = new Person { Name = "" };
Console.WriteLine(p.Name);  // unknown
```
### 3. Implement indexers for indexed access

Target: Implement indexers for indexed access. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```csharp
class Matrix
{
    private readonly int[,] _data;
    public Matrix(int[,] data) => _data = data;
    public int this[int r, int c] => _data[r, c];
}
var m = new Matrix(new int[,] { { 1, 2 }, { 3, 4 } });
Console.WriteLine(m[1, 0]);   // 3 (indexer)
```
### 4. Use init-only and expression-bodied members

Target: Use init-only and expression-bodied members. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```csharp
class Stats
{
    public int Count { get; init; }   // init-only (set at construction)
    public string Name { get; set; } = "default";
}
var s = new Stats { Count = 5, Name = "x" };
Console.WriteLine($"{s.Count} {s.Name}");
```

## Practice Questions

1. What is the key idea behind "Properties, Indexers, and Fields"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Properties, Indexers, and Fields with analogies and real-world examples"
1. "Show me common mistakes beginners make with Properties, Indexers, and Fields"
1. "Provide advanced patterns and performance considerations for Properties, Indexers, and Fields"

## Key Takeaways

- Master the core ideas of Properties, Indexers, and Fields through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked Microsoft Learn docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
