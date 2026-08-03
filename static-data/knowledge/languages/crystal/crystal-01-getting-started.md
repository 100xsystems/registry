---
{
  "title": "Getting Started with Crystal",
  "description": "Install, compile, and run Crystal.",
  "type": "lesson",
  "order": 1,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Install Crystal",
    "Compile with crystal build",
    "Write hello world",
    "Run with crystal run"
  ],
  "knowledge_refs": [
    "crystal/crystal-01-getting-started"
  ],
  "prerequisites": [
    "None — this is the entry point"
  ],
  "references": [
    {
      "title": "Crystal Language Reference",
      "url": "https://crystal-lang.org/reference/",
      "description": "Official docs"
    },
    {
      "title": "Crystal for Rubyists",
      "url": "https://crystal-lang.org/reference/guides/faq.html",
      "description": "Migration guide"
    },
    {
      "title": "Crystal Book",
      "url": "https://crystal-lang.org/reference/",
      "description": "Official reference book"
    },
    {
      "title": "Crystal Forum",
      "url": "https://forum.crystal-lang.org/",
      "description": "Community"
    }
  ]
}
---

# CRYSTAL-01-GETTING-STARTED: Getting Started with Crystal

## Introduction

Install, compile, and run Crystal. By the end of this lesson you will be able to: Install Crystal; Compile with crystal build; Write hello world; Run with crystal run.

## Key Concepts

### 1. Install Crystal

Target: Install Crystal. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```crystal
puts "Hello, World!"
```
### 2. Compile with crystal build

Target: Compile with crystal build. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```crystal
crystal run hello.cr
```
### 3. Write hello world

Target: Write hello world. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```crystal
crystal build hello.cr -o hello
./hello
```
### 4. Run with crystal run

Target: Run with crystal run. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```crystal
puts "Hello, " + ARGV[0]? || "World"
```

## Practice Questions

1. What is the key idea behind "Getting Started with Crystal"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with Crystal with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with Crystal"
1. "Provide advanced patterns and performance considerations for Getting Started with Crystal"

## Key Takeaways

- Master the core ideas of Getting Started with Crystal through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
