---
{
  "title": "Control Flow",
  "description": "Conditionals, switch, and loops.",
  "type": "lesson",
  "order": 5,
  "duration": "50 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use if/else and ternary conditions",
    "Write exhaustive switch statements",
    "Iterate with for-in, while, and repeat-while",
    "Use break, continue, and labeled statements"
  ],
  "knowledge_refs": [
    "swift/swift-05-control-flow"
  ],
  "prerequisites": [
    "SWIFT-02"
  ],
  "references": [
    {
      "title": "Swift Book — Control Flow",
      "url": "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/controlflow/"
    },
    {
      "title": "Swift Book — Switch",
      "url": "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/controlflow/#Switch"
    },
    {
      "title": "Swift Book — For-In Loops",
      "url": "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/controlflow/#For-In-Loops"
    }
  ]
}
---

# SWIFT-05-CONTROL-FLOW: Control Flow

## Introduction

Conditionals, switch, and loops. By the end of this lesson you will be able to: Use if/else and ternary conditions; Write exhaustive switch statements; Iterate with for-in, while, and repeat-while; Use break, continue, and labeled statements.

## Key Concepts

### 1. Use if/else and ternary conditions

Target: Use if/else and ternary conditions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```swift
// if / else if / else
let score = 85
if score >= 90 {
    print("A")
} else if score >= 80 {
    print("B")
} else {
    print("C")
}
let pass = score >= 50 ? "pass" : "fail"
print(pass)
```
### 2. Write exhaustive switch statements

Target: Write exhaustive switch statements. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```swift
// switch must be exhaustive
let status = 404
switch status {
case 200, 204: print("ok")
case 404:      print("not found")
case 500:      print("server error")
case let code where code >= 400:
    print("client error \(code)")
default:        print("unknown")
}
```
### 3. Iterate with for-in, while, and repeat-while

Target: Iterate with for-in, while, and repeat-while. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```swift
// loops
for i in 0..<5 { print(i, terminator: "") }
print()
var n = 0
while n < 3 { n += 1 }
print(n)
repeat {
    print("once")
} while false
```
### 4. Use break, continue, and labeled statements

Target: Use break, continue, and labeled statements. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```swift
// break, continue, labels
outer: for i in 1...5 {
    for j in 1...5 {
        if j == 2 { continue }
        if i == 3 { break outer }
        print("(\(i),\(j))", terminator: " ")
    }
}
print()
```

## Practice Questions

1. What is the key idea behind "Control Flow"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Control Flow with analogies and real-world examples"
1. "Show me common mistakes beginners make with Control Flow"
1. "Provide advanced patterns and performance considerations for Control Flow"

## Key Takeaways

- Master the core ideas of Control Flow through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
