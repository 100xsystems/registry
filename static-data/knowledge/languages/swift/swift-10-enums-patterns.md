---
{
  "title": "Enums and Pattern Matching",
  "description": "Enumerations with associated values and pattern matching.",
  "type": "lesson",
  "order": 10,
  "duration": "75 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define enums with raw and associated values",
    "Match with switch and if case",
    "Use Optionals through pattern matching",
    "Write recursive enums"
  ],
  "knowledge_refs": [
    "swift/swift-10-enums-patterns"
  ],
  "prerequisites": [
    "SWIFT-06"
  ],
  "references": [
    {
      "title": "Swift Book — Enumerations",
      "url": "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/enumerations/"
    },
    {
      "title": "Swift Book — Patterns",
      "url": "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/patterns/"
    },
    {
      "title": "Swift Book — Optional Binding",
      "url": "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/thebasics/#Optional-Binding"
    }
  ]
}
---

# SWIFT-10-ENUMS-PATTERNS: Enums and Pattern Matching

## Introduction

Enumerations with associated values and pattern matching. By the end of this lesson you will be able to: Define enums with raw and associated values; Match with switch and if case; Use Optionals through pattern matching; Write recursive enums.

## Key Concepts

### 1. Define enums with raw and associated values

Target: Define enums with raw and associated values. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```swift
// enums with raw values
enum Direction: String {
    case north, south, east, west
}
let d = Direction.north
print(d.rawValue)          // "north"
print(Direction(rawValue: "east")!)  // .east
```
### 2. Match with switch and if case

Target: Match with switch and if case. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```swift
// associated values
enum Result {
    case success(Int)
    case failure(String)
}
let r = Result.success(200)
switch r {
case .success(let code): print("ok \(code)")
case .failure(let msg):  print("err \(msg)")
}
```
### 3. Use Optionals through pattern matching

Target: Use Optionals through pattern matching. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```swift
// if case and guard case
let value: Result = .failure("timeout")
if case .failure(let msg) = value {
    print("failed: \(msg)")
}
func describe(_ r: Result) -> String {
    if case .success(let code) = r, code >= 200, code < 300 {
        return "successful request"
    }
    return "other"
}
print(describe(value))
```
### 4. Write recursive enums

Target: Write recursive enums. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```swift
// recursive enums
indirect enum Expression {
    case number(Int)
    case add(Expression, Expression)
    case multiply(Expression, Expression)
}
let e = Expression.add(.number(2), .multiply(.number(3), .number(4)))
func eval(_ ex: Expression) -> Int {
    switch ex {
    case .number(let n): return n
    case .add(let a, let b): return eval(a) + eval(b)
    case .multiply(let a, let b): return eval(a) * eval(b)
    }
}
print(eval(e))  // 14
```

## Practice Questions

1. What is the key idea behind "Enums and Pattern Matching"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Enums and Pattern Matching with analogies and real-world examples"
1. "Show me common mistakes beginners make with Enums and Pattern Matching"
1. "Provide advanced patterns and performance considerations for Enums and Pattern Matching"

## Key Takeaways

- Master the core ideas of Enums and Pattern Matching through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
