---
{
  "title": "Functions",
  "description": "Write typed functions.",
  "type": "lesson",
  "order": 7,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write functions",
    "Use default parameters",
    "Use overloads",
    "Return tuples"
  ],
  "knowledge_refs": [
    "d/d-07-functions"
  ],
  "prerequisites": [
    "D-06: Control Flow"
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

# D-07-FUNCTIONS: Functions

## Introduction

Write typed functions. By the end of this lesson you will be able to: Write functions; Use default parameters; Use overloads; Return tuples.

## Key Concepts

### 1. Write functions

Target: Write functions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```d
import std.stdio;

int add(int a, int b) {
    return a + b;
}

void main() {
    writeln(add(2, 3));
}
```
### 2. Use default parameters

Target: Use default parameters. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```d
string greet(string name, string title = "Mr") {
    return title ~ " " ~ name;
}

writeln(greet("Ada"));
writeln(greet("Ada", "Dr"));
```
### 3. Use overloads

Target: Use overloads. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```d
import std.typecons;
auto divmod(int a, int b) {
    return tuple(a / b, a % b);
}

auto r = divmod(7, 2);
writeln(r[0], " ", r[1]);
```
### 4. Return tuples

Target: Return tuples. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```d
int add(int a, int b) => a + b;  // short syntax
```

## Practice Questions

1. What is the key idea behind "Functions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Functions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Functions"
1. "Provide advanced patterns and performance considerations for Functions"

## Key Takeaways

- Master the core ideas of Functions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
