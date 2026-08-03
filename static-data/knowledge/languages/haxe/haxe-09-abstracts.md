---
{
  "title": "Abstract Types",
  "description": "Type wrappers with zero cost.",
  "type": "lesson",
  "order": 9,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Define abstract types",
    "Wrap primitives",
    "Add methods",
    "Control conversions"
  ],
  "knowledge_refs": [
    "haxe/haxe-09-abstracts"
  ],
  "prerequisites": [
    "Haxe-08: Enums (ADTs)"
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

# HAXE-09-ABSTRACTS: Abstract Types

## Introduction

Type wrappers with zero cost. By the end of this lesson you will be able to: Define abstract types; Wrap primitives; Add methods; Control conversions.

## Key Concepts

### 1. Define abstract types

Target: Define abstract types. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```haxe
abstract UserId(Int) {
  public function new(id:Int) this = id;
}
```
### 2. Wrap primitives

Target: Wrap primitives. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```haxe
abstract Celsius(Float) {
  public inline function new(v:Float) this = v;

  public var fahrenheit(get, never):Float;
  function get_fahrenheit():Float return this * 9 / 5 + 32;
}
```
### 3. Add methods

Target: Add methods. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```haxe
abstract Meters(Int) to Int {}
```
### 4. Control conversions

Target: Control conversions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```haxe
abstract Percent(Int) from Int {}
```

## Practice Questions

1. What is the key idea behind "Abstract Types"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Abstract Types with analogies and real-world examples"
1. "Show me common mistakes beginners make with Abstract Types"
1. "Provide advanced patterns and performance considerations for Abstract Types"

## Key Takeaways

- Master the core ideas of Abstract Types through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
