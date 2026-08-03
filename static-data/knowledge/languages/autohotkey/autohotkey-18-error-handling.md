---
{
  "title": "Error Handling",
  "description": "Try, catch, and validation.",
  "type": "lesson",
  "order": 18,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use try/catch",
    "Throw errors",
    "Check ErrorLevel",
    "Validate inputs"
  ],
  "knowledge_refs": [
    "autohotkey/autohotkey-18-error-handling"
  ],
  "prerequisites": [
    "AutoHotkey-17: Configuration and JSON"
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

# AUTOHOTKEY-18-ERROR-HANDLING: Error Handling

## Introduction

Try, catch, and validation. By the end of this lesson you will be able to: Use try/catch; Throw errors; Check ErrorLevel; Validate inputs.

## Key Concepts

### 1. Use try/catch

Target: Use try/catch. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```autohotkey
try
{
    value := FileRead("missing.txt")
}
catch Error as e
{
    MsgBox "Error: " e.Message
}
```
### 2. Throw errors

Target: Throw errors. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```autohotkey
throw ValueError("Bad input")
```
### 3. Check ErrorLevel

Target: Check ErrorLevel. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```autohotkey
FileRead "data.txt"
if (ErrorLevel)
    MsgBox "read failed"
```
### 4. Validate inputs

Target: Validate inputs. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```autohotkey
if not IsNumber(input)
    MsgBox "not a number"
```

## Practice Questions

1. What is the key idea behind "Error Handling"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Error Handling with analogies and real-world examples"
1. "Show me common mistakes beginners make with Error Handling"
1. "Provide advanced patterns and performance considerations for Error Handling"

## Key Takeaways

- Master the core ideas of Error Handling through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
