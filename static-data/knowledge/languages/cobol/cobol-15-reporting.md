---
{
  "title": "Report Writing",
  "description": "REPORT SECTION and report generation.",
  "type": "lesson",
  "order": 15,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Define report groups",
    "Generate headers and footers",
    "Accumulate control totals",
    "Produce formatted reports"
  ],
  "knowledge_refs": [
    "cobol/cobol-15-reporting"
  ],
  "prerequisites": [
    "COBOL-14: Indexed and Relative Files"
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

# COBOL-15-REPORTING: Report Writing

## Introduction

REPORT SECTION and report generation. By the end of this lesson you will be able to: Define report groups; Generate headers and footers; Accumulate control totals; Produce formatted reports.

## Key Concepts

### 1. Define report groups

Target: Define report groups. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```cobol
       FD WS-REPORT.
       REPORT SECTION.
       RD WS-RPT.
       01 HEADING-LINE.
          05 PIC X(30) VALUE "SALES REPORT".
```
### 2. Generate headers and footers

Target: Generate headers and footers. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```cobol
       REPORT SECTION.
       RD WS-RPT CONTROL IS WS-DEPT.
       01 DETAIL-LINE.
          05 WS-DEPT-COL PIC X(10).
```
### 3. Accumulate control totals

Target: Accumulate control totals. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```cobol
       INITIATE WS-RPT.
       GENERATE DETAIL-LINE.
       TERMINATE WS-RPT.
```
### 4. Produce formatted reports

Target: Produce formatted reports. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```cobol
       01 FOOTING-LINE.
          05 PIC X(10) VALUE "TOTAL:".
          05 WS-TOTAL-COL PIC Z(9).
```

## Practice Questions

1. What is the key idea behind "Report Writing"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Report Writing with analogies and real-world examples"
1. "Show me common mistakes beginners make with Report Writing"
1. "Provide advanced patterns and performance considerations for Report Writing"

## Key Takeaways

- Master the core ideas of Report Writing through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
