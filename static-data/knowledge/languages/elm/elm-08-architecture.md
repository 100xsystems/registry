---
{
  "title": "The Elm Architecture",
  "description": "Model, update, and view.",
  "type": "lesson",
  "order": 8,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define the Model",
    "Write update with messages",
    "Render with view",
    "Wire up init"
  ],
  "knowledge_refs": [
    "elm/elm-08-architecture"
  ],
  "prerequisites": [
    "Elm-07: Custom Types"
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

# ELM-08-ARCHITECTURE: The Elm Architecture

## Introduction

Model, update, and view. By the end of this lesson you will be able to: Define the Model; Write update with messages; Render with view; Wire up init.

## Key Concepts

### 1. Define the Model

Target: Define the Model. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```elm
type Msg = Increment | Decrement

type alias Model = Int

update : Msg -> Model -> Model
update msg model =
    case msg of
        Increment -> model + 1
        Decrement -> model - 1
```
### 2. Write update with messages

Target: Write update with messages. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```elm
view : Model -> Html Msg
view model =
    div []
        [ button [ onClick Decrement ] [ text "-" ]
        , text (String.fromInt model)
        , button [ onClick Increment ] [ text "+" ]
        ]
```
### 3. Render with view

Target: Render with view. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```elm
main : Program () Model Msg
main =
    Browser.sandbox
        { init = 0
        , update = update
        , view = view
        }
```
### 4. Wire up init

Target: Wire up init. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```elm
init : Model
init = 0
```

## Practice Questions

1. What is the key idea behind "The Elm Architecture"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain The Elm Architecture with analogies and real-world examples"
1. "Show me common mistakes beginners make with The Elm Architecture"
1. "Provide advanced patterns and performance considerations for The Elm Architecture"

## Key Takeaways

- Master the core ideas of The Elm Architecture through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
