---
{
  "title": "Strings and String Manipulation",
  "description": "String literals, interpolation, Unicode, and the string API.",
  "type": "lesson",
  "order": 4,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Build strings with literals and interpolation",
    "Understand String as a collection of Characters",
    "Manipulate strings with the standard API",
    "Handle Unicode and substrings safely"
  ],
  "knowledge_refs": [
    "swift/swift-04-strings"
  ],
  "prerequisites": [
    "SWIFT-02"
  ],
  "references": [
    {
      "title": "Swift Book — Strings and Characters",
      "url": "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/stringsandcharacters/"
    },
    {
      "title": "Apple — String",
      "url": "https://developer.apple.com/documentation/swift/string"
    },
    {
      "title": "Swift Book — Substrings",
      "url": "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/stringsandcharacters/#Substrings"
    }
  ]
}
---

# SWIFT-04-STRINGS: Strings and String Manipulation

## Introduction

String literals, interpolation, Unicode, and the string API. By the end of this lesson you will be able to: Build strings with literals and interpolation; Understand String as a collection of Characters; Manipulate strings with the standard API; Handle Unicode and substrings safely.

## Key Concepts

### 1. Build strings with literals and interpolation

Target: Build strings with literals and interpolation. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```swift
// string literals and interpolation
let name = "Alice"
let age = 30
let msg = "\(name) is \(age) years old"
let multiline = """
Line one
Line two
"""
print(msg, multiline)
```
### 2. Understand String as a collection of Characters

Target: Understand String as a collection of Characters. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```swift
// strings are collections of Characters
let s = "héllo"
print(s.count)          // 5 (graphemes, not bytes)
for ch in s { print(ch, terminator: " ") }
print()
```
### 3. Manipulate strings with the standard API

Target: Manipulate strings with the standard API. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```swift
// common operations
var s = "Hello, World"
print(s.uppercased())          // HELLO, WORLD
print(s.lowercased())
print(s.hasPrefix("Hello"))    // true
print(s.split(separator: ",")) // ["Hello", " World"]
print(s.replacingOccurrences(of: "World", with: "Swift"))
```
### 4. Handle Unicode and substrings safely

Target: Handle Unicode and substrings safely. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```swift
// substrings share storage
let full = "The quick brown fox"
let first = full.prefix(3)      // Substring "The"
let word = String(first)        // convert to String to keep
print(word, full.count, first.count)
```

## Practice Questions

1. What is the key idea behind "Strings and String Manipulation"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Strings and String Manipulation with analogies and real-world examples"
1. "Show me common mistakes beginners make with Strings and String Manipulation"
1. "Provide advanced patterns and performance considerations for Strings and String Manipulation"

## Key Takeaways

- Master the core ideas of Strings and String Manipulation through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
