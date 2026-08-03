---
{
  "title": "Closures",
  "description": "First-class functions.",
  "type": "lesson",
  "order": 5,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write closures",
    "Pass closures",
    "Capture variables",
    "Use closure methods"
  ],
  "knowledge_refs": [
    "groovy/groovy-05-closures"
  ],
  "prerequisites": [
    "Groovy-04: Lists and Maps"
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

# GROOVY-05-CLOSURES: Closures

## Introduction

First-class functions. By the end of this lesson you will be able to: Write closures; Pass closures; Capture variables; Use closure methods.

## Key Concepts

### 1. Write closures

Target: Write closures. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```groovy
def square = { it * it }
println square(5)
```
### 2. Pass closures

Target: Pass closures. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```groovy
def apply = { f, x -> f(x) }
apply({ n -> n + 1 }, 41)
```
### 3. Capture variables

Target: Capture variables. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```groovy
def counter = 0
def inc = { counter++ }
inc(); inc()
println counter
```
### 4. Use closure methods

Target: Use closure methods. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```groovy
[1, 2, 3].findAll { it > 1 }.each { println it }
```

## Practice Questions

1. What is the key idea behind "Closures"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Closures with analogies and real-world examples"
1. "Show me common mistakes beginners make with Closures"
1. "Provide advanced patterns and performance considerations for Closures"

## Key Takeaways

- Master the core ideas of Closures through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
