---
{
  "title": "Input Handling",
  "description": "Keyboard, mouse, and actions.",
  "type": "lesson",
  "order": 9,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Poll input",
    "Use Input.is_action_pressed",
    "Handle mouse events",
    "Map input actions"
  ],
  "knowledge_refs": [
    "gdscript/gdscript-09-input"
  ],
  "prerequisites": [
    "GDScript-08: Physics and Movement"
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

# GDSCRIPT-09-INPUT: Input Handling

## Introduction

Keyboard, mouse, and actions. By the end of this lesson you will be able to: Poll input; Use Input.is_action_pressed; Handle mouse events; Map input actions.

## Key Concepts

### 1. Poll input

Target: Poll input. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```gdscript
func _process(delta):
    if Input.is_action_pressed("ui_right"):
        position.x += 10 * delta
```
### 2. Use Input.is_action_pressed

Target: Use Input.is_action_pressed. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```gdscript
func _input(event):
    if event is InputEventKey and event.pressed:
        print(event.keycode)
```
### 3. Handle mouse events

Target: Handle mouse events. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```gdscript
func _unhandled_input(event):
    if event is InputEventMouseButton and event.button_index == MOUSE_BUTTON_LEFT:
        print("clicked at ", event.position)
```
### 4. Map input actions

Target: Map input actions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```gdscript
Input.action_press("jump")
```

## Practice Questions

1. What is the key idea behind "Input Handling"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Input Handling with analogies and real-world examples"
1. "Show me common mistakes beginners make with Input Handling"
1. "Provide advanced patterns and performance considerations for Input Handling"

## Key Takeaways

- Master the core ideas of Input Handling through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
