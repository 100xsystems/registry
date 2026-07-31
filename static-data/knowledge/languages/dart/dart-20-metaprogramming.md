---
{
  "title": "Annotations and Metaprogramming",
  "description": "Annotations, code generation, and build_runner.",
  "type": "lesson",
  "order": 20,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Define and use annotations",
    "Set up code generation with build_runner",
    "Use json_serializable for models",
    "Understand source generation limits"
  ],
  "knowledge_refs": [
    "dart/dart-20-metaprogramming"
  ],
  "prerequisites": [
    "DART-18"
  ],
  "references": [
    {
      "title": "Dart — Metadata",
      "url": "https://dart.dev/language/metadata"
    },
    {
      "title": "build_runner — pub.dev",
      "url": "https://pub.dev/packages/build_runner"
    },
    {
      "title": "json_serializable — pub.dev",
      "url": "https://pub.dev/packages/json_serializable"
    }
  ]
}
---

# DART-20-METAPROGRAMMING: Annotations and Metaprogramming

## Introduction

Annotations, code generation, and build_runner. By the end of this lesson you will be able to: Define and use annotations; Set up code generation with build_runner; Use json_serializable for models; Understand source generation limits.

## Key Concepts

### 1. Define and use annotations

Target: Define and use annotations. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```dart
// annotations
class Immutable {
  const Immutable();
}
@Immutable()
class Point {
  final int x, y;
  const Point(this.x, this.y);
}
void main() {
  print(Point(1, 2));
}
```
### 2. Set up code generation with build_runner

Target: Set up code generation with build_runner. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```dart
// build_runner setup
// pubspec.yaml:
// dependencies:
//   json_annotation: ^4.9.0
// dev_dependencies:
//   build_runner: ^2.4.0
//   json_serializable: ^6.8.0
void main() {
  print("codegen setup ready");
}
```
### 3. Use json_serializable for models

Target: Use json_serializable for models. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```dart
// json_serializable model
import 'package:json_annotation/json_annotation.dart';
part 'user.g.dart';
@JsonSerializable()
class User {
  final String name;
  final int age;
  User({required this.name, required this.age});
  factory User.fromJson(Map<String, dynamic> json) => _$UserFromJson(json);
  Map<String, dynamic> toJson() => _$UserToJson(this);
}
```
### 4. Understand source generation limits

Target: Understand source generation limits. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```dart
// generating
// terminal:
//   dart run build_runner build
// generates user.g.dart with the serialization code
// then: User.fromJson({"name": "Alice", "age": 30})
void main() {
  print("run: dart run build_runner build");
}
```

## Practice Questions

1. What is the key idea behind "Annotations and Metaprogramming"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Annotations and Metaprogramming with analogies and real-world examples"
1. "Show me common mistakes beginners make with Annotations and Metaprogramming"
1. "Provide advanced patterns and performance considerations for Annotations and Metaprogramming"

## Key Takeaways

- Master the core ideas of Annotations and Metaprogramming through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
