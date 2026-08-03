---
{
  "title": "Variables and Expressions",
  "description": "Store and manipulate data.",
  "type": "lesson",
  "order": 3,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Declare variables",
    "Concatenate strings",
    "Do arithmetic",
    "Use ternary"
  ],
  "knowledge_refs": [
    "autohotkey/autohotkey-03-variables"
  ],
  "prerequisites": [
    "AutoHotkey-02: Hotkeys and Hotstrings"
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

# AUTOHOTKEY-03-VARIABLES: Variables and Expressions

## Introduction

Store and manipulate data. By the end of this lesson you will be able to: Declare variables; Concatenate strings; Do arithmetic; Use ternary.

## Key Concepts

### 1. Declare variables

Target: Declare variables. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```autohotkey
name := "Ada"
age := 36
MsgBox "Hello, " name
```
### 2. Concatenate strings

Target: Concatenate strings. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```autohotkey
x := 5
y := 10
MsgBox x + y
```
### 3. Do arithmetic

Target: Do arithmetic. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```autohotkey
greeting := "Hello" . " " . "World"
```
### 4. Use ternary

Target: Use ternary. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```autohotkey
result := (x > 5) ? "big" : "small"
```

## Practice Questions

1. What is the key idea behind "Variables and Expressions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Variables and Expressions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Variables and Expressions"
1. "Provide advanced patterns and performance considerations for Variables and Expressions"

## Key Takeaways

- Master the core ideas of Variables and Expressions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
