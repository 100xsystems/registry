---
{
  "title": "Methods and Parameters",
  "description": "Method signatures, ref/out/in params, params arrays, named and optional arguments.",
  "type": "lesson",
  "order": 5,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Declare methods with return types and parameters",
    "Use ref, out, and in parameter modifiers",
    "Use params arrays for variable argument counts",
    "Use named and optional arguments"
  ],
  "knowledge_refs": [
    "csharp/cs-05-methods"
  ],
  "prerequisites": [
    "CS-04"
  ],
  "references": [
    {
      "title": "C# Methods Guide",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/methods"
    },
    {
      "title": "Method Parameters",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/method-parameters"
    },
    {
      "title": "ref Keyword",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/ref"
    }
  ]
}
---

# CS-05-METHODS: Methods and Parameters

## Introduction

Method signatures, ref/out/in params, params arrays, named and optional arguments. By the end of this lesson you will be able to: Declare methods with return types and parameters; Use ref, out, and in parameter modifiers; Use params arrays for variable argument counts; Use named and optional arguments.

## Key Concepts

### 1. Declare methods with return types and parameters

Target: Declare methods with return types and parameters. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```csharp
static int Add(int a, int b) => a + b;
static void Greet(string name) => Console.WriteLine($"Hi {name}");
Console.WriteLine(Add(2, 3));
Greet("Alice");
```
### 2. Use ref, out, and in parameter modifiers

Target: Use ref, out, and in parameter modifiers. Apply the idiomatic pattern — this is how production C# expresses this idea, so study the shape of the code.

```csharp
static void Swap(ref int x, ref int y)
{
    (x, y) = (y, x);
}
int a = 1, b = 2;
Swap(ref a, ref b);
Console.WriteLine($"{a} {b}");  // 2 1
```
### 3. Use params arrays for variable argument counts

Target: Use params arrays for variable argument counts. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```csharp
static bool TryParseNum(string s, out int result)
{
    return int.TryParse(s, out result);
}
if (TryParseNum("42", out int n)) Console.WriteLine(n);
```
### 4. Use named and optional arguments

Target: Use named and optional arguments. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```csharp
static int Sum(params int[] nums) => nums.Sum();
static string Label(string name = "guest") => name;
Console.WriteLine(Sum(1, 2, 3, 4));     // 10
Console.WriteLine(Label());              // guest
Console.WriteLine(Label(name: "Bob"));  // named arg
```

## Practice Questions

1. What is the key idea behind "Methods and Parameters"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Methods and Parameters with analogies and real-world examples"
1. "Show me common mistakes beginners make with Methods and Parameters"
1. "Provide advanced patterns and performance considerations for Methods and Parameters"

## Key Takeaways

- Master the core ideas of Methods and Parameters through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked Microsoft Learn docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
