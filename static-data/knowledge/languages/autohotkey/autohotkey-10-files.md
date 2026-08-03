---
{
  "title": "File Operations",
  "description": "Read, write, and manage files.",
  "type": "lesson",
  "order": 10,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Read files",
    "Write files",
    "List files",
    "Check existence"
  ],
  "knowledge_refs": [
    "autohotkey/autohotkey-10-files"
  ],
  "prerequisites": [
    "AutoHotkey-09: Clipboard Manipulation"
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

# AUTOHOTKEY-10-FILES: File Operations

## Introduction

Read, write, and manage files. By the end of this lesson you will be able to: Read files; Write files; List files; Check existence.

## Key Concepts

### 1. Read files

Target: Read files. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```autohotkey
content := FileRead("data.txt")
MsgBox content
```
### 2. Write files

Target: Write files. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```autohotkey
FileAppend "new line`n", "log.txt"
```
### 3. List files

Target: List files. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```autohotkey
Loop Files "*.txt"
    MsgBox A_LoopFileName
```
### 4. Check existence

Target: Check existence. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```autohotkey
if (FileExist("config.ini"))
    MsgBox "exists"
```

## Practice Questions

1. What is the key idea behind "File Operations"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain File Operations with analogies and real-world examples"
1. "Show me common mistakes beginners make with File Operations"
1. "Provide advanced patterns and performance considerations for File Operations"

## Key Takeaways

- Master the core ideas of File Operations through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
