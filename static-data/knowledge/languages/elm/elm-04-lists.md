---
{
  "title": "Lists",
  "description": "Immutable lists and List module.",
  "type": "lesson",
  "order": 4,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Create lists",
    "Cons with ::",
    "Use List.map and filter",
    "Fold with foldl"
  ],
  "knowledge_refs": [
    "elm/elm-04-lists"
  ],
  "prerequisites": [
    "Elm-03: Numbers and Strings"
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

# ELM-04-LISTS: Lists

## Introduction

Immutable lists and List module. By the end of this lesson you will be able to: Create lists; Cons with ::; Use List.map and filter; Fold with foldl.

## Key Concepts

### 1. Create lists

Target: Create lists. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```elm
nums = [1, 2, 3]
first = 0 :: nums
```
### 2. Cons with ::

Target: Cons with ::. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```elm
List.map (\n -> n * 2) [1, 2, 3]
```
### 3. Use List.map and filter

Target: Use List.map and filter. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```elm
List.filter (\n -> n > 2) [1, 2, 3, 4]
```
### 4. Fold with foldl

Target: Fold with foldl. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```elm
List.foldl (+) 0 [1, 2, 3]
```

## Practice Questions

1. What is the key idea behind "Lists"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Lists with analogies and real-world examples"
1. "Show me common mistakes beginners make with Lists"
1. "Provide advanced patterns and performance considerations for Lists"

## Key Takeaways

- Master the core ideas of Lists through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
