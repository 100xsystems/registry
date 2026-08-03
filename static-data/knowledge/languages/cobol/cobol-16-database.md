---
{
  "title": "Database Access (SQL/DB2)",
  "description": "Embedded SQL in COBOL.",
  "type": "lesson",
  "order": 16,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Embed SQL statements",
    "Declare host variables",
    "Process query results",
    "Handle SQL errors"
  ],
  "knowledge_refs": [
    "cobol/cobol-16-database"
  ],
  "prerequisites": [
    "COBOL-15: Report Writing"
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

# COBOL-16-DATABASE: Database Access (SQL/DB2)

## Introduction

Embedded SQL in COBOL. By the end of this lesson you will be able to: Embed SQL statements; Declare host variables; Process query results; Handle SQL errors.

## Key Concepts

### 1. Embed SQL statements

Target: Embed SQL statements. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```cobol
       EXEC SQL
          SELECT NAME INTO :WS-NAME FROM EMP
          WHERE ID = :WS-ID
       END-EXEC.
```
### 2. Declare host variables

Target: Declare host variables. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```cobol
           EXEC SQL
              INSERT INTO EMP (ID, NAME)
              VALUES (:WS-ID, :WS-NAME)
           END-EXEC.
```
### 3. Process query results

Target: Process query results. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```cobol
       EXEC SQL
          DECLARE C1 CURSOR FOR SELECT * FROM EMP
       END-EXEC.
```
### 4. Handle SQL errors

Target: Handle SQL errors. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```cobol
           EXEC SQL WHENEVER SQLERROR
              PERFORM SQL-ERROR-PARA
           END-EXEC.
```

## Practice Questions

1. What is the key idea behind "Database Access (SQL/DB2)"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Database Access (SQL/DB2) with analogies and real-world examples"
1. "Show me common mistakes beginners make with Database Access (SQL/DB2)"
1. "Provide advanced patterns and performance considerations for Database Access (SQL/DB2)"

## Key Takeaways

- Master the core ideas of Database Access (SQL/DB2) through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
