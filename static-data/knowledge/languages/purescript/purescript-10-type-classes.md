---
{
  "title": "Type Classes",
  "description": "Polymorphic behavior.",
  "type": "lesson",
  "order": 10,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Understand type classes",
    "Use Show and Eq",
    "Define instances",
    "Use class constraints"
  ],
  "knowledge_refs": [
    "purescript/purescript-10-type-classes"
  ],
  "prerequisites": [
    "PureScript-09: Pattern Matching"
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

# PURESCRIPT-10-TYPE-CLASSES: Type Classes

## Introduction

Polymorphic behavior. By the end of this lesson you will be able to: Understand type classes; Use Show and Eq; Define instances; Use class constraints.

## Key Concepts

### 1. Understand type classes

Target: Understand type classes. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```purescript
import Prelude (class Show, show)
```
### 2. Use Show and Eq

Target: Use Show and Eq. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```purescript
show 42
show "hi"
```
### 3. Define instances

Target: Define instances. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```purescript
data Color = Red | Green | Blue

instance showColor :: Show Color where
  show Red = "red"
  show Green = "green"
  show Blue = "blue"
```
### 4. Use class constraints

Target: Use class constraints. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```purescript
instance eqColor :: Eq Color where
  eq Red Red = true
  eq Green Green = true
  eq Blue Blue = true
  eq _ _ = false
```

## Practice Questions

1. What is the key idea behind "Type Classes"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Type Classes with analogies and real-world examples"
1. "Show me common mistakes beginners make with Type Classes"
1. "Provide advanced patterns and performance considerations for Type Classes"

## Key Takeaways

- Master the core ideas of Type Classes through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
