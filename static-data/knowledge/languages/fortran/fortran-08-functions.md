---
{
  "title": "Functions",
  "description": "Write and call functions with intent.",
  "type": "lesson",
  "order": 8,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write functions",
    "Use intent(in) arguments",
    "Return values properly",
    "Call intrinsic functions"
  ],
  "knowledge_refs": [
    "fortran/fortran-08-functions"
  ],
  "prerequisites": [
    "Fortran-07: Character Strings"
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

# FORTRAN-08-FUNCTIONS: Functions

## Introduction

Write and call functions with intent. By the end of this lesson you will be able to: Write functions; Use intent(in) arguments; Return values properly; Call intrinsic functions.

## Key Concepts

### 1. Write functions

Target: Write functions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```fortran
program use_f
  implicit none
  print *, add(2, 3)
contains
  integer function add(a, b)
    integer, intent(in) :: a, b
    add = a + b
  end function add
end program use_f
```
### 2. Use intent(in) arguments

Target: Use intent(in) arguments. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```fortran
real function area(r)
  real, intent(in) :: r
  real, parameter :: pi = 3.14159
  area = pi * r * r
end function area
```
### 3. Return values properly

Target: Return values properly. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```fortran
integer function fact(n)
  integer, intent(in) :: n
  integer :: i
  fact = 1
  do i = 2, n
    fact = fact * i
  end do
end function fact
```
### 4. Call intrinsic functions

Target: Call intrinsic functions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```fortran
print *, abs(-5), sqrt(16.0), nint(3.7)
```

## Practice Questions

1. What is the key idea behind "Functions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Functions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Functions"
1. "Provide advanced patterns and performance considerations for Functions"

## Key Takeaways

- Master the core ideas of Functions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
