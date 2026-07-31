---
{
  "title": "Getting Started with Dart",
  "description": "Install Dart, run scripts, and meet the Dart VM.",
  "type": "lesson",
  "order": 1,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Install Dart and run your first program",
    "Use print and string interpolation",
    "Pass command-line arguments",
    "Understand the Dart VM and compilation modes"
  ],
  "knowledge_refs": [
    "dart/dart-01-getting-started"
  ],
  "prerequisites": [],
  "references": [
    {
      "title": "Dart — Get Started",
      "url": "https://dart.dev/get-started"
    },
    {
      "title": "Dart — Language Tour",
      "url": "https://dart.dev/language"
    },
    {
      "title": "DartPad",
      "url": "https://dartpad.dev/"
    }
  ]
}
---

# DART-01-GETTING-STARTED: Getting Started with Dart

## Introduction

Install Dart, run scripts, and meet the Dart VM. By the end of this lesson you will be able to: Install Dart and run your first program; Use print and string interpolation; Pass command-line arguments; Understand the Dart VM and compilation modes.

## Key Concepts

### 1. Install Dart and run your first program

Target: Install Dart and run your first program. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```dart
// hello.dart — run: dart run hello.dart
void main() {
  print("Hello, 100x Systems!");
  var name = "Dart";
  print("Welcome to $name!");
}
```
### 2. Use print and string interpolation

Target: Use print and string interpolation. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```dart
// command-line arguments
void main(List<String> args) {
  print("args: $args");
  var who = args.isNotEmpty ? args[0] : "world";
  print("Hello, $who");
}
// dart run hello.dart alice -> args: [alice]
```
### 3. Pass command-line arguments

Target: Pass command-line arguments. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```dart
// compilation modes
// JIT: dart run (fast startup, used in dev)
// AOT: dart compile exe (native, fast runtime)
// Wasm: dart compile wasm
// JS: dart compile js
void main() {
  print("VM ready");
}
```
### 4. Understand the Dart VM and compilation modes

Target: Understand the Dart VM and compilation modes. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```dart
// package layout
// my_app/
//   pubspec.yaml
//   bin/main.dart     -> executable
//   lib/              -> public library
//   test/             -> tests
void main() {
  print("standard layout");
}
```

## Practice Questions

1. What is the key idea behind "Getting Started with Dart"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with Dart with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with Dart"
1. "Provide advanced patterns and performance considerations for Getting Started with Dart"

## Key Takeaways

- Master the core ideas of Getting Started with Dart through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
