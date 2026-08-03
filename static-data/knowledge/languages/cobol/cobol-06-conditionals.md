---
{
  "title": "IF and Evaluate",
  "description": "Conditional logic and structured decisions.",
  "type": "lesson",
  "order": 6,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Write IF/ELSE branches",
    "Use nested conditions",
    "Use EVALUATE statements",
    "Test conditions properly"
  ],
  "knowledge_refs": [
    "cobol/cobol-06-conditionals"
  ],
  "prerequisites": [
    "COBOL-05: Arithmetic Operations"
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

# COBOL-06-CONDITIONALS: IF and Evaluate

## Introduction

Conditional logic and structured decisions. By the end of this lesson you will be able to: Write IF/ELSE branches; Use nested conditions; Use EVALUATE statements; Test conditions properly.

## Key Concepts

### 1. Write IF/ELSE branches

Target: Write IF/ELSE branches. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```cobol
           IF WS-AGE >= 18
              DISPLAY "Adult"
           ELSE
              DISPLAY "Minor"
           END-IF.
```
### 2. Use nested conditions

Target: Use nested conditions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```cobol
           IF WS-GRADE = "A" AND WS-PASS = "Y"
              DISPLAY "Excellent"
           END-IF.
```
### 3. Use EVALUATE statements

Target: Use EVALUATE statements. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```cobol
           EVALUATE WS-OPTION
              WHEN "1" DISPLAY "One"
              WHEN "2" DISPLAY "Two"
              WHEN OTHER DISPLAY "Other"
           END-EVALUATE.
```
### 4. Test conditions properly

Target: Test conditions properly. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```cobol
           IF WS-NUM > 0
              DISPLAY "Positive"
           END-IF.
```

## Practice Questions

1. What is the key idea behind "IF and Evaluate"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain IF and Evaluate with analogies and real-world examples"
1. "Show me common mistakes beginners make with IF and Evaluate"
1. "Provide advanced patterns and performance considerations for IF and Evaluate"

## Key Takeaways

- Master the core ideas of IF and Evaluate through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
