---
{
  "title": "Control Flow",
  "description": "if, else, switch.",
  "type": "lesson",
  "order": 4,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use if/else",
    "Use switch",
    "Compare values",
    "Check conditions"
  ],
  "knowledge_refs": [
    "autohotkey/autohotkey-04-control-flow"
  ],
  "prerequisites": [
    "AutoHotkey-03: Variables and Expressions"
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

# AUTOHOTKEY-04-CONTROL-FLOW: Control Flow

## Introduction

if, else, switch. By the end of this lesson you will be able to: Use if/else; Use switch; Compare values; Check conditions.

## Key Concepts

### 1. Use if/else

Target: Use if/else. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```autohotkey
score := 85
if (score >= 90)
    MsgBox "A"
else if (score >= 80)
    MsgBox "B"
else
    MsgBox "C"
```
### 2. Use switch

Target: Use switch. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```autohotkey
x := 2
switch x
{
    case 1: MsgBox "one"
    case 2: MsgBox "two"
    default: MsgBox "other"
}
```
### 3. Compare values

Target: Compare values. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```autohotkey
if WinExist("Untitled - Notepad")
    MsgBox "Notepad is open"
```
### 4. Check conditions

Target: Check conditions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```autohotkey
if (FileExist("data.txt"))
    MsgBox "File exists"
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
