---
{
  "title": "Getting Started with Swift",
  "description": "Install Swift, run scripts, and understand the SwiftPM workflow.",
  "type": "lesson",
  "order": 1,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Install Swift and run your first script",
    "Use print and string interpolation",
    "Work with CommandLine arguments",
    "Understand the SwiftPM project layout"
  ],
  "knowledge_refs": [
    "swift/swift-01-getting-started"
  ],
  "prerequisites": [],
  "references": [
    {
      "title": "Swift.org — Getting Started",
      "url": "https://www.swift.org/getting-started/"
    },
    {
      "title": "Swift Book — A Swift Tour",
      "url": "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/guidedtour/"
    },
    {
      "title": "Swift Package Manager",
      "url": "https://www.swift.org/package-manager/"
    }
  ]
}
---

# SWIFT-01-GETTING-STARTED: Getting Started with Swift

## Introduction

Install Swift, run scripts, and understand the SwiftPM workflow. By the end of this lesson you will be able to: Install Swift and run your first script; Use print and string interpolation; Work with CommandLine arguments; Understand the SwiftPM project layout.

## Key Concepts

### 1. Install Swift and run your first script

Target: Install Swift and run your first script. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```swift
// hello.swift — run with: swift hello.swift
print("Hello, 100x Systems!")
let name = "Swift"
print("Welcome to \(name)!")
```
### 2. Use print and string interpolation

Target: Use print and string interpolation. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```swift
// CommandLine arguments
for arg in CommandLine.arguments {
    print("arg: \(arg)")
}
// swift hello.swift alice bob -> prints script path + args
```
### 3. Work with CommandLine arguments

Target: Work with CommandLine arguments. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```swift
import Foundation
let info = ProcessInfo.processInfo
print("OS: \(info.operatingSystemVersionString)")
print("PID: \(info.processIdentifier)")
let env = info.environment
print("HOME: \(env["HOME"] ?? "unknown")")
```
### 4. Understand the SwiftPM project layout

Target: Understand the SwiftPM project layout. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```swift
// SwiftPM layout
// Package.swift at root:
//   swift build   -> .build/debug/
//   swift run     -> run the executable
//   swift test    -> run tests
// Sources/MyLib/ and Tests/MyLibTests/ mirror each other.
```

## Practice Questions

1. What is the key idea behind "Getting Started with Swift"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with Swift with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with Swift"
1. "Provide advanced patterns and performance considerations for Getting Started with Swift"

## Key Takeaways

- Master the core ideas of Getting Started with Swift through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
