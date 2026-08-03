---
{
  "title": "Getting Started with Groovy",
  "description": "Install, run scripts, and hello world.",
  "type": "lesson",
  "order": 1,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Install Groovy",
    "Run scripts with groovy",
    "Use the REPL",
    "Write hello world"
  ],
  "knowledge_refs": [
    "groovy/groovy-01-getting-started"
  ],
  "prerequisites": [
    "None — this is the entry point"
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

# GROOVY-01-GETTING-STARTED: Getting Started with Groovy

## Introduction

Install, run scripts, and hello world. By the end of this lesson you will be able to: Install Groovy; Run scripts with groovy; Use the REPL; Write hello world.

## Key Concepts

### 1. Install Groovy

Target: Install Groovy. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```groovy
println "Hello, World!"
```
### 2. Run scripts with groovy

Target: Run scripts with groovy. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```groovy
groovy hello.groovy
```
### 3. Use the REPL

Target: Use the REPL. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```groovy
groovy -e 'println "hello"'
```
### 4. Write hello world

Target: Write hello world. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```groovy
def name = "Ada"
println "Hello, ${name}!"
```

## Practice Questions

1. What is the key idea behind "Getting Started with Groovy"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with Groovy with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with Groovy"
1. "Provide advanced patterns and performance considerations for Getting Started with Groovy"

## Key Takeaways

- Master the core ideas of Getting Started with Groovy through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
