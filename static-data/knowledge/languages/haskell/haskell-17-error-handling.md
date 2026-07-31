---
{
  "title": "Error Handling",
  "description": "Exceptions, pure errors, and the ExceptT pattern.",
  "type": "lesson",
  "order": 17,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Throw and catch exceptions",
    "Use Either for pure error handling",
    "Distinguish exceptions from values",
    "Handle resource cleanup"
  ],
  "knowledge_refs": [
    "haskell/haskell-17-error-handling"
  ],
  "prerequisites": [
    "HASKELL-14"
  ],
  "references": [
    {
      "title": "Haskell Wiki — Exception",
      "url": "https://wiki.haskell.org/Exception"
    },
    {
      "title": "Hackage — Control.Exception",
      "url": "https://hackage.haskell.org/package/base/docs/Control-Exception.html"
    },
    {
      "title": "Haskell Wiki — Error vs Exception",
      "url": "https://wiki.haskell.org/Error_vs._Exception"
    }
  ]
}
---

# HASKELL-17-ERROR-HANDLING: Error Handling

## Introduction

Exceptions, pure errors, and the ExceptT pattern. By the end of this lesson you will be able to: Throw and catch exceptions; Use Either for pure error handling; Distinguish exceptions from values; Handle resource cleanup.

## Key Concepts

### 1. Throw and catch exceptions

Target: Throw and catch exceptions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```haskell
-- pure errors with Either
safeDiv :: Int -> Int -> Either String Int
safeDiv _ 0 = Left "division by zero"
safeDiv a b = Right (a `div` b)

main :: IO ()
main = print (safeDiv 10 0)
```
### 2. Use Either for pure error handling

Target: Use Either for pure error handling. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```haskell
-- exceptions in IO
import Control.Exception

main :: IO ()
main = do
  result <- try (evaluate (div 1 0)) :: IO (Either SomeException Int)
  case result of
    Left e  -> putStrLn ("caught: " ++ show e)
    Right n -> print n
```
### 3. Distinguish exceptions from values

Target: Distinguish exceptions from values. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```haskell
-- throw and catch
import Control.Exception

data MyError = MyError String deriving Show
instance Exception MyError

main :: IO ()
main = do
  catch
    (throwIO (MyError "boom"))
    (\e -> putStrLn ("handled: " ++ show (e :: MyError)))
```
### 4. Handle resource cleanup

Target: Handle resource cleanup. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```haskell
-- bracket for cleanup
import Control.Exception

withFileSafe :: FilePath -> (String -> IO a) -> IO a
withFileSafe path f = bracket
  (readFile path)
  (\_ -> putStrLn "closed")
  f

main :: IO ()
main = withFileSafe "data.txt" (putStrLn . take 20)
```

## Practice Questions

1. What is the key idea behind "Error Handling"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Error Handling with analogies and real-world examples"
1. "Show me common mistakes beginners make with Error Handling"
1. "Provide advanced patterns and performance considerations for Error Handling"

## Key Takeaways

- Master the core ideas of Error Handling through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
