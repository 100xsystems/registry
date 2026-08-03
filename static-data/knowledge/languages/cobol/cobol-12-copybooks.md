---
{
  "title": "Copybooks and Modularity",
  "description": "COPY statements and shared data definitions.",
  "type": "lesson",
  "order": 12,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use COPY statements",
    "Structure copybooks",
    "Replace text with REPLACING",
    "Share record layouts"
  ],
  "knowledge_refs": [
    "cobol/cobol-12-copybooks"
  ],
  "prerequisites": [
    "COBOL-11: Sorting Data"
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

# COBOL-12-COPYBOOKS: Copybooks and Modularity

## Introduction

COPY statements and shared data definitions. By the end of this lesson you will be able to: Use COPY statements; Structure copybooks; Replace text with REPLACING; Share record layouts.

## Key Concepts

### 1. Use COPY statements

Target: Use COPY statements. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```cobol
           COPY CUST-RECORD.
```
### 2. Structure copybooks

Target: Structure copybooks. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```cobol
           COPY CUST-RECORD REPLACING CUSTOMER BY VENDOR.
```
### 3. Replace text with REPLACING

Target: Replace text with REPLACING. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```cobol
       *  COPYBOOK: CUST-RECORD
       01 CUSTOMER.
          05 CUST-ID PIC 9(6).
```
### 4. Share record layouts

Target: Share record layouts. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```cobol
       DATA DIVISION.
       WORKING-STORAGE SECTION.
           COPY CUST-RECORD.
```

## Practice Questions

1. What is the key idea behind "Copybooks and Modularity"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Copybooks and Modularity with analogies and real-world examples"
1. "Show me common mistakes beginners make with Copybooks and Modularity"
1. "Provide advanced patterns and performance considerations for Copybooks and Modularity"

## Key Takeaways

- Master the core ideas of Copybooks and Modularity through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
