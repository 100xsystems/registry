---
{
  "title": "Clipboard Manipulation",
  "description": "Read, write, and transform clipboard.",
  "type": "lesson",
  "order": 9,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Read clipboard",
    "Write clipboard",
    "Transform text",
    "Use clipboard history"
  ],
  "knowledge_refs": [
    "autohotkey/autohotkey-09-clipboard"
  ],
  "prerequisites": [
    "AutoHotkey-08: Sending Keystrokes"
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

# AUTOHOTKEY-09-CLIPBOARD: Clipboard Manipulation

## Introduction

Read, write, and transform clipboard. By the end of this lesson you will be able to: Read clipboard; Write clipboard; Transform text; Use clipboard history.

## Key Concepts

### 1. Read clipboard

Target: Read clipboard. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```autohotkey
^c
Sleep 50
MsgBox A_Clipboard
```
### 2. Write clipboard

Target: Write clipboard. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```autohotkey
A_Clipboard := "new content"
```
### 3. Transform text

Target: Transform text. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```autohotkey
^c
Sleep 50
A_Clipboard := StrReplace(A_Clipboard, "old", "new")
```
### 4. Use clipboard history

Target: Use clipboard history. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```autohotkey
A_Clipboard := FormatTime(, "yyyy-MM-dd")
```

## Practice Questions

1. What is the key idea behind "Clipboard Manipulation"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Clipboard Manipulation with analogies and real-world examples"
1. "Show me common mistakes beginners make with Clipboard Manipulation"
1. "Provide advanced patterns and performance considerations for Clipboard Manipulation"

## Key Takeaways

- Master the core ideas of Clipboard Manipulation through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
