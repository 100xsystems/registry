---
{
  "title": "UI and HUDs",
  "description": "Labels, buttons, and layouts.",
  "type": "lesson",
  "order": 14,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create UI nodes",
    "Update labels",
    "Connect buttons",
    "Build HUDs"
  ],
  "knowledge_refs": [
    "gdscript/gdscript-14-ui"
  ],
  "prerequisites": [
    "GDScript-13: Areas and Collisions"
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

# GDSCRIPT-14-UI: UI and HUDs

## Introduction

Labels, buttons, and layouts. By the end of this lesson you will be able to: Create UI nodes; Update labels; Connect buttons; Build HUDs.

## Key Concepts

### 1. Create UI nodes

Target: Create UI nodes. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```gdscript
func _ready():
    $HUD/HealthLabel.text = "HP: " + str(hp)
```
### 2. Update labels

Target: Update labels. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```gdscript
func _ready():
    $Button.pressed.connect(_on_clicked)

func _on_clicked():
    print("clicked")
```
### 3. Connect buttons

Target: Connect buttons. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```gdscript
func update_score(points):
    score += points
    $HUD/ScoreLabel.text = str(score)
```
### 4. Build HUDs

Target: Build HUDs. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```gdscript
var label = Label.new()
label.text = "hello"
add_child(label)
```

## Practice Questions

1. What is the key idea behind "UI and HUDs"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain UI and HUDs with analogies and real-world examples"
1. "Show me common mistakes beginners make with UI and HUDs"
1. "Provide advanced patterns and performance considerations for UI and HUDs"

## Key Takeaways

- Master the core ideas of UI and HUDs through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
