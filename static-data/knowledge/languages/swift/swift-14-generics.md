---
{
  "title": "Generics",
  "description": "Generic functions, types, and constraints.",
  "type": "lesson",
  "order": 14,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Write generic functions",
    "Design generic types",
    "Constrain with protocol requirements",
    "Use associated types and where clauses"
  ],
  "knowledge_refs": [
    "swift/swift-14-generics"
  ],
  "prerequisites": [
    "SWIFT-11"
  ],
  "references": [
    {
      "title": "Swift Book — Generics",
      "url": "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/generics/"
    },
    {
      "title": "Swift Book — Associated Types",
      "url": "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/generics/#Associated-Types"
    },
    {
      "title": "Swift Book — Where Clauses",
      "url": "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/generics/#Generic-Where-Clauses"
    }
  ]
}
---

# SWIFT-14-GENERICS: Generics

## Introduction

Generic functions, types, and constraints. By the end of this lesson you will be able to: Write generic functions; Design generic types; Constrain with protocol requirements; Use associated types and where clauses.

## Key Concepts

### 1. Write generic functions

Target: Write generic functions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```swift
// generic functions
func swapValues<T>(_ a: inout T, _ b: inout T) {
    let tmp = a; a = b; b = tmp
}
var x = 1, y = 2
swapValues(&x, &y)
print(x, y)  // 2 1
var s1 = "a", s2 = "b"
swapValues(&s1, &s2)
print(s1, s2)
```
### 2. Design generic types

Target: Design generic types. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```swift
// generic types
struct Stack<Element> {
    private var items: [Element] = []
    mutating func push(_ e: Element) { items.append(e) }
    mutating func pop() -> Element? { items.popLast() }
    var count: Int { items.count }
}
var stack = Stack<Int>()
stack.push(1); stack.push(2)
print(stack.pop() ?? 0, stack.count)  // 2 1
```
### 3. Constrain with protocol requirements

Target: Constrain with protocol requirements. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```swift
// constraints
func largest<T: Comparable>(_ a: T, _ b: T) -> T {
    a > b ? a : b
}
print(largest(3, 7))        // 7
print(largest("cat", "dog")) // "dog"
```
### 4. Use associated types and where clauses

Target: Use associated types and where clauses. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```swift
// associated types + where
protocol Container {
    associatedtype Item
    mutating func append(_ item: Item)
    var count: Int { get }
}
extension Array: Container {}
func firstElement<C: Container>(_ c: C) -> C.Item? {
    guard c.count > 0, let items = c as? [C.Item] else { return nil }
    return items[0]
}
let arr = [10, 20, 30]
print(firstElement(arr) ?? 0)  // 10
```

## Practice Questions

1. What is the key idea behind "Generics"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Generics with analogies and real-world examples"
1. "Show me common mistakes beginners make with Generics"
1. "Provide advanced patterns and performance considerations for Generics"

## Key Takeaways

- Master the core ideas of Generics through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
