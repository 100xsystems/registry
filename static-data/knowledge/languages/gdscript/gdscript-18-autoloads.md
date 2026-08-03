---
{
  "title": "Autoload Singletons",
  "description": "Global game state.",
  "type": "lesson",
  "order": 18,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Create autoloads",
    "Access global state",
    "Manage singletons",
    "Persist between scenes"
  ],
  "knowledge_refs": [
    "gdscript/gdscript-18-autoloads"
  ],
  "prerequisites": [
    "GDScript-17: Threads and Async"
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

# GDSCRIPT-18-AUTOLOADS: Autoload Singletons

## Introduction

Global game state. By the end of this lesson you will be able to: Create autoloads; Access global state; Manage singletons; Persist between scenes.

## Key Concepts

### 1. Create autoloads

Target: Create autoloads. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```gdscript
extends Node

var score = 0
var player_name = "Ada"
```
### 2. Access global state

Target: Access global state. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```gdscript
func _ready():
    Game.score = 10
    print(Game.score)
```
### 3. Manage singletons

Target: Manage singletons. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```gdscript
extends Node

signal game_over

func end_game():
    game_over.emit()
```
### 4. Persist between scenes

Target: Persist between scenes. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```gdscript
Game.player_name = "Grace"
print(Game.player_name)
```

## Practice Questions

1. What is the key idea behind "Autoload Singletons"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Autoload Singletons with analogies and real-world examples"
1. "Show me common mistakes beginners make with Autoload Singletons"
1. "Provide advanced patterns and performance considerations for Autoload Singletons"

## Key Takeaways

- Master the core ideas of Autoload Singletons through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
