---
{
  "title": "Indexed and Relative Files",
  "description": "Random access file organizations.",
  "type": "lesson",
  "order": 14,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Declare indexed files",
    "Read by key",
    "Write and rewrite records",
    "Handle record status"
  ],
  "knowledge_refs": [
    "cobol/cobol-14-indexed-files"
  ],
  "prerequisites": [
    "COBOL-13: Subprograms and CALL"
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

# COBOL-14-INDEXED-FILES: Indexed and Relative Files

## Introduction

Random access file organizations. By the end of this lesson you will be able to: Declare indexed files; Read by key; Write and rewrite records; Handle record status.

## Key Concepts

### 1. Declare indexed files

Target: Declare indexed files. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```cobol
       SELECT WS-FILE ASSIGN TO "data.dat"
              ORGANIZATION IS INDEXED
              ACCESS MODE IS DYNAMIC
              RECORD KEY IS WS-KEY.
```
### 2. Read by key

Target: Read by key. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```cobol
           READ WS-FILE KEY IS WS-KEY
              INVALID KEY DISPLAY "Not found"
           END-READ.
```
### 3. Write and rewrite records

Target: Write and rewrite records. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```cobol
           WRITE WS-REC
              INVALID KEY DISPLAY "Duplicate"
           END-WRITE.
```
### 4. Handle record status

Target: Handle record status. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```cobol
           REWRITE WS-REC.
```

## Practice Questions

1. What is the key idea behind "Indexed and Relative Files"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Indexed and Relative Files with analogies and real-world examples"
1. "Show me common mistakes beginners make with Indexed and Relative Files"
1. "Provide advanced patterns and performance considerations for Indexed and Relative Files"

## Key Takeaways

- Master the core ideas of Indexed and Relative Files through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
