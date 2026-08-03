---
{
  "title": "Sorting Data",
  "description": "SORT verb and file sorting.",
  "type": "lesson",
  "order": 11,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use the SORT verb",
    "Define sort keys",
    "Merge with MERGE",
    "Process sorted output"
  ],
  "knowledge_refs": [
    "cobol/cobol-11-sort"
  ],
  "prerequisites": [
    "COBOL-10: Sequential File I/O"
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

# COBOL-11-SORT: Sorting Data

## Introduction

SORT verb and file sorting. By the end of this lesson you will be able to: Use the SORT verb; Define sort keys; Merge with MERGE; Process sorted output.

## Key Concepts

### 1. Use the SORT verb

Target: Use the SORT verb. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```cobol
           SORT WS-SORTFILE ON ASCENDING KEY WS-KEY
              USING WS-INPUT GIVING WS-OUTPUT.
```
### 2. Define sort keys

Target: Define sort keys. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```cobol
           SORT WS-FILE ON DESCENDING KEY WS-SALARY.
```
### 3. Merge with MERGE

Target: Merge with MERGE. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```cobol
           MERGE WS-MERGE-FILE ON ASCENDING KEY WS-ID
              USING WS-FILE1 WS-FILE2
              GIVING WS-OUT.
```
### 4. Process sorted output

Target: Process sorted output. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```cobol
       SORT-FILE-PARA.
           SORT WS-SORTFILE ON ASCENDING KEY WS-NAME
              INPUT PROCEDURE IN-PARA
              OUTPUT PROCEDURE OUT-PARA.
```

## Practice Questions

1. What is the key idea behind "Sorting Data"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Sorting Data with analogies and real-world examples"
1. "Show me common mistakes beginners make with Sorting Data"
1. "Provide advanced patterns and performance considerations for Sorting Data"

## Key Takeaways

- Master the core ideas of Sorting Data through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
