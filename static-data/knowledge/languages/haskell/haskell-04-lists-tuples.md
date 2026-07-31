---
{
  "title": "Lists and Tuples",
  "description": "List construction, ranges, list functions, and tuples.",
  "type": "lesson",
  "order": 4,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Build lists with : and ranges",
    "Use map, filter, and folds on lists",
    "Access elements safely with head/tail/!!",
    "Pair values with tuples"
  ],
  "knowledge_refs": [
    "haskell/haskell-04-lists-tuples"
  ],
  "prerequisites": [
    "HASKELL-03"
  ],
  "references": [
    {
      "title": "Learn You a Haskell — Starting Out",
      "url": "https://learnyouahaskell.github.io/starting-out.html"
    },
    {
      "title": "Hackage — Data.List",
      "url": "https://hackage.haskell.org/package/base/docs/Data-List.html"
    },
    {
      "title": "Haskell Wiki — List Processing",
      "url": "https://wiki.haskell.org/How_to_work_on_lists"
    }
  ]
}
---

# HASKELL-04-LISTS-TUPLES: Lists and Tuples

## Introduction

List construction, ranges, list functions, and tuples. By the end of this lesson you will be able to: Build lists with : and ranges; Use map, filter, and folds on lists; Access elements safely with head/tail/!!; Pair values with tuples.

## Key Concepts

### 1. Build lists with : and ranges

Target: Build lists with : and ranges. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```haskell
-- list construction
main :: IO ()
main = do
  let xs = 1 : 2 : 3 : []    -- cons
  print xs
  print [1, 2, 3]            -- sugar
  print [1..10]              -- range
  print [1,3..9]             -- step
```
### 2. Use map, filter, and folds on lists

Target: Use map, filter, and folds on lists. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```haskell
-- basic list functions
main :: IO ()
main = do
  print (head [1, 2, 3])    -- 1
  print (tail [1, 2, 3])    -- [2,3]
  print (length [1..5])     -- 5
  print (sum [1..5])        -- 15
  print (reverse [1..4])
```
### 3. Access elements safely with head/tail/!!

Target: Access elements safely with head/tail/!!. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```haskell
-- map and filter
main :: IO ()
main = do
  print (map (*2) [1..5])      -- [2,4,6,8,10]
  print (filter even [1..10])  -- [2,4,6,8,10]
  print (take 3 [1..])         -- [1,2,3] (lazy!)
```
### 4. Pair values with tuples

Target: Pair values with tuples. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```haskell
-- tuples
main :: IO ()
main = do
  let pair = (1, "one")
  print (fst pair)          -- 1
  print (snd pair)          -- "one"
  print (zip [1, 2] ["a", "b"])  -- [(1,"a"),(2,"b")]
```

## Practice Questions

1. What is the key idea behind "Lists and Tuples"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Lists and Tuples with analogies and real-world examples"
1. "Show me common mistakes beginners make with Lists and Tuples"
1. "Provide advanced patterns and performance considerations for Lists and Tuples"

## Key Takeaways

- Master the core ideas of Lists and Tuples through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
