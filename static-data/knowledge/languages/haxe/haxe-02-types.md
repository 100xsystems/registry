---
{
  "title": "Types and Variables",
  "description": "Static typing with inference.",
  "type": "lesson",
  "order": 2,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Declare typed variables",
    "Use type inference",
    "Use constants",
    "Understand the type system"
  ],
  "knowledge_refs": [
    "haxe/haxe-02-types"
  ],
  "prerequisites": [
    "Haxe-01: Getting Started with Haxe"
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

# HAXE-02-TYPES: Types and Variables

## Introduction

Static typing with inference. By the end of this lesson you will be able to: Declare typed variables; Use type inference; Use constants; Understand the type system.

## Key Concepts

### 1. Declare typed variables

Target: Declare typed variables. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```haxe
var score:Int = 0;
var name:String = "Ada";
var speed:Float = 2.5;
```
### 2. Use type inference

Target: Use type inference. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```haxe
var x = 42;    // inferred Int
```
### 3. Use constants

Target: Use constants. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```haxe
var pi = 3.14; // inferred Float
```
### 4. Understand the type system

Target: Understand the type system. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```haxe
static inline var MAX = 100;
```

## Practice Questions

1. What is the key idea behind "Types and Variables"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Types and Variables with analogies and real-world examples"
1. "Show me common mistakes beginners make with Types and Variables"
1. "Provide advanced patterns and performance considerations for Types and Variables"

## Key Takeaways

- Master the core ideas of Types and Variables through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
