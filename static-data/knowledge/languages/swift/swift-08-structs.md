---
{
  "title": "Structs and Value Semantics",
  "description": "Structures, properties, methods, and copy-on-write behavior.",
  "type": "lesson",
  "order": 8,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define structs with stored and computed properties",
    "Use memberwise initializers",
    "Mutate values with mutating methods",
    "Reason about value semantics and COW"
  ],
  "knowledge_refs": [
    "swift/swift-08-structs"
  ],
  "prerequisites": [
    "SWIFT-07"
  ],
  "references": [
    {
      "title": "Swift Book — Structures and Classes",
      "url": "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/structuresandclasses/"
    },
    {
      "title": "Swift Book — Properties",
      "url": "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/properties/"
    },
    {
      "title": "Swift Book — Methods",
      "url": "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/methods/"
    }
  ]
}
---

# SWIFT-08-STRUCTS: Structs and Value Semantics

## Introduction

Structures, properties, methods, and copy-on-write behavior. By the end of this lesson you will be able to: Define structs with stored and computed properties; Use memberwise initializers; Mutate values with mutating methods; Reason about value semantics and COW.

## Key Concepts

### 1. Define structs with stored and computed properties

Target: Define structs with stored and computed properties. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```swift
// struct with stored + computed properties
struct Rectangle {
    var width: Double
    var height: Double
    var area: Double { width * height }
}
let r = Rectangle(width: 3, height: 4)
print(r.area)  // 12.0
```
### 2. Use memberwise initializers

Target: Use memberwise initializers. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```swift
import Foundation
// memberwise init + custom init
struct Point {
    var x: Double
    var y: Double
    init(x: Double) { self.x = x; self.y = 0 }
    func distance(to other: Point) -> Double {
        hypot(x - other.x, y - other.y)
    }
}
let p = Point(x: 3)
print(p.distance(to: Point(x: 0, y: 4)))
```
### 3. Mutate values with mutating methods

Target: Mutate values with mutating methods. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```swift
// mutating methods
struct Counter {
    private(set) var count = 0
    mutating func increment() { count += 1 }
    mutating func reset() { count = 0 }
}
var c = Counter()
c.increment(); c.increment()
print(c.count)  // 2
```
### 4. Reason about value semantics and COW

Target: Reason about value semantics and COW. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```swift
// value semantics — copies are independent
var a = [1, 2, 3]
var b = a
b.append(4)
print(a)  // [1, 2, 3]
print(b)  // [1, 2, 3, 4] (COW keeps memory efficient)
```

## Practice Questions

1. What is the key idea behind "Structs and Value Semantics"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Structs and Value Semantics with analogies and real-world examples"
1. "Show me common mistakes beginners make with Structs and Value Semantics"
1. "Provide advanced patterns and performance considerations for Structs and Value Semantics"

## Key Takeaways

- Master the core ideas of Structs and Value Semantics through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
