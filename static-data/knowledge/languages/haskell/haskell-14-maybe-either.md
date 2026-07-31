---
{
  "title": "Maybe and Either",
  "description": "Optional values, error recovery, and safe functions.",
  "type": "lesson",
  "order": 14,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Handle failure with Maybe",
    "Return details with Either",
    "Chain computations in context",
    "Use safe versions of partial functions"
  ],
  "knowledge_refs": [
    "haskell/haskell-14-maybe-either"
  ],
  "prerequisites": [
    "HASKELL-12"
  ],
  "references": [
    {
      "title": "Learn You a Haskell — Maybe and Either",
      "url": "https://learnyouahaskell.github.io/functors-applicative-functors-and-monoids.html#maybe-and-either"
    },
    {
      "title": "Hackage — Data.Maybe",
      "url": "https://hackage.haskell.org/package/base/docs/Data-Maybe.html"
    },
    {
      "title": "Hackage — Data.Either",
      "url": "https://hackage.haskell.org/package/base/docs/Data-Either.html"
    }
  ]
}
---

# HASKELL-14-MAYBE-EITHER: Maybe and Either

## Introduction

Optional values, error recovery, and safe functions. By the end of this lesson you will be able to: Handle failure with Maybe; Return details with Either; Chain computations in context; Use safe versions of partial functions.

## Key Concepts

### 1. Handle failure with Maybe

Target: Handle failure with Maybe. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```haskell
-- Maybe for optional values
safeHead :: [a] -> Maybe a
safeHead []    = Nothing
safeHead (x:_) = Just x

main :: IO ()
main = do
  print (safeHead [1, 2])  -- Just 1
  print (safeHead [])      -- Nothing
```
### 2. Return details with Either

Target: Return details with Either. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```haskell
-- Either for errors
parseInt :: String -> Either String Int
parseInt s
  | not (null s) && all (`elem` ['0'..'9']) s = Right (read s)
  | otherwise                 = Left ("not a number: " ++ s)

main :: IO ()
main = do
  print (parseInt "42")     -- Right 42
  print (parseInt "abc")    -- Left ...
```
### 3. Chain computations in context

Target: Chain computations in context. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```haskell
-- chaining Maybe
lookupUser :: String -> Maybe Int
lookupUser name = lookup name [("alice", 1), ("bob", 2)]

lookupOrder :: Int -> Maybe String
lookupOrder uid = lookup uid [(1, "keyboard"), (2, "mouse")]

userOrder :: String -> Maybe String
userOrder name = do
  uid <- lookupUser name
  order <- lookupOrder uid
  return order

main :: IO ()
main = print (userOrder "alice")  -- Just "keyboard"
```
### 4. Use safe versions of partial functions

Target: Use safe versions of partial functions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```haskell
-- maybe and either eliminators
main :: IO ()
main = do
  print (maybe 0 (+1) (Just 4))   -- 5
  print (maybe 0 (+1) Nothing)    -- 0
  print (either (const 0) id (Right 9))  -- 9
  print (either (const 0) id (Left "x")) -- 0
```

## Practice Questions

1. What is the key idea behind "Maybe and Either"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Maybe and Either with analogies and real-world examples"
1. "Show me common mistakes beginners make with Maybe and Either"
1. "Provide advanced patterns and performance considerations for Maybe and Either"

## Key Takeaways

- Master the core ideas of Maybe and Either through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
