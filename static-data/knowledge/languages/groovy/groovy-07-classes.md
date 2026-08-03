---
{
  "title": "Classes and Traits",
  "description": "OOP in Groovy.",
  "type": "lesson",
  "order": 7,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define classes",
    "Use properties",
    "Write constructors",
    "Use traits"
  ],
  "knowledge_refs": [
    "groovy/groovy-07-classes"
  ],
  "prerequisites": [
    "Groovy-06: String Handling"
  ],
  "references": [
    {
      "title": "Groovy Documentation",
      "url": "https://groovy-lang.org/documentation.html",
      "description": "Official docs"
    },
    {
      "title": "Groovy Tutorial (Groovy-lang)",
      "url": "https://groovy-lang.org/single-page-documentation.html",
      "description": "Official reference"
    },
    {
      "title": "Groovy in Action",
      "url": "https://www.manning.com/books/groovy-in-action-second-edition",
      "description": "Book"
    }
  ]
}
---

# GROOVY-07-CLASSES: Classes and Traits

## Introduction

OOP in Groovy. By the end of this lesson you will be able to: Define classes; Use properties; Write constructors; Use traits.

## Key Concepts

### 1. Define classes

Target: Define classes. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```groovy
class Person {
  String name
  int age
}

def p = new Person(name: "Ada", age: 36)
println p.name
```
### 2. Use properties

Target: Use properties. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```groovy
class Counter {
  int count = 0
  void increment() { count++ }
}
```
### 3. Write constructors

Target: Write constructors. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```groovy
class Point {
  int x, y
  Point(int x, int y) { this.x = x; this.y = y }
}
```
### 4. Use traits

Target: Use traits. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```groovy
trait Greeter {
  String greeting() { "hello" }
}

class Person implements Greeter {}
```

## Practice Questions

1. What is the key idea behind "Classes and Traits"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Classes and Traits with analogies and real-world examples"
1. "Show me common mistakes beginners make with Classes and Traits"
1. "Provide advanced patterns and performance considerations for Classes and Traits"

## Key Takeaways

- Master the core ideas of Classes and Traits through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
