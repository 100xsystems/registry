---
{
  "title": "Advanced: Reflection, Attributes, and Memory",
  "description": "Reflection, custom attributes, unsafe code, garbage collection, performance.",
  "type": "lesson",
  "order": 21,
  "duration": "75 min",
  "difficulty": "expert",
  "learning_objectives": [
    "Inspect types at runtime with reflection",
    "Define and apply custom attributes",
    "Write unsafe code with pointers",
    "Understand GC and deterministic disposal"
  ],
  "knowledge_refs": [
    "csharp/cs-21-advanced"
  ],
  "prerequisites": [
    "CS-20"
  ],
  "references": [
    {
      "title": "Reflection and Attributes",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/advanced-topics/reflection-and-attributes/"
    },
    {
      "title": "Garbage Collection",
      "url": "https://learn.microsoft.com/en-us/dotnet/standard/garbage-collection/"
    },
    {
      "title": "Unsafe Code Guide",
      "url": "https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/unsafe-code"
    }
  ]
}
---

# CS-21-ADVANCED: Advanced: Reflection, Attributes, and Memory

## Introduction

Reflection, custom attributes, unsafe code, garbage collection, performance. By the end of this lesson you will be able to: Inspect types at runtime with reflection; Define and apply custom attributes; Write unsafe code with pointers; Understand GC and deterministic disposal.

## Key Concepts

### 1. Inspect types at runtime with reflection

Target: Inspect types at runtime with reflection. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```csharp
var type = typeof(string);
Console.WriteLine(type.Name);       // String
Console.WriteLine(type.IsSealed);   // True
foreach (var m in type.GetMethods().Take(5))
    Console.WriteLine(m.Name);
```
### 2. Define and apply custom attributes

Target: Define and apply custom attributes. Apply the idiomatic pattern — this is how production C# expresses this idea, so study the shape of the code.

```csharp
[AttributeUsage(AttributeTargets.Class)]
class DeprecatedAttribute : Attribute
{
    public string Reason { get; }
    public DeprecatedAttribute(string reason) => Reason = reason;
}

[Deprecated("use NewApi instead")]
class OldApi { }
var attr = typeof(OldApi).GetCustomAttributes(typeof(DeprecatedAttribute), false)[0]
    as DeprecatedAttribute;
Console.WriteLine(attr?.Reason);
```
### 3. Write unsafe code with pointers

Target: Write unsafe code with pointers. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```csharp
unsafe
{
    int value = 42;
    int* p = &value;          // pointer to value
    Console.WriteLine(*p);    // 42
}
// compile with: dotnet build /unsafe or <AllowUnsafeBlocks>true</AllowUnsafeBlocks>
```
### 4. Understand GC and deterministic disposal

Target: Understand GC and deterministic disposal. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```csharp
// GC: managed heap, generations, finalizers
var obj = new object();
var weak = new WeakReference(obj);
obj = null;
GC.Collect();
Console.WriteLine(weak.IsAlive);  // usually False after collection

// deterministic disposal
using var resource = new MemoryStream();
Console.WriteLine(resource.Length);
```

## Practice Questions

1. What is the key idea behind "Advanced: Reflection, Attributes, and Memory"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Advanced: Reflection, Attributes, and Memory with analogies and real-world examples"
1. "Show me common mistakes beginners make with Advanced: Reflection, Attributes, and Memory"
1. "Provide advanced patterns and performance considerations for Advanced: Reflection, Attributes, and Memory"

## Key Takeaways

- Master the core ideas of Advanced: Reflection, Attributes, and Memory through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked Microsoft Learn docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
