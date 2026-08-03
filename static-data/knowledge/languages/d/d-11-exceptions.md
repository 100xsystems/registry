---
{
  "title": "Exceptions",
  "description": "Try, catch, and custom errors.",
  "type": "lesson",
  "order": 11,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Throw exceptions",
    "Catch exceptions",
    "Use finally",
    "Define custom exceptions"
  ],
  "knowledge_refs": [
    "d/d-11-exceptions"
  ],
  "prerequisites": [
    "D-10: Interfaces"
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

# D-11-EXCEPTIONS: Exceptions

## Introduction

Try, catch, and custom errors. By the end of this lesson you will be able to: Throw exceptions; Catch exceptions; Use finally; Define custom exceptions.

## Key Concepts

### 1. Throw exceptions

Target: Throw exceptions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```d
import std.stdio;

void main() {
    try {
        throw new Exception("boom");
    } catch (Exception e) {
        writeln(e.msg);
    }
}
```
### 2. Catch exceptions

Target: Catch exceptions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```d
try {
    risky();
} catch (FileException e) {
    writeln("file error");
} catch (Exception e) {
    writeln("other");
}
```
### 3. Use finally

Target: Use finally. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```d
class MyError : Exception {
    this(string msg) { super(msg); }
}

throw new MyError("custom failure");
```
### 4. Define custom exceptions

Target: Define custom exceptions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```d
try {
    work();
} finally {
    cleanup();
}
```

## Practice Questions

1. What is the key idea behind "Exceptions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Exceptions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Exceptions"
1. "Provide advanced patterns and performance considerations for Exceptions"

## Key Takeaways

- Master the core ideas of Exceptions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
