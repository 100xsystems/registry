---
{
  "title": "Let and Where",
  "description": "Local bindings.",
  "type": "lesson",
  "order": 4,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use let bindings",
    "Use where clauses",
    "Shadow names",
    "Structure helpers"
  ],
  "knowledge_refs": [
    "purescript/purescript-04-let-where"
  ],
  "prerequisites": [
    "PureScript-03: Types"
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

# PURESCRIPT-04-LET-WHERE: Let and Where

## Introduction

Local bindings. By the end of this lesson you will be able to: Use let bindings; Use where clauses; Shadow names; Structure helpers.

## Key Concepts

### 1. Use let bindings

Target: Use let bindings. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```purescript
area :: Number -> Number
area r =
  let pi = 3.14159
  in pi * r * r
```
### 2. Use where clauses

Target: Use where clauses. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```purescript
volume :: Number -> Number
volume r = area r * r
  where
  area r = pi * r * r
  pi = 3.14159
```
### 3. Shadow names

Target: Shadow names. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```purescript
main = log (show (area 2.0))
```
### 4. Structure helpers

Target: Structure helpers. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```purescript
f x = a + b
  where
  a = x * 2
  b = x + 1
```

## Practice Questions

1. What is the key idea behind "Let and Where"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Let and Where with analogies and real-world examples"
1. "Show me common mistakes beginners make with Let and Where"
1. "Provide advanced patterns and performance considerations for Let and Where"

## Key Takeaways

- Master the core ideas of Let and Where through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
