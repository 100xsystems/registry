---
{
  "title": "Values and Functions",
  "description": "Immutability, functions, and types.",
  "type": "lesson",
  "order": 2,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Write pure functions",
    "Use type annotations",
    "Apply functions with |>",
    "Understand immutability"
  ],
  "knowledge_refs": [
    "elm/elm-02-values"
  ],
  "prerequisites": [
    "Elm-01: Getting Started with Elm"
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

# ELM-02-VALUES: Values and Functions

## Introduction

Immutability, functions, and types. By the end of this lesson you will be able to: Write pure functions; Use type annotations; Apply functions with |>; Understand immutability.

## Key Concepts

### 1. Write pure functions

Target: Write pure functions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```elm
add : Int -> Int -> Int
add a b =
    a + b
```
### 2. Use type annotations

Target: Use type annotations. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```elm
greet : String -> String
greet name =
    "Hello, " ++ name ++ "!"
```
### 3. Apply functions with |>

Target: Apply functions with |>. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```elm
double : Int -> Int
double x = x * 2

main =
    text (String.fromInt (double 21))
```
### 4. Understand immutability

Target: Understand immutability. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```elm
4 |> double |> String.fromInt |> text
```

## Practice Questions

1. What is the key idea behind "Values and Functions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Values and Functions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Values and Functions"
1. "Provide advanced patterns and performance considerations for Values and Functions"

## Key Takeaways

- Master the core ideas of Values and Functions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
