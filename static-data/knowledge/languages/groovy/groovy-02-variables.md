---
{
  "title": "Variables and Types",
  "description": "Dynamic typing and type inference.",
  "type": "lesson",
  "order": 2,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use def for dynamic typing",
    "Declare typed variables",
    "Use strings and numbers",
    "Understand GStrings"
  ],
  "knowledge_refs": [
    "groovy/groovy-02-variables"
  ],
  "prerequisites": [
    "Groovy-01: Getting Started with Groovy"
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

# GROOVY-02-VARIABLES: Variables and Types

## Introduction

Dynamic typing and type inference. By the end of this lesson you will be able to: Use def for dynamic typing; Declare typed variables; Use strings and numbers; Understand GStrings.

## Key Concepts

### 1. Use def for dynamic typing

Target: Use def for dynamic typing. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```groovy
def x = 42
def name = "Ada"
def pi = 3.14
```
### 2. Declare typed variables

Target: Declare typed variables. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```groovy
int count = 10
String message = "hello"
```
### 3. Use strings and numbers

Target: Use strings and numbers. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```groovy
def greeting = "Hello, $name!"   // GString
```
### 4. Understand GStrings

Target: Understand GStrings. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```groovy
println x.class
```

## Practice Questions

1. What is the key idea behind "Variables and Types"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Variables and Types with analogies and real-world examples"
1. "Show me common mistakes beginners make with Variables and Types"
1. "Provide advanced patterns and performance considerations for Variables and Types"

## Key Takeaways

- Master the core ideas of Variables and Types through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
