---
{
  "title": "Structs",
  "description": "Value types and methods.",
  "type": "lesson",
  "order": 8,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define structs",
    "Add methods",
    "Use constructors",
    "Define operators"
  ],
  "knowledge_refs": [
    "d/d-08-structs"
  ],
  "prerequisites": [
    "D-07: Functions"
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

# D-08-STRUCTS: Structs

## Introduction

Value types and methods. By the end of this lesson you will be able to: Define structs; Add methods; Use constructors; Define operators.

## Key Concepts

### 1. Define structs

Target: Define structs. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```d
import std.stdio;

struct Point {
    int x, y;

    this(int x, int y) {
        this.x = x;
        this.y = y;
    }

    int magnitude() {
        return x * x + y * y;
    }
}

void main() {
    auto p = Point(3, 4);
    writeln(p.magnitude());
}
```
### 2. Add methods

Target: Add methods. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```d
struct Counter {
    int count;

    void increment() {
        count++;
    }
}
```
### 3. Use constructors

Target: Use constructors. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```d
struct Vec2 {
    float x, y;

    Vec2 opBinary(string op)(Vec2 other) if (op == "+") {
        return Vec2(x + other.x, y + other.y);
    }
}
```
### 4. Define operators

Target: Define operators. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```d
struct Temperature {
    double celsius;
    double fahrenheit() const {
        return celsius * 9 / 5 + 32;
    }
}
```

## Practice Questions

1. What is the key idea behind "Structs"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Structs with analogies and real-world examples"
1. "Show me common mistakes beginners make with Structs"
1. "Provide advanced patterns and performance considerations for Structs"

## Key Takeaways

- Master the core ideas of Structs through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
