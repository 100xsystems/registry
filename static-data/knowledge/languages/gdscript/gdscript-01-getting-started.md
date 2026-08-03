---
{
  "title": "Getting Started with GDScript",
  "description": "Godot editor, scripts, and hello.",
  "type": "lesson",
  "order": 1,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Create a Godot project",
    "Attach scripts to nodes",
    "Print output",
    "Run the scene"
  ],
  "knowledge_refs": [
    "gdscript/gdscript-01-getting-started"
  ],
  "prerequisites": [
    "None — this is the entry point"
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

# GDSCRIPT-01-GETTING-STARTED: Getting Started with GDScript

## Introduction

Godot editor, scripts, and hello. By the end of this lesson you will be able to: Create a Godot project; Attach scripts to nodes; Print output; Run the scene.

## Key Concepts

### 1. Create a Godot project

Target: Create a Godot project. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```gdscript
extends Node

func _ready():
    print("Hello, World!")
```
### 2. Attach scripts to nodes

Target: Attach scripts to nodes. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```gdscript
extends Node

func _ready():
    print("Hello, ", "Godot!")
```
### 3. Print output

Target: Print output. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```gdscript
extends Node

func _ready():
    var greeting = "Hello"
    print(greeting)
```
### 4. Run the scene

Target: Run the scene. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```gdscript
extends Node

func _ready():
    print(1 + 2)
    print("num: ", 42)
```

## Practice Questions

1. What is the key idea behind "Getting Started with GDScript"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with GDScript with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with GDScript"
1. "Provide advanced patterns and performance considerations for Getting Started with GDScript"

## Key Takeaways

- Master the core ideas of Getting Started with GDScript through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
