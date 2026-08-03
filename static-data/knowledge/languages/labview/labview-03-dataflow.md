---
{
  "title": "Dataflow Programming",
  "description": "Wires, terminals, and execution order.",
  "type": "lesson",
  "order": 3,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Understand dataflow model",
    "Wire controls to functions",
    "Trace execution order",
    "Use tunnels"
  ],
  "knowledge_refs": [
    "labview/labview-03-dataflow"
  ],
  "prerequisites": [
    "LabVIEW-02: Controls and Palettes"
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

# LABVIEW-03-DATAFLOW: Dataflow Programming

## Introduction

Wires, terminals, and execution order. By the end of this lesson you will be able to: Understand dataflow model; Wire controls to functions; Trace execution order; Use tunnels.

## Key Concepts

### 1. Understand dataflow model

Target: Understand dataflow model. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```text
# Wire a Numeric Control into the Add function; wire Add output to an indicator.
```
### 2. Wire controls to functions

Target: Wire controls to functions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```text
# Dataflow: a node runs when all inputs are ready.
```
### 3. Trace execution order

Target: Trace execution order. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```text
# Use the Probe tool (right-click wire > Probe) to see values.
```
### 4. Use tunnels

Target: Use tunnels. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```text
# Highlight Execution (light bulb icon) animates data flow.
```

## Practice Questions

1. What is the key idea behind "Dataflow Programming"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Dataflow Programming with analogies and real-world examples"
1. "Show me common mistakes beginners make with Dataflow Programming"
1. "Provide advanced patterns and performance considerations for Dataflow Programming"

## Key Takeaways

- Master the core ideas of Dataflow Programming through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
