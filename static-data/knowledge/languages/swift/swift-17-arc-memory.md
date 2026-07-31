---
{
  "title": "Memory Management and ARC",
  "description": "Automatic Reference Counting, strong cycles, and weak references.",
  "type": "lesson",
  "order": 17,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Understand how ARC manages class instances",
    "Break strong reference cycles with weak",
    "Use unowned references carefully",
    "Avoid closure capture cycles"
  ],
  "knowledge_refs": [
    "swift/swift-17-arc-memory"
  ],
  "prerequisites": [
    "SWIFT-09"
  ],
  "references": [
    {
      "title": "Swift Book — Automatic Reference Counting",
      "url": "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/automaticreferencecounting/"
    },
    {
      "title": "Swift Book — Resolving Cycles",
      "url": "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/automaticreferencecounting/#Resolving-Strong-Reference-Cycles-Between-Class-Instances"
    },
    {
      "title": "Apple — Memory Safety",
      "url": "https://developer.apple.com/documentation/swift/memory-safety"
    }
  ]
}
---

# SWIFT-17-ARC-MEMORY: Memory Management and ARC

## Introduction

Automatic Reference Counting, strong cycles, and weak references. By the end of this lesson you will be able to: Understand how ARC manages class instances; Break strong reference cycles with weak; Use unowned references carefully; Avoid closure capture cycles.

## Key Concepts

### 1. Understand how ARC manages class instances

Target: Understand how ARC manages class instances. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```swift
// ARC tracks references
class Token {
    let id: String
    init(id: String) { self.id = id }
    deinit { print("token \(id) freed") }
}
var t: Token? = Token(id: "a1")
var t2 = t          // +1 strong ref
t = nil
print("still alive") // t2 holds it
t2 = nil            // now deinit fires
```
### 2. Break strong reference cycles with weak

Target: Break strong reference cycles with weak. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```swift
// strong reference cycle
class Owner {
    var pet: Pet?
    deinit { print("owner gone") }
}
class Pet {
    weak var owner: Owner?   // weak breaks the cycle
    deinit { print("pet gone") }
}
var owner: Owner? = Owner()
var pet: Pet? = Pet()
owner?.pet = pet
pet?.owner = owner
owner = nil
pet = nil  // both deinit now (with weak)
```
### 3. Use unowned references carefully

Target: Use unowned references carefully. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```swift
// unowned — assume the other is alive
class Client {
    var card: CreditCard?
    deinit { print("client gone") }
}
class CreditCard {
    unowned let client: Client
    init(client: Client) { self.client = client }
    deinit { print("card gone") }
}
var alice: Client? = Client()
alice?.card = CreditCard(client: alice!)
alice = nil  // both deinit
```
### 4. Avoid closure capture cycles

Target: Avoid closure capture cycles. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```swift
// closure capture cycles
class Downloader {
    var progress: ((Double) -> Void)?
    func start() {
        progress = { [weak self] p in
            print("progress \(p)")
            _ = self   // weak self avoids the cycle
        }
    }
}
var dl: Downloader? = Downloader()
dl?.start()
dl = nil
```

## Practice Questions

1. What is the key idea behind "Memory Management and ARC"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Memory Management and ARC with analogies and real-world examples"
1. "Show me common mistakes beginners make with Memory Management and ARC"
1. "Provide advanced patterns and performance considerations for Memory Management and ARC"

## Key Takeaways

- Master the core ideas of Memory Management and ARC through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
