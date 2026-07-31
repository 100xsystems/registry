---
{
  "title": "Codable and File I/O",
  "description": "Codable, JSON encoding/decoding, and the file system.",
  "type": "lesson",
  "order": 18,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Conform types to Codable",
    "Encode and decode JSON",
    "Read and write files with FileManager",
    "Handle dates and custom keys"
  ],
  "knowledge_refs": [
    "swift/swift-18-codable-files"
  ],
  "prerequisites": [
    "SWIFT-12"
  ],
  "references": [
    {
      "title": "Apple — Codable",
      "url": "https://developer.apple.com/documentation/swift/codable"
    },
    {
      "title": "Apple — JSONEncoder",
      "url": "https://developer.apple.com/documentation/foundation/jsonencoder"
    },
    {
      "title": "Apple — FileManager",
      "url": "https://developer.apple.com/documentation/foundation/filemanager"
    }
  ]
}
---

# SWIFT-18-CODABLE-FILES: Codable and File I/O

## Introduction

Codable, JSON encoding/decoding, and the file system. By the end of this lesson you will be able to: Conform types to Codable; Encode and decode JSON; Read and write files with FileManager; Handle dates and custom keys.

## Key Concepts

### 1. Conform types to Codable

Target: Conform types to Codable. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```swift
import Foundation
// Codable conformance
struct User: Codable {
    let name: String
    let age: Int
    let tags: [String]
}
let user = User(name: "Alice", age: 30, tags: ["swift", "ios"])
```
### 2. Encode and decode JSON

Target: Encode and decode JSON. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```swift
import Foundation
// encode to JSON
let encoder = JSONEncoder()
encoder.outputFormatting = [.prettyPrinted, .sortedKeys]
let data = try encoder.encode(user)
print(String(data: data, encoding: .utf8)!)
```
### 3. Read and write files with FileManager

Target: Read and write files with FileManager. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```swift
import Foundation
// decode from JSON
let json = #"{"name":"Bob","age":25,"tags":["server"]}"#
let decoder = JSONDecoder()
let decoded = try decoder.decode(User.self, from: Data(json.utf8))
print(decoded.name, decoded.tags)
```
### 4. Handle dates and custom keys

Target: Handle dates and custom keys. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```swift
import Foundation
// continues from sample 2 (data + path)
// file I/O
let dir = FileManager.default.temporaryDirectory
let path = dir.appendingPathComponent("user.json")
try data.write(to: path)                    // write
try? FileManager.default.removeItem(at: path)  // cleanup
print(path.path)
```

## Practice Questions

1. What is the key idea behind "Codable and File I/O"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Codable and File I/O with analogies and real-world examples"
1. "Show me common mistakes beginners make with Codable and File I/O"
1. "Provide advanced patterns and performance considerations for Codable and File I/O"

## Key Takeaways

- Master the core ideas of Codable and File I/O through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
