---
{
  "title": "Data Logging",
  "description": "Record and replay data.",
  "type": "lesson",
  "order": 17,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Log to TDMS",
    "Read TDMS files",
    "Stream to disk",
    "Use the Datalogging palette"
  ],
  "knowledge_refs": [
    "labview/labview-17-data-logging"
  ],
  "prerequisites": [
    "LabVIEW-16: Data Acquisition (DAQ)"
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

# LABVIEW-17-DATA-LOGGING: Data Logging

## Introduction

Record and replay data. By the end of this lesson you will be able to: Log to TDMS; Read TDMS files; Stream to disk; Use the Datalogging palette.

## Key Concepts

### 1. Log to TDMS

Target: Log to TDMS. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```text
# TDMS Write (Programming > File I/O > TDMS) streams data.
```
### 2. Read TDMS files

Target: Read TDMS files. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```text
# TDMS Read reloads logged data.
```
### 3. Stream to disk

Target: Stream to disk. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```text
# Open TDMS Reference first, then TDMS Write.
```
### 4. Use the Datalogging palette

Target: Use the Datalogging palette. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```text
# TDMS files are self-describing and fast.
```

## Practice Questions

1. What is the key idea behind "Data Logging"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Data Logging with analogies and real-world examples"
1. "Show me common mistakes beginners make with Data Logging"
1. "Provide advanced patterns and performance considerations for Data Logging"

## Key Takeaways

- Master the core ideas of Data Logging through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
