---
{
  "title": "Modules and Imports",
  "description": "Module structure, exports, and qualified imports.",
  "type": "lesson",
  "order": 16,
  "duration": "50 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Declare modules and export lists",
    "Import modules qualified",
    "Hide and rename imports",
    "Organize a multi-file project"
  ],
  "knowledge_refs": [
    "haskell/haskell-16-modules"
  ],
  "prerequisites": [
    "HASKELL-12"
  ],
  "references": [
    {
      "title": "Learn You a Haskell — Modules",
      "url": "https://learnyouahaskell.github.io/modules.html"
    },
    {
      "title": "Haskell Wiki — Modules",
      "url": "https://wiki.haskell.org/Modules"
    },
    {
      "title": "GHC Users Guide — Modules",
      "url": "https://downloads.haskell.org/ghc/latest/docs/users_guide/"
    }
  ]
}
---

# HASKELL-16-MODULES: Modules and Imports

## Introduction

Module structure, exports, and qualified imports. By the end of this lesson you will be able to: Declare modules and export lists; Import modules qualified; Hide and rename imports; Organize a multi-file project.

## Key Concepts

### 1. Declare modules and export lists

Target: Declare modules and export lists. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```haskell
-- module with export list
module Math2 (square, cube) where

square :: Int -> Int
square x = x * x

cube :: Int -> Int
cube x = x * x * x

-- internal helper not exported
secret :: Int -> Int
secret x = x + 1
```
### 2. Import modules qualified

Target: Import modules qualified. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```haskell
-- importing modules
import Data.List (sort, nub)
import qualified Data.Map as Map
import Data.Char (toUpper)

main :: IO ()
main = do
  print (sort [3, 1, 2])         -- [1,2,3]
  print (nub [1, 1, 2])          -- [1,2]
  print (Map.fromList [(1, "a")])
  print (map toUpper "hello")    -- "HELLO"
```
### 3. Hide and rename imports

Target: Hide and rename imports. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```haskell
-- hiding and renaming
import Data.List hiding (sort)
import qualified Data.List as L

main :: IO ()
main = do
  print (L.sort [3, 1, 2])
  print "hiding works"
```
### 4. Organize a multi-file project

Target: Organize a multi-file project. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```haskell
-- multi-file project
-- src/Lib.hs:
-- module Lib (greet) where
-- greet :: String -> String
-- greet name = "Hello, " ++ name
--
-- app/Main.hs:
-- import Lib (greet)
-- main :: IO ()
-- main = putStrLn (greet "world")
main :: IO ()
main = putStrLn "cabal build"
```

## Practice Questions

1. What is the key idea behind "Modules and Imports"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Modules and Imports with analogies and real-world examples"
1. "Show me common mistakes beginners make with Modules and Imports"
1. "Provide advanced patterns and performance considerations for Modules and Imports"

## Key Takeaways

- Master the core ideas of Modules and Imports through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
