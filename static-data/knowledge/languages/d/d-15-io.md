---
{
  "title": "File and Stream IO",
  "description": "Read and write files.",
  "type": "lesson",
  "order": 15,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Read files",
    "Write files",
    "Read line by line",
    "Handle binary data"
  ],
  "knowledge_refs": [
    "d/d-15-io"
  ],
  "prerequisites": [
    "D-14: Concurrency"
  ],
  "references": [
    {
      "title": "D Language Reference",
      "url": "https://dlang.org/spec/spec.html",
      "description": "Official language spec"
    },
    {
      "title": "D Programming Tour",
      "url": "https://tour.dlang.org/",
      "description": "Interactive language tour"
    },
    {
      "title": "D Wiki",
      "url": "https://wiki.dlang.org/",
      "description": "Community wiki"
    },
    {
      "title": "DUB Package Manager",
      "url": "https://code.dlang.org/",
      "description": "Package registry"
    }
  ]
}
---

# D-15-IO: File and Stream IO

## Introduction

Read and write files. By the end of this lesson you will be able to: Read files; Write files; Read line by line; Handle binary data.

## Key Concepts

### 1. Read files

Target: Read files. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```d
import std.stdio;

void main() {
    auto data = readText("data.txt");
    writeln(data);
}
```
### 2. Write files

Target: Write files. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```d
import std.file;
write("out.txt", "hello");
```
### 3. Read line by line

Target: Read line by line. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```d
foreach (line; File("data.txt").byLine) {
    writeln(line);
}
```
### 4. Handle binary data

Target: Handle binary data. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```d
import std.stdio;

auto f = File("out.txt", "w");
f.writeln("line one");
f.writeln("line two");
f.close();
```

## Practice Questions

1. What is the key idea behind "File and Stream IO"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain File and Stream IO with analogies and real-world examples"
1. "Show me common mistakes beginners make with File and Stream IO"
1. "Provide advanced patterns and performance considerations for File and Stream IO"

## Key Takeaways

- Master the core ideas of File and Stream IO through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
