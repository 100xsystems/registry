---
{
  "title": "Performance and Optimization",
  "description": "Value semantics, COW, profiling, and measurement.",
  "type": "lesson",
  "order": 21,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Optimize value type copying with COW",
    "Use lazy properties and caching",
    "Measure with continuous benchmarks",
    "Profile with Instruments"
  ],
  "knowledge_refs": [
    "swift/swift-21-performance"
  ],
  "prerequisites": [
    "SWIFT-17"
  ],
  "references": [
    {
      "title": "Apple — Swift Performance WWDC",
      "url": "https://developer.apple.com/videos/play/wwdc2016/416/"
    },
    {
      "title": "Swift Book — Lazy Stored Properties",
      "url": "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/properties/#Lazy-Stored-Properties"
    },
    {
      "title": "Apple — Continuous Benchmarking",
      "url": "https://developer.apple.com/documentation/xcode/improving-your-app-s-performance"
    }
  ]
}
---

# SWIFT-21-PERFORMANCE: Performance and Optimization

## Introduction

Value semantics, COW, profiling, and measurement. By the end of this lesson you will be able to: Optimize value type copying with COW; Use lazy properties and caching; Measure with continuous benchmarks; Profile with Instruments.

## Key Concepts

### 1. Optimize value type copying with COW

Target: Optimize value type copying with COW. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```swift
// value types are cheap thanks to COW
var large = Array(repeating: 0, count: 1_000_000)
var copy = large            // shares storage — O(1)
copy[0] = 1                 // only now does it copy
print(large[0], copy[0])    // 0 1
```
### 2. Use lazy properties and caching

Target: Use lazy properties and caching. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```swift
// lazy properties compute once
struct Report {
    let rows: [Int]
    lazy var total: Int = rows.reduce(0, +)
    init(rows: [Int]) { self.rows = rows }
}
var rep = Report(rows: [1, 2, 3])
print(rep.total)  // computed now, cached after
```
### 3. Measure with continuous benchmarks

Target: Measure with continuous benchmarks. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```swift
// prefer value types for performance
struct ValueBox { var x: Int; var y: Int }
let boxes = (0..<100).map { ValueBox(x: $0, y: $0 * 2) }
print(boxes.count, MemoryLayout<ValueBox>.size)  // 16 bytes
```
### 4. Profile with Instruments

Target: Profile with Instruments. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```swift
// benchmarking a function
import Foundation
let start = DispatchTime.now()
let sum = (0..<1_000_000).reduce(0, +)
let elapsed = DispatchTime.now().uptimeNanoseconds - start.uptimeNanoseconds
print("sum=\(sum) in \(Double(elapsed) / 1e6) ms")
```

## Practice Questions

1. What is the key idea behind "Performance and Optimization"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Performance and Optimization with analogies and real-world examples"
1. "Show me common mistakes beginners make with Performance and Optimization"
1. "Provide advanced patterns and performance considerations for Performance and Optimization"

## Key Takeaways

- Master the core ideas of Performance and Optimization through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
