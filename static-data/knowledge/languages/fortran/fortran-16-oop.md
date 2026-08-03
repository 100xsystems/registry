---
{
  "title": "Object-Oriented Fortran",
  "description": "Type-bound procedures and inheritance.",
  "type": "lesson",
  "order": 16,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Bind procedures to types",
    "Use inheritance",
    "Write generic interfaces",
    "Use class polymorphism"
  ],
  "knowledge_refs": [
    "fortran/fortran-16-oop"
  ],
  "prerequisites": [
    "Fortran-15: Pointers"
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

# FORTRAN-16-OOP: Object-Oriented Fortran

## Introduction

Type-bound procedures and inheritance. By the end of this lesson you will be able to: Bind procedures to types; Use inheritance; Write generic interfaces; Use class polymorphism.

## Key Concepts

### 1. Bind procedures to types

Target: Bind procedures to types. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```fortran
type :: shape
  real :: area
contains
  procedure :: compute => shape_compute
end type shape
```
### 2. Use inheritance

Target: Use inheritance. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```fortran
type, extends(shape) :: circle
  real :: radius
end type circle
```
### 3. Write generic interfaces

Target: Write generic interfaces. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```fortran
interface area
  module procedure area_circle, area_square
end interface
```
### 4. Use class polymorphism

Target: Use class polymorphism. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```fortran
class(shape), allocatable :: s
allocate(circle :: s)
```

## Practice Questions

1. What is the key idea behind "Object-Oriented Fortran"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Object-Oriented Fortran with analogies and real-world examples"
1. "Show me common mistakes beginners make with Object-Oriented Fortran"
1. "Provide advanced patterns and performance considerations for Object-Oriented Fortran"

## Key Takeaways

- Master the core ideas of Object-Oriented Fortran through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
