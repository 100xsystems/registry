---
{
  "title": "Functions and Closures",
  "description": "Function declarations, labels, and closure capture.",
  "type": "lesson",
  "order": 7,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Define functions with labels and defaults",
    "Pass functions as values",
    "Write closures and capture context",
    "Use trailing closure syntax"
  ],
  "knowledge_refs": [
    "swift/swift-07-functions-closures"
  ],
  "prerequisites": [
    "SWIFT-05"
  ],
  "references": [
    {
      "title": "Swift Book — Functions",
      "url": "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/functions/"
    },
    {
      "title": "Swift Book — Closures",
      "url": "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/closures/"
    },
    {
      "title": "Swift Book — Capture Lists",
      "url": "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/closures/#Capturing-Values"
    }
  ]
}
---

# SWIFT-07-FUNCTIONS-CLOSURES: Functions and Closures

## Introduction

Function declarations, labels, and closure capture. By the end of this lesson you will be able to: Define functions with labels and defaults; Pass functions as values; Write closures and capture context; Use trailing closure syntax.

## Key Concepts

### 1. Define functions with labels and defaults

Target: Define functions with labels and defaults. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```swift
// function declarations
func greet(name: String, times: Int = 1) -> String {
    return String(repeating: "Hi \(name)! ", count: times)
}
print(greet(name: "Alice"))        // default times
print(greet(name: "Bob", times: 2))
print(greet(name: "Cal", times: 3))
```
### 2. Pass functions as values

Target: Pass functions as values. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```swift
// argument labels and _
func add(_ a: Int, _ b: Int) -> Int { a + b }
func distance(from x: Int, to y: Int) -> Int { abs(x - y) }
print(add(2, 3))
print(distance(from: 1, to: 10))
```
### 3. Write closures and capture context

Target: Write closures and capture context. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```swift
// variadic and inout
func sum(_ numbers: Int...) -> Int {
    numbers.reduce(0, +)
}
print(sum(1, 2, 3, 4))
func increment(_ value: inout Int) {
    value += 1
}
var n = 41
increment(&n)
print(n)  // 42
```
### 4. Use trailing closure syntax

Target: Use trailing closure syntax. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```swift
// closures and trailing syntax
let names = ["Zoe", "Amy", "Bo"]
let sorted = names.sorted { $0 < $1 }
let mapped = names.map { $0.uppercased() }
print(sorted, mapped)
// capture context
var counter = 0
let incrementer = { counter += 1 }
incrementer(); incrementer()
print(counter)  // 2
```

## Practice Questions

1. What is the key idea behind "Functions and Closures"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Functions and Closures with analogies and real-world examples"
1. "Show me common mistakes beginners make with Functions and Closures"
1. "Provide advanced patterns and performance considerations for Functions and Closures"

## Key Takeaways

- Master the core ideas of Functions and Closures through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
