---
{
  "title": "Variables and Constants",
  "description": "Object declaration, initialization, and constants.",
  "type": "lesson",
  "order": 3,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Declare typed variables",
    "Initialize values safely",
    "Use constants for safety",
    "Rename with renames"
  ],
  "knowledge_refs": [
    "ada/ada-03-declarations"
  ],
  "prerequisites": [
    "Ada-02: Types and Subtypes"
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

# ADA-03-DECLARATIONS: Variables and Constants

## Introduction

Object declaration, initialization, and constants. By the end of this lesson you will be able to: Declare typed variables; Initialize values safely; Use constants for safety; Rename with renames.

## Key Concepts

### 1. Declare typed variables

Target: Declare typed variables. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ada
count : Integer := 0;
count := count + 1;
```
### 2. Initialize values safely

Target: Initialize values safely. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ada
Pi : constant := 3.14159;
```
### 3. Use constants for safety

Target: Use constants for safety. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ada
Name : constant String := "Ada";
-- String length known at compile time
```
### 4. Rename with renames

Target: Rename with renames. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ada
Full_Name : String renames Name;
```

## Practice Questions

1. What is the key idea behind "Variables and Constants"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Variables and Constants with analogies and real-world examples"
1. "Show me common mistakes beginners make with Variables and Constants"
1. "Provide advanced patterns and performance considerations for Variables and Constants"

## Key Takeaways

- Master the core ideas of Variables and Constants through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
