---
{
  "title": "Derived Types",
  "description": "Structures and user-defined data.",
  "type": "lesson",
  "order": 11,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define derived types",
    "Access components",
    "Initialize derived values",
    "Pass derived types to procedures"
  ],
  "knowledge_refs": [
    "fortran/fortran-11-derived-types"
  ],
  "prerequisites": [
    "Fortran-10: Modules"
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

# FORTRAN-11-DERIVED-TYPES: Derived Types

## Introduction

Structures and user-defined data. By the end of this lesson you will be able to: Define derived types; Access components; Initialize derived values; Pass derived types to procedures.

## Key Concepts

### 1. Define derived types

Target: Define derived types. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```fortran
type :: person
  character(len=30) :: name
  integer :: age
end type person
```
### 2. Access components

Target: Access components. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```fortran
type(person) :: p
p%name = "Ada"
p%age = 36
```
### 3. Initialize derived values

Target: Initialize derived values. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```fortran
type(point) :: origin = point(0.0, 0.0)
```
### 4. Pass derived types to procedures

Target: Pass derived types to procedures. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```fortran
subroutine show(p)
  type(person), intent(in) :: p
  print *, p%name, p%age
end subroutine show
```

## Practice Questions

1. What is the key idea behind "Derived Types"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Derived Types with analogies and real-world examples"
1. "Show me common mistakes beginners make with Derived Types"
1. "Provide advanced patterns and performance considerations for Derived Types"

## Key Takeaways

- Master the core ideas of Derived Types through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
