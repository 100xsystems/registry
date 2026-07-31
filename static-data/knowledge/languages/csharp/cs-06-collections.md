---
{
  "title": "Arrays, Lists, and Collections",
  "description": "Arrays, List<T>, Dictionary<TKey,TValue>, Queue, Stack; collection initializers.",
  "type": "lesson",
  "order": 6,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Work with single and multi-dimensional arrays",
    "Use List<T> and common collection methods",
    "Use Dictionary<TKey,TValue> for keyed lookup",
    "Use Queue and Stack for ordered processing"
  ],
  "knowledge_refs": [
    "csharp/cs-06-collections"
  ],
  "prerequisites": [
    "CS-05"
  ],
  "references": [
    {
      "title": "Collections Overview",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/collections"
    },
    {
      "title": "Array Guide",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/arrays/"
    },
    {
      "title": "Generic Collections",
      "url": "https://learn.microsoft.com/en-us/dotnet/standard/collections/generic/"
    }
  ]
}
---

# CS-06-COLLECTIONS: Arrays, Lists, and Collections

## Introduction

Arrays, List<T>, Dictionary<TKey,TValue>, Queue, Stack; collection initializers. By the end of this lesson you will be able to: Work with single and multi-dimensional arrays; Use List<T> and common collection methods; Use Dictionary<TKey,TValue> for keyed lookup; Use Queue and Stack for ordered processing.

## Key Concepts

### 1. Work with single and multi-dimensional arrays

Target: Work with single and multi-dimensional arrays. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```csharp
int[] nums = { 5, 3, 1 };
Array.Sort(nums);
Console.WriteLine(string.Join(",", nums));  // 1,3,5
int[,] grid = { { 1, 2 }, { 3, 4 } };
Console.WriteLine(grid[1, 0]);             // 3
```
### 2. Use List<T> and common collection methods

Target: Use List<T> and common collection methods. Apply the idiomatic pattern — this is how production C# expresses this idea, so study the shape of the code.

```csharp
var list = new List<string> { "a" };
list.Add("b");
list.Insert(0, "z");
list.Remove("a");
Console.WriteLine(string.Join(",", list)); // z,b
```
### 3. Use Dictionary<TKey,TValue> for keyed lookup

Target: Use Dictionary<TKey,TValue> for keyed lookup. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```csharp
var dict = new Dictionary<string, int>
{
    ["one"] = 1,
    ["two"] = 2
};
dict["three"] = 3;
Console.WriteLine(dict.ContainsKey("two"));   // True
Console.WriteLine(dict.GetValueOrDefault("x")); // 0
```
### 4. Use Queue and Stack for ordered processing

Target: Use Queue and Stack for ordered processing. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```csharp
var queue = new Queue<int>();
queue.Enqueue(1); queue.Enqueue(2);
Console.WriteLine(queue.Dequeue());   // 1 (FIFO)

var stack = new Stack<int>();
stack.Push(1); stack.Push(2);
Console.WriteLine(stack.Pop());       // 2 (LIFO)
```

## Practice Questions

1. What is the key idea behind "Arrays, Lists, and Collections"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Arrays, Lists, and Collections with analogies and real-world examples"
1. "Show me common mistakes beginners make with Arrays, Lists, and Collections"
1. "Provide advanced patterns and performance considerations for Arrays, Lists, and Collections"

## Key Takeaways

- Master the core ideas of Arrays, Lists, and Collections through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked Microsoft Learn docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
