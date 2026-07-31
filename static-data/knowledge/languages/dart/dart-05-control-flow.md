---
{
  "title": "Control Flow",
  "description": "if, switch, and loops.",
  "type": "lesson",
  "order": 5,
  "duration": "50 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use if and else conditionals",
    "Match with modern switch expressions",
    "Iterate with for, for-in, and while",
    "Use break, continue, and labels"
  ],
  "knowledge_refs": [
    "dart/dart-05-control-flow"
  ],
  "prerequisites": [
    "DART-02"
  ],
  "references": [
    {
      "title": "Dart — Control Flow",
      "url": "https://dart.dev/language/control-flow"
    },
    {
      "title": "Dart — Switch Statements",
      "url": "https://dart.dev/language/branches#switch"
    },
    {
      "title": "Dart — Loops",
      "url": "https://dart.dev/language/loops"
    }
  ]
}
---

# DART-05-CONTROL-FLOW: Control Flow

## Introduction

if, switch, and loops. By the end of this lesson you will be able to: Use if and else conditionals; Match with modern switch expressions; Iterate with for, for-in, and while; Use break, continue, and labels.

## Key Concepts

### 1. Use if and else conditionals

Target: Use if and else conditionals. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```dart
// if and else
void main() {
  var score = 85;
  if (score >= 90) {
    print("A");
  } else if (score >= 80) {
    print("B");
  } else {
    print("C");
  }
  var pass = score >= 50 ? "pass" : "fail";
  print(pass);
}
```
### 2. Match with modern switch expressions

Target: Match with modern switch expressions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```dart
// switch expression (Dart 3)
void main() {
  var status = 404;
  var message = switch (status) {
    200 || 204 => "ok",
    404 => "not found",
    500 => "server error",
    >= 400 && < 500 => "client error",
    _ => "unknown",
  };
  print(message);
}
```
### 3. Iterate with for, for-in, and while

Target: Iterate with for, for-in, and while. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```dart
// loops
void main() {
  for (var i = 0; i < 5; i++) { print(i); }
  var items = ["a", "b", "c"];
  for (var item in items) { print(item); }
  var n = 0;
  while (n < 3) { n++; }
  print(n);
}
```
### 4. Use break, continue, and labels

Target: Use break, continue, and labels. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```dart
// break and continue
void main() {
  for (var i = 1; i <= 10; i++) {
    if (i % 3 == 0) continue;
    if (i == 8) break;
    print(i);
  }
  // 1 2 4 5 7
}
```

## Practice Questions

1. What is the key idea behind "Control Flow"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Control Flow with analogies and real-world examples"
1. "Show me common mistakes beginners make with Control Flow"
1. "Provide advanced patterns and performance considerations for Control Flow"

## Key Takeaways

- Master the core ideas of Control Flow through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
