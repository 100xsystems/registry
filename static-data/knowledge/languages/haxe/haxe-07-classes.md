---
{
  "title": "Classes and OOP",
  "description": "Classes, inheritance, and interfaces.",
  "type": "lesson",
  "order": 7,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define classes",
    "Use inheritance",
    "Implement interfaces",
    "Use abstract classes"
  ],
  "knowledge_refs": [
    "haxe/haxe-07-classes"
  ],
  "prerequisites": [
    "Haxe-06: Strings"
  ],
  "references": [
    {
      "title": "Haxe Documentation",
      "url": "https://haxe.org/documentation/",
      "description": "Official docs"
    },
    {
      "title": "Haxe Manual",
      "url": "https://haxe.org/manual/introduction.html",
      "description": "The language manual"
    },
    {
      "title": "Haxe Cookbook",
      "url": "https://code.haxe.org/",
      "description": "Community recipes"
    }
  ]
}
---

# HAXE-07-CLASSES: Classes and OOP

## Introduction

Classes, inheritance, and interfaces. By the end of this lesson you will be able to: Define classes; Use inheritance; Implement interfaces; Use abstract classes.

## Key Concepts

### 1. Define classes

Target: Define classes. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```haxe
class Person {
  public var name:String;
  public var age:Int;

  public function new(name:String, age:Int) {
    this.name = name;
    this.age = age;
  }
}
```
### 2. Use inheritance

Target: Use inheritance. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```haxe
class Dog extends Animal {
  override public function speak() { trace("Woof"); }
}
```
### 3. Implement interfaces

Target: Implement interfaces. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```haxe
interface Shape {
  public function area():Float;
}
```
### 4. Use abstract classes

Target: Use abstract classes. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```haxe
class Square implements Shape {
  public function area():Float return side * side;
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
