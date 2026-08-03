---
{
  "title": "Hotkeys and Hotstrings",
  "description": "Modifiers, triggers, and expansions.",
  "type": "lesson",
  "order": 2,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use modifier keys",
    "Define hotstrings",
    "Send keystrokes",
    "Use remapping"
  ],
  "knowledge_refs": [
    "autohotkey/autohotkey-02-hotkeys"
  ],
  "prerequisites": [
    "AutoHotkey-01: Getting Started with AutoHotkey"
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

# AUTOHOTKEY-02-HOTKEYS: Hotkeys and Hotstrings

## Introduction

Modifiers, triggers, and expansions. By the end of this lesson you will be able to: Use modifier keys; Define hotstrings; Send keystrokes; Use remapping.

## Key Concepts

### 1. Use modifier keys

Target: Use modifier keys. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```autohotkey
^s::Send "^s"   ; pass through
```
### 2. Define hotstrings

Target: Define hotstrings. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```autohotkey
::btw::by the way
```
### 3. Send keystrokes

Target: Send keystrokes. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```autohotkey
!f::Send "file"
```
### 4. Use remapping

Target: Use remapping. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```autohotkey
CapsLock::Ctrl     ; remap key
```

## Practice Questions

1. What is the key idea behind "Hotkeys and Hotstrings"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Hotkeys and Hotstrings with analogies and real-world examples"
1. "Show me common mistakes beginners make with Hotkeys and Hotstrings"
1. "Provide advanced patterns and performance considerations for Hotkeys and Hotstrings"

## Key Takeaways

- Master the core ideas of Hotkeys and Hotstrings through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
