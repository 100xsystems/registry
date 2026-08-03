---
{
  "title": "Types and Variables",
  "description": "Built-in types and declarations.",
  "type": "lesson",
  "order": 2,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use integer types",
    "Use floating point",
    "Declare variables with auto",
    "Use immutable and const"
  ],
  "knowledge_refs": [
    "d/d-02-types"
  ],
  "prerequisites": [
    "D-01: Getting Started with D"
  ],
  "references": [
    {
      "title": "D Language Reference",
      "url": "https://dlang.org/spec/spec.html",
      "description": "Official language spec"
    },
    {
      "title": "D Programming Tour",
      "url": "https://tour.dlang.org/",
      "description": "Interactive language tour"
    },
    {
      "title": "D Wiki",
      "url": "https://wiki.dlang.org/",
      "description": "Community wiki"
    },
    {
      "title": "DUB Package Manager",
      "url": "https://code.dlang.org/",
      "description": "Package registry"
    }
  ]
}
---

# D-02-TYPES: Types and Variables

## Introduction

Built-in types and declarations. By the end of this lesson you will be able to: Use integer types; Use floating point; Declare variables with auto; Use immutable and const.

## Key Concepts

### 1. Use integer types

Target: Use integer types. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```d
import std.stdio;

void main() {
    int i = 10;
    double d = 3.14;
    string s = "D";
    bool b = true;
    writeln(i, " ", d, " ", s, " ", b);
}
```
### 2. Use floating point

Target: Use floating point. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```d
auto x = 42;       // int
auto y = 3.14;     // double
writeln(typeof(x), " ", typeof(y));
```
### 3. Declare variables with auto

Target: Declare variables with auto. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```d
immutable int MAX = 100;
const int MIN = 0;
```
### 4. Use immutable and const

Target: Use immutable and const. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```d
ulong big = 1_000_000_000_000;   // underscores for readability
```

## Practice Questions

1. What is the key idea behind "Types and Variables"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Types and Variables with analogies and real-world examples"
1. "Show me common mistakes beginners make with Types and Variables"
1. "Provide advanced patterns and performance considerations for Types and Variables"

## Key Takeaways

- Master the core ideas of Types and Variables through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
