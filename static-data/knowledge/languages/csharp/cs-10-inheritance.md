---
{
  "title": "Inheritance and Polymorphism",
  "description": "Base and derived classes, virtual/override, protected members, sealed.",
  "type": "lesson",
  "order": 10,
  "duration": "75 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create base and derived classes",
    "Override virtual methods with override",
    "Access base members through protected and base",
    "Use sealed to prevent inheritance"
  ],
  "knowledge_refs": [
    "csharp/cs-10-inheritance"
  ],
  "prerequisites": [
    "CS-09"
  ],
  "references": [
    {
      "title": "Inheritance in C#",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/object-oriented/inheritance"
    },
    {
      "title": "Polymorphism",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/object-oriented/polymorphism"
    },
    {
      "title": "virtual Keyword",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/virtual"
    }
  ]
}
---

# CS-10-INHERITANCE: Inheritance and Polymorphism

## Introduction

Base and derived classes, virtual/override, protected members, sealed. By the end of this lesson you will be able to: Create base and derived classes; Override virtual methods with override; Access base members through protected and base; Use sealed to prevent inheritance.

## Key Concepts

### 1. Create base and derived classes

Target: Create base and derived classes. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```csharp
class Animal { public virtual string Speak() => "..."; }
class Dog : Animal { public override string Speak() => "Woof"; }
Console.WriteLine(new Dog().Speak());  // Woof
```
### 2. Override virtual methods with override

Target: Override virtual methods with override. Apply the idiomatic pattern — this is how production C# expresses this idea, so study the shape of the code.

```csharp
class Animal { public virtual string Speak() => "..."; }
class Dog : Animal { public override string Speak() => "Woof"; }
class Cat : Animal { public override string Speak() => "Meow"; }

Animal[] animals = { new Dog(), new Cat() };
foreach (var a in animals) Console.WriteLine(a.Speak());
```
### 3. Access base members through protected and base

Target: Access base members through protected and base. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```csharp
class Base { protected int _x; public Base(int x) => _x = x; }
class Derived : Base
{
    public Derived(int x) : base(x) { }
    public void Show() => Console.WriteLine(_x);
}
new Derived(7).Show();  // 7 (protected member)
```
### 4. Use sealed to prevent inheritance

Target: Use sealed to prevent inheritance. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```csharp
class SealedOne { public void Do() { } }
// sealed class: cannot be inherited
class Final : SealedOne { }
Console.WriteLine(typeof(Final).Name);
```

## Practice Questions

1. What is the key idea behind "Inheritance and Polymorphism"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Inheritance and Polymorphism with analogies and real-world examples"
1. "Show me common mistakes beginners make with Inheritance and Polymorphism"
1. "Provide advanced patterns and performance considerations for Inheritance and Polymorphism"

## Key Takeaways

- Master the core ideas of Inheritance and Polymorphism through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked Microsoft Learn docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
