---
{
  "title": "Performance and Optimization",
  "description": "Efficient table and file processing.",
  "type": "lesson",
  "order": 18,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Optimize table searches",
    "Use binary search",
    "Minimize I/O",
    "Use compiler options"
  ],
  "knowledge_refs": [
    "cobol/cobol-18-performance"
  ],
  "prerequisites": [
    "COBOL-17: Debugging COBOL"
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

# COBOL-18-PERFORMANCE: Performance and Optimization

## Introduction

Efficient table and file processing. By the end of this lesson you will be able to: Optimize table searches; Use binary search; Minimize I/O; Use compiler options.

## Key Concepts

### 1. Optimize table searches

Target: Optimize table searches. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```cobol
           SEARCH ALL WS-TABLE
              AT END DISPLAY "Not found"
              WHEN WS-KEY(WS-IDX) = WS-TARGET
                 DISPLAY "Found"
           END-SEARCH.
```
### 2. Use binary search

Target: Use binary search. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```cobol
           PERFORM VARYING I FROM 1 BY 1
              UNTIL I > WS-MAX OR WS-FOUND = "Y"
           END-PERFORM.
```
### 3. Minimize I/O

Target: Minimize I/O. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```cobol
           MOVE 0 TO WS-COUNTER.
           PERFORM UNTIL WS-COUNTER > 1000
              ADD 1 TO WS-COUNTER
           END-PERFORM.
```
### 4. Use compiler options

Target: Use compiler options. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```cobol
       *  compiler: cobc -O2 program.cob
```

## Practice Questions

1. What is the key idea behind "Performance and Optimization"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Performance and Optimization with analogies and real-world examples"
1. "Show me common mistakes beginners make with Performance and Optimization"
1. "Provide advanced patterns and performance considerations for Performance and Optimization"

## Key Takeaways

- Master the core ideas of Performance and Optimization through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
