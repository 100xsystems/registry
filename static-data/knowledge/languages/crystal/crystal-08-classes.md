---
{
  "title": "Classes",
  "description": "OOP with classes and accessors.",
  "type": "lesson",
  "order": 8,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define classes",
    "Add getters/setters",
    "Use initialize",
    "Write instance methods"
  ],
  "knowledge_refs": [
    "crystal/crystal-08-classes"
  ],
  "prerequisites": [
    "Crystal-07: Methods"
  ],
  "references": [
    {
      "title": "Crystal Language Reference",
      "url": "https://crystal-lang.org/reference/",
      "description": "Official docs"
    },
    {
      "title": "Crystal for Rubyists",
      "url": "https://crystal-lang.org/reference/guides/faq.html",
      "description": "Migration guide"
    },
    {
      "title": "Crystal Book",
      "url": "https://crystal-lang.org/reference/",
      "description": "Official reference book"
    },
    {
      "title": "Crystal Forum",
      "url": "https://forum.crystal-lang.org/",
      "description": "Community"
    }
  ]
}
---

# CRYSTAL-08-CLASSES: Classes

## Introduction

OOP with classes and accessors. By the end of this lesson you will be able to: Define classes; Add getters/setters; Use initialize; Write instance methods.

## Key Concepts

### 1. Define classes

Target: Define classes. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```crystal
class Person
  getter name : String
  getter age : Int32

  def initialize(@name, @age)
  end

  def greet
    "Hi, I am #{@name}"
  end
end

p = Person.new("Ada", 36)
puts p.greet
```
### 2. Add getters/setters

Target: Add getters/setters. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```crystal
class Counter
  property count = 0

  def increment!
    @count += 1
  end
end
```
### 3. Use initialize

Target: Use initialize. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```crystal
class Point
  def initialize(@x : Int32, @y : Int32)
  end

  def +(other : Point)
    Point.new(@x + other.x, @y + other.y)
  end
end
```
### 4. Write instance methods

Target: Write instance methods. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```crystal
class Config
  @@instances = 0

  def self.count
    @@instances
  end
end
```

## Practice Questions

1. What is the key idea behind "Classes"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Classes with analogies and real-world examples"
1. "Show me common mistakes beginners make with Classes"
1. "Provide advanced patterns and performance considerations for Classes"

## Key Takeaways

- Master the core ideas of Classes through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
