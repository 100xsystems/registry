---
{
  "title": "Getting Started with COBOL",
  "description": "Divisions, identification, and hello world.",
  "type": "lesson",
  "order": 1,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Understand the four divisions",
    "Write a hello world program",
    "Compile with GnuCOBOL",
    "Read simple COBOL output"
  ],
  "knowledge_refs": [
    "cobol/cobol-01-getting-started"
  ],
  "prerequisites": [
    "None — this is the entry point"
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

# COBOL-01-GETTING-STARTED: Getting Started with COBOL

## Introduction

Divisions, identification, and hello world. By the end of this lesson you will be able to: Understand the four divisions; Write a hello world program; Compile with GnuCOBOL; Read simple COBOL output.

## Key Concepts

### 1. Understand the four divisions

Target: Understand the four divisions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. HELLO.
       PROCEDURE DIVISION.
           DISPLAY "Hello, World!".
           STOP RUN.
```
### 2. Write a hello world program

Target: Write a hello world program. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```cobol
cobc -x hello.cob
./hello
```
### 3. Compile with GnuCOBOL

Target: Compile with GnuCOBOL. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. GREET.
       PROCEDURE DIVISION.
           DISPLAY "Hello, " WITH NO ADVANCING.
           DISPLAY "User!".
           STOP RUN.
```
### 4. Read simple COBOL output

Target: Read simple COBOL output. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. FACTS.
       PROCEDURE DIVISION.
           DISPLAY "COBOL: Common Business Oriented Language".
           STOP RUN.
```

## Practice Questions

1. What is the key idea behind "Getting Started with COBOL"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with COBOL with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with COBOL"
1. "Provide advanced patterns and performance considerations for Getting Started with COBOL"

## Key Takeaways

- Master the core ideas of Getting Started with COBOL through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
