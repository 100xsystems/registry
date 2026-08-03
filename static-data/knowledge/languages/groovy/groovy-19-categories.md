---
{
  "title": "Categories",
  "description": "Scoped method injection.",
  "type": "lesson",
  "order": 19,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Define categories",
    "Use @Category",
    "Use withCategory",
    "Scope extensions"
  ],
  "knowledge_refs": [
    "groovy/groovy-19-categories"
  ],
  "prerequisites": [
    "Groovy-18: Ratpack and Microservices"
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

# GROOVY-19-CATEGORIES: Categories

## Introduction

Scoped method injection. By the end of this lesson you will be able to: Define categories; Use @Category; Use withCategory; Scope extensions.

## Key Concepts

### 1. Define categories

Target: Define categories. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```groovy
@Category(String)
class StringCategory {
  String shout() { this.toUpperCase() + "!" }
}

use(StringCategory) {
  println "hello".shout()
}
```
### 2. Use @Category

Target: Use @Category. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```groovy
class MathCategory {
  static Integer triple(Integer self) { self * 3 }
}
use(MathCategory) { println 4.triple() }
```
### 3. Use withCategory

Target: Use withCategory. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```groovy
@Category(List)
class ListCategory {
  Number sum() { this.sum() }
}
```
### 4. Scope extensions

Target: Scope extensions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```groovy
use(StringCategory) { assert "hi".shout() == "HI!" }
```

## Practice Questions

1. What is the key idea behind "Categories"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Categories with analogies and real-world examples"
1. "Show me common mistakes beginners make with Categories"
1. "Provide advanced patterns and performance considerations for Categories"

## Key Takeaways

- Master the core ideas of Categories through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
