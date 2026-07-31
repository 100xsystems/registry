---
{
  "title": "Inheritance and Interfaces",
  "description": "extends, implements, mixins, and abstract classes.",
  "type": "lesson",
  "order": 9,
  "duration": "75 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Extend classes and override members",
    "Implement interfaces implicitly",
    "Compose behavior with mixins",
    "Design with abstract classes"
  ],
  "knowledge_refs": [
    "dart/dart-09-inheritance-interfaces"
  ],
  "prerequisites": [
    "DART-08"
  ],
  "references": [
    {
      "title": "Dart — Inheritance",
      "url": "https://dart.dev/language/extend"
    },
    {
      "title": "Dart — Mixins",
      "url": "https://dart.dev/language/mixins"
    },
    {
      "title": "Dart — Abstract Classes",
      "url": "https://dart.dev/language/classes#abstract-classes"
    }
  ]
}
---

# DART-09-INHERITANCE-INTERFACES: Inheritance and Interfaces

## Introduction

extends, implements, mixins, and abstract classes. By the end of this lesson you will be able to: Extend classes and override members; Implement interfaces implicitly; Compose behavior with mixins; Design with abstract classes.

## Key Concepts

### 1. Extend classes and override members

Target: Extend classes and override members. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```dart
// inheritance
class Animal {
  final String name;
  Animal(this.name);
  String speak() => "...";
}
class Dog extends Animal {
  Dog(String name) : super(name);
  @override
  String speak() => "Woof!";
}
void main() {
  print(Dog("Rex").speak());
}
```
### 2. Implement interfaces implicitly

Target: Implement interfaces implicitly. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```dart
// abstract classes + interfaces
abstract class Shape {
  double area();
  String describe() => "area = ${area()}";
}
class Circle extends Shape {
  final double r;
  Circle(this.r);
  @override
  double area() => 3.14159 * r * r;
}
void main() {
  print(Circle(2).describe());
}
```
### 3. Compose behavior with mixins

Target: Compose behavior with mixins. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```dart
// mixins
mixin Timestampable {
  DateTime? createdAt;
  void touch() => createdAt = DateTime.now();
}
class Post with Timestampable {
  final String title;
  Post(this.title);
}
void main() {
  var post = Post("Hello");
  post.touch();
  print(post.createdAt != null);
}
```
### 4. Design with abstract classes

Target: Design with abstract classes. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```dart
// sealed classes (Dart 3)
sealed class HttpResult {}
class Ok extends HttpResult {
  final String body;
  Ok(this.body);
}
class Err extends HttpResult {
  final int code;
  Err(this.code);
}
String describe(HttpResult r) => switch (r) {
  Ok(:var body) => "ok: $body",
  Err(:var code) => "err: $code",
};
void main() {
  print(describe(Ok("data")));
}
```

## Practice Questions

1. What is the key idea behind "Inheritance and Interfaces"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Inheritance and Interfaces with analogies and real-world examples"
1. "Show me common mistakes beginners make with Inheritance and Interfaces"
1. "Provide advanced patterns and performance considerations for Inheritance and Interfaces"

## Key Takeaways

- Master the core ideas of Inheritance and Interfaces through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
