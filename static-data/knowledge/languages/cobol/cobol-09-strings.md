---
{
  "title": "String Handling",
  "description": "STRING, UNSTRING, and character manipulation.",
  "type": "lesson",
  "order": 9,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Concatenate with STRING",
    "Split with UNSTRING",
    "Inspect characters",
    "Handle delimiters"
  ],
  "knowledge_refs": [
    "cobol/cobol-09-strings"
  ],
  "prerequisites": [
    "COBOL-08: Tables and Arrays"
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

# COBOL-09-STRINGS: String Handling

## Introduction

STRING, UNSTRING, and character manipulation. By the end of this lesson you will be able to: Concatenate with STRING; Split with UNSTRING; Inspect characters; Handle delimiters.

## Key Concepts

### 1. Concatenate with STRING

Target: Concatenate with STRING. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```cobol
           STRING WS-FIRST DELIMITED BY SPACE
                  " " DELIMITED BY SIZE
                  WS-LAST DELIMITED BY SPACE
                  INTO WS-FULL END-STRING.
```
### 2. Split with UNSTRING

Target: Split with UNSTRING. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```cobol
           UNSTRING WS-DATA DELIMITED BY ","
              INTO WS-A WS-B WS-C END-UNSTRING.
```
### 3. Inspect characters

Target: Inspect characters. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```cobol
           INSPECT WS-NAME TALLYING WS-CNT FOR CHARACTERS.
```
### 4. Handle delimiters

Target: Handle delimiters. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```cobol
           INSPECT WS-DATA REPLACING ALL " " BY "-".
```

## Practice Questions

1. What is the key idea behind "String Handling"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain String Handling with analogies and real-world examples"
1. "Show me common mistakes beginners make with String Handling"
1. "Provide advanced patterns and performance considerations for String Handling"

## Key Takeaways

- Master the core ideas of String Handling through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
