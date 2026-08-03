---
{
  "title": "Strings",
  "description": "Fixed, bounded, and unbounded strings.",
  "type": "lesson",
  "order": 6,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use fixed-length strings",
    "Work with Ada.Strings.Unbounded",
    "Concatenate and compare",
    "Convert between string types"
  ],
  "knowledge_refs": [
    "ada/ada-06-strings"
  ],
  "prerequisites": [
    "Ada-05: Control Flow: if, case, loops"
  ],
  "references": [
    {
      "title": "Ada Reference Manual",
      "url": "https://www.adaic.org/resources/add_content/standards/",
      "description": "The official language standard"
    },
    {
      "title": "Learn Ada",
      "url": "https://learn.adacore.com/",
      "description": "AdaCore official interactive course"
    },
    {
      "title": "Ada Programming (Wikibooks)",
      "url": "https://en.wikibooks.org/wiki/Ada_Programming",
      "description": "Community textbook"
    }
  ]
}
---

# ADA-06-STRINGS: Strings

## Introduction

Fixed, bounded, and unbounded strings. By the end of this lesson you will be able to: Use fixed-length strings; Work with Ada.Strings.Unbounded; Concatenate and compare; Convert between string types.

## Key Concepts

### 1. Use fixed-length strings

Target: Use fixed-length strings. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ada
Greeting : String (1 .. 13) := "Hello, World!";
```
### 2. Work with Ada.Strings.Unbounded

Target: Work with Ada.Strings.Unbounded. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ada
with Ada.Strings.Unbounded;
use Ada.Strings.Unbounded;
S : Unbounded_String := To_Unbounded_String ("Hi");
```
### 3. Concatenate and compare

Target: Concatenate and compare. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ada
Full : String := "Ada" & " " & "Lovelace";
```
### 4. Convert between string types

Target: Convert between string types. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ada
with Ada.Strings.Fixed;
Position := Ada.Strings.Fixed.Index (S, "World");
```

## Practice Questions

1. What is the key idea behind "Strings"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Strings with analogies and real-world examples"
1. "Show me common mistakes beginners make with Strings"
1. "Provide advanced patterns and performance considerations for Strings"

## Key Takeaways

- Master the core ideas of Strings through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
