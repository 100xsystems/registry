---
{
  "title": "Types and Functions",
  "description": "Type signatures, pure functions, and type inference.",
  "type": "lesson",
  "order": 2,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Write explicit type signatures",
    "Define pure functions with equations",
    "Let the compiler infer types",
    "Use let, where, and guards"
  ],
  "knowledge_refs": [
    "haskell/haskell-02-types-functions"
  ],
  "prerequisites": [
    "HASKELL-01"
  ],
  "references": [
    {
      "title": "Learn You a Haskell — Types and Typeclasses",
      "url": "https://learnyouahaskell.github.io/types-and-typeclasses.html"
    },
    {
      "title": "Haskell Wiki — Type Inference",
      "url": "https://wiki.haskell.org/Type_inference"
    },
    {
      "title": "Haskell — Function Basics",
      "url": "https://learnyouahaskell.github.io/syntax-in-functions.html"
    }
  ]
}
---

# HASKELL-02-TYPES-FUNCTIONS: Types and Functions

## Introduction

Type signatures, pure functions, and type inference. By the end of this lesson you will be able to: Write explicit type signatures; Define pure functions with equations; Let the compiler infer types; Use let, where, and guards.

## Key Concepts

### 1. Write explicit type signatures

Target: Write explicit type signatures. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```haskell
-- explicit type signature
addOne :: Int -> Int
addOne x = x + 1

main :: IO ()
main = print (addOne 41)  -- 42
```
### 2. Define pure functions with equations

Target: Define pure functions with equations. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```haskell
-- type inference
-- let the compiler figure out the types
main :: IO ()
main = do
  let triple x = x * 3
  print (triple 14)   -- 42
  print (triple 2.5)  -- 7.5 (polymorphic)
```
### 3. Let the compiler infer types

Target: Let the compiler infer types. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```haskell
-- let and where
main :: IO ()
main = do
  let a = 20          -- let binding in do block
  print (a + b)
  where b = 22        -- where binds for the whole main
```
### 4. Use let, where, and guards

Target: Use let, where, and guards. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```haskell
-- guards
classify :: Int -> String
classify n
  | n >= 90    = "A"
  | n >= 80    = "B"
  | otherwise  = "C"

main :: IO ()
main = print (classify 85)  -- "B"
```

## Practice Questions

1. What is the key idea behind "Types and Functions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Types and Functions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Types and Functions"
1. "Provide advanced patterns and performance considerations for Types and Functions"

## Key Takeaways

- Master the core ideas of Types and Functions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
