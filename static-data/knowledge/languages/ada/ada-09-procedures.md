---
{
  "title": "Procedures and Functions",
  "description": "Subprograms, parameters, and modes.",
  "type": "lesson",
  "order": 9,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write functions and procedures",
    "Use parameter modes in/out/in out",
    "Pass by reference safely",
    "Overload subprogram names"
  ],
  "knowledge_refs": [
    "ada/ada-09-procedures"
  ],
  "prerequisites": [
    "Ada-08: Records and Variants"
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

# ADA-09-PROCEDURES: Procedures and Functions

## Introduction

Subprograms, parameters, and modes. By the end of this lesson you will be able to: Write functions and procedures; Use parameter modes in/out/in out; Pass by reference safely; Overload subprogram names.

## Key Concepts

### 1. Write functions and procedures

Target: Write functions and procedures. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ada
function Add (A, B : Integer) return Integer is
begin
   return A + B;
end Add;
```
### 2. Use parameter modes in/out/in out

Target: Use parameter modes in/out/in out. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ada
procedure Swap (A, B : in out Integer) is
   Tmp : Integer := A;
begin
   A := B;
   B := Tmp;
end Swap;
```
### 3. Pass by reference safely

Target: Pass by reference safely. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ada
procedure Log (Msg : in String) is
begin
   Ada.Text_IO.Put_Line (Msg);
end Log;
```
### 4. Overload subprogram names

Target: Overload subprogram names. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ada
function Max (A, B : Integer) return Integer is
begin
   return (if A > B then A else B);
end Max;
```

## Practice Questions

1. What is the key idea behind "Procedures and Functions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Procedures and Functions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Procedures and Functions"
1. "Provide advanced patterns and performance considerations for Procedures and Functions"

## Key Takeaways

- Master the core ideas of Procedures and Functions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
