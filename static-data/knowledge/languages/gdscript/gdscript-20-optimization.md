---
{
  "title": "Performance Tips",
  "description": "Keep games running fast.",
  "type": "lesson",
  "order": 20,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Avoid per-frame allocations",
    "Use pools",
    "Limit draw calls",
    "Profile performance"
  ],
  "knowledge_refs": [
    "gdscript/gdscript-20-optimization"
  ],
  "prerequisites": [
    "GDScript-19: Exporting Games"
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

# GDSCRIPT-20-OPTIMIZATION: Performance Tips

## Introduction

Keep games running fast. By the end of this lesson you will be able to: Avoid per-frame allocations; Use pools; Limit draw calls; Profile performance.

## Key Concepts

### 1. Avoid per-frame allocations

Target: Avoid per-frame allocations. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```gdscript
var reused_array = []

func _physics_process(delta):
    reused_array.clear()
    reused_array.append(1)
```
### 2. Use pools

Target: Use pools. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```gdscript
preload("res://scene.tscn")   # compile-time load
```
### 3. Limit draw calls

Target: Limit draw calls. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```gdscript
get_tree().debug_collisions_hint = false
```
### 4. Profile performance

Target: Profile performance. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```gdscript
var profiler = Engine.get_frames_per_second()
print(profiler)
```

## Practice Questions

1. What is the key idea behind "Performance Tips"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Performance Tips with analogies and real-world examples"
1. "Show me common mistakes beginners make with Performance Tips"
1. "Provide advanced patterns and performance considerations for Performance Tips"

## Key Takeaways

- Master the core ideas of Performance Tips through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
