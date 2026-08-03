---
{
  "title": "Effects",
  "description": "Effect type for side effects.",
  "type": "lesson",
  "order": 12,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Understand Effect",
    "Run effects in main",
    "Sequence effects",
    "Use Effect.Console"
  ],
  "knowledge_refs": [
    "purescript/purescript-12-effect"
  ],
  "prerequisites": [
    "PureScript-11: Custom Data Types"
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

# PURESCRIPT-12-EFFECT: Effects

## Introduction

Effect type for side effects. By the end of this lesson you will be able to: Understand Effect; Run effects in main; Sequence effects; Use Effect.Console.

## Key Concepts

### 1. Understand Effect

Target: Understand Effect. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```purescript
import Effect (Effect)
import Effect.Console (log)
```
### 2. Run effects in main

Target: Run effects in main. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```purescript
main :: Effect Unit
main = do
  log "line one"
  log "line two"
```
### 3. Sequence effects

Target: Sequence effects. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```purescript
main = log (show (1 + 1))
```
### 4. Use Effect.Console

Target: Use Effect.Console. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```purescript
import Effect.Random (random)
main = do
  r <- random
  log (show r)
```

## Practice Questions

1. What is the key idea behind "Effects"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Effects with analogies and real-world examples"
1. "Show me common mistakes beginners make with Effects"
1. "Provide advanced patterns and performance considerations for Effects"

## Key Takeaways

- Master the core ideas of Effects through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
