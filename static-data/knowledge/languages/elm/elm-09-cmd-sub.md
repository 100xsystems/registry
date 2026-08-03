---
{
  "title": "Commands and Subscriptions",
  "description": "Side effects handled by the runtime.",
  "type": "lesson",
  "order": 9,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Understand Cmd",
    "Understand Sub",
    "Use Time subscriptions",
    "Fetch data"
  ],
  "knowledge_refs": [
    "elm/elm-09-cmd-sub"
  ],
  "prerequisites": [
    "Elm-08: The Elm Architecture"
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

# ELM-09-CMD-SUB: Commands and Subscriptions

## Introduction

Side effects handled by the runtime. By the end of this lesson you will be able to: Understand Cmd; Understand Sub; Use Time subscriptions; Fetch data.

## Key Concepts

### 1. Understand Cmd

Target: Understand Cmd. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```elm
import Browser
import Html
import Html.Events exposing (onClick)
import Random
```
### 2. Understand Sub

Target: Understand Sub. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```elm
type Msg = NewRandom Int

update : Msg -> Model -> ( Model, Cmd Msg )
update msg model =
    case msg of
        NewRandom n ->
            ( n, Cmd.none )
```
### 3. Use Time subscriptions

Target: Use Time subscriptions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```elm
type Msg = Tick Float

subscriptions : Model -> Sub Msg
subscriptions _ =
    Time.every 1000 Tick
```
### 4. Fetch data

Target: Fetch data. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```elm
rollDice : Cmd Msg
rollDice =
    Random.generate NewRandom (Random.int 1 6)
```

## Practice Questions

1. What is the key idea behind "Commands and Subscriptions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Commands and Subscriptions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Commands and Subscriptions"
1. "Provide advanced patterns and performance considerations for Commands and Subscriptions"

## Key Takeaways

- Master the core ideas of Commands and Subscriptions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
