---
{
  "title": "Loops",
  "description": "Iteration and repetition.",
  "type": "lesson",
  "order": 5,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use Loop count",
    "Use While",
    "Use For over objects",
    "Break and continue"
  ],
  "knowledge_refs": [
    "autohotkey/autohotkey-05-loops"
  ],
  "prerequisites": [
    "AutoHotkey-04: Control Flow"
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

# AUTOHOTKEY-05-LOOPS: Loops

## Introduction

Iteration and repetition. By the end of this lesson you will be able to: Use Loop count; Use While; Use For over objects; Break and continue.

## Key Concepts

### 1. Use Loop count

Target: Use Loop count. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```autohotkey
Loop 5
{
    MsgBox "Iteration " A_Index
}
```
### 2. Use While

Target: Use While. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```autohotkey
i := 0
while (i < 5)
{
    i++
    MsgBox i
}
```
### 3. Use For over objects

Target: Use For over objects. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```autohotkey
for fruit in ["apple", "banana"]
    MsgBox fruit
```
### 4. Break and continue

Target: Break and continue. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```autohotkey
Loop 10
{
    if (A_Index = 5)
        break
    if (A_Index = 3)
        continue
}
```

## Practice Questions

1. What is the key idea behind "Loops"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Loops with analogies and real-world examples"
1. "Show me common mistakes beginners make with Loops"
1. "Provide advanced patterns and performance considerations for Loops"

## Key Takeaways

- Master the core ideas of Loops through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
