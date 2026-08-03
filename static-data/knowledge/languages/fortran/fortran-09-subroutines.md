---
{
  "title": "Subroutines",
  "description": "Procedures with multiple outputs.",
  "type": "lesson",
  "order": 9,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write subroutines",
    "Use intent(inout) arguments",
    "Call by reference semantics",
    "Structure programs with procedures"
  ],
  "knowledge_refs": [
    "fortran/fortran-09-subroutines"
  ],
  "prerequisites": [
    "Fortran-08: Functions"
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

# FORTRAN-09-SUBROUTINES: Subroutines

## Introduction

Procedures with multiple outputs. By the end of this lesson you will be able to: Write subroutines; Use intent(inout) arguments; Call by reference semantics; Structure programs with procedures.

## Key Concepts

### 1. Write subroutines

Target: Write subroutines. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```fortran
program use_s
  implicit none
  integer :: x, y
  x = 1; y = 2
  call swap(x, y)
  print *, x, y
contains
  subroutine swap(a, b)
    integer, intent(inout) :: a, b
    integer :: t
    t = a; a = b; b = t
  end subroutine swap
end program use_s
```
### 2. Use intent(inout) arguments

Target: Use intent(inout) arguments. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```fortran
subroutine stats(v, n, mean, std)
  integer, intent(in) :: n
  real, intent(in) :: v(n)
  real, intent(out) :: mean, std
  mean = sum(v) / n
  std = sqrt(sum((v - mean)**2) / n)
end subroutine stats
```
### 3. Call by reference semantics

Target: Call by reference semantics. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```fortran
call init(data)
call process(data)
call finalize(data)
```
### 4. Structure programs with procedures

Target: Structure programs with procedures. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```fortran
subroutine report(x, y)
  integer, intent(in) :: x
  integer, intent(out) :: y
  y = x * 2
end subroutine report
```

## Practice Questions

1. What is the key idea behind "Subroutines"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Subroutines with analogies and real-world examples"
1. "Show me common mistakes beginners make with Subroutines"
1. "Provide advanced patterns and performance considerations for Subroutines"

## Key Takeaways

- Master the core ideas of Subroutines through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
