---
{
  "title": "Getting Started with Haskell",
  "description": "Install GHC, run scripts, and explore the interactive REPL.",
  "type": "lesson",
  "order": 1,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Install GHC and the cabal/stack toolchain",
    "Run scripts with runghc and compile with ghc",
    "Explore expressions in GHCi",
    "Understand the purely functional model"
  ],
  "knowledge_refs": [
    "haskell/haskell-01-getting-started"
  ],
  "prerequisites": [],
  "references": [
    {
      "title": "Haskell.org — Downloads",
      "url": "https://www.haskell.org/downloads/"
    },
    {
      "title": "GHC Users Guide",
      "url": "https://downloads.haskell.org/ghc/latest/docs/users_guide/"
    },
    {
      "title": "Learn You a Haskell — Introduction",
      "url": "https://learnyouahaskell.github.io/introduction.html"
    }
  ]
}
---

# HASKELL-01-GETTING-STARTED: Getting Started with Haskell

## Introduction

Install GHC, run scripts, and explore the interactive REPL. By the end of this lesson you will be able to: Install GHC and the cabal/stack toolchain; Run scripts with runghc and compile with ghc; Explore expressions in GHCi; Understand the purely functional model.

## Key Concepts

### 1. Install GHC and the cabal/stack toolchain

Target: Install GHC and the cabal/stack toolchain. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```haskell
-- hello.hs — run: runghc hello.hs or ghc -o hello hello.hs && ./hello
main :: IO ()
main = putStrLn "Hello, 100x Systems!"
```
### 2. Run scripts with runghc and compile with ghc

Target: Run scripts with runghc and compile with ghc. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```haskell
-- GHCi interactive session
-- $ ghci
-- Prelude> 2 + 2
-- 4
-- Prelude> :t (++)
-- (++) :: [a] -> [a] -> [a]
main :: IO ()
main = putStrLn "explore with :t and :info"
```
### 3. Explore expressions in GHCi

Target: Explore expressions in GHCi. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```haskell
-- pure expression, no side effects
square :: Int -> Int
square x = x * x

main :: IO ()
main = print (square 9)  -- 81
```
### 4. Understand the purely functional model

Target: Understand the purely functional model. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```haskell
-- the purely functional model
-- functions are values; no mutable state
add :: Int -> Int -> Int
add a b = a + b

main :: IO ()
main = print (add 20 22)  -- 42
```

## Practice Questions

1. What is the key idea behind "Getting Started with Haskell"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with Haskell with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with Haskell"
1. "Provide advanced patterns and performance considerations for Getting Started with Haskell"

## Key Takeaways

- Master the core ideas of Getting Started with Haskell through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
