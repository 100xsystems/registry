---
{
  "title": "Asynchronous Programming",
  "description": "Future, async, await, and async* generators.",
  "type": "lesson",
  "order": 13,
  "duration": "75 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create and await Futures",
    "Handle errors in async code",
    "Run tasks concurrently with Future.wait",
    "Yield values with Streams"
  ],
  "knowledge_refs": [
    "dart/dart-13-async"
  ],
  "prerequisites": [
    "DART-12"
  ],
  "references": [
    {
      "title": "Dart — Async Programming",
      "url": "https://dart.dev/language/async"
    },
    {
      "title": "Dart — Future API",
      "url": "https://api.dart.dev/stable/dart-async/Future-class.html"
    },
    {
      "title": "Dart — Asynchronous Codelab",
      "url": "https://dart.dev/codelabs/async-await"
    }
  ]
}
---

# DART-13-ASYNC: Asynchronous Programming

## Introduction

Future, async, await, and async* generators. By the end of this lesson you will be able to: Create and await Futures; Handle errors in async code; Run tasks concurrently with Future.wait; Yield values with Streams.

## Key Concepts

### 1. Create and await Futures

Target: Create and await Futures. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```dart
// Future + async/await
Future<String> fetchUser() async {
  await Future.delayed(Duration(milliseconds: 100));
  return "Alice";
}
Future<void> main() async {
  var user = await fetchUser();
  print("user: $user");
}
```
### 2. Handle errors in async code

Target: Handle errors in async code. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```dart
// async error handling
Future<int> parse(String raw) async {
  if (raw.isEmpty) throw FormatException("empty");
  return int.parse(raw);
}
Future<void> main() async {
  try {
    print(await parse("42"));
  } on FormatException catch (e) {
    print("err: $e");
  }
}
```
### 3. Run tasks concurrently with Future.wait

Target: Run tasks concurrently with Future.wait. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```dart
// Future.wait
Future<int> fetch(int id) async {
  await Future.delayed(Duration(milliseconds: 10));
  return id * id;
}
Future<void> main() async {
  var results = await Future.wait([fetch(3), fetch(4)]);
  print(results);         // [9, 16]
  print(results.fold(0, (a, b) => a + b));  // 25
}
```
### 4. Yield values with Streams

Target: Yield values with Streams. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```dart
// async* generator
Stream<int> countdown(int from) async* {
  for (var i = from; i > 0; i--) {
    yield i;
    await Future.delayed(Duration(milliseconds: 10));
  }
}
Future<void> main() async {
  await for (var n in countdown(3)) {
    print(n);   // 3 2 1
  }
}
```

## Practice Questions

1. What is the key idea behind "Asynchronous Programming"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Asynchronous Programming with analogies and real-world examples"
1. "Show me common mistakes beginners make with Asynchronous Programming"
1. "Provide advanced patterns and performance considerations for Asynchronous Programming"

## Key Takeaways

- Master the core ideas of Asynchronous Programming through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
