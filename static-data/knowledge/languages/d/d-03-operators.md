---
{
  "title": "Operators and Expressions",
  "description": "Arithmetic, bitwise, and ternary.",
  "type": "lesson",
  "order": 3,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use arithmetic operators",
    "Use bitwise operators",
    "Use the ternary operator",
    "Handle integer division"
  ],
  "knowledge_refs": [
    "d/d-03-operators"
  ],
  "prerequisites": [
    "D-02: Types and Variables"
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

# D-03-OPERATORS: Operators and Expressions

## Introduction

Arithmetic, bitwise, and ternary. By the end of this lesson you will be able to: Use arithmetic operators; Use bitwise operators; Use the ternary operator; Handle integer division.

## Key Concepts

### 1. Use arithmetic operators

Target: Use arithmetic operators. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```d
writeln(7 / 2);   // 3 — integer division
writeln(7.0 / 2); // 3.5
```
### 2. Use bitwise operators

Target: Use bitwise operators. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```d
writeln(0b1100 & 0b1010);  // 8
writeln(0b1100 | 0b1010);  // 14
```
### 3. Use the ternary operator

Target: Use the ternary operator. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```d
int a = 10;
writeln(a > 5 ? "big" : "small");
```
### 4. Handle integer division

Target: Handle integer division. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```d
writeln(2 ^^ 10);  // 1024 — power operator
```

## Practice Questions

1. What is the key idea behind "Operators and Expressions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Operators and Expressions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Operators and Expressions"
1. "Provide advanced patterns and performance considerations for Operators and Expressions"

## Key Takeaways

- Master the core ideas of Operators and Expressions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
