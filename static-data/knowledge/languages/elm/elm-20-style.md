---
{
  "title": "Styling Elm Apps",
  "description": "CSS strategies and elm-ui.",
  "type": "lesson",
  "order": 20,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use plain CSS classes",
    "Use elm-ui layout",
    "Build responsive layouts",
    "Theme applications"
  ],
  "knowledge_refs": [
    "elm/elm-20-style"
  ],
  "prerequisites": [
    "Elm-19: Optimizing Elm Apps"
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

# ELM-20-STYLE: Styling Elm Apps

## Introduction

CSS strategies and elm-ui. By the end of this lesson you will be able to: Use plain CSS classes; Use elm-ui layout; Build responsive layouts; Theme applications.

## Key Concepts

### 1. Use plain CSS classes

Target: Use plain CSS classes. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```elm
div [ class "card" ] [ text "content" ]
```
### 2. Use elm-ui layout

Target: Use elm-ui layout. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```elm
import Element as E

view : Model -> E.Element Msg
view model =
    E.layout [] (E.text "hello")
```
### 3. Build responsive layouts

Target: Build responsive layouts. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```elm
E.row [ E.spacing 10 ] [ E.text "a", E.text "b" ]
```
### 4. Theme applications

Target: Theme applications. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```elm
E.column [ E.padding 20 ] [ header, body ]
```

## Practice Questions

1. What is the key idea behind "Styling Elm Apps"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Styling Elm Apps with analogies and real-world examples"
1. "Show me common mistakes beginners make with Styling Elm Apps"
1. "Provide advanced patterns and performance considerations for Styling Elm Apps"

## Key Takeaways

- Master the core ideas of Styling Elm Apps through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
