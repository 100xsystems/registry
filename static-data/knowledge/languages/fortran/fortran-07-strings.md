---
{
  "title": "Character Strings",
  "description": "Character variables, concatenation, and intrinsics.",
  "type": "lesson",
  "order": 7,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Declare character variables",
    "Concatenate with //",
    "Use trim, len, adjustl",
    "Compare strings"
  ],
  "knowledge_refs": [
    "fortran/fortran-07-strings"
  ],
  "prerequisites": [
    "Fortran-06: Arrays"
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

# FORTRAN-07-STRINGS: Character Strings

## Introduction

Character variables, concatenation, and intrinsics. By the end of this lesson you will be able to: Declare character variables; Concatenate with //; Use trim, len, adjustl; Compare strings.

## Key Concepts

### 1. Declare character variables

Target: Declare character variables. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```fortran
program str
  implicit none
  character(len=20) :: name = "Ada"
  print *, name
end program str
```
### 2. Concatenate with //

Target: Concatenate with //. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```fortran
character(len=50) :: full
full = "Hello" // " " // "World"
```
### 3. Use trim, len, adjustl

Target: Use trim, len, adjustl. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```fortran
print *, trim("  padded  ")
print *, len("hello")
```
### 4. Compare strings

Target: Compare strings. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```fortran
if (trim(a) == trim(b)) then
  print *, "equal"
end if
```

## Practice Questions

1. What is the key idea behind "Character Strings"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Character Strings with analogies and real-world examples"
1. "Show me common mistakes beginners make with Character Strings"
1. "Provide advanced patterns and performance considerations for Character Strings"

## Key Takeaways

- Master the core ideas of Character Strings through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
