---
{
  "title": "Typeclasses",
  "description": "Eq, Ord, Show, Read, Num, and custom typeclasses.",
  "type": "lesson",
  "order": 12,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use the standard typeclasses",
    "Derive instances automatically",
    "Define custom typeclasses",
    "Reason with class constraints"
  ],
  "knowledge_refs": [
    "haskell/haskell-12-typeclasses"
  ],
  "prerequisites": [
    "HASKELL-11"
  ],
  "references": [
    {
      "title": "Learn You a Haskell — Typeclasses",
      "url": "https://learnyouahaskell.github.io/types-and-typeclasses.html"
    },
    {
      "title": "Haskell Wiki — Typeclass",
      "url": "https://wiki.haskell.org/Typeclass"
    },
    {
      "title": "Haskell Report — Classes",
      "url": "https://www.haskell.org/onlinereport/haskell2010/haskellch4.html#x10-820004.3"
    }
  ]
}
---

# HASKELL-12-TYPECLASSES: Typeclasses

## Introduction

Eq, Ord, Show, Read, Num, and custom typeclasses. By the end of this lesson you will be able to: Use the standard typeclasses; Derive instances automatically; Define custom typeclasses; Reason with class constraints.

## Key Concepts

### 1. Use the standard typeclasses

Target: Use the standard typeclasses. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```haskell
-- typeclass constraints
same :: (Eq a) => a -> a -> String
same x y
  | x == y    = "equal"
  | otherwise = "different"

main :: IO ()
main = do
  print (same 1 1)         -- "equal"
  print (same "a" "b")     -- "different"
```
### 2. Derive instances automatically

Target: Derive instances automatically. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```haskell
-- deriving standard typeclasses
data Color = Red | Green | Blue
  deriving (Eq, Ord, Show, Read, Enum, Bounded)

main :: IO ()
main = do
  print [Red .. Blue]     -- [Red,Green,Blue]
  print (minBound :: Color, maxBound :: Color)
```
### 3. Define custom typeclasses

Target: Define custom typeclasses. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```haskell
-- custom typeclass
describe :: Show a => a -> String
describe x = "value: " ++ show x

class Describable a where
  describe2 :: a -> String

instance Describable Int where
  describe2 n = "integer " ++ show n

main :: IO ()
main = do
  print (describe 42)
  print (describe2 (5 :: Int))
```
### 4. Reason with class constraints

Target: Reason with class constraints. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```haskell
-- numeric typeclasses
import Data.Ratio
main :: IO ()
main = do
  print (2 :: Integer)              -- exact
  print (2 :: Int)                  -- machine word
  print (2.5 :: Double)
  print (2.5 :: Rational)           -- exact fraction
  print (1 / 3 :: Double, 1 / 3 :: Rational)
```

## Practice Questions

1. What is the key idea behind "Typeclasses"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Typeclasses with analogies and real-world examples"
1. "Show me common mistakes beginners make with Typeclasses"
1. "Provide advanced patterns and performance considerations for Typeclasses"

## Key Takeaways

- Master the core ideas of Typeclasses through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
