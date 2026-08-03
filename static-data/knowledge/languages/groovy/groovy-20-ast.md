---
{
  "title": "AST Transformations",
  "description": "Compile-time code generation.",
  "type": "lesson",
  "order": 20,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use @ToString",
    "Use @Canonical",
    "Use @Builder",
    "Write custom transforms"
  ],
  "knowledge_refs": [
    "groovy/groovy-20-ast"
  ],
  "prerequisites": [
    "Groovy-19: Categories"
  ],
  "references": [
    {
      "title": "Groovy Documentation",
      "url": "https://groovy-lang.org/documentation.html",
      "description": "Official docs"
    },
    {
      "title": "Groovy Tutorial (Groovy-lang)",
      "url": "https://groovy-lang.org/single-page-documentation.html",
      "description": "Official reference"
    },
    {
      "title": "Groovy in Action",
      "url": "https://www.manning.com/books/groovy-in-action-second-edition",
      "description": "Book"
    }
  ]
}
---

# GROOVY-20-AST: AST Transformations

## Introduction

Compile-time code generation. By the end of this lesson you will be able to: Use @ToString; Use @Canonical; Use @Builder; Write custom transforms.

## Key Concepts

### 1. Use @ToString

Target: Use @ToString. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```groovy
import groovy.transform.*

@Canonical
class Person {
  String name
  int age
}

println new Person("Ada", 36)
```
### 2. Use @Canonical

Target: Use @Canonical. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```groovy
@ToString
class Point { int x, y }
```
### 3. Use @Builder

Target: Use @Builder. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```groovy
@Builder
class Widget {
  String name
  int size
}

def w = Widget.builder().name("w").size(5).build()
```
### 4. Write custom transforms

Target: Write custom transforms. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```groovy
@TupleConstructor
class Pair { int a; int b }
```

## Practice Questions

1. What is the key idea behind "AST Transformations"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain AST Transformations with analogies and real-world examples"
1. "Show me common mistakes beginners make with AST Transformations"
1. "Provide advanced patterns and performance considerations for AST Transformations"

## Key Takeaways

- Master the core ideas of AST Transformations through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
