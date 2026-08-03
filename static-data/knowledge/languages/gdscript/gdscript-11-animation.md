---
{
  "title": "Animations",
  "description": "Animate sprites and properties.",
  "type": "lesson",
  "order": 11,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Play animations",
    "Use AnimationPlayer",
    "Tween properties",
    "Sync animations"
  ],
  "knowledge_refs": [
    "gdscript/gdscript-11-animation"
  ],
  "prerequisites": [
    "GDScript-10: Custom Classes and Inheritance"
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

# GDSCRIPT-11-ANIMATION: Animations

## Introduction

Animate sprites and properties. By the end of this lesson you will be able to: Play animations; Use AnimationPlayer; Tween properties; Sync animations.

## Key Concepts

### 1. Play animations

Target: Play animations. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```gdscript
func _ready():
    $AnimationPlayer.play("walk")
```
### 2. Use AnimationPlayer

Target: Use AnimationPlayer. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```gdscript
var tween = create_tween()
tween.tween_property(self, "position", Vector2(100, 100), 1.0)
```
### 3. Tween properties

Target: Tween properties. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```gdscript
func _ready():
    $AnimationPlayer.play("idle")
```
### 4. Sync animations

Target: Sync animations. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```gdscript
var tween = create_tween()
tween.tween_property($Sprite2D, "modulate:a", 0.0, 0.5)
```

## Practice Questions

1. What is the key idea behind "Animations"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Animations with analogies and real-world examples"
1. "Show me common mistakes beginners make with Animations"
1. "Provide advanced patterns and performance considerations for Animations"

## Key Takeaways

- Master the core ideas of Animations through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
