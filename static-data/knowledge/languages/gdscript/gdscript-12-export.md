---
{
  "title": "Exporting Variables",
  "description": "Configure nodes in the editor.",
  "type": "lesson",
  "order": 12,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use @export",
    "Expose typed ranges",
    "Use @export_group",
    "Tune values from editor"
  ],
  "knowledge_refs": [
    "gdscript/gdscript-12-export"
  ],
  "prerequisites": [
    "GDScript-11: Animation"
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

# GDSCRIPT-12-EXPORT: Exporting Variables

## Introduction

Configure nodes in the editor. By the end of this lesson you will be able to: Use @export; Expose typed ranges; Use @export_group; Tune values from editor.

## Key Concepts

### 1. Use @export

Target: Use @export. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```gdscript
extends Node2D

@export var speed = 100.0
@export var color: Color = Color.WHITE
```
### 2. Expose typed ranges

Target: Expose typed ranges. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```gdscript
@export_range(0, 10, 0.5) var volume = 1.0
```
### 3. Use @export_group

Target: Use @export_group. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```gdscript
@export var items: Array[String] = []
```
### 4. Tune values from editor

Target: Tune values from editor. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```gdscript
@export_group("Combat")
@export var damage = 10
@export var cooldown = 0.5
```

## Practice Questions

1. What is the key idea behind "Exporting Variables"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Exporting Variables with analogies and real-world examples"
1. "Show me common mistakes beginners make with Exporting Variables"
1. "Provide advanced patterns and performance considerations for Exporting Variables"

## Key Takeaways

- Master the core ideas of Exporting Variables through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
