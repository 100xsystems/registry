---
{
  "title": "Configuration and JSON",
  "description": "Persist settings.",
  "type": "lesson",
  "order": 17,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Read/write INI files",
    "Parse JSON",
    "Save settings",
    "Use registry"
  ],
  "knowledge_refs": [
    "autohotkey/autohotkey-17-json-ini"
  ],
  "prerequisites": [
    "AutoHotkey-16: Image and Pixel Search"
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

# AUTOHOTKEY-17-JSON-INI: Configuration and JSON

## Introduction

Persist settings. By the end of this lesson you will be able to: Read/write INI files; Parse JSON; Save settings; Use registry.

## Key Concepts

### 1. Read/write INI files

Target: Read/write INI files. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```autohotkey
IniWrite "value", "config.ini", "section", "key"
value := IniRead("config.ini", "section", "key")
```
### 2. Parse JSON

Target: Parse JSON. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```autohotkey
import json

; via external JSON lib
parsed := JSON.parse(text)
```
### 3. Save settings

Target: Save settings. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```autohotkey
RegWrite "value", "REG_SZ", "HKCU\Software\MyApp", "Setting"
val := RegRead("HKCU\Software\MyApp", "Setting")
```
### 4. Use registry

Target: Use registry. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```autohotkey
A_WorkingDir := "C:\Users\me"
```

## Practice Questions

1. What is the key idea behind "Configuration and JSON"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Configuration and JSON with analogies and real-world examples"
1. "Show me common mistakes beginners make with Configuration and JSON"
1. "Provide advanced patterns and performance considerations for Configuration and JSON"

## Key Takeaways

- Master the core ideas of Configuration and JSON through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
