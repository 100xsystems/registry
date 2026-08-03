---
{
  "title": "Numbers and Strings",
  "description": "Basic types and conversions.",
  "type": "lesson",
  "order": 3,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use Int and Float",
    "Convert between numbers",
    "Manipulate strings",
    "Use String module functions"
  ],
  "knowledge_refs": [
    "elm/elm-03-numbers-strings"
  ],
  "prerequisites": [
    "Elm-02: Values and Functions"
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

# ELM-03-NUMBERS-STRINGS: Numbers and Strings

## Introduction

Basic types and conversions. By the end of this lesson you will be able to: Use Int and Float; Convert between numbers; Manipulate strings; Use String module functions.

## Key Concepts

### 1. Use Int and Float

Target: Use Int and Float. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```elm
add : Float -> Float -> Float
add a b = a + b
```
### 2. Convert between numbers

Target: Convert between numbers. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```elm
String.fromInt 42
String.fromFloat 3.14
```
### 3. Manipulate strings

Target: Manipulate strings. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```elm
String.length "hello"
String.toUpper "hi"
```
### 4. Use String module functions

Target: Use String module functions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```elm
String.split "," "a,b,c"
```

## Practice Questions

1. What is the key idea behind "Numbers and Strings"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Numbers and Strings with analogies and real-world examples"
1. "Show me common mistakes beginners make with Numbers and Strings"
1. "Provide advanced patterns and performance considerations for Numbers and Strings"

## Key Takeaways

- Master the core ideas of Numbers and Strings through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
