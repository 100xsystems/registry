---
{
  "title": "Generics",
  "description": "Type-parameterized code.",
  "type": "lesson",
  "order": 9,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write generic procs",
    "Use generic types",
    "Constrain type params",
    "Build generic collections"
  ],
  "knowledge_refs": [
    "nim/nim-09-generics"
  ],
  "prerequisites": [
    "Nim-08: Enums and Case Objects"
  ],
  "references": [
    {
      "title": "Nim Manual",
      "url": "https://nim-lang.org/docs/manual.html",
      "description": "Official language manual"
    },
    {
      "title": "Nim by Example",
      "url": "https://nim-by-example.github.io/",
      "description": "Practical Nim examples"
    },
    {
      "title": "Nim Tutorial",
      "url": "https://nim-lang.org/docs/tut1.html",
      "description": "Official tutorial"
    },
    {
      "title": "Nim Forum",
      "url": "https://forum.nim-lang.org/",
      "description": "Community discussions"
    }
  ]
}
---

# NIM-09-GENERICS: Generics

## Introduction

Type-parameterized code. By the end of this lesson you will be able to: Write generic procs; Use generic types; Constrain type params; Build generic collections.

## Key Concepts

### 1. Write generic procs

Target: Write generic procs. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```nim
proc identity[T](x: T): T = x

echo identity(42)
echo identity("hi")
```
### 2. Use generic types

Target: Use generic types. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```nim
proc first[T](s: seq[T]): T = s[0]
```
### 3. Constrain type params

Target: Constrain type params. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```nim
proc max[T](a, b: T): T =
  if a > b: a else: b
```
### 4. Build generic collections

Target: Build generic collections. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```nim
type
  Stack[T] = object
    items: seq[T]
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
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
