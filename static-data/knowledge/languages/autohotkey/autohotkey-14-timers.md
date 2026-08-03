---
{
  "title": "Timers",
  "description": "Scheduled actions.",
  "type": "lesson",
  "order": 14,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Set timers",
    "Repeat actions",
    "Cancel timers",
    "Use SetTimer"
  ],
  "knowledge_refs": [
    "autohotkey/autohotkey-14-timers"
  ],
  "prerequisites": [
    "AutoHotkey-13: String Functions"
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

# AUTOHOTKEY-14-TIMERS: Timers

## Introduction

Scheduled actions. By the end of this lesson you will be able to: Set timers; Repeat actions; Cancel timers; Use SetTimer.

## Key Concepts

### 1. Set timers

Target: Set timers. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```autohotkey
SetTimer Check, 5000

Check()
{
    MsgBox "5 seconds passed"
}
```
### 2. Repeat actions

Target: Repeat actions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```autohotkey
SetTimer Flash, 1000

Flash()
{
    MsgBox "tick"
}
```
### 3. Cancel timers

Target: Cancel timers. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```autohotkey
SetTimer Check, 0   ; disable
```
### 4. Use SetTimer

Target: Use SetTimer. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```autohotkey
SetTimer () => MsgBox "periodic", 3000
```

## Practice Questions

1. What is the key idea behind "Timers"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Timers with analogies and real-world examples"
1. "Show me common mistakes beginners make with Timers"
1. "Provide advanced patterns and performance considerations for Timers"

## Key Takeaways

- Master the core ideas of Timers through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
