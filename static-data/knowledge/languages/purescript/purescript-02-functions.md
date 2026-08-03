---
{
  "title": "Functions",
  "description": "Pure functions and type annotations.",
  "type": "lesson",
  "order": 2,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Write pure functions",
    "Annotate types",
    "Use application",
    "Use operator sections"
  ],
  "knowledge_refs": [
    "purescript/purescript-02-functions"
  ],
  "prerequisites": [
    "PureScript-01: Getting Started with PureScript"
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

# PURESCRIPT-02-FUNCTIONS: Functions

## Introduction

Pure functions and type annotations. By the end of this lesson you will be able to: Write pure functions; Annotate types; Use application; Use operator sections.

## Key Concepts

### 1. Write pure functions

Target: Write pure functions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```purescript
add :: Int -> Int -> Int
add a b = a + b
```
### 2. Annotate types

Target: Annotate types. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```purescript
square :: Int -> Int
square x = x * x
```
### 3. Use application

Target: Use application. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```purescript
main = log (show (square 5))
```
### 4. Use operator sections

Target: Use operator sections. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```purescript
double :: Int -> Int
double = (_ * 2)
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
