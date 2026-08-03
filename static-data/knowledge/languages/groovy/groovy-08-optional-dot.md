---
{
  "title": "Safe Navigation and Null Handling",
  "description": "Null-safe operators.",
  "type": "lesson",
  "order": 8,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use ?. operator",
    "Use elvis operator",
    "Use ?: default",
    "Handle nulls safely"
  ],
  "knowledge_refs": [
    "groovy/groovy-08-optional-dot"
  ],
  "prerequisites": [
    "Groovy-07: Classes and Traits"
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

# GROOVY-08-OPTIONAL-DOT: Safe Navigation and Null Handling

## Introduction

Null-safe operators. By the end of this lesson you will be able to: Use ?. operator; Use elvis operator; Use ?: default; Handle nulls safely.

## Key Concepts

### 1. Use ?. operator

Target: Use ?. operator. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```groovy
def name = user?.name   // null-safe
```
### 2. Use elvis operator

Target: Use elvis operator. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```groovy
def city = user?.address?.city ?: "unknown"
```
### 3. Use ?: default

Target: Use ?: default. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```groovy
def count = list?.size() ?: 0
```
### 4. Handle nulls safely

Target: Handle nulls safely. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```groovy
def value = map.key ?: "default"
```

## Practice Questions

1. What is the key idea behind "Safe Navigation and Null Handling"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Safe Navigation and Null Handling with analogies and real-world examples"
1. "Show me common mistakes beginners make with Safe Navigation and Null Handling"
1. "Provide advanced patterns and performance considerations for Safe Navigation and Null Handling"

## Key Takeaways

- Master the core ideas of Safe Navigation and Null Handling through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
