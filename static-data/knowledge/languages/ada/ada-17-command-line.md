---
{
  "title": "Command-Line Interfaces",
  "description": "Parse arguments and build tools.",
  "type": "lesson",
  "order": 17,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Read command-line arguments",
    "Parse options",
    "Return exit codes",
    "Build a small CLI tool"
  ],
  "knowledge_refs": [
    "ada/ada-17-command-line"
  ],
  "prerequisites": [
    "Ada-16: Tasking and Concurrency"
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

# ADA-17-COMMAND-LINE: Command-Line Interfaces

## Introduction

Parse arguments and build tools. By the end of this lesson you will be able to: Read command-line arguments; Parse options; Return exit codes; Build a small CLI tool.

## Key Concepts

### 1. Read command-line arguments

Target: Read command-line arguments. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ada
with Ada.Command_Line;
use Ada.Command_Line;
if Argument_Count = 0 then
   Put_Line ("Usage: tool FILE");
end if;
```
### 2. Parse options

Target: Parse options. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ada
Arg := Argument (1);
```
### 3. Return exit codes

Target: Return exit codes. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ada
Set_Exit_Status (1);
```
### 4. Build a small CLI tool

Target: Build a small CLI tool. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ada
for i in 1 .. Argument_Count loop
   Put_Line (i'Image & ": " & Argument (i));
end loop;
```

## Practice Questions

1. What is the key idea behind "Command-Line Interfaces"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Command-Line Interfaces with analogies and real-world examples"
1. "Show me common mistakes beginners make with Command-Line Interfaces"
1. "Provide advanced patterns and performance considerations for Command-Line Interfaces"

## Key Takeaways

- Master the core ideas of Command-Line Interfaces through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
