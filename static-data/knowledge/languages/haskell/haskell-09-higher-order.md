---
{
  "title": "Higher-Order Functions",
  "description": "map, filter, fold, and function arguments.",
  "type": "lesson",
  "order": 9,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Transform lists with map and filter",
    "Reduce with foldr and foldl",
    "Pass functions as arguments",
    "Use takeWhile, dropWhile, and zipWith"
  ],
  "knowledge_refs": [
    "haskell/haskell-09-higher-order"
  ],
  "prerequisites": [
    "HASKELL-08"
  ],
  "references": [
    {
      "title": "Learn You a Haskell — Higher Order Functions",
      "url": "https://learnyouahaskell.github.io/higher-order-functions.html"
    },
    {
      "title": "Haskell Wiki — Fold",
      "url": "https://wiki.haskell.org/Fold"
    },
    {
      "title": "Hackage — Data.List Functions",
      "url": "https://hackage.haskell.org/package/base/docs/Data-List.html"
    }
  ]
}
---

# HASKELL-09-HIGHER-ORDER: Higher-Order Functions

## Introduction

map, filter, fold, and function arguments. By the end of this lesson you will be able to: Transform lists with map and filter; Reduce with foldr and foldl; Pass functions as arguments; Use takeWhile, dropWhile, and zipWith.

## Key Concepts

### 1. Transform lists with map and filter

Target: Transform lists with map and filter. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```haskell
-- map, filter, fold
main :: IO ()
main = do
  print (map (*2) [1..5])
  print (filter (>2) [1..5])
  print (foldr (+) 0 [1..5])   -- 15
  print (foldl (+) 0 [1..5])   -- 15
```
### 2. Reduce with foldr and foldl

Target: Reduce with foldr and foldl. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```haskell
-- passing functions
applyTwice :: (a -> a) -> a -> a
applyTwice f x = f (f x)

main :: IO ()
main = print (applyTwice (*2) 10)  -- 40
```
### 3. Pass functions as arguments

Target: Pass functions as arguments. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```haskell
-- takeWhile and dropWhile
main :: IO ()
main = do
  print (takeWhile (<5) [1..10])      -- [1,2,3,4]
  print (dropWhile (<5) [1..10])      -- [5..10]
  print (zipWith (+) [1,2] [3,4])     -- [4,6]
```
### 4. Use takeWhile, dropWhile, and zipWith

Target: Use takeWhile, dropWhile, and zipWith. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```haskell
-- fold with non-commutative functions
main :: IO ()
main = do
  print (foldr (:) [] [1..3])  -- [1,2,3] (right)
  print (foldl (flip (:)) [] [1..3])  -- [3,2,1] (left)
```

## Practice Questions

1. What is the key idea behind "Higher-Order Functions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Higher-Order Functions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Higher-Order Functions"
1. "Provide advanced patterns and performance considerations for Higher-Order Functions"

## Key Takeaways

- Master the core ideas of Higher-Order Functions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
