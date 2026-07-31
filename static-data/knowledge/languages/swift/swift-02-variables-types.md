---
{
  "title": "Variables and Data Types",
  "description": "Constants, variables, type inference, and the core value types.",
  "type": "lesson",
  "order": 2,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Declare variables with var and constants with let",
    "Let the compiler infer types",
    "Work with Int, Double, String, Bool, and Character",
    "Convert between types safely"
  ],
  "knowledge_refs": [
    "swift/swift-02-variables-types"
  ],
  "prerequisites": [
    "SWIFT-01"
  ],
  "references": [
    {
      "title": "Swift Book — The Basics",
      "url": "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/thebasics/"
    },
    {
      "title": "Swift Book — Basic Operators",
      "url": "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/basicoperators/"
    },
    {
      "title": "Apple — Swift Data Types",
      "url": "https://developer.apple.com/documentation/swift/data-types"
    }
  ]
}
---

# SWIFT-02-VARIABLES-TYPES: Variables and Data Types

## Introduction

Constants, variables, type inference, and the core value types. By the end of this lesson you will be able to: Declare variables with var and constants with let; Let the compiler infer types; Work with Int, Double, String, Bool, and Character; Convert between types safely.

## Key Concepts

### 1. Declare variables with var and constants with let

Target: Declare variables with var and constants with let. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```swift
// var vs let
var score = 42          // inferred Int
let maxScore = 100      // constant
score += 1
// maxScore = 101       // error: cannot assign to let
print(score, maxScore)
```
### 2. Let the compiler infer types

Target: Let the compiler infer types. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```swift
// type inference
let count = 10                 // Int
let pi = 3.14                  // Double
let greeting = "hi"            // String
let ok = true                  // Bool
let ch: Character = "A"        // explicit annotation
print(type(of: count), type(of: pi))
```
### 3. Work with Int, Double, String, Bool, and Character

Target: Work with Int, Double, String, Bool, and Character. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```swift
// explicit types and conversion
let a: Int = 5
let b: Double = 2.5
let sum = Double(a) + b        // 7.5
let text = String(sum)         // "7.5"
let rounded = Int(b)           // 2 (truncates)
print(sum, text, rounded)
```
### 4. Convert between types safely

Target: Convert between types safely. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```swift
// type safety — no implicit conversions
var x = 3
var y = 0.14
// let z = x + y   // error: Binary operator + cannot be applied
let z = Double(x) + y
print(z)  // 3.14
```

## Practice Questions

1. What is the key idea behind "Variables and Data Types"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Variables and Data Types with analogies and real-world examples"
1. "Show me common mistakes beginners make with Variables and Data Types"
1. "Provide advanced patterns and performance considerations for Variables and Data Types"

## Key Takeaways

- Master the core ideas of Variables and Data Types through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
