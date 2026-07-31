---
{
  "title": "Testing with HUnit and QuickCheck",
  "description": "Unit tests and property-based testing.",
  "type": "lesson",
  "order": 20,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Write HUnit test cases",
    "Define QuickCheck properties",
    "Test pure functions systematically",
    "Run tests with cabal test"
  ],
  "knowledge_refs": [
    "haskell/haskell-20-testing"
  ],
  "prerequisites": [
    "HASKELL-12"
  ],
  "references": [
    {
      "title": "Hackage — QuickCheck",
      "url": "https://hackage.haskell.org/package/QuickCheck"
    },
    {
      "title": "Hackage — HUnit",
      "url": "https://hackage.haskell.org/package/HUnit"
    },
    {
      "title": "Haskell Wiki — Testing",
      "url": "https://wiki.haskell.org/Testing"
    }
  ]
}
---

# HASKELL-20-TESTING: Testing with HUnit and QuickCheck

## Introduction

Unit tests and property-based testing. By the end of this lesson you will be able to: Write HUnit test cases; Define QuickCheck properties; Test pure functions systematically; Run tests with cabal test.

## Key Concepts

### 1. Write HUnit test cases

Target: Write HUnit test cases. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```haskell
-- HUnit test
import Test.HUnit

double :: Int -> Int
double x = x * 2

main :: IO ()
main = do
  let t1 = TestCase (assertEqual "double 21" 42 (double 21))
  runTestTT t1
  return ()
```
### 2. Define QuickCheck properties

Target: Define QuickCheck properties. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```haskell
-- QuickCheck property
import Test.QuickCheck

reverseIdempotent :: [Int] -> Bool
reverseIdempotent xs = reverse (reverse xs) == xs

main :: IO ()
main = quickCheck reverseIdempotent  -- +++ OK, passed 100 tests
```
### 3. Test pure functions systematically

Target: Test pure functions systematically. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```haskell
-- QuickCheck with generators
import Test.QuickCheck
import Data.List (nub)

commutativeAdd :: Int -> Int -> Bool
commutativeAdd a b = a + b == b + a

main :: IO ()
main = do
  quickCheck commutativeAdd
  quickCheck (\xs -> length (nub xs) <= length xs)
```
### 4. Run tests with cabal test

Target: Run tests with cabal test. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```haskell
-- testing with cabal
-- stack test  /  cabal test
-- Spec.hs contains all properties
main :: IO ()
main = do
  putStrLn "run with: cabal test"
```

## Practice Questions

1. What is the key idea behind "Testing with HUnit and QuickCheck"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Testing with HUnit and QuickCheck with analogies and real-world examples"
1. "Show me common mistakes beginners make with Testing with HUnit and QuickCheck"
1. "Provide advanced patterns and performance considerations for Testing with HUnit and QuickCheck"

## Key Takeaways

- Master the core ideas of Testing with HUnit and QuickCheck through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
