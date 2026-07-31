---
{
  "title": "Performance and Optimization",
  "description": "Strictness, unboxed types, profiling, and benchmarks.",
  "type": "lesson",
  "order": 21,
  "duration": "75 min",
  "difficulty": "expert",
  "learning_objectives": [
    "Use strict fields and bang patterns",
    "Profile with GHC profiling",
    "Optimize hot loops",
    "Use Data.Map and Data.Sequence"
  ],
  "knowledge_refs": [
    "haskell/haskell-21-performance"
  ],
  "prerequisites": [
    "HASKELL-18"
  ],
  "references": [
    {
      "title": "GHC Users Guide — Profiling",
      "url": "https://downloads.haskell.org/ghc/latest/docs/users_guide/profiling.html"
    },
    {
      "title": "Haskell Wiki — Performance",
      "url": "https://wiki.haskell.org/Performance"
    },
    {
      "title": "Haskell Wiki — Bang Patterns",
      "url": "https://wiki.haskell.org/Bang_patterns"
    }
  ]
}
---

# HASKELL-21-PERFORMANCE: Performance and Optimization

## Introduction

Strictness, unboxed types, profiling, and benchmarks. By the end of this lesson you will be able to: Use strict fields and bang patterns; Profile with GHC profiling; Optimize hot loops; Use Data.Map and Data.Sequence.

## Key Concepts

### 1. Use strict fields and bang patterns

Target: Use strict fields and bang patterns. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```haskell
-- strict fields and bang patterns
{-# LANGUAGE BangPatterns #-}

-- strict accumulator avoids thunk buildup
sumStrict :: [Int] -> Int
sumStrict = go 0
  where
    go !acc []     = acc
    go !acc (x:xs) = go (acc + x) xs

main :: IO ()
main = print (sumStrict [1..100000])
```
### 2. Profile with GHC profiling

Target: Profile with GHC profiling. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```haskell
-- unboxed arrays for performance
import Data.Array
import Data.Array.Unboxed

main :: IO ()
main = do
  let arr :: UArray Int Int
      arr = listArray (1, 5) [10, 20, 30, 40, 50]
  print (arr ! 3)   -- 30
  print (elems arr)
```
### 3. Optimize hot loops

Target: Optimize hot loops. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```haskell
-- Data.Map for fast lookups
import qualified Data.Map as Map

main :: IO ()
main = do
  let m = Map.fromList [(k, k * k) | k <- [1..10000]]
  print (Map.lookup 999 m)  -- Just 998001
  print (Map.size m)        -- 10000
```
### 4. Use Data.Map and Data.Sequence

Target: Use Data.Map and Data.Sequence. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```haskell
-- profiling
-- compile: ghc -prof -fprof-auto -rtsopts Main.hs
-- run:     ./Main +RTS -p
-- view:    cat Main.prof
main :: IO ()
main = print (sum [1..1000000])
```

## Practice Questions

1. What is the key idea behind "Performance and Optimization"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Performance and Optimization with analogies and real-world examples"
1. "Show me common mistakes beginners make with Performance and Optimization"
1. "Provide advanced patterns and performance considerations for Performance and Optimization"

## Key Takeaways

- Master the core ideas of Performance and Optimization through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
