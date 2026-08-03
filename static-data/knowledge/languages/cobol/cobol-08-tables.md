---
{
  "title": "Tables and Arrays",
  "description": "OCCURS clauses and table processing.",
  "type": "lesson",
  "order": 8,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define tables with OCCURS",
    "Index and access elements",
    "Iterate over tables",
    "Use subscripting safely"
  ],
  "knowledge_refs": [
    "cobol/cobol-08-tables"
  ],
  "prerequisites": [
    "COBOL-07: PERFORM and Paragraphs"
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

# COBOL-08-TABLES: Tables and Arrays

## Introduction

OCCURS clauses and table processing. By the end of this lesson you will be able to: Define tables with OCCURS; Index and access elements; Iterate over tables; Use subscripting safely.

## Key Concepts

### 1. Define tables with OCCURS

Target: Define tables with OCCURS. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```cobol
       01 WS-TABLE.
          05 WS-ENTRY PIC 9(3) OCCURS 10 TIMES.
```
### 2. Index and access elements

Target: Index and access elements. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```cobol
           MOVE 5 TO WS-ENTRY(1).
           DISPLAY WS-ENTRY(1).
```
### 3. Iterate over tables

Target: Iterate over tables. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```cobol
           PERFORM VARYING I FROM 1 BY 1 UNTIL I > 10
              DISPLAY WS-ENTRY(I)
           END-PERFORM.
```
### 4. Use subscripting safely

Target: Use subscripting safely. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```cobol
       01 WS-MATRIX.
          05 WS-ROW OCCURS 3 TIMES.
             10 WS-CELL PIC 9 OCCURS 3 TIMES.
```

## Practice Questions

1. What is the key idea behind "Tables and Arrays"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Tables and Arrays with analogies and real-world examples"
1. "Show me common mistakes beginners make with Tables and Arrays"
1. "Provide advanced patterns and performance considerations for Tables and Arrays"

## Key Takeaways

- Master the core ideas of Tables and Arrays through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
