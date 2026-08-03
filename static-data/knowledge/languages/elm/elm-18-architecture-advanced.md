---
{
  "title": "Advanced Architecture Patterns",
  "description": "OutMsg and parent-child flows.",
  "type": "lesson",
  "order": 18,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use the OutMsg pattern",
    "Manage complex updates",
    "Structure large apps",
    "Decouple modules"
  ],
  "knowledge_refs": [
    "elm/elm-18-architecture-advanced"
  ],
  "prerequisites": [
    "Elm-17: JavaScript Interop"
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

# ELM-18-ARCHITECTURE-ADVANCED: Advanced Architecture Patterns

## Introduction

OutMsg and parent-child flows. By the end of this lesson you will be able to: Use the OutMsg pattern; Manage complex updates; Structure large apps; Decouple modules.

## Key Concepts

### 1. Use the OutMsg pattern

Target: Use the OutMsg pattern. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```elm
type OutMsg = SaveRequested String
```
### 2. Manage complex updates

Target: Manage complex updates. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```elm
update : Msg -> Model -> ( Model, Cmd Msg, List OutMsg )
```
### 3. Structure large apps

Target: Structure large apps. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```elm
case childResult of
    Just out ->
        case out of
            SaveRequested d -> ( { m | saved = True }, Cmd.none, [] )
```
### 4. Decouple modules

Target: Decouple modules. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```elm
-- keep modules small and message flows explicit
```

## Practice Questions

1. What is the key idea behind "Advanced Architecture Patterns"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Advanced Architecture Patterns with analogies and real-world examples"
1. "Show me common mistakes beginners make with Advanced Architecture Patterns"
1. "Provide advanced patterns and performance considerations for Advanced Architecture Patterns"

## Key Takeaways

- Master the core ideas of Advanced Architecture Patterns through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
