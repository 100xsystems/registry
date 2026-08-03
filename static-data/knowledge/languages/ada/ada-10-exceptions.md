---
{
  "title": "Exceptions",
  "description": "Raise, handle, and propagate exceptions.",
  "type": "lesson",
  "order": 10,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Declare exception types",
    "Raise exceptions",
    "Handle with exception blocks",
    "Use standard exceptions"
  ],
  "knowledge_refs": [
    "ada/ada-10-exceptions"
  ],
  "prerequisites": [
    "Ada-09: Procedures and Functions"
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

# ADA-10-EXCEPTIONS: Exceptions

## Introduction

Raise, handle, and propagate exceptions. By the end of this lesson you will be able to: Declare exception types; Raise exceptions; Handle with exception blocks; Use standard exceptions.

## Key Concepts

### 1. Declare exception types

Target: Declare exception types. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ada
Divide_By_Zero : exception;
```
### 2. Raise exceptions

Target: Raise exceptions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ada
if B = 0 then
   raise Divide_By_Zero;
end if;
```
### 3. Handle with exception blocks

Target: Handle with exception blocks. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ada
begin
   Compute;
exception
   when Divide_By_Zero =>
      Ada.Text_IO.Put_Line ("Caught division by zero");
end;
```
### 4. Use standard exceptions

Target: Use standard exceptions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ada
begin
   Danger;
exception
   when Constraint_Error => Put ("Range check failed");
   when others => Put ("Something else");
end;
```

## Practice Questions

1. What is the key idea behind "Exceptions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Exceptions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Exceptions"
1. "Provide advanced patterns and performance considerations for Exceptions"

## Key Takeaways

- Master the core ideas of Exceptions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
