---
{
  "title": "Either",
  "description": "Typed errors.",
  "type": "lesson",
  "order": 8,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use Either type",
    "Pattern match Left/Right",
    "Use Either as result",
    "Map over Right"
  ],
  "knowledge_refs": [
    "purescript/purescript-08-either"
  ],
  "prerequisites": [
    "PureScript-07: Maybe"
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

# PURESCRIPT-08-EITHER: Either

## Introduction

Typed errors. By the end of this lesson you will be able to: Use Either type; Pattern match Left/Right; Use Either as result; Map over Right.

## Key Concepts

### 1. Use Either type

Target: Use Either type. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```purescript
import Data.Either (Either(..))
```
### 2. Pattern match Left/Right

Target: Pattern match Left/Right. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```purescript
divide :: Int -> Int -> Either String Int
divide _ 0 = Left "division by zero"
divide a b = Right (a / b)
```
### 3. Use Either as result

Target: Use Either as result. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```purescript
case divide 10 2 of
  Right n -> log (show n)
  Left e -> log e
```
### 4. Map over Right

Target: Map over Right. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```purescript
map (_ * 2) (Right 21)
```

## Practice Questions

1. What is the key idea behind "Either"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Either with analogies and real-world examples"
1. "Show me common mistakes beginners make with Either"
1. "Provide advanced patterns and performance considerations for Either"

## Key Takeaways

- Master the core ideas of Either through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
