---
{
  "title": "Classes and Objects",
  "description": "Classes, constructors, fields, and methods.",
  "type": "lesson",
  "order": 8,
  "duration": "75 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define classes with fields and methods",
    "Use initializing and named constructors",
    "Use getters and setters",
    "Understand cascade notation"
  ],
  "knowledge_refs": [
    "dart/dart-08-classes"
  ],
  "prerequisites": [
    "DART-07"
  ],
  "references": [
    {
      "title": "Dart — Classes",
      "url": "https://dart.dev/language/classes"
    },
    {
      "title": "Dart — Constructors",
      "url": "https://dart.dev/language/constructors"
    },
    {
      "title": "Dart — Cascade Notation",
      "url": "https://dart.dev/language/classes#cascade-notation"
    }
  ]
}
---

# DART-08-CLASSES: Classes and Objects

## Introduction

Classes, constructors, fields, and methods. By the end of this lesson you will be able to: Define classes with fields and methods; Use initializing and named constructors; Use getters and setters; Understand cascade notation.

## Key Concepts

### 1. Define classes with fields and methods

Target: Define classes with fields and methods. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```dart
// class basics
class Product {
  final String name;
  final double price;
  int stock;
  Product(this.name, this.price, {this.stock = 0});
  String summary() => "$name — \$$price (stock: $stock)";
}
void main() {
  var p = Product("Keyboard", 49.99, stock: 12);
  print(p.summary());
}
```
### 2. Use initializing and named constructors

Target: Use initializing and named constructors. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```dart
// named and factory constructors
class Point {
  final double x, y;
  Point(this.x, this.y);
  Point.origin() : x = 0, y = 0;
  factory Point.fromList(List<double> v) => Point(v[0], v[1]);
}
void main() {
  print(Point.origin().x);
  print(Point.fromList([1, 2]).y);
}
```
### 3. Use getters and setters

Target: Use getters and setters. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```dart
// getters and setters
class Thermostat {
  double _celsius = 20;
  double get fahrenheit => _celsius * 9 / 5 + 32;
  set fahrenheit(double f) => _celsius = (f - 32) * 5 / 9;
}
void main() {
  var t = Thermostat();
  print(t.fahrenheit);  // 68.0
  t.fahrenheit = 77;
  print(t.fahrenheit);  // 77.0
}
```
### 4. Understand cascade notation

Target: Understand cascade notation. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```dart
// cascade notation
void main() {
  var sb = StringBuffer()
    ..write("Hello ")
    ..write("Dart!")..write(" ");
  var list = <int>[]
    ..add(1)
    ..add(2)
    ..add(3);
  print(sb.toString());
  print(list);
}
```

## Practice Questions

1. What is the key idea behind "Classes and Objects"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Classes and Objects with analogies and real-world examples"
1. "Show me common mistakes beginners make with Classes and Objects"
1. "Provide advanced patterns and performance considerations for Classes and Objects"

## Key Takeaways

- Master the core ideas of Classes and Objects through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
