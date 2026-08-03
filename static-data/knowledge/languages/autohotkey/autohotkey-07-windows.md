---
{
  "title": "Window Management",
  "description": "Activate, close, and manipulate windows.",
  "type": "lesson",
  "order": 7,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Activate windows",
    "Close windows",
    "Move and resize",
    "Wait for windows"
  ],
  "knowledge_refs": [
    "autohotkey/autohotkey-07-windows"
  ],
  "prerequisites": [
    "AutoHotkey-06: Functions"
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

# AUTOHOTKEY-07-WINDOWS: Window Management

## Introduction

Activate, close, and manipulate windows. By the end of this lesson you will be able to: Activate windows; Close windows; Move and resize; Wait for windows.

## Key Concepts

### 1. Activate windows

Target: Activate windows. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```autohotkey
WinActivate "Untitled - Notepad"
```
### 2. Close windows

Target: Close windows. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```autohotkey
WinClose "Untitled - Notepad"
```
### 3. Move and resize

Target: Move and resize. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```autohotkey
WinMove 100, 100, 800, 600, "Untitled"
```
### 4. Wait for windows

Target: Wait for windows. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```autohotkey
WinWait "Notepad"
WinActivate
```

## Practice Questions

1. What is the key idea behind "Window Management"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Window Management with analogies and real-world examples"
1. "Show me common mistakes beginners make with Window Management"
1. "Provide advanced patterns and performance considerations for Window Management"

## Key Takeaways

- Master the core ideas of Window Management through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
