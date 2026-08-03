---
{
  "title": "Arithmetic Operations",
  "description": "ADD, SUBTRACT, MULTIPLY, DIVIDE, COMPUTE.",
  "type": "lesson",
  "order": 5,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use ADD and SUBTRACT",
    "Use MULTIPLY and DIVIDE",
    "Compute with COMPUTE",
    "Handle ROUNDED and ON SIZE ERROR"
  ],
  "knowledge_refs": [
    "cobol/cobol-05-arithmetic"
  ],
  "prerequisites": [
    "COBOL-04: MOVE and DISPLAY"
  ],
  "references": [
    {
      "title": "GnuCOBOL Manual",
      "url": "https://www.ibm.com/docs/en/cobol-zos/",
      "description": "IBM Enterprise COBOL documentation"
    },
    {
      "title": "GnuCOBOL Documentation",
      "url": "https://gnucobol.sourceforge.io/",
      "description": "Open-source COBOL compiler"
    },
    {
      "title": "COBOL Tutorial (TutorialsPoint)",
      "url": "https://www.tutorialspoint.com/cobol/index.htm",
      "description": "Beginner COBOL guide"
    }
  ]
}
---

# COBOL-05-ARITHMETIC: Arithmetic Operations

## Introduction

ADD, SUBTRACT, MULTIPLY, DIVIDE, COMPUTE. By the end of this lesson you will be able to: Use ADD and SUBTRACT; Use MULTIPLY and DIVIDE; Compute with COMPUTE; Handle ROUNDED and ON SIZE ERROR.

## Key Concepts

### 1. Use ADD and SUBTRACT

Target: Use ADD and SUBTRACT. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```cobol
           ADD 10 TO WS-TOTAL.
           SUBTRACT 5 FROM WS-TOTAL.
```
### 2. Use MULTIPLY and DIVIDE

Target: Use MULTIPLY and DIVIDE. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```cobol
           MULTIPLY WS-A BY WS-B GIVING WS-C.
```
### 3. Compute with COMPUTE

Target: Compute with COMPUTE. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```cobol
           COMPUTE WS-TOTAL = WS-A + WS-B * 2.
```
### 4. Handle ROUNDED and ON SIZE ERROR

Target: Handle ROUNDED and ON SIZE ERROR. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```cobol
           ADD WS-A TO WS-B ROUNDED
              ON SIZE ERROR DISPLAY "Overflow" END-ADD.
```

## Practice Questions

1. What is the key idea behind "Arithmetic Operations"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Arithmetic Operations with analogies and real-world examples"
1. "Show me common mistakes beginners make with Arithmetic Operations"
1. "Provide advanced patterns and performance considerations for Arithmetic Operations"

## Key Takeaways

- Master the core ideas of Arithmetic Operations through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
