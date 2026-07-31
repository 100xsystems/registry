---
{
  "title": "Classes and Objects",
  "description": "Class declarations, constructors, this, static members, and object initializers.",
  "type": "lesson",
  "order": 8,
  "duration": "75 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Declare classes with fields, properties, and methods",
    "Write constructors and overloads",
    "Use static members and classes",
    "Use object and collection initializers"
  ],
  "knowledge_refs": [
    "csharp/cs-08-classes-objects"
  ],
  "prerequisites": [
    "CS-07"
  ],
  "references": [
    {
      "title": "OOP in C#",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/object-oriented/"
    },
    {
      "title": "Classes and Structs",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/types/classes"
    },
    {
      "title": "Constructors",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/constructors"
    }
  ]
}
---

# CS-08-CLASSES-OBJECTS: Classes and Objects

## Introduction

Class declarations, constructors, this, static members, and object initializers. By the end of this lesson you will be able to: Declare classes with fields, properties, and methods; Write constructors and overloads; Use static members and classes; Use object and collection initializers.

## Key Concepts

### 1. Declare classes with fields, properties, and methods

Target: Declare classes with fields, properties, and methods. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```csharp
class BankAccount
{
    public decimal Balance { get; private set; }
    public BankAccount(decimal initial) => Balance = initial;
    public void Deposit(decimal amount) => Balance += amount;
}
var acct = new BankAccount(100m);
acct.Deposit(50m);
Console.WriteLine(acct.Balance);   // 150
```
### 2. Write constructors and overloads

Target: Write constructors and overloads. Apply the idiomatic pattern — this is how production C# expresses this idea, so study the shape of the code.

```csharp
class Point
{
    public int X { get; }
    public int Y { get; }
    public Point(int x, int y) { X = x; Y = y; }
    public override string ToString() => $"({X}, {Y})";
}
Console.WriteLine(new Point(3, 4));  // (3, 4)
```
### 3. Use static members and classes

Target: Use static members and classes. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```csharp
class Counter
{
    public static int Instances { get; private set; }
    public Counter() => Instances++;
    public static void Describe() => Console.WriteLine($"Count: {Instances}");
}
new Counter(); new Counter();
Counter.Describe();   // Count: 2 (static, no instance)
```
### 4. Use object and collection initializers

Target: Use object and collection initializers. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```csharp
var p = new Point(1, 2);
p = new Point { X = 5, Y = 6 };   // re-assign (immutable props)
var list = new List<Point> { new(0, 0), new(1, 1) };
Console.WriteLine(list.Count);
```

## Practice Questions

1. What is the key idea behind "Classes and Objects"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Classes and Objects with analogies and real-world examples"
1. "Show me common mistakes beginners make with Classes and Objects"
1. "Provide advanced patterns and performance considerations for Classes and Objects"

## Key Takeaways

- Master the core ideas of Classes and Objects through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked Microsoft Learn docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
