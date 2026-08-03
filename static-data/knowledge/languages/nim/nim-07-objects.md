---
{
  "title": "Objects and References",
  "description": "Define and use object types.",
  "type": "lesson",
  "order": 7,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define object types",
    "Create object instances",
    "Access fields",
    "Use default field values"
  ],
  "knowledge_refs": [
    "nim/nim-07-objects"
  ],
  "prerequisites": [
    "Nim-06: Procedures"
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

# NIM-07-OBJECTS: Objects and References

## Introduction

Define and use object types. By the end of this lesson you will be able to: Define object types; Create object instances; Access fields; Use default field values.

## Key Concepts

### 1. Define object types

Target: Define object types. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```nim
type
  Person = object
    name: string
    age: int

let p = Person(name: "Ada", age: 36)
echo p.name
```
### 2. Create object instances

Target: Create object instances. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```nim
type
  Point = object
    x, y: float

let origin = Point(x: 0.0, y: 0.0)
```
### 3. Access fields

Target: Access fields. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```nim
var p: Person
p.name = "Grace"
p.age = 85
```
### 4. Use default field values

Target: Use default field values. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```nim
type
  Account = object
    balance: float = 0.0
```

## Practice Questions

1. What is the key idea behind "Objects and References"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Objects and References with analogies and real-world examples"
1. "Show me common mistakes beginners make with Objects and References"
1. "Provide advanced patterns and performance considerations for Objects and References"

## Key Takeaways

- Master the core ideas of Objects and References through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
