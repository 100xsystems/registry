---
{
  "title": "Advanced Hotkeys",
  "description": "Context-sensitive hotkeys and modes.",
  "type": "lesson",
  "order": 15,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use #IfWinActive",
    "Create mode toggles",
    "Use key-up triggers",
    "Chain hotkeys"
  ],
  "knowledge_refs": [
    "autohotkey/autohotkey-15-hotkeys-advanced"
  ],
  "prerequisites": [
    "AutoHotkey-14: Timers"
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

# AUTOHOTKEY-15-HOTKEYS-ADVANCED: Advanced Hotkeys

## Introduction

Context-sensitive hotkeys and modes. By the end of this lesson you will be able to: Use #IfWinActive; Create mode toggles; Use key-up triggers; Chain hotkeys.

## Key Concepts

### 1. Use #IfWinActive

Target: Use #IfWinActive. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```autohotkey
#HotIf WinActive("ahk_class Notepad")
^d::MsgBox "in notepad"
#HotIf
```
### 2. Create mode toggles

Target: Create mode toggles. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```autohotkey
capsToggled := false
CapsLock::
{
    capsToggled := !capsToggled
    if (capsToggled)
        MsgBox "mode on"
    else
        MsgBox "mode off"
}
```
### 3. Use key-up triggers

Target: Use key-up triggers. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```autohotkey
a & b::MsgBox "a then b"
```
### 4. Chain hotkeys

Target: Chain hotkeys. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```autohotkey
^!+s::MsgBox "Ctrl+Alt+Shift+S"
```

## Practice Questions

1. What is the key idea behind "Advanced Hotkeys"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Advanced Hotkeys with analogies and real-world examples"
1. "Show me common mistakes beginners make with Advanced Hotkeys"
1. "Provide advanced patterns and performance considerations for Advanced Hotkeys"

## Key Takeaways

- Master the core ideas of Advanced Hotkeys through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
