---
{
  "title": "The Four Divisions",
  "description": "Identification, Environment, Data, and Procedure.",
  "type": "lesson",
  "order": 2,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Structure the identification division",
    "Set up the environment division",
    "Declare the data division",
    "Write the procedure division"
  ],
  "knowledge_refs": [
    "cobol/cobol-02-divisions"
  ],
  "prerequisites": [
    "COBOL-01: Getting Started with COBOL"
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

# COBOL-02-DIVISIONS: The Four Divisions

## Introduction

Identification, Environment, Data, and Procedure. By the end of this lesson you will be able to: Structure the identification division; Set up the environment division; Declare the data division; Write the procedure division.

## Key Concepts

### 1. Structure the identification division

Target: Structure the identification division. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. DEMO.
       ENVIRONMENT DIVISION.
       DATA DIVISION.
       PROCEDURE DIVISION.
           STOP RUN.
```
### 2. Set up the environment division

Target: Set up the environment division. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```cobol
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-NAME PIC X(20).
```
### 3. Declare the data division

Target: Declare the data division. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```cobol
       PROCEDURE DIVISION.
       MAIN-PARA.
           DISPLAY "Running".
           STOP RUN.
```
### 4. Write the procedure division

Target: Write the procedure division. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. VERSION.
       REMARKS. Sample program with comments.
```

## Practice Questions

1. What is the key idea behind "The Four Divisions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain The Four Divisions with analogies and real-world examples"
1. "Show me common mistakes beginners make with The Four Divisions"
1. "Provide advanced patterns and performance considerations for The Four Divisions"

## Key Takeaways

- Master the core ideas of The Four Divisions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
