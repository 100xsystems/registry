---
{
  "title": "Maybe",
  "description": "Optional values.",
  "type": "lesson",
  "order": 7,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use Maybe type",
    "Pattern match Just/Nothing",
    "Use map on Maybe",
    "Use fromMaybe"
  ],
  "knowledge_refs": [
    "purescript/purescript-07-maybe"
  ],
  "prerequisites": [
    "PureScript-06: Records"
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

# PURESCRIPT-07-MAYBE: Maybe

## Introduction

Optional values. By the end of this lesson you will be able to: Use Maybe type; Pattern match Just/Nothing; Use map on Maybe; Use fromMaybe.

## Key Concepts

### 1. Use Maybe type

Target: Use Maybe type. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```purescript
import Data.Maybe (Maybe(..))
```
### 2. Pattern match Just/Nothing

Target: Pattern match Just/Nothing. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```purescript
safeHead :: Array Int -> Maybe Int
safeHead [] = Nothing
safeHead (x : _) = Just x
```
### 3. Use map on Maybe

Target: Use map on Maybe. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```purescript
main = log (show (safeHead [1, 2]))
```
### 4. Use fromMaybe

Target: Use fromMaybe. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```purescript
import Data.Maybe (fromMaybe)
value = fromMaybe 0 (safeHead [])
```

## Practice Questions

1. What is the key idea behind "Maybe"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Maybe with analogies and real-world examples"
1. "Show me common mistakes beginners make with Maybe"
1. "Provide advanced patterns and performance considerations for Maybe"

## Key Takeaways

- Master the core ideas of Maybe through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
