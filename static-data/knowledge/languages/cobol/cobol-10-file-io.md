---
{
  "title": "Sequential File I/O",
  "description": "Open, read, write, and close sequential files.",
  "type": "lesson",
  "order": 10,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Declare file records in FD",
    "Open files in modes",
    "Read and write records",
    "Detect end of file"
  ],
  "knowledge_refs": [
    "cobol/cobol-10-file-io"
  ],
  "prerequisites": [
    "COBOL-09: String Handling"
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

# COBOL-10-FILE-IO: Sequential File I/O

## Introduction

Open, read, write, and close sequential files. By the end of this lesson you will be able to: Declare file records in FD; Open files in modes; Read and write records; Detect end of file.

## Key Concepts

### 1. Declare file records in FD

Target: Declare file records in FD. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```cobol
       FD WS-FILE.
       01 WS-REC PIC X(80).
```
### 2. Open files in modes

Target: Open files in modes. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```cobol
           OPEN INPUT WS-FILE.
           OPEN OUTPUT WS-OUTFILE.
```
### 3. Read and write records

Target: Read and write records. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```cobol
           READ WS-FILE
              AT END SET WS-EOF TO TRUE
           END-READ.
```
### 4. Detect end of file

Target: Detect end of file. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```cobol
           WRITE WS-OUTREC.
           CLOSE WS-FILE.
```

## Practice Questions

1. What is the key idea behind "Sequential File I/O"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Sequential File I/O with analogies and real-world examples"
1. "Show me common mistakes beginners make with Sequential File I/O"
1. "Provide advanced patterns and performance considerations for Sequential File I/O"

## Key Takeaways

- Master the core ideas of Sequential File I/O through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
