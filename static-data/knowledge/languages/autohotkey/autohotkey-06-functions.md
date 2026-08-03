---
{
  "title": "Functions",
  "description": "Define and call functions.",
  "type": "lesson",
  "order": 6,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define functions",
    "Pass parameters",
    "Return values",
    "Use defaults"
  ],
  "knowledge_refs": [
    "autohotkey/autohotkey-06-functions"
  ],
  "prerequisites": [
    "AutoHotkey-05: Loops"
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

# AUTOHOTKEY-06-FUNCTIONS: Functions

## Introduction

Define and call functions. By the end of this lesson you will be able to: Define functions; Pass parameters; Return values; Use defaults.

## Key Concepts

### 1. Define functions

Target: Define functions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```autohotkey
Add(a, b)
{
    return a + b
}

MsgBox Add(2, 3)
```
### 2. Pass parameters

Target: Pass parameters. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```autohotkey
Greet(name, excited := false)
{
    return excited ? "HI " name : "hi " name
}
```
### 3. Return values

Target: Return values. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```autohotkey
IsEven(n)
{
    return Mod(n, 2) = 0
}
```
### 4. Use defaults

Target: Use defaults. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```autohotkey
GetConfig(key, def := "")
{
    return IniRead("config.ini", "main", key, def)
}
```

## Practice Questions

1. What is the key idea behind "Functions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Functions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Functions"
1. "Provide advanced patterns and performance considerations for Functions"

## Key Takeaways

- Master the core ideas of Functions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
