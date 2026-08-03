---
{
  "title": "Strings",
  "description": "UTF-8 strings and text processing.",
  "type": "lesson",
  "order": 4,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Work with string literals",
    "Concatenate strings",
    "Format with format",
    "Iterate characters"
  ],
  "knowledge_refs": [
    "d/d-04-strings"
  ],
  "prerequisites": [
    "D-03: Operators and Expressions"
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

# D-04-STRINGS: Strings

## Introduction

UTF-8 strings and text processing. By the end of this lesson you will be able to: Work with string literals; Concatenate strings; Format with format; Iterate characters.

## Key Concepts

### 1. Work with string literals

Target: Work with string literals. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```d
import std.stdio;

void main() {
    string a = "Hello";
    string b = a ~ " World";
    writeln(b);
}
```
### 2. Concatenate strings

Target: Concatenate strings. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```d
import std.format;
writeln(format("%d + %d = %d", 2, 3, 5));
```
### 3. Format with format

Target: Format with format. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```d
import std.algorithm, std.array;
auto upper = "hello".toUpper();
writeln(upper);
```
### 4. Iterate characters

Target: Iterate characters. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```d
foreach (c; "ABC") {
    write(c, " ");
}
```

## Practice Questions

1. What is the key idea behind "Strings"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Strings with analogies and real-world examples"
1. "Show me common mistakes beginners make with Strings"
1. "Provide advanced patterns and performance considerations for Strings"

## Key Takeaways

- Master the core ideas of Strings through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
