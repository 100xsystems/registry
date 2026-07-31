---
{
  "title": "Exceptions and Error Handling",
  "description": "throw, try-catch, finally, and custom exceptions.",
  "type": "lesson",
  "order": 11,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Throw exceptions with throw",
    "Catch with try-catch and rethrow",
    "Run cleanup with finally",
    "Define custom exception types"
  ],
  "knowledge_refs": [
    "dart/dart-11-exceptions"
  ],
  "prerequisites": [
    "DART-10"
  ],
  "references": [
    {
      "title": "Dart — Error Handling",
      "url": "https://dart.dev/language/error-handling"
    },
    {
      "title": "Dart — Exceptions API",
      "url": "https://api.dart.dev/stable/dart-core/Exception-class.html"
    },
    {
      "title": "Dart — Error Class",
      "url": "https://api.dart.dev/stable/dart-core/Error-class.html"
    }
  ]
}
---

# DART-11-EXCEPTIONS: Exceptions and Error Handling

## Introduction

throw, try-catch, finally, and custom exceptions. By the end of this lesson you will be able to: Throw exceptions with throw; Catch with try-catch and rethrow; Run cleanup with finally; Define custom exception types.

## Key Concepts

### 1. Throw exceptions with throw

Target: Throw exceptions with throw. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```dart
// try-catch
void main() {
  try {
    var n = int.parse("abc");
    print(n);
  } on FormatException catch (e) {
    print("bad number: $e");
  }
}
```
### 2. Catch with try-catch and rethrow

Target: Catch with try-catch and rethrow. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```dart
// catch all + finally
void main() {
  try {
    throw StateError("boom");
  } catch (e, st) {
    print("caught: $e");
    print("stack: ${st.toString().split("\n").first}");
  } finally {
    print("cleanup");
  }
}
```
### 3. Run cleanup with finally

Target: Run cleanup with finally. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```dart
// custom exceptions + rethrow
class PaymentFailed implements Exception {
  final String message;
  PaymentFailed(this.message);
  @override
  String toString() => "PaymentFailed: $message";
}
void charge(double amount) {
  if (amount > 100) throw PaymentFailed("limit exceeded");
}
void main() {
  try {
    charge(500);
  } on PaymentFailed catch (e) {
    print(e);
  }
}
```
### 4. Define custom exception types

Target: Define custom exception types. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```dart
// run-time errors
void main() {
  try {
    var list = <int>[];
    print(list.first);
  } on RangeError catch (e) {
    print("range: $e");
  } on StateError catch (e) {
    print("state: $e");
  }
}
```

## Practice Questions

1. What is the key idea behind "Exceptions and Error Handling"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Exceptions and Error Handling with analogies and real-world examples"
1. "Show me common mistakes beginners make with Exceptions and Error Handling"
1. "Provide advanced patterns and performance considerations for Exceptions and Error Handling"

## Key Takeaways

- Master the core ideas of Exceptions and Error Handling through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
