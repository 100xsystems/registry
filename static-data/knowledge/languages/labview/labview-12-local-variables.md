---
{
  "title": "Local Variables and Properties",
  "description": "Share data within a VI.",
  "type": "lesson",
  "order": 12,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create local variables",
    "Use property nodes",
    "Control UI remotely",
    "Understand race conditions"
  ],
  "knowledge_refs": [
    "labview/labview-12-local-variables"
  ],
  "prerequisites": [
    "LabVIEW-11: SubVIs"
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

# LABVIEW-12-LOCAL-VARIABLES: Local Variables and Properties

## Introduction

Share data within a VI. By the end of this lesson you will be able to: Create local variables; Use property nodes; Control UI remotely; Understand race conditions.

## Key Concepts

### 1. Create local variables

Target: Create local variables. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```text
# Right-click a control > Create > Local Variable.
```
### 2. Use property nodes

Target: Use property nodes. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```text
# Property Node (right-click > Create > Property Node) changes
# control properties like Visible and Value.
```
### 3. Control UI remotely

Target: Control UI remotely. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```text
# Use Value property to read/write from the block diagram.
```
### 4. Understand race conditions

Target: Understand race conditions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```text
# Be careful: locals can race; prefer wires.
```

## Practice Questions

1. What is the key idea behind "Local Variables and Properties"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Local Variables and Properties with analogies and real-world examples"
1. "Show me common mistakes beginners make with Local Variables and Properties"
1. "Provide advanced patterns and performance considerations for Local Variables and Properties"

## Key Takeaways

- Master the core ideas of Local Variables and Properties through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
