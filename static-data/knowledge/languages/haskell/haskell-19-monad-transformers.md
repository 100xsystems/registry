---
{
  "title": "Monad Transformers",
  "description": "ReaderT, StateT, MaybeT, and transformer stacks.",
  "type": "lesson",
  "order": 19,
  "duration": "75 min",
  "difficulty": "expert",
  "learning_objectives": [
    "Combine monads with transformers",
    "Use StateT for mutable state",
    "Use ReaderT for configuration",
    "Lift operations through stacks"
  ],
  "knowledge_refs": [
    "haskell/haskell-19-monad-transformers"
  ],
  "prerequisites": [
    "HASKELL-13"
  ],
  "references": [
    {
      "title": "Haskell Wiki — Monad Transformers",
      "url": "https://wiki.haskell.org/Monad_Transformers_Explained"
    },
    {
      "title": "Hackage — Control.Monad.Trans.State",
      "url": "https://hackage.haskell.org/package/transformers/docs/Control-Monad-Trans-State.html"
    },
    {
      "title": "Hackage — Control.Monad.Trans.Reader",
      "url": "https://hackage.haskell.org/package/transformers/docs/Control-Monad-Trans-Reader.html"
    }
  ]
}
---

# HASKELL-19-MONAD-TRANSFORMERS: Monad Transformers

## Introduction

ReaderT, StateT, MaybeT, and transformer stacks. By the end of this lesson you will be able to: Combine monads with transformers; Use StateT for mutable state; Use ReaderT for configuration; Lift operations through stacks.

## Key Concepts

### 1. Combine monads with transformers

Target: Combine monads with transformers. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```haskell
-- StateT: mutable state in a monad
import Control.Monad.Trans.State

increment :: State Int Int
increment = do
  n <- get
  put (n + 1)
  return n

main :: IO ()
main = print (runState (increment >> increment) 0)  -- (1, 2)
```
### 2. Use StateT for mutable state

Target: Use StateT for mutable state. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```haskell
-- ReaderT: configuration
import Control.Monad.Trans.Reader

greeting :: Reader String String
greeting = do
  name <- ask
  return ("Hello, " ++ name)

main :: IO ()
main = print (runReader greeting "Alice")  -- "Hello, Alice"
```
### 3. Use ReaderT for configuration

Target: Use ReaderT for configuration. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```haskell
-- MaybeT: failure in a stack
import Control.Monad.Trans.Maybe

safe :: MaybeT IO Int
safe = do
  x <- MaybeT (return (Just 5))
  y <- MaybeT (return Nothing)
  return (x + y)

main :: IO ()
main = do
  result <- runMaybeT safe
  print result  -- Nothing
```
### 4. Lift operations through stacks

Target: Lift operations through stacks. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```haskell
-- lifting through stacks
import Control.Monad.Trans.State
import Control.Monad.Trans.Class

main :: IO ()
main = do
  let st = StateT $ \s -> return (s, s + 1)
  result <- runStateT (lift (putStrLn "effect") >> st) 0
  print result
```

## Practice Questions

1. What is the key idea behind "Monad Transformers"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Monad Transformers with analogies and real-world examples"
1. "Show me common mistakes beginners make with Monad Transformers"
1. "Provide advanced patterns and performance considerations for Monad Transformers"

## Key Takeaways

- Master the core ideas of Monad Transformers through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
