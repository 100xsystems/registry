---
{
  "title": "Variables and Data Types",
  "description": "var, final, const, and the core built-in types.",
  "type": "lesson",
  "order": 2,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Declare variables with var and typed forms",
    "Use final and const for immutability",
    "Work with int, double, String, bool, and lists",
    "Use dynamic and Object judiciously"
  ],
  "knowledge_refs": [
    "dart/dart-02-variables-types"
  ],
  "prerequisites": [
    "DART-01"
  ],
  "references": [
    {
      "title": "Dart — Variables",
      "url": "https://dart.dev/language/variables"
    },
    {
      "title": "Dart — Built-in Types",
      "url": "https://dart.dev/language/built-in-types"
    },
    {
      "title": "Dart — Final and Const",
      "url": "https://dart.dev/language/variables#final-and-const"
    }
  ]
}
---

# DART-02-VARIABLES-TYPES: Variables and Data Types

## Introduction

var, final, const, and the core built-in types. By the end of this lesson you will be able to: Declare variables with var and typed forms; Use final and const for immutability; Work with int, double, String, bool, and lists; Use dynamic and Object judiciously.

## Key Concepts

### 1. Declare variables with var and typed forms

Target: Declare variables with var and typed forms. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```dart
// var vs final vs const
void main() {
  var score = 42;        // inferred int
  final name = "Dart";   // set once at runtime
  const pi = 3.14159;    // compile-time constant
  // score = "x";        // error: int
  // name = "Java";      // error: final
  print("$score $name $pi");
}
```
### 2. Use final and const for immutability

Target: Use final and const for immutability. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```dart
// explicit types
void main() {
  int count = 10;
  double ratio = 0.5;
  String greeting = "hi";
  bool ok = true;
  List<int> nums = [1, 2, 3];
  print("$count $ratio $greeting $ok $nums");
}
```
### 3. Work with int, double, String, bool, and lists

Target: Work with int, double, String, bool, and lists. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```dart
// dynamic and Object
void main() {
  dynamic anything = 42;
  anything = "now a string";     // allowed
  Object obj = 42;
  // obj = "x";                   // allowed (Object is a supertype)
  // obj.round();                 // error: Object has no round()
  print(anything is String);      // true
  print(obj is int);              // true
}
```
### 4. Use dynamic and Object judiciously

Target: Use dynamic and Object judiciously. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```dart
// type conversion
void main() {
  var n = int.parse("42");
  var d = double.parse("3.14");
  var s = 42.toString();
  var b = double.tryParse("x") ?? 0.0;
  print("$n $d $s $b");
}
```

## Practice Questions

1. What is the key idea behind "Variables and Data Types"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Variables and Data Types with analogies and real-world examples"
1. "Show me common mistakes beginners make with Variables and Data Types"
1. "Provide advanced patterns and performance considerations for Variables and Data Types"

## Key Takeaways

- Master the core ideas of Variables and Data Types through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
