---
{
  "title": "File Input/Output",
  "description": "Read and write files with formatting.",
  "type": "lesson",
  "order": 12,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Open files with open",
    "Read and write formatted data",
    "Use format statements",
    "Handle iostat errors"
  ],
  "knowledge_refs": [
    "fortran/fortran-12-io"
  ],
  "prerequisites": [
    "Fortran-11: Derived Types"
  ],
  "references": [
    {
      "title": "Fortran 90/95 Standard",
      "url": "https://wg5-fortran.org/",
      "description": "The official standards committee"
    },
    {
      "title": "Fortran Best Practices",
      "url": "https://fortran-lang.org/en/learn/",
      "description": "fortran-lang.org learning resources"
    },
    {
      "title": "Modern Fortran Explained",
      "url": "https://www.oxford.universitypressscholarship.com/",
      "description": "Metcalf, Reid & Cohen textbook"
    }
  ]
}
---

# FORTRAN-12-IO: File Input/Output

## Introduction

Read and write files with formatting. By the end of this lesson you will be able to: Open files with open; Read and write formatted data; Use format statements; Handle iostat errors.

## Key Concepts

### 1. Open files with open

Target: Open files with open. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```fortran
program fileio
  implicit none
  integer :: unit, ios
  open(newunit=unit, file="data.txt", status="old", action="read", iostat=ios)
  if (ios /= 0) print *, "Error opening"
  close(unit)
end program fileio
```
### 2. Read and write formatted data

Target: Read and write formatted data. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```fortran
write(unit, *) "hello"
write(unit, "(I5)") 42
```
### 3. Use format statements

Target: Use format statements. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```fortran
read(unit, *, iostat=ios) x
if (ios /= 0) print *, "Read failed"
```
### 4. Handle iostat errors

Target: Handle iostat errors. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```fortran
open(10, file="out.txt")
write(10, "(A, I3)") "count=", 7
close(10)
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
