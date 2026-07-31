---
{
  "title": "Functions",
  "description": "Declarations, optional parameters, and lambdas.",
  "type": "lesson",
  "order": 7,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Declare functions with return types",
    "Use named and positional optional parameters",
    "Write arrow functions and closures",
    "Use higher-order functions"
  ],
  "knowledge_refs": [
    "dart/dart-07-functions"
  ],
  "prerequisites": [
    "DART-05"
  ],
  "references": [
    {
      "title": "Dart — Functions",
      "url": "https://dart.dev/language/functions"
    },
    {
      "title": "Dart — Parameters",
      "url": "https://dart.dev/language/functions#parameters"
    },
    {
      "title": "Dart — Closures",
      "url": "https://dart.dev/language/functions#lexical-scope"
    }
  ]
}
---

# DART-07-FUNCTIONS: Functions

## Introduction

Declarations, optional parameters, and lambdas. By the end of this lesson you will be able to: Declare functions with return types; Use named and positional optional parameters; Write arrow functions and closures; Use higher-order functions.

## Key Concepts

### 1. Declare functions with return types

Target: Declare functions with return types. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```dart
// function basics
String greet(String name, {int times = 1}) {
  return "Hi $name! " * times;
}
void main() {
  print(greet("Alice"));
  print(greet("Bob", times: 2));
}
```
### 2. Use named and positional optional parameters

Target: Use named and positional optional parameters. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```dart
// optional parameters
void show({String? title, List<String> tags = const []}) {
  print("title: ${title ?? "untitled"}");
  print("tags: $tags");
}
void main() {
  show(tags: ["a", "b"]);
  show();
}
```
### 3. Write arrow functions and closures

Target: Write arrow functions and closures. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```dart
// arrow functions and closures
void main() {
  int square(int n) => n * n;
  var counter = 0;
  int increment() => ++counter;   // closure over counter
  print(square(9));               // 81
  print(increment());             // 1
  print(increment());             // 2
}
```
### 4. Use higher-order functions

Target: Use higher-order functions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```dart
// higher-order functions
void main() {
  var names = ["Zoe", "Amy"];
  var upper = names.map((n) => n.toUpperCase()).toList();
  print(upper);
  var evens = [1, 2, 3, 4].where((n) => n.isEven).toList();
  print(evens);
  var total = [1, 2, 3].reduce((a, b) => a + b);
  print(total);
}
```

## Practice Questions

1. What is the key idea behind "Functions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Functions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Functions"
1. "Provide advanced patterns and performance considerations for Functions"

## Key Takeaways

- Master the core ideas of Functions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
