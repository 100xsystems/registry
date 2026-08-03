---
{
  "title": "Subprograms and CALL",
  "description": "CALL statements and linkage sections.",
  "type": "lesson",
  "order": 13,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write called subprograms",
    "Pass data via LINKAGE",
    "Use CALL and USING",
    "Return control properly"
  ],
  "knowledge_refs": [
    "cobol/cobol-13-subprograms"
  ],
  "prerequisites": [
    "COBOL-12: Copybooks and Modularity"
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

# COBOL-13-SUBPROGRAMS: Subprograms and CALL

## Introduction

CALL statements and linkage sections. By the end of this lesson you will be able to: Write called subprograms; Pass data via LINKAGE; Use CALL and USING; Return control properly.

## Key Concepts

### 1. Write called subprograms

Target: Write called subprograms. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. UTILITY.
       DATA DIVISION.
       LINKAGE SECTION.
       01 LS-NUM PIC 9(3).
```
### 2. Pass data via LINKAGE

Target: Pass data via LINKAGE. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```cobol
           CALL "UTILITY" USING WS-NUM.
```
### 3. Use CALL and USING

Target: Use CALL and USING. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```cobol
           CALL "UTILITY" USING BY REFERENCE WS-NUM,
                BY CONTENT WS-OTHER.
```
### 4. Return control properly

Target: Return control properly. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```cobol
       PROCEDURE DIVISION USING LS-NUM.
           ADD 1 TO LS-NUM.
           GOBACK.
```

## Practice Questions

1. What is the key idea behind "Subprograms and CALL"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Subprograms and CALL with analogies and real-world examples"
1. "Show me common mistakes beginners make with Subprograms and CALL"
1. "Provide advanced patterns and performance considerations for Subprograms and CALL"

## Key Takeaways

- Master the core ideas of Subprograms and CALL through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
