---
{
  "title": "Error Handling",
  "description": "Throwing functions, do-catch, and error propagation.",
  "type": "lesson",
  "order": 13,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define error types conforming to Error",
    "Throw and catch errors",
    "Propagate errors with try",
    "Clean up with defer"
  ],
  "knowledge_refs": [
    "swift/swift-13-error-handling"
  ],
  "prerequisites": [
    "SWIFT-12"
  ],
  "references": [
    {
      "title": "Swift Book — Error Handling",
      "url": "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/errorhandling/"
    },
    {
      "title": "Apple — Error Protocol",
      "url": "https://developer.apple.com/documentation/swift/error"
    },
    {
      "title": "Swift Book — Defer",
      "url": "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/errorhandling/#Specifying-Cleanup-Actions"
    }
  ]
}
---

# SWIFT-13-ERROR-HANDLING: Error Handling

## Introduction

Throwing functions, do-catch, and error propagation. By the end of this lesson you will be able to: Define error types conforming to Error; Throw and catch errors; Propagate errors with try; Clean up with defer.

## Key Concepts

### 1. Define error types conforming to Error

Target: Define error types conforming to Error. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```swift
// define + throw + catch
enum FileError: Error {
    case notFound
    case unreadable(String)
}
func loadFile(_ path: String) throws -> String {
    guard path != "" else { throw FileError.notFound }
    if path.hasSuffix(".txt") { return "contents of \(path)" }
    throw FileError.unreadable(path)
}
do {
    let text = try loadFile("notes.txt")
    print(text)
} catch FileError.notFound {
    print("no such file")
} catch {
    print("other error: \(error)")
}
```
### 2. Throw and catch errors

Target: Throw and catch errors. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```swift
// propagating with try
typealias FileLoader = (String) throws -> String
func safeLoad(_ path: String, using loader: FileLoader) -> String? {
    try? loader(path)   // converts error to nil
}
let result = safeLoad("a.txt", using: loadFile)
print(result ?? "failed")
```
### 3. Propagate errors with try

Target: Propagate errors with try. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```swift
// try? and try!
let a = try? loadFile("missing.txt")  // nil
// let b = try! loadFile("")            // crashes if it throws
print(a ?? "nil from try?")
```
### 4. Clean up with defer

Target: Clean up with defer. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```swift
// defer for cleanup
func process(_ path: String) throws {
    print("open resource")
    defer { print("close resource") }
    let data = try loadFile(path)
    print("got \(data.count) chars")
}
try? process("data.txt")
```

## Practice Questions

1. What is the key idea behind "Error Handling"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Error Handling with analogies and real-world examples"
1. "Show me common mistakes beginners make with Error Handling"
1. "Provide advanced patterns and performance considerations for Error Handling"

## Key Takeaways

- Master the core ideas of Error Handling through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
