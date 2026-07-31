---
{
  "title": "Advanced Isolates and Compute",
  "description": "Worker pools, message ports, and CPU-bound work.",
  "type": "lesson",
  "order": 19,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Build worker pools with SendPort and ReceivePort",
    "Stream results back to the main isolate",
    "Offload CPU-heavy work",
    "Avoid blocking the event loop"
  ],
  "knowledge_refs": [
    "dart/dart-19-isolates-advanced"
  ],
  "prerequisites": [
    "DART-16"
  ],
  "references": [
    {
      "title": "Dart — ReceivePort API",
      "url": "https://api.dart.dev/stable/dart-isolate/ReceivePort-class.html"
    },
    {
      "title": "Dart — SendPort API",
      "url": "https://api.dart.dev/stable/dart-isolate/SendPort-class.html"
    },
    {
      "title": "Dart — Concurrency Patterns",
      "url": "https://dart.dev/language/concurrency#isolates"
    }
  ]
}
---

# DART-19-ISOLATES-ADVANCED: Advanced Isolates and Compute

## Introduction

Worker pools, message ports, and CPU-bound work. By the end of this lesson you will be able to: Build worker pools with SendPort and ReceivePort; Stream results back to the main isolate; Offload CPU-heavy work; Avoid blocking the event loop.

## Key Concepts

### 1. Build worker pools with SendPort and ReceivePort

Target: Build worker pools with SendPort and ReceivePort. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```dart
// worker pool pattern
import 'dart:isolate';
Future<int> computeSum(int n) async {
  return Isolate.run(() {
    var sum = 0;
    for (var i = 1; i <= n; i++) {
      sum += i;
    }
    return sum;
  });
}
Future<void> main() async {
  var results = await Future.wait([computeSum(100), computeSum(200)]);
  print(results);  // both offloaded
}
```
### 2. Stream results back to the main isolate

Target: Stream results back to the main isolate. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```dart
// streaming results
import 'dart:isolate';
void produce(SendPort port) async {
  for (var i = 1; i <= 5; i++) {
    await Future.delayed(const Duration(milliseconds: 10));
    port.send(i * i);
  }
}
Future<void> main() async {
  var receive = ReceivePort();
  await Isolate.spawn(produce, receive.sendPort);
  await for (var v in receive.take(5)) {
    print(v);
  }
  receive.close();
}
```
### 3. Offload CPU-heavy work

Target: Offload CPU-heavy work. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```dart
// CPU-bound offload
import 'dart:isolate';
Future<void> main() async {
  var before = DateTime.now();
  var heavy = await Isolate.run(() {
    var primes = <int>[];
    for (var n = 2; primes.length < 5000; n++) {
      var isPrime = true;
      for (var d = 2; d * d <= n; d++) {
        if (n % d == 0) {
          isPrime = false;
          break;
        }
      }
      if (isPrime) primes.add(n);
    }
    return primes.last;
  });
  print("last prime: $heavy");
  print("took: ${DateTime.now().difference(before)}");
}
```
### 4. Avoid blocking the event loop

Target: Avoid blocking the event loop. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```dart
// never block the event loop
import 'dart:io';
void main() {
  // File.readAsStringSync() blocks — prefer async in servers
  // Future.forEach + async reads keep the loop responsive
  print("sync vs async I/O");
}
```

## Practice Questions

1. What is the key idea behind "Advanced Isolates and Compute"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Advanced Isolates and Compute with analogies and real-world examples"
1. "Show me common mistakes beginners make with Advanced Isolates and Compute"
1. "Provide advanced patterns and performance considerations for Advanced Isolates and Compute"

## Key Takeaways

- Master the core ideas of Advanced Isolates and Compute through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
