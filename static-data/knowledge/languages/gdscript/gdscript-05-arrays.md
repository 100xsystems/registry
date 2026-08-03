---
{
  "title": "Arrays and Dictionaries",
  "description": "Collections in GDScript.",
  "type": "lesson",
  "order": 5,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Create arrays",
    "Access elements",
    "Use dictionaries",
    "Iterate collections"
  ],
  "knowledge_refs": [
    "gdscript/gdscript-05-arrays"
  ],
  "prerequisites": [
    "GDScript-04: Functions"
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

# GDSCRIPT-05-ARRAYS: Arrays and Dictionaries

## Introduction

Collections in GDScript. By the end of this lesson you will be able to: Create arrays; Access elements; Use dictionaries; Iterate collections.

## Key Concepts

### 1. Create arrays

Target: Create arrays. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```gdscript
var items = ["sword", "shield"]
items.append("potion")
print(items[0])
```
### 2. Access elements

Target: Access elements. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```gdscript
var scores = [10, 20, 30]
for s in scores:
    print(s)
```
### 3. Use dictionaries

Target: Use dictionaries. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```gdscript
var player = {"name": "Ada", "hp": 100}
print(player["name"])
```
### 4. Iterate collections

Target: Iterate collections. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```gdscript
for key in player:
    print(key, ": ", player[key])
```

## Practice Questions

1. What is the key idea behind "Arrays and Dictionaries"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Arrays and Dictionaries with analogies and real-world examples"
1. "Show me common mistakes beginners make with Arrays and Dictionaries"
1. "Provide advanced patterns and performance considerations for Arrays and Dictionaries"

## Key Takeaways

- Master the core ideas of Arrays and Dictionaries through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
