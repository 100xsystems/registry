---
{
  "title": "Tasking and Concurrency",
  "description": "Ada's native tasking model.",
  "type": "lesson",
  "order": 16,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Create task types",
    "Use entries and accepts",
    "Synchronize with protected objects",
    "Avoid race conditions"
  ],
  "knowledge_refs": [
    "ada/ada-16-tasking"
  ],
  "prerequisites": [
    "Ada-15: File Input/Output"
  ],
  "references": [
    {
      "title": "Ada Reference Manual",
      "url": "https://www.adaic.org/resources/add_content/standards/",
      "description": "The official language standard"
    },
    {
      "title": "Learn Ada",
      "url": "https://learn.adacore.com/",
      "description": "AdaCore official interactive course"
    },
    {
      "title": "Ada Programming (Wikibooks)",
      "url": "https://en.wikibooks.org/wiki/Ada_Programming",
      "description": "Community textbook"
    }
  ]
}
---

# ADA-16-TASKING: Tasking and Concurrency

## Introduction

Ada's native tasking model. By the end of this lesson you will be able to: Create task types; Use entries and accepts; Synchronize with protected objects; Avoid race conditions.

## Key Concepts

### 1. Create task types

Target: Create task types. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ada
task Worker is
   entry Start;
end Worker;

task body Worker is
begin
   accept Start;
   Put_Line ("Working");
end Worker;
```
### 2. Use entries and accepts

Target: Use entries and accepts. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ada
task type Printer;
P : Printer;
```
### 3. Synchronize with protected objects

Target: Synchronize with protected objects. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ada
protected Counter is
   procedure Inc;
   function Get return Integer;
private
   Value : Integer := 0;
end Counter;
```
### 4. Avoid race conditions

Target: Avoid race conditions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ada
select
   accept Stop;
else
   delay 1.0;
end select;
```

## Practice Questions

1. What is the key idea behind "Tasking and Concurrency"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Tasking and Concurrency with analogies and real-world examples"
1. "Show me common mistakes beginners make with Tasking and Concurrency"
1. "Provide advanced patterns and performance considerations for Tasking and Concurrency"

## Key Takeaways

- Master the core ideas of Tasking and Concurrency through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
