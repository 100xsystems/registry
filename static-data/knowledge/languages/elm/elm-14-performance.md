---
{
  "title": "Performance",
  "description": "Virtual DOM and optimization.",
  "type": "lesson",
  "order": 14,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Understand virtual DOM",
    "Use keys in lists",
    "Avoid expensive computations",
    "Use Html.Lazy"
  ],
  "knowledge_refs": [
    "elm/elm-14-performance"
  ],
  "prerequisites": [
    "Elm-13: Routing"
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

# ELM-14-PERFORMANCE: Performance

## Introduction

Virtual DOM and optimization. By the end of this lesson you will be able to: Understand virtual DOM; Use keys in lists; Avoid expensive computations; Use Html.Lazy.

## Key Concepts

### 1. Understand virtual DOM

Target: Understand virtual DOM. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```elm
Html.Lazy.lazy viewItem item
```
### 2. Use keys in lists

Target: Use keys in lists. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```elm
List.indexedMap (\i item -> Html.Keyed.node "li" [ (String.fromInt i, viewItem item) ]) items
```
### 3. Avoid expensive computations

Target: Avoid expensive computations. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```elm
view : Model -> Html Msg
view model =
    Html.Lazy.lazy2 viewFor model.filters model.items
```
### 4. Use Html.Lazy

Target: Use Html.Lazy. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```elm
-- measure with elm/browser Debug.todo or performance tools
```

## Practice Questions

1. What is the key idea behind "Performance"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Performance with analogies and real-world examples"
1. "Show me common mistakes beginners make with Performance"
1. "Provide advanced patterns and performance considerations for Performance"

## Key Takeaways

- Master the core ideas of Performance through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
