---
{
  "title": "AutoHotkey v2 Best Practices",
  "description": "Modern idioms and structure.",
  "type": "lesson",
  "order": 20,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Structure scripts well",
    "Use classes",
    "Write clean v2 code",
    "Use Strict mode"
  ],
  "knowledge_refs": [
    "autohotkey/autohotkey-20-ahk2"
  ],
  "prerequisites": [
    "AutoHotkey-19: Running Programs"
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

# AUTOHOTKEY-20-AHK2: AutoHotkey v2 Best Practices

## Introduction

Modern idioms and structure. By the end of this lesson you will be able to: Structure scripts well; Use classes; Write clean v2 code; Use Strict mode.

## Key Concepts

### 1. Structure scripts well

Target: Structure scripts well. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```autohotkey
class Calculator
{
    static Add(a, b) => a + b
}

MsgBox Calculator.Add(2, 3)
```
### 2. Use classes

Target: Use classes. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```autohotkey
#Requires AutoHotkey v2.0
```
### 3. Write clean v2 code

Target: Write clean v2 code. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```autohotkey
MyApp()
{
    ; main entry
}

MyApp()
```
### 4. Use Strict mode

Target: Use Strict mode. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```autohotkey
const APP_NAME := "My Tool"
#Requires AutoHotkey v2.0
```

## Practice Questions

1. What is the key idea behind "AutoHotkey v2 Best Practices"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain AutoHotkey v2 Best Practices with analogies and real-world examples"
1. "Show me common mistakes beginners make with AutoHotkey v2 Best Practices"
1. "Provide advanced patterns and performance considerations for AutoHotkey v2 Best Practices"

## Key Takeaways

- Master the core ideas of AutoHotkey v2 Best Practices through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
