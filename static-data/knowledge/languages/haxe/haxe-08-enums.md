---
{
  "title": "Enums (ADTs)",
  "description": "Algebraic data types.",
  "type": "lesson",
  "order": 8,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define enums",
    "Carry data in variants",
    "Pattern match enums",
    "Use enum constructors"
  ],
  "knowledge_refs": [
    "haxe/haxe-08-enums"
  ],
  "prerequisites": [
    "Haxe-07: Classes and OOP"
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

# HAXE-08-ENUMS: Enums (ADTs)

## Introduction

Algebraic data types. By the end of this lesson you will be able to: Define enums; Carry data in variants; Pattern match enums; Use enum constructors.

## Key Concepts

### 1. Define enums

Target: Define enums. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```haxe
enum Color { Red; Green; Blue; }
```
### 2. Carry data in variants

Target: Carry data in variants. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```haxe
enum Shape { Circle(r:Float); Square(side:Float); }

function area(s:Shape):Float {
  return switch (s) {
    case Circle(r): 3.14159 * r * r;
    case Square(side): side * side;
  }
}
```
### 3. Pattern match enums

Target: Pattern match enums. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```haxe
enum Maybe<T> { Some(v:T); None; }
```
### 4. Use enum constructors

Target: Use enum constructors. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```haxe
var c = Color.Red;
switch (c) { case Red: trace("red"); case _: }
```

## Practice Questions

1. What is the key idea behind "Enums (ADTs)"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Enums (ADTs) with analogies and real-world examples"
1. "Show me common mistakes beginners make with Enums (ADTs)"
1. "Provide advanced patterns and performance considerations for Enums (ADTs)"

## Key Takeaways

- Master the core ideas of Enums (ADTs) through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
