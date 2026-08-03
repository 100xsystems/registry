---
{
  "title": "Getting Started with D",
  "description": "Install DMD/LDC, compile, and run.",
  "type": "lesson",
  "order": 1,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Install a D compiler",
    "Compile with dmd",
    "Write hello world",
    "Use rdmd for scripts"
  ],
  "knowledge_refs": [
    "d/d-01-getting-started"
  ],
  "prerequisites": [
    "None — this is the entry point"
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

# D-01-GETTING-STARTED: Getting Started with D

## Introduction

Install DMD/LDC, compile, and run. By the end of this lesson you will be able to: Install a D compiler; Compile with dmd; Write hello world; Use rdmd for scripts.

## Key Concepts

### 1. Install a D compiler

Target: Install a D compiler. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```d
import std.stdio;

void main() {
    writeln("Hello, World!");
}
```
### 2. Compile with dmd

Target: Compile with dmd. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```d
dmd hello.d -of=hello
./hello
```
### 3. Write hello world

Target: Write hello world. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```d
import std.stdio;

void main(string[] args) {
    foreach (arg; args) {
        writeln(arg);
    }
}
```
### 4. Use rdmd for scripts

Target: Use rdmd for scripts. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```d
import std.stdio;

void main() {
    write("no newline");
    writeln(" with newline");
}
```

## Practice Questions

1. What is the key idea behind "Getting Started with D"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with D with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with D"
1. "Provide advanced patterns and performance considerations for Getting Started with D"

## Key Takeaways

- Master the core ideas of Getting Started with D through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
