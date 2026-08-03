---
{
  "title": "Arrays",
  "description": "Homogeneous collections.",
  "type": "lesson",
  "order": 5,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create arrays",
    "Use Data.Array functions",
    "Map and filter",
    "Fold arrays"
  ],
  "knowledge_refs": [
    "purescript/purescript-05-arrays"
  ],
  "prerequisites": [
    "PureScript-04: Let and Where"
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

# PURESCRIPT-05-ARRAYS: Arrays

## Introduction

Homogeneous collections. By the end of this lesson you will be able to: Create arrays; Use Data.Array functions; Map and filter; Fold arrays.

## Key Concepts

### 1. Create arrays

Target: Create arrays. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```purescript
import Data.Array (map, filter, foldl)
```
### 2. Use Data.Array functions

Target: Use Data.Array functions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```purescript
nums :: Array Int
nums = [1, 2, 3]
```
### 3. Map and filter

Target: Map and filter. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```purescript
doubled = map (_ * 2) nums
```
### 4. Fold arrays

Target: Fold arrays. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```purescript
sum = foldl (+) 0 nums
```

## Practice Questions

1. What is the key idea behind "Arrays"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Arrays with analogies and real-world examples"
1. "Show me common mistakes beginners make with Arrays"
1. "Provide advanced patterns and performance considerations for Arrays"

## Key Takeaways

- Master the core ideas of Arrays through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
