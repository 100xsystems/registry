---
{
  "title": "Scenes and Nodes",
  "description": "Compose games with the scene tree.",
  "type": "lesson",
  "order": 7,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Understand the scene tree",
    "Get child nodes",
    "Add children",
    "Use groups"
  ],
  "knowledge_refs": [
    "gdscript/gdscript-07-scenes"
  ],
  "prerequisites": [
    "GDScript-06: Signals"
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

# GDSCRIPT-07-SCENES: Scenes and Nodes

## Introduction

Compose games with the scene tree. By the end of this lesson you will be able to: Understand the scene tree; Get child nodes; Add children; Use groups.

## Key Concepts

### 1. Understand the scene tree

Target: Understand the scene tree. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```gdscript
extends Node2D

func _ready():
    var child = get_node("Sprite2D")
    print(child)
```
### 2. Get child nodes

Target: Get child nodes. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```gdscript
var sprite = $Sprite2D   # shorthand
```
### 3. Add children

Target: Add children. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```gdscript
var new_node = Label.new()
add_child(new_node)
```
### 4. Use groups

Target: Use groups. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```gdscript
func _ready():
    for node in get_tree().get_nodes_in_group("enemies"):
        print(node)
```

## Practice Questions

1. What is the key idea behind "Scenes and Nodes"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Scenes and Nodes with analogies and real-world examples"
1. "Show me common mistakes beginners make with Scenes and Nodes"
1. "Provide advanced patterns and performance considerations for Scenes and Nodes"

## Key Takeaways

- Master the core ideas of Scenes and Nodes through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
