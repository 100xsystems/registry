---
{
  "title": "Async Programming: async/await and Tasks",
  "description": "Task-based async model, await semantics, parallel tasks, error handling.",
  "type": "lesson",
  "order": 16,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Understand the Task Asynchronous Programming model",
    "Write async methods with async/await",
    "Run tasks in parallel with Task.WhenAll",
    "Handle errors in async code"
  ],
  "knowledge_refs": [
    "csharp/cs-16-async"
  ],
  "prerequisites": [
    "CS-15"
  ],
  "references": [
    {
      "title": "Task-based Asynchronous Programming",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/task-asynchronous-programming-model"
    },
    {
      "title": "Async Scenarios",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/async-scenarios"
    },
    {
      "title": "Async File Access",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/using-async-for-file-access"
    }
  ]
}
---

# CS-16-ASYNC: Async Programming: async/await and Tasks

## Introduction

Task-based async model, await semantics, parallel tasks, error handling. By the end of this lesson you will be able to: Understand the Task Asynchronous Programming model; Write async methods with async/await; Run tasks in parallel with Task.WhenAll; Handle errors in async code.

## Key Concepts

### 1. Understand the Task Asynchronous Programming model

Target: Understand the Task Asynchronous Programming model. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```csharp
async Task<string> FetchAsync(HttpClient client, string url)
{
    return await client.GetStringAsync(url);
}
using var http = new HttpClient();
string html = await FetchAsync(http, "https://example.com");
Console.WriteLine($"Fetched {html.Length} chars");
```
### 2. Write async methods with async/await

Target: Write async methods with async/await. Apply the idiomatic pattern — this is how production C# expresses this idea, so study the shape of the code.

```csharp
static async Task<int> DelayCountAsync()
{
    await Task.Delay(100);
    return 42;
}
int result = await DelayCountAsync();
Console.WriteLine(result);  // 42 (non-blocking await)
```
### 3. Run tasks in parallel with Task.WhenAll

Target: Run tasks in parallel with Task.WhenAll. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```csharp
// Parallel: run independent tasks concurrently
Task<int> t1 = Task.Run(() => { Task.Delay(50).Wait(); return 1; });
Task<int> t2 = Task.Run(() => { Task.Delay(50).Wait(); return 2; });
int[] results = await Task.WhenAll(t1, t2);
Console.WriteLine(results.Sum());  // 3
```
### 4. Handle errors in async code

Target: Handle errors in async code. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```csharp
try
{
    await Task.Run(() => throw new InvalidOperationException("boom"));
}
catch (InvalidOperationException ex)
{
    Console.WriteLine($"Caught: {ex.Message}");  // async error propagation
}
```

## Practice Questions

1. What is the key idea behind "Async Programming: async/await and Tasks"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Async Programming: async/await and Tasks with analogies and real-world examples"
1. "Show me common mistakes beginners make with Async Programming: async/await and Tasks"
1. "Provide advanced patterns and performance considerations for Async Programming: async/await and Tasks"

## Key Takeaways

- Master the core ideas of Async Programming: async/await and Tasks through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked Microsoft Learn docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
