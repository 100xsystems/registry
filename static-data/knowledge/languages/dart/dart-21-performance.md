---
{
  "title": "Performance and Best Practices",
  "description": "Event loop, allocation, profiling, and idiomatic code.",
  "type": "lesson",
  "order": 21,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Understand the event loop model",
    "Minimize allocations in hot paths",
    "Apply idiomatic best practices",
    "Profile with the Dart VM tools"
  ],
  "knowledge_refs": [
    "dart/dart-21-performance"
  ],
  "prerequisites": [
    "DART-20"
  ],
  "references": [
    {
      "title": "Dart — Event Loop",
      "url": "https://dart.dev/articles/archive/event-loop"
    },
    {
      "title": "Dart — Performance",
      "url": "https://dart.dev/tools/dart-devtools"
    },
    {
      "title": "Dart — Effective Dart",
      "url": "https://dart.dev/effective-dart"
    }
  ]
}
---

# DART-21-PERFORMANCE: Performance and Best Practices

## Introduction

Event loop, allocation, profiling, and idiomatic code. By the end of this lesson you will be able to: Understand the event loop model; Minimize allocations in hot paths; Apply idiomatic best practices; Profile with the Dart VM tools.

## Key Concepts

### 1. Understand the event loop model

Target: Understand the event loop model. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```dart
// event loop model
import 'dart:async';
void main() {
  print("start");
  Future.delayed(Duration.zero, () => print("event"));
  scheduleMicrotask(() => print("microtask"));
  print("end");
}
// start, end, microtask, event
```
### 2. Minimize allocations in hot paths

Target: Minimize allocations in hot paths. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```dart
// avoid allocations in hot paths
void main() {
  // reuse buffers in loops
  var sb = StringBuffer();
  for (var i = 0; i < 1000; i++) {
    sb..write(i)..write(", ");
  }
  print(sb.length);
  // prefer growable=false when size is known
  var list = List<int>.filled(3, 0, growable: false);
  print(list);
}
```
### 3. Apply idiomatic best practices

Target: Apply idiomatic best practices. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```dart
// idiomatic code
void main() {
  var nums = [1, 2, 3, 4];
  // cascade + spread + collection if
  var result = [
    ...nums.where((n) => n.isEven),
    if (nums.length > 2) 99,
  ];
  print(result);  // [2, 4, 99]
  // null-aware operators
  String? name;
  var shown = name?.toUpperCase() ?? "anonymous";
  print(shown);
}
```
### 4. Profile with the Dart VM tools

Target: Profile with the Dart VM tools. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```dart
// profiling
// dart run --observe bin/app.dart
// opens VM Service for CPU + memory profiling
// dart devtools          -> DevTools UI
// dart run --profile     -> AOT-ish profiling mode
void main() {
  print("devtools: dart devtools");
}
```

## Practice Questions

1. What is the key idea behind "Performance and Best Practices"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Performance and Best Practices with analogies and real-world examples"
1. "Show me common mistakes beginners make with Performance and Best Practices"
1. "Provide advanced patterns and performance considerations for Performance and Best Practices"

## Key Takeaways

- Master the core ideas of Performance and Best Practices through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
