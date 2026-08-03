---
{
  "title": "Interfaces",
  "description": "Abstract contracts.",
  "type": "lesson",
  "order": 10,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define interfaces",
    "Implement interfaces",
    "Use interface references",
    "Compose behaviors"
  ],
  "knowledge_refs": [
    "d/d-10-interfaces"
  ],
  "prerequisites": [
    "D-09: Classes and OOP"
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

# D-10-INTERFACES: Interfaces

## Introduction

Abstract contracts. By the end of this lesson you will be able to: Define interfaces; Implement interfaces; Use interface references; Compose behaviors.

## Key Concepts

### 1. Define interfaces

Target: Define interfaces. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```d
import std.stdio;

interface Shape {
    double area();
}

class Square : Shape {
    double side;
    override double area() { return side * side; }
}

void main() {
    Shape s = new Square();
    writeln(s.area());
}
```
### 2. Implement interfaces

Target: Implement interfaces. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```d
interface Logger {
    void log(string msg);
}

class ConsoleLogger : Logger {
    override void log(string msg) { writeln(msg); }
}
```
### 3. Use interface references

Target: Use interface references. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```d
interface Drawable { void draw(); }
interface Resizable { void resize(double f); }

class Widget : Drawable, Resizable {
    override void draw() {}
    override void resize(double f) {}
}
```
### 4. Compose behaviors

Target: Compose behaviors. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```d
interface Comparable { int compare(Comparable other); }
```

## Practice Questions

1. What is the key idea behind "Interfaces"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Interfaces with analogies and real-world examples"
1. "Show me common mistakes beginners make with Interfaces"
1. "Provide advanced patterns and performance considerations for Interfaces"

## Key Takeaways

- Master the core ideas of Interfaces through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
