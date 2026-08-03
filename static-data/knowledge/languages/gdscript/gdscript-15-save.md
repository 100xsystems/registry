---
{
  "title": "Saving and Loading",
  "description": "Persist game state.",
  "type": "lesson",
  "order": 15,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Write save files",
    "Read save files",
    "Serialize data",
    "Load game state"
  ],
  "knowledge_refs": [
    "gdscript/gdscript-15-save"
  ],
  "prerequisites": [
    "GDScript-14: UI and HUDs"
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

# GDSCRIPT-15-SAVE: Saving and Loading

## Introduction

Persist game state. By the end of this lesson you will be able to: Write save files; Read save files; Serialize data; Load game state.

## Key Concepts

### 1. Write save files

Target: Write save files. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```gdscript
var data = {"score": score, "hp": hp}
var file = FileAccess.open("user://save.json", FileAccess.WRITE)
file.store_string(JSON.stringify(data))
file.close()
```
### 2. Read save files

Target: Read save files. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```gdscript
if FileAccess.file_exists("user://save.json"):
    var file = FileAccess.open("user://save.json", FileAccess.READ)
    var data = JSON.parse_string(file.get_as_text())
    file.close()
```
### 3. Serialize data

Target: Serialize data. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```gdscript
var dir = DirAccess.open("user://")
if not dir.dir_exists("saves"):
    dir.make_dir("saves")
```
### 4. Load game state

Target: Load game state. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```gdscript
DirAccess.remove_absolute("user://save.json")
```

## Practice Questions

1. What is the key idea behind "Saving and Loading"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Saving and Loading with analogies and real-world examples"
1. "Show me common mistakes beginners make with Saving and Loading"
1. "Provide advanced patterns and performance considerations for Saving and Loading"

## Key Takeaways

- Master the core ideas of Saving and Loading through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
