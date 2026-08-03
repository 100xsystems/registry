---
{
  "title": "Control Flow",
  "description": "Conditionals and loops.",
  "type": "lesson",
  "order": 3,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Write if/else",
    "Use switch",
    "Use for loops",
    "Use each closures"
  ],
  "knowledge_refs": [
    "groovy/groovy-03-control-flow"
  ],
  "prerequisites": [
    "Groovy-02: Variables and Types"
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

# GROOVY-03-CONTROL-FLOW: Control Flow

## Introduction

Conditionals and loops. By the end of this lesson you will be able to: Write if/else; Use switch; Use for loops; Use each closures.

## Key Concepts

### 1. Write if/else

Target: Write if/else. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```groovy
def score = 85
if (score >= 90) {
  println "A"
} else if (score >= 80) {
  println "B"
} else {
  println "C"
}
```
### 2. Use switch

Target: Use switch. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```groovy
switch (n) {
  case 1: println "one"; break
  default: println "other"
}
```
### 3. Use for loops

Target: Use for loops. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```groovy
for (i in 1..5) { println i }
```
### 4. Use each closures

Target: Use each closures. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```groovy
[1, 2, 3].each { println it }
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
