---
{
  "title": "Algebraic Data Types",
  "description": "data declarations, sum types, and product types.",
  "type": "lesson",
  "order": 11,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Define data types with constructors",
    "Compose sum and product types",
    "Use record syntax",
    "Derive typeclass instances"
  ],
  "knowledge_refs": [
    "haskell/haskell-11-algebraic-data"
  ],
  "prerequisites": [
    "HASKELL-10"
  ],
  "references": [
    {
      "title": "Learn You a Haskell — Making Our Own Types",
      "url": "https://learnyouahaskell.github.io/making-our-own-types-and-typeclasses.html"
    },
    {
      "title": "Haskell Wiki — Algebraic Data Type",
      "url": "https://wiki.haskell.org/Algebraic_data_type"
    },
    {
      "title": "Haskell Report — Data Declarations",
      "url": "https://www.haskell.org/onlinereport/haskell2010/haskellch4.html#x10-700004.2"
    }
  ]
}
---

# HASKELL-11-ALGEBRAIC-DATA: Algebraic Data Types

## Introduction

data declarations, sum types, and product types. By the end of this lesson you will be able to: Define data types with constructors; Compose sum and product types; Use record syntax; Derive typeclass instances.

## Key Concepts

### 1. Define data types with constructors

Target: Define data types with constructors. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```haskell
-- data declaration
-- sum type: a value is one of these
data Bool2 = True2 | False2

data Direction = North | South | East | West

data Shape = Circle Double | Rect Double Double

main :: IO ()
main = print "data types defined"
```
### 2. Compose sum and product types

Target: Compose sum and product types. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```haskell
-- product types (record syntax)
data Person = Person
  { name :: String
  , age  :: Int
  } deriving (Show)

main :: IO ()
main = do
  let alice = Person { name = "Alice", age = 30 }
  print (name alice)   -- "Alice"
  print alice
```
### 3. Use record syntax

Target: Use record syntax. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```haskell
-- recursion in types
data Tree a = Empty | Node a (Tree a) (Tree a)

treeSum :: Tree Int -> Int
treeSum Empty = 0
treeSum (Node v l r) = v + treeSum l + treeSum r

main :: IO ()
main = do
  let t = Node 1 (Node 2 Empty Empty) (Node 3 Empty Empty)
  print (treeSum t)  -- 6
```
### 4. Derive typeclass instances

Target: Derive typeclass instances. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```haskell
-- deriving instances
data Point = Point Int Int
  deriving (Eq, Ord, Show, Read)

main :: IO ()
main = do
  print (Point 1 2 == Point 1 2)  -- True
  print (Point 1 2 < Point 3 4)   -- True
  print (read "Point 5 6" :: Point)
```

## Practice Questions

1. What is the key idea behind "Algebraic Data Types"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Algebraic Data Types with analogies and real-world examples"
1. "Show me common mistakes beginners make with Algebraic Data Types"
1. "Provide advanced patterns and performance considerations for Algebraic Data Types"

## Key Takeaways

- Master the core ideas of Algebraic Data Types through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
