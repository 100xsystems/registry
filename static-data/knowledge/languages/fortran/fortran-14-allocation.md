---
{
  "title": "Dynamic Allocation",
  "description": "allocatable arrays and pointers.",
  "type": "lesson",
  "order": 14,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Declare allocatable arrays",
    "Allocate and deallocate",
    "Use move_alloc",
    "Check allocation status"
  ],
  "knowledge_refs": [
    "fortran/fortran-14-allocation"
  ],
  "prerequisites": [
    "Fortran-13: Intrinsic Functions"
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

# FORTRAN-14-ALLOCATION: Dynamic Allocation

## Introduction

allocatable arrays and pointers. By the end of this lesson you will be able to: Declare allocatable arrays; Allocate and deallocate; Use move_alloc; Check allocation status.

## Key Concepts

### 1. Declare allocatable arrays

Target: Declare allocatable arrays. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```fortran
integer, allocatable :: a(:)
allocate(a(10))
a = 0
deallocate(a)
```
### 2. Allocate and deallocate

Target: Allocate and deallocate. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```fortran
integer, allocatable :: m(:,:)
allocate(m(3, 3))
```
### 3. Use move_alloc

Target: Use move_alloc. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```fortran
if (allocated(a)) then
  deallocate(a)
end if
```
### 4. Check allocation status

Target: Check allocation status. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```fortran
allocate(a(100))
allocate(b(200))
b = a
call move_alloc(b, a)
```

## Practice Questions

1. What is the key idea behind "Dynamic Allocation"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Dynamic Allocation with analogies and real-world examples"
1. "Show me common mistakes beginners make with Dynamic Allocation"
1. "Provide advanced patterns and performance considerations for Dynamic Allocation"

## Key Takeaways

- Master the core ideas of Dynamic Allocation through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
