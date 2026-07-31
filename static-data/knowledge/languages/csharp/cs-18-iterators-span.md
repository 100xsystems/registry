---
{
  "title": "Iterators, IEnumerable, and Span<T>",
  "description": "yield return, IEnumerable/IEnumerator, lazy evaluation, Span and Memory.",
  "type": "lesson",
  "order": 18,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Implement iterators with yield return",
    "Understand lazy evaluation",
    "Iterate with IEnumerator manually",
    "Use Span<T> for allocation-free access"
  ],
  "knowledge_refs": [
    "csharp/cs-18-iterators-span"
  ],
  "prerequisites": [
    "CS-17"
  ],
  "references": [
    {
      "title": "Iterators",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/iterators"
    },
    {
      "title": "IEnumerable Interface",
      "url": "https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.ienumerable-1"
    },
    {
      "title": "Span and Memory",
      "url": "https://learn.microsoft.com/en-us/dotnet/standard/memory-and-spans/"
    }
  ]
}
---

# CS-18-ITERATORS-SPAN: Iterators, IEnumerable, and Span<T>

## Introduction

yield return, IEnumerable/IEnumerator, lazy evaluation, Span and Memory. By the end of this lesson you will be able to: Implement iterators with yield return; Understand lazy evaluation; Iterate with IEnumerator manually; Use Span<T> for allocation-free access.

## Key Concepts

### 1. Implement iterators with yield return

Target: Implement iterators with yield return. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```csharp
static IEnumerable<int> Fib()
{
    int a = 0, b = 1;
    while (true) { yield return a; (a, b) = (b, a + b); }
}
foreach (var f in Fib().Take(8)) Console.Write($"{f} ");  // 0 1 1 2 3 5 8 13
```
### 2. Understand lazy evaluation

Target: Understand lazy evaluation. Apply the idiomatic pattern — this is how production C# expresses this idea, so study the shape of the code.

```csharp
static IEnumerable<int> Range(int start, int count)
{
    for (int i = 0; i < count; i++) yield return start + i;
}
var r = Range(10, 3);  // nothing runs yet (lazy)
Console.WriteLine(string.Join(",", r));  // 10,11,12
```
### 3. Iterate with IEnumerator manually

Target: Iterate with IEnumerator manually. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```csharp
// IEnumerable<T> = read-only forward iteration
IEnumerable<int> seq = new[] { 1, 2, 3 };
var e = seq.GetEnumerator();
while (e.MoveNext()) Console.Write(e.Current);  // 123
```
### 4. Use Span<T> for allocation-free access

Target: Use Span<T> for allocation-free access. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```csharp
// Span<T>: allocation-free slice over contiguous memory
Span<int> span = stackalloc int[] { 1, 2, 3, 4 };
var slice = span[1..3];
Console.WriteLine(string.Join(",", slice.ToArray()));  // 2,3
```

## Practice Questions

1. What is the key idea behind "Iterators, IEnumerable, and Span<T>"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Iterators, IEnumerable, and Span<T> with analogies and real-world examples"
1. "Show me common mistakes beginners make with Iterators, IEnumerable, and Span<T>"
1. "Provide advanced patterns and performance considerations for Iterators, IEnumerable, and Span<T>"

## Key Takeaways

- Master the core ideas of Iterators, IEnumerable, and Span<T> through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked Microsoft Learn docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
