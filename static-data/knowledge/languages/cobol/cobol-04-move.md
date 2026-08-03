---
{
  "title": "MOVE and DISPLAY",
  "description": "Data movement and output formatting.",
  "type": "lesson",
  "order": 4,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Move values between fields",
    "Display formatted output",
    "Understand elementary moves",
    "Initialize data with MOVE"
  ],
  "knowledge_refs": [
    "cobol/cobol-04-move"
  ],
  "prerequisites": [
    "COBOL-03: Data Types and Pictures"
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

# COBOL-04-MOVE: MOVE and DISPLAY

## Introduction

Data movement and output formatting. By the end of this lesson you will be able to: Move values between fields; Display formatted output; Understand elementary moves; Initialize data with MOVE.

## Key Concepts

### 1. Move values between fields

Target: Move values between fields. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```cobol
           MOVE 25 TO WS-AGE.
           DISPLAY "Age: " WS-AGE.
```
### 2. Display formatted output

Target: Display formatted output. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```cobol
           MOVE "Hello" TO WS-NAME.
           DISPLAY WS-NAME.
```
### 3. Understand elementary moves

Target: Understand elementary moves. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```cobol
           MOVE SPACES TO WS-NAME.
           MOVE ZEROES TO WS-COUNT.
```
### 4. Initialize data with MOVE

Target: Initialize data with MOVE. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```cobol
           MOVE WS-A TO WS-B.
           DISPLAY WS-B.
```

## Practice Questions

1. What is the key idea behind "MOVE and DISPLAY"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain MOVE and DISPLAY with analogies and real-world examples"
1. "Show me common mistakes beginners make with MOVE and DISPLAY"
1. "Provide advanced patterns and performance considerations for MOVE and DISPLAY"

## Key Takeaways

- Master the core ideas of MOVE and DISPLAY through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
