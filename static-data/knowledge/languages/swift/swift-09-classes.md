---
{
  "title": "Classes and Reference Semantics",
  "description": "Classes, inheritance, and reference behavior.",
  "type": "lesson",
  "order": 9,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define classes with properties and methods",
    "Understand reference semantics",
    "Override methods and use super",
    "Use access control with private and internal"
  ],
  "knowledge_refs": [
    "swift/swift-09-classes"
  ],
  "prerequisites": [
    "SWIFT-08"
  ],
  "references": [
    {
      "title": "Swift Book — Classes",
      "url": "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/structuresandclasses/#Classes-Are-Reference-Types"
    },
    {
      "title": "Swift Book — Inheritance",
      "url": "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/inheritance/"
    },
    {
      "title": "Swift Book — Access Control",
      "url": "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/accesscontrol/"
    }
  ]
}
---

# SWIFT-09-CLASSES: Classes and Reference Semantics

## Introduction

Classes, inheritance, and reference behavior. By the end of this lesson you will be able to: Define classes with properties and methods; Understand reference semantics; Override methods and use super; Use access control with private and internal.

## Key Concepts

### 1. Define classes with properties and methods

Target: Define classes with properties and methods. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```swift
// class with reference semantics
class Person {
    var name: String
    init(name: String) { self.name = name }
    func greet() { print("Hi, I am \(name)") }
}
let alice = Person(name: "Alice")
let copy = alice       // SAME instance
copy.name = "Alicia"
print(alice.name)      // "Alicia" — shared state!
```
### 2. Understand reference semantics

Target: Understand reference semantics. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```swift
// inheritance
class Animal {
    let name: String
    init(name: String) { self.name = name }
    func speak() -> String { "..." }
}
class Dog: Animal {
    override func speak() -> String { "Woof!" }
}
let rex = Dog(name: "Rex")
print(rex.speak())  // Woof!
```
### 3. Override methods and use super

Target: Override methods and use super. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```swift
// deinit and lifecycle
class Logger {
    let tag: String
    init(tag: String) { self.tag = tag; print("\(tag) created") }
    deinit { print("\(tag) destroyed") }
    func log(_ s: String) { print("\(tag): \(s)") }
}
var lg: Logger? = Logger(tag: "app")
lg?.log("boot")
lg = nil  // triggers deinit
```
### 4. Use access control with private and internal

Target: Use access control with private and internal. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```swift
// access control
class Bank {
    private var balance: Int = 0
    internal var owner: String
    init(owner: String) { self.owner = owner }
    func deposit(_ amount: Int) { balance += amount }
    func currentBalance() -> Int { balance }
}
let acc = Bank(owner: "Alice")
acc.deposit(100)
print(acc.currentBalance())
```

## Practice Questions

1. What is the key idea behind "Classes and Reference Semantics"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Classes and Reference Semantics with analogies and real-world examples"
1. "Show me common mistakes beginners make with Classes and Reference Semantics"
1. "Provide advanced patterns and performance considerations for Classes and Reference Semantics"

## Key Takeaways

- Master the core ideas of Classes and Reference Semantics through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
