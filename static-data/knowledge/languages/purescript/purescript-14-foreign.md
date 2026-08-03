---
{
  "title": "Foreign Function Interface",
  "description": "Call JavaScript.",
  "type": "lesson",
  "order": 14,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Write FFI files",
    "Import JS functions",
    "Export to JS",
    "Handle unsafe values"
  ],
  "knowledge_refs": [
    "purescript/purescript-14-foreign"
  ],
  "prerequisites": [
    "PureScript-13: Do Notation"
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

# PURESCRIPT-14-FOREIGN: Foreign Function Interface

## Introduction

Call JavaScript. By the end of this lesson you will be able to: Write FFI files; Import JS functions; Export to JS; Handle unsafe values.

## Key Concepts

### 1. Write FFI files

Target: Write FFI files. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```purescript
-- src/Math.js
exports.double = function(x) { return x * 2; };
```
### 2. Import JS functions

Target: Import JS functions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```purescript
foreign import double :: Int -> Int
```
### 3. Export to JS

Target: Export to JS. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```purescript
main = log (show (double 21))
```
### 4. Handle unsafe values

Target: Handle unsafe values. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```purescript
foreign import data Date :: Type
foreign import now :: Effect Date
```

## Practice Questions

1. What is the key idea behind "Foreign Function Interface"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Foreign Function Interface with analogies and real-world examples"
1. "Show me common mistakes beginners make with Foreign Function Interface"
1. "Provide advanced patterns and performance considerations for Foreign Function Interface"

## Key Takeaways

- Master the core ideas of Foreign Function Interface through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
