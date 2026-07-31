---
{
  "title": "Control Flow and Switch Expressions",
  "description": "if/else, switch statements and expressions, loops, and jump statements.",
  "type": "lesson",
  "order": 4,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Write if/else branching logic",
    "Use switch statements and switch expressions",
    "Use for, foreach, while, and do-while loops",
    "Apply break, continue, and return control keywords"
  ],
  "knowledge_refs": [
    "csharp/cs-04-control-flow"
  ],
  "prerequisites": [
    "CS-03"
  ],
  "references": [
    {
      "title": "Selection Statements",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/selection-statements"
    },
    {
      "title": "Iteration Statements",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/iteration-statements"
    },
    {
      "title": "Jump Statements",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/jump-statements"
    }
  ]
}
---

# CS-04-CONTROL-FLOW: Control Flow and Switch Expressions

## Introduction

if/else, switch statements and expressions, loops, and jump statements. By the end of this lesson you will be able to: Write if/else branching logic; Use switch statements and switch expressions; Use for, foreach, while, and do-while loops; Apply break, continue, and return control keywords.

## Key Concepts

### 1. Write if/else branching logic

Target: Write if/else branching logic. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```csharp
int score = 85;
if (score >= 90) Console.WriteLine("A");
else if (score >= 80) Console.WriteLine("B");
else Console.WriteLine("C");
```
### 2. Use switch statements and switch expressions

Target: Use switch statements and switch expressions. Apply the idiomatic pattern — this is how production C# expresses this idea, so study the shape of the code.

```csharp
int day = 3;
string name = day switch
{
    1 => "Monday",
    2 => "Tuesday",
    _ => "Other"
};
Console.WriteLine(name);
```
### 3. Use for, foreach, while, and do-while loops

Target: Use for, foreach, while, and do-while loops. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```csharp
for (int i = 0; i < 3; i++) Console.Write(i);       // 012
foreach (var c in "abc") Console.Write(c);           // abc
int j = 0;
while (j < 2) { Console.Write(j); j++; }             // 01
do { Console.Write("run"); } while (false);          // runs once
```
### 4. Apply break, continue, and return control keywords

Target: Apply break, continue, and return control keywords. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```csharp
for (int i = 0; i < 10; i++)
{
    if (i == 2) continue;      // skip 2
    if (i == 5) break;         // stop at 5
    Console.Write(i);          // 0134
}
```

## Practice Questions

1. What is the key idea behind "Control Flow and Switch Expressions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Control Flow and Switch Expressions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Control Flow and Switch Expressions"
1. "Provide advanced patterns and performance considerations for Control Flow and Switch Expressions"

## Key Takeaways

- Master the core ideas of Control Flow and Switch Expressions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked Microsoft Learn docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
