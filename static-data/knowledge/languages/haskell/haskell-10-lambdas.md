---
{
  "title": "Lambdas and Composition",
  "description": "Anonymous functions, sections, and the (.) operator.",
  "type": "lesson",
  "order": 10,
  "duration": "50 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write lambda expressions",
    "Compose functions point-free",
    "Use $ for application",
    "Read and write idiomatic pipelines"
  ],
  "knowledge_refs": [
    "haskell/haskell-10-lambdas"
  ],
  "prerequisites": [
    "HASKELL-09"
  ],
  "references": [
    {
      "title": "Learn You a Haskell — Lambdas",
      "url": "https://learnyouahaskell.github.io/higher-order-functions.html#lambdas"
    },
    {
      "title": "Haskell Wiki — Pointfree",
      "url": "https://wiki.haskell.org/Pointfree"
    },
    {
      "title": "Haskell Wiki — Function Composition",
      "url": "https://wiki.haskell.org/Function_composition"
    }
  ]
}
---

# HASKELL-10-LAMBDAS: Lambdas and Composition

## Introduction

Anonymous functions, sections, and the (.) operator. By the end of this lesson you will be able to: Write lambda expressions; Compose functions point-free; Use $ for application; Read and write idiomatic pipelines.

## Key Concepts

### 1. Write lambda expressions

Target: Write lambda expressions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```haskell
-- lambda syntax
main :: IO ()
main = do
  let add = \x y -> x + y
  print (add 2 3)  -- 5
  print (map (\x -> x * x) [1..4])  -- [1,4,9,16]
```
### 2. Compose functions point-free

Target: Compose functions point-free. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```haskell
-- point-free style
main :: IO ()
main = do
  let oddCount = length . filter odd
  print (oddCount [1..10])  -- 5
  let sumSquares = sum . map (^2)
  print (sumSquares [1..4])  -- 30
```
### 3. Use $ for application

Target: Use $ for application. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```haskell
-- the $ operator
main :: IO ()
main = do
  -- avoids parentheses: f (g x) == f $ g x
  print (map (+1) (filter even [1..10]))
  print $ map (+1) $ filter even [1..10]
```
### 4. Read and write idiomatic pipelines

Target: Read and write idiomatic pipelines. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```haskell
-- pipeline of transforms
main :: IO ()
main = do
  let result = sum . map (*2) . filter odd $ [1..10]
  print result  -- odd:1,3,5,7,9 -> *2 -> sum = 50
```

## Practice Questions

1. What is the key idea behind "Lambdas and Composition"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Lambdas and Composition with analogies and real-world examples"
1. "Show me common mistakes beginners make with Lambdas and Composition"
1. "Provide advanced patterns and performance considerations for Lambdas and Composition"

## Key Takeaways

- Master the core ideas of Lambdas and Composition through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
