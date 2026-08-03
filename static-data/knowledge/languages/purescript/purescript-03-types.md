---
{
  "title": "Types",
  "description": "Primitive types and aliases.",
  "type": "lesson",
  "order": 3,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use Int, Number, String",
    "Use Boolean",
    "Define type aliases",
    "Use unit"
  ],
  "knowledge_refs": [
    "purescript/purescript-03-types"
  ],
  "prerequisites": [
    "PureScript-02: Functions"
  ],
  "references": [
    {
      "title": "PureScript Documentation",
      "url": "https://pursuit.purescript.org/",
      "description": "Official package search"
    },
    {
      "title": "PureScript by Example",
      "url": "https://book.purescript.org/",
      "description": "The official book"
    },
    {
      "title": "PureScript Guide",
      "url": "https://github.com/JordanMartinez/purescript-jordans-reference",
      "description": "Community reference"
    }
  ]
}
---

# PURESCRIPT-03-TYPES: Types

## Introduction

Primitive types and aliases. By the end of this lesson you will be able to: Use Int, Number, String; Use Boolean; Define type aliases; Use unit.

## Key Concepts

### 1. Use Int, Number, String

Target: Use Int, Number, String. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```purescript
x :: Int
x = 42
```
### 2. Use Boolean

Target: Use Boolean. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```purescript
pi :: Number
pi = 3.14159
```
### 3. Define type aliases

Target: Define type aliases. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```purescript
type Name = String
name :: Name
name = "Ada"
```
### 4. Use unit

Target: Use unit. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```purescript
type Point = { x :: Number, y :: Number }
```

## Practice Questions

1. What is the key idea behind "Types"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Types with analogies and real-world examples"
1. "Show me common mistakes beginners make with Types"
1. "Provide advanced patterns and performance considerations for Types"

## Key Takeaways

- Master the core ideas of Types through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
