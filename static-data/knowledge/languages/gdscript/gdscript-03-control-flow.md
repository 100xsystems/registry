---
{
  "title": "Control Flow",
  "description": "if, match, and loops.",
  "type": "lesson",
  "order": 3,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Write if/elif/else",
    "Use match statements",
    "Use for loops",
    "Use while loops"
  ],
  "knowledge_refs": [
    "gdscript/gdscript-03-control-flow"
  ],
  "prerequisites": [
    "GDScript-02: Variables and Types"
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

# GDSCRIPT-03-CONTROL-FLOW: Control Flow

## Introduction

if, match, and loops. By the end of this lesson you will be able to: Write if/elif/else; Use match statements; Use for loops; Use while loops.

## Key Concepts

### 1. Write if/elif/else

Target: Write if/elif/else. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```gdscript
var hp = 30
if hp > 75:
    print("healthy")
elif hp > 25:
    print("wounded")
else:
    print("critical")
```
### 2. Use match statements

Target: Use match statements. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```gdscript
match state:
    "idle":
        print("standing")
    "run":
        print("running")
    _:
        print("unknown")
```
### 3. Use for loops

Target: Use for loops. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```gdscript
for i in range(3):
    print(i)
```
### 4. Use while loops

Target: Use while loops. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```gdscript
var i = 0
while i < 3:
    print(i)
    i += 1
```

## Practice Questions

1. What is the key idea behind "Control Flow"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Control Flow with analogies and real-world examples"
1. "Show me common mistakes beginners make with Control Flow"
1. "Provide advanced patterns and performance considerations for Control Flow"

## Key Takeaways

- Master the core ideas of Control Flow through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
