---
{
  "title": "JSON Decoding",
  "description": "Compose decoders for complex data.",
  "type": "lesson",
  "order": 11,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Decode primitives",
    "Use mapN combinators",
    "Decode lists",
    "Handle optional fields"
  ],
  "knowledge_refs": [
    "elm/elm-11-json"
  ],
  "prerequisites": [
    "Elm-10: HTTP Requests"
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

# ELM-11-JSON: JSON Decoding

## Introduction

Compose decoders for complex data. By the end of this lesson you will be able to: Decode primitives; Use mapN combinators; Decode lists; Handle optional fields.

## Key Concepts

### 1. Decode primitives

Target: Decode primitives. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```elm
import Json.Decode as D

D.string
D.int
D.bool
```
### 2. Use mapN combinators

Target: Use mapN combinators. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```elm
D.map2 (\a b -> ( a, b ))
    (D.field "x" D.int)
    (D.field "y" D.int)
```
### 3. Decode lists

Target: Decode lists. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```elm
D.list D.string
```
### 4. Handle optional fields

Target: Handle optional fields. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```elm
D.maybe (D.field "nickname" D.string)
```

## Practice Questions

1. What is the key idea behind "JSON Decoding"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain JSON Decoding with analogies and real-world examples"
1. "Show me common mistakes beginners make with JSON Decoding"
1. "Provide advanced patterns and performance considerations for JSON Decoding"

## Key Takeaways

- Master the core ideas of JSON Decoding through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
