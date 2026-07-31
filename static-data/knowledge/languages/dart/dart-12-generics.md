---
{
  "title": "Generics",
  "description": "Generic functions, classes, and bounds.",
  "type": "lesson",
  "order": 12,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write generic functions and classes",
    "Constrain type parameters",
    "Use collection literals with generics",
    "Understand reification limits"
  ],
  "knowledge_refs": [
    "dart/dart-12-generics"
  ],
  "prerequisites": [
    "DART-09"
  ],
  "references": [
    {
      "title": "Dart — Generics",
      "url": "https://dart.dev/language/generics"
    },
    {
      "title": "Dart — Generic Functions",
      "url": "https://dart.dev/language/generics#using-generic-methods"
    },
    {
      "title": "Dart — Type Literals",
      "url": "https://dart.dev/language/generics#reified-generics"
    }
  ]
}
---

# DART-12-GENERICS: Generics

## Introduction

Generic functions, classes, and bounds. By the end of this lesson you will be able to: Write generic functions and classes; Constrain type parameters; Use collection literals with generics; Understand reification limits.

## Key Concepts

### 1. Write generic functions and classes

Target: Write generic functions and classes. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```dart
// generic functions
T identity<T>(T value) => value;
void main() {
  print(identity(42));
  print(identity("text"));
  print(identity<List<int>>([1, 2]));
}
```
### 2. Constrain type parameters

Target: Constrain type parameters. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```dart
// generic classes
class Stack<T> {
  final List<T> _items = [];
  void push(T item) => _items.add(item);
  T? pop() => _items.isEmpty ? null : _items.removeLast();
  int get size => _items.length;
}
void main() {
  var s = Stack<int>();
  s.push(1);
  s.push(2);
  print(s.pop());
  print(s.size);
}
```
### 3. Use collection literals with generics

Target: Use collection literals with generics. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```dart
// bounds
T maxOf2<T extends Comparable<T>>(T a, T b) => a.compareTo(b) > 0 ? a : b;
void main() {
  print(maxOf2(3, 7));
  print(maxOf2("cat", "dog"));
}
// note: int implements Comparable<num>, so T infers to num here —
// returns num, not int (fine for comparisons)
```
### 4. Understand reification limits

Target: Understand reification limits. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```dart
// generic with collections
void main() {
  var nums = <int>[1, 2, 3];
  var labels = <String, int>{"a": 1};
  T? firstOrNull<T>(List<T> items) => items.isEmpty ? null : items.first;
  print(firstOrNull(nums));
  print(firstOrNull(<int>[]));
  print(labels);
}
```

## Practice Questions

1. What is the key idea behind "Generics"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Generics with analogies and real-world examples"
1. "Show me common mistakes beginners make with Generics"
1. "Provide advanced patterns and performance considerations for Generics"

## Key Takeaways

- Master the core ideas of Generics through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
