---
{
  "title": "Enums and Case Objects",
  "description": "Enumerations and variant objects.",
  "type": "lesson",
  "order": 8,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define enums",
    "Use case with enums",
    "Use case objects",
    "Convert enums to strings"
  ],
  "knowledge_refs": [
    "nim/nim-08-enums"
  ],
  "prerequisites": [
    "Nim-07: Objects and References"
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

# NIM-08-ENUMS: Enums and Case Objects

## Introduction

Enumerations and variant objects. By the end of this lesson you will be able to: Define enums; Use case with enums; Use case objects; Convert enums to strings.

## Key Concepts

### 1. Define enums

Target: Define enums. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```nim
type
  Color = enum
    Red, Green, Blue

let c = Green
echo c
```
### 2. Use case with enums

Target: Use case with enums. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```nim
type
  ShapeKind = enum
    Circle, Square
  Shape = object
    case kind: ShapeKind
    of Circle:
      radius: float
    of Square:
      side: float
```
### 3. Use case objects

Target: Use case objects. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```nim
case c
of Red: echo "red"
of Green: echo "green"
of Blue: echo "blue"
```
### 4. Convert enums to strings

Target: Convert enums to strings. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```nim
echo ord(Green), " ", $Green
```

## Practice Questions

1. What is the key idea behind "Enums and Case Objects"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Enums and Case Objects with analogies and real-world examples"
1. "Show me common mistakes beginners make with Enums and Case Objects"
1. "Provide advanced patterns and performance considerations for Enums and Case Objects"

## Key Takeaways

- Master the core ideas of Enums and Case Objects through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
