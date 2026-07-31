---
{
  "title": "Testing with XCTest and Swift Testing",
  "description": "Unit tests, assertions, and test organization.",
  "type": "lesson",
  "order": 20,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write XCTest test classes",
    "Use Swift Testing macros",
    "Structure tests with setup and teardown",
    "Run tests from the command line"
  ],
  "knowledge_refs": [
    "swift/swift-20-testing"
  ],
  "prerequisites": [
    "SWIFT-19"
  ],
  "references": [
    {
      "title": "Apple — XCTest",
      "url": "https://developer.apple.com/documentation/xctest"
    },
    {
      "title": "Swift Testing — Documentation",
      "url": "https://developer.apple.com/documentation/testing"
    },
    {
      "title": "Swift Package Manager — Testing",
      "url": "https://www.swift.org/getting-started/testing/"
    }
  ]
}
---

# SWIFT-20-TESTING: Testing with XCTest and Swift Testing

## Introduction

Unit tests, assertions, and test organization. By the end of this lesson you will be able to: Write XCTest test classes; Use Swift Testing macros; Structure tests with setup and teardown; Run tests from the command line.

## Key Concepts

### 1. Write XCTest test classes

Target: Write XCTest test classes. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```swift
import XCTest
final class CalculatorTests: XCTestCase {
    func testAddition() {
        XCTAssertEqual(2 + 2, 4)
        XCTAssertTrue(2 + 2 == 4)
    }
    func testOptional() {
        let value: Int? = 7
        XCTAssertNotNil(value)
        XCTAssertEqual(value, 7)
    }
}
```
### 2. Use Swift Testing macros

Target: Use Swift Testing macros. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```swift
import Testing
// Swift Testing (Xcode 16+) uses @Test instead of classes
@Test func arithmetic() {
    #expect(3 * 3 == 9)
}
@Test(arguments: [1, 2, 3])
func tableDriven(n: Int) {
    #expect(n > 0)
}
```
### 3. Structure tests with setup and teardown

Target: Structure tests with setup and teardown. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```swift
import XCTest
final class SetupTests: XCTestCase {
    var values: [Int] = []
    override func setUp() {
        super.setUp()
        values = [1, 2, 3]
    }
    func testCount() {
        XCTAssertEqual(values.count, 3)
    }
}
```
### 4. Run tests from the command line

Target: Run tests from the command line. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```swift
import XCTest
// performance measurement
final class PerfTests: XCTestCase {
    func testSortPerformance() {
        let data = (0..<10_000).shuffled()
        measure {
            _ = data.sorted()
        }
    }
}
```

## Practice Questions

1. What is the key idea behind "Testing with XCTest and Swift Testing"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Testing with XCTest and Swift Testing with analogies and real-world examples"
1. "Show me common mistakes beginners make with Testing with XCTest and Swift Testing"
1. "Provide advanced patterns and performance considerations for Testing with XCTest and Swift Testing"

## Key Takeaways

- Master the core ideas of Testing with XCTest and Swift Testing through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
