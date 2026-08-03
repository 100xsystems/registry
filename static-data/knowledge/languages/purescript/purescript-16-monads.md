---
{
  "title": "Monads",
  "description": "The Monad type class.",
  "type": "lesson",
  "order": 16,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Understand Monad",
    "Use bind and pure",
    "Chain computations",
    "Use do with Monads"
  ],
  "knowledge_refs": [
    "purescript/purescript-16-monads"
  ],
  "prerequisites": [
    "PureScript-15: Lists and Folds"
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

# PURESCRIPT-16-MONADS: Monads

## Introduction

The Monad type class. By the end of this lesson you will be able to: Understand Monad; Use bind and pure; Chain computations; Use do with Monads.

## Key Concepts

### 1. Understand Monad

Target: Understand Monad. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```purescript
import Prelude (bind, pure)
```
### 2. Use bind and pure

Target: Use bind and pure. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```purescript
compute :: Maybe Int
compute = do
  a <- Just 5
  b <- Just 3
  pure (a * b)
```
### 3. Chain computations

Target: Chain computations. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```purescript
eitherCompute :: Either String Int
eitherCompute = do
  a <- Right 5
  b <- Right 3
  pure (a + b)
```
### 4. Use do with Monads

Target: Use do with Monads. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```purescript
import Control.Monad.Except (ExceptT, lift)
```

## Practice Questions

1. What is the key idea behind "Monads"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Monads with analogies and real-world examples"
1. "Show me common mistakes beginners make with Monads"
1. "Provide advanced patterns and performance considerations for Monads"

## Key Takeaways

- Master the core ideas of Monads through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
