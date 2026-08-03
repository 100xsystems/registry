---
{
  "title": "Mainframe and z/OS COBOL",
  "description": "JCL, datasets, and enterprise integration.",
  "type": "lesson",
  "order": 20,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Understand JCL structure",
    "Compile on z/OS",
    "Use VSAM datasets",
    "Integrate with CICS"
  ],
  "knowledge_refs": [
    "cobol/cobol-20-mainframe"
  ],
  "prerequisites": [
    "COBOL-19: Modern COBOL Practices"
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

# COBOL-20-MAINFRAME: Mainframe and z/OS COBOL

## Introduction

JCL, datasets, and enterprise integration. By the end of this lesson you will be able to: Understand JCL structure; Compile on z/OS; Use VSAM datasets; Integrate with CICS.

## Key Concepts

### 1. Understand JCL structure

Target: Understand JCL structure. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```cobol
//JOB1 JOB (ACCT),CLASS=A,MSGCLASS=H
//STEP1 EXEC PGM=MYPROG
```
### 2. Compile on z/OS

Target: Compile on z/OS. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```cobol
//DD1 DD DSN=MY.DATA.SET,DISP=SHR
```
### 3. Use VSAM datasets

Target: Use VSAM datasets. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```cobol
       EXEC CICS
          SEND TEXT FROM(WS-MSG)
       END-EXEC.
```
### 4. Integrate with CICS

Target: Integrate with CICS. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```cobol
//STEP1 EXEC PGM=IGYCRCTL
//SYSIN DD DSN=SRC.COBOL(MYPROG),DISP=SHR
```

## Practice Questions

1. What is the key idea behind "Mainframe and z/OS COBOL"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Mainframe and z/OS COBOL with analogies and real-world examples"
1. "Show me common mistakes beginners make with Mainframe and z/OS COBOL"
1. "Provide advanced patterns and performance considerations for Mainframe and z/OS COBOL"

## Key Takeaways

- Master the core ideas of Mainframe and z/OS COBOL through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
