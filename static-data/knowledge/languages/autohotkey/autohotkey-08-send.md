---
{
  "title": "Sending Keystrokes",
  "description": "Send commands and input modes.",
  "type": "lesson",
  "order": 8,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Send text",
    "Send key combos",
    "Use SendInput",
    "Use special keys"
  ],
  "knowledge_refs": [
    "autohotkey/autohotkey-08-send"
  ],
  "prerequisites": [
    "AutoHotkey-07: Window Management"
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

# AUTOHOTKEY-08-SEND: Sending Keystrokes

## Introduction

Send commands and input modes. By the end of this lesson you will be able to: Send text; Send key combos; Use SendInput; Use special keys.

## Key Concepts

### 1. Send text

Target: Send text. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```autohotkey
Send "Hello, World!"
```
### 2. Send key combos

Target: Send key combos. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```autohotkey
Send "^c"        ; copy
Send "^v"        ; paste
```
### 3. Use SendInput

Target: Use SendInput. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```autohotkey
SendInput "fast typing{Enter}"
```
### 4. Use special keys

Target: Use special keys. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```autohotkey
Send "{Enter}{Tab}{Shift down}{Shift up}"
```

## Practice Questions

1. What is the key idea behind "Sending Keystrokes"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Sending Keystrokes with analogies and real-world examples"
1. "Show me common mistakes beginners make with Sending Keystrokes"
1. "Provide advanced patterns and performance considerations for Sending Keystrokes"

## Key Takeaways

- Master the core ideas of Sending Keystrokes through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
