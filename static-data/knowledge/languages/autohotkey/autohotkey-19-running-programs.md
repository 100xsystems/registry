---
{
  "title": "Running Programs",
  "description": "Launch apps and control processes.",
  "type": "lesson",
  "order": 19,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Run programs",
    "Run with args",
    "Check processes",
    "Wait for processes"
  ],
  "knowledge_refs": [
    "autohotkey/autohotkey-19-running-programs"
  ],
  "prerequisites": [
    "AutoHotkey-18: Error Handling"
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

# AUTOHOTKEY-19-RUNNING-PROGRAMS: Running Programs

## Introduction

Launch apps and control processes. By the end of this lesson you will be able to: Run programs; Run with args; Check processes; Wait for processes.

## Key Concepts

### 1. Run programs

Target: Run programs. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```autohotkey
Run "notepad.exe"
```
### 2. Run with args

Target: Run with args. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```autohotkey
Run "python.exe script.py arg1"
```
### 3. Check processes

Target: Check processes. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```autohotkey
if ProcessExist("notepad.exe")
    MsgBox "running"
```
### 4. Wait for processes

Target: Wait for processes. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```autohotkey
RunWait "cmd.exe /c dir > out.txt"
```

## Practice Questions

1. What is the key idea behind "Running Programs"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Running Programs with analogies and real-world examples"
1. "Show me common mistakes beginners make with Running Programs"
1. "Provide advanced patterns and performance considerations for Running Programs"

## Key Takeaways

- Master the core ideas of Running Programs through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
