---
{
  "title": "Variables and Types",
  "description": "var, let, const, and built-in types.",
  "type": "lesson",
  "order": 2,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use var, let, and const",
    "Work with integer types",
    "Use floats and strings",
    "Understand type inference"
  ],
  "knowledge_refs": [
    "nim/nim-02-variables"
  ],
  "prerequisites": [
    "Nim-01: Getting Started with Nim"
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

# NIM-02-VARIABLES: Variables and Types

## Introduction

var, let, const, and built-in types. By the end of this lesson you will be able to: Use var, let, and const; Work with integer types; Use floats and strings; Understand type inference.

## Key Concepts

### 1. Use var, let, and const

Target: Use var, let, and const. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```nim
var x = 10
let y = 20        # immutable
const z = 30      # compile-time

echo x, " ", y, " ", z
```
### 2. Work with integer types

Target: Work with integer types. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```nim
var count: int = 0
count += 1
```
### 3. Use floats and strings

Target: Use floats and strings. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```nim
let pi = 3.14159
let name = "Nim"
```
### 4. Understand type inference

Target: Understand type inference. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```nim
var a = 5
var b = 2
echo a div b, " ", a mod b
```

## Practice Questions

1. What is the key idea behind "Variables and Types"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Variables and Types with analogies and real-world examples"
1. "Show me common mistakes beginners make with Variables and Types"
1. "Provide advanced patterns and performance considerations for Variables and Types"

## Key Takeaways

- Master the core ideas of Variables and Types through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
