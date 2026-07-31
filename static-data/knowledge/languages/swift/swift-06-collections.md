---
{
  "title": "Collections: Array, Dictionary, Set",
  "description": "The three collection types and their algorithms.",
  "type": "lesson",
  "order": 6,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Build and mutate arrays",
    "Look up and store data in dictionaries",
    "Use sets for membership and uniqueness",
    "Apply map, filter, and reduce"
  ],
  "knowledge_refs": [
    "swift/swift-06-collections"
  ],
  "prerequisites": [
    "SWIFT-05"
  ],
  "references": [
    {
      "title": "Swift Book — Collection Types",
      "url": "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/collectiontypes/"
    },
    {
      "title": "Apple — Array",
      "url": "https://developer.apple.com/documentation/swift/array"
    },
    {
      "title": "Swift Book — Higher-Order Functions",
      "url": "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/collectiontypes/#Iterating-Over-a-Dictionary"
    }
  ]
}
---

# SWIFT-06-COLLECTIONS: Collections: Array, Dictionary, Set

## Introduction

The three collection types and their algorithms. By the end of this lesson you will be able to: Build and mutate arrays; Look up and store data in dictionaries; Use sets for membership and uniqueness; Apply map, filter, and reduce.

## Key Concepts

### 1. Build and mutate arrays

Target: Build and mutate arrays. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```swift
// arrays
var fruits = ["apple", "banana", "cherry"]
fruits.append("date")
fruits.insert("fig", at: 0)
fruits.remove(at: 1)
print(fruits)
print(fruits[0], fruits.count)
```
### 2. Look up and store data in dictionaries

Target: Look up and store data in dictionaries. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```swift
// dictionaries
var user: [String: Any] = ["name": "Alice", "age": 30]
user["admin"] = true
user["age"] = nil        // removes the key
if let name = user["name"] as? String {
    print("hello \(name)")
}
```
### 3. Use sets for membership and uniqueness

Target: Use sets for membership and uniqueness. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```swift
// sets
var tags: Set = ["swift", "ios", "server"]
tags.insert("vapor")
let swift = tags.contains("swift")     // true
let a: Set = [1, 2, 3]
let b: Set = [2, 3, 4]
print(a.union(b))        // [1, 2, 3, 4]
print(a.intersection(b)) // [2, 3]
```
### 4. Apply map, filter, and reduce

Target: Apply map, filter, and reduce. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```swift
// higher-order functions
let nums = [1, 2, 3, 4, 5]
let doubled = nums.map { $0 * 2 }
let evens = nums.filter { $0 % 2 == 0 }
let sum = nums.reduce(0, +)
print(doubled, evens, sum)
```

## Practice Questions

1. What is the key idea behind "Collections: Array, Dictionary, Set"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Collections: Array, Dictionary, Set with analogies and real-world examples"
1. "Show me common mistakes beginners make with Collections: Array, Dictionary, Set"
1. "Provide advanced patterns and performance considerations for Collections: Array, Dictionary, Set"

## Key Takeaways

- Master the core ideas of Collections: Array, Dictionary, Set through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
