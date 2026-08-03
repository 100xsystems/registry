---
{
  "title": "Modern COBOL Practices",
  "description": "Date handling and modern standards.",
  "type": "lesson",
  "order": 19,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Handle dates with proper formats",
    "Use modern standards",
    "Integrate with JSON/XML",
    "Write maintainable COBOL"
  ],
  "knowledge_refs": [
    "cobol/cobol-19-y2k-era"
  ],
  "prerequisites": [
    "COBOL-18: Performance and Optimization"
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

# COBOL-19-Y2K-ERA: Modern COBOL Practices

## Introduction

Date handling and modern standards. By the end of this lesson you will be able to: Handle dates with proper formats; Use modern standards; Integrate with JSON/XML; Write maintainable COBOL.

## Key Concepts

### 1. Handle dates with proper formats

Target: Handle dates with proper formats. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```cobol
       01 WS-DATE PIC 9(8).
           MOVE FUNCTION CURRENT-DATE TO WS-DATE.
```
### 2. Use modern standards

Target: Use modern standards. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```cobol
       01 WS-TODAY.
          05 WS-YEAR PIC 9(4).
          05 WS-MONTH PIC 99.
          05 WS-DAY PIC 99.
```
### 3. Integrate with JSON/XML

Target: Integrate with JSON/XML. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```cobol
           MOVE FUNCTION CURRENT-DATE(1:8) TO WS-DATE.
```
### 4. Write maintainable COBOL

Target: Write maintainable COBOL. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```cobol
       *  keep comments and structure clear
```

## Practice Questions

1. What is the key idea behind "Modern COBOL Practices"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Modern COBOL Practices with analogies and real-world examples"
1. "Show me common mistakes beginners make with Modern COBOL Practices"
1. "Provide advanced patterns and performance considerations for Modern COBOL Practices"

## Key Takeaways

- Master the core ideas of Modern COBOL Practices through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
