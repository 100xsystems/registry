---
{
  "title": "Numbers and Math",
  "description": "Integer types, floating point, overflow behavior, and math.",
  "type": "lesson",
  "order": 3,
  "duration": "50 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use Int, Int32, Int64, and UInt appropriately",
    "Handle Double vs Float precision",
    "Use overflow operators deliberately",
    "Leverage the Foundation math functions"
  ],
  "knowledge_refs": [
    "swift/swift-03-numbers-math"
  ],
  "prerequisites": [
    "SWIFT-02"
  ],
  "references": [
    {
      "title": "Swift Book — Integers",
      "url": "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/thebasics/#Integer-Bounds"
    },
    {
      "title": "Swift Book — Numeric Literals",
      "url": "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/thebasics/#Numeric-Literals"
    },
    {
      "title": "Apple — Double",
      "url": "https://developer.apple.com/documentation/swift/double"
    }
  ]
}
---

# SWIFT-03-NUMBERS-MATH: Numbers and Math

## Introduction

Integer types, floating point, overflow behavior, and math. By the end of this lesson you will be able to: Use Int, Int32, Int64, and UInt appropriately; Handle Double vs Float precision; Use overflow operators deliberately; Leverage the Foundation math functions.

## Key Concepts

### 1. Use Int, Int32, Int64, and UInt appropriately

Target: Use Int, Int32, Int64, and UInt appropriately. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```swift
// integer types
let small: Int8 = 127        // -128...127
let big: Int64 = 9_223_372_036_854_775_807
let unsigned: UInt = 42
print(Int8.min, Int8.max, Int64.max)
print(big)
```
### 2. Handle Double vs Float precision

Target: Handle Double vs Float precision. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```swift
// floating point
let d: Double = 0.1 + 0.2     // 0.30000000000000004
print(d)
let f: Float = 0.1 + 0.2
print(f)
// compare with tolerance
print(abs(d - 0.3) < 1e-9 ? "close" : "not close")
```
### 3. Use overflow operators deliberately

Target: Use overflow operators deliberately. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```swift
// overflow operators
var max = Int8.max           // 127
// max += 1                   // traps: arithmetic overflow
let wrapped = Int8.max &+ 1  // -128 (deliberate)
print(wrapped)
```
### 4. Leverage the Foundation math functions

Target: Leverage the Foundation math functions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```swift
import Foundation
let r = sqrt(16.0)              // 4.0
let p = pow(2.0, 10.0)          // 1024.0
let rnd = Int.random(in: 1...6) // inclusive range
print(r, p, rnd)
```

## Practice Questions

1. What is the key idea behind "Numbers and Math"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Numbers and Math with analogies and real-world examples"
1. "Show me common mistakes beginners make with Numbers and Math"
1. "Provide advanced patterns and performance considerations for Numbers and Math"

## Key Takeaways

- Master the core ideas of Numbers and Math through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
