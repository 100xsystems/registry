---
{
  "title": "Concurrency: async/await",
  "description": "Async functions, tasks, and structured concurrency.",
  "type": "lesson",
  "order": 15,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Mark functions async and await results",
    "Run work in parallel with async-let",
    "Group tasks with TaskGroup",
    "Understand the MainActor context"
  ],
  "knowledge_refs": [
    "swift/swift-15-concurrency"
  ],
  "prerequisites": [
    "SWIFT-14"
  ],
  "references": [
    {
      "title": "Swift Book — Concurrency",
      "url": "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/"
    },
    {
      "title": "Apple — Task",
      "url": "https://developer.apple.com/documentation/swift/task"
    },
    {
      "title": "Swift Book — Structured Concurrency",
      "url": "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/#Structured-Concurrency"
    }
  ]
}
---

# SWIFT-15-CONCURRENCY: Concurrency: async/await

## Introduction

Async functions, tasks, and structured concurrency. By the end of this lesson you will be able to: Mark functions async and await results; Run work in parallel with async-let; Group tasks with TaskGroup; Understand the MainActor context.

## Key Concepts

### 1. Mark functions async and await results

Target: Mark functions async and await results. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```swift
import Foundation
// async function
func fetchUser() async -> String {
    try? await Task.sleep(nanoseconds: 100_000_000)
    return "Alice"
}
// top-level entry point
func main() async {
    let user = await fetchUser()
    print("user: \(user)")
}
await main()
```
### 2. Run work in parallel with async-let

Target: Run work in parallel with async-let. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```swift
// async-let for parallel work
func fetch(_ id: Int) async -> Int { id * id }
func main2() async {
    async let a = fetch(3)
    async let b = fetch(4)
    let sum = await a + await b
    print("parallel sum: \(sum)")  // 25
}
await main2()
```
### 3. Group tasks with TaskGroup

Target: Group tasks with TaskGroup. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```swift
// TaskGroup
func sumAll(_ nums: [Int]) async -> Int {
    await withTaskGroup(of: Int.self) { group in
        for n in nums {
            group.addTask { n * n }
        }
        var total = 0
        for await v in group { total += v }
        return total
    }
}
func main3() async {
    print(await sumAll([1, 2, 3, 4]))  // 30
}
await main3()
```
### 4. Understand the MainActor context

Target: Understand the MainActor context. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```swift
// MainActor isolation
import Foundation
@MainActor
final class ViewModel {
    private(set) var items: [String] = []
    func load() async {
        try? await Task.sleep(nanoseconds: 10_000_000)
        items = ["a", "b"]
    }
}
func main4() async {
    let vm = ViewModel()
    await vm.load()
    print(await vm.items)
}
await main4()
```

## Practice Questions

1. What is the key idea behind "Concurrency: async/await"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Concurrency: async/await with analogies and real-world examples"
1. "Show me common mistakes beginners make with Concurrency: async/await"
1. "Provide advanced patterns and performance considerations for Concurrency: async/await"

## Key Takeaways

- Master the core ideas of Concurrency: async/await through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
