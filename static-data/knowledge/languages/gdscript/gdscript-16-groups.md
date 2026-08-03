---
{
  "title": "Groups and Communication",
  "description": "Broadcast to many nodes.",
  "type": "lesson",
  "order": 16,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Add nodes to groups",
    "Call group methods",
    "Get group lists",
    "Use groups for systems"
  ],
  "knowledge_refs": [
    "gdscript/gdscript-16-groups"
  ],
  "prerequisites": [
    "GDScript-15: Saving and Loading"
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

# GDSCRIPT-16-GROUPS: Groups and Communication

## Introduction

Broadcast to many nodes. By the end of this lesson you will be able to: Add nodes to groups; Call group methods; Get group lists; Use groups for systems.

## Key Concepts

### 1. Add nodes to groups

Target: Add nodes to groups. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```gdscript
func _ready():
    add_to_group("enemies")
```
### 2. Call group methods

Target: Call group methods. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```gdscript
get_tree().call_group("enemies", "take_damage", 10)
```
### 3. Get group lists

Target: Get group lists. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```gdscript
for enemy in get_tree().get_nodes_in_group("enemies"):
    enemy.take_damage(10)
```
### 4. Use groups for systems

Target: Use groups for systems. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```gdscript
if is_in_group("player"):
    print("I am the player")
```

## Practice Questions

1. What is the key idea behind "Groups and Communication"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Groups and Communication with analogies and real-world examples"
1. "Show me common mistakes beginners make with Groups and Communication"
1. "Provide advanced patterns and performance considerations for Groups and Communication"

## Key Takeaways

- Master the core ideas of Groups and Communication through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
