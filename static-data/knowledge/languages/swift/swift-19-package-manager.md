---
{
  "title": "Swift Package Manager",
  "description": "Package.swift, dependencies, and building libraries.",
  "type": "lesson",
  "order": 19,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Declare packages and products",
    "Add and resolve dependencies",
    "Build executables and libraries",
    "Share packages with the ecosystem"
  ],
  "knowledge_refs": [
    "swift/swift-19-package-manager"
  ],
  "prerequisites": [
    "SWIFT-01"
  ],
  "references": [
    {
      "title": "Swift Package Manager — Getting Started",
      "url": "https://www.swift.org/getting-started/package-manager/"
    },
    {
      "title": "Swift Package Manager — PackageDescription",
      "url": "https://docs.swift.org/package-manager/PackageDescription/index.html"
    },
    {
      "title": "Swift Package Index",
      "url": "https://swiftpackageindex.com/"
    }
  ]
}
---

# SWIFT-19-PACKAGE-MANAGER: Swift Package Manager

## Introduction

Package.swift, dependencies, and building libraries. By the end of this lesson you will be able to: Declare packages and products; Add and resolve dependencies; Build executables and libraries; Share packages with the ecosystem.

## Key Concepts

### 1. Declare packages and products

Target: Declare packages and products. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```swift
// swift package init --type executable
// Package.swift:
//   // swift-tools-version: 5.10
//   import PackageDescription
//   let package = Package(
//       name: "MyLib",
//       targets: [.executableTarget(name: "MyLib")]
//   )
print("package created")
```
### 2. Add and resolve dependencies

Target: Add and resolve dependencies. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```swift
// adding dependencies
// Package.swift:
//   dependencies: [
//       .package(url: "https://github.com/apple/swift-algorithms.git",
//                from: "1.2.0")
//   ],
//   targets: [.executableTarget(name: "MyLib",
//               dependencies: [.product(name: "Algorithms",
//                               package: "swift-algorithms")])]
```
### 3. Build executables and libraries

Target: Build executables and libraries. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```swift
import Algorithms
// after adding the Algorithms dependency
let array = [1, 2, 3, 4]
for chunk in array.chunks(ofCount: 2) {
    print(chunk, terminator: " ")
}
print()
```
### 4. Share packages with the ecosystem

Target: Share packages with the ecosystem. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```swift
// command-line workflow
// swift build       -> compile
// swift run         -> execute
// swift test        -> run tests
// swift package update   -> refresh deps
// swift package dump-package
print("build, run, test, update")
```

## Practice Questions

1. What is the key idea behind "Swift Package Manager"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Swift Package Manager with analogies and real-world examples"
1. "Show me common mistakes beginners make with Swift Package Manager"
1. "Provide advanced patterns and performance considerations for Swift Package Manager"

## Key Takeaways

- Master the core ideas of Swift Package Manager through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
