---
{
  "title": "File Input/Output",
  "description": "Text and binary file handling.",
  "type": "lesson",
  "order": 15,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Open and close text files",
    "Read and write text",
    "Handle end of file",
    "Work with binary files"
  ],
  "knowledge_refs": [
    "ada/ada-15-file-io"
  ],
  "prerequisites": [
    "Ada-14: Tagged Types and OOP"
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

# ADA-15-FILE-IO: File Input/Output

## Introduction

Text and binary file handling. By the end of this lesson you will be able to: Open and close text files; Read and write text; Handle end of file; Work with binary files.

## Key Concepts

### 1. Open and close text files

Target: Open and close text files. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ada
with Ada.Text_IO;
use Ada.Text_IO;
F : File_Type;
```
### 2. Read and write text

Target: Read and write text. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ada
Open (F, In_File, "data.txt");
```
### 3. Handle end of file

Target: Handle end of file. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ada
while not End_Of_File (F) loop
   Get_Line (F, Line);
   Put_Line (Line);
end loop;
```
### 4. Work with binary files

Target: Work with binary files. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ada
Create (F, Out_File, "out.txt");
Put_Line (F, "written line");
Close (F);
```

## Practice Questions

1. What is the key idea behind "File Input/Output"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain File Input/Output with analogies and real-world examples"
1. "Show me common mistakes beginners make with File Input/Output"
1. "Provide advanced patterns and performance considerations for File Input/Output"

## Key Takeaways

- Master the core ideas of File Input/Output through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
