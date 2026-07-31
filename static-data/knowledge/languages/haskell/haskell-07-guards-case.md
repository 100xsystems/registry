---
{
  "title": "Guards and Case Expressions",
  "description": "Boolean guards, where bindings, and case-of.",
  "type": "lesson",
  "order": 7,
  "duration": "50 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Write multi-branch guards",
    "Bind values in where clauses",
    "Use case expressions",
    "Match with otherwise"
  ],
  "knowledge_refs": [
    "haskell/haskell-07-guards-case"
  ],
  "prerequisites": [
    "HASKELL-06"
  ],
  "references": [
    {
      "title": "Learn You a Haskell — Guards",
      "url": "https://learnyouahaskell.github.io/syntax-in-functions.html#guards-guards"
    },
    {
      "title": "Haskell Report — Case Expressions",
      "url": "https://www.haskell.org/onlinereport/haskell2010/haskellch3.html#x8-460003.13"
    },
    {
      "title": "Haskell Wiki — Case",
      "url": "https://wiki.haskell.org/Case"
    }
  ]
}
---

# HASKELL-07-GUARDS-CASE: Guards and Case Expressions

## Introduction

Boolean guards, where bindings, and case-of. By the end of this lesson you will be able to: Write multi-branch guards; Bind values in where clauses; Use case expressions; Match with otherwise.

## Key Concepts

### 1. Write multi-branch guards

Target: Write multi-branch guards. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```haskell
-- guards
max3 :: Int -> Int -> Int -> Int
max3 a b c
  | a >= b && a >= c = a
  | b >= c           = b
  | otherwise        = c

main :: IO ()
main = print (max3 3 9 5)  -- 9
```
### 2. Bind values in where clauses

Target: Bind values in where clauses. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```haskell
-- guards with where
bodyMassIndex :: Double -> Double -> String
bodyMassIndex weight height
  | bmi < 18.5 = "underweight"
  | bmi < 25   = "normal"
  | otherwise  = "overweight"
  where bmi = weight / (height * height)

main :: IO ()
main = print (bodyMassIndex 70 1.75)
```
### 3. Use case expressions

Target: Use case expressions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```haskell
-- case expression
main :: IO ()
main = do
  let status = 404
  print $ case status of
    200 -> "ok"
    404 -> "not found"
    _   -> "unknown"
```
### 4. Match with otherwise

Target: Match with otherwise. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```haskell
-- case with patterns
main :: IO ()
main = do
  let maybeNum = Just 7
  print $ case maybeNum of
    Just n  -> n * 2
    Nothing -> 0
```

## Practice Questions

1. What is the key idea behind "Guards and Case Expressions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Guards and Case Expressions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Guards and Case Expressions"
1. "Provide advanced patterns and performance considerations for Guards and Case Expressions"

## Key Takeaways

- Master the core ideas of Guards and Case Expressions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
