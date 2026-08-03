---
{
  "title": "Do Notation",
  "description": "Sequence computations.",
  "type": "lesson",
  "order": 13,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use do blocks",
    "Bind with <-",
    "Use let in do",
    "Sequence IO"
  ],
  "knowledge_refs": [
    "purescript/purescript-13-do-notation"
  ],
  "prerequisites": [
    "PureScript-12: Effects"
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

# PURESCRIPT-13-DO-NOTATION: Do Notation

## Introduction

Sequence computations. By the end of this lesson you will be able to: Use do blocks; Bind with <-; Use let in do; Sequence IO.

## Key Concepts

### 1. Use do blocks

Target: Use do blocks. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```purescript
main = do
  log "starting"
  log "done"
```
### 2. Bind with <-

Target: Bind with <-. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```purescript
main = do
  x <- pure 5
  log (show (x * 2))
```
### 3. Use let in do

Target: Use let in do. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```purescript
main = do
  let name = "Ada"
  log ("Hello, " <> name)
```
### 4. Sequence IO

Target: Sequence IO. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```purescript
greet :: Effect Unit
greet = do
  log "Hello!"
  log "Again!"
```

## Practice Questions

1. What is the key idea behind "Do Notation"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Do Notation with analogies and real-world examples"
1. "Show me common mistakes beginners make with Do Notation"
1. "Provide advanced patterns and performance considerations for Do Notation"

## Key Takeaways

- Master the core ideas of Do Notation through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
