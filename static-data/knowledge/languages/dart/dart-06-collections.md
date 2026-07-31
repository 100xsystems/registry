---
{
  "title": "Collections",
  "description": "Lists, sets, maps, and collection operators.",
  "type": "lesson",
  "order": 6,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Build and mutate lists",
    "Store unique values in sets",
    "Map keys to values",
    "Transform with map, where, and fold"
  ],
  "knowledge_refs": [
    "dart/dart-06-collections"
  ],
  "prerequisites": [
    "DART-05"
  ],
  "references": [
    {
      "title": "Dart — Collections",
      "url": "https://dart.dev/language/collections"
    },
    {
      "title": "Dart — List API",
      "url": "https://api.dart.dev/stable/dart-core/List-class.html"
    },
    {
      "title": "Dart — Iterable Operations",
      "url": "https://dart.dev/codelabs/iterables"
    }
  ]
}
---

# DART-06-COLLECTIONS: Collections

## Introduction

Lists, sets, maps, and collection operators. By the end of this lesson you will be able to: Build and mutate lists; Store unique values in sets; Map keys to values; Transform with map, where, and fold.

## Key Concepts

### 1. Build and mutate lists

Target: Build and mutate lists. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```dart
// lists
void main() {
  var fruits = ["apple", "banana", "cherry"];
  fruits.add("date");
  fruits.insert(0, "fig");
  fruits.removeAt(1);
  print(fruits);
  print(fruits[0]);
  print(fruits.length);
}
```
### 2. Store unique values in sets

Target: Store unique values in sets. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```dart
// sets and maps
void main() {
  var tags = <String>{"dart", "web", "server"};
  tags.add("flutter");
  print(tags.contains("dart"));
  var user = {"name": "Alice", "age": 30};
  user["admin"] = true;
  user.remove("age");
  print(user);
}
```
### 3. Map keys to values

Target: Map keys to values. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```dart
// transform
void main() {
  var nums = [1, 2, 3, 4, 5];
  var doubled = nums.map((n) => n * 2).toList();
  var evens = nums.where((n) => n.isEven).toList();
  var sum = nums.fold(0, (acc, n) => acc + n);
  print("$doubled $evens $sum");
}
```
### 4. Transform with map, where, and fold

Target: Transform with map, where, and fold. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```dart
// sorting
void main() {
  var people = [
    {"name": "Zoe", "age": 30},
    {"name": "Amy", "age": 25},
    {"name": "Bo", "age": 40},
  ];
  people.sort((a, b) => (a["age"]! as int).compareTo(b["age"]! as int));
  print(people.map((p) => p["name"]).toList());
}
```

## Practice Questions

1. What is the key idea behind "Collections"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Collections with analogies and real-world examples"
1. "Show me common mistakes beginners make with Collections"
1. "Provide advanced patterns and performance considerations for Collections"

## Key Takeaways

- Master the core ideas of Collections through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
