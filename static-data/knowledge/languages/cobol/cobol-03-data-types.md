---
{
  "title": "Data Types and Pictures",
  "description": "PIC clauses, USAGE, and level numbers.",
  "type": "lesson",
  "order": 3,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Define PIC X and PIC 9 fields",
    "Use USAGE clauses",
    "Structure level numbers",
    "Declare group items"
  ],
  "knowledge_refs": [
    "cobol/cobol-03-data-types"
  ],
  "prerequisites": [
    "COBOL-02: The Four Divisions"
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

# COBOL-03-DATA-TYPES: Data Types and Pictures

## Introduction

PIC clauses, USAGE, and level numbers. By the end of this lesson you will be able to: Define PIC X and PIC 9 fields; Use USAGE clauses; Structure level numbers; Declare group items.

## Key Concepts

### 1. Define PIC X and PIC 9 fields

Target: Define PIC X and PIC 9 fields. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```cobol
       01 WS-NAME PIC X(30).
       01 WS-AGE PIC 9(3).
```
### 2. Use USAGE clauses

Target: Use USAGE clauses. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```cobol
       01 WS-SALARY PIC 9(7)V99.
       01 WS-RATE PIC S9(3)V99 COMP-3.
```
### 3. Structure level numbers

Target: Structure level numbers. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```cobol
       01 WS-EMPLOYEE.
          05 WS-ID PIC 9(5).
          05 WS-DEPT PIC X(10).
```
### 4. Declare group items

Target: Declare group items. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```cobol
       01 WS-FLAG PIC X VALUE "N".
```

## Practice Questions

1. What is the key idea behind "Data Types and Pictures"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Data Types and Pictures with analogies and real-world examples"
1. "Show me common mistakes beginners make with Data Types and Pictures"
1. "Provide advanced patterns and performance considerations for Data Types and Pictures"

## Key Takeaways

- Master the core ideas of Data Types and Pictures through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
