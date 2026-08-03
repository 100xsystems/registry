---
{
  "title": "Arrays and Objects",
  "description": "Collections in v2.",
  "type": "lesson",
  "order": 12,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create arrays",
    "Access elements",
    "Use maps",
    "Iterate objects"
  ],
  "knowledge_refs": [
    "autohotkey/autohotkey-12-arrays-objects"
  ],
  "prerequisites": [
    "AutoHotkey-11: GUIs"
  ],
  "references": [
    {
      "title": "AutoHotkey Documentation",
      "url": "https://www.autohotkey.com/docs/",
      "description": "Official docs"
    },
    {
      "title": "AutoHotkey v2 Changes",
      "url": "https://www.autohotkey.com/docs/v2/",
      "description": "Version 2 documentation"
    },
    {
      "title": "AutoHotkey Forum",
      "url": "https://www.autohotkey.com/boards/",
      "description": "Community forum"
    }
  ]
}
---

# AUTOHOTKEY-12-ARRAYS-OBJECTS: Arrays and Objects

## Introduction

Collections in v2. By the end of this lesson you will be able to: Create arrays; Access elements; Use maps; Iterate objects.

## Key Concepts

### 1. Create arrays

Target: Create arrays. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```autohotkey
colors := ["red", "green", "blue"]
MsgBox colors[1]
```
### 2. Access elements

Target: Access elements. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```autohotkey
colors.Push("yellow")
MsgBox colors.Length
```
### 3. Use maps

Target: Use maps. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```autohotkey
person := Map("name", "Ada", "age", 36)
MsgBox person["name"]
```
### 4. Iterate objects

Target: Iterate objects. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```autohotkey
for key, value in person
    MsgBox key ": " value
```

## Practice Questions

1. What is the key idea behind "Arrays and Objects"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Arrays and Objects with analogies and real-world examples"
1. "Show me common mistakes beginners make with Arrays and Objects"
1. "Provide advanced patterns and performance considerations for Arrays and Objects"

## Key Takeaways

- Master the core ideas of Arrays and Objects through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
