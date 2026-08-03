---
{
  "title": "Maybe and Result",
  "description": "Handle missing values safely.",
  "type": "lesson",
  "order": 5,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Understand Maybe",
    "Pattern match on Maybe",
    "Use Result for errors",
    "Chain with andThen"
  ],
  "knowledge_refs": [
    "elm/elm-05-maybe"
  ],
  "prerequisites": [
    "Elm-04: Lists"
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

# ELM-05-MAYBE: Maybe and Result

## Introduction

Handle missing values safely. By the end of this lesson you will be able to: Understand Maybe; Pattern match on Maybe; Use Result for errors; Chain with andThen.

## Key Concepts

### 1. Understand Maybe

Target: Understand Maybe. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```elm
parse : String -> Maybe Int
parse s =
    String.toInt s
```
### 2. Pattern match on Maybe

Target: Pattern match on Maybe. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```elm
case parse "42" of
    Just n -> text ("number: " ++ String.fromInt n)
    Nothing -> text "not a number"
```
### 3. Use Result for errors

Target: Use Result for errors. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```elm
divide : Float -> Float -> Result String Float
divide _ 0 =
    Err "divide by zero"
divide a b =
    Ok (a / b)
```
### 4. Chain with andThen

Target: Chain with andThen. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```elm
String.toInt "5"
    |> Maybe.andThen (\n -> String.toInt (String.fromInt (n * 2)))
```

## Practice Questions

1. What is the key idea behind "Maybe and Result"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Maybe and Result with analogies and real-world examples"
1. "Show me common mistakes beginners make with Maybe and Result"
1. "Provide advanced patterns and performance considerations for Maybe and Result"

## Key Takeaways

- Master the core ideas of Maybe and Result through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
