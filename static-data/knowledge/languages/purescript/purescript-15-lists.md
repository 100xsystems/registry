---
{
  "title": "Lists and Folds",
  "description": "Linked lists.",
  "type": "lesson",
  "order": 15,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use Data.List",
    "Build lists",
    "Fold lists",
    "Use list functions"
  ],
  "knowledge_refs": [
    "purescript/purescript-15-lists"
  ],
  "prerequisites": [
    "PureScript-14: Foreign Function Interface"
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

# PURESCRIPT-15-LISTS: Lists and Folds

## Introduction

Linked lists. By the end of this lesson you will be able to: Use Data.List; Build lists; Fold lists; Use list functions.

## Key Concepts

### 1. Use Data.List

Target: Use Data.List. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```purescript
import Data.List (List(..), (:))
```
### 2. Build lists

Target: Build lists. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```purescript
nums :: List Int
nums = 1 : 2 : 3 : Nil
```
### 3. Fold lists

Target: Fold lists. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```purescript
sum = foldl (+) 0 nums
```
### 4. Use list functions

Target: Use list functions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```purescript
map (_ * 2) nums
```

## Practice Questions

1. What is the key idea behind "Lists and Folds"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Lists and Folds with analogies and real-world examples"
1. "Show me common mistakes beginners make with Lists and Folds"
1. "Provide advanced patterns and performance considerations for Lists and Folds"

## Key Takeaways

- Master the core ideas of Lists and Folds through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
