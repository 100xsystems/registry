---
{
  "title": "Templates and Generics",
  "description": "Compile-time code reuse.",
  "type": "lesson",
  "order": 13,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Write template functions",
    "Use template structs",
    "Constrain with is",
    "Use CTFE"
  ],
  "knowledge_refs": [
    "d/d-13-generics"
  ],
  "prerequisites": [
    "D-12: Ranges and Algorithms"
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

# D-13-GENERICS: Templates and Generics

## Introduction

Compile-time code reuse. By the end of this lesson you will be able to: Write template functions; Use template structs; Constrain with is; Use CTFE.

## Key Concepts

### 1. Write template functions

Target: Write template functions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```d
import std.stdio;

T identity(T)(T value) {
    return value;
}

void main() {
    writeln(identity(42));
    writeln(identity("hi"));
}
```
### 2. Use template structs

Target: Use template structs. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```d
struct Box(T) {
    T value;
}

auto b = Box!int(42);
writeln(b.value);
```
### 3. Constrain with is

Target: Constrain with is. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```d
T maxOf(T)(T a, T b) if (is(typeof(a > b))) {
    return a > b ? a : b;
}
```
### 4. Use CTFE

Target: Use CTFE. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```d
enum square(int n) { return n * n; }   // compile-time
writeln(square(5));
```

## Practice Questions

1. What is the key idea behind "Templates and Generics"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Templates and Generics with analogies and real-world examples"
1. "Show me common mistakes beginners make with Templates and Generics"
1. "Provide advanced patterns and performance considerations for Templates and Generics"

## Key Takeaways

- Master the core ideas of Templates and Generics through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
