---
{
  "title": "Instrument Control",
  "description": "Talk to hardware (VISA/SCPI).",
  "type": "lesson",
  "order": 15,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Understand VISA",
    "Write SCPI commands",
    "Query instruments",
    "Use Instrument I/O Assistant"
  ],
  "knowledge_refs": [
    "labview/labview-15-instrument-control"
  ],
  "prerequisites": [
    "LabVIEW-14: File I/O"
  ],
  "references": [
    {
      "title": "LabVIEW Documentation",
      "url": "https://www.ni.com/docs/en-US/bundle/labview",
      "description": "Official NI documentation"
    },
    {
      "title": "LabVIEW Tutorials",
      "url": "https://learn.ni.com/",
      "description": "NI learning center"
    },
    {
      "title": "NI Community",
      "url": "https://forums.ni.com/t5/LabVIEW/bd-p/170",
      "description": "Community forum"
    }
  ]
}
---

# LABVIEW-15-INSTRUMENT-CONTROL: Instrument Control

## Introduction

Talk to hardware (VISA/SCPI). By the end of this lesson you will be able to: Understand VISA; Write SCPI commands; Query instruments; Use Instrument I/O Assistant.

## Key Concepts

### 1. Understand VISA

Target: Understand VISA. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```text
# Instrument I/O > VISA session.
# VISA Write sends a command; VISA Read receives a response.
```
### 2. Write SCPI commands

Target: Write SCPI commands. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```text
# Typical SCPI: "*IDN?" queries the instrument identity.
```
### 3. Query instruments

Target: Query instruments. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```text
# Use property nodes to set baud rate on serial sessions.
```
### 4. Use Instrument I/O Assistant

Target: Use Instrument I/O Assistant. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```text
# Instrument I/O Assistant auto-generates code.
```

## Practice Questions

1. What is the key idea behind "Instrument Control"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Instrument Control with analogies and real-world examples"
1. "Show me common mistakes beginners make with Instrument Control"
1. "Provide advanced patterns and performance considerations for Instrument Control"

## Key Takeaways

- Master the core ideas of Instrument Control through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
