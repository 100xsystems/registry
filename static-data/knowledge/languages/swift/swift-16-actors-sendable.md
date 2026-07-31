---
{
  "title": "Actors and Sendable",
  "description": "Actor isolation, Sendable, and safe shared state.",
  "type": "lesson",
  "order": 16,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Isolate mutable state with actors",
    "Call actor methods with await",
    "Annotate types with Sendable",
    "Avoid data races by design"
  ],
  "knowledge_refs": [
    "swift/swift-16-actors-sendable"
  ],
  "prerequisites": [
    "SWIFT-15"
  ],
  "references": [
    {
      "title": "Swift Book — Actors",
      "url": "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/#Actors"
    },
    {
      "title": "Apple — Sendable",
      "url": "https://developer.apple.com/documentation/swift/sendable"
    },
    {
      "title": "Swift Book — Sendable Conformance",
      "url": "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/#Sendable"
    }
  ]
}
---

# SWIFT-16-ACTORS-SENDABLE: Actors and Sendable

## Introduction

Actor isolation, Sendable, and safe shared state. By the end of this lesson you will be able to: Isolate mutable state with actors; Call actor methods with await; Annotate types with Sendable; Avoid data races by design.

## Key Concepts

### 1. Isolate mutable state with actors

Target: Isolate mutable state with actors. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```swift
// actor isolation
actor BankAccount {
    private var balance = 0
    func deposit(_ amount: Int) { balance += amount }
    func withdraw(_ amount: Int) -> Bool {
        guard balance >= amount else { return false }
        balance -= amount
        return true
    }
    func currentBalance() -> Int { balance }
}
func main5() async {
    let acc = BankAccount()
    await acc.deposit(100)
    print(await acc.currentBalance())  // 100
}
await main5()
```
### 2. Call actor methods with await

Target: Call actor methods with await. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```swift
// Sendable value types
struct Invoice: Sendable {
    let id: Int
    let total: Double
}
// structs of value types are automatically Sendable
func process(_ invoice: Invoice) { print(invoice.id) }
let inv = Invoice(id: 1, total: 99.0)
process(inv)
```
### 3. Annotate types with Sendable

Target: Annotate types with Sendable. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```swift
// global actors
import Foundation
@globalActor
struct MyActor {
    static let shared = MyActor()
}
@MyActor
func isolatedWork() { print("on MyActor") }
func main6() async {
    await isolatedWork()
}
await main6()
```
### 4. Avoid data races by design

Target: Avoid data races by design. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```swift
// data race prevention with actors
actor Counter2 {
    private var value = 0
    func increment() -> Int {
        value += 1
        return value
    }
}
func main7() async {
    let c = Counter2()
    await withTaskGroup(of: Int.self) { group in
        for _ in 0..<10 {
            group.addTask { await c.increment() }
        }
        for await v in group { print(v, terminator: " ") }
    }
}
await main7()  // 1...10 — no race
```

## Practice Questions

1. What is the key idea behind "Actors and Sendable"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Actors and Sendable with analogies and real-world examples"
1. "Show me common mistakes beginners make with Actors and Sendable"
1. "Provide advanced patterns and performance considerations for Actors and Sendable"

## Key Takeaways

- Master the core ideas of Actors and Sendable through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
