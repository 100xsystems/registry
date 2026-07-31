---
{
  "title": "Numbers and Math",
  "description": "int, double, num, and the dart:math library.",
  "type": "lesson",
  "order": 3,
  "duration": "50 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use int, double, and the num supertype",
    "Convert between numeric types",
    "Use dart:math functions",
    "Generate random numbers"
  ],
  "knowledge_refs": [
    "dart/dart-03-numbers-math"
  ],
  "prerequisites": [
    "DART-02"
  ],
  "references": [
    {
      "title": "Dart — Numbers",
      "url": "https://dart.dev/language/built-in-types#numbers"
    },
    {
      "title": "Dart — dart:math Library",
      "url": "https://api.dart.dev/stable/dart-math/dart-math-library.html"
    },
    {
      "title": "Dart — Numbers API",
      "url": "https://api.dart.dev/stable/dart-core/num-class.html"
    }
  ]
}
---

# DART-03-NUMBERS-MATH: Numbers and Math

## Introduction

int, double, num, and the dart:math library. By the end of this lesson you will be able to: Use int, double, and the num supertype; Convert between numeric types; Use dart:math functions; Generate random numbers.

## Key Concepts

### 1. Use int, double, and the num supertype

Target: Use int, double, and the num supertype. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```dart
// num, int, double
void main() {
  int whole = 42;
  double frac = 3.14;
  num either = 42;      // num is the supertype
  either = 3.14;        // still fine
  print("$whole $frac $either");
}
```
### 2. Convert between numeric types

Target: Convert between numeric types. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```dart
// conversions and precision
void main() {
  var sum = 0.1 + 0.2;            // 0.30000000000000004
  print(sum);
  var asInt = sum.toInt();        // 0
  var rounded = sum.round();      // 0
  var str = 3.14159.toStringAsFixed(2);  // "3.14"
  print("$asInt $rounded $str");
}
```
### 3. Use dart:math functions

Target: Use dart:math functions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```dart
// dart:math
import 'dart:math';
void main() {
  print(sqrt(16));            // 4.0
  print(pow(2, 10));          // 1024
  print(max(3, 7));           // 7
  print(min(3, 7));           // 3
}
```
### 4. Generate random numbers

Target: Generate random numbers. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```dart
// randomness
import 'dart:math';
void main() {
  var rng = Random();
  print(rng.nextInt(6) + 1);        // 1..6
  print(rng.nextDouble());          // 0..1
  print(rng.nextBool());
  var seeded = Random(42);          // reproducible
  print(seeded.nextInt(100));
}
```

## Practice Questions

1. What is the key idea behind "Numbers and Math"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Numbers and Math with analogies and real-world examples"
1. "Show me common mistakes beginners make with Numbers and Math"
1. "Provide advanced patterns and performance considerations for Numbers and Math"

## Key Takeaways

- Master the core ideas of Numbers and Math through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
