---
{
  "title": "Functors, Applicatives, and Monads",
  "description": "fmap, <$>, <*>, >>=, and do notation.",
  "type": "lesson",
  "order": 13,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Map over contexts with Functor",
    "Apply functions with Applicative",
    "Sequence effects with Monad",
    "Write do-notation"
  ],
  "knowledge_refs": [
    "haskell/haskell-13-functors-monads"
  ],
  "prerequisites": [
    "HASKELL-12"
  ],
  "references": [
    {
      "title": "Learn You a Haskell — Functors Applicatives Monads",
      "url": "https://learnyouahaskell.github.io/functors-applicative-functors-and-monoids.html"
    },
    {
      "title": "Haskell Wiki — Monad",
      "url": "https://wiki.haskell.org/Monad"
    },
    {
      "title": "Hackage — Control.Monad",
      "url": "https://hackage.haskell.org/package/base/docs/Control-Monad.html"
    }
  ]
}
---

# HASKELL-13-FUNCTORS-MONADS: Functors, Applicatives, and Monads

## Introduction

fmap, <$>, <*>, >>=, and do notation. By the end of this lesson you will be able to: Map over contexts with Functor; Apply functions with Applicative; Sequence effects with Monad; Write do-notation.

## Key Concepts

### 1. Map over contexts with Functor

Target: Map over contexts with Functor. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```haskell
-- Functor: fmap over a context
main :: IO ()
main = do
  print (fmap (*2) [1, 2, 3])     -- [2,4,6]
  print (fmap (*2) (Just 5))      -- Just 10
  print (fmap (*2) Nothing)       -- Nothing
  print ((*2) <$> Just 5)         -- infix fmap
```
### 2. Apply functions with Applicative

Target: Apply functions with Applicative. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```haskell
-- Applicative: apply functions in context
main :: IO ()
main = do
  print ((+) <$> Just 3 <*> Just 4)   -- Just 7
  print ((+) <$> Just 3 <*> Nothing)  -- Nothing
  print (pure 5 :: Maybe Int)         -- Just 5
```
### 3. Sequence effects with Monad

Target: Sequence effects with Monad. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```haskell
-- Monad: sequence with >>=
main :: IO ()
main = do
  print (Just 3 >>= \x -> Just (x * 2))   -- Just 6
  print (Nothing >>= \x -> Just (x * 2))  -- Nothing
  print ([1, 2, 3] >>= \x -> [x, x])      -- [1,1,2,2,3,3]
```
### 4. Write do-notation

Target: Write do-notation. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```haskell
-- do-notation is >>= sugar
addMaybe :: Maybe Int -> Maybe Int -> Maybe Int
addMaybe mx my = do
  x <- mx
  y <- my
  return (x + y)

main :: IO ()
main = do
  print (addMaybe (Just 3) (Just 4))  -- Just 7
  print (addMaybe (Just 3) Nothing)   -- Nothing
```

## Practice Questions

1. What is the key idea behind "Functors, Applicatives, and Monads"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Functors, Applicatives, and Monads with analogies and real-world examples"
1. "Show me common mistakes beginners make with Functors, Applicatives, and Monads"
1. "Provide advanced patterns and performance considerations for Functors, Applicatives, and Monads"

## Key Takeaways

- Master the core ideas of Functors, Applicatives, and Monads through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
