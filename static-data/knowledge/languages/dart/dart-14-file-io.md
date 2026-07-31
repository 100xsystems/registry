---
{
  "title": "File I/O and dart:io",
  "description": "Reading and writing files, and environment access.",
  "type": "lesson",
  "order": 14,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Read and write text files",
    "Read lines asynchronously",
    "Work with directories",
    "Access environment variables and args"
  ],
  "knowledge_refs": [
    "dart/dart-14-file-io"
  ],
  "prerequisites": [
    "DART-11"
  ],
  "references": [
    {
      "title": "Dart — dart:io Library",
      "url": "https://api.dart.dev/stable/dart-io/dart-io-library.html"
    },
    {
      "title": "Dart — File Class",
      "url": "https://api.dart.dev/stable/dart-io/File-class.html"
    },
    {
      "title": "Dart — Command-Line Apps",
      "url": "https://dart.dev/tutorials/server/cmdline"
    }
  ]
}
---

# DART-14-FILE-IO: File I/O and dart:io

## Introduction

Reading and writing files, and environment access. By the end of this lesson you will be able to: Read and write text files; Read lines asynchronously; Work with directories; Access environment variables and args.

## Key Concepts

### 1. Read and write text files

Target: Read and write text files. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```dart
// write and read text
import 'dart:io';
void main() {
  var file = File("data.txt");
  file.writeAsStringSync("line one\nline two\n");
  var text = file.readAsStringSync();
  var lines = file.readAsLinesSync();
  print(text);
  print(lines);
}
```
### 2. Read lines asynchronously

Target: Read lines asynchronously. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```dart
// async file I/O
import 'dart:io';
Future<void> main() async {
  var file = File("data.txt");
  await file.writeAsString("async write\n");
  var lines = await file.readAsLines();
  print(lines);
  await file.delete();
}
```
### 3. Work with directories

Target: Work with directories. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```dart
// directories
import 'dart:io';
void main() {
  var dir = Directory(".");
  var entries = dir.listSync(recursive: false);
  for (var e in entries.take(3)) {
    print(e.path);
  }
  print("cwd: ${Directory.current.path}");
}
```
### 4. Access environment variables and args

Target: Access environment variables and args. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```dart
// env + args
import 'dart:io';
void main(List<String> args) {
  print("args: $args");
  print("HOME: ${Platform.environment["HOME"] ?? "unknown"}");
  print("OS: ${Platform.operatingSystem}");
}
```

## Practice Questions

1. What is the key idea behind "File I/O and dart:io"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain File I/O and dart:io with analogies and real-world examples"
1. "Show me common mistakes beginners make with File I/O and dart:io"
1. "Provide advanced patterns and performance considerations for File I/O and dart:io"

## Key Takeaways

- Master the core ideas of File I/O and dart:io through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
