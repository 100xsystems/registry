---
{
  "title": "Packages and Pub",
  "description": "pubspec.yaml, dependencies, and the pub ecosystem.",
  "type": "lesson",
  "order": 18,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create a package with pubspec.yaml",
    "Add and manage dependencies",
    "Understand version constraints",
    "Publish and consume packages"
  ],
  "knowledge_refs": [
    "dart/dart-18-packages"
  ],
  "prerequisites": [
    "DART-01"
  ],
  "references": [
    {
      "title": "Dart — Pub",
      "url": "https://dart.dev/tools/pub"
    },
    {
      "title": "Dart — Packages",
      "url": "https://dart.dev/guides/packages"
    },
    {
      "title": "pub.dev",
      "url": "https://pub.dev/"
    }
  ]
}
---

# DART-18-PACKAGES: Packages and Pub

## Introduction

pubspec.yaml, dependencies, and the pub ecosystem. By the end of this lesson you will be able to: Create a package with pubspec.yaml; Add and manage dependencies; Understand version constraints; Publish and consume packages.

## Key Concepts

### 1. Create a package with pubspec.yaml

Target: Create a package with pubspec.yaml. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```dart
// pubspec.yaml
// name: my_app
// description: A sample Dart app
// environment:
//   sdk: ^3.4.0
// dependencies:
//   http: ^1.2.0
void main() {
  print("pubspec ready");
}
```
### 2. Add and manage dependencies

Target: Add and manage dependencies. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```dart
// adding dependencies
// dart pub add http
// dart pub add dev:test
// dart pub upgrade
// dart pub get (after editing pubspec)
void main() {
  print("dependency workflow");
}
```
### 3. Understand version constraints

Target: Understand version constraints. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```dart
// version constraints
// ^1.2.0    -> >=1.2.0 <2.0.0 (caret)
// >=1.0.0 <2.0.0  -> explicit range
// 1.2.3     -> exact
// any       -> avoid in production
// pubspec.lock pins resolved versions
void main() {
  print("semver constraints");
}
```
### 4. Publish and consume packages

Target: Publish and consume packages. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```dart
// consuming a package
// import 'package:http/http.dart' as http;  // used in the commented call below
Future<void> main() async {
  // var res = await http.get(Uri.parse("https://example.com"));
  // print(res.statusCode);
  print("http package ready");
}
```

## Practice Questions

1. What is the key idea behind "Packages and Pub"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Packages and Pub with analogies and real-world examples"
1. "Show me common mistakes beginners make with Packages and Pub"
1. "Provide advanced patterns and performance considerations for Packages and Pub"

## Key Takeaways

- Master the core ideas of Packages and Pub through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
