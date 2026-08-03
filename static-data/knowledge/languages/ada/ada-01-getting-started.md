---
{
  "title": "Getting Started with Ada",
  "description": "GNAT toolchain, hello world, and the Ada model.",
  "type": "lesson",
  "order": 1,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Install the GNAT toolchain",
    "Write and compile a hello world",
    "Understand program structure",
    "Use Ada.Text_IO for output"
  ],
  "knowledge_refs": [
    "ada/ada-01-getting-started"
  ],
  "prerequisites": [
    "None — this is the entry point"
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

# ADA-01-GETTING-STARTED: Getting Started with Ada

## Introduction

GNAT toolchain, hello world, and the Ada model. By the end of this lesson you will be able to: Install the GNAT toolchain; Write and compile a hello world; Understand program structure; Use Ada.Text_IO for output.

## Key Concepts

### 1. Install the GNAT toolchain

Target: Install the GNAT toolchain. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ada
with Ada.Text_IO;

procedure Hello is
begin
   Ada.Text_IO.Put_Line ("Hello, World!");
end Hello;
```
### 2. Write and compile a hello world

Target: Write and compile a hello world. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ada
gnatmake hello.adb
./hello
```
### 3. Understand program structure

Target: Understand program structure. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ada
with Ada.Text_IO;

procedure Greet is
begin
   Ada.Text_IO.Put_Line ("Hello, " & Ada.Command_Line.Argument (1));
end Greet;
```
### 4. Use Ada.Text_IO for output

Target: Use Ada.Text_IO for output. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ada
with Ada.Text_IO;

procedure Basics is
begin
   Ada.Text_IO.Put ("No newline");
   Ada.Text_IO.New_Line;
end Basics;
```

## Practice Questions

1. What is the key idea behind "Getting Started with Ada"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with Ada with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with Ada"
1. "Provide advanced patterns and performance considerations for Getting Started with Ada"

## Key Takeaways

- Master the core ideas of Getting Started with Ada through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
