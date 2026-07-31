---
{
  "title": "Testing with Dart",
  "description": "Unit tests, matchers, and test organization.",
  "type": "lesson",
  "order": 17,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write unit tests with the test package",
    "Use matchers for readable assertions",
    "Test async code",
    "Run tests with the Dart CLI"
  ],
  "knowledge_refs": [
    "dart/dart-17-testing"
  ],
  "prerequisites": [
    "DART-16"
  ],
  "references": [
    {
      "title": "Dart — Testing",
      "url": "https://dart.dev/libraries/testing"
    },
    {
      "title": "test package — GitHub",
      "url": "https://github.com/dart-lang/test"
    },
    {
      "title": "Dart — Test API",
      "url": "https://pub.dev/documentation/test/latest/"
    }
  ]
}
---

# DART-17-TESTING: Testing with Dart

## Introduction

Unit tests, matchers, and test organization. By the end of this lesson you will be able to: Write unit tests with the test package; Use matchers for readable assertions; Test async code; Run tests with the Dart CLI.

## Key Concepts

### 1. Write unit tests with the test package

Target: Write unit tests with the test package. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```dart
// unit test basics
import 'package:test/test.dart';
void main() {
  test("addition works", () {
    expect(2 + 2, equals(4));
  });
}
```
### 2. Use matchers for readable assertions

Target: Use matchers for readable assertions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```dart
// matchers
import 'package:test/test.dart';
void main() {
  test("matchers", () {
    expect("hello", contains("ell"));
    expect([1, 2, 3], hasLength(3));
    expect(3.14, closeTo(3.1, 0.1));
    expect(() => throw StateError("x"), throwsStateError);
  });
}
```
### 3. Test async code

Target: Test async code. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```dart
// async tests
import 'package:test/test.dart';
Future<String> fetch() async => "data";
void main() {
  test("async result", () async {
    expect(await fetch(), "data");
  });
}
```
### 4. Run tests with the Dart CLI

Target: Run tests with the Dart CLI. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```dart
// groups
import 'package:test/test.dart';
void main() {
  group("Calculator", () {
    test("adds", () {
      expect(2 + 2, 4);
    });
    test("multiplies", () {
      expect(3 * 3, 9);
    });
  });
}
// run: dart test
```

## Practice Questions

1. What is the key idea behind "Testing with Dart"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Testing with Dart with analogies and real-world examples"
1. "Show me common mistakes beginners make with Testing with Dart"
1. "Provide advanced patterns and performance considerations for Testing with Dart"

## Key Takeaways

- Master the core ideas of Testing with Dart through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
