---
{
  "title": "Pattern Matching",
  "description": "Case expressions.",
  "type": "lesson",
  "order": 9,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write case expressions",
    "Match constructors",
    "Use guards",
    "Match literals"
  ],
  "knowledge_refs": [
    "purescript/purescript-09-pattern-matching"
  ],
  "prerequisites": [
    "PureScript-08: Either"
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

# PURESCRIPT-09-PATTERN-MATCHING: Pattern Matching

## Introduction

Case expressions. By the end of this lesson you will be able to: Write case expressions; Match constructors; Use guards; Match literals.

## Key Concepts

### 1. Write case expressions

Target: Write case expressions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```purescript
describe :: Int -> String
describe n =
  case n of
    0 -> "zero"
    1 -> "one"
    _ -> "many"
```
### 2. Match constructors

Target: Match constructors. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```purescript
classify :: Int -> String
classify n
  | n < 0 = "negative"
  | n == 0 = "zero"
  | otherwise = "positive"
```
### 3. Use guards

Target: Use guards. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```purescript
sumPair :: (Int, Int) -> Int
sumPair (a, b) = a + b
```
### 4. Match literals

Target: Match literals. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```purescript
case pair of
  (0, 0) -> "origin"
  _ -> "elsewhere"
```

## Practice Questions

1. What is the key idea behind "Pattern Matching"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Pattern Matching with analogies and real-world examples"
1. "Show me common mistakes beginners make with Pattern Matching"
1. "Provide advanced patterns and performance considerations for Pattern Matching"

## Key Takeaways

- Master the core ideas of Pattern Matching through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
