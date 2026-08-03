---
{
  "title": "File I/O",
  "description": "Groovy file helpers.",
  "type": "lesson",
  "order": 11,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Read files",
    "Write files",
    "Read lines",
    "Use new File"
  ],
  "knowledge_refs": [
    "groovy/groovy-11-io"
  ],
  "prerequisites": [
    "Groovy-10: Concurrency with GPars"
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

# GROOVY-11-IO: File I/O

## Introduction

Groovy file helpers. By the end of this lesson you will be able to: Read files; Write files; Read lines; Use new File.

## Key Concepts

### 1. Read files

Target: Read files. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```groovy
def text = new File("data.txt").text
```
### 2. Write files

Target: Write files. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```groovy
new File("out.txt").text = "hello"
```
### 3. Read lines

Target: Read lines. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```groovy
new File("data.txt").eachLine { println it }
```
### 4. Use new File

Target: Use new File. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```groovy
new File("data.txt").withReader { reader -> println reader.readLine() }
```

## Practice Questions

1. What is the key idea behind "File I/O"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain File I/O with analogies and real-world examples"
1. "Show me common mistakes beginners make with File I/O"
1. "Provide advanced patterns and performance considerations for File I/O"

## Key Takeaways

- Master the core ideas of File I/O through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
