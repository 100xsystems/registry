---
{
  "title": "Unit Testing with unittest",
  "description": "Embedded tests in D code.",
  "type": "lesson",
  "order": 18,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Write unittest blocks",
    "Use assert in tests",
    "Run with -unittest",
    "Test templates"
  ],
  "knowledge_refs": [
    "d/d-18-testing"
  ],
  "prerequisites": [
    "D-17: Mixins and Code Generation"
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

# D-18-TESTING: Unit Testing with unittest

## Introduction

Embedded tests in D code. By the end of this lesson you will be able to: Write unittest blocks; Use assert in tests; Run with -unittest; Test templates.

## Key Concepts

### 1. Write unittest blocks

Target: Write unittest blocks. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```d
import std.stdio;

int add(int a, int b) {
    return a + b;
}

unittest {
    assert(add(2, 3) == 5);
}

void main() {}
```
### 2. Use assert in tests

Target: Use assert in tests. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```d
dmd -unittest -main app.d -of=test && ./test
```
### 3. Run with -unittest

Target: Run with -unittest. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```d
unittest {
    assert([1, 2, 3].sum == 6);
    assert("abc".length == 3);
}
```
### 4. Test templates

Target: Test templates. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```d
T square(T)(T x) { return x * x; }

unittest {
    assert(square(4) == 16);
    assert(square(2.5) == 6.25);
}
```

## Practice Questions

1. What is the key idea behind "Unit Testing with unittest"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Unit Testing with unittest with analogies and real-world examples"
1. "Show me common mistakes beginners make with Unit Testing with unittest"
1. "Provide advanced patterns and performance considerations for Unit Testing with unittest"

## Key Takeaways

- Master the core ideas of Unit Testing with unittest through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
