---
{
  "title": "Getting Started with Elm",
  "description": "Install the compiler and build a first app.",
  "type": "lesson",
  "order": 1,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Install Elm",
    "Write hello world with Html",
    "Compile with elm make",
    "Run elm reactor"
  ],
  "knowledge_refs": [
    "elm/elm-01-getting-started"
  ],
  "prerequisites": [
    "None — this is the entry point"
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

# ELM-01-GETTING-STARTED: Getting Started with Elm

## Introduction

Install the compiler and build a first app. By the end of this lesson you will be able to: Install Elm; Write hello world with Html; Compile with elm make; Run elm reactor.

## Key Concepts

### 1. Install Elm

Target: Install Elm. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```elm
module Main exposing (main)

import Html

main =
    Html.text "Hello, World!"
```
### 2. Write hello world with Html

Target: Write hello world with Html. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```elm
elm make src/Main.elm --output=main.js
```
### 3. Compile with elm make

Target: Compile with elm make. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```elm
module Main exposing (main)

import Html exposing (text)

main = text "hello"
```
### 4. Run elm reactor

Target: Run elm reactor. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```elm
elm reactor   # open http://localhost:8000
```

## Practice Questions

1. What is the key idea behind "Getting Started with Elm"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with Elm with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with Elm"
1. "Provide advanced patterns and performance considerations for Getting Started with Elm"

## Key Takeaways

- Master the core ideas of Getting Started with Elm through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
