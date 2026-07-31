---
{
  "title": "Delegates, Events, and Lambdas",
  "description": "Delegate types, multicast delegates, events, lambda expressions, Func/Action.",
  "type": "lesson",
  "order": 14,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Declare and use delegate types",
    "Understand multicast delegates",
    "Implement publisher-subscriber with events",
    "Write lambda expressions with Func/Action"
  ],
  "knowledge_refs": [
    "csharp/cs-14-delegates-events"
  ],
  "prerequisites": [
    "CS-13"
  ],
  "references": [
    {
      "title": "Delegates and Lambdas",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/types/delegates-lambdas"
    },
    {
      "title": "Events Guide",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/events-overview"
    },
    {
      "title": "Lambda Expressions",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/lambda-expressions"
    }
  ]
}
---

# CS-14-DELEGATES-EVENTS: Delegates, Events, and Lambdas

## Introduction

Delegate types, multicast delegates, events, lambda expressions, Func/Action. By the end of this lesson you will be able to: Declare and use delegate types; Understand multicast delegates; Implement publisher-subscriber with events; Write lambda expressions with Func/Action.

## Key Concepts

### 1. Declare and use delegate types

Target: Declare and use delegate types. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```csharp
delegate int MathOp(int a, int b);
MathOp add = (a, b) => a + b;
Console.WriteLine(add(5, 3));  // 8
```
### 2. Understand multicast delegates

Target: Understand multicast delegates. Apply the idiomatic pattern — this is how production C# expresses this idea, so study the shape of the code.

```csharp
// Multicast: += chains invocations
Action<string> log = m => Console.WriteLine($"[A] {m}");
log += m => Console.WriteLine($"[B] {m}");
log("hello");
// [A] hello
// [B] hello
```
### 3. Implement publisher-subscriber with events

Target: Implement publisher-subscriber with events. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```csharp
class Button
{
    public event EventHandler? Clicked;
    public void Press() => Clicked?.Invoke(this, EventArgs.Empty);
}
var btn = new Button();
btn.Clicked += (s, e) => Console.WriteLine("Clicked!");
btn.Press();   // Clicked!
```
### 4. Write lambda expressions with Func/Action

Target: Write lambda expressions with Func/Action. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```csharp
Func<int, int> square = x => x * x;
Func<int, int, int> add = (a, b) => a + b;
var nums = new[] { 1, 2, 3 };
Console.WriteLine(nums.Select(square).Sum()); // 14
Console.WriteLine(add(2, 3));                 // 5
```

## Practice Questions

1. What is the key idea behind "Delegates, Events, and Lambdas"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Delegates, Events, and Lambdas with analogies and real-world examples"
1. "Show me common mistakes beginners make with Delegates, Events, and Lambdas"
1. "Provide advanced patterns and performance considerations for Delegates, Events, and Lambdas"

## Key Takeaways

- Master the core ideas of Delegates, Events, and Lambdas through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked Microsoft Learn docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
