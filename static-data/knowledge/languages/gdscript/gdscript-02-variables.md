---
{
  "title": "Variables and Types",
  "description": "Typed and untyped declarations.",
  "type": "lesson",
  "order": 2,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Declare variables",
    "Use explicit types",
    "Use constants",
    "Understand inference"
  ],
  "knowledge_refs": [
    "gdscript/gdscript-02-variables"
  ],
  "prerequisites": [
    "GDScript-01: Getting Started with GDScript"
  ],
  "references": [
    {
      "title": "Godot Docs: GDScript",
      "url": "https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/index.html",
      "description": "Official documentation"
    },
    {
      "title": "GDScript Reference",
      "url": "https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_basics.html",
      "description": "Language reference"
    },
    {
      "title": "Godot Community",
      "url": "https://godotengine.org/community/",
      "description": "Community links"
    }
  ]
}
---

# GDSCRIPT-02-VARIABLES: Variables and Types

## Introduction

Typed and untyped declarations. By the end of this lesson you will be able to: Declare variables; Use explicit types; Use constants; Understand inference.

## Key Concepts

### 1. Declare variables

Target: Declare variables. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```gdscript
var score = 0
var name = "Ada"
var speed = 2.5
```
### 2. Use explicit types

Target: Use explicit types. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```gdscript
var health: int = 100
var title: String = "Hero"
```
### 3. Use constants

Target: Use constants. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```gdscript
const MAX_HP = 100
const PI = 3.14159
```
### 4. Understand inference

Target: Understand inference. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```gdscript
var alive: bool = true
var items: Array = []
```

## Practice Questions

1. What is the key idea behind "Variables and Types"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Variables and Types with analogies and real-world examples"
1. "Show me common mistakes beginners make with Variables and Types"
1. "Provide advanced patterns and performance considerations for Variables and Types"

## Key Takeaways

- Master the core ideas of Variables and Types through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
