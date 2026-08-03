---
{
  "title": "HTTP Requests",
  "description": "Fetch data from APIs.",
  "type": "lesson",
  "order": 10,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use Http module",
    "Decode JSON",
    "Handle loading states",
    "Show errors"
  ],
  "knowledge_refs": [
    "elm/elm-10-http"
  ],
  "prerequisites": [
    "Elm-09: Commands and Subscriptions"
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

# ELM-10-HTTP: HTTP Requests

## Introduction

Fetch data from APIs. By the end of this lesson you will be able to: Use Http module; Decode JSON; Handle loading states; Show errors.

## Key Concepts

### 1. Use Http module

Target: Use Http module. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```elm
import Http
import Json.Decode as Decode
```
### 2. Decode JSON

Target: Decode JSON. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```elm
getUser : Cmd Msg
getUser =
    Http.get
        { url = "https://api.example.com/user"
        , expect = Http.expectJson GotUser userDecoder
        }
```
### 3. Handle loading states

Target: Handle loading states. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```elm
userDecoder : Decode.Decoder User
userDecoder =
    Decode.map2 User
        (Decode.field "name" Decode.string)
        (Decode.field "age" Decode.int)
```
### 4. Show errors

Target: Show errors. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```elm
type Msg = GotUser (Result Http.Error User)
```

## Practice Questions

1. What is the key idea behind "HTTP Requests"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain HTTP Requests with analogies and real-world examples"
1. "Show me common mistakes beginners make with HTTP Requests"
1. "Provide advanced patterns and performance considerations for HTTP Requests"

## Key Takeaways

- Master the core ideas of HTTP Requests through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
