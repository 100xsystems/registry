---
{
  "title": "Pattern Matching",
  "description": "Function equations, list patterns, and wildcards.",
  "type": "lesson",
  "order": 6,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Pattern match on function arguments",
    "Destructure lists and tuples",
    "Use the wildcard _ and as-patterns",
    "Handle partial patterns safely"
  ],
  "knowledge_refs": [
    "haskell/haskell-06-pattern-matching"
  ],
  "prerequisites": [
    "HASKELL-05"
  ],
  "references": [
    {
      "title": "Learn You a Haskell — Syntax in Functions",
      "url": "https://learnyouahaskell.github.io/syntax-in-functions.html"
    },
    {
      "title": "Haskell Wiki — Pattern Matching",
      "url": "https://wiki.haskell.org/Pattern_matching"
    },
    {
      "title": "Haskell Report — Patterns",
      "url": "https://www.haskell.org/onlinereport/haskell2010/haskellch3.html#x8-580003.17"
    }
  ]
}
---

# HASKELL-06-PATTERN-MATCHING: Pattern Matching

## Introduction

Function equations, list patterns, and wildcards. By the end of this lesson you will be able to: Pattern match on function arguments; Destructure lists and tuples; Use the wildcard _ and as-patterns; Handle partial patterns safely.

## Key Concepts

### 1. Pattern match on function arguments

Target: Pattern match on function arguments. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```haskell
-- pattern matching on arguments
myHead :: [a] -> a
myHead (x : _) = x

main :: IO ()
main = print (myHead [7, 8, 9])  -- 7
```
### 2. Destructure lists and tuples

Target: Destructure lists and tuples. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```haskell
-- multiple equations
fib :: Int -> Int
fib 0 = 0
fib 1 = 1
fib n = fib (n - 1) + fib (n - 2)

main :: IO ()
main = print (fib 10)  -- 55
```
### 3. Use the wildcard _ and as-patterns

Target: Use the wildcard _ and as-patterns. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```haskell
-- tuple and list patterns
main :: IO ()
main = do
  let (a, b) = (3, 4)
  print (a + b)                -- 7
  let (x : rest) = [1, 2, 3]
  print (x, rest)              -- (1,[2,3])
```
### 4. Handle partial patterns safely

Target: Handle partial patterns safely. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```haskell
-- as-patterns and wildcards
firstLetter :: String -> Char
firstLetter s@(c : _) = c
-- s is the whole string; c is the head
main :: IO ()
main = do
  print (firstLetter "abc")
  let _ = "ignored"   -- wildcard binding
  print "ok"
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
