---
{
  "title": "Isolates and Concurrency",
  "description": "Isolates, message passing, and parallel execution.",
  "type": "lesson",
  "order": 16,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Spawn isolates for parallel work",
    "Send and receive messages",
    "Use Isolate.run for one-off tasks",
    "Share memory patterns safely"
  ],
  "knowledge_refs": [
    "dart/dart-16-isolates"
  ],
  "prerequisites": [
    "DART-15"
  ],
  "references": [
    {
      "title": "Dart — Concurrency",
      "url": "https://dart.dev/language/concurrency"
    },
    {
      "title": "Dart — Isolate Class",
      "url": "https://api.dart.dev/stable/dart-isolate/Isolate-class.html"
    },
    {
      "title": "Dart — Isolates Codelab",
      "url": "https://dart.dev/codelabs/isolates"
    }
  ]
}
---

# DART-16-ISOLATES: Isolates and Concurrency

## Introduction

Isolates, message passing, and parallel execution. By the end of this lesson you will be able to: Spawn isolates for parallel work; Send and receive messages; Use Isolate.run for one-off tasks; Share memory patterns safely.

## Key Concepts

### 1. Spawn isolates for parallel work

Target: Spawn isolates for parallel work. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```dart
// Isolate.run (one-off work)
import 'dart:isolate';
Future<void> main() async {
  var result = await Isolate.run(() {
    var sum = 0;
    for (var i = 1; i <= 1000000; i++) {
      sum += i;
    }
    return sum;
  });
  print(result);  // runs on another isolate
}
```
### 2. Send and receive messages

Target: Send and receive messages. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```dart
// spawn with SendPort
import 'dart:isolate';
void worker(SendPort port) {
  port.send("hello from isolate");
}
Future<void> main() async {
  var receive = ReceivePort();
  await Isolate.spawn(worker, receive.sendPort);
  var msg = await receive.first;
  print(msg);
  receive.close();
}
```
### 3. Use Isolate.run for one-off tasks

Target: Use Isolate.run for one-off tasks. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```dart
// two-way messaging
import 'dart:isolate';
void worker(SendPort replyTo) {
  var receive = ReceivePort();
  replyTo.send(receive.sendPort);   // hand back our port
  receive.listen((msg) {
    replyTo.send("echo: $msg");
  });
}
Future<void> main() async {
  var control = ReceivePort();
  await Isolate.spawn(worker, control.sendPort);
  var workerPort = await control.first as SendPort;
  workerPort.send("ping");
  print(await control.first);   // echo: ping
  control.close();
}
```
### 4. Share memory patterns safely

Target: Share memory patterns safely. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```dart
// event loop note
void main() {
  print("1: sync");
  Future(() => print("2: event"));
  Future.microtask(() => print("3: microtask first"));
  scheduleMicrotask(() => print("4: microtask"));
  print("5: sync end");
}
// order: 1, 5, 3, 4, 2 (microtasks FIFO, then events)
```

## Practice Questions

1. What is the key idea behind "Isolates and Concurrency"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Isolates and Concurrency with analogies and real-world examples"
1. "Show me common mistakes beginners make with Isolates and Concurrency"
1. "Provide advanced patterns and performance considerations for Isolates and Concurrency"

## Key Takeaways

- Master the core ideas of Isolates and Concurrency through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
