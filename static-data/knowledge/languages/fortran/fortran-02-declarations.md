---
{
  "title": "Variables and Declarations",
  "description": "Implicit typing, kinds, and declarations.",
  "type": "lesson",
  "order": 2,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Declare variables with types",
    "Use integer and real kinds",
    "Declare parameters with parameter",
    "Turn off implicit typing"
  ],
  "knowledge_refs": [
    "fortran/fortran-02-declarations"
  ],
  "prerequisites": [
    "Fortran-01: Getting Started with Fortran"
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

# FORTRAN-02-DECLARATIONS: Variables and Declarations

## Introduction

Implicit typing, kinds, and declarations. By the end of this lesson you will be able to: Declare variables with types; Use integer and real kinds; Declare parameters with parameter; Turn off implicit typing.

## Key Concepts

### 1. Declare variables with types

Target: Declare variables with types. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```fortran
program vars
  implicit none
  integer :: i
  real :: x
end program vars
```
### 2. Use integer and real kinds

Target: Use integer and real kinds. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```fortran
program kinds
  implicit none
  integer, parameter :: dp = selected_real_kind(15, 307)
  real(kind=dp) :: pi
end program kinds
```
### 3. Declare parameters with parameter

Target: Declare parameters with parameter. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```fortran
program consts
  implicit none
  real, parameter :: pi = 3.14159265
  print *, pi
end program consts
```
### 4. Turn off implicit typing

Target: Turn off implicit typing. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```fortran
program init
  implicit none
  integer :: count = 0
  real :: total = 0.0
end program init
```

## Practice Questions

1. What is the key idea behind "Variables and Declarations"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Variables and Declarations with analogies and real-world examples"
1. "Show me common mistakes beginners make with Variables and Declarations"
1. "Provide advanced patterns and performance considerations for Variables and Declarations"

## Key Takeaways

- Master the core ideas of Variables and Declarations through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
