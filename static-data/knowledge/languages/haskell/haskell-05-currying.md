---
{
  "title": "Currying and Partial Application",
  "description": "Curried functions, sections, and application.",
  "type": "lesson",
  "order": 5,
  "duration": "50 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Understand implicit currying",
    "Partially apply functions",
    "Use operator sections",
    "Compose functions with (.)"
  ],
  "knowledge_refs": [
    "haskell/haskell-05-currying"
  ],
  "prerequisites": [
    "HASKELL-04"
  ],
  "references": [
    {
      "title": "Learn You a Haskell — Higher Order Functions",
      "url": "https://learnyouahaskell.github.io/higher-order-functions.html"
    },
    {
      "title": "Haskell Wiki — Currying",
      "url": "https://wiki.haskell.org/Currying"
    },
    {
      "title": "Haskell Wiki — Pointfree",
      "url": "https://wiki.haskell.org/Pointfree"
    }
  ]
}
---

# HASKELL-05-CURRYING: Currying and Partial Application

## Introduction

Curried functions, sections, and application. By the end of this lesson you will be able to: Understand implicit currying; Partially apply functions; Use operator sections; Compose functions with (.).

## Key Concepts

### 1. Understand implicit currying

Target: Understand implicit currying. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```haskell
-- currying: functions take one argument at a time
add :: Int -> Int -> Int
add a b = a + b

main :: IO ()
main = do
  print (add 2 3)      -- 5
  print ((add 2) 3)    -- explicit partial application
```
### 2. Partially apply functions

Target: Partially apply functions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```haskell
-- partial application
add :: Int -> Int -> Int
add a b = a + b

addTwo :: Int -> Int
addTwo = add 2

main :: IO ()
main = print (addTwo 40)  -- 42
```
### 3. Use operator sections

Target: Use operator sections. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```haskell
-- operator sections
main :: IO ()
main = do
  let addOne = (+ 1)
  let double = (* 2)
  print (addOne 41)      -- 42
  print (map (+1) [1, 2])  -- [2,3]
```
### 4. Compose functions with (.)

Target: Compose functions with (.). Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```haskell
-- function composition
main :: IO ()
main = do
  let f = (* 2) . (+ 1)   -- add 1, then double
  print (f 4)             -- 10
  print ((length . filter even) [1..10])  -- 5
```

## Practice Questions

1. What is the key idea behind "Currying and Partial Application"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Currying and Partial Application with analogies and real-world examples"
1. "Show me common mistakes beginners make with Currying and Partial Application"
1. "Provide advanced patterns and performance considerations for Currying and Partial Application"

## Key Takeaways

- Master the core ideas of Currying and Partial Application through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
