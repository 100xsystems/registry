---
{
  "title": "Lazy Evaluation",
  "description": "Thunks, infinite structures, and strictness.",
  "type": "lesson",
  "order": 18,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Understand lazy by default",
    "Work with infinite lists",
    "Control evaluation with seq and $!",
    "Reason about space usage"
  ],
  "knowledge_refs": [
    "haskell/haskell-18-lazy-evaluation"
  ],
  "prerequisites": [
    "HASKELL-13"
  ],
  "references": [
    {
      "title": "Haskell Wiki — Lazy Evaluation",
      "url": "https://wiki.haskell.org/Lazy_evaluation"
    },
    {
      "title": "Haskell Wiki — Foldr Foldl Foldl'",
      "url": "https://wiki.haskell.org/Foldr_Foldl_Foldl%27"
    },
    {
      "title": "Haskell Wiki — Space Leak",
      "url": "https://wiki.haskell.org/Space_leak"
    }
  ]
}
---

# HASKELL-18-LAZY-EVALUATION: Lazy Evaluation

## Introduction

Thunks, infinite structures, and strictness. By the end of this lesson you will be able to: Understand lazy by default; Work with infinite lists; Control evaluation with seq and $!; Reason about space usage.

## Key Concepts

### 1. Understand lazy by default

Target: Understand lazy by default. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```haskell
-- lazy: infinite lists
main :: IO ()
main = do
  print (take 5 [1..])          -- [1,2,3,4,5]
  print (take 5 (repeat "x"))   -- ["x"...]
  print (take 3 (cycle [1, 2])) -- [1,2,1]
```
### 2. Work with infinite lists

Target: Work with infinite lists. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```haskell
-- infinite fibs via laziness
fibs :: [Integer]
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

main :: IO ()
main = print (take 10 fibs)  -- [0,1,1,2,3,5,8,13,21,34]
```
### 3. Control evaluation with seq and $!

Target: Control evaluation with seq and $!. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```haskell
-- seq and strict application
main :: IO ()
main = do
  let x = undefined
  print $ seq () "not evaluated"  -- fine
  -- print $ seq x "boom"          -- would error if forced
  print (1 + 1 `seq` 2 + 2)
```
### 4. Reason about space usage

Target: Reason about space usage. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```haskell
-- foldl' for space safety
import Data.List (foldl')

main :: IO ()
main = do
  print (foldl' (+) 0 [1..1000000])  -- strict, no stack overflow
  print (sum [1..1000000])
```

## Practice Questions

1. What is the key idea behind "Lazy Evaluation"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Lazy Evaluation with analogies and real-world examples"
1. "Show me common mistakes beginners make with Lazy Evaluation"
1. "Provide advanced patterns and performance considerations for Lazy Evaluation"

## Key Takeaways

- Master the core ideas of Lazy Evaluation through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
