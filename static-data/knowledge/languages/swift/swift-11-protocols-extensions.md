---
{
  "title": "Protocols and Extensions",
  "description": "Protocols, conformances, and extension-driven design.",
  "type": "lesson",
  "order": 11,
  "duration": "75 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define and conform to protocols",
    "Compose requirements with protocol inheritance",
    "Extend types with protocols and methods",
    "Provide default implementations"
  ],
  "knowledge_refs": [
    "swift/swift-11-protocols-extensions"
  ],
  "prerequisites": [
    "SWIFT-09"
  ],
  "references": [
    {
      "title": "Swift Book — Protocols",
      "url": "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/protocols/"
    },
    {
      "title": "Swift Book — Extensions",
      "url": "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/extensions/"
    },
    {
      "title": "Swift Book — Protocol-Oriented Programming",
      "url": "https://developer.apple.com/videos/play/wwdc2015/408/"
    }
  ]
}
---

# SWIFT-11-PROTOCOLS-EXTENSIONS: Protocols and Extensions

## Introduction

Protocols, conformances, and extension-driven design. By the end of this lesson you will be able to: Define and conform to protocols; Compose requirements with protocol inheritance; Extend types with protocols and methods; Provide default implementations.

## Key Concepts

### 1. Define and conform to protocols

Target: Define and conform to protocols. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```swift
// protocol + conformance
protocol Describable {
    var summary: String { get }
}
struct Order: Describable {
    let id: Int
    var summary: String { "order #\(id)" }
}
let o = Order(id: 42)
print(o.summary)
```
### 2. Compose requirements with protocol inheritance

Target: Compose requirements with protocol inheritance. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```swift
// protocol inheritance
protocol Named {
    var name: String { get }
}
protocol Greetable: Named {
    func greet() -> String
}
extension Greetable {
    func greet() -> String { "Hello, \(name)!" }
}
struct User: Greetable {
    let name: String
}
print(User(name: "Alice").greet())
```
### 3. Extend types with protocols and methods

Target: Extend types with protocols and methods. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```swift
// extensions add behavior
protocol Togglable {
    mutating func toggle()
}
extension Bool: Togglable {
    mutating func toggle() { self = !self }
}
var flag = true
flag.toggle()
print(flag)  // false
```
### 4. Provide default implementations

Target: Provide default implementations. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```swift
// default implementations + collections of protocols
protocol Shape {
    var area: Double { get }
    func describe() -> String
}
extension Shape {
    func describe() -> String { "area = \(area)" }
}
struct Circle: Shape { let r: Double; var area: Double { .pi * r * r } }
let shapes: [any Shape] = [Circle(r: 2)]
for s in shapes { print(s.describe()) }
```

## Practice Questions

1. What is the key idea behind "Protocols and Extensions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Protocols and Extensions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Protocols and Extensions"
1. "Provide advanced patterns and performance considerations for Protocols and Extensions"

## Key Takeaways

- Master the core ideas of Protocols and Extensions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
