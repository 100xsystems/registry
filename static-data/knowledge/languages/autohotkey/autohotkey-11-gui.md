---
{
  "title": "GUIs",
  "description": "Build simple interfaces.",
  "type": "lesson",
  "order": 11,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create a GUI",
    "Add controls",
    "Handle events",
    "Show dialogs"
  ],
  "knowledge_refs": [
    "autohotkey/autohotkey-11-gui"
  ],
  "prerequisites": [
    "AutoHotkey-10: File Operations"
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

# AUTOHOTKEY-11-GUI: GUIs

## Introduction

Build simple interfaces. By the end of this lesson you will be able to: Create a GUI; Add controls; Handle events; Show dialogs.

## Key Concepts

### 1. Create a GUI

Target: Create a GUI. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```autohotkey
myGui := Gui()
myGui.Add("Text", , "Hello!")
myGui.Show()
```
### 2. Add controls

Target: Add controls. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```autohotkey
myGui := Gui()
myGui.Add("Edit", "vInput w200")
myGui.Add("Button", "gSubmit", "OK")
myGui.Show()

Submit(*)
{
    saved := myGui.Submit()
    MsgBox saved.Input
}
```
### 3. Handle events

Target: Handle events. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```autohotkey
MsgBox "Simple dialog"
```
### 4. Show dialogs

Target: Show dialogs. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```autohotkey
result := MsgBox("Continue?", "Question", "YesNo")
if (result = "Yes")
    MsgBox "Continuing"
```

## Practice Questions

1. What is the key idea behind "GUIs"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain GUIs with analogies and real-world examples"
1. "Show me common mistakes beginners make with GUIs"
1. "Provide advanced patterns and performance considerations for GUIs"

## Key Takeaways

- Master the core ideas of GUIs through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
