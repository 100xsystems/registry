---
{
  "title": "Data Acquisition (DAQ)",
  "description": "Read sensors with DAQmx.",
  "type": "lesson",
  "order": 16,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use DAQmx API",
    "Configure analog input",
    "Read samples",
    "Handle sampling rates"
  ],
  "knowledge_refs": [
    "labview/labview-16-daq"
  ],
  "prerequisites": [
    "LabVIEW-15: Instrument Control"
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

# LABVIEW-16-DAQ: Data Acquisition (DAQ)

## Introduction

Read sensors with DAQmx. By the end of this lesson you will be able to: Use DAQmx API; Configure analog input; Read samples; Handle sampling rates.

## Key Concepts

### 1. Use DAQmx API

Target: Use DAQmx API. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```text
# DAQmx Create Virtual Channel > Analog Input > Voltage.
```
### 2. Configure analog input

Target: Configure analog input. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```text
# DAQmx Timing configures the sample clock.
```
### 3. Read samples

Target: Read samples. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```text
# DAQmx Read brings samples into LabVIEW.
```
### 4. Handle sampling rates

Target: Handle sampling rates. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```text
# DAQmx Start Task / Clear Task manage the lifecycle.
```

## Practice Questions

1. What is the key idea behind "Data Acquisition (DAQ)"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Data Acquisition (DAQ) with analogies and real-world examples"
1. "Show me common mistakes beginners make with Data Acquisition (DAQ)"
1. "Provide advanced patterns and performance considerations for Data Acquisition (DAQ)"

## Key Takeaways

- Master the core ideas of Data Acquisition (DAQ) through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
