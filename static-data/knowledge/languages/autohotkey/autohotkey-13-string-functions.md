---
{
  "title": "String Functions",
  "description": "Manipulate and transform text.",
  "type": "lesson",
  "order": 13,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use StrSplit",
    "Use StrReplace",
    "Use SubStr",
    "Use RegExMatch"
  ],
  "knowledge_refs": [
    "autohotkey/autohotkey-13-string-functions"
  ],
  "prerequisites": [
    "AutoHotkey-12: Arrays and Objects"
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

# AUTOHOTKEY-13-STRING-FUNCTIONS: String Functions

## Introduction

Manipulate and transform text. By the end of this lesson you will be able to: Use StrSplit; Use StrReplace; Use SubStr; Use RegExMatch.

## Key Concepts

### 1. Use StrSplit

Target: Use StrSplit. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```autohotkey
parts := StrSplit("a,b,c", ",")
MsgBox parts[2]
```
### 2. Use StrReplace

Target: Use StrReplace. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```autohotkey
MsgBox StrReplace("hello world", "o", "0")
```
### 3. Use SubStr

Target: Use SubStr. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```autohotkey
MsgBox SubStr("Hello", 2, 3)
```
### 4. Use RegExMatch

Target: Use RegExMatch. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```autohotkey
match := RegExMatch("hello 123", "\d+", &found)
if (match)
    MsgBox found[]
```

## Practice Questions

1. What is the key idea behind "String Functions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain String Functions with analogies and real-world examples"
1. "Show me common mistakes beginners make with String Functions"
1. "Provide advanced patterns and performance considerations for String Functions"

## Key Takeaways

- Master the core ideas of String Functions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
