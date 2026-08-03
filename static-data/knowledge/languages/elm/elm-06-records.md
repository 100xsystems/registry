---
{
  "title": "Records",
  "description": "Structured data with named fields.",
  "type": "lesson",
  "order": 6,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create records",
    "Access and update fields",
    "Use record types",
    "Pattern match records"
  ],
  "knowledge_refs": [
    "elm/elm-06-records"
  ],
  "prerequisites": [
    "Elm-05: Maybe and Result"
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

# ELM-06-RECORDS: Records

## Introduction

Structured data with named fields. By the end of this lesson you will be able to: Create records; Access and update fields; Use record types; Pattern match records.

## Key Concepts

### 1. Create records

Target: Create records. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```elm
type alias Person =
    { name : String, age : Int }

ada = { name = "Ada", age = 36 }
```
### 2. Access and update fields

Target: Access and update fields. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```elm
ada.name
{ ada | age = 37 }
```
### 3. Use record types

Target: Use record types. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```elm
type alias Point = { x : Float, y : Float }
origin : Point
origin = { x = 0, y = 0 }
```
### 4. Pattern match records

Target: Pattern match records. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```elm
describe : Person -> String
describe p =
    p.name ++ " is " ++ String.fromInt p.age
```

## Practice Questions

1. What is the key idea behind "Records"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Records with analogies and real-world examples"
1. "Show me common mistakes beginners make with Records"
1. "Provide advanced patterns and performance considerations for Records"

## Key Takeaways

- Master the core ideas of Records through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
