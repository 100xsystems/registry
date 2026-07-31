---
{
  "title": "IO and Effectful Programming",
  "description": "The IO type, do-notation, and pure/impure boundaries.",
  "type": "lesson",
  "order": 15,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Perform I/O with the IO type",
    "Sequence actions with do-notation",
    "Keep effects at the boundaries",
    "Use getLine, putStrLn, and readFile"
  ],
  "knowledge_refs": [
    "haskell/haskell-15-io-monads"
  ],
  "prerequisites": [
    "HASKELL-13"
  ],
  "references": [
    {
      "title": "Learn You a Haskell — Input and Output",
      "url": "https://learnyouahaskell.github.io/input-and-output.html"
    },
    {
      "title": "Haskell Wiki — IO",
      "url": "https://wiki.haskell.org/IO"
    },
    {
      "title": "Haskell Wiki — Do Notation",
      "url": "https://wiki.haskell.org/Do_notation_considered_harmful"
    }
  ]
}
---

# HASKELL-15-IO-MONADS: IO and Effectful Programming

## Introduction

The IO type, do-notation, and pure/impure boundaries. By the end of this lesson you will be able to: Perform I/O with the IO type; Sequence actions with do-notation; Keep effects at the boundaries; Use getLine, putStrLn, and readFile.

## Key Concepts

### 1. Perform I/O with the IO type

Target: Perform I/O with the IO type. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```haskell
-- basic IO actions
main :: IO ()
main = do
  putStrLn "What is your name?"
  name <- getLine
  putStrLn ("Hello, " ++ name ++ "!")
```
### 2. Sequence actions with do-notation

Target: Sequence actions with do-notation. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```haskell
-- sequencing actions
main :: IO ()
main = do
  putStr "one " >> putStrLn "two"   -- one two
  sequence_ [putStrLn "a", putStrLn "b"]
  mapM_ print [1, 2, 3]
```
### 3. Keep effects at the boundaries

Target: Keep effects at the boundaries. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```haskell
-- reading and writing files
main :: IO ()
main = do
  writeFile "data.txt" "line one\nline two\n"
  content <- readFile "data.txt"
  putStrLn content
  let lines2 = lines content
  print (length lines2)   -- 2
```
### 4. Use getLine, putStrLn, and readFile

Target: Use getLine, putStrLn, and readFile. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```haskell
-- pure core, effectful shell
compute :: [Int] -> Int
compute = sum . map (^2)   -- pure

main :: IO ()
main = do
  input <- getContents
  let nums = map read (words input)
  print (compute nums)
```

## Practice Questions

1. What is the key idea behind "IO and Effectful Programming"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain IO and Effectful Programming with analogies and real-world examples"
1. "Show me common mistakes beginners make with IO and Effectful Programming"
1. "Provide advanced patterns and performance considerations for IO and Effectful Programming"

## Key Takeaways

- Master the core ideas of IO and Effectful Programming through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
