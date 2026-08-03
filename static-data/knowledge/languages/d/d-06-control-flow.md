---
{
  "title": "Control Flow",
  "description": "if, switch, and loops.",
  "type": "lesson",
  "order": 6,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Write if/else chains",
    "Use switch statements",
    "Use foreach loops",
    "Use while loops"
  ],
  "knowledge_refs": [
    "d/d-06-control-flow"
  ],
  "prerequisites": [
    "D-05: Arrays and Slices"
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

# D-06-CONTROL-FLOW: Control Flow

## Introduction

if, switch, and loops. By the end of this lesson you will be able to: Write if/else chains; Use switch statements; Use foreach loops; Use while loops.

## Key Concepts

### 1. Write if/else chains

Target: Write if/else chains. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```d
int score = 85;
if (score >= 90) {
    writeln("A");
} else if (score >= 80) {
    writeln("B");
} else {
    writeln("C");
}
```
### 2. Use switch statements

Target: Use switch statements. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```d
switch (n) {
    case 1: writeln("one"); break;
    case 2: writeln("two"); break;
    default: writeln("other");
}
```
### 3. Use foreach loops

Target: Use foreach loops. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```d
foreach (i; 0..5) {
    writeln(i);
}
```
### 4. Use while loops

Target: Use while loops. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```d
int i = 0;
while (i < 3) {
    writeln(i);
    i++;
}
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
