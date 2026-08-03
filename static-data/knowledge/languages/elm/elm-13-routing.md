---
{
  "title": "Routing",
  "description": "Hash routing and page navigation.",
  "type": "lesson",
  "order": 13,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Set up Browser.application",
    "Define route types",
    "Parse URLs",
    "Navigate with links"
  ],
  "knowledge_refs": [
    "elm/elm-13-routing"
  ],
  "prerequisites": [
    "Elm-12: Forms and User Input"
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

# ELM-13-ROUTING: Routing

## Introduction

Hash routing and page navigation. By the end of this lesson you will be able to: Set up Browser.application; Define route types; Parse URLs; Navigate with links.

## Key Concepts

### 1. Set up Browser.application

Target: Set up Browser.application. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```elm
type Route
    = Home
    | About
    | User String
```
### 2. Define route types

Target: Define route types. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```elm
fromUrl : Url -> Maybe Route
fromUrl url =
    case url.path of
        "/" -> Just Home
        "/about" -> Just About
        _ -> Nothing
```
### 3. Parse URLs

Target: Parse URLs. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```elm
a [ href "/about" ] [ text "About" ]
```
### 4. Navigate with links

Target: Navigate with links. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```elm
Browser.application
    { init = init, update = update, subscriptions = subscriptions, view = view, onUrlRequest = LinkClicked, onUrlChange = UrlChanged }
```

## Practice Questions

1. What is the key idea behind "Routing"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Routing with analogies and real-world examples"
1. "Show me common mistakes beginners make with Routing"
1. "Provide advanced patterns and performance considerations for Routing"

## Key Takeaways

- Master the core ideas of Routing through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
