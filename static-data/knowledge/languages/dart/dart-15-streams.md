---
{
  "title": "Streams and Reactive Data",
  "description": "Streams, broadcast streams, and stream operators.",
  "type": "lesson",
  "order": 15,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Listen to single-subscription streams",
    "Use broadcast streams for fan-out",
    "Transform with map, where, and fold",
    "Control backpressure"
  ],
  "knowledge_refs": [
    "dart/dart-15-streams"
  ],
  "prerequisites": [
    "DART-13"
  ],
  "references": [
    {
      "title": "Dart — Streams",
      "url": "https://dart.dev/libraries/async/streams"
    },
    {
      "title": "Dart — Stream API",
      "url": "https://api.dart.dev/stable/dart-async/Stream-class.html"
    },
    {
      "title": "Dart — Streams Codelab",
      "url": "https://dart.dev/codelabs/async-await"
    }
  ]
}
---

# DART-15-STREAMS: Streams and Reactive Data

## Introduction

Streams, broadcast streams, and stream operators. By the end of this lesson you will be able to: Listen to single-subscription streams; Use broadcast streams for fan-out; Transform with map, where, and fold; Control backpressure.

## Key Concepts

### 1. Listen to single-subscription streams

Target: Listen to single-subscription streams. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```dart
// single-subscription stream
import 'dart:async';
Future<void> main() async {
  var stream = Stream.fromIterable([1, 2, 3]);
  await for (var n in stream) {
    print(n);
  }
}
```
### 2. Use broadcast streams for fan-out

Target: Use broadcast streams for fan-out. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```dart
// broadcast stream
import 'dart:async';
Future<void> main() async {
  var controller = StreamController<int>.broadcast();
  controller.stream.listen((n) => print("a: $n"));
  controller.stream.listen((n) => print("b: $n"));
  controller.add(1);
  controller.add(2);
  await controller.close();
}
```
### 3. Transform with map, where, and fold

Target: Transform with map, where, and fold. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```dart
// stream operators
import 'dart:async';
Future<void> main() async {
  var squares = Stream.fromIterable([1, 2, 3, 4])
      .map((n) => n * n)
      .where((n) => n.isEven);
  await for (var n in squares) {
    print(n);  // 4 16
  }
}
```
### 4. Control backpressure

Target: Control backpressure. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```dart
// stream from future and manual control
import 'dart:async';
Future<void> main() async {
  var fromFuture = Stream.fromFuture(Future.value("done"));
  await for (var v in fromFuture) {
    print(v);
  }
  var periodic = Stream.periodic(
    const Duration(milliseconds: 10),
    (i) => i * i,
  ).take(3);
  await for (var n in periodic) {
    print(n);  // 0 1 4
  }
}
```

## Practice Questions

1. What is the key idea behind "Streams and Reactive Data"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Streams and Reactive Data with analogies and real-world examples"
1. "Show me common mistakes beginners make with Streams and Reactive Data"
1. "Provide advanced patterns and performance considerations for Streams and Reactive Data"

## Key Takeaways

- Master the core ideas of Streams and Reactive Data through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
