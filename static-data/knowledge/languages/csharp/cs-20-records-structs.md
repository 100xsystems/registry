---
{
  "title": "Records, Structs, and Tuples",
  "description": "Record types, with-expressions, tuples, deconstruction, structs as value types.",
  "type": "lesson",
  "order": 20,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Define record types with value equality",
    "Use with-expressions for non-destructive mutation",
    "Use tuples and deconstruction",
    "Write structs with value semantics"
  ],
  "knowledge_refs": [
    "csharp/cs-20-records-structs"
  ],
  "prerequisites": [
    "CS-19"
  ],
  "references": [
    {
      "title": "Records Guide",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/types/records"
    },
    {
      "title": "Tuples Guide",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/types/tuples"
    },
    {
      "title": "Struct Types",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/struct"
    }
  ]
}
---

# CS-20-RECORDS-STRUCTS: Records, Structs, and Tuples

## Introduction

Record types, with-expressions, tuples, deconstruction, structs as value types. By the end of this lesson you will be able to: Define record types with value equality; Use with-expressions for non-destructive mutation; Use tuples and deconstruction; Write structs with value semantics.

## Key Concepts

### 1. Define record types with value equality

Target: Define record types with value equality. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```csharp
record Person(string Name, int Age);
var alice = new Person("Alice", 30);
Console.WriteLine(alice);   // Person { Name = Alice, Age = 30 }
Console.WriteLine(alice == new Person("Alice", 30));  // True (value eq)
```
### 2. Use with-expressions for non-destructive mutation

Target: Use with-expressions for non-destructive mutation. Apply the idiomatic pattern — this is how production C# expresses this idea, so study the shape of the code.

```csharp
record Person(string Name, int Age);
var alice = new Person("Alice", 30);
var bob = alice with { Age = 31 };   // non-destructive copy
Console.WriteLine(bob);   // Person { Name = Alice, Age = 31 }
```
### 3. Use tuples and deconstruction

Target: Use tuples and deconstruction. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```csharp
var tuple = (Name: "Alice", Age: 30);   // named tuple
Console.WriteLine($"{tuple.Name} {tuple.Age}");
var (name, age) = tuple;                 // deconstruction
Console.WriteLine($"{name} {age}");
```
### 4. Write structs with value semantics

Target: Write structs with value semantics. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```csharp
struct Point
{
    public int X { get; set; }
    public int Y { get; set; }
}
// structs are value types: copies on assignment
Point p1 = new() { X = 1, Y = 2 };
Point p2 = p1;
p2.X = 99;
Console.WriteLine(p1.X);  // 1 (p2 is a copy)
```

## Practice Questions

1. What is the key idea behind "Records, Structs, and Tuples"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Records, Structs, and Tuples with analogies and real-world examples"
1. "Show me common mistakes beginners make with Records, Structs, and Tuples"
1. "Provide advanced patterns and performance considerations for Records, Structs, and Tuples"

## Key Takeaways

- Master the core ideas of Records, Structs, and Tuples through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked Microsoft Learn docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
