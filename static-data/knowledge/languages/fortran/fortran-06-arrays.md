---
{
  "title": "Arrays",
  "description": "Array declaration, slicing, and array operations.",
  "type": "lesson",
  "order": 6,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Declare 1-D and 2-D arrays",
    "Slice array sections",
    "Use array constructors",
    "Apply whole-array operations"
  ],
  "knowledge_refs": [
    "fortran/fortran-06-arrays"
  ],
  "prerequisites": [
    "Fortran-05: Loops"
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

# FORTRAN-06-ARRAYS: Arrays

## Introduction

Array declaration, slicing, and array operations. By the end of this lesson you will be able to: Declare 1-D and 2-D arrays; Slice array sections; Use array constructors; Apply whole-array operations.

## Key Concepts

### 1. Declare 1-D and 2-D arrays

Target: Declare 1-D and 2-D arrays. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```fortran
program arr
  implicit none
  integer, dimension(5) :: v
  v = (/ 1, 2, 3, 4, 5 /)
  print *, v
end program arr
```
### 2. Slice array sections

Target: Slice array sections. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```fortran
real, dimension(3, 3) :: m
m = 0.0
```
### 3. Use array constructors

Target: Use array constructors. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```fortran
integer :: a(10)
a(1:5) = 1
a(6:10) = 2
```
### 4. Apply whole-array operations

Target: Apply whole-array operations. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```fortran
print *, sum(v), maxval(v), minval(v)
```

## Practice Questions

1. What is the key idea behind "Arrays"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Arrays with analogies and real-world examples"
1. "Show me common mistakes beginners make with Arrays"
1. "Provide advanced patterns and performance considerations for Arrays"

## Key Takeaways

- Master the core ideas of Arrays through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
