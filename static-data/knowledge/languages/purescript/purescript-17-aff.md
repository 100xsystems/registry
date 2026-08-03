---
{
  "title": "Asynchronous with Aff",
  "description": "Async programming.",
  "type": "lesson",
  "order": 17,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Understand Aff",
    "Delay and timeouts",
    "Run parallel effects",
    "Handle errors"
  ],
  "knowledge_refs": [
    "purescript/purescript-17-aff"
  ],
  "prerequisites": [
    "PureScript-16: Monads"
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

# PURESCRIPT-17-AFF: Asynchronous with Aff

## Introduction

Async programming. By the end of this lesson you will be able to: Understand Aff; Delay and timeouts; Run parallel effects; Handle errors.

## Key Concepts

### 1. Understand Aff

Target: Understand Aff. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```purescript
import Effect.Aff (Aff, delay, launchAff_)
```
### 2. Delay and timeouts

Target: Delay and timeouts. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```purescript
import Data.Time.Duration (Milliseconds(..))
```
### 3. Run parallel effects

Target: Run parallel effects. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```purescript
main = launchAff_ do
  delay (Milliseconds 1000.0)
  log "after 1s"
```
### 4. Handle errors

Target: Handle errors. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```purescript
import Effect.Aff (parallel)
main = launchAff_ do
  result <- parallel (pure 42)
  log (show result)
```

## Practice Questions

1. What is the key idea behind "Asynchronous with Aff"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Asynchronous with Aff with analogies and real-world examples"
1. "Show me common mistakes beginners make with Asynchronous with Aff"
1. "Provide advanced patterns and performance considerations for Asynchronous with Aff"

## Key Takeaways

- Master the core ideas of Asynchronous with Aff through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
