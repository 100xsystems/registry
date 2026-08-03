---
{
  "title": "Custom Types",
  "description": "Enums and tagged unions.",
  "type": "lesson",
  "order": 7,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define custom types",
    "Pattern match variants",
    "Carry data in variants",
    "Model states with types"
  ],
  "knowledge_refs": [
    "elm/elm-07-union-types"
  ],
  "prerequisites": [
    "Elm-06: Records"
  ],
  "references": [
    {
      "title": "Elm Guide",
      "url": "https://guide.elm-lang.org/",
      "description": "Official guide — the best way to start"
    },
    {
      "title": "Elm Packages",
      "url": "https://package.elm-lang.org/",
      "description": "Package registry"
    },
    {
      "title": "Elm Syntax",
      "url": "https://elm-lang.org/docs/syntax",
      "description": "Language syntax reference"
    },
    {
      "title": "Elm Discourse",
      "url": "https://discourse.elm-lang.org/",
      "description": "Community forum"
    }
  ]
}
---

# ELM-07-UNION-TYPES: Custom Types

## Introduction

Enums and tagged unions. By the end of this lesson you will be able to: Define custom types; Pattern match variants; Carry data in variants; Model states with types.

## Key Concepts

### 1. Define custom types

Target: Define custom types. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```elm
type Color
    = Red
    | Green
    | Blue
```
### 2. Pattern match variants

Target: Pattern match variants. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```elm
type Shape
    = Circle Float
    | Square Float

area : Shape -> Float
area shape =
    case shape of
        Circle r -> 3.14159 * r * r
        Square s -> s * s
```
### 3. Carry data in variants

Target: Carry data in variants. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```elm
type State
    = Loading
    | Loaded (List String)
    | Failed String
```
### 4. Model states with types

Target: Model states with types. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```elm
type Direction = North | South | East | West

turn : Direction -> Direction
turn d =
    case d of
        North -> East
        East -> South
        South -> West
        West -> North
```

## Practice Questions

1. What is the key idea behind "Custom Types"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Custom Types with analogies and real-world examples"
1. "Show me common mistakes beginners make with Custom Types"
1. "Provide advanced patterns and performance considerations for Custom Types"

## Key Takeaways

- Master the core ideas of Custom Types through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
