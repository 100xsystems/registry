---
{
  "title": "Strings and String Manipulation",
  "description": "String literals, interpolation, and the string API.",
  "type": "lesson",
  "order": 4,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Write single, double, and triple-quoted strings",
    "Interpolate with $ and ${}",
    "Manipulate strings with the standard library",
    "Handle multi-line and raw strings"
  ],
  "knowledge_refs": [
    "dart/dart-04-strings"
  ],
  "prerequisites": [
    "DART-02"
  ],
  "references": [
    {
      "title": "Dart — Strings",
      "url": "https://dart.dev/language/built-in-types#strings"
    },
    {
      "title": "Dart — String API",
      "url": "https://api.dart.dev/stable/dart-core/String-class.html"
    },
    {
      "title": "Dart — String Methods",
      "url": "https://api.dart.dev/stable/dart-core/String-class.html#instance-methods"
    }
  ]
}
---

# DART-04-STRINGS: Strings and String Manipulation

## Introduction

String literals, interpolation, and the string API. By the end of this lesson you will be able to: Write single, double, and triple-quoted strings; Interpolate with $ and ${}; Manipulate strings with the standard library; Handle multi-line and raw strings.

## Key Concepts

### 1. Write single, double, and triple-quoted strings

Target: Write single, double, and triple-quoted strings. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```dart
// literals and interpolation
void main() {
  var name = "Alice";
  var age = 30;
  var msg = "$name is $age years old";
  var expr = "double: ${age * 2}";
  var dollar = "cost: \$5";        // escaped dollar
  print(msg);
  print(expr);
  print(dollar);
}
```
### 2. Interpolate with $ and ${}

Target: Interpolate with $ and ${}. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```dart
// multi-line and raw strings
void main() {
  var multiline = """
Line one
Line two
""";
  var raw = r"C:\Users\name";      // raw string
  print(multiline);
  print(raw);
}
```
### 3. Manipulate strings with the standard library

Target: Manipulate strings with the standard library. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```dart
// string operations
void main() {
  var s = "Hello, World";
  print(s.toUpperCase());
  print(s.toLowerCase());
  print(s.startsWith("Hello"));
  print(s.split(","));
  print(s.replaceAll("World", "Dart"));
  print(s.substring(0, 5));
  print(s.length);
}
```
### 4. Handle multi-line and raw strings

Target: Handle multi-line and raw strings. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```dart
// builders and joins
void main() {
  var sb = StringBuffer();
  for (var i = 0; i < 3; i++) {
    sb.write("line$i; ");
  }
  print(sb.toString());
  print(["a", "b", "c"].join(" | "));
  print("hello".padLeft(10));
}
```

## Practice Questions

1. What is the key idea behind "Strings and String Manipulation"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Strings and String Manipulation with analogies and real-world examples"
1. "Show me common mistakes beginners make with Strings and String Manipulation"
1. "Provide advanced patterns and performance considerations for Strings and String Manipulation"

## Key Takeaways

- Master the core ideas of Strings and String Manipulation through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
