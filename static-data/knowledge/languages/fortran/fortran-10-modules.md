---
{
  "title": "Modules",
  "description": "Module encapsulation and interfaces.",
  "type": "lesson",
  "order": 10,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write modules",
    "Use public/private access",
    "Import with use",
    "Share constants"
  ],
  "knowledge_refs": [
    "fortran/fortran-10-modules"
  ],
  "prerequisites": [
    "Fortran-09: Subroutines"
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

# FORTRAN-10-MODULES: Modules

## Introduction

Module encapsulation and interfaces. By the end of this lesson you will be able to: Write modules; Use public/private access; Import with use; Share constants.

## Key Concepts

### 1. Write modules

Target: Write modules. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```fortran
module math_utils
  implicit none
  real, parameter :: pi = 3.14159
contains
  real function area(r)
    real, intent(in) :: r
    area = pi * r * r
  end function area
end module math_utils

program main
  use math_utils
  implicit none
  print *, area(2.0)
end program main
```
### 2. Use public/private access

Target: Use public/private access. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```fortran
module config
  implicit none
  integer, parameter :: max_size = 1000
  private
  public :: max_size
end module config
```
### 3. Import with use

Target: Import with use. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```fortran
module types
  implicit none
  type :: point
    real :: x, y
  end type point
end module types
```
### 4. Share constants

Target: Share constants. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```fortran
use math_utils, only: pi
```

## Practice Questions

1. What is the key idea behind "Modules"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Modules with analogies and real-world examples"
1. "Show me common mistakes beginners make with Modules"
1. "Provide advanced patterns and performance considerations for Modules"

## Key Takeaways

- Master the core ideas of Modules through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
