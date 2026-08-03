---
{
  "title": "UFCS and Function Composition",
  "description": "Unified function call syntax.",
  "type": "lesson",
  "order": 16,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use UFCS chains",
    "Compose functions",
    "Build readable pipelines",
    "Extend built-in types"
  ],
  "knowledge_refs": [
    "d/d-16-ufcs"
  ],
  "prerequisites": [
    "D-15: File and Stream IO"
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

# D-16-UFCS: UFCS and Function Composition

## Introduction

Unified function call syntax. By the end of this lesson you will be able to: Use UFCS chains; Compose functions; Build readable pipelines; Extend built-in types.

## Key Concepts

### 1. Use UFCS chains

Target: Use UFCS chains. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```d
import std.stdio;
import std.algorithm;

void main() {
    "hello".toUpper().writeln;
}
```
### 2. Compose functions

Target: Compose functions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```d
auto result = [1, 2, 3, 4]
    .map!(n => n * 2)
    .filter!(n => n > 3)
    .array;
writeln(result);
```
### 3. Build readable pipelines

Target: Build readable pipelines. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```d
string shout(string s) { return s.toUpper() ~ "!"; }
writeln("hi".shout);
```
### 4. Extend built-in types

Target: Extend built-in types. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```d
auto words = "a b c".split;
writeln(words.length);
```

## Practice Questions

1. What is the key idea behind "UFCS and Function Composition"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain UFCS and Function Composition with analogies and real-world examples"
1. "Show me common mistakes beginners make with UFCS and Function Composition"
1. "Provide advanced patterns and performance considerations for UFCS and Function Composition"

## Key Takeaways

- Master the core ideas of UFCS and Function Composition through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
