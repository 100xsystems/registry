---
{
  "title": "JavaScript Interop",
  "description": "Ports and custom elements.",
  "type": "lesson",
  "order": 17,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use ports",
    "Send data to JS",
    "Receive data from JS",
    "Build custom elements"
  ],
  "knowledge_refs": [
    "elm/elm-17-interop"
  ],
  "prerequisites": [
    "Elm-16: Testing with elm-test"
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

# ELM-17-INTEROP: JavaScript Interop

## Introduction

Ports and custom elements. By the end of this lesson you will be able to: Use ports; Send data to JS; Receive data from JS; Build custom elements.

## Key Concepts

### 1. Use ports

Target: Use ports. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```elm
port sendMessage : String -> Cmd msg
port receiveMessage : (String -> msg) -> Sub msg
```
### 2. Send data to JS

Target: Send data to JS. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```elm
module Main exposing (..)
import Html

port module Main exposing (main)
```
### 3. Receive data from JS

Target: Receive data from JS. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```elm
sendMessage "hello from elm"
```
### 4. Build custom elements

Target: Build custom elements. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```elm
app.ports.receiveMessage.subscribe(function (msg) { console.log(msg); });
```

## Practice Questions

1. What is the key idea behind "JavaScript Interop"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain JavaScript Interop with analogies and real-world examples"
1. "Show me common mistakes beginners make with JavaScript Interop"
1. "Provide advanced patterns and performance considerations for JavaScript Interop"

## Key Takeaways

- Master the core ideas of JavaScript Interop through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
