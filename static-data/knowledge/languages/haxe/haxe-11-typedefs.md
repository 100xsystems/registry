---
{
  "title": "Typedefs",
  "description": "Structural types.",
  "type": "lesson",
  "order": 11,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define typedefs",
    "Use structural typing",
    "Compose typedefs",
    "Use optional fields"
  ],
  "knowledge_refs": [
    "haxe/haxe-11-typedefs"
  ],
  "prerequisites": [
    "Haxe-10: Generics"
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

# HAXE-11-TYPEDEFS: Typedefs

## Introduction

Structural types. By the end of this lesson you will be able to: Define typedefs; Use structural typing; Compose typedefs; Use optional fields.

## Key Concepts

### 1. Define typedefs

Target: Define typedefs. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```haxe
typedef User = {
  var name:String;
  var age:Int;
}
```
### 2. Use structural typing

Target: Use structural typing. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```haxe
typedef Point = { x:Float, y:Float };
var p:Point = { x: 0, y: 0 };
```
### 3. Compose typedefs

Target: Compose typedefs. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```haxe
typedef Config = {
  ?verbose:Bool;
  var port:Int;
}
```
### 4. Use optional fields

Target: Use optional fields. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```haxe
typedef Callback = Int -> Void;
```

## Practice Questions

1. What is the key idea behind "Typedefs"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Typedefs with analogies and real-world examples"
1. "Show me common mistakes beginners make with Typedefs"
1. "Provide advanced patterns and performance considerations for Typedefs"

## Key Takeaways

- Master the core ideas of Typedefs through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
