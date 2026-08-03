---
{
  "title": "Classes and OOP",
  "description": "Reference types with inheritance.",
  "type": "lesson",
  "order": 9,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define classes",
    "Use inheritance",
    "Override methods",
    "Use abstract classes"
  ],
  "knowledge_refs": [
    "d/d-09-classes"
  ],
  "prerequisites": [
    "D-08: Structs"
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

# D-09-CLASSES: Classes and OOP

## Introduction

Reference types with inheritance. By the end of this lesson you will be able to: Define classes; Use inheritance; Override methods; Use abstract classes.

## Key Concepts

### 1. Define classes

Target: Define classes. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```d
import std.stdio;

class Animal {
    string name;
    this(string name) { this.name = name; }
    void speak() { writeln("..."); }
}

class Dog : Animal {
    this(string name) { super(name); }
    override void speak() { writeln("Woof"); }
}

void main() {
    auto d = new Dog("Rex");
    d.speak();
}
```
### 2. Use inheritance

Target: Use inheritance. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```d
class Shape {
    abstract double area();
}

class Circle : Shape {
    double radius;
    override double area() { return 3.14159 * radius * radius; }
}
```
### 3. Override methods

Target: Override methods. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```d
class Point {
    private int x, y;

    int getX() const { return x; }
    void setX(int v) { x = v; }
}
```
### 4. Use abstract classes

Target: Use abstract classes. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```d
class Singleton {
    private static Singleton instance;
    static Singleton getInstance() {
        if (instance is null) instance = new Singleton();
        return instance;
    }
}
```

## Practice Questions

1. What is the key idea behind "Classes and OOP"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Classes and OOP with analogies and real-world examples"
1. "Show me common mistakes beginners make with Classes and OOP"
1. "Provide advanced patterns and performance considerations for Classes and OOP"

## Key Takeaways

- Master the core ideas of Classes and OOP through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
