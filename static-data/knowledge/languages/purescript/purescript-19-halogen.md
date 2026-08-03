---
{
  "title": "UI with Halogen",
  "description": "Type-safe React-like UI.",
  "type": "lesson",
  "order": 19,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Set up Halogen",
    "Define components",
    "Handle actions",
    "Render HTML"
  ],
  "knowledge_refs": [
    "purescript/purescript-19-halogen"
  ],
  "prerequisites": [
    "PureScript-18: Testing"
  ],
  "references": [
    {
      "title": "PureScript Documentation",
      "url": "https://pursuit.purescript.org/",
      "description": "Official package search"
    },
    {
      "title": "PureScript by Example",
      "url": "https://book.purescript.org/",
      "description": "The official book"
    },
    {
      "title": "PureScript Guide",
      "url": "https://github.com/JordanMartinez/purescript-jordans-reference",
      "description": "Community reference"
    }
  ]
}
---

# PURESCRIPT-19-HALOGEN: UI with Halogen

## Introduction

Type-safe React-like UI. By the end of this lesson you will be able to: Set up Halogen; Define components; Handle actions; Render HTML.

## Key Concepts

### 1. Set up Halogen

Target: Set up Halogen. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```purescript
import Halogen as H
import Halogen.HTML as HH
import Halogen.HTML.Events as HE
```
### 2. Define components

Target: Define components. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```purescript
data Action = Increment | Decrement
```
### 3. Handle actions

Target: Handle actions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```purescript
component :: forall q i o m. H.Component q i o m
component = H.mkComponent
  { initialState: const 0
  , render: render
  , eval: H.mkEval H.defaultEval { handleAction = handleAction }
  }
```
### 4. Render HTML

Target: Render HTML. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```purescript
render :: Int -> H.ComponentHTML Action () m
render count =
  HH.div_
    [ HH.text (show count)
    , HH.button [ HE.onClick (const Increment) ] [ HH.text "+" ]
    ]
```

## Practice Questions

1. What is the key idea behind "UI with Halogen"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain UI with Halogen with analogies and real-world examples"
1. "Show me common mistakes beginners make with UI with Halogen"
1. "Provide advanced patterns and performance considerations for UI with Halogen"

## Key Takeaways

- Master the core ideas of UI with Halogen through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
