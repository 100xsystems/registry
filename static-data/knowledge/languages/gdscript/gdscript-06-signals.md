---
{
  "title": "Signals",
  "description": "Event-driven communication.",
  "type": "lesson",
  "order": 6,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Declare signals",
    "Emit signals",
    "Connect signals",
    "Disconnect signals"
  ],
  "knowledge_refs": [
    "gdscript/gdscript-06-signals"
  ],
  "prerequisites": [
    "GDScript-05: Arrays and Dictionaries"
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

# GDSCRIPT-06-SIGNALS: Signals

## Introduction

Event-driven communication. By the end of this lesson you will be able to: Declare signals; Emit signals; Connect signals; Disconnect signals.

## Key Concepts

### 1. Declare signals

Target: Declare signals. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```gdscript
signal health_changed(new_hp)

func take_damage(amount):
    hp -= amount
    health_changed.emit(hp)
```
### 2. Emit signals

Target: Emit signals. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```gdscript
func _ready():
    button.pressed.connect(_on_button_pressed)

func _on_button_pressed():
    print("clicked")
```
### 3. Connect signals

Target: Connect signals. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```gdscript
signal died
func _ready():
    died.connect(queue_free)
```
### 4. Disconnect signals

Target: Disconnect signals. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```gdscript
if not node.connected:
    node.connect("pressed", Callable(self, "_on_pressed"))
```

## Practice Questions

1. What is the key idea behind "Signals"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Signals with analogies and real-world examples"
1. "Show me common mistakes beginners make with Signals"
1. "Provide advanced patterns and performance considerations for Signals"

## Key Takeaways

- Master the core ideas of Signals through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
