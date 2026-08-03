---
{
  "title": "PERFORM and Paragraphs",
  "description": "Structured control flow and paragraphs.",
  "type": "lesson",
  "order": 7,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Call paragraphs with PERFORM",
    "Use PERFORM ... TIMES",
    "Use PERFORM UNTIL",
    "Structure program flow"
  ],
  "knowledge_refs": [
    "cobol/cobol-07-perform"
  ],
  "prerequisites": [
    "COBOL-06: IF and Evaluate"
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

# COBOL-07-PERFORM: PERFORM and Paragraphs

## Introduction

Structured control flow and paragraphs. By the end of this lesson you will be able to: Call paragraphs with PERFORM; Use PERFORM ... TIMES; Use PERFORM UNTIL; Structure program flow.

## Key Concepts

### 1. Call paragraphs with PERFORM

Target: Call paragraphs with PERFORM. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```cobol
           PERFORM INIT-PARA.
           PERFORM PROCESS-PARA.
           STOP RUN.
       INIT-PARA.
           MOVE 0 TO WS-COUNT.
```
### 2. Use PERFORM ... TIMES

Target: Use PERFORM ... TIMES. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```cobol
           PERFORM DISPLAY-STEP 5 TIMES.
```
### 3. Use PERFORM UNTIL

Target: Use PERFORM UNTIL. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```cobol
           PERFORM UNTIL WS-DONE = "Y"
              ADD 1 TO WS-COUNT
           END-PERFORM.
```
### 4. Structure program flow

Target: Structure program flow. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```cobol
       MAIN-PARA.
           PERFORM 1000-INIT
           PERFORM 2000-PROCESS
           PERFORM 9000-EXIT.
           STOP RUN.
```

## Practice Questions

1. What is the key idea behind "PERFORM and Paragraphs"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain PERFORM and Paragraphs with analogies and real-world examples"
1. "Show me common mistakes beginners make with PERFORM and Paragraphs"
1. "Provide advanced patterns and performance considerations for PERFORM and Paragraphs"

## Key Takeaways

- Master the core ideas of PERFORM and Paragraphs through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
