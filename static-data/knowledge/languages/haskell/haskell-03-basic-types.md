---
{
  "title": "Basic Types and Typeclasses",
  "description": "Int, Integer, Float, Double, Bool, Char, and String.",
  "type": "lesson",
  "order": 3,
  "duration": "50 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use numeric types Int and Integer",
    "Work with floating-point types",
    "Handle Bool, Char, and String",
    "Understand the Num typeclass hierarchy"
  ],
  "knowledge_refs": [
    "haskell/haskell-03-basic-types"
  ],
  "prerequisites": [
    "HASKELL-02"
  ],
  "references": [
    {
      "title": "Haskell Report — Basic Types",
      "url": "https://www.haskell.org/onlinereport/haskell2010/haskellch6.html"
    },
    {
      "title": "Learn You a Haskell — Types",
      "url": "https://learnyouahaskell.github.io/types-and-typeclasses.html"
    },
    {
      "title": "Hackage — Prelude",
      "url": "https://hackage.haskell.org/package/base/docs/Prelude.html"
    }
  ]
}
---

# HASKELL-03-BASIC-TYPES: Basic Types and Typeclasses

## Introduction

Int, Integer, Float, Double, Bool, Char, and String. By the end of this lesson you will be able to: Use numeric types Int and Integer; Work with floating-point types; Handle Bool, Char, and String; Understand the Num typeclass hierarchy.

## Key Concepts

### 1. Use numeric types Int and Integer

Target: Use numeric types Int and Integer. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```haskell
-- numeric types
main :: IO ()
main = do
  print (42 :: Int)           -- fixed-precision
  print (2 ^ 100 :: Integer)  -- arbitrary precision
  print (3.14 :: Double)
  print (2.5 :: Float)
```
### 2. Work with floating-point types

Target: Work with floating-point types. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```haskell
-- Bool, Char, String
truthy :: Bool
truthy = True

letter :: Char
letter = 'A'

word :: String
word = "hello"

main :: IO ()
main = print (truthy, letter, word)
```
### 3. Handle Bool, Char, and String

Target: Handle Bool, Char, and String. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```haskell
-- the Num typeclass
-- +, -, *, negate work on any Num
main :: IO ()
main = do
  print (fromIntegral 42 :: Double)
  print (round 3.7)     -- 4
  print (truncate 3.7)  -- 3
  print (abs (-5))      -- 5
```
### 4. Understand the Num typeclass hierarchy

Target: Understand the Num typeclass hierarchy. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```haskell
-- conversions
main :: IO ()
main = do
  print (read "42" :: Int)          -- 42
  print (show 3.14)                 -- "3.14"
  print (read "True" :: Bool)       -- True
  print (fromIntegral (7 :: Int) :: Double)  -- 7.0
```

## Practice Questions

1. What is the key idea behind "Basic Types and Typeclasses"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Basic Types and Typeclasses with analogies and real-world examples"
1. "Show me common mistakes beginners make with Basic Types and Typeclasses"
1. "Provide advanced patterns and performance considerations for Basic Types and Typeclasses"

## Key Takeaways

- Master the core ideas of Basic Types and Typeclasses through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
