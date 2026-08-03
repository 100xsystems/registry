---
{
  "title": "Custom Classes and Inheritance",
  "description": "Extend nodes and structure code.",
  "type": "lesson",
  "order": 10,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create class_name",
    "Extend built-in types",
    "Override methods",
    "Use super"
  ],
  "knowledge_refs": [
    "gdscript/gdscript-10-classes"
  ],
  "prerequisites": [
    "GDScript-09: Input Handling"
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

# GDSCRIPT-10-CLASSES: Custom Classes and Inheritance

## Introduction

Extend nodes and structure code. By the end of this lesson you will be able to: Create class_name; Extend built-in types; Override methods; Use super.

## Key Concepts

### 1. Create class_name

Target: Create class_name. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```gdscript
class_name Player

extends CharacterBody2D

var hp = 100
```
### 2. Extend built-in types

Target: Extend built-in types. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```gdscript
class_name Enemy
extends CharacterBody2D

func take_damage(d):
    hp -= d
    if hp <= 0:
        queue_free()
```
### 3. Override methods

Target: Override methods. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```gdscript
func _ready():
    super()
    print("player ready")
```
### 4. Use super

Target: Use super. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```gdscript
var e: Enemy = Enemy.new()
```

## Practice Questions

1. What is the key idea behind "Custom Classes and Inheritance"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Custom Classes and Inheritance with analogies and real-world examples"
1. "Show me common mistakes beginners make with Custom Classes and Inheritance"
1. "Provide advanced patterns and performance considerations for Custom Classes and Inheritance"

## Key Takeaways

- Master the core ideas of Custom Classes and Inheritance through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
