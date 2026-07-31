---
{
  "title": "LINQ: Language Integrated Query",
  "description": "Query and method syntax, deferred execution, standard query operators.",
  "type": "lesson",
  "order": 13,
  "duration": "75 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write LINQ queries with method syntax",
    "Write LINQ queries with query syntax",
    "Use aggregation operators (Sum, Average, Min, Max, Count)",
    "Understand deferred vs immediate execution"
  ],
  "knowledge_refs": [
    "csharp/cs-13-linq"
  ],
  "prerequisites": [
    "CS-12"
  ],
  "references": [
    {
      "title": "Introduction to LINQ Queries",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/linq/get-started/introduction-to-linq-queries"
    },
    {
      "title": "Standard Query Operators",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/linq/query-expression-basics"
    },
    {
      "title": "LINQ Method Syntax",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/linq/get-started/write-linq-queries"
    }
  ]
}
---

# CS-13-LINQ: LINQ: Language Integrated Query

## Introduction

Query and method syntax, deferred execution, standard query operators. By the end of this lesson you will be able to: Write LINQ queries with method syntax; Write LINQ queries with query syntax; Use aggregation operators (Sum, Average, Min, Max, Count); Understand deferred vs immediate execution.

## Key Concepts

### 1. Write LINQ queries with method syntax

Target: Write LINQ queries with method syntax. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```csharp
var nums = new[] { 1, 2, 3, 4 };
var evens = nums.Where(n => n % 2 == 0);        // method syntax
var doubled = nums.Select(n => n * 2);
Console.WriteLine(string.Join(",", evens));     // 2,4
Console.WriteLine(string.Join(",", doubled));   // 2,4,6,8
```
### 2. Write LINQ queries with query syntax

Target: Write LINQ queries with query syntax. Apply the idiomatic pattern — this is how production C# expresses this idea, so study the shape of the code.

```csharp
var people = new[] { new { Name = "Alice", Age = 30 }, new { Name = "Bob", Age = 25 } };
var query = from p in people              // query syntax
            where p.Age >= 25
            orderby p.Age descending
            select p.Name;
foreach (var n in query) Console.WriteLine(n);  // Alice, Bob
```
### 3. Use aggregation operators (Sum, Average, Min, Max, Count)

Target: Use aggregation operators (Sum, Average, Min, Max, Count). Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```csharp
var nums = new[] { 1, 2, 3, 4, 5 };
Console.WriteLine(nums.Sum());          // 15
Console.WriteLine(nums.Average());      // 3
Console.WriteLine(nums.Min());          // 1
Console.WriteLine(nums.Max());          // 5
Console.WriteLine(nums.Count(n => n > 2)); // 3
```
### 4. Understand deferred vs immediate execution

Target: Understand deferred vs immediate execution. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```csharp
// Deferred execution: query runs when enumerated
var q = nums.Where(n => n > 2);
nums = nums.Append(9).ToArray();        // 9 not in q yet
Console.WriteLine(string.Join(",", q)); // 3,4,5
var eager = nums.Where(n => n > 2).ToList();  // immediate
```

## Practice Questions

1. What is the key idea behind "LINQ: Language Integrated Query"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain LINQ: Language Integrated Query with analogies and real-world examples"
1. "Show me common mistakes beginners make with LINQ: Language Integrated Query"
1. "Provide advanced patterns and performance considerations for LINQ: Language Integrated Query"

## Key Takeaways

- Master the core ideas of LINQ: Language Integrated Query through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked Microsoft Learn docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
