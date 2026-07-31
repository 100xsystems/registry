---
{
  "title": "Generics",
  "description": "Generic types and methods, constraints, and covariance/contravariance.",
  "type": "lesson",
  "order": 12,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write generic classes and methods",
    "Apply type parameter constraints",
    "Understand covariance and contravariance",
    "Use generic collections effectively"
  ],
  "knowledge_refs": [
    "csharp/cs-12-generics"
  ],
  "prerequisites": [
    "CS-11"
  ],
  "references": [
    {
      "title": "Generics Overview",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/types/generics"
    },
    {
      "title": "Generic Constraints",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/generics/constraints-on-type-parameters"
    },
    {
      "title": "Variance in Generics",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/covariance-contravariance/"
    }
  ]
}
---

# CS-12-GENERICS: Generics

## Introduction

Generic types and methods, constraints, and covariance/contravariance. By the end of this lesson you will be able to: Write generic classes and methods; Apply type parameter constraints; Understand covariance and contravariance; Use generic collections effectively.

## Key Concepts

### 1. Write generic classes and methods

Target: Write generic classes and methods. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```csharp
class Box<T>
{
    public T Value { get; set; } = default!;
}
var intBox = new Box<int> { Value = 42 };
var strBox = new Box<string> { Value = "hi" };
Console.WriteLine($"{intBox.Value} {strBox.Value}");
```
### 2. Apply type parameter constraints

Target: Apply type parameter constraints. Apply the idiomatic pattern — this is how production C# expresses this idea, so study the shape of the code.

```csharp
static T Max<T>(T a, T b) where T : IComparable<T>
    => a.CompareTo(b) >= 0 ? a : b;
Console.WriteLine(Max(3, 9));            // 9
Console.WriteLine(Max("apple", "pear")); // pear
```
### 3. Understand covariance and contravariance

Target: Understand covariance and contravariance. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```csharp
class Repository<T> where T : class, new()
{
    private readonly List<T> _items = new();
    public void Add(T item) => _items.Add(item);
    public int Count => _items.Count;
}
var repo = new Repository<string>();
repo.Add("a");
Console.WriteLine(repo.Count);  // 1
```
### 4. Use generic collections effectively

Target: Use generic collections effectively. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```csharp
// Covariance: IEnumerable<Derived> is IEnumerable<Base>
IEnumerable<string> strings = new[] { "a", "b" };
IEnumerable<object> objs = strings;   // OK (out T)
foreach (var o in objs) Console.WriteLine(o);
```

## Practice Questions

1. What is the key idea behind "Generics"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Generics with analogies and real-world examples"
1. "Show me common mistakes beginners make with Generics"
1. "Provide advanced patterns and performance considerations for Generics"

## Key Takeaways

- Master the core ideas of Generics through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked Microsoft Learn docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
