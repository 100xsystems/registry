---
{
  "title": "Recursion",
  "description": "Recursive functions, base cases, and induction.",
  "type": "lesson",
  "order": 8,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write recursive functions",
    "Use recursion on lists",
    "Reason with induction",
    "Implement folds from scratch"
  ],
  "knowledge_refs": [
    "haskell/haskell-08-recursion"
  ],
  "prerequisites": [
    "HASKELL-06"
  ],
  "references": [
    {
      "title": "Learn You a Haskell — Recursion",
      "url": "https://learnyouahaskell.github.io/recursion.html"
    },
    {
      "title": "Haskell Wiki — Recursion",
      "url": "https://wiki.haskell.org/Recursion"
    },
    {
      "title": "Haskell Wiki — Fold",
      "url": "https://wiki.haskell.org/Fold"
    }
  ]
}
---

# HASKELL-08-RECURSION: Recursion

## Introduction

Recursive functions, base cases, and induction. By the end of this lesson you will be able to: Write recursive functions; Use recursion on lists; Reason with induction; Implement folds from scratch.

## Key Concepts

### 1. Write recursive functions

Target: Write recursive functions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```haskell
-- recursive sum
sumList :: [Int] -> Int
sumList []     = 0
sumList (x:xs) = x + sumList xs

main :: IO ()
main = print (sumList [1..5])  -- 15
```
### 2. Use recursion on lists

Target: Use recursion on lists. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```haskell
-- recursive map
myMap :: (a -> b) -> [a] -> [b]
myMap _ []     = []
myMap f (x:xs) = f x : myMap f xs

main :: IO ()
main = print (myMap (*2) [1..4])  -- [2,4,6,8]
```
### 3. Reason with induction

Target: Reason with induction. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```haskell
-- recursion on natural numbers
factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n * factorial (n - 1)

main :: IO ()
main = print (factorial 6)  -- 720
```
### 4. Implement folds from scratch

Target: Implement folds from scratch. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```haskell
-- fold from scratch
myFoldr :: (a -> b -> b) -> b -> [a] -> b
myFoldr _ acc []     = acc
myFoldr f acc (x:xs) = f x (myFoldr f acc xs)

main :: IO ()
main = print (myFoldr (+) 0 [1..5])  -- 15
```

## Practice Questions

1. What is the key idea behind "Recursion"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Recursion with analogies and real-world examples"
1. "Show me common mistakes beginners make with Recursion"
1. "Provide advanced patterns and performance considerations for Recursion"

## Key Takeaways

- Master the core ideas of Recursion through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
