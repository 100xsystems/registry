---
{
  "title": "Reusable Components",
  "description": "Compose modules and components.",
  "type": "lesson",
  "order": 15,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Split code into modules",
    "Pass callbacks down",
    "Lift state up",
    "Build reusable views"
  ],
  "knowledge_refs": [
    "elm/elm-15-reusable"
  ],
  "prerequisites": [
    "Elm-14: Performance"
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

# ELM-15-REUSABLE: Reusable Components

## Introduction

Compose modules and components. By the end of this lesson you will be able to: Split code into modules; Pass callbacks down; Lift state up; Build reusable views.

## Key Concepts

### 1. Split code into modules

Target: Split code into modules. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```elm
module Counter exposing (Msg, view, update)
```
### 2. Pass callbacks down

Target: Pass callbacks down. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```elm
type Msg = Increment | Decrement
```
### 3. Lift state up

Target: Lift state up. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```elm
view : Int -> (Msg -> parentMsg) -> Html parentMsg
view count toParent =
    button [ onClick (toParent Increment) ] [ text (String.fromInt count) ]
```
### 4. Build reusable views

Target: Build reusable views. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```elm
type alias ParentMsg = ChildMsg | Reset
```

## Practice Questions

1. What is the key idea behind "Reusable Components"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Reusable Components with analogies and real-world examples"
1. "Show me common mistakes beginners make with Reusable Components"
1. "Provide advanced patterns and performance considerations for Reusable Components"

## Key Takeaways

- Master the core ideas of Reusable Components through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
