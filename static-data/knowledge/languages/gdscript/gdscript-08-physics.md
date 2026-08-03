---
{
  "title": "Physics and Movement",
  "description": "Move and collide in 2D.",
  "type": "lesson",
  "order": 8,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use process and physics frames",
    "Move with velocity",
    "Detect collisions",
    "Use delta time"
  ],
  "knowledge_refs": [
    "gdscript/gdscript-08-physics"
  ],
  "prerequisites": [
    "GDScript-07: Scenes and Nodes"
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

# GDSCRIPT-08-PHYSICS: Physics and Movement

## Introduction

Move and collide in 2D. By the end of this lesson you will be able to: Use process and physics frames; Move with velocity; Detect collisions; Use delta time.

## Key Concepts

### 1. Use process and physics frames

Target: Use process and physics frames. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```gdscript
extends CharacterBody2D

var speed = 300.0

func _physics_process(delta):
    var input = Input.get_vector("left", "right", "up", "down")
    velocity = input * speed
    move_and_slide()
```
### 2. Move with velocity

Target: Move with velocity. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```gdscript
func _process(delta):
    position.x += 100 * delta
```
### 3. Detect collisions

Target: Detect collisions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```gdscript
func _physics_process(delta):
    velocity.y += 980 * delta   # gravity
    move_and_slide()
```
### 4. Use delta time

Target: Use delta time. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```gdscript
func _on_body_entered(body):
    print(body.name, " entered")
```

## Practice Questions

1. What is the key idea behind "Physics and Movement"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Physics and Movement with analogies and real-world examples"
1. "Show me common mistakes beginners make with Physics and Movement"
1. "Provide advanced patterns and performance considerations for Physics and Movement"

## Key Takeaways

- Master the core ideas of Physics and Movement through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
