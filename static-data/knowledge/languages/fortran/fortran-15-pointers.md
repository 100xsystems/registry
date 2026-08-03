---
{
  "title": "Pointers",
  "description": "Pointer association and targets.",
  "type": "lesson",
  "order": 15,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Declare pointers",
    "Associate with targets",
    "Use pointer arrays",
    "Nullify pointers"
  ],
  "knowledge_refs": [
    "fortran/fortran-15-pointers"
  ],
  "prerequisites": [
    "Fortran-14: Dynamic Allocation"
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

# FORTRAN-15-POINTERS: Pointers

## Introduction

Pointer association and targets. By the end of this lesson you will be able to: Declare pointers; Associate with targets; Use pointer arrays; Nullify pointers.

## Key Concepts

### 1. Declare pointers

Target: Declare pointers. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```fortran
integer, target :: x
integer, pointer :: p
p => x
```
### 2. Associate with targets

Target: Associate with targets. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```fortran
p => null()
if (associated(p)) then
  print *, "associated"
end if
```
### 3. Use pointer arrays

Target: Use pointer arrays. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```fortran
integer, pointer :: row(:)
row => matrix(:, 2)
```
### 4. Nullify pointers

Target: Nullify pointers. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```fortran
real, pointer :: list(:)
allocate(list(10))
```

## Practice Questions

1. What is the key idea behind "Pointers"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Pointers with analogies and real-world examples"
1. "Show me common mistakes beginners make with Pointers"
1. "Provide advanced patterns and performance considerations for Pointers"

## Key Takeaways

- Master the core ideas of Pointers through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
