---
{
  "title": "Null Safety",
  "description": "Nullable types, sound null safety, and the ?. operators.",
  "type": "lesson",
  "order": 10,
  "duration": "50 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Declare nullable types with ?",
    "Use ?., !!, and ?? operators",
    "Promote types after null checks",
    "Use late for delayed initialization"
  ],
  "knowledge_refs": [
    "dart/dart-10-null-safety"
  ],
  "prerequisites": [
    "DART-02"
  ],
  "references": [
    {
      "title": "Dart — Null Safety",
      "url": "https://dart.dev/null-safety"
    },
    {
      "title": "Dart — Null Safety Tour",
      "url": "https://dart.dev/null-safety/understanding-null-safety"
    },
    {
      "title": "Dart — Late Variables",
      "url": "https://dart.dev/null-safety#late-variables"
    }
  ]
}
---

# DART-10-NULL-SAFETY: Null Safety

## Introduction

Nullable types, sound null safety, and the ?. operators. By the end of this lesson you will be able to: Declare nullable types with ?; Use ?., !!, and ?? operators; Promote types after null checks; Use late for delayed initialization.

## Key Concepts

### 1. Declare nullable types with ?

Target: Declare nullable types with ?. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```dart
// nullable basics
void main() {
  String? maybe = "hello";
  print(maybe);
  maybe = null;
  print(maybe?.length);   // null
  print(maybe ?? "empty"); // "empty"
}
```
### 2. Use ?., !!, and ?? operators

Target: Use ?., !!, and ?? operators. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```dart
// safe call chains
class Address {
  final String city;
  Address(this.city);
}
class Person {
  final Address? address;
  Person(this.address);
}
void main() {
  var p = Person(Address("Paris"));
  print(p.address?.city);              // Paris
  var none = Person(null);
  print(none.address?.city ?? "unknown");  // unknown
}
```
### 3. Promote types after null checks

Target: Promote types after null checks. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```dart
// promotion and !!
void main() {
  String? raw = "42";
  if (raw != null) {
    print(raw.length);    // promoted to String
  }
  var n = raw!.length;   // force unwrap
  print(n);
  raw = null;
  // print(raw.length);   // error: String? has no length
  print(raw ?? "null");
}
```
### 4. Use late for delayed initialization

Target: Use late for delayed initialization. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```dart
// late variables
void main() {
  late String heavy;
  // heavy not yet initialized
  heavy = "computed later";
  print(heavy);
  late final int cached = _expensive();
  print(cached);  // computed once
  print(cached);  // cached
}
int _expensive() {
  print("computing...");
  return 42;
}
```

## Practice Questions

1. What is the key idea behind "Null Safety"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Null Safety with analogies and real-world examples"
1. "Show me common mistakes beginners make with Null Safety"
1. "Provide advanced patterns and performance considerations for Null Safety"

## Key Takeaways

- Master the core ideas of Null Safety through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
